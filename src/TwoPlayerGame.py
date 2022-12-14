class TwoPlayerGame:
   """
   An abstract template class to setup a two player game: supports undo/redo functionality
   """
   def __init__(self, **kwargs):
      """
      Initializes the class; enable_undo_redo is a required
      keyword argument for any game
      """
      self._cur_player_id = 0
      self._turn_number = 1

      self._enable_undo_redo = kwargs.get('enable_undo_redo')
      
      if self._enable_undo_redo == 'on':
         self._history = [None] #none maintained at end of current history for redo edge casing behavior
         self._history_idx = -1 #position of last performed command

   def get_next_turn(self):
      """
      Gets next turn from current player
      Returns false is game is over
      """
      if self._enable_undo_redo == 'on':
         history_choice = ''
         valid_choices = ['undo', 'redo', 'next']
         while(history_choice not in valid_choices):
            history_choice = input('undo, redo, or next\n')
         
         if (history_choice == 'next'):
            if not self._perform_move():
               return False
         elif (history_choice == 'undo'):
            if (not self._undo_step()):
               return True
            else:
               self._turn_number -= 1
               self._cur_player_id = 1 - self._cur_player_id
               return True
         else:
            if (not self._redo_step()):
               return True
            else:
               self._turn_number += 1
               self._cur_player_id = 1 - self._cur_player_id
               return True
      else:
         if not self._perform_move():
            self._cur_player_id = 1 - self._cur_player_id
            self._turn_number += 1
            return False
      self._turn_number += 1
      self._cur_player_id = 1 - self._cur_player_id
      return True
         
   def _perform_move(self):
      """
      Performs the move, returns False if game is over
      """
      pass
   
   def _undo_step(self):
      """Returns true on success, false on failure"""
      if self._history_idx == -1:
         print(self._board)
         return False
      self._history[self._history_idx].undo(self._board)
      self._history_idx -= 1
      print(self._board)
      return True
   
   
   def _redo_step(self):
      """Returns true on success, false on failure"""
      if self._history[self._history_idx + 1] == None:
         print(self._board)
         return False
      self._history_idx += 1
      self._history[self._history_idx].execute(self._board)
      print(self._board)
      return True
   