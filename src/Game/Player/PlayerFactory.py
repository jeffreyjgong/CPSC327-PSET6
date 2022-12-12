from .HumanPlayer import HumanPlayer
from .HeuristicPlayer import HeuristicPlayer
from .RandomPlayer import RandomPlayer

class PlayerFactory:
   def get_player(player_type, player_id, board):
      if (player_type == 'human'):
         return HumanPlayer(player_id, board)
      elif (player_type == 'heuristic'):
         return HeuristicPlayer(player_id, board)
      else:
         return RandomPlayer(player_id, board)