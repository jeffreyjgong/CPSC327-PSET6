class Position:
   """
   A class representing a position on the board
   """
   def __init__(self, r, c):
      self._r = r
      self._c = c
      self._h = 0

   def _get_r(self):
      return self._r
   
   r = property(fget=_get_r, doc='row number')
   
   def _get_c(self):
      return self._c
   
   c = property(fget=_get_c, doc='column number')
   
   def _get_h(self):
      return self._h
      
   def _set_h(self, val):
      self._h = val
         
   h = property(fget=_get_h, fset=_set_h, doc='height')
   
   def __str__(self):
      return '(' + str(self._r) + ',' + str(self._c) + ') h:' + str(self._h)
   
   def check_same_pos(self, pos2):
      if self.x == pos2.x and self.y == pos2.y:
         return True
      return False