from .Player import Player

class HumanPlayer(Player):
   """
   A class to represent a Human Player
   """

   def __init__(self, player_id):
      super().__init__(player_id)
   
   def get_player_move(self):
      return super().get_player_move()