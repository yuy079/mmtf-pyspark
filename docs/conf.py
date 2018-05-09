#/!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# MMTF-PySpark documentation build configuration file, created by
# sphinx-quickstart on Tue May  8 00:03:06 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.7.4'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'numpydoc.numpydoc',
    'nbsphinx',
]

try:
    import numpydoc
except ImportError:
    msg = "Error: numpydoc must be installed before generating this documentation"
    raise ImportError(msg)

try:
    import sphinx_bootstrap_theme
except ImportError:
    msg = "Error: sphinx_bootstrap_thememust be installed before generating this documentation"
    raise ImportError(msg)

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'MMTF-PySpark'
copyright = '2018, UC San Diego'
author = ''

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.2.4'
# The full version, including alpha/beta/rc tags.
release = version

# Date format
today_fmt = '%B %d, %Y'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
autosummary_generate = True
autodoc_docstring_signature = True

autodoc_mock_imports = [
    'pyspark', 'pyspark.sql', 'pyspark.ml.linalg', 'pyspark.ml.regression',
]

nbsphinx_epilog = """

.. raw:: html

   <div class="btn-container">
       <a class="btn btn-download" role="button" href="{{ env.doc2path(env.docname, base='../../../') }}" download>Download Notebook</a>
   </div>

"""



# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_logo = '_static/mmTF-dark-blue.png'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    # Tab name for entire site.
    'navbar_site_name': 'Home',
    # A list of tuples containing pages or urls to link to.
    'navbar_links': [
        ('Home', 'index'),
        ('Examples', 'demo'),
        ('Documentation', 'contents'),
    ],
    # Render the next and previous page links in navbar. 
    'navbar_sidebarrel': True,
    # Render the current pages TOC in the navbar.)
    'navbar_pagenav': True,
    # Global TOC depth for "site" navbar tab.
    'globaltoc_depth': 2,
    # Fix navigation bar to top of page?
    'navbar_fixed_top': True,
    # Location of link to source.
    'source_link_position': "footer",
    # Bootswatch (http://bootswatch.com/) theme.
    'bootswatch_theme': "paper",
    # Choose Bootstrap version.
    'bootstrap_version': "3",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

def setup(app):
    app.add_stylesheet("custom.css")
    app.add_stylesheet("_static/custom.css")

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'MMTF-PySparkdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'MMTF-PySpark.tex', 'MMTF-PySpark Documentation',
     'not me', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'mmtf-pyspark', 'MMTF-PySpark Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'MMTF-PySpark', 'MMTF-PySpark Documentation',
     author, 'MMTF-PySpark', 'One line description of project.',
     'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/3/': None}
