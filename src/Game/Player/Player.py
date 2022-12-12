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

   def select_worker(self):
      """
      Returns which worker is moving
      """
      pass

   def select_direction(self):
      """
      Returns which direction to move worker in
      """
      pass

   def select_build_direction(self):
      """
      Returns the direction to build in
      """
      pass