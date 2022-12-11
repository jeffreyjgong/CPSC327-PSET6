import sys

class GameManager:
   """
   A class to represent the Game CLI interface

   Attributes
   ----------
   TBD
   """
   def __init__(self):
      """
      Constructs the necessary attributes for the BankCLI object
      """
   
   def run(self, params):
      """
      Executes the game loop
      """

if __name__ == '__main__':
   params = ['human', 'human', 'off', 'off']

   for i in range(1, len(sys.argv)):
      params[i-1] = sys.argv[i]
   
   if params[0] != 'human' and params[1] != 'human':
      print('Turning history off, as two computers are playing against each other.')
      params[2] = 'off'
   
   SantoriniCLI = GameManager()
   SantoriniCLI.run(params)