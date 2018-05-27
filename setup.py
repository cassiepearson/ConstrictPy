from setuptools import setup, find_packages

setup(
    name="constrictpy",
    version="0.1",
    description="Wrap R for microbiome analysis.",
    url="https://github.com/ahoetker/ConstrictPy",
    author="Chris Negrich",
    author_email="foo@placeholder.net",
    install_requires=[
        "numpy",
        "scipy",
        "pandas",
        "xlrd",
        "networkx",
        "matplotlib",
        "rpy2",
    ],
    entry_points={
        "console_scripts": ["test-constrictpy=constrictpy.command_line:main"]
    },
    packages=find_packages(),
    zip_safe=False,
)
