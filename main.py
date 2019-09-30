import pygame
import variables as v
v.init()

from Game import *
from Shop import *
from GetKey import *
from Menu import *
from Options import *
from Reset import *

pygame.init()
v.screen = pygame.display.set_mode((1280, 720)) # Définir la taille de l'écran
v.font = pygame.font.SysFont(v.fontName, v.fontSize)
v.width, v.height = pygame.display.get_surface().get_size()
timer = pygame.time.Clock()

v.billet = pygame.image.load("data/billet.png").convert()
v.onglet = pygame.image.load("data/onglet.png")
v.bgshop = pygame.image.load("data/shop_bg.png").convert()
v.bg_users = pygame.image.load("data/bg_users.png").convert()

while v.MainGameMaster: # boucle principale du jeu
	pygame.display.flip() # Actualisation de la page

	AutoClick(timer.tick())
	if v.toshow == 'Shop': Shop()
	if v.toshow == 'Game': Game() # affichages des différents pages
	if v.toshow == 'Menu': Menu()
	if v.toshow == 'Option': Option()
	if v.toshow == 'Reset': Reset()

	for event in pygame.event.get():
		if event.type == pygame.QUIT: v.MainGameMaster = False
		if event.type == pygame.KEYDOWN: keyPressed(event.key, event.unicode) # On verifie si une touche a été appuyée
		if event.type == pygame.MOUSEBUTTONDOWN: mousePressed(pygame.mouse.get_pos()) # On vérifie un clic souris
		if event.type == pygame.KEYUP: v.keyCode = 0
pygame.quit()