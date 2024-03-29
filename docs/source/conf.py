# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


import sys
import os
# Make sure we import sympy from git
sys.path.insert(0, os.path.abspath('../../src/'))

import geo3py
import sphinx_rtd_theme

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'geo3py'
copyright = '2022, Kaare G. S. Hansen, s214282 - DTU'
author = 'Kaare G. S. Hansen'
version = geo3py.__version__


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', #'sphinx.ext.linkcode',
              'sphinx.ext.mathjax',
              'sphinx.ext.graphviz', 'matplotlib.sphinxext.plot_directive',
              'sphinx.ext.intersphinx',
              'sphinx_copybutton',
              'nbsphinx',
              'sphinx_charts.charts',
              'jupyter_sphinx',
              'sphinx_rtd_theme',
              'sphinx_git',
              ]


templates_path = ['_templates']
exclude_patterns = []


# -- Notebook configuration --------------------------------------------------
#nbsphinx_execute = 'always'




# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_js_files = ["https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js"]

# html_theme = 'alabaster'
# html_theme = 'classic'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = "geo3py-logo-white.svg"
html_theme_options = {
    'logo_only': True,
    'display_version': True,
    #'use_download_button': True,
    'prev_next_buttons_location': 'both',
    'style_external_links': True,

}

html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "KaareH", # Username
    "github_repo": "GEO3Py", # Repo name
    "github_version": "main", # Version
    "conf_py_path": "/docs/source/", # Path in the checkout to the docs root
}

# -- Options for LaTeX output -------------------------------------------------

latex_logo = "geo3py-logo.png"
latex_elements = {
    'extrapackages': r'\usepackage{mathrsfs}',
    'papersize': 'a4paper'
}

