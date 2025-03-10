# -*- coding: utf-8 -*-
#
# CNP3 documentation build configuration file, created by
# sphinx-quickstart on Tue Sep  8 22:48:38 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('/Users/obo/Library/Python/2.7/site-packages/sphinxcontrib_mscgen-0.4-py2.7.egg/sphinxcontrib'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.#
extensions = ['sphinx.ext.todo', 'sphinx.ext.pngmath', 'sphinxcontrib.mscgen','sphinx.ext.graphviz']
#, 'sphinx.ext.numfig'] 
#'rst2pdf.pdfbuilder', 'rst2pdf.pdfmath', 'sphinx.ext.pngmath' ]
#, 
# 'sphinx.ext.autodoc','rst2pdf.pdfbuilder']
#extensions = ['sphinx.ext.pngmath', 'rst2pdf.pdfbuilder']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Computer networking : Principles, Protocols and Practice'
copyright = u'2013 Olivier Bonaventure'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build']

# List of files that should not be automatically compiled by sphynx because they are included

exclude_patterns = [ '*#*',   # emacs backups
                     'MCQ/*']

# epilog add to all included files
#rst_epilog = """
#.. include:: links.rst
#"""


# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
#html_theme = 'sphinxdoc'
#html_theme = 'agogo'
html_theme = 'haiku'
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {stickysidebar=True}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Computer Networking : Principles, Protocols and Practice"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "Computer Networking : Principles, Protocols and Practice"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_use_modindex = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'CNP3doc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = 'a4'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '11pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'CNP3.tex', u'Computer Networking : Principles, Protocols and Practice',
   u'Olivier Bonaventure', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "cnp3.png"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True


# -- Options for PDF output --------------------------------------------------
# Grouping the document tree into PDF files. List of tuples # (source start file, target name, title, author, options). # # If there is more than one author, separate them with \\. # For example: r'Guido van Rossum\\Fred L. Drake, Jr., editor' #
# The options element is a dictionary that lets you override # this config per-document. # For example, # ('index', u'MyProject', u'My Project', u'Author Name',
# dict(pdf_compressed = True)) # would mean that specific document would be compressed # regardless of the global pdf_compressed setting.
#pdf_documents = [ ('index', u'MyProject', u'My Project', u'Author Name'),]
# A comma-separated list of custom stylesheets. Example: pdf_stylesheets = ['sphinx','kerning','a4']
# Create a compressed PDF # Use True/False or 1/0 # Example: compressed=True #pdf_compressed = False
# A colon-separated list of folders to search for fonts. Example: # pdf_font_path = ['/usr/share/fonts', '/usr/share/texmf-dist/fonts/']
# Language to be used for hyphenation support #pdf_language = "en_US"
# Mode for literal blocks wider than the frame. Can be # overflow, shrink or truncate
#pdf_fit_mode = "shrink"
# Section level that forces a break page. # For example: 1 means top-level sections start in a new page # 0 means disabled #pdf_break_level = 0
# When a section starts in a new page, force it to be 'even', 'odd', # or just use 'any' #pdf_breakside = 'any'
# Insert footnotes where they are defined instead of # at the end. #pdf_inline_footnotes = True
# verbosity level. 0 1 or 2 #pdf_verbosity = 0
# If false, no index is generated. #pdf_use_index = True
# If false, no modindex is generated. #pdf_use_modindex = True
# If false, no coverpage is generated. #pdf_use_coverpage = True
# Documents to append as an appendix to all manuals. #pdf_appendices = []
# Enable experimental feature to split table cells. Use it # if you get "DelayedTable too big" errors #pdf_splittables = False


# ----- pdf options for rst2pdf -----
#
#
#pdf_documents = [ 
#        ('index', project, project, u'Computer networking : Principles, Protocols and Practice', u'Computer networking : Principles, Protocols and Practice', u'Olivier Bonaventure'), 
#    ]
# A comma-separated list of custom stylesheets. Example:
#pdf_stylesheets = ['sphinx','kerning','a4']

# Language to be used for hyphenation support
#pdf_language = "en_US"
    
# Mode for literal blocks wider than the frame. Can be
# overflow, shrink or truncate
#pdf_fit_mode = "shrink"

    # Section level that forces a break page.
    # For example: 1 means top-level sections start in a new page
    # 0 means disabled
    #pdf_break_level = 0

# When a section starts in a new page, force it to be 'even', 'odd',
# or just use 'any'
#pdf_breakside = 'any'

# Insert footnotes where they are defined instead of 
# at the end.
#pdf_inline_footnotes = True

# verbosity level. 0 1 or 2
#pdf_verbosity = 0

# If false, no index is generated.
#pdf_use_index = True

    # If false, no modindex is generated.
    #pdf_use_modindex = True

# If false, no coverpage is generated.
#pdf_use_coverpage = True
   
    # Name of the cover page template to use
    #pdf_cover_template = 'sphinxcover.tmpl'

# ----- Options for epub output ----------
#
#epub_basename
#The basename for the epub file. It defaults to the project name.

#epub_theme
#The HTML theme for the epub output. Since the default themes are not optimized for small screen space, using the same theme for HTML and epub output is usually not wise. This defaults to 'epub', a theme designed to save visual space.

epub_title="Computer Networking : Principles, Protocols and Practice"
#The title of the document. It defaults to the html_title option but can be set independently for epub creation.

epub_author="Olivier Bonaventure"
#The author of the document. This is put in the Dublin Core metadata. The default value is 'unknown'.

epub_language="en"
#The language of the document. This is put in the Dublin Core metadata. The default is the language option or 'en' if unset.

epub_publisher="Presses Universitaires de Louvain"
#The publisher of the document. This is put in the Dublin Core metadata. You may use any sensible string, e.g. the project homepage. The default value is 'unknown'.

epub_copyright="Copyright 2011, Olivier Bonaventure"
#The copyright of the document. It defaults to the copyright option but can be set independently for epub creation.

epub_identifier="http://inl.info.ucl.ac.be/cnp3"
#An identifier for the document. This is put in the Dublin Core metadata. For published documents this is the ISBN number, but you can also use an alternative scheme, e.g. the project homepage. The default value is 'unknown'.

epub_scheme="URL"
#The publication scheme for the epub_identifier. This is put in the Dublin Core metadata. For published books the scheme is 'ISBN'. If you use the project homepage, 'URL' seems reasonable. The default value is 'unknown'.

#epub_uid="CNP3_"+version
#A unique identifier for the document. This is put in the Dublin Core metadata. You may use a random string. The default value is 'unknown'.

#epub_pre_files
#Additional files that should be inserted before the text generated by Sphinx. It is a list of tuples containing the file name and the title. If the title is empty, no entry is added to toc.ncx. Example:

# pour mobi
#epub_pre_files = [
#    ('index.html', 'Overview'),
#]
#The default value is [].

#epub_post_files
#Additional files that should be inserted after the text generated by Sphinx. It is a list of tuples containing the file name and the title. This option can be used to add an appendix. If the title is empty, no entry is added to toc.ncx. The default value is [].

#epub_exclude_files
#A list of files that are generated/copied in the build directory but should not be included in the epub file. The default value is [].

#epub_tocdepth
#The depth of the table of contents in the file toc.ncx. It should be an integer greater than zero. The default value is 3. Note: A deeply nested table of contents may be difficult to navigate.

#epub_tocdup
#This flag determines if a toc entry is inserted again at the beginning of it’s nested toc listing. This allows easier navitation to the top of a chapter, but can be confusing because it mixes entries of differnet depth in one list. The default value is True.

epub_cover=('cnp3.png','')
#The cover page information. This is a tuple containing the filenames of the cover image and the html template. The rendered html cover page is inserted as the first item in the spine in content.opf. If the template filename is empty, no html cover page is created. No cover at all is created if the tuple is empty. Examples:
#epub_cover = ('_static/cover.png', 'epub-cover.html')
#epub_cover = ('_static/cover.png', '')
#epub_cover = ()


# numfig:
#numfig_number_figures = True
#numfig_figure_caption_prefix = "Fig."



# graphviz

#graphviz_dot_args= "-v"
