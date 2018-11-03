import os
from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    send_from_directory,
    current_app,
    session,
)
from werkzeug.utils import secure_filename
from app import app, db
from app.models import Job
from app.forms import MethodSelectionForm, DataUploadForm, CombinedForm
from constrictpy.analyze import doConstrictPy, analyzeJob
from constrictpy.io_handling import ensureDir, clearDir
from time import time
from hashlib import md5
import os
import json
from datetime import datetime


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Home")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/newjob", methods=["GET", "POST"])
def newjob():
    form = CombinedForm()
    if form.validate_on_submit():
        data = form.data.copy()
        f = data.get("datafile")
        filename = secure_filename(f.filename)
        hash = md5((filename + str(time())).encode()).hexdigest()  # ugly
        uploads = app.config.get("UPLOAD_FOLDER")
        results = app.config.get("RESULTS_FOLDER")
        source_file = os.path.join(uploads, hash + filename)
        f.save(source_file)
        flash("{} uploaded successfully!".format(filename))
        methods = data.copy()
        del(methods["datafile"])
        del(methods["csrf_token"])
        del(methods["submit"])
        J = Job(
            name=data.get("job_name"),
            hash=hash,
            uploaded=datetime.now(),
            source=os.path.abspath(source_file),
            methods=json.dumps(methods),
            result_dir=os.path.join(results, hash),
            result_zip=os.path.join(results, hash, "archive.zip"),
            complete=False,
        )
        db.session.add(J)
        J.launch_task("analyze_job")
        db.session.commit()
        return redirect(url_for("upload_success"))
    return render_template("newjob.html", title="New Job", form=form)


@app.route("/upload_success")
def upload_success():
    return render_template("upload_success.html", title="Success")


@app.route("/jobs")
def jobs():
    joblist = Job.query.all()
    completed = []
    pending = []
    for job in joblist:
        if os.path.exists(os.path.abspath(job.result_zip)):
            completed.append(job)
        else:
            pending.append(job)
    return render_template("jobs.html", title="Jobs", completed=completed, pending=pending)


@app.route("/results/<path:filename>", methods=["GET", "POST"])
def download(filename):
    uploads = os.path.join(current_app.root_path, app.config["UPLOAD_FOLDER"])
    return send_from_directory(directory=uploads, filename=filename)
