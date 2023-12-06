from setuptools import setup, find_packages
import os
import sys


with open('LICENSE.txt', 'r', encoding='utf-8') as file:
    license_text = file.read()

name = "pybioportal"
version = "1.0.0"
description = "A Python package to easily retrieve data from cBioPortal."
author = "Matteo Valerio"
url = "https://github.com/Matteo-Valerio/pyBioPortal"
doc_url = "https://pybioportal.readthedocs.io"
license = license_text
keywords = "cBioPortal, API, bioinformatics"

install_requires = [
    "requests>=2.0.0",
    "pandas>=1.0.0",
    "numpy>=1.23.0"
]

packages = ["pybioportal"]

if __name__ == "__main__":

    # output folder for package distribution file tar.gz and whl
    version_folder = f"dist/v{version}/pypi"
    
    # create output folder if not exists
    if not os.path.exists(version_folder):
        os.makedirs(version_folder)

    # check if command is python setup.py
    if len(sys.argv) == 1 and sys.argv[0] == "setup.py":
        # adding option for building
        sys.argv += ["sdist", "--dist-dir", version_folder]
        sys.argv += ["bdist_wheel", "--dist-dir", version_folder]

setup(
    name=name,
    version=version,
    description=description,
    author=author,
    #author_email=author_email,
    url=url,
    project_urls={
        "Documentation": doc_url
    },
    license=license,
    keywords=keywords,
    install_requires=install_requires,
    packages=packages,
    entry_points={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)


# Remove the build and pybioportal.egg-info directory after creating the packages
if os.path.exists("build"):
    if os.name == "nt":  # Check if running on Windows
        os.system(f"rmdir /s /q build")
    else:  # For Unix-like systems
        os.system(f"rm -rf build")

if os.path.exists("pybioportal.egg-info"):
    if os.name == "nt":  # Check if running on Windows
        os.system(f"rmdir /s /q pybioportal.egg-info")
    else:  # For Unix-like systems
        os.system(f"rm -rf pybioportal.egg-info")