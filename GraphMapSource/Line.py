# Danny Garcia
# Line.py

# Modules
from .Window import Window as Window
from .GraphicsPrimitive import GraphicsPrimitive as GraphicsPrimitive

# Line class (Primitive)
class Line(GraphicsPrimitive):

    # Constructor
    def __init__(self, window_name, point_a, point_b, color=(0, 0, 0),
    width=1, dash=(), inplace=True):

        # Arguments
        self._window = window_name
        self._point_a = point_a
        self._point_b = point_b
        self._color = color
        self._width = width
        self._dash = dash

        self._item = "N/A"

        # Draws inplace if desired
        self.draw() if inplace else None

    # Class representation
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
            self._item = self._window.window.create_line(self._point_a,
            self._point_b, fill=Window.rgb_to_bit(self._color),
            width=self._width, dash=self._dash)
            self._window.object_list.append(self._item)
        else: print("Object already drawn.")

    # Moves the line
    def move(self, x=0, y=0):
        self._point_a = (self._point_a[0] + x, self._point_a[1] + y)
        self._point_b = (self._point_b[0] + x, self._point_b[1] + y)

        if self.is_drawn():
            self.undraw()
            self.draw()

    # Copies the line
    def copy(self):
        return Line(self._window, self._point_a, self._point_b,
        color=self._color, width=self._width, dash=self._dash)

    # Returns the length of the line
    def length(self):
        return math.sqrt(((self._point_b[0] - self._point_a[0]) ** 2) +
        ((self._point_b[1] - self._point_a[1]) ** 2))

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
