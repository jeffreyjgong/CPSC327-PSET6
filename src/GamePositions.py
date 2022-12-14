from Position import Position

class GamePositions:
   """
   A class representing a 5x5 grid of positions
   Has iterator to return valid neighboring positions to a specified tile
   """
   def __init__(self):
      """
      Initializes positions
      """

      self._neighbor_offset = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
      self.pos_arr = [[Position(r, c) for c in range(0,5)] for r in range(0,5)]

   def set_iter_center(self, r, c):
      self._iter_center_r = r
      self._iter_center_c = c

   def __iter__(self):
      self._curr_iter_idx = 0
      return self

   def __next__(self):
      """Only returns valid neighboring positions"""
      
      while self._curr_iter_idx < len(self._neighbor_offset):
         r = self._iter_center_r + self._neighbor_offset[self._curr_iter_idx][0]
         c = self._iter_center_c + self._neighbor_offset[self._curr_iter_idx][1]
         self._curr_iter_idx += 1
         if r >= 0 and r < 5 and c >= 0 and c < 5:
            return self.pos_arr[r][c]
      raise StopIteration