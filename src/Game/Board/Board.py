from Position import Position

class Board:
   """
   A class representing a Santorini board
   """
   def __init__(self):
      """Initializes boar
         self._workers[p][w] represents the worker w for player p
          white is player 0, blue is player 1
         A and Y represent worker 0, B and Z represent worker 1"""
      self._positions = [[Position(x, y) for x in range(0,5)] for y in range(0,5)]
      #setup workers
      self._worker_names = [['A', 'B'], ['Y', 'Z']]
      self._workers = [[None for x in range(0,2)] for y in range(0,2)]
      self._workers[0][0] = self._positions[1][3]
      self._workers[0][1] = self._positions[3][1]
      self._workers[1][0] = self._positions[1][1]
      self._workers[1][1] = self._positions[3][3]
      #setup variables for iterator
      self._curr_iter_idx = None
      self._iter_center_x = 0
      self._iter_center_y = 0
      self._neighbor_offset = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]

   def _set_iter_center(self, x, y):
      self._iter_center_x = x
      self._iter_center_y = y

   def __iter__(self):
      self._curr_iter_idx = 0
      return self

   def __next__(self):
      while self._curr_iter_idx < len(self._neighbor_offset):
         x = self._iter_center_x + self._neighbor_offset[self._curr_iter_idx][0]
         y = self._iter_center_y + self._neighbor_offset[self._curr_iter_idx][1]
         self._curr_iter_idx += 1
         if x >= 0 and x < 5 and y >= 0 and y < 5:
            return self._positions[x][y]
      raise StopIteration

   def __str__(self):
      board_str_lst = []
      for x in range(0,5):
         board_str_lst.append('+--+--+--+--+--+\n')
         for y in range(0,5):
            board_str_lst.append('|')
            board_str_lst.append(str(self._positions[x][y].h))
            has_worker = False
            for p in range(0,2):
               for w in range(0,2):
                  if self._workers[p][w].x == x and self._workers[p][w].y == y:
                     board_str_lst.append(self._worker_names[p][w])
                     has_worker = True
            if not has_worker:
               board_str_lst.append(' ')
         board_str_lst.append("|\n")
      board_str_lst.append('+--+--+--+--+--+\n')
      return "".join(board_str_lst)
      
if __name__ == '__main__':
  b = Board()
  b._set_iter_center(4,4)
  for pos in b:
     print(pos)