from .Board.Board import Board
from .TwoPlayerGame import TwoPlayerGame
from .Player.PlayerFactory import PlayerFactory
from .Player.Player import Player
from .Score import Score
from .Moves.ExecuteMove import ExecuteMove

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
      self._white_id = 0
      self._blue_id = 1
      self._players = [Player(None, None) for _ in range(0,2)]
      self._player_factory = PlayerFactory()
      self._players[self._white_id] = self._player_factory.get_player(self._white_player_type, self._white_id, self._board)
      self._players[self._blue_id] = self._player_factory.get_player(self._blue_player_type, self._blue_id, self._board)

      super().__init__(**kwargs)
   

   def get_next_turn(self):
      cur_player = self._players[self._cur_player_id]
      turn_string = f'Turn: {self._turn_number}, {cur_player.color} ({cur_player.workers[0]}{cur_player.workers[1]})'

      if (self._enable_score_display == 'on'):
         cur_score = Score(self._board.height_score(self._cur_player_id), self._board.center_score(self._cur_player_id), self._board.distance_score(self._cur_player_id))

         turn_string += ', ' + str(cur_score)
      
      print(turn_string)
      
      return super().get_next_turn()


   def _perform_move(self):
      cur_player = self._players[self._cur_player_id]
      other_player = self._players[1 - self._cur_player_id]

      # check if other player has won (worker on lvl 3)
      if other_player.has_won():
         print(other_player.color + " has won")
         return False

      # check if curr player cannot move and build (other player wins)
      if len(cur_player.get_movable_workers()) == 0:
         print(other_player.color + " has won")
         return False

      worker_name = cur_player.select_worker(other_player)
      move_direction = cur_player.select_move_direction(worker_name, other_player)
      
      # move worker temporarily
      temp_move = ExecuteMove(worker_name, move_direction, None)
      temp_move.execute(self._board)

      # validate build direction with updated worker position
      build_direction = cur_player.select_build_direction(worker_name, other_player)

      # revert temporary move
      temp_move.undo(self._board)

      # build and execute command object, add it to history
      move = ExecuteMove(worker_name, move_direction, build_direction)
      move.execute(self._board)
      if self._enable_undo_redo == 'on':
         self._history_idx += 1 
         if len(self._history) == self._history_idx:
            self._history.append(move)
            self._history.append(None)
         else:
            self._history[self._history_idx] = move
            if len(self._history) == self._history_idx + 1:
               self._history.append(None)
            else:
               self._history[self._history_idx + 1] = None
      
      # print board
      print(self._board)
      
      return True