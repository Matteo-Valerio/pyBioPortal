# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath(".."))


project = 'pybioportal'
copyright = '2023, Matteo Valerio'
author = 'Matteo Valerio'
version = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "nbsphinx"]
#add_module_names = False

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

html_css_files = [
    'css/custom_template.css',
]

html_theme_options = {
    #"icon_links_label": "Quick Links",
    "logo": {
        "text": "pybioportal",
        "image_light": "_static/pbp_light_logo.png",
        "image_dark": "_static/pbp_dark_logo.png",
    },
    "favicons": [
      {
         "rel": "icon",
         "sizes": "16x16",
         "href": "pbp_dark_logo.png",
      },
      {
         "rel": "icon",
         "sizes": "32x32",
         "href": "pbp_dark_logo.png",
      },
      {
         "rel": "apple-touch-icon",
         "sizes": "180x180",
         "href": "pbp_dark_logo.png",
         "color": "#000000",
      },
   ],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/Matteo-Valerio/pyBioPortal",
            "icon": "fab fa-github-square",
            "type": "fontawesome",
        }
        # {
        #     "name": "Twitter",
        #     "url": "https://twitter.com/<your-handle>",
        #     "icon": "fab fa-twitter-square",
        #     # The default for `type` is `fontawesome` so it is not actually required in any of the above examples as it is shown here
        # },
    ],
    "show_prev_next": True,
    "external_links": [
      {"name": "cBioPortal", "url": "https://www.cbioportal.org/"},
      {"name": "cBioPortal API", "url": "https://www.cbioportal.org/api/swagger-ui/index.html"}
    ],
    "footer_start": ["copyright"],
    "footer_center": ["sphinx-version"],
    "footer_end": ["theme-version"]
}


