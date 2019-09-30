import pygame
import json
import variables as v
v.init()
from ProcToPy import *

def Shop():
	v.toshow = 'Game'
	v.m_images    = []
	v.m_mouvement = []
	v.m_price     = []
	v.m_eps       = []
	v.m_unlock    = []
	v.m_users     = []
	v.u_birth     = []
	v.u_death     = []
	v.u_num       = []
	v.u_sum       = []
	v.u_default   = []
	v.u_eps       = []
	canpass = False

	with open('data/prices.json', 'r', encoding="utf-8") as mf:
		json_data = json.load(mf)

	for m in json_data:

		if json_data[m]['id'] == v.shop:
			if json_data[m]['unlock'] == "False" and v.Economia >= json_data[m]['price']:
				json_data[m]['unlock'] = "True"
				v.Economia -= json_data[m]['price']
				canpass = True
			if json_data[m]['unlock'] == "True": canpass = True

			if canpass == True:
				for user in json_data[m]['users']: 
					v.m_users.append(user)

					if json_data[m]['users'][user]['id'] == v.shopPers and v.Economia >= json_data[m]['users'][user]['default'] * (1.15**json_data[m]['users'][user]['num']):
						v.Economia -= json_data[m]['users'][user]['default'] * (1.15**json_data[m]['users'][user]['num'])
						json_data[m]['users'][user]['num'] += 1
						v.EPS += json_data[m]['users'][user]['EPS']

					v.m_images.append(pygame.image.load(f"data/portraits/{user}.jpg"))
					v.u_birth.append(json_data[m]['users'][user]['birth'])
					v.u_death.append(json_data[m]['users'][user]['death'])
					v.u_num.append(json_data[m]['users'][user]['num'])
					v.u_sum.append(json_data[m]['users'][user]['sum'])
					v.u_default.append(json_data[m]['users'][user]['default'])
					v.u_eps.append(json_data[m]['users'][user]['EPS'])

		v.m_mouvement.append(m)
		v.m_price.append(json_data[m]['price'])
		v.m_eps.append(json_data[m]['EPS'])
		v.m_unlock.append(json_data[m]['unlock'])

	v.shopPers = 0

	with open('data/prices.json', 'w', encoding='utf-8') as mw:
		json.dump(json_data, mw)
		mw.close()



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