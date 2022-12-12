from .Player import Player

class HumanPlayer(Player):
   """
   A class to represent a Human Player
   """

   def __init__(self, player_id, board):
      super().__init__(player_id, board)
   
   def select_worker(self):
      worker_name = input('Select a worker to move\n')
      return worker_name
   
   def select_direction(self):
      direction = input('Select a direction to move (n, ne, e, se, s, sw, w, nw)\n')
      return direction
   
   def select_build_direction(self):
      build_direction = input('Select a direction to build (n, ne, e, se, s, sw, w, nw)\n')
      return build_direction