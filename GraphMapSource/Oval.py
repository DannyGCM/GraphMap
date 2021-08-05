# Danny Garcia
# Oval.py

# Modules
from .Window import Window as Window
from .GraphicsPrimitive import GraphicsPrimitive as GraphicsPrimitive

# Oval class (Primitive)
class Oval(GraphicsPrimitive):

    # Constructor
    def __init__(self, window_name, point_a, point_b, color=(0, 0, 0),
    outline_color=(0, 0, 0), outline_width=0, inplace=True):

        # Arguments
        self._window = window_name
        self._point_a = point_a
        self._point_b = point_b
        self._color = color
        self._outline_color = outline_color
        self._outline_width = outline_width

        self._item = "N/A"

        # Draws inplace if desired
        self.draw() if inplace else None

    # Class representation
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
            self._item = self._window.window.create_oval(self._point_a,
            self._point_b, fill=Window.rgb_to_bit(self._color),
            outline=Window.rgb_to_bit(self._outline_color),
            width=self._outline_width)
            self._window.object_list.append(self._item)
        else: print("Object already drawn.")

    # Moves the oval
    def move(self, x=0, y=0):
        self._point_a = (self._point_a[0] + x, self._point_a[1] + y)
        self._point_b = (self._point_b[0] + x, self._point_b[1] + y)

        if self.is_drawn():
            self.undraw()
            self.draw()

    # Copies the oval
    def copy(self):
        return Oval(self._window, self._point_a, self._point_b,
        color=self._color, outline_color=self._outline_color,
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
