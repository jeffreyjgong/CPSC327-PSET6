from Game.Board.Board import Board

def test_board_iterator_corner_upper_left():
   b = Board()
   b._set_iter_center(0,0)

   correct_positions = [[0,1],[1,0],[1,1]]
   correct_num = 0

   for i,p in enumerate(b):
      assert p.r == correct_positions[i][0]
      assert p.c == correct_positions[i][1]
      correct_num += 1
   
   assert correct_num == 3

def test_board_iterator_corner_upper_right():
   b = Board()
   b._set_iter_center(0,4)

   correct_positions = [[0,3],[1,3],[1,4]]
   correct_num = 0

   for i,p in enumerate(b):
      assert p.r == correct_positions[i][0]
      assert p.c == correct_positions[i][1]
      correct_num += 1
   
   assert correct_num == 3

def test_board_iterator_corner_lower_left():
   b = Board()
   b._set_iter_center(4,0)

   correct_positions = [[3,0],[3,1],[4,1]]
   correct_num = 0

   for i,p in enumerate(b):
      assert p.r == correct_positions[i][0]
      assert p.c == correct_positions[i][1]
      correct_num += 1
   
   assert correct_num == 3

def test_board_iterator_corner_lower_right():
   b = Board()
   b._set_iter_center(4,4)

   correct_positions = [[3,3],[3,4],[4,3]]
   correct_num = 0

   for i,p in enumerate(b):
      assert p.r == correct_positions[i][0]
      assert p.c == correct_positions[i][1]
      correct_num += 1
   
   assert correct_num == 3

def test_board_iterator_middle():
   b = Board()
   b._set_iter_center(2,3)

   correct_positions = [[1,2],[1,3],[1,4],[2,2],[2,4],[3,2],[3,3],[3,4]]
   correct_num = 0

   for i,p in enumerate(b):
      assert p.r == correct_positions[i][0]
      assert p.c == correct_positions[i][1]
      correct_num += 1
   
   assert correct_num == 8
