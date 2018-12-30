# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#

# -- Project information -----------------------------------------------------
project = 'Recipes'
copyright = '2019, P Adhia'
author = 'P Adhia'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"

# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    'collapse_navigation': False,
    'display_version': False,
    'navigation_depth': 1,
}

# -- Options for manual page output ------------------------------------------
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = True
