class Santorini :
   """
   An abstract template class to setup a two player game
   """
   def __init__(self, **kwargs):
      """
      Initializes the class
      """
      
      self._white_player_type = kwargs['white_player_type']
      self._blue_player_type = kwargs['blue_player_type']
      self._enable_score_display = kwargs['enable_score_display']
      super().__init__()
   
   def _perform_move(self):
      pass
   
   def _undo_step(self):
      pass
   
   def _redo_step(self):
      pass
   