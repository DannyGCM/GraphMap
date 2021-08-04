# Danny Garcia
# Window.py

# Modules
import pathlib
import tkinter as tk
import time

# Window Class
class Window:

    # Constructor
    def __init__(self, title="GraphMap Window", size=(400, 400),
    fullscreen=False, frame_cap=80, background=(60, 60, 60),
    icon=str(pathlib.Path(__file__).parent.resolve()) + "\icon.ico"):

        # Arguments
        self._title = title
        self._size = size
        self._fullscreen = fullscreen
        self._background = background
        self.frame_cap = frame_cap
        self._object_list = []
        self._icon = icon

        # Root generation
        self._root = tk.Tk()
        self._root.geometry(f"{self._size[0]}x{self._size[1]}")
        self._root.title(str(self._title))
        self._root.resizable(0, 0)

        # Makes window fullscreen
        if self._fullscreen: self._root.attributes("-fullscreen", True)

        # Sets defined icon
        self._root.iconbitmap(self._icon)

        # Root bind behaviours
        self._root.protocol("WM_DELETE_WINDOW", self.on_quit)
        self._root.bind_all("<Key>", self.on_key)
        self._root.bind_all("<Button-1>", self.on_button_1)
        self._root.bind_all("<Button-2>", self.on_button_2)
        self._root.bind_all("<Button-3>", self.on_button_3)
        self._root.bind("<Motion>", self.on_motion)

        # Window generation
        self._window = tk.Canvas(self._root, width=self._size[0],
        height=self._size[1], highlightthickness=0,
        bg=self.rgb_to_bit(self._background))
        self._window.pack()

        # Input record
        self._last_key = ""
        self._last_mouse = [0, 0, 0]
        self._last_motion = (0, 0)

        # Variables
        self._last_update = time.time()
        self.object_list = []
        self._running = True
        self._frame = 0

    # Class representation
    def __repr__(self):
        text = "<Window Object>\n"
        text += f"Title: {self._title}\n"
        text += f"Size: {self._size}\n"
        text += f"Frame_cap: {self.frame_cap}"
        return text

    # Class print behaviour
    def __str__(self): return self.__repr__()

    # Ticks root unit of time
    def tick(self): self._root.update()

    # Updates a frame, used as a unit of time
    def update(self):

        # Checks for complex objects
        for object_ in self.object_list:
            if type(object_) == tuple:
                object_[0].tick()

        # Regulates frame delay
        if self.frame_cap != -1:
            time_lapsed = time.time() - self._last_update

            if time_lapsed <= 1 / self.frame_cap:
                time.sleep((1 / self.frame_cap) - time_lapsed)
            self._last_update = time.time()

        # Updates window's data
        self._last_key = ""
        self._last_mouse = [0, 0, 0]

        self.tick()
        self._frame += 1

    # Quit behaviour
    def on_quit(self): self._running = False

    # Destroys the root
    def quit(self): self._root.destroy()

    # Key behaviour
    def on_key(self, event):
        self._last_key = event.char if len(event.char) == 1 else event.keysym

    # Mouse left click behaviour
    def on_button_1(self, event): self._last_mouse[0] = 1

    # Mouse middle click behaviour
    def on_button_2(self, event): self._last_mouse[1] = 1

    # Mouse right click behaviour
    def on_button_3(self, event): self._last_mouse[2] = 1

    # Mouse movement behaviour
    def on_motion(self, event): self._last_motion = (event.x, event.y)

    # Changes the application's icon
    def change_icon(self, path): self._root.iconbitmap(path)

    # Removes all drawn objects
    def clear(self):
        self._object_list = []
        self._window.delete("all")

    # Returns width of window in pixels
    def width(self): return self._size[0]

    # Returns height of window in pixels
    def height(self): return self._size[1]

    # Properties
    @property
    def window(self):
        return self._window

    @property
    def running(self):
        return self._running

    @property
    def title(self):
        return self._title

    @property
    def fullscreen(self):
        return self._fullscreen

    @property
    def background(self):
        return self._background

    @property
    def last_key(self):
        return self._last_key

    @property
    def last_mouse(self):
        return self._last_mouse

    @property
    def last_motion(self):
        return self._last_motion

    @property
    def last_update(self):
        return self._last_update

    @property
    def frame(self):
        return self._frame

    @property
    def size(self):
        return self._size

    @property
    def icon(self):
        return self._icon

    # Setters
    @background.setter
    def background(self, color):
        self._background = color
        self._window.configure(background=self.rgb_to_bit(color))

    @icon.setter
    def icon(self, path):
        self._icon = path
        self._root.iconbitmap(self._icon)

    # Converts rgb color to 64bit color
    @staticmethod
    def rgb_to_bit(color):
        return "#{:02X}{:02X}{:02X}".format(color[0], color[1], color[2])
