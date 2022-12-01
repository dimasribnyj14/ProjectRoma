import pygame
import modules.images as image
import modules.json_game as config
import json
pygame.init()
win = pygame.display.set_mode((config.config["width"],config.config["height"]))