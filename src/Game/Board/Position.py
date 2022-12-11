class Position:
   """
   A class representing a position on the board
   """
   def __init__(self, x, y):
      self._x = x
      self._y = y
      self._h = 0

   def _get_x(self):
      return self._x
   
   x = property(fget=_get_x, doc="x coordinate")
   
   def _get_y(self):
      return self._y
   
   y = property(fget=_get_y, doc="y coordinate")
   
   def _get_h(self):
      return self._h
      
   def _set_h(self, val):
      self._h = val
         
   h = property(fget=_get_h, fset=_set_h, doc="height")
   
   def __str__(self):
      return "(" + str(self._x) + "," + str(self._y) + ") h:" + str(self._h)