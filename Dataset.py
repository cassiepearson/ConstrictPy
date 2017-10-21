import pandas as pd


class Dataset:

    def __init__(self, name, source):
        """ Initialize Dataset


        Keyword arguments:
        name -- String describing the Dataset
        source -- DataFrame from the prepared data file
        """
        self.name = name
        self.source = source
        self.stats = {}

    def addStats(self, label, frame):
        """ Add DataFrame of statistics to self.stats

        Keyword arguments:
        label -- not String, just simple name for data computed
        frame -- DataFrame of computed statistics to be added
        """
        self.stats[label] = frame

    def printStats(self):
        """ Print all statistics with labels """
        for label in self.stats:
            print label
            print self.stats[label]

    def statsToCSV(self, output_dir):
        """ Save all statistics as CSV files in the format:
                name_of_dataframe_name_of_dataset


        Keyword arguments:
        output_dir -- String of the data output directory
        """
        for label in self.stats:
            filename = output_dir + label + "_" + self.name
            self.stats[label].to_csv(filename)
