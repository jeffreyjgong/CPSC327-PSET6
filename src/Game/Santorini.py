from .Board.Board import Board
from .TwoPlayerGame import TwoPlayerGame
from .Player.PlayerFactory import PlayerFactory

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
      self._player_factory = PlayerFactory()

      self._players[self._white_id] = self._player_factory.get_player(self._white_player_type, self._white_id, self._board)
      self._players[self._blue_id] = self._player_factory.get_player(self._blue_player_type, self._blue_id, self._board)
      
      self._cur_player_id = self._white_id

      # TODO: add history of commands

      super().__init__()
   
   def _perform_move(self):
      pass
   
   def _undo_step(self):
      pass
   
   def _redo_step(self):
      pass