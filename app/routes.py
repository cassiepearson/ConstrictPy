import os
from flask import render_template, flash, redirect, url_for, send_from_directory, current_app
from werkzeug.utils import secure_filename
from shutil import copyfile
from app import app
from app.forms import MethodSelectionForm, DataUploadForm
from constrictpy.analyze import doConstrictPy
from constrictpy.io_handling import ensureDir, clearDir


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = DataUploadForm()
    if form.validate_on_submit():
        f = form.datafile.data
        filename = secure_filename(f.filename)
        uploads_dir = os.path.join(app.instance_path, 'uploads')
        ensureDir(uploads_dir)
        clearDir(uploads_dir)
        f.save(os.path.join(app.instance_path, 'uploads', filename))
        flash("{} uploaded successfully!".format(filename))
        return redirect(url_for('selectmethods'))
    return render_template('upload.html', form=form)

@app.route('/selectmethods', methods=['GET', 'POST'])
def selectmethods():
    form = MethodSelectionForm()
    if form.validate_on_submit():
        data = form.data.copy()
        del(data['csrf_token'])
        del(data['submit'])
        datafile = os.path.join(app.instance_path, 'uploads', "Prepared_Data.xlsx")
        doConstrictPy(datafile, data)
        return redirect(url_for('analysis'))
    return render_template('selectmethods.html', title='Select Methods', form=form)

@app.route('/analysis')
def analysis():
    return render_template('analysis.html', title='Analysis')

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, filename=filename)