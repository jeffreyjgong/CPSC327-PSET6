from .Player import Player

class HumanPlayer(Player):
   """
   A class to represent a Human Player
   """

   def __init__(self, player_id, board):
      super().__init__(player_id, board)
   
   def select_worker(self, other_player):
      valid_worker_name = False
      worker_name = ''
      while(not valid_worker_name):
         worker_name = input(self._worker_prompt)
         if (worker_name not in self.workers and worker_name not in other_player.workers):
            print('Not a valid worker')
         elif (worker_name in other_player.workers):
            print('That is not your worker')
         else:
            # TODO: check if this is the right string to print
            if (not self._board.worker_has_possible_move_and_build(worker_name)):
               print('No possible moves for this worker')
            else:
               valid_worker_name = True
      return worker_name
   
   def select_move_direction(self, worker_name, other_player):
      valid_move_direction = False
      move_direction = ''
      while(not valid_move_direction):
         move_direction = input(self._move_prompt)
         if (not self._board.validate_direction(move_direction)):
            print('Not a valid direction')
         elif (not self._board.validate_move_direction(worker_name, move_direction)):
            print('Cannot move ' + move_direction)
         else:
            valid_move_direction = True
      return move_direction
   
   def select_build_direction(self, worker_name, other_player):
      valid_build_direction = False
      build_direction = ''
      while(not valid_build_direction):
         build_direction = input(self._direction_prompt)
         if (not self._board.validate_direction(build_direction)):
            print('Not a valid direction')
         elif (not self._board.validate_build_direction(worker_name, build_direction)):
            print('Cannot build ' + build_direction)
         else:
            valid_build_direction = True
      return build_direction