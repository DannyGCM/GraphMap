# Danny Garcia
# Polygon.py

# Modules
from .Window import Window as Window
from .GraphicsPrimitive import GraphicsPrimitive as GraphicsPrimitive

# Polygon class (Primitive)
class Polygon(GraphicsPrimitive):

    # Constructor
    def __init__(self, window_name, points, color=(0, 0, 0),
    outline_color=(0, 0, 0), outline_width=0, inplace=True):

        # Arguments
        self._window = window_name
        self._points = list(points)
        self._color = color
        self._outline_color = outline_color
        self._outline_width = outline_width

        self._item = "N/A"

        # Draws inplace if desired
        self.draw() if inplace else None

    # Class representation
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
            self._item = self._window.window.create_polygon(self._points,
            fill=Window.rgb_to_bit(self._color),
            outline=Window.rgb_to_bit(self._outline_color),
            width=self._outline_width)
            self._window.object_list.append(self._item)
        else: print("Object already drawn.")

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
        return Polygon(self._window, self._points, color=self._color,
        outline_color=self._outline_color, outline_width=self._outline_width)

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
