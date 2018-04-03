from setuptools import setup, find_packages

setup(name='constrictpy',
      version='0.1',
      description='Wrap R for microbiome analysis.',
      url='https://github.com/ahoetker/ConstrictPy',
      author='Chris Negrich',
      author_email='foo@placeholder.net',
      install_requires=[
          'numpy==1.13.3',
          'scipy==0.19.1',
          'pandas==0.20.3',
          'xlrd==1.1.0',
          'networkx==2.0',
          'matplotlib==2.1.0',
          'rpy2==2.9.0',
      ],
      packages=find_packages(),
      zip_safe=False)
