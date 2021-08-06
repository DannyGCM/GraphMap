# Danny Garcia
# Button.py

# Modules
from .Text import Text as Text
from .Image import Image as Image
from .Rectangle import Rectangle as Rectangle
from .Window import Window as Window
import time

# Button class
class Button:

    # Constructor
    def __init__(self, window_name, point_a, point_b, box_color=(0, 0, 0),
    outline_color=(0, 0, 0), hovered_box_color=(40, 40, 40),
    hovered_outline_color=(40, 40, 40), clicked_box_color=(80, 80, 80),
    clicked_outline_color=(80, 80, 80), outline_width=0, text="", font="Times",
    font_size=20, font_color=(255, 255, 255),
    hovered_font_color=(210, 210, 210), clicked_font_color=(170, 170, 170),
    bold=False, italic=False, image_path="", hovered_image_path="",
    clicked_image_path="", inplace=True):

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
        self.draw() if inplace else None

    # Class representation
    def __repr__(self):
        text = "<Button Object>\n"
        text += f"Point A: {self._point_a}\n"
        text += f"Point B: {self._point_b}\n"
        return text

    # Class print behaviour
    def __str__(self): return self.__repr__()

    # Gets draw status of the button
    def is_drawn(self):
        return (self,) in self._window.object_list

    # Sets the button's boundaries
    def _set_boundaries(self):
        self._left_boundary = self._point_a[0] if self._point_a[0] < \
        self._point_b[0] else self._point_b[0]
        self._right_boundary = self._point_a[0] if self._point_a[0] > \
        self._point_b[0] else self._point_b[0]
        self._up_boundary = self._point_a[1] if self._point_a[1] > \
        self._point_b[1] else self._point_b[1]
        self._down_boundary = self._point_a[1] if self._point_a[1] < \
        self._point_b[1] else self._point_b[1]

    # Draws the button
    def draw(self):
        if not self.is_drawn(): self._window.object_list.append((self,))
        else: print("Object already drawn.")

    # Undraw the button
    def undraw(self):
        if self.is_drawn():
            self._window.window.delete(self._box, self._image, self._text)
            del self._window.object_list[
            self._window.object_list.index((self,))]
        else: print("Object isn't drawn.")

    # Updates the button
    def update(self):
        # Gives clicked button animation time to be displayed
        if self._status == "CLICKED":
            time.sleep(1 / 30)

        # Updates status
        if not (self._left_boundary < self._window.last_motion[0] < \
        self._right_boundary and self._up_boundary > \
        self._window.last_motion[1] > self._down_boundary):

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
        if self._current_status == "INACTIVE" and \
        self._current_status != self._status:

            # Box
            self._box = Rectangle(self._window, self._point_a, self._point_b,
            color=self.box_color, outline_color=self.outline_color,
            outline_width=self.outline_width)

            # Image
            self._image = Image(self._window, (self._point_a[0] + \
            (abs(self._point_a[0] - self._point_b[0]) // 2), self._point_a[1] \
            + (abs(self._point_a[1] - self._point_b[1]) // 2)),
            self.image_path, anchor_type="center")
            assert self._image.width() < abs(self._point_a[0] - \
            self._point_b[0]) and self._image.height() < abs(
            self._point_a[1] - self._point_b[1]), \
            "Image must be smaller than the button."

            # Text
            self._text = Text(self._window, (self._point_a[0] + \
            (abs(self._point_a[0] - self._point_b[0]) // 2), self._point_a[1] \
            + (abs(self._point_a[1] - self._point_b[1])) // 2), self.text,
            self.font, self.font_size, color=self.font_color,
            bold=self.bold, italic=self.italic, anchor="center")

            self._status = self._current_status

        # Hovered
        elif self._current_status == "HOVERED" and \
        self._current_status != self._status:

            # Box
            self._box = Rectangle(self._window, self._point_a, self._point_b,
            color=self.hovered_box_color, outline_color = \
            self.hovered_outline_color, outline_width=self.outline_width)

            # Image
            self._image = Image(self._window, (self._point_a[0] + \
            (abs(self._point_a[0] - self._point_b[0]) // 2),
            self._point_a[1] + (abs(self._point_a[1] - self._point_b[1]) // 2)),
            self.hovered_image_path, anchor_type="center")
            assert self._image.width() < abs(self._point_a[0] - \
            self._point_b[0]) and self._image.height() < abs(
            self._point_a[1] - self._point_b[1]), \
            "Image must be smaller than the button."

            # Text
            self._text = Text(self._window, (self._point_a[0] + \
            (abs(self._point_a[0] - self._point_b[0]) // 2), self._point_a[1] \
            + (abs(self._point_a[1] - self._point_b[1])) // 2), self.text,
            self.font, self.font_size, color=self.hovered_font_color,
            bold=self.bold, italic=self.italic, anchor="center")

            self._status = self._current_status

        # Clicked
        elif self._current_status == "CLICKED" and \
        self._current_status != self._status:

            # Box
            self._box = Rectangle(self._window, self._point_a, self._point_b,
            color=self.clicked_box_color, outline_color = \
            self.clicked_outline_color, outline_width=self.outline_width)

            # Image
            self._image = Image(self._window, (self._point_a[0] + \
            (abs(self._point_a[0] - self._point_b[0]) // 2), self._point_a[1] \
            + (abs(self._point_a[1] - self._point_b[1]) // 2)),
            self.clicked_image_path, anchor_type="center")
            assert self._image.width() < abs(self._point_a[0] - \
            self._point_b[0]) and self._image.height() < abs(
            self._point_a[1] - self._point_b[1]), \
            "Image must be smaller than the button."

            # Text
            self._text = Text(self._window, (self._point_a[0] + \
            (abs(self._point_a[0] - self._point_b[0]) // 2), self._point_a[1] \
            + (abs(self._point_a[1] - self._point_b[1])) // 2), self.text,
            self.font, self.font_size, color=self.clicked_font_color,
            bold=self.bold, italic=self.italic, anchor="center")

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
        return Button(self._window, self._point_a, self._point_b,
        box_color=self.box_color, outline_color=self.outline_color,
        hovered_box_color=self.hovered_box_color, hovered_outline_color = \
        self.hovered_outline_color, clicked_box_color=self.clicked_box_color,
        clicked_outline_color=self.clicked_outline_color, outline_width = \
        self.outline_width, text=self.text, font=self.font, font_size = \
        self.font_size, font_color=self.font_color, hovered_font_color = \
        self.hovered_font_color, clicked_font_color=self.clicked_font_color,
        bold=self.bold, italic=self.italic, image_path=self.image_path,
        hovered_image_path=self.hovered_image_path, clicked_image_path = \
        self.clicked_image_path)

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
