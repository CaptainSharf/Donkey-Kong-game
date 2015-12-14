import pygame
from board import board
from stuff import *
from objects import fireball
from player import *
clock=pygame.time.Clock()
white=(255,255,255)
gamexit=False
ex=False
while not gamexit:
    bo=board()
    if ex==False:
        wally(bo)
        donk.put(bo,white)
        putcoin(bo)
        p.put(bo,white)
        control(bo,donk)
        ex=checkcollision(bo,p.x,p.y)
        collectcoin(bo,p.x,p.y)
       # if bo.b[p.x][p.y].char=="C":
        #    print "S"
        p.fall(bo)
        q.put(bo,32,3,white)
        if p.y==3:
            p.score+=50
            refresh()
        #if bo.b[p.x][p.y].char!="P":
        #ex=p.collide(bo)
        prnt("Your Score:"+str(p.score),bo,63)
        prnt("Lives Left:"+str(p.lives),bo,65)
    else:
        ex=False
        refresh()
        p.score-=25
        p.lives-=1
        if p.lives==0:
            gamexit=True
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gamexit=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_d:
                p.move_right(bo)
            elif event.key==pygame.K_a:
                p.move_left(bo)
            elif event.key==pygame.K_w and checkup(bo,p.x,p.y):
                p.move_up()
            elif event.key==pygame.K_s and checkdown(bo,p.x,p.y):
                p.move_down()
            elif event.key==pygame.K_SPACE and (bo.b[p.x][p.y+1]!=None and bo.b[p.x][p.y+1].char=="X"):
                p.control=-2
            elif event.key==pygame.K_q:
                gamexit=True
    pygame.display.update()
    clock.tick(1000)
pygame.quit()
quit()
