# usage:
#           from constants import BG_COLOR, HEADINGFONT, MENUFONT, COLUMN_PER_ROW
#
import pyglet

BG_COLOR = "#3d6466"
HEADINGFONT = "TkHeadingFont"
try:
    pyglet.font.add_file("./TkinterRecipes/fonts/Ubuntu-Bold.ttf")      # replace Heading Font
    HEADINGFONT = "Ubuntu"
except:
    pass
MENUFONT = "TkMenuFont"
try:
    pyglet.font.add_file("./TkinterRecipes/fonts/Shanti-Regular.ttf")   # replace Menu Font
    MENUFONT = "Shanti"
except:
    pass

COLUMN_PER_ROW = 4