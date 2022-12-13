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
      
      if self._enable_undo_redo == 'on':
         self._history = [None] #none maintained at end of current history for redo edge casing behavior
         self._history_idx = -1 #position of last performed command

   def get_next_turn(self):
      """
      Gets next turn from current player
      """
      if self._enable_undo_redo == 'on':
         history_choice = ''
         valid_choices = ['undo', 'redo', 'next']
         while(history_choice not in valid_choices):
            history_choice = input('undo, redo, or next\n')
         
         if (history_choice == 'next'):
            self._perform_move()
         elif (history_choice == 'undo'):
            self._undo_step()
         else:
            self._redo_step()
      else:
         self._perform_move()  
         
   def _perform_move(self):
      """
      Performs the move, exits if game is over
      """
      pass
   
   def _undo_step(self):
      """Returns true on success, false on failure"""
      if self._history_idx == -1:
         return False
      self._history[self._history_idx].undo(self._board)
      self._history_idx -= 1
      return True
   
   
   def _redo_step(self):
      """Returns true on success, false on failure"""
      if self._history[self._history_idx + 1] == None:
         return False
      self._history_idx += 1
      self._history[self._history_idx].execute(self._board)
      return True
   