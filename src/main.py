import sys
from GameManager import GameManager

allowed_params = [['human', 'heuristic', 'random'], ['human', 'heuristic', 'random'], ['on', 'off'], ['on', 'off']]

# initially loaded with default values
params = ['human', 'human', 'off', 'off']

for i in range(1, len(sys.argv)):
   # check if valid
   if (sys.argv[i] not in allowed_params[i-1]):
      sys.exit("Invalid command line argument: " + sys.argv[i])
   
   # set param
   params[i-1] = sys.argv[i]

# Turn history off if two computers
if params[0] != 'human' and params[1] != 'human':
   params[2] = 'off'

SantoriniCLI = GameManager()
SantoriniCLI.run(params)