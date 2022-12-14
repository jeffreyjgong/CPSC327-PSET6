class Score:
   """
   A class to keep track of scores easily
   """
   def __init__(self, height_score, center_score, distance_score):
      self.height_score = height_score
      self.center_score = center_score
      self.distance_score = distance_score
   
   def __str__(self):
      return f'({self.height_score}, {self.center_score}, {self.distance_score})'