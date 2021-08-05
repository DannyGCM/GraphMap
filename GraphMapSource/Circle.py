# Danny Garcia
# Circle.py

# Modules
from .Window import Window as Window
from .GraphicsPrimitive import GraphicsPrimitive as GraphicsPrimitive

# Circle class (Primitive)
class Circle(GraphicsPrimitive):

    # Constructor
    def __init__(self, window_name, point, radius=5, color=(0, 0, 0),
    outline_color=(0, 0, 0), outline_width=0, inplace_draw=True):

        # Arguments
        self._window = window_name
        self._point = point
        self._radius = radius
        self._color = color
        self._outline_color = outline_color
        self._outline_width = outline_width

        self._item = "N/A"

        # Draws inplace if desired
        self.draw() if inplace_draw else None

    # Class representation
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
            self._item = self._window.window.create_oval(self._point[0] - \
            self._radius, self._point[1] + self._radius, self._point[0] + \
            self._radius, self._point[1] - self._radius,
            fill=Window.rgb_to_bit(self._color), outline=Window.rgb_to_bit(
            self._outline_color), width=self._outline_width)
            self._window.object_list.append(self._item)
        else: print("Object already drawn.")

    # Moves the circle
    def move(self, x=0, y=0):
        self._point = (self._point[0] + x, self._point[1] + y)

        if self.is_drawn():
            self.undraw()
            self.draw()

    # Copies the circle
    def copy(self):
        return Circle(self._window, self._point, radius=self._radius,
        color=self._color, outline_color=self._outline_color,
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
