class CommandWithUndo:
   """
   An abstract command class that supports undo
   """
   def execute(self):
      """Runs the required command"""
      raise NotImplementedError()
   
   def undo(self):
      """Undoes the command"""
      raise NotImplementedError()