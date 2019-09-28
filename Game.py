import pygame
import json
import variables as v
v.init()
from ProcToPy import *


def Game():
	background(0)
	textAlign("CENTER")
	text(f"Economia : {v.Economia}", 194, 20)
	text(f"par seconde : {v.EPS}", 194, 40)

	image(v.billet, 20, v.height/2-int(540/3)/2, int(1045/3), int(540/3))

	image(v.bgshop, 592, 0)
	fill(255, 255, 255)
	textAlign("LEFT")
	for i in range(len(v.m_mouvement)):
		image(v.onglet, 388, 80*i)
		if v.m_unlock[i] == "True": fill(0, 255, 0)
		else: fill(255, 0, 0)
		text(v.m_mouvement[i], 400, 80*(i+1)-32)
	fill(255)

	for i in range(len(v.m_users)):
		image(v.bg_users, 592, 120*i)
		textAlign("LEFT")
		text(v.m_users[i], 600, 120*(i+1)-48)
		textAlign("RIGHT")
		text(v.u_num[i], 1280, 120*(i+1)-48)

def ChangementMenu():
	v.toshow = 'Game'
	v.m_mouvement = []
	v.m_default = []
	v.m_eps = []
	v.m_unlock = []
	v.m_users = []
	v.u_birth = []
	v.u_death = []
	v.u_num = []
	v.u_sum = []
	v.u_default = []
	v.u_eps = []
	with open('data/prices.json', 'r', encoding="utf-8") as mf:
		json_data = json.load(mf)
	for m in json_data:
		v.m_mouvement.append(m)
		v.m_default.append(json_data[m]['default'])
		v.m_eps.append(json_data[m]['EPS'])
		v.m_unlock.append(json_data[m]['unlock'])
		if json_data[m]['id'] == v.shop:
			for user in json_data[m]['users']: 
				v.m_users.append(user)
				v.u_birth.append(json_data[m]['users'][user]['birth'])
				v.u_death.append(json_data[m]['users'][user]['death'])
				v.u_num.append(json_data[m]['users'][user]['num'])
				v.u_sum.append(json_data[m]['users'][user]['sum'])
				v.u_default.append(json_data[m]['users'][user]['default'])
				v.u_eps.append(json_data[m]['users'][user]['EPS'])



# PrixN = PrixBase * 1.15^n

'''
         NAME          COST       CPS
Cursor :               15         0.1
Grandma:               100        1
Farm :                 1.1 K      8
Mine :                 12 K       47
Factory :              130 K      260
Bank :                 1'4 M      1.4 K
Temple :               20 M       7.8 K
Wizard Tower :         330 M      44 K
Shipment :             5.1 B      260 K
Alchemy Lab :          75 B       1.6 M
Portal :               1 T        10 M
Time Machine :         14 T       65 M
Antimatter Condenser : 170 T      430 M
Prism :                2.1 Q      2.9 B
ChanceMaker :          26 Q       21 B
Fractal Engine :       310 Q      150 B

K = 1'000				  (Kilo     / Mille    )
M = 1'000'000 			  (Mega     / Million  )
B = 1'000'000'000 		  (Billion  / Milliard )
T = 1'000'000'000'000 	  (Trillion / Trillon  )
Q = 1'000'000'000'000'000 (Quadrion / Trilliard)
'''