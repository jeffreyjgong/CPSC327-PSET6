class Player:
   """
   An abstract class to represent a player of the game
   """
   
   def __init__(self, player_id, board):
      self._board = board
      self.player_id = player_id
      if (self.player_id == 0):
         self._color = "white"
         self._workers = ['A', 'B']
      else:
         self._color = "blue"
         self._workers = ['Y', 'Z']
      
   def _get_color(self):
      return self._color
   
   color = property(fget=_get_color, doc='player color')

   def _get_workers(self):
      return self._workers
   
   workers = property(fget=_get_workers, doc='player workers')

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
   
   def _get_valid_move_directions(self):
      """
      Returns a list of valid move directions
      """
      pass
   
   def _get_valid_build_directions(self):
      """
      Returns a list of valid move directions
      """
      pass