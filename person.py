from board import board
class person:
    char="P"
    x=0
    y=0
    def put(self,board,color):
        board.create(self.char,self.x,self.y,color)

class queen:
    def __init__(self):
        self.char="Q"
    def put(self,board,x,y,color):
        board.create(self.char,x,y,color)

class donkey(person):
    def __init__(self,x,y):
        self.char="D"
        self.x=x
        self.y=y
        self.spin=1
    def put(self,board,color):
        if self.spin==1 and self.x<=40:
            if self.x==40:
                self.spin=-1
            else:
                self.x+=1
        else:
            if self.spin==-1 and self.x>=1:
                if self.x==1:
                    self.spin=1
                else:
                    self.x-=1
        board.create(self.char,self.x,self.y,color)

class player(person):
    def __init__(self,x,y):
        self.char="P"
        self.x=x
        self.y=y
        self.lives=3
        self.control=0
        self.score=0
    def move_right(self,board):
        if self.x<78:
            self.x+=1
    def move_left(self,board):
        if self.x>1:
            self.x-=1
    def move_up(self):
            self.y-=1
    def move_down(self):
            self.y+=1
    def fall(self,board):
        if self.control<0:
            self.control+=1
            self.y-=1
        else:
            if board.b[self.x][self.y+1]==None:
                self.y+=1
    def collide(self,board):
        if board.b[self.x][self.y]=="O":
            return True
        else:
            return False
 
