from . import CommandWithUndo

class ExecuteMove(CommandWithUndo):
   """
   A class to execute a Santorini move
   """
   def __init__(self, worker, move_dir, build_dir):
      self._selected_worker = worker
      self._move_dir = move_dir
      self._build_dir = build_dir
      self._directional_opposites = {'nw': 'se', 'n': 's', 'ne': 'sw', 'w': 'e', 'e': 'w', 'sw': 'ne', 's': 'n', 'se': 'nw'}
      
   def execute(self, board):
      """Runs the required command"""
      board.move_worker(self._selected_worker, self._move_dir)
      board.build_from_worker(self._selected_worker, self._build_dir)
   
   def undo(self, board):
      """Undoes the command"""
      board.undo_build_from_worker(self._selected_worker, self._build_dir)
      board.move_worker(self._selected_worker, self._directional_opposites[self._move_dir])      