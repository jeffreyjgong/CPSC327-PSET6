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
      self._direction_dict = {'nw': [-1,-1], 'n': [-1,0], 'ne': [-1,1], 'w': [0,-1], 'e': [0,1], 'sw': [1,-1], 's': [1,0], 'se': [1,1]}
      
   def validate_direction(self, dir):
      """
      Checks if inputed direction is valid
      """
      if dir in self._direction_dict.keys():
         return True
      return False
   
   def get_worker_height(self, worker_name):
      """
      Returns a worker to height dictionary
      """
      return self._workers[worker_name]

   def _is_valid_and_free_loc(self, r, c):
      """
         Checks if a position on the board is both valid and free
      """
      #check if out of bounds or if it contains a dome
      if r < 0 or r >= 5 or c < 0 or c > 5 or self._positions[r][c].h == 4:
         return False
      
      #See if a worker is occupying that tile
      for worker_name in self._workers.keys():
         if self._positions[r][c].check_same_pos(self._workers[worker_name]):
            return False
      return True
      
   def validate_build_direction(self, worker_name, direction):
      """
      Checks if the build direction for the specified worker is valid
      """
      r = self._workers[worker_name].r + self._direction_dict[direction][0]
      c = self._workers[worker_name].c + self._direction_dict[direction][1]
      return self._is_valid_and_free_loc(r,c)
      
   def validate_move_direction(self, worker_name, direction):
      """
      Checks if the move direction for the specified worker is valid
      """
      r = self._workers[worker_name].r + self._direction_dict[direction][0]
      c = self._workers[worker_name].c + self._direction_dict[direction][1]
      if not self._is_valid_and_free_loc(r,c):
         return False
      
      #worker's height can increase by a max of 1
      if self._positions[r][c].h - self._workers[worker_name].h > 1:
         return False
      
      return True
      
   def move_worker(self, worker_name, direction):
      """
      Moves the specified worker
      """
      self._workers[worker_name] = self._positions[self._workers[worker_name].r + self._direction_dict[direction][0]][self._workers[worker_name].c + self._direction_dict[direction][1]]

   def build_from_worker(self, worker_name, direction):
      """
      Builds from the specified worker
      """
      self._positions[self._workers[worker_name].r + self._direction_dict[direction][0]][self._workers[worker_name].c + self._direction_dict[direction][1]].h += 1
   
   def undo_build_from_worker(self, worker_name, direction):
      """
      Undoes build from the specified worker
      """
      self._positions[self._workers[worker_name].r + self._direction_dict[direction][0]][self._workers[worker_name].c + self._direction_dict[direction][1]].h -= 1

   def worker_has_possible_move_and_build(self, worker_name):
      """
      Checks if the specified worker has a possible move and build
      """
      for move_dir in self._direction_dict.keys():
         #check if valid move direction
         if self.validate_move_direction(worker_name, move_dir):
            #temporarily move worker to valid move direction
            self._workers[worker_name] = self._positions[self._workers[worker_name].r + self._direction_dict[move_dir][0]][self._workers[worker_name].c + self._direction_dict[move_dir][1]]
            #check if valid build direction
            for build_dir in self._direction_dict.keys():
               if self.validate_build_direction(worker_name, build_dir):
                  #undo temporary move
                  self._workers[worker_name] = self._positions[self._workers[worker_name].r - self._direction_dict[move_dir][0]][self._workers[worker_name].c - self._direction_dict[move_dir][1]]
                  return True
      #undo temporary move
      self._workers[worker_name] = self._positions[self._workers[worker_name].r - self._direction_dict[move_dir][0]][self._workers[worker_name].c - self._direction_dict[move_dir][1]]
      return False

   def set_iter_center(self, r, c):
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