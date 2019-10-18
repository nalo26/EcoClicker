import pygame
from random import randint
import variables as v
v.init()
from ProcToPy import *

addx = 0

def Game():
	background(0)
	MoveCoin()
	textAlign("CENTER")
	textSize(24)
	fill(255)
	text(f"€conomia : {Convert(v.Economia)}", 194, 20)
	text(f"par seconde : {Convert(v.EPS)}", 194, 40)
	if v.BilletState == 'high': image(v.billet, 20, v.height/2-int(540/3)/2, int(1045/3), int(540/3))
	else: 
		image(v.billet, 25, v.height/2-int(540/3)/2+5, int(1045/3)-10, int(540/3)-10)
		v.timeStateBillet += 1
		if v.timeStateBillet >= 10: 
			v.timeStateBillet = 0
			v.BilletState = 'high'

	fill(255, 255, 255)
	textAlign("LEFT")
	textSize(24)
	for i in range(len(v.m_mouvement)):
		if v.shop == i+1: addx = 10
		else: addx = 0
		if v.m_unlock[i] == "True":
			fill(255)
			image(v.onglet_unlock, 388+addx, 80*i)
		else:
			fill(79, 79, 79)
			image(v.onglet_lock, 388+addx, 80*i)
		text(v.m_mouvement[i], 400+addx, 80*(i+1)-47)
		text(f"{Convert(v.m_price[i])}€ / x{Convert(v.m_cb[i])}CB", 400+addx, 80*(i+1)-15)
	fill(255)
	image(v.bgshop, 592, 0)

	for i in range(len(v.m_users)):
		if v.Economia >= v.u_price[i]:
			image(v.bgusers_unlock, 592, 120*i)
			fill(255)
		else:
			image(v.bgusers_lock, 592, 120*i)
			fill(79)
		image(v.u_images[i], 595, 120*i+2, 96, 116)
		textAlign("LEFT")
		text(v.m_users[i], 695, 120*i+25)
		textSize(15)
		text(f"{v.u_birth[i]} - {v.u_death[i]}", 695, 120*i+44)
		textSize(24)
		text(f"{Convert(v.u_price[i])}€ / +{Convert(v.u_eps[i])} EPS", 695, 120*i+90)
		textAlign("RIGHT")
		text(f"x{v.u_num[i]}", 1280-5, 120*i+25)
	DrawClick()

def AutoClick(tick):
	v.Economia += v.EPS * (tick/1000)
	v.s_eco_tot += v.EPS * (tick/1000)
	v.s_time += tick/1000

def PopUp():
	k = v.shopPers-1
	Game()
	image(v.popUp, v.width/2-688/2, 0)
	image(v.u_images[k], 321, 25, 150, 180)
	textAlign("CENTER")
	fill(255)
	textSize(30)
	text(v.m_users[k], v.width/2+80, 50)
	textSize(15)
	text(f"{v.u_birth[k]} - {v.u_death[k]}", v.width/2+80, 80)
	textWrap(v.u_sum[k], 320, 220, 642, 477)

class Coin:
	def __init__(self):
		self.x = randint(0, 358)
		self.y = -30

	def move(self):
		self.y += 1
		image(v.CoinIm, self.x, self.y, 30, 30)
		if self.y > v.height: v.cCoins.remove(self)

class Click:
	def __init__(self, x, y):
		# self.x = randint(20, 368)
		# self.y = randint(270, 450)
		self.x = x
		self.y = y
		self.t = 0

	def act(self):
		self.t += 1
		self.y -= 1
		fill(255)
		text(f"+{v.CB}", self.x, self.y)
		# print(self.t, self.x, self.y)
		if self.t > 50: v.cClicks.remove(self)

def MoveCoin():
	for coin in v.cCoins:
		coin.move()

def DrawClick():
	for click in v.cClicks:
		click.act()