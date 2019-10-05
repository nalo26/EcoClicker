import pygame
import variables as v
v.init()
from ProcToPy import *

addx = 0

def Game():
	background(0)
	textAlign("CENTER")
	textSize(24)
	fill(255)
	text(f"€conomia : {int(v.Economia)}", 194, 20)
	text(f"par seconde : {round(v.EPS, 2)}", 194, 40)

	image(v.billet, 20, v.height/2-int(540/3)/2, int(1045/3), int(540/3))

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
		text(f"{v.m_price[i]}€ / {v.m_eps[i]}EPS", 400+addx, 80*(i+1)-15)
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
		# text(v.u_sum[i], 695, 120*i+90)
		text(v.u_price[i], 695, 120*i+90)
		textAlign("RIGHT")
		textSize(24)
		text(v.u_num[i], 1280-5, 120*i+25)

def AutoClick(tick):
	v.Economia += v.EPS * (tick/1000)

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