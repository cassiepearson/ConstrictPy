from app import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    hash = db.Column(db.String(32), unique=True)
    uploaded = db.Column(db.DateTime())
    source = db.Column(db.String(200), unique=True)
    methods = db.Column(db.Text)
    completed = db.Column(db.Boolean)
    result_dir = db.Column(db.String(200), unique=True)
    result_zip = db.Column(db.String(200), unique=True)

    def __repr__(self):
        return "<Name {}>".format(self.name)
