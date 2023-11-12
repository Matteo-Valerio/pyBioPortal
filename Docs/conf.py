# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = 'pyBioGate'
copyright = '2023, Matteo Valerio'
author = 'Matteo Valerio'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc"]
add_module_names = False

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

html_theme_options = {
    #"icon_links_label": "Quick Links",
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/<your-org>/<your-repo>",
            "icon": "fab fa-github-square",
            "type": "fontawesome",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/<your-handle>",
            "icon": "fab fa-twitter-square",
            # The default for `type` is `fontawesome` so it is not actually required in any of the above examples as it is shown here
        },
    ]
}
