import sys
from .Player import Player
from ..Moves.ExecuteMove import ExecuteMove
import random

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
   
   def select_worker(self, other_player):
      (worker_choice, move_choice, build_choice) = self.calculate_heuristic()
      self._worker_choice = worker_choice
      self._move_choice = move_choice
      self._build_choice =  build_choice
      return worker_choice

   def select_move_direction(self, worker_name, other_player):
      return self._move_choice

   def select_build_direction(self, worker_name, other_player):
      print(self._worker_choice + ',' + self._move_choice + ',' + self._build_choice)
      return self._build_choice
   
   def calculate_heuristic(self):
      movable_workers = self.get_movable_workers()

      # (move_score, worker_name, move_direction)
      possible_moves = []

      for worker_name in movable_workers:
         move_list = self._get_valid_move_directions(worker_name)
         for move_direction in move_list:
            temp_move = ExecuteMove(worker_name, move_direction, None)
            temp_move.execute(self._board)
            move_score = 0
            if (len(self._get_valid_build_directions(worker_name)) > 0):
               if (self._board.get_worker_height(worker_name) == 3):
                  move_score = -1
               else:
                  move_score = self._height_weight * self._board.height_score(self._player_id) + self._center_weight * self._board.center_score(self._player_id) + self._distance_weight * self._board.distance_score(self._player_id)
               res = (move_score, worker_name, move_direction)
               possible_moves.append(res)
            temp_move.undo(self._board)
      
      possible_moves.sort(key=lambda a: a[0])

      if (len(possible_moves) == 0):
         other_color = 'blue' if self._color == 'white' else 'white'
         sys.exit(other_color + ' has won')
      elif (possible_moves[0][0] == -1):
         temp_move = ExecuteMove(possible_moves[0][1], possible_moves[0][2], None)
         temp_move.execute(self._board)
         build_direction = random.choice(self._get_valid_build_directions(possible_moves[0][1]))
         temp_move.undo(self._board)
         ans = (possible_moves[0][1], possible_moves[0][2], build_direction)
         return ans
      else:
         max_el = len(possible_moves) - 1
         temp_move = ExecuteMove(possible_moves[max_el][1], possible_moves[max_el][2], None)
         temp_move.execute(self._board)
         build_direction = random.choice(self._get_valid_build_directions(possible_moves[max_el][1]))
         temp_move.undo(self._board)
         ans = (possible_moves[max_el][1], possible_moves[max_el][2], build_direction)
         return ans

