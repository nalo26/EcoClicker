import pygame

def init():
	global MainGameMaster, toshow, screen, height, width, color, fontName, fontSize, font, textAlign # pygame
	global billet, onglet_unlock, onglet_lock, bgshop, bgusers_unlock, bgusers_lock, option_bg # pictures
	global mouseX, mouseY, keyCode
	global Economia, EPS, oldShop, shop, shopPers
	global m_mouvement, m_price, m_eps, m_unlock, m_users, u_birth, u_death, u_num, u_sum, u_default, u_eps, u_price, m_images # data from json

	MainGameMaster = True
	# toshow = 'Reset'
	toshow = 'Reset'
	screen = pygame.display.set_mode((1280, 720))
	height = 0
	width = 0
	color = (255, 255, 255, 0)
	fontName = "MS Reference Sans Serif"
	fontSize = 24
	font = 0
	textAlign = 'LEFT'

	billet = pygame.image.load("data/billet.png").convert()
	onglet_unlock = pygame.image.load("data/onglet_unlock.png")
	onglet_lock   = pygame.image.load("data/onglet_lock.png")
	bgshop = pygame.image.load("data/shop_bg.png").convert()
	bgusers_unlock = pygame.image.load("data/bg_users_unlock.png").convert()
	bgusers_lock   = pygame.image.load("data/bg_users_lock.png").convert()
	option_bg = pygame.image.load("data/option_bg.png").convert()
	popUp = pygame.image.load("data/popUp.png").convert()

	mouseX = 0
	mouseY = 0
	keyCode = 0

	Economia = 1000000.0
	EPS = 0 # eco par seconde
	oldShop = 0
	shop = 0
	shopPers = 0

	m_mouvement = []
	m_price = []
	m_eps = []
	m_unlock = []
	m_users = []
	u_birth = []
	u_death = []
	u_num = []
	u_sum = []
	u_default = []
	u_eps = []
	u_price = []

	u_images = []