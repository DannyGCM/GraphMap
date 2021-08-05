# Danny Garcia
# Text.py

# Modules
from .Window import Window as Window
from .GraphicsPrimitive import GraphicsPrimitive as GraphicsPrimitive

# Text class (Primitive)
class Text(GraphicsPrimitive):

    # Constructor
    def __init__(self, window_name, point, text, font, size, color=(0, 0, 0),
    bold=False, italic=False, anchor="nw", inplace=True):

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

        # Draws inplace if desired
        self.draw() if inplace else None

    # Class representation
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
            self._item = self._window.window.create_text(self._point,
            fill=Window.rgb_to_bit(self._color), font=self._font + \
            f" {str(self._size)}" + ("", " italic")[self._italic] + \
            ("", " bold")[self._bold], text=self._text, anchor=self._anchor)
            self._window.object_list.append(self._item)
        else: print("Object already drawn.")

    # Moves the text
    def move(self, x=0, y=0):
        self._point = (self._point[0] + x, self._point[1] + y)

        if self.is_drawn():
            self.undraw()
            self.draw()

    # Copies the text
    def copy(self):
        return Text(self._window, self._point, self._text, self._font,
        self._size, color=self._color, bold=self._bold, italic=self._italic,
        anchor=self._anchor)

    # Returns width of text in pixels
    def width(self):
        return tk.font.Font(size=self._size, family=self._font,
        slant=("roman", "italic")[self._italic],
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
