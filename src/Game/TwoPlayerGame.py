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

   def get_next_turn(self):
      """
      Gets next turn from current player
      """
      pass
         
   def _perform_move(self):
      """
      Performs the move, exits if game is over
      """
      pass
   
   def _undo_step(self):
      """
      Undo the previous move
      """
      pass
   
   def _redo_step(self):
      """
      Reverts an undo
      """
      pass
   