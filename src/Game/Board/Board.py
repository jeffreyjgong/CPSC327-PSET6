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
      self._workers = {}
      self._workers['A'] = self._positions[3][1]
      self._workers['B'] = self._positions[1][3]
      self._workers['Y'] = self._positions[1][1]
      self._workers['Z'] = self._positions[3][3]

      #setup variables for iterator
      self._curr_iter_idx = None
      self._iter_center_r = 0
      self._iter_center_c = 0

      # top down, left to right
      self._neighbor_offset = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

      # directions to position offsets
      self._direction_dict = {'nw': [-1,-1], 'n': [0,-1], 'ne': [1,-1], 'w': [-1,0], 'e': [1,0], 'sw': [-1,1], 's': [0,1], 'se': [1,1]}
      
   def validate_direction(self, dir):
      """
      Checks if inputed direction is valid
      """
      if dir in self._direction_dict.keys():
         return True
      return False
      
   def validate_move_direction(self, worker_name, direction):
      """
      Checks if the move direction for the specified worker is valid
      """
      move_tile = Position(self._workers[worker_name].r + self._direction_dict[direction][0],self._workers[worker_name].c + self._direction_dict[direction][1])
      
      #check if out of bounds or if it contains a dome
      if move_tile.r < 0 or move_tile.r >= 5 or move_tile.c < 0 or move_tile.c > 5 or move_tile.h == 4:
         return False
      
      #See if a worker is occupying that tile
      for worker_name in self._workers.keys():
         if move_tile.check_same_pos(self._workers[worker_name]):
            return False
      return True

   def validate_build_direction(self, worker_name, direction):
      """
      Checks if the build direction for the specified worker is valid
      """
      build_tile = Position(self._workers[worker_name].r + self._direction_dict[direction][0],self._workers[worker_name].c + self._direction_dict[direction][1])
      if build_tile.h == 4:
         return False
      return True
      
      
   def move_worker(self, worker_name, direction):
      """
      Moves the specified worker
      """
      pass

   def build_from_worker(self, worker_name, build_direction):
      """
      Builds from the specified worker
      """
      pass
   
   def undo_build_from_worker(self, worker_name, build_direction):
      """
      Undoes build from the specified worker
      """
      pass

   def worker_has_possible_move_and_build(self, worker_name):
      """
      Checks if the specified worker has a possible move and build
      """
      valid_move_dir = False
      for dir in self._direction_dict.keys():
         if self.validate_move_direction(worker_name, dir):
            valid_move_dir = True
      if valid_move_dir == False:
         return False
      
      valid_build_dir = False
      for dir in self._direction_dict.keys():
         if self.validate_build_direction(worker_name, dir):
            valid_build_dir = True
      if valid_build_dir == False:
         return False
      
      return True

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
                  worker_name = self._worker_names[p][w]
                  if self._workers[worker_name].r == r and self._workers[worker_name].c == c:
                     board_str_lst.append(worker_name)
                     has_worker = True
            if not has_worker:
               board_str_lst.append(' ')
         board_str_lst.append('|\n')
      board_str_lst.append('+--+--+--+--+--+\n')
      return ''.join(board_str_lst)