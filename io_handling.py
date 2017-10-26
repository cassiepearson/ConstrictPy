import glob
import os, os.path
import errno # Used to check for race condition in ensureDir


def clearDir(dir_path): # remove all files from a directory
    filelist = glob.glob(os.path.join(dir_path, "*.*"))
    for f in filelist:
        os.remove(f)
        
        
def ensureDir(dir_path): # create the directory if it doesn't exist
    try:
        os.makedirs(dir_path)
    except OSError as e: # why does the OS complain about making the dir? 
        if e.errno != errno.EEXIST: # is it just because the dir exists? No?
            raise # OK, then tell me about it.
            
            
def writeOutToCSV(output_dir, dataset):
    """
    Takes an output directory and dataset as arguments, and puts all the
    stats in that dataset into labelled .csv files in output_dir. 
    """
    export_data = dataset.getStats()
    for label in export_data:
        file_name = "%s.%s" % (label, 'csv')
        file_path = os.path.join(output_dir, file_name)
        export_data[label].to_csv(file_path)
