import sys
from Game.Santorini import Santorini

class GameManager:
   """
   A class to represent the Game CLI interface
   """
   def __init__(self):
      """
      Constructs necessary attributes for GameManager
      """
      pass
   
   def run(self, params):
      """
      Executes the game loop
      """
      self._game = Santorini(white_player_type = params[0], blue_player_type = params[1], enable_undo_redo = params[2], enable_score_display = params[3])
      print(self._game._board)

      # next turn
      while(self._game.get_next_turn()):
         pass