class Submarine():
  def __init__(self) -> None:
      self.depth = 0
      self.horisontal = 0
      self.aim = 0

  def change_horisontal(self,n):
    self.horisontal += n
    self.depth += self.aim*n
  
  def change_depth(self,n):
    self.depth += n

  def change_aim(self,n):
    self.aim += n
  
  def parse_moves(self,moves):
    moves = [(x.split(" ")[0],int(x.split(" ")[1])) for x in moves]
    for move in moves:
      if move[0] == "up":
        self.change_aim(-move[1])
      if move[0] == "down":
        self.change_aim(move[1])
      if move[0] == "forward":
        self.change_horisontal(move[1])
    
  def print_position(self):
    print("Depth: ",self.depth)
    print("Horisontal:",self.horisontal)
    print("Combined",self.depth*self.horisontal)


moves = []
with open("day2.txt","r") as f:
  moves = f.readlines()


sub = Submarine()
sub.parse_moves(moves)
sub.print_position()
