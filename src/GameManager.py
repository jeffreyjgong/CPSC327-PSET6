import sys

class GameManager:
   """
   A class to represent the Game CLI interface

   Attributes
   ----------
   TODO
   """
   def __init__(self):
      """
      Constructs the necessary attributes for the BankCLI object
      """
      self._whitePlayerType = "human"
      self._bluePlayerType = "human"
      self._enableUndoRedo = "off"
      self._enableScoreDisplay = "off"
   
   def run(self, params):
      """
      Executes the game loop
      """
      self._whitePlayerType = params[0]
      self._bluePlayerType = params[1]
      self._enableUndoRedo = params[2]
      self._enableScoreDisplay = params[3]

if __name__ == '__main__':
   allowedParams = [['human', 'heuristic', 'random'], ['human', 'heuristic', 'random'], ['on', 'off'], ['on', 'off']]

   # initially loaded with default values
   params = ['human', 'human', 'off', 'off']

   for i in range(1, len(sys.argv)):
      # check if valid
      if (sys.argv[i] not in allowedParams[i-1]):
         sys.exit("Invalid command line argument: " + sys.argv[i])
      
      # set param
      params[i-1] = sys.argv[i]
   
   # edge case
   if params[0] != 'human' and params[1] != 'human':
      print('Turning history off, as two computers are playing against each other.')
      params[2] = 'off'
   
   SantoriniCLI = GameManager()
   SantoriniCLI.run(params)