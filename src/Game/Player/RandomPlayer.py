from .Player import Player

class RandomPlayer(Player):
   """
   A class to represent a Random Player
   """

   def __init__(self, player_id):
      super().__init__(player_id)
   
   def select_worker(self):
      return super().select_worker()
   
   def select_direction(self):
      return super().select_direction()
   
   def select_build_direction(self):
      return super().select_build_direction()