import pygame

def init():
	global MainGameMaster, toshow, screen, height, width, color, fontName, fontSize, font, textAlign # pygame
	global billet # pictures
	global mouseX, mouseY, keyCode
	global Economia, EPS, shop
	global econo_list

	MainGameMaster = True
	toshow = 'LoadData'
	screen = pygame.display.set_mode((1280, 720))
	height = 0
	width = 0
	color = (255, 255, 255, 0)
	fontName = "MS Reference Sans Serif"
	fontSize = 24
	font = 0
	textAlign = 'LEFT'

	billet = pygame.image.load("data/billet.png").convert()
	onglet = pygame.image.load("data/onglet.png")
	bgshop = pygame.image.load("data/shop_bg.png").convert()
	bg_users = pygame.image.load("data/bg_users.png").convert()

	mouseX = 0
	mouseY = 0
	keyCode = 0

	Economia = 0
	EPS = 0 # eco par seconde
	shop = 1

	econo_list = []
	count = []