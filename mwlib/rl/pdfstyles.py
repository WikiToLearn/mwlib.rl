#! /usr/bin/env python
#! -*- coding:utf-8 -*-

# Copyright (c) 2007, PediaPress GmbH
# See README.txt for additional licensing information.

#################################################################
#
# PLEASE DO NOT EDIT THIS FILE UNLESS YOU KNOW WHAT YOU ARE DOING
#
# If you want to customize the layout of the pdf, do this in
# a separate file customconfig.py
#
#################################################################


import os

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.lib.units import cm

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4


# used to mark translateable strings:
if '_' not in globals():
    _ = lambda x: x


serif_font =  "FreeSerif"
sans_font = "FreeSans"
mono_font = "FreeMono"
default_font = 'FreeSerif'


from reportlab import rl_config
rl_config.canvas_basefontname = default_font


######### PAGE CONFIGURATION

page_width, page_height = A4   # roughly: pW= 21*cm pH=29*cm

page_margin_left = 2 * cm
page_margin_right = 2 * cm
page_margin_top = 2 * cm
page_margin_bottom = 2 * cm

header_margin_hor = 1.5 * cm
header_margin_vert= 1.5 * cm

footer_margin_hor = 1.5 * cm
footer_margin_vert= 1.5 * cm

# margins for title page
title_margin_left = page_margin_left
title_margin_right = page_margin_right
title_margin_top = page_margin_top
title_margin_bottom = page_margin_bottom

show_title_page = True
show_title_page_footer = True
show_page_header = True 
show_page_footer = True
page_break_after_article = False

show_article_attribution = True   # Show/Hide article source and contributors
show_article_hr = True           # Underline each article header by a horizontal rule
show_wiki_license = True

# NOTE: strings can contain reportlab styling tags the text needs to be xml excaped.
# more information is available in the reportlab user documentation (http://www.reportlab.com/docs/userguide.pdf)
# check the section 6.2 "Paragraph XML Markup Tags"
# since the documenatition is not guaranteed to be up to date, you might also want to check the docsting of the
# Paragraph class (reportlab/platypus/paragraph.py --> class Paragraph())
# e.g. the use of inline images is not included in the official documenation of reportlab
pagefooter = u''

#### TITLE PAGE

title_page_image = '' # path of an image that is to be displayed on the title page
title_page_image_size = (12*cm, 17*cm) # max. width, height of image, aspect ratio is kept
# position of image relativ to bottom, left corner.
# If component is set to None the image is centered
# It is ensured that the image is not moved out of the page boundaries
title_page_image_pos = (None, None)

titlepagefooter = _(u'PDF generated using the open source mwlib toolkit. See http://code.pediapress.com/ for more information.')
show_creation_date = True

# if enabled a table of contents is printed at the beginning of the pdf
# note that no TOC is generated if only one article is rendered
render_toc = True

### TABLE CONFIG

tableOverflowTolerance = 20  # max width overflow for tables    unit: pt 
cell_padding = 3
min_rows_for_break = 3 # page breaks before tables are only forced if more than n rows are present

# if set to True column widths are extracted from wiki markup if possible
table_widths_from_markup = False

# alignment of tables: TA_LEFT | TA_CENTER | TA_RIGHT
table_align = TA_CENTER

######### TREECLEANER CONFIGURATION

treecleaner_skip_methods = ['fixPreFormatted', 'removeEmptyReferenceLists']

######### IMAGE CONFIGURATION

# margins for floated images - margins like in html/css: (top, right, bottom, left)
img_margins_float_left = (0, 0.4*cm, 0.7*cm, 0) # img that is left aligned
img_margins_float_right = (0, 0, 0.7*cm, 0.4*cm) # ...
img_margins_float = (0.2*cm,0.2*cm,0.2*cm,0.2*cm) # any other alignment

img_default_thumb_width = 180
img_max_thumb_width = 0.6 # fraction of print width for floated images
img_max_thumb_height = 0.45
img_min_res = 75
img_inline_scale_factor = 0.7 # factor by which inline images are scaled.
print_width_px = 540 # 540px are assumed to be the equivalent for a full print width

img_border_color=(0.75, 0.75, 0.75)

link_images = True

######### TEXT CONFIGURATION
font_size = 10
leading = 15
text_align = TA_JUSTIFY # default alignment of text outside of tables TA_LEFT, TA_JUSTIFY, TA_RIGHT, TA_CENTER are valid
table_text_align = TA_LEFT # ... inside of tables
min_lines_after_heading = 5

small_font_size = 8
small_leading = 12

big_font_size = 12
big_leading = 17

para_left_indent = 25 # indentation of paragraphs...
para_right_indent = 25 # indentation of paragraphs...
list_left_indent = 12 # indentation of lists per level

tabsize = 6

source_max_line_len = 72 # if printing a source node, the maximum number of chars in one line

no_float_math_len = 150

max_math_width = 2500
max_math_height = 2500
#set to CJK if a PDF is rendered mainly using chinese, japanese or korean glyphs
word_wrap=None

min_preformatted_size = 5


chapter_rule_color = colors.black
# misc options

list_item_style = u'\u2022'

url_blacklist = ['http://toolserver.org']

# URLs in tables are put in the reference section if
# url_ref_in_table = True and url is longer than url_ref_len
url_ref_in_table = True
url_ref_len = 30

class BaseStyle(ParagraphStyle):

    def __init__(self, name, parent=None, **kw):
        ParagraphStyle.__init__(self, name=name, parent=parent, **kw)
        self.fontName = serif_font
        self.fontSize = font_size
        self.leading = leading
        self.autoLeading = 'max'
        self.leftIndent = 0
        self.rightIndent = 0
        self.firstLineIndent = 0
        self.alignment = text_align
        self.spaceBefore = 3
        self.spaceAfter = 0
        self.bulletFontName = serif_font
        self.bulletFontSize = font_size
        self.bulletIndent = 0
        self.textColor = colors.black
        self.backColor = None
        self.wordWrap = None
        self.textTransform = None
        
def text_style(mode='p', indent_lvl=0, in_table=0, relsize='normal', text_align=None):
    """
    mode: p (normal paragraph), blockquote, center (centered paragraph), footer, figure (figure caption text),
          preformatted, list, license, licenselist, box, references, articlefoot
    relsize: relative text size: small, normal, big  (currently only used for preformatted nodes
    indent_lvl: level of indentation in lists or indented paragraphs
    in_table: 0 - outside table
              1 or above - inside table (nesting level of table)
    text_align: left, center, right, justify
    """

    if not text_align:
        text_align = 'left'

    style = BaseStyle(name='text_style_%s_indent_%d_table_%d_size_%s' % (mode, indent_lvl, in_table, relsize))
    style.flowable = True # needed for "flowing" paragraphs around figures

    if word_wrap in ['CJK', 'RTL'] and mode not in ['preformatted', 'source']:
        style.wordWrap = word_wrap

    if in_table > 0:
        style.alignment = table_text_align
    if text_align == 'right':
        style.alignment = TA_RIGHT
    elif text_align == 'center':
        style.alignment = TA_CENTER

    if in_table or mode in ['footer', 'figure'] or (mode=='preformatted' and relsize=='small'):
        style.fontSize=small_font_size
        style.bulletFontSize = small_font_size
        style.leading = small_leading
        if relsize == 'small':
            style.fontSize -= 1
        elif relsize == 'big':
            style.fontSize += 1

    if mode == 'blockquote':
        style.rightIndent = para_right_indent
        indent_lvl += 1

    if mode in ['footer', 'figure', 'center']:
        style.alignment = TA_CENTER

    if mode in ['references', 'articlefoot', 'source', 'preformatted', 'list', 'attribution', 'img_attribution']:
        style.alignment = TA_LEFT

    if mode in ['attribution', 'img_attribution']:
        style.fontSize = 6
        style.leading = 8
        style.spaceBefore = 6

    if mode == 'img_attribution':
        style.spaceBefore = 2
        
    if mode in ['articlefoot', 'references']:
        style.fontSize=small_font_size
        style.leading=small_leading
        style.bulletFontSize = small_font_size

    if mode == 'box' or mode == 'source' or mode == 'preformatted':
        style.backColor = '#eeeeee'
        style.borderPadding = 3 # borderPadding is not calculated onto the box dimensions.
        style.spaceBefore = 6 # therefore spaceBefore = 3 + borderPadding
        style.spaceAfter = 9 # add an extra 3 to spaceAfter, b/c spacing seems to small otherwise
    
    if mode == 'source' or mode == 'preformatted':
        style.fontName = mono_font   
        style.flowable = False
        
    if mode == 'list' or mode == 'references':
        style.spaceBefore = 0
        style.bulletIndent = list_left_indent * max(0, indent_lvl-1)
        style.leftIndent = list_left_indent * indent_lvl
    else:
        style.leftIndent = indent_lvl*para_left_indent

    if mode == 'booktitle':
        style.fontSize = 36
        style.leading = 40
        style.spaceBefore = 16
        style.fontName= sans_font
        style.alignment = TA_LEFT
        
    if mode == 'booksubtitle':
        style.fontSize = 24
        style.leading = 30
        style.fontName= sans_font
        style.alignment = TA_LEFT

    if word_wrap == 'RTL':
        # switch all alignment, indentations for rtl languages
        if style.alignment in [TA_LEFT, TA_JUSTIFY]:
            style.alignment = TA_RIGHT
        elif style.alignment == TA_RIGHT:
            style.alignment = TA_LEFT

        style.leftIndent, style.rightIndent = style.rightIndent, style.leftIndent

    if mode == 'license':
        style.fontSize = 5
        style.leading = 1
        style.spaceBefore = 0

    if mode == 'licenselist':
        style.fontSize = 5
        style.leading = 1
        style.spaceBefore = 0
        style.bulletIndent = list_left_indent * max(0, indent_lvl-1)
        style.leftIndent = list_left_indent * indent_lvl
        style.bulletFontSize = 5

    if mode == 'toc_group':
        style.fontSize = 18
        style.leading = 22
       
    if mode == 'toc_chapter':
        style.fontSize = 14
        style.leading = 18
        
    if mode == 'toc_article':
        style.fontSize = 10
        style.leading = 12
        style.leftIndent = para_left_indent

    return style

table_style = {'spaceBefore': 0.25*cm,
               'spaceAfter': 0.25*cm}


class BaseHeadingStyle(ParagraphStyle):

    def __init__(self, name, parent=None, **kw):
        ParagraphStyle.__init__(self, name=name, parent=parent, **kw)
        self.fontName = serif_font
        self.fontSize = big_font_size
        self.leading = leading
        self.autoLeading = 'max'
        self.leftIndent = 0
        self.rightIndent = 0
        self.firstLineIndent = 0
        self.alignment = TA_LEFT        
        self.spaceBefore = 12
        self.spaceAfter = 6
        self.bulletFontName = serif_font
        self.bulletFontSize = big_font_size
        self.bulletIndent = 0
        self.textColor = colors.black
        self.backcolor = None
        self.wordWrap = None
        self.textTransform = None
        #self.allowWidows = 0
        #self.allowOrphans = 0
        
def heading_style(mode='chapter', lvl=1, text_align=None):

    style = BaseHeadingStyle(name='heading_style_%s_%d' % (mode, lvl))

    if word_wrap == 'RTL':
        style.wordWrap = 'RTL'
        if not text_align:
            style.alignment = TA_RIGHT

    if mode == 'chapter':
        style.fontSize = 26
        style.leading = 30
        style.alignment = TA_CENTER
    elif mode == 'article':
        style.fontSize = 22
        style.leading = 26
        style.spaceBefore = 20
        style.spaceAfter = 2
    elif mode == 'section':
        lvl = max(min(5,lvl), 1)  
        style.fontSize = 18 - (lvl - 1) * 2
        style.leading = style.fontSize + max(2, min(int(style.fontSize / 5), 3)) # magic: increase in leading is between 2 and 3 depending on fontsize...
        style.spaceBefore = min(style.leading, 20)
        if lvl > 1: # needed for "flowing" paragraphs around figures
            style.flowable = True
    elif mode == 'tablecaption':
        style.fontSize = 12
        style.leading = 16
        style.alignment = TA_CENTER
        style.flowable = False
        style.spaceAfter = 0
    elif mode == "license":
        style.fontSize = 7
        style.leading = 5
        style.spaceAfter = 0
        style.spaceBefore = 2

    if text_align == 'left':
        style.alignment = TA_LEFT
    elif text_align == 'center':
        style.alignment = TA_CENTER
    elif text_align == 'right':
        style.alignment = TA_RIGHT
    elif text_align == 'justify':
        style.alignment = TA_JUSTIFY
    
    style.prevent_post_pagebreak = True
    return style
    

# import custom configuration to override configuration values
# if doing so, you need to be careful not to break things...
try:
    from customconfig import *
except ImportError:
    pass


print_width = page_width - page_margin_left - page_margin_right
print_height = page_height - page_margin_top - page_margin_bottom

article_start_min_space = 0.5*print_height # if less space is available on the current page a page break is inserted
article_start_min_space_infobox = 0.9*print_height # as above. but if the article starts with an infobox the required space should be higher

min_table_space = print_height / 4 # if less space is available, a page break will be inserted before the table
