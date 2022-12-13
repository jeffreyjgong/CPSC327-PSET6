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
      self._build_choice = ''
      super().__init__(player_id, board)
   
   def select_worker(self):
      (worker_choice, move_choice, build_choice) = self.calculate_heuristic()
      self._worker_choice = worker_choice
      self._move_choice = move_choice
      self._build_choice =  build_choice
      return worker_choice

   def select_direction(self):
      return self._move_choice

   def select_build_direction(self):
      print(self._worker_choice + ',' + self._move_choice + ',' + self._build_choice)
      return self._build_choice
   
   def calculate_heuristic(self):
      pass
