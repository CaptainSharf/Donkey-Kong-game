import random
from person import *
from board import board
from objects import coins
white=(255,255,255)
p=player(24,58)
donk=donkey(1,9)
q=queen()
co={}
for i in range(5):
    temp=random.randrange(21,78)
    co[(temp,17)]=coins(temp,17,white)
for i in range(5):
    temp=random.randrange(1,59)
    co[(temp,27)]=coins(temp,27,white)
for i in range(5):
    temp=random.randrange(31,78)
    co[(temp,39)]=coins(temp,39,white)
for i in range(10):
    temp=random.randrange(1,79)
    co[(temp,58)]=coins(temp,58,white)
