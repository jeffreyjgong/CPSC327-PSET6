from .Player import Player

class HeuristicPlayer(Player):
   """
   A class to represent a Heuristic Player
   """

   def __init__(self, player_id, board):
      self._height_weight = 3
      self._center_weight = 2
      self._distance_weight = 1
      self._worker_choice = ''
      self._move_choice = ''
      super().__init__(player_id, board)
   
   def select_worker(self):
      worker_choice = ''
      self._worker_choice = worker_choice
      return worker_choice

   def select_direction(self):
      move_choice = ''
      self._move_choice = move_choice
      return move_choice

   def select_build_direction(self):
      build_choice = ''
      print(self._worker_choice + ',' + self._move_choice + ',' + build_choice)
      return build_choice