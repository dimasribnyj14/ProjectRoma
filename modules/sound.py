import os
import pygame
pygame.init()
class sound:
    def __init__(self,name = None, volume = None):
        self.name = name
        self.volume = volume
        self.sound = None
    def load(self):
        path = os.path.abspath(__file__+"/../..")
        path = os.path.join(path, self.name)
        sound_load = os.path.join(sound_load, self.name)
        self.sound = pygame.mixer.Sound(self.name)
        pygame.mixer.Sound.set_volume(self.sound,self.volume)
    def play(self):
        self.sound = pygame.mixer.Sound.play(self.sound)