import os
import sys
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def requires():
    r = ['requests>=1.1.0']
    if sys.version_info < (2, 7):
        r.append('ordereddict')
    return r

setup(
    name="solar",
    version="0.4.011.mylanium",
    author="Alexander Koval",
    author_email="kovalidis@gmail.com",
    description=("A library to use solr in python projects."),
    license="BSD",
    keywords="solr solar pysolr",
    url="https://github.com/anti-social/solar",
    packages=find_packages(exclude=["tests.*", "tests"]),
    long_description=read('README.rst'),
    install_requires=requires(),
    extras_require={
        'tomcat': [
            'lxml',
            'cssselect',
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
