# -*- coding: utf-8 -*-

project = 'Recipes'
copyright = '2019, P Adhia'
author = 'P Adhia'

version = ''
release = ''

extensions = [
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
default_role = 'index'

html_theme = "alabaster"
html_theme_options = {
    'show_powered_by': False,
}
html_sidebars = {
    '**': ['about.html', 'navigation.html', 'relations.html', 'searchbox.html']
}

html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = True
