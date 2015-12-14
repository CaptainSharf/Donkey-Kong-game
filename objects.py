from board import board
from board import obj
from person import donkey
#polymorphism for wall and stairs
class wall:
    def __init__(self):
        self.char="X"
    def build(self,board,y,(x1,x2),color): #colors of x
        c=x1
        while(c<=x2):
                board.create(self.char,c,y,color) #colors of x
                c+=1
class fireball:
    def __init__(self,board,donkey):
        self.x=donkey.x+1
        self.y=donkey.y
        self.char="O"
        self.spin=1
        self.check=0
    def put(self,board,color,donkey):
        if self.x<=78 and self.y<=58 and self.x>=1 and self.y>=1:
            if board.b[self.x][self.y+1]!=None and board.b[self.x][(self.y)+1].char=="X":
                self.check=0
                if self.spin==1:
                    self.x+=1
                else:
                    self.x-=1
            else:
                if self.check==0:
                    self.spin=self.spin*(-1)
                    self.check=1
                self.y+=1
        else:
            self.x=donkey.x+1
            self.y=donkey.y
            selfspin=1
        board.create(self.char,self.x,self.y,color)

class stairs(wall):
    def __init__(self):
        self.char="H"
    def build(self,board,x,(y1,y2),color):
        c=y1
        while(c<=y2):
            board.create(self.char,x,c,color)
            c+=1
            
class coins:
    def __init__(self,x,y,color):
        self.char="C"
        self.x=x
        self.y=y
        self.color=color
        self.collected=0
    def put(self,board):
        board.create(self.char,self.x,self.y,self.color)
