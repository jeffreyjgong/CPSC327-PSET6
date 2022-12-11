import sys
from Game import Santorini

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
      while self._game.next_turn():
         pass
      

if __name__ == '__main__':
   allowed_params = [['human', 'heuristic', 'random'], ['human', 'heuristic', 'random'], ['on', 'off'], ['on', 'off']]

   # initially loaded with default values
   params = ['human', 'human', 'off', 'off']

   for i in range(1, len(sys.argv)):
      # check if valid
      if (sys.argv[i] not in allowed_params[i-1]):
         sys.exit("Invalid command line argument: " + sys.argv[i])
      
      # set param
      params[i-1] = sys.argv[i]
   
   # edge case
   if params[0] != 'human' and params[1] != 'human':
      print('Turning history off, as two computers are playing against each other.')
      params[2] = 'off'
   
   SantoriniCLI = GameManager()
   SantoriniCLI.run(params)