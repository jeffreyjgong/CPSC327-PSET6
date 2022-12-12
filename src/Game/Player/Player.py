class Player:
   """
   An abstract class to represent a player of the game
   """
   
   def __init__(self, player_id):
      self.player_id = player_id

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