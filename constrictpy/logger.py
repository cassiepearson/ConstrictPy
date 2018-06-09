import logging
import pkg_resources
from time import strftime

loggers = {}


def getLogger(name, logmode, clear=True):

    global loggers

    if loggers.get(name):
        return loggers.get(name)
    else:
        # determine log level from input
        logmode = logmode.lower()
        if logmode == "debug":
            loglevel = logging.DEBUG
        elif logmode == "warning":
            loglevel = logging.WARNING
        else:
            loglevel = logging.INFO

        # set the log filename
        ts = strftime("%Y-%m-%d-%H.%M.%S")
        logfile = pkg_resources.resource_filename("logs", "logs/{}.log".format(ts))

        # clear the log file
        if clear is True:
            with open(logfile, "w") as f:
                f.write("")
                f.close()

        # Create Logger object
        logFormatter = logging.Formatter("%(levelname)s:%(module)s: %(message)s")
        rootLogger = logging.getLogger(name)
        rootLogger.setLevel(loglevel)

        fileHandler = logging.FileHandler(logfile)
        fileHandler.setFormatter(logFormatter)
        fileHandler.setLevel(loglevel)
        rootLogger.addHandler(fileHandler)

        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(logFormatter)
        consoleHandler.setLevel(loglevel)
        rootLogger.addHandler(consoleHandler)

        return rootLogger
