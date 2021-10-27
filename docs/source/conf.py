# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'iThesis'
copyright = '2021, MHESI'
author = 'Sopanawit Pi'


release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

latex_engine = 'xelatex'
latex_use_xindy = False
latex_elements = {
    # 'pointsize': '10pt',
    'papersize': 'a4paper',
    'preamble': '\\usepackage[UTF8]{ctex}\n',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
# latex_documents = [
#   ('index', 'phpMyAdmin.tex', u'phpMyAdmin Documentation',
#    u'The phpMyAdmin devel team', 'manual'),
# ]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
