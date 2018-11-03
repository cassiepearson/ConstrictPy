from flask import current_app
from app import db
import redis
import rq

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    hash = db.Column(db.String(32), unique=True)
    uploaded = db.Column(db.DateTime())
    source = db.Column(db.String(200))
    methods = db.Column(db.Text)
    result_dir = db.Column(db.String(200), unique=True)
    result_zip = db.Column(db.String(200), unique=True)
    complete = db.Column(db.Boolean)
    tasks = db.relationship('Task', backref='job', lazy='dynamic')

    def launch_task(self, name, *args, **kwargs):
        rq_job = current_app.task_queue.enqueue("app.tasks." + name, self,
                                                *args, **kwargs, timeout=360)
        task = Task(id=rq_job.get_id(), name=name, job=self)
        db.session.add(task)
        return task

    def get_tasks_in_progress(self):
        return Task.query.filter_by(job=self, complete=False).all()


    def __repr__(self):
        return "<Name {}>".format(self.name)


class Task(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(128), index=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    complete = db.Column(db.Boolean, default=False)

    def get_rq_job(self):
        try:
            rq_job = rq.job.Job.fetch(self.id, connection=current_app.redis)
        except (redis.exceptions.RedisError, rq.exceptions.NoSuchJobEror):
            return None
        return rq_job
