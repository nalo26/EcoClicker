import pygame

def init():
	global MainGameMaster, toshow, screen, height, width, color, fontName, fontSize, font, textAlign, pourcStep # pygame
	global billet, onglet_unlock, onglet_lock, bgshop, bgusers_unlock, bgusers_lock, option_bg, bg, ecoplus # pictures
	global mouseX, mouseY, keyCode # inputs
	global Economia, EPS, CB, oldShop, shop, shopPers, BilletState, timeStateBillet # game variables
	global cCoins, cClicks
	global m_mouvement, m_price, m_cb, m_unlock, m_users, u_birth, u_death, u_num, u_sum, u_default, u_eps, u_price, m_images # data from json
	global s_eco_tot, s_time, s_u_tot, s_u_act, s_u_price, s_m_act, s_m_price, s_clicks # stats

	MainGameMaster = True
	toshow = 'Reset'
	screen = pygame.display.set_mode((1280, 720))
	height = 0
	width = 0
	color = (255, 255, 255, 0)
	fontName = "MS Reference Sans Serif"
	fontSize = 24
	font = 0
	textAlign = 'LEFT'
	pourcStep = 0

	billet = pygame.image.load("data/billet.png").convert()
	CoinIm = pygame.image.load("data/coin.png")
	onglet_unlock = pygame.image.load("data/onglet_unlock.png")
	onglet_lock   = pygame.image.load("data/onglet_lock.png")
	bgshop = pygame.image.load("data/shop_bg.png").convert()
	bgusers_unlock = pygame.image.load("data/bg_users_unlock.png").convert()
	bgusers_lock   = pygame.image.load("data/bg_users_lock.png").convert()
	option_bg = pygame.image.load("data/option_bg.png").convert()
	popUp = pygame.image.load("data/popUp.png").convert()
	bg = pygame.image.load("data/bg.png").convert()
	ecoplus = pygame.image.load("data/ecoplus.png").convert()

	mouseX = 0
	mouseY = 0
	keyCode = 0

	Economia = 1000000.0
	EPS = 0 # eco par seconde
	CB = 1
	oldShop = 0
	shop = 0
	shopPers = 0
	BilletState = 'high'
	timeStateBillet = 0

	cCoins = []
	cClicks = []

	m_mouvement = []
	m_price = []
	m_cb = []
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

	s_eco_tot = 0
	s_time = 0
	s_u_tot = 0
	s_u_act = 0
	s_u_price = 0
	s_m_tot = 0
	s_m_act = 0
	s_m_price = 0
	s_clicks = 0