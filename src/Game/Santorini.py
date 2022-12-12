from .Board.Board import Board
from .TwoPlayerGame import TwoPlayerGame
from .Player.PlayerFactory import PlayerFactory
from .Player.Player import Player
from .Score import Score

class Santorini(TwoPlayerGame):
   """
   A class to set up the Santorini Board game
   """
   def __init__(self, **kwargs):
      """
      Initializes the class
      """
      
      self._white_player_type = kwargs.get('white_player_type')
      self._blue_player_type = kwargs.get('blue_player_type')
      self._enable_score_display = kwargs.get('enable_score_display')
      self._board = Board()
      self._turn_number = 1
      self._white_id = 0
      self._blue_id = 1
      self._players = [Player(None, None) for _ in range(0,2)]
      self._player_factory = PlayerFactory()
      self._players[self._white_id] = self._player_factory.get_player(self._white_player_type, self._white_id, self._board)
      self._players[self._blue_id] = self._player_factory.get_player(self._blue_player_type, self._blue_id, self._board)
      
      self._cur_player_id = self._white_id

      # TODO: add history of commands

      super().__init__(**kwargs)
   
   def get_next_turn(self):
      cur_player = self._players[self._cur_player_id]
      turn_string = f'Turn: {self._turn_number}, {cur_player.color} ({cur_player.workers[0]}{cur_player.workers[1]})'

      if (self._enable_score_display == 'on'):
         # TODO: calculate score
         cur_score = Score(-1, -1, -1)

         turn_string += ', ' + str(cur_score)
      
      print(turn_string)
      
      if (self._enable_undo_redo == 'on'):
         history_choice = ''
         valid_choices = ['undo', 'redo', 'next']
         while(history_choice not in valid_choices):
            history_choice = input('undo, redo, or next\n')
         
         if (history_choice == 'next'):
            self._perform_move()
         elif (history_choice == 'undo'):
            self._undo_step()
         else:
            self._redo_step()
      else:
         self._perform_move()  


   def _perform_move(self):
      cur_player = self._players[self._cur_player_id]

      # check if other player has won (worker on lvl 3)

      # check if cur player cannot move and build (other player wins)

      # validate worker name
      valid_worker_name = False
      worker_name = ''
      while(not valid_worker_name):
         worker_name = cur_player.select_worker()
         if (worker_name not in self._players[0].workers and worker_name not in self._players[1].workers):
            print('Not a valid worker')
         elif (worker_name in self._players[1-self._cur_player_id]):
            print('That is not your worker')
         else:
            # TODO: check if this is the right string to print
            if (not self._board.worker_has_possible_move_and_build(worker_name)):
               print('No possible moves for this worker')
            else:
               valid_worker_name = True

      # validate move direction
      valid_move_direction = False
      move_direction = ''
      
      while(not valid_move_direction):
         move_direction = cur_player.select_direction()
         if (move_direction not in self._board.directions):
            print('Not a valid direction')
         elif (not self._board.validate_move_direction(worker_name, move_direction)):
            print('Cannot move ' + move_direction)
         else:
            valid_move_direction = True
      
      # move worker temporarily
      self._board.move_worker(worker_name, move_direction)

      # validate build direction with updated worker position
      valid_build_direction = False
      build_direction = ''

      while(not valid_build_direction):
         build_direction = cur_player.select_build_direction()
         if (build_direction not in self._board.directions):
            print('Not a valid direction')
         elif (not self._board.validate_build_direction(worker_name, build_direction)):
            print('Cannot build ' + build_direction)
         else:
            valid_build_direction = True

      # revert temporary move
      self._board.move_worker(worker_name, self._board.directional_opposites[move_direction])

      # build command object
      
      # execute command

      # add command object to history

      # add to turn
      self._turn_number += 1

      # switch players
      self._cur_player_id = 1 - self._cur_player_id
      
   
   def _undo_step(self):
      pass
   
   def _redo_step(self):
      pass