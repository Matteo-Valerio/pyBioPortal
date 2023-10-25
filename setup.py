from setuptools import setup, find_packages

# Metadati del package
name = "pyBioGate"
version = "0.1.0"
description = "Un package per l'accesso alle API di cBioPortal."
author = "Matteo Valerio"
author_email = "tua@email.com"
url = "https://github.com/tuoaccount/pyBioGate"
license = "MIT"
keywords = "cBioPortal, API, bioinformatics"

# Dipendenze del package
install_requires = [
    # Specifica le dipendenze qui, ad esempio:
    "requests>=2.29.0",
    "pandas>=1.5.3"
]

# Trova automaticamente tutti i moduli e i pacchetti
packages = find_packages()

setup(
    name=name,
    version=version,
    description=description,
    author=author,
    author_email=author_email,
    url=url,
    license=license,
    keywords=keywords,
    install_requires=install_requires,
    packages=packages,
    entry_points={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
