# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


import sphinx_rtd_theme

project = 'pythonatomistics'
copyright = '2023, Yavar'
author = 'Yavar'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.extlinks',
              'sphinx.ext.viewcode',
              'sphinx.ext.napoleon',
              'sphinx.ext.mathjax',
              'sphinx.ext.intersphinx']


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

#mathjax_path = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js'


default_role = 'math'

mathjax3_config = {
    'tex': {
        'macros': {
            'br': '{\\mathbf r}',
            'bk': '{\\mathbf k}',
            'bG': '{\\mathbf G}'}}}
