import pygame
pygame.init()
display_width=80
display_height=69
class obj:
    def __init__(self,char,color):
        self.char=char
        self.font=pygame.font.SysFont(None,20)
        self.text=self.font.render(char,True,color)
# board object inherits object class
class board:
    def __init__(self):
        self.display=pygame.display.set_mode((10*display_width,10*display_height))
        self.b=[[None]*display_height for i in range(display_width)]
    def create(self,char,x,y,color):
        self.b[x][y]=obj(char,color)
        self.display.blit(self.b[x][y].text,[10*x,10*y])
