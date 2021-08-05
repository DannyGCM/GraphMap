# Danny Garcia
# GraphicsPrimitive.py

# Parent class for primitives
class GraphicsPrimitive:

    # Class print behaviour
    def __str__(self): return self.__repr__()

    # Returns object's draw status
    def is_drawn(self):
        return self._item in self._window.object_list

    # Undraws the object
    def undraw(self):
        if self.is_drawn():
            self._window.window.delete(self._item)
            del self._window.object_list[
            self._window.object_list.index(self._item)]
        else: print("Object isn't drawn.")
