from .Player import Player

class HumanPlayer(Player):
   """
   A class to represent a Human Player
   """

   def __init__(self, player_id, board):
      super().__init__(player_id, board)
   
   def select_worker(self):
      return super().select_worker()
   
   def select_direction(self):
      return super().select_direction()
   
   def select_build_direction(self):
      return super().select_build_direction()