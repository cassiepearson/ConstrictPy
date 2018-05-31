import glob
import os
import os.path
import errno  # Used to check for race condition in ensureDir
import pandas as pd
import rpy2.robjects as robjects
from rpy2.robjects import r, pandas2ri
import logging
from time import strftime
from shutil import make_archive, copytree, copyfile

def clearDir(dir_path):  # remove all files from a directory
    filelist = glob.glob(os.path.join(dir_path, "*.*"))
    for f in filelist:
        os.remove(f)


def ensureDir(dir_path):  # create the directory if it doesn't exist
    try:
        os.makedirs(dir_path)
    except OSError as e:  # why does the OS complain about making the dir?
        if e.errno != errno.EEXIST:  # is it just because the dir exists? No?
            raise  # OK, then tell me about it.

def compressDir(target, root_dir):
    """
    Takes a directory and returns the compressed result as a file path
    """
    make_archive(target, 'zip', root_dir)

def moveToUploads(file):
    uploads_dir = os.path.join("app", "uploads")
    ensureDir(uploads_dir)
    clearDir(uploads_dir)
    filepath = os.path.join(file)
    copyfile(filepath, os.path.join(uploads_dir, "archive.zip"))

def datasetToCSV(output_dir, dataset):
    """
    Takes an output directory and dataset as arguments, and puts all the
    stats in that dataset into labelled .csv files in output_dir.
    """
    export_data = dataset.getStats()
    for label in export_data:
        file_name = "%s.%s" % (label, "csv")
        file_path = os.path.join(output_dir, file_name)
        export_data[label].to_csv(file_path)


def datasetToRdata(output_dir, dataset):
    """
    Takes an output directory and dataset as arguments, converts the stats
    in that dataset to R dataframes, then saves the R dataframes as labelled
    R data objects in output_dir.
    """
    pandas2ri.activate()
    export_data = dataset.getStats()
    for label in export_data:
        file_name = "%s.%s" % (label, "Rdata")
        file_path = os.path.join(output_dir, file_name)
        r_df = pandas2ri.py2ri(export_data[label])
        robjects.r.assign(label, r_df)
        robjects.r("save(%s, file='%s')" % (label, file_path))


def batchSaveToFile(output_dir, datasets, filetype, clear=False):
    """
    Save lots of dataframes to files. This is probably the function to call
    in main(), instead of iterating over datasetToX.

    Keyword arguments:
        output_dir - output directory
        datasets - list of Dataset objects
        filetype - string describing desired output
        clear - should output_dir be cleared? default False.
    """

    if clear is True:
        clearDir(output_dir)  # clear before writing new files

    logging.info(f"Saving dataframes to {output_dir} as type {filetype}...")

    filetype = str.lower(str(filetype))  # quick and dirty normalization

    if filetype == "csv":
        for dataset in datasets:
            logging.info(f"\tSaving dataframes from {dataset.name}...")
            datasetToCSV(output_dir, dataset)
    elif filetype == "r" or filetype == "rdata":
        for dataset in datasets:
            logging.info(f"\tSaving dataframes from {dataset.name}...")
            datasetToRdata(output_dir, dataset)
    else:
        logging.warning(f"\t{filetype} is not an acceptable filetype (csv, r, rdata)")

    logging.info("{} batch save complete".format(filetype))
