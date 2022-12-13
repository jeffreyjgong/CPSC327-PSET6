from .Player import Player
import random

class RandomPlayer(Player):
   """
   A class to represent a Random Player
   """

   def __init__(self, player_id, board):
      super().__init__(player_id, board)
   
   def select_worker(self, other_player):
      """
      Returns which worker is moving
      """
      print(self._worker_prompt)
      worker_choice = random.choice(self.get_movable_workers())
      print(worker_choice)
      return worker_choice
   
   def select_move_direction(self, worker_name, other_player):
      """
      Returns which direction to move worker in
      """
      print(self._move_prompt)
      move_choice = random.choice(self._get_valid_move_directions(worker_name))
      print(move_choice)
      return move_choice

   def select_build_direction(self, worker_name, other_player):
      """
      Returns the direction to build in
      """
      print(self._direction_prompt)
      direction_choice = random.choice(self._get_valid_build_directions(worker_name))
      print(direction_choice)
      return direction_choice
