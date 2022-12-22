# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'geo3py'
copyright = '2022, Kaare G. S. Hansen, s214282 - DTU'
author = 'Kaare G. S. Hansen'

import sys
import os

# Make sure we import sympy from git
sys.path.insert(0, os.path.abspath('../../src'))

import geo3py
#import geo3py.surface


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', #'sphinx.ext.linkcode',
              'sphinx.ext.mathjax',
              'sphinx.ext.graphviz', 'matplotlib.sphinxext.plot_directive',
              'sphinx.ext.intersphinx',
              ]



templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
