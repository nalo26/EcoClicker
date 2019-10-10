import pygame
from random import randint
import variables as v
v.init()

from Game import *
from Shop import *
from GetKey import *
from Options import *
from Reset import *

pygame.init()
v.screen = pygame.display.set_mode((1280, 720)) # Définir la taille de l'écran
v.font = pygame.font.SysFont(v.fontName, v.fontSize)
v.width, v.height = pygame.display.get_surface().get_size()
timer = pygame.time.Clock()

def Loading():
	image(v.bg, 0, 0)
	textAlign("CENTER")
	textSize(72)
	fill(255)
	text("Chargement...", v.width/2, v.height/2-100)
	rect(200, v.height/2, v.width-400, 30)
	fill(255, 0, 0)
	v.pourcStep += randint(0, 1)/300
	rect(202, v.height/2+2, int((v.width-404)*v.pourcStep), 26)
	if v.pourcStep >= 1: v.toshow = 'Game'

v.billet = pygame.image.load("data/billet.png").convert()
v.CoinIm = pygame.image.load("data/coin.png")
v.onglet_unlock = pygame.image.load("data/onglet_unlock.png")
v.onglet_lock   = pygame.image.load("data/onglet_lock.png")
v.bgshop = pygame.image.load("data/shop_bg.png").convert()
v.bgusers_unlock = pygame.image.load("data/bg_users_unlock.png").convert()
v.bgusers_lock   = pygame.image.load("data/bg_users_lock.png").convert()
v.option_bg = pygame.image.load("data/option_bg.png").convert()
v.popUp = pygame.image.load("data/popUp.png").convert()
v.bg = pygame.image.load("data/bg.png").convert()
v.ecoplus = pygame.image.load("data/ecoplus.png").convert()

while v.MainGameMaster: # boucle principale du jeu
	pygame.display.flip() # Actualisation de la page

	AutoClick(timer.tick())
	if v.toshow == 'Loading': Loading()
	if v.toshow == 'PopUp': PopUp()
	if v.toshow == 'Game': Game() # affichages des différents pages
	if v.toshow == 'Option': Option()
	if v.toshow == 'Stats': Stats()
	if v.toshow == 'Credits': Credits()
	if v.toshow == 'Shop': Shop()
	if v.toshow == 'Reset': Reset()

	for event in pygame.event.get():
		if event.type == pygame.QUIT: v.MainGameMaster = False
		if event.type == pygame.KEYDOWN: keyPressed(event.key, event.unicode) # On verifie si une touche a été appuyée
		if event.type == pygame.MOUSEBUTTONDOWN: mousePressed(pygame.mouse.get_pos()) # On vérifie un clic souris
		if event.type == pygame.KEYUP: v.keyCode = 0
pygame.quit()