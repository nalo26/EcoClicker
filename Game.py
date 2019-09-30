import pygame
import variables as v
v.init()
from ProcToPy import *


def Game():
	background(0)
	textAlign("CENTER")
	text(f"€conomia : {int(v.Economia)}", 194, 20)
	text(f"par seconde : {v.EPS}", 194, 40)

	image(v.billet, 20, v.height/2-int(540/3)/2, int(1045/3), int(540/3))

	image(v.bgshop, 592, 0)
	fill(255, 255, 255)
	textAlign("LEFT")
	textSize(24)
	for i in range(len(v.m_mouvement)):
		image(v.onglet, 388, 80*i)
		if v.m_unlock[i] == "True": fill(0, 255, 0)
		else: fill(255, 0, 0)
		text(v.m_mouvement[i], 400, 80*(i+1)-47)
		text(f"{v.m_price[i]}€ / {v.m_eps[i]}EPS", 400, 80*(i+1)-15)
	fill(255)

	for i in range(len(v.m_users)):
		image(v.bg_users, 592, 120*i)
		image(v.m_images[i], 595, 120*i+2, 96, 116)
		textAlign("LEFT")
		text(v.m_users[i], 695, 120*i+25)
		textSize(15)
		text(f"{v.u_birth[i]} - {v.u_death[i]}", 695, 120*i+44)
		text(v.u_sum[i], 695, 120*i+90)
		textAlign("RIGHT")
		textSize(24)
		text(v.u_num[i], 1280-5, 120*i+25)

def AutoClick(tick):
	v.Economia += v.EPS * tick/1000