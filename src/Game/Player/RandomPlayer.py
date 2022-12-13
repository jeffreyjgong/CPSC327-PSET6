from .Player import Player
from random import random

class RandomPlayer(Player):
   """
   A class to represent a Random Player
   """

   def __init__(self, player_id, board):
      super().__init__(player_id, board)
   
   def select_worker(self):
      #Find valid workers
      movable_workers = []
      for worker_name in self._players[self._cur_player_id].workers:
         if self._board.worker_has_possible_move_and_build(worker_name):
            movable_workers += 1
      if movable_workers == 0:
         print(self._players[1 - self._cur_player_id].color + " has won")
      return super().select_worker()
   
   def select_direction(self):
      return super().select_direction()
   
   def select_build_direction(self):
      return super().select_build_direction()