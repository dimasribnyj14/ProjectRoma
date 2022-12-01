import os
import pygame
pygame.init()
class Images:
    def __init__(self,name=None,x=None,y=None,width=None,height=None):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = None
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        if self.name:
            self.load_image()
    def load_image(self):
        path = os.path.abspath(__file__+"/../..")
        path = os.path.join(path, self.name)
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
    def image_show(self,win):
        win.blit(self.image,(self.x,self.y))