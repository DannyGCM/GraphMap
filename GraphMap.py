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

# GraphicsPrimitive class (Parent class for primitives)
class GraphicsPrimitive:
    def __str__(self):
        return self.__repr__()

    # Returns object's draw status
    def is_drawn(self):
        return self._item in self._window.object_list

    # Undraws the object
    def undraw(self):
        if self.is_drawn():
            self._window.window.delete(self._item)
            del self._window.object_list[self._window.object_list.index(self._item)]
        else:
            print("Object isn't drawn.")


# Line class (Primitive)
class Line(GraphicsPrimitive):
    def __init__(self, window_name, point_a, point_b, color=(0, 0, 0), width=1, dash=(), inplace_draw=True):
        # Arguments
        self._window = window_name
        self._point_a = point_a
        self._point_b = point_b
        self._color = color
        self._width = width
        self._dash = dash

        self._item = "N/A"

        self.draw() if inplace_draw else None

    def __repr__(self):
        text = "<Line Object>\n"
        text += f"Point A: {self._point_a}\n"
        text += f"Point B: {self._point_b}\n"
        text += f"Color: {self._color}\n"
        text += f"Width: {self._width}\n"
        text += f"Dash: {self._dash}"
        return text

    # Draws the line
    def draw(self):
        if not self.is_drawn():
            self._item = self._window.window.create_line(self._point_a, self._point_b,
                                                         fill=Window.rgb_to_bit(self._color),
                                                         width=self._width, dash=self._dash)
            self._window.object_list.append(self._item)
        else:
            print("Object already drawn.")

    # Moves the line
    def move(self, x=0, y=0):
        self._point_a = (self._point_a[0] + x, self._point_a[1] + y)
        self._point_b = (self._point_b[0] + x, self._point_b[1] + y)

        if self.is_drawn():
            self.undraw()
            self.draw()

    # Copies the line
    def copy(self):
        return Line(self._window, self._point_a, self._point_b, color=self._color, width=self._width, dash=self._dash)

    # Returns the length of the line
    def length(self):
        return math.sqrt(((self._point_b[0] - self._point_a[0]) ** 2) + ((self._point_b[1] - self._point_a[1]) ** 2))

    # Properties
    @property
    def window(self):
        return self._window

    @property
    def point_a(self):
        return self._point_a

    @property
    def point_b(self):
        return self._point_b

    @property
    def color(self):
        return self._color

    @property
    def width(self):
        return self._width

    @property
    def dash(self):
        return self._dash

    # Setters
    @point_a.setter
    def point_a(self, point):
        self._point_a = point

        if self.is_drawn():
            self.undraw()
            self.draw()

    @point_b.setter
    def point_b(self, point):
        self._point_b = point

        if self.is_drawn():
            self.undraw()
            self.draw()

    @color.setter
    def color(self, color):
        self._color = color

        if self.is_drawn():
            self.undraw()
            self.draw()

    @width.setter
    def width(self, width):
        self._width = width

        if self.is_drawn():
            self.undraw()
            self.draw()

    @dash.setter
    def dash(self, dash):
        self._dash = dash

        if self.is_drawn():
            self.undraw()
            self.draw()


# Rectangle class (Primitive)
class Rectangle(GraphicsPrimitive):
    def __init__(self, window_name, point_a, point_b, color=(0, 0, 0), outline_color=(0, 0, 0), outline_width=0,
                 inplace_draw=True):
        # Arguments
        self._window = window_name
        self._point_a = point_a
        self._point_b = point_b
        self._color = color
        self._outline_color = outline_color
        self._outline_width = outline_width

        self._item = "N/A"

        self.draw() if inplace_draw else None

    def __repr__(self):
        text = "<Rectangle Object>\n"
        text += f"Point A: {self._point_a}\n"
        text += f"Point B: {self._point_b}\n"
        text += f"Color: {self._color}\n"
        text += f"Outline Color: {self._outline_color}\n"
        text += f"Outline Width: {self._outline_width}"
        return text

    # Draws the rectangle
    def draw(self):
        if not self.is_drawn():
            self._item = self._window.window.create_rectangle(self._point_a, self._point_b,
                                                              fill=Window.rgb_to_bit(self._color),
                                                              outline=Window.rgb_to_bit(self._outline_color),
                                                              width=self._outline_width)
            self._window.object_list.append(self._item)
        else:
            print("Object already drawn.")

    # Moves the rectangle
    def move(self, x=0, y=0):
        self._point_a = (self._point_a[0] + x, self._point_a[1] + y)
        self._point_b = (self._point_b[0] + x, self._point_b[1] + y)

        if self.is_drawn():
            self.undraw()
            self.draw()

    # Copies the rectangle
    def copy(self):
        return Rectangle(self._window, self.point_a, self.point_b, color=self.color, outline_color=self.outline_color,
                         outline_width=self.outline_width)

    # Properties
    @property
    def window(self):
        return self._window

    @property
    def point_a(self):
        return self._point_a

    @property
    def point_b(self):
        return self._point_b

    @property
    def color(self):
        return self._color

    @property
    def outline_color(self):
        return self._outline_color

    @property
    def outline_width(self):
        return self._outline_width

    # Setters
    @point_a.setter
    def point_a(self, point):
        self._point_a = point

        if self.is_drawn():
            self.undraw()
            self.draw()

    @point_b.setter
    def point_b(self, point):
        self._point_b = point

        if self.is_drawn():
            self.undraw()
            self.draw()

    @color.setter
    def color(self, color):
        self._color = color

        if self.is_drawn():
            self.undraw()
            self.draw()

    @outline_color.setter
    def outline_color(self, color):
        self._outline_color = color

        if self.is_drawn():
            self.undraw()
            self.draw()

    @outline_width.setter
    def outline_width(self, width):
        self._outline_width = width

        if self.is_drawn():
            self.undraw()
            self.draw()


# Polygon class (Primitive)
class Polygon(GraphicsPrimitive):
    def __init__(self, window_name, points, color=(0, 0, 0), outline_color=(0, 0, 0), outline_width=0,
                 inplace_draw=True):
        # Arguments
        self._window = window_name
        self._points = list(points)
        self._color = color
        self._outline_color = outline_color
        self._outline_width = outline_width

        self._item = "N/A"

        self.draw() if inplace_draw else None

    def __repr__(self):
        text = "<Polygon Object>\n"
        text += f"Number Of Points: {len(self._points) // 2}\n"
        text += f"Color: {self._color}\n"
        text += f"Outline Color: {self._outline_color}\n"
        text += f"Outline Width: {self._outline_width}"
        return text

    # Draws the polygon
    def draw(self):
        if not self.is_drawn():
            self._item = self._window.window.create_polygon(self._points, fill=Window.rgb_to_bit(self._color),
                                                            outline=Window.rgb_to_bit(self._outline_color),
                                                            width=self._outline_width)
            self._window.object_list.append(self._item)
        else:
            print("Object already drawn.")

    # Moves the polygon
    def move(self, x=0, y=0):
        for point in range(len(self._points)):
            if point % 2 == 0:
                self._points[point] += x
            else:
                self._points[point] += y

        if self.is_drawn():
            self.undraw()
            self.draw()

    # Copies the polygon
    def copy(self):
        return Polygon(self._window, self._points, color=self._color, outline_color=self._outline_color,
                       outline_width=self._outline_width)

    # Properties
    @property
    def window(self):
        return self._window

    @property
    def points(self):
        return self._points

    @property
    def color(self):
        return self._color

    @property
    def outline_color(self):
        return self._outline_color

    @property
    def outline_width(self):
        return self._outline_width

    # Setters
    @color.setter
    def color(self, color):
        self._color = color

        if self.is_drawn():
            self.undraw()
            self.draw()

    @outline_color.setter
    def outline_color(self, color):
        self._outline_color = color

        if self.is_drawn():
            self.undraw()
            self.draw()

    @outline_width.setter
    def outline_width(self, width):
        self._outline_width = width

        if self.is_drawn():
            self.undraw()
            self.draw()


# Circle class (Primitive)
class Circle(GraphicsPrimitive):
    def __init__(self, window_name, point, radius=5, color=(0, 0, 0), outline_color=(0, 0, 0), outline_width=0,
                 inplace_draw=True):
        # Arguments
        self._window = window_name
        self._point = point
        self._radius = radius
        self._color = color
        self._outline_color = outline_color
        self._outline_width = outline_width

        self._item = "N/A"

        self.draw() if inplace_draw else None

    def __repr__(self):
        text = "<Circle Object>\n"
        text += f"Point: {self._point}\n"
        text += f"Radius: {self._radius}\n"
        text += f"Color: {self._color}\n"
        text += f"Outline Color: {self._outline_color}\n"
        text += f"Outline Width: {self._outline_width}"
        return text

    # Draws the circle
    def draw(self):
        if not self.is_drawn():
            self._item = self._window.window.create_oval(self._point[0] - self._radius, self._point[1] + self._radius,
                                                         self._point[0] + self._radius, self._point[1] - self._radius,
                                                         fill=Window.rgb_to_bit(self._color),
                                                         outline=Window.rgb_to_bit(self._outline_color),
                                                         width=self._outline_width)
            self._window.object_list.append(self._item)
        else:
            print("Object already drawn.")

    # Moves the circle
    def move(self, x=0, y=0):
        self._point = (self._point[0] + x, self._point[1] + y)

        if self.is_drawn():
            self.undraw()
            self.draw()

    # Copies the circle
    def copy(self):
        return Circle(self._window, self._point, radius=self._radius, color=self._color,
                      outline_color=self._outline_color,
                      outline_width=self._outline_width)

    # Properties
    @property
    def window(self):
        return self._window

    @property
    def point(self):
        return self._point

    @property
    def radius(self):
        return self._radius

    @property
    def color(self):
        return self._color

    @property
    def outline_color(self):
        return self._outline_color

    @property
    def outline_width(self):
        return self._outline_width

    # Setters
    @point.setter
    def point(self, point):
        self._point = point

        if self.is_drawn():
            self.undraw()
            self.draw()

    @radius.setter
    def radius(self, radius):
        self._radius = radius

        if self.is_drawn():
            self.undraw()
            self.draw()

    @color.setter
    def color(self, color):
        self._color = color

        if self.is_drawn():
            self.undraw()
            self.draw()

    @outline_color.setter
    def outline_color(self, color):
        self._outline_color = color

        if self.is_drawn():
            self.undraw()
            self.draw()

    @outline_width.setter
    def outline_width(self, width):
        self._outline_width = width

        if self.is_drawn():
            self.undraw()
            self.draw()


# Oval class (Primitive)
class Oval(GraphicsPrimitive):
    def __init__(self, window_name, point_a, point_b, color=(0, 0, 0), outline_color=(0, 0, 0), outline_width=0,
                 inplace_draw=True):
        # Arguments
        self._window = window_name
        self._point_a = point_a
        self._point_b = point_b
        self._color = color
        self._outline_color = outline_color
        self._outline_width = outline_width

        self._item = "N/A"

        self.draw() if inplace_draw else None

    def __repr__(self):
        text = "<Oval Object>\n"
        text += f"Point A: {self._point_a}\n"
        text += f"Point B: {self._point_b}\n"
        text += f"Color: {self._color}\n"
        text += f"Outline Color: {self._outline_color}\n"
        text += f"Outline Width: {self._outline_width}"
        return text

    # Draws the oval
    def draw(self):
        if not self.is_drawn():
            self._item = self._window.window.create_oval(self._point_a, self._point_b,
                                                         fill=Window.rgb_to_bit(self._color),
                                                         outline=Window.rgb_to_bit(self._outline_color),
                                                         width=self._outline_width)
            self._window.object_list.append(self._item)
        else:
            print("Object already drawn.")

    # Moves the oval
    def move(self, x=0, y=0):
        self._point_a = (self._point_a[0] + x, self._point_a[1] + y)
        self._point_b = (self._point_b[0] + x, self._point_b[1] + y)

        if self.is_drawn():
            self.undraw()
            self.draw()

    # Copies the oval
    def copy(self):
        return Oval(self._window, self._point_a, self._point_b, color=self._color, outline_color=self._outline_color,
                    outline_width=self._outline_width)

    # Properties
    @property
    def window(self):
        return self._window

    @property
    def point_a(self):
        return self._point_a

    @property
    def point_b(self):
        return self._point_b

    @property
    def color(self):
        return self._color

    @property
    def outline_color(self):
        return self._outline_color

    @property
    def outline_width(self):
        return self._outline_width

    # Setters
    @point_a.setter
    def point_a(self, point):
        self._point_a = point

        if self.is_drawn():
            self.undraw()
            self.draw()

    @point_b.setter
    def point_b(self, point):
        self._point_b = point

        if self.is_drawn():
            self.undraw()
            self.draw()

    @color.setter
    def color(self, color):
        self._color = color

        if self.is_drawn():
            self.undraw()
            self.draw()

    @outline_color.setter
    def outline_color(self, color):
        self._outline_color = color

        if self.is_drawn():
            self.undraw()
            self.draw()

    @outline_width.setter
    def outline_width(self, width):
        self._outline_width = width

        if self.is_drawn():
            self.undraw()
            self.draw()


# Text class (Primitive)
class Text(GraphicsPrimitive):
    def __init__(self, window_name, point, text, font, size, color=(0, 0, 0), bold=False, italic=False, anchor="nw",
                 inplace_draw=True):
        # Arguments
        self._window = window_name
        self._point = point
        self._text = text
        self._font = font
        self._size = size
        self._color = color
        self._bold = bold
        self._italic = italic
        self._anchor = anchor

        self._item = "N/A"

        self.draw() if inplace_draw else None

    def __repr__(self):
        text = "<Text Object>\n"
        text += f"Point: {self._point}\n"
        text += f"Text: {self._text}\n"
        text += f"Font: {self._font}\n"
        text += f"Size: {self._size}\n"
        text += f"Color: {self._color}\n"
        text += f"Bold: {self._bold}\n"
        text += f"Italic: {self._italic}\n"
        text += f"Anchor: {self._anchor}"
        return text

    # Draws the text
    def draw(self):
        if not self.is_drawn():
            self._item = self._window.window.create_text(self._point, fill=Window.rgb_to_bit(self._color),
                                                         font=self._font + f" {str(self._size)}" +
                                                         ("", " italic")[self._italic] +
                                                         ("", " bold")[self._bold], text=self._text,
                                                         anchor=self._anchor)
            self._window.object_list.append(self._item)
        else:
            print("Object already drawn.")

    # Moves the text
    def move(self, x=0, y=0):
        self._point = (self._point[0] + x, self._point[1] + y)

        if self.is_drawn():
            self.undraw()
            self.draw()

    # Copies the text
    def copy(self):
        return Text(self._window, self._point, self._text, self._font, self._size, color=self._color, bold=self._bold,
                    italic=self._italic, anchor=self._anchor)

    # Returns width of text in pixels
    def width(self):
        return tk.font.Font(size=self._size, family=self._font, slant=("roman", "italic")[self._italic],
                            weight=("normal", "bold")[self._bold]).measure(self._text)

    # Properties
    @property
    def window(self):
        return self._window

    @property
    def point(self):
        return self._point

    @property
    def text(self):
        return self._text

    @property
    def font(self):
        return self._font

    @property
    def size(self):
        return self._size

    @property
    def color(self):
        return self._color

    @property
    def bold(self):
        return self._bold

    @property
    def italic(self):
        return self._italic

    @property
    def anchor(self):
        return self._anchor

    # Setters
    @point.setter
    def point(self, point):
        self._point = point

        if self.is_drawn():
            self.undraw()
            self.draw()

    @text.setter
    def text(self, text):
        self._text = text

        if self.is_drawn():
            self.undraw()
            self.draw()

    @font.setter
    def font(self, font):
        self._font = font

        if self.is_drawn():
            self.undraw()
            self.draw()

    @size.setter
    def size(self, size):
        self._size = size

        if self.is_drawn():
            self.undraw()
            self.draw()

    @color.setter
    def color(self, color):
        self._color = color

        if self.is_drawn():
            self.undraw()
            self.draw()

    @bold.setter
    def bold(self, bold):
        self._bold = bold

        if self.is_drawn():
            self.undraw()
            self.draw()

    @italic.setter
    def italic(self, italic):
        self._italic = italic

        if self.is_drawn():
            self.undraw()
            self.draw()

    @anchor.setter
    def anchor(self, anchor):
        self._anchor = anchor

        if self.is_drawn():
            self.undraw()
            self.draw()


# Image class (Primitive)
class Image(GraphicsPrimitive):
    def __init__(self, window_name, point, path, anchor_type="nw", inplace_draw=True):
        # Arguments
        self._window = window_name
        self._path = path
        self._image = tk.PhotoImage(file=path)
        self._point = point
        self._anchor_type = (tk.NW, tk.CENTER)[("nw", "center").index(anchor_type)]

        self._item = "N/A"

        self.draw() if inplace_draw else None

    def __repr__(self):
        text = "<Image Object>\n"
        text += f"Path: {self._path}\n"
        text += f"Point: {self._point}\n"
        text += f"Anchor Type: {self._anchor_type}"
        return text

    # Draws image
    def draw(self):
        if not self.is_drawn():
            self._item = self._window.window.create_image(self._point, image=self._image, anchor=self._anchor_type)
            self._window.object_list.append(self._item)
        else:
            print("Object already drawn.")

    # Moves the image
    def move(self, x=0, y=0):
        self._point = (self._point[0] + x, self._point[1] + y)

        if self.is_drawn():
            self.undraw()
            self.draw()

    # Copies the image
    def copy(self):
        return Image(self._window, self._point, self._path,
                     anchor_type=("nw", "center")[(tk.NW, tk.CENTER).index(self._anchor_type)])

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
        self._anchor_type = (tk.NW, tk.CENTER)[("nw", "center").index(anchor_type)]


# Button class
class Button:
    def __init__(self, window_name, point_a, point_b, box_color=(0, 0, 0), outline_color=(0, 0, 0),
                 hovered_box_color=(40, 40, 40), hovered_outline_color=(40, 40, 40), clicked_box_color=(80, 80, 80),
                 clicked_outline_color=(80, 80, 80), outline_width=0, text="", font="Times", font_size=20,
                 font_color=(255, 255, 255), hovered_font_color=(210, 210, 210), clicked_font_color=(170, 170, 170),
                 bold=False, italic=False, image_path="", hovered_image_path="", clicked_image_path="", inplace_draw=True):
        # Arguments
        self._window = window_name
        self._point_a = point_a
        self._point_b = point_b
        self.box_color = box_color
        self.outline_color = outline_color
        self.hovered_box_color = hovered_box_color
        self.hovered_outline_color = hovered_outline_color
        self.clicked_box_color = clicked_box_color
        self.clicked_outline_color = clicked_outline_color
        self.outline_width = outline_width
        self.text = text
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.hovered_font_color = hovered_font_color
        self.clicked_font_color = clicked_font_color
        self.bold = bold
        self.italic = italic
        self.image_path = image_path
        self.hovered_image_path = hovered_image_path
        self.clicked_image_path = clicked_image_path

        # Components
        self._box, self._image, self._text = "N/A", "N/A", "N/A"

        # Variables
        self._current_status = "NONE_"
        self._status = "NONE"
        self._initializing = True

        self._set_boundaries()
        self.draw() if inplace_draw else None

    def __repr__(self):
        text = "<Button Object>\n"
        text += f"Point A: {self._point_a}\n"
        text += f"Point B: {self._point_b}\n"
        return text

    def __str__(self):
        return self.__repr__()

    # Gets draw status of the button
    def is_drawn(self):
        return (self,) in self._window.object_list

    # Sets the button's boundaries
    def _set_boundaries(self):
        self._left_boundary = self._point_a[0] if self._point_a[0] < self._point_b[0] else self._point_b[0]
        self._right_boundary = self._point_a[0] if self._point_a[0] > self._point_b[0] else self._point_b[0]
        self._up_boundary = self._point_a[1] if self._point_a[1] > self._point_b[1] else self._point_b[1]
        self._down_boundary = self._point_a[1] if self._point_a[1] < self._point_b[1] else self._point_b[1]

    # Draws the button
    def draw(self):
        if not self.is_drawn():
            self._window.object_list.append((self,))
        else:
            print("Object already drawn.")

    # Undraw the button
    def undraw(self):
        if self.is_drawn():
            self._window.window.delete(self._box, self._image, self._text)
            del self._window.object_list[self._window.object_list.index((self,))]
        else:
            print("Object isn't drawn.")

    # Updates the button
    def update(self):
        # Gives clicked button animation time to be displayed
        if self._status == "CLICKED":
            time.sleep(1 / 30)

        # Updates status
        if not (self._left_boundary < self._window.last_motion[0] < self._right_boundary and
                self._up_boundary > self._window.last_motion[1] > self._down_boundary):
            if self._current_status != "INACTIVE":
                self._current_status = "INACTIVE"
        else:
            if self._window.last_mouse[0]:
                if self._current_status != "CLICKED":
                    self._current_status = "CLICKED"
            else:
                if self._current_status != "HOVERED":
                    self._current_status = "HOVERED"

        # Undraws components
        if not self._initializing and self._current_status != self._status:
            self._box.undraw()
            self._image.undraw()
            self._text.undraw()

            # Resets components
            self._box, self._image, self._text = "N/A", "N/A", "N/A"

        # Updates components
        # Inactive
        if self._current_status == "INACTIVE" and self._current_status != self._status:
            # Box
            self._box = Rectangle(self._window, self._point_a, self._point_b, color=self.box_color,
                                  outline_color=self.outline_color, outline_width=self.outline_width)
            # Image
            self._image = Image(self._window, (self._point_a[0] + (abs(self._point_a[0] - self._point_b[0]) // 2),
                                               self._point_a[1] + (abs(self._point_a[1] - self._point_b[1]) // 2)),
                                self.image_path, anchor_type="center")
            assert self._image.width() < abs(self._point_a[0] - self._point_b[0]) and self._image.height() < abs(
                self._point_a[1] - self._point_b[1]), "Image must be smaller than the button."
            # Text
            self._text = Text(self._window, (self._point_a[0] + (abs(self._point_a[0] - self._point_b[0]) // 2),
                                             self._point_a[1] + (abs(self._point_a[1] - self._point_b[1])) // 2),
                              self.text, self.font, self.font_size, color=self.font_color,
                              bold=self.bold, italic=self.italic, anchor="center")

            self._status = self._current_status

        # Hovered
        elif self._current_status == "HOVERED" and self._current_status != self._status:
            # Box
            self._box = Rectangle(self._window, self._point_a, self._point_b, color=self.hovered_box_color,
                                  outline_color=self.hovered_outline_color, outline_width=self.outline_width)
            # Image
            self._image = Image(self._window, (self._point_a[0] + (abs(self._point_a[0] - self._point_b[0]) // 2),
                                               self._point_a[1] + (abs(self._point_a[1] - self._point_b[1]) // 2)),
                                self.hovered_image_path, anchor_type="center")
            assert self._image.width() < abs(self._point_a[0] - self._point_b[0]) and self._image.height() < abs(
                self._point_a[1] - self._point_b[1]), "Image must be smaller than the button."
            # Text
            self._text = Text(self._window, (self._point_a[0] + (abs(self._point_a[0] - self._point_b[0]) // 2),
                                             self._point_a[1] + (abs(self._point_a[1] - self._point_b[1])) // 2),
                              self.text, self.font, self.font_size,
                              color=self.hovered_font_color, bold=self.bold, italic=self.italic, anchor="center")

            self._status = self._current_status
        # Clicked
        elif self._current_status == "CLICKED" and self._current_status != self._status:
            # Box
            self._box = Rectangle(self._window, self._point_a, self._point_b, color=self.clicked_box_color,
                                  outline_color=self.clicked_outline_color, outline_width=self.outline_width)
            # Image
            self._image = Image(self._window, (self._point_a[0] + (abs(self._point_a[0] - self._point_b[0]) // 2),
                                               self._point_a[1] + (abs(self._point_a[1] - self._point_b[1]) // 2)),
                                self.clicked_image_path, anchor_type="center")
            assert self._image.width() < abs(self._point_a[0] - self._point_b[0]) and self._image.height() < abs(
                self._point_a[1] - self._point_b[1]), "Image must be smaller than the button."
            # Text
            self._text = Text(self._window, (self._point_a[0] + (abs(self._point_a[0] - self._point_b[0]) // 2),
                                             self._point_a[1] + (abs(self._point_a[1] - self._point_b[1])) // 2),
                              self.text, self.font, self.font_size,
                              color=self.clicked_font_color, bold=self.bold, italic=self.italic, anchor="center")

            self._status = self._current_status

        if self._initializing:
            self._initializing = False

    # Moves the button
    def move(self, x=0, y=0):
        self._point_a = (self._point_a[0] + x, self._point_a[1] + y)
        self._point_b = (self._point_b[0] + x, self._point_b[1] + y)

        self._set_boundaries()

    # Copies the button
    def copy(self):
        return Button(self._window, self._point_a, self._point_b, box_color=self.box_color,
                      outline_color=self.outline_color, hovered_box_color=self.hovered_box_color,
                      hovered_outline_color=self.hovered_outline_color, clicked_box_color=self.clicked_box_color,
                      clicked_outline_color=self.clicked_outline_color, outline_width=self.outline_width,
                      text=self.text, font=self.font, font_size=self.font_size,
                      font_color=self.font_color, hovered_font_color=self.hovered_font_color,
                      clicked_font_color=self.clicked_font_color,
                      bold=self.bold, italic=self.italic, image_path=self.image_path,
                      hovered_image_path=self.hovered_image_path,
                      clicked_image_path=self.clicked_image_path)

    # Properties
    @property
    def point_a(self):
        return self._point_a

    @property
    def point_b(self):
        return self._point_B

    @property
    def status(self):
        return self._status

    # Setters
    @point_a.setter
    def point_a(self, point):
        self._point_a = point

        self._set_boundaries()

    @point_b.setter
    def point_b(self, point):
        self._point_b = point

        self._set_boundaries()


# Input Box Class
class InputBox:
    def __init__(self, window_name, point, length=200, height=30, text="SEARCH", bar_color=(200, 200, 200),
                 outline_color=(0, 0, 0), outline_width=0, text_y_margin=-1, text_x_margin=6, font="Consolas",
                 font_size=20, font_color=(20, 20, 20), bold=False, italic=False, pointer_width=2,
                 pointer_length=10, pointer_x_margin=4, pointer_y_margin=4, pointer_blink_frames=400,
                 pointer_color=(0, 0, 0), force_case="NONE", inplace_draw=True):
        # Arguments
        self._window = window_name
        self._point = point
        self.length = length
        self.height = height
        self.text = text
        self.bar_color = bar_color
        self.outline_color = outline_color
        self.outline_width = outline_width
        self.text_y_margin = text_y_margin
        self.text_x_margin = text_x_margin
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.bold = bold
        self.italic = italic
        self.pointer_width = pointer_width
        self.pointer_length = pointer_length
        self.pointer_x_margin = pointer_x_margin
        self.pointer_y_margin = pointer_y_margin
        self.pointer_blink_frames = pointer_blink_frames
        self.pointer_color = pointer_color
        self.force_case = force_case

        # Odd margins rounded down

        # Components
        self._bar, self._text, self._pointer = "N/A", "N/A", "N/A"

        # Variables
        self._current_status = "INACTIVE"
        self._status = "NONE"
        self._action = "NONE"
        self._initializing = True

        self._set_boundaries()
        self.draw() if inplace_draw else None

    def __repr__(self):
        text = "<InputBox Object>\n"
        text += f"Point {self._point}\n"
        text += f"Text: {self._text}\n"
        return text

    def __str__(self):
        return self.__repr__()

    # Gets draw status of the inputBox
    def is_drawn(self):
        return (self,) in self._window.object_list

    # Sets the inputBox's boundaries
    def _set_boundaries(self):
        self._left_boundary = self._point[0]
        self._right_boundary = self._point[0] + self.length
        self._up_boundary = self._point[1]
        self._down_boundary = self._point[1] + self.height

    # Draws the inputBox
    def draw(self):
        if not self.is_drawn():
            self._window.object_list.append((self,))
        else:
            print("Object already drawn.")

    # Undraw the inputBox
    def undraw(self):
        if self.is_drawn():
            self._window.window.delete(self._bar, self._text, self._pointer)
            del self._window.object_list[self._window.object_list.index((self,))]
        else:
            print("Object isn't drawn.")

    # Updates the inputBox
    def update(self):
        # Update status
        if self._window.last_mouse[0]:
            if self._left_boundary < self._window.last_motion[0] < self._right_boundary and \
                    self._up_boundary < self._window._last_motion[1] < self._down_boundary:
                if self._current_status != "CLICKED":
                    self._current_status = "CLICKED"
            else:
                if self._current_status != "INACTIVE":
                    self._current_status = "INACTIVE"

        # Undraws components
        if not self._initializing and self._current_status != self._status:
            self._bar.undraw()
            self._text.undraw()
            self._pointer.undraw()

            # Reset components
            self._bar, self._text, self._pointer = "N/A", "N/A", "N/A"

        # Update Text
        if self._window.last_key and self._current_status == "CLICKED":
            if self._window.last_key == "\n":
                if self._action != "SUBMITTED":
                    self._action = "SUBMITTED"
            else:
                if self._action != "NONE":
                    self._action = "NONE"
                if self._window.last_key == "\b":
                    if len(self.text) > 0:
                        self.text = self.text[:-1]
                else:
                    if len(self._window.last_key) == 1:
                        temp_text = Text(self._window,
                                         (self._point[0] + self.text_x_margin, self._point[1] + self.text_y_margin),
                                         self.text + self._window.last_key, self.font, self.font_size,
                                         color=self.font_color,
                                         bold=self.bold, italic=self.italic, inplace_draw=False)
                        if temp_text.width() <= self.length:
                            if self.force_case == "UPPER":
                                self.text += self._window.last_key.upper()
                            elif self.force_case == "LOWER":
                                self.text += self._window.last_key.lower()
                            else:
                                self.text += self._window.last_key

        # Update components
        # Inactive
        if self._current_status == "INACTIVE" and self._current_status != self._status:
            # Bar
            self._bar = Rectangle(self._window, self._point,
                                  (self._point[0] + self.length, self._point[1] + self.height), color=self.bar_color,
                                  outline_color=self.outline_color, outline_width=self.outline_width)
            # Text
            self._text = Text(self._window, (self._point[0] + self.text_x_margin, self._point[1] + self.text_y_margin),
                              self.text, self.font, self.font_size, color=self.font_color,
                              bold=self.bold, italic=self.italic)
            assert self._text.width() < self.length, "Text must be shorter than inputBox bar."
            # Pointer
            self._pointer = Line(self._window, (0, 0), (0, 0))

            self._status = self._current_status
        # Performance is affected when typing
        elif self._current_status == "CLICKED":
            if self._status == self._current_status:
                self._bar.undraw()
                self._text.undraw()
                self._pointer.undraw()

            # Bar
            self._bar = Rectangle(self._window, self._point,
                                  (self._point[0] + self.length, self._point[1] + self.height), color=self.bar_color,
                                  outline_color=self.outline_color, outline_width=self.outline_width)
            # Text
            self._text = Text(self._window, (self._point[0] + self.text_x_margin, self._point[1] + self.text_y_margin),
                              self.text, self.font, self.font_size, color=self.font_color,
                              bold=self.bold, italic=self.italic)
            assert self._text.width() < self.length, "Text must be shorter than inputBox bar."
            # Pointer
            if self._window.frame % self.pointer_blink_frames <= self.pointer_blink_frames // 2:
                self._pointer = Line(self._window, (
                    self._point[0] + self._text.width() + self.pointer_x_margin + self.text_x_margin,
                    self._point[1] + self.text_y_margin + self.pointer_y_margin), (
                                         self._point[
                                             0] + self._text.width() + self.pointer_x_margin + self.text_x_margin,
                                         self._point[1] + self.height - self.text_y_margin - self.pointer_y_margin),
                                     color=self.pointer_color,
                                     width=self.pointer_width)
            else:
                self._pointer = Line(self._window, (0, 0), (0, 0))

            self._status = self._current_status

        if self._initializing:
            self._initializing = False

    # Moves the inputBox
    def move(self, x=0, y=0):
        self._point = (self._point[0] + x, self._point[1] + y)

        self._set_boundaries()

    # Copies the inputBox
    def copy(self):
        return InputBox(self._window, self.point, length=self.length, height=self.height, text=self.text,
                        bar_color=self.bar_color,
                        outline_color=self.outline_color, outline_width=self.outline_width,
                        text_y_margin=self.text_y_margin,
                        text_x_margin=self.text_x_margin, font=self.font,
                        font_size=self.font_size, font_color=self.font_color, bold=self.bold, italic=self.italic,
                        pointer_width=self.pointer_width,
                        pointer_length=self.pointer_length, pointer_x_margin=self.pointer_x_margin,
                        pointer_y_margin=self.pointer_y_margin, pointer_blink_frames=self.pointer_blink_frames,
                        pointer_color=self.pointer_color)

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, point):
        self._point = point

        self._set_boundaries()
