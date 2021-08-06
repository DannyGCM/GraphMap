# Danny Garcia
# GraphMap.py

# Modules
import tkinter.font
import sys
import os

# Python Version Check
if sys.version_info[0] < 3:
    raise PythonVersionException("GraphMap is only compatible with Python 3")

# Imports window object
from .GraphMapSource.Window import Window as Window

# Graphics Primitives
from .GraphMapSource.Line import Line as Line
from .GraphMapSource.Rectangle import Rectangle as Rectangle
from .GraphMapSource.Polygon import Polygon as Polygon
from .GraphMapSource.Circle import Circle as Circle
from .GraphMapSource.Oval import Oval as Oval
from .GraphMapSource.Text import Text as Text
from .GraphMapSource.Image import Image as Image

# Composite objects
from .GraphMapSource.Button import Button as Button
from .GraphMapSource.InputBox import InputBox as InputBox
