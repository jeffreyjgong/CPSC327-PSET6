from .Position import Position

class Board:
   """
   A class representing a Santorini board
   """
   def __init__(self):
      """
      Initializes board
         self._workers[p][w] represents the worker w for player p
          white is player 0, blue is player 1
         A and Y represent worker 0, B and Z represent worker 1
      """

      self._positions = [[Position(r, c) for c in range(0,5)] for r in range(0,5)]

      #setup workers
      self._worker_names = [['A', 'B'], ['Y', 'Z']]
      self._workers = [[None for _ in range(0,2)] for _ in range(0,2)]
      self._workers[0][0] = self._positions[1][3]
      self._workers[0][1] = self._positions[3][1]
      self._workers[1][0] = self._positions[1][1]
      self._workers[1][1] = self._positions[3][3]

      #setup variables for iterator
      self._curr_iter_idx = None
      self._iter_center_r = 0
      self._iter_center_c = 0

      # top down, left to right
      self._neighbor_offset = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

   def _set_iter_center(self, r, c):
      self._iter_center_r = r
      self._iter_center_c = c

   def __iter__(self):
      self._curr_iter_idx = 0
      return self

   def __next__(self):
      while self._curr_iter_idx < len(self._neighbor_offset):
         r = self._iter_center_r + self._neighbor_offset[self._curr_iter_idx][0]
         c = self._iter_center_c + self._neighbor_offset[self._curr_iter_idx][1]
         self._curr_iter_idx += 1
         if r >= 0 and r < 5 and c >= 0 and c < 5:
            return self._positions[r][c]
      raise StopIteration

   def __str__(self):
      board_str_lst = []
      for r in range(0,5):
         board_str_lst.append('+--+--+--+--+--+\n')
         for c in range(0,5):
            board_str_lst.append('|')
            board_str_lst.append(str(self._positions[r][c].h))
            has_worker = False
            for p in range(0,2):
               for w in range(0,2):
                  if self._workers[p][w].r == r and self._workers[p][w].c == c:
                     board_str_lst.append(self._worker_names[p][w])
                     has_worker = True
            if not has_worker:
               board_str_lst.append(' ')
         board_str_lst.append("|\n")
      board_str_lst.append('+--+--+--+--+--+\n')
      return "".join(board_str_lst)