class TwoPlayerGame:
   """
   An abstract template class to setup a two player game
   """
   def __init__(self, **kwargs):
      """
      Initializes the class; enable_undo_redo is a required
      keyword argument for any game
      """
      self._enable_undo_redo = kwargs.get('enable_undo_redo')

   def next_turn(self):
      """
      Gets next turn, returns true if the game is over
      """
      
         
   
   def _perform_move(self):
      pass
   
   def _undo_step(self):
      pass
   
   def _redo_step(self):
      pass
   