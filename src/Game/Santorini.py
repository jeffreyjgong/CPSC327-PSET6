from .Board.Board import Board
from .Player.HeuristicPlayer import HeuristicPlayer
from .Player.HumanPlayer import HumanPlayer
from .Player.RandomPlayer import RandomPlayer
from .TwoPlayerGame import TwoPlayerGame

class Santorini(TwoPlayerGame):
   """
   A class to set up the Santorini Board game
   """
   def __init__(self, **kwargs):
      """
      Initializes the class
      """
      
      self._white_player_type = kwargs['white_player_type']
      self._blue_player_type = kwargs['blue_player_type']
      self._enable_score_display = kwargs['enable_score_display']
      self._board = Board()
      self._turn_number = 1
      self._white_id = 0
      self._blue_id = 1
      self._players = [None for _ in range(0,2)]

      self._initialize_player(self._white_player_type, self._white_id)
      self._initialize_player(self._blue_player_type, self._blue_id)
      
      self._cur_player_id = self._white_id

      # TODO: add history of commands

      super().__init__()
   
   def _perform_move(self):
      pass
   
   def _undo_step(self):
      pass
   
   def _redo_step(self):
      pass

   def _initialize_player(self, player_type, player_id):
      if (player_type == 'human'):
         self._players[player_id] = HumanPlayer(player_id)
      elif (self._blue_player_type == 'heuristic'):
         self._players[player_id] = HeuristicPlayer(player_id)
      else:
         self._players[player_id] = RandomPlayer(player_id)