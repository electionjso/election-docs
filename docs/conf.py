import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'JSO Documentation'
author = 'Rama Shanker'
release = '2026'

extensions = ['myst_parser']  # To use Markdown

templates_path = ['_templates']
html_static_path = ['_static']

# The master toctree document.
master_doc = 'index'

html_theme = 'sphinx_rtd_theme'
html_logo = '_static/jso.jpg'
html_theme_options = {
    "logo_only": True,
    "display_version": False
}

# Custom sidebar
html_sidebars = {
    '**': ['custom-sidebar.html']
}

# Load custom CSS
html_css_files = [
    'custom.css',
]