class Player:
   """
   An abstract class to represent a player of the game
   """
   
   def __init__(self, player_id, board):
      self._board = board
      self._player_id = player_id
      if (self._player_id == 0):
         self._color = "white"
         self._workers = ['A', 'B']
      else:
         self._color = "blue"
         self._workers = ['Y', 'Z']
      self._worker_prompt = 'Select a worker to move'
      self._move_prompt = 'Select a direction to move (n, ne, e, se, s, sw, w, nw)'
      self._direction_prompt = 'Select a direction to build (n, ne, e, se, s, sw, w, nw)'
      
   def _get_player_id(self):
      return self._player_id
   
   player_id = property(fget=_get_player_id, doc='player id')
      
   def _get_color(self):
      return self._color
   
   color = property(fget=_get_color, doc='player color')

   def _get_workers(self):
      return self._workers
   
   workers = property(fget=_get_workers, doc='player workers')

   def has_won(self):
      """
      Returns true if there is an l3 worker
      """
      for worker_name in self._workers:
         if self._board.get_worker_height(worker_name) == 3:
            return True
      return False
   
   def select_worker(self, other_player):
      """
      Returns which worker is moving
      """
      pass

   def select_move_direction(self, worker_name, other_player):
      """
      Returns which direction to move worker in
      """
      pass

   def select_build_direction(self, worker_name, other_player):
      """
      Returns the direction to build in
      """
      pass
   
   def get_movable_workers(self):
      """
      Returns a list of worker names for movable workers 
      """
      movable_workers = []
      for worker_name in self.workers:
         if self._board.worker_has_possible_move_and_build(worker_name):
            movable_workers.append(worker_name)
      return movable_workers 
   
   def _get_valid_move_directions(self, worker_name):
      """
      Returns a list of valid move directions
      """
      possible_directions = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
      valid_directions = []
      for dir in possible_directions:
         if not self._board.validate_direction(dir):
            continue
         if self._board.validate_move_direction(worker_name, dir):
            valid_directions.append(dir)
      return valid_directions
      
   def _get_valid_build_directions(self, worker_name):
      """
      Returns a list of valid build directions
      """
      possible_directions = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
      valid_directions = []
      for dir in possible_directions:
         if not self._board.validate_direction(dir):
            continue
         if self._board.validate_build_direction(worker_name, dir):
            valid_directions.append(dir)
      return valid_directions