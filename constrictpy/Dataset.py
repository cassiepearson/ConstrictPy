import pandas as pd  # Necessary to handle dataframes
from constrictpy.logger import getLogger

# define module-level logger
logger = getLogger(__name__, "info")


class Dataset:

    def __init__(self, name, source):
        """
        Initialize Dataset

        Keyword arguments:
        name -- String describing the Dataset
        source -- DataFrame from the prepared data file
        """
        self.name = name
        self.source = source
        self.stats = {"source": self.source}

    def addStats(self, label, frame):
        """
        Add DataFrame of statistics to self.stats

        Keyword arguments:
        label -- not String, just simple name for data computed
        frame -- DataFrame of computed statistics to be added
        """
        self.stats[label] = frame

    def logStats(self):
        """ Print all statistics with labels """
        for label in self.stats:
            logger.info(label)
            logger.info(self.stats[label])

    def statsToCSV(self, output_dir):
        """
        DEPRECATED IN FAVOR OF io_handling FUNCTION AND Dataset.getStats
        Save all statistics as CSV files in the format:
                name_of_dataframe_name_of_dataset

        Keyword arguments:
        output_dir -- String of the data output directory
        """
        for label in self.stats:
            # filename = f"{output_dir}{label}_{self.name}{'.csv'}"
            filename = "{0}{1}_{2}.csv".format(output_dir, label, self.name)
            self.stats[label].to_csv(filename)

    def getStats(self):
        """
        Return dict of DataFrames in self.stats with _sheetname added

        This is mainly intended to feed to a file output function
        """
        stats_out = {}
        for label in self.stats:
            # full_name = f"{label}_{self.name}"
            full_name = "{0}_{1}".format(label, self.name)
            stats_out[full_name] = self.stats[label]
        return stats_out
