# ConstrictPy

![](assets/logo.png)

Original Philosophy:
  For all analysis, the entire table provided is used. This will need to be
  parsed down to the desired values. All math is done pairwise by columns. Data
  is reformatted manually before analysis to allow for clean labels during import.
  This program was originally written with a tool framework but then changed to
  a more basic framework to allow for efficient analysis. The approach for the
  code framework is "quick and dirty" with accurate analysis. For more flexible
  functionality, the program could be converted to a general tool. Of the desired
  provided analysis list, all analysis that has low statistical value or is
  not applicable is omitted.

Current Philosophy:
  This project has expanded to make the set of methods original implemented here more
  efficient, accurate, and usable. From the original program, we have expanded the
  python tool to include more methods and a much more robust object-oriented framework.
  Additionally, now the python portion is a tool wrapper for the analysis in R. The
  analysis in R has become a project and package of its own. The project is still a
  work in progress and is expanding rapidly. Current plans involve the full project
  being available in July 2018.

## Getting Started

Follow these instructions to install the in-development version of ConstrictPy.

### Prerequisites

+ A working Python environment (Python 3.6.x)
+ pip
+ R

*Recommendation*: Use your preferred virtual environment tool to create an
environment for developing this application.

*Double Secret Recommendation*: Use `Anaconda` as your python environment
manager, and you can automatically use R as `.../anaconda/envs/$ENV/bin/R`.

### Installing

(Optional: activate your Python virtual environment.)

Clone the project repository

`git clone https://github.com/ahoetker/ConstrictPy.git`

cd to the project directory

`cd ConstrictPy`

Install the project dependencies with pip

`pip install -r requirements.txt`

For package development, install the python package in development mode

`pip install -e .`

## Running Tests

There are currently *no* tests for ConstrictPy, unit or otherwise.

## Deployment

** Not recommended in this version **

If the package is installed in development mode, remove it

`pip uninstall constrictpy`

install the package using pip

`pip install .`

## Versioning

There is currently *no* versioning system for ConstrictPy, we just use
different branches.

## Authors

Author | Contact | Github
--- | --- | ---
Christopher Negrich | cnegrich@gmail.com | [cnegrich](https://github.com/cnegrich)
Andrew Hoetker | ahoetker@me.com | [ahoetker](https://github.com/ahoetker)
Courtney Johnson | cejohn32@asu.edu | [cejohn32](https://github.com/cejohn32)

## License

There is currently *no* license for ConstrictPy, but **no stealing**.
