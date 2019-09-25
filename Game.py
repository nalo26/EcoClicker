import pygame
import json
import variables as v
v.init()
from ProcToPy import *

mouvement_list = []
# v.econo_list = ['e']

def Game():
	background(0)
	textAlign("CENTER")
	text(f"Economia : {v.Economia}", 194, 20)
	text(f"par seconde : {v.EPS}", 194, 40)

	image(v.billet, 20, v.height/2-int(540/3)/2, int(1045/3), int(540/3))

	image(v.bgshop, 592, 0)
	fill(255, 255, 255)
	textAlign("LEFT")
	for i in range(len(mouvement_list)):
		image(v.onglet, 388, 80*i)
		text(mouvement_list[i], 400, 80*(i+1)-32)

	for i in range(len(v.econo_list)):
		image(v.bg_users, 592, 80*i)
		textAlign("LEFT")
		text(v.econo_list[i], 600, 80*(i+1)-32)
		textAlign("RIGHT")
		text(v.count[i], 1280, 80*(i+1)-32)

def ChangementMenu():
	v.toshow = 'Game'
	v.econo_list = []
	v.count = []
	with open('data/prices.json', 'r', encoding="utf-8") as mf:
		json_data = json.load(mf)
	for m in json_data:
		mouvement_list.append(m)
		if json_data[m]['id'] == v.shop:
			for user in json_data[m]['users']: 
				v.econo_list.append(user)
				v.count.append(json_data[m]['users'][user]['num'])


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