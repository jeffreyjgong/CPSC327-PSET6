from .Player import Player

class RandomPlayer(Player):
   """
   A class to represent a Random Player
   """

   def __init__(self, player_id):
      super().__init__(player_id)
   
   def get_player_move(self):
      return super().get_player_move()