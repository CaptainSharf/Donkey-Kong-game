import random
from board import board
from objects import wall
from objects import fireball
from person import donkey
from player import p
from player import donk
from objects import stairs
from player import co
white=(255,255,255)
wall=wall()
stair=stairs()
coin={}
ball=[ None for i in range(5)]
def wally(board):
    stair.build(board,35,(4,10),white)
    wall.build(board,10,(0,29),white)
    wall.build(board,10,(31,34),white)
    wall.build(board,10,(36,39),white)
    wall.build(board,10,(41,50),white)
    stair.build(board,30,(10,18),white)
    stair.build(board,40,(10,18),white)
    wall.build(board,18,(21,29),white)
    wall.build(board,18,(31,39),white)
    wall.build(board,18,(41,79),white)
    stair.build(board,20,(18,28),white)
    stair.build(board,40,(18,28),white)
    wall.build(board,28,(0,19),white)
    wall.build(board,28,(21,39),white)
    wall.build(board,28,(41,49),white)
    wall.build(board,28,(51,54),white)
    wall.build(board,28,(56,60),white)
    stair.build(board,50,(28,40),white)
    stair.build(board,55,(28,40),white)
    wall.build(board,40,(39,39),white)
    wall.build(board,40,(41,44),white)
    wall.build(board,40,(46,49),white)
    wall.build(board,40,(51,54),white)
    wall.build(board,40,(56,79),white)
    stair.build(board,45,(40,50),white)
    stair.build(board,40,(40,50),white)
    wall.build(board,50,(31,39),white)
    wall.build(board,50,(41,44),white)
    wall.build(board,50,(46,50),white)
    wall.build(board,50,(0,29),white)
    stair.build(board,30,(50,59),white)
    for z in range(58):
        wall.build(board,z,(0,0),white)
        wall.build(board,z,(79,79),white)
    wall.build(board,0,(0,79),white)
    wall.build(board,59,(0,79),white)
    wall.build(board,4,(30,34),white)
    wall.build(board,4,(36,40),white)

def control(board,donkey):
    if ball[0]==None:
        ball[0]=fireball(board,donk)
        #print ball[0].char
    i=0
    while i in range(5) and ball[i]!=None:
        ball[i].put(board,white,donk)
        if i+1 in range (5) and ball[i+1]==None and ball[i].y==donk.y+3:
            ball[i+1]=fireball(board,donk)
        i+=1

def checkcollision(board,x,y):
    if board.b[x][y].char=="O":
        return True
    else:
        return False


def checkup(board,x,y):
    if (board.b[x-1][y]!=None and board.b[x-1][y].char=="X") or (board.b[x+1][y]!=None and board.b[x+1][y].char=="X"):
        temp=True
    else:
        temp=False
    if(board.b[x][y-1]!=None and board.b[x][y-1].char=="H") or temp:
        return True
    else:
        return False

def checkdown(board,x,y):
    if (board.b[x][y+1]!=None and board.b[x][y+1].char=="H"):
        return True
    else:
        return False

def prnt(msg,board,y):
    i=30
    for c in msg:
        board.create(c,i,y,white)
        i+=1

def collectcoin(board,x,y):
    temp=(x,y)
    if temp in co and co[temp].collected==0:
        co[(x,y)].collected=1
        p.score+=5
        #print p.score

def putcoin(board):
    for x in co:
        if co[x].collected==0:
            co[x].put(board)
def refresh():
    ball=[None for i in range(20)]
    donk.x=1
    donk.spin=1
    p.x=1
    p.y=58
