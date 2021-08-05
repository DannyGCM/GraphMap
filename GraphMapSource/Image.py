# Danny Garcia
# Image.py

# Modules
import tkinter as tk
from .Window import Window as Window
from .GraphicsPrimitive import GraphicsPrimitive as GraphicsPrimitive

# Image class (Primitive)
class Image(GraphicsPrimitive):

    # Constructor
    def __init__(self, window_name, point, path, anchor_type="nw",
    inplace=True):

        # Arguments
        self._window = window_name
        self._path = path
        self._image = tk.PhotoImage(file=path)
        self._point = point
        self._anchor_type = \
        (tk.NW, tk.CENTER)[("nw", "center").index(anchor_type)]

        self._item = "N/A"

        # Draws inplace if desired
        self.draw() if inplace else None

    # Class representation
    def __repr__(self):
        text = "<Image Object>\n"
        text += f"Path: {self._path}\n"
        text += f"Point: {self._point}\n"
        text += f"Anchor Type: {self._anchor_type}"
        return text

    # Draws image
    def draw(self):
        if not self.is_drawn():
            self._item = self._window.window.create_image(self._point,
            image=self._image, anchor=self._anchor_type)
            self._window.object_list.append(self._item)
        else: print("Object already drawn.")

    # Moves the image
    def move(self, x=0, y=0):
        self._point = (self._point[0] + x, self._point[1] + y)

        if self.is_drawn():
            self.undraw()
            self.draw()

    # Copies the image
    def copy(self):
        return Image(self._window, self._point, self._path, anchor_type = \
        ("nw", "center")[(tk.NW, tk.CENTER).index(self._anchor_type)])

    # Returns width of image in pixels
    def width(self):
        return self._image.width()

    # Returns height of image in pixels
    def height(self):
        return self._image.height()

    # Properties
    @property
    def window(self):
        return self._window

    @property
    def path(self):
        return self._path

    @property
    def image(self):
        return self._path

    @property
    def point(self):
        return self._point

    @property
    def anchor_type(self):
        return ("nw", "center")[(tk.NW, tk.CENTER).index(self._anchor_type)]

    # Setters
    @path.setter
    def path(self, path):
        self._path = path
        self._image = tk.PhotoImage(file=path)

        if self.is_drawn():
            self.undraw()
            self.draw()

    @image.setter
    def image(self, path):
        self._path = path
        self._image = tk.PhotoImage(file=path)

        if self.is_drawn():
            self.undraw()
            self.draw()

    @point.setter
    def point(self, point):
        self._point = point

        if self.is_drawn():
            self.undraw()
            self.draw()

    @anchor_type.setter
    def anchor_type(self, anchor_type):
        self._anchor_type = \
        (tk.NW, tk.CENTER)[("nw", "center").index(anchor_type)]
