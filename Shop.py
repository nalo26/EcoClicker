import pygame
import json
import variables as v
v.init()
from ProcToPy import *

def Shop():
	if v.toshow == 'Loading': pass
	if v.toshow == 'Shop': v.toshow = 'Game'
	v.m_mouvement = []
	v.m_price     = []
	v.m_cb        = []
	v.m_unlock    = []
	canpass = False

	with open('data/prices.json', 'r', encoding="utf-8") as mf:
		json_data = json.load(mf)

	for m in json_data:

		if json_data[m]['id'] == v.shop:
			if json_data[m]['unlock'] == "False" and v.Economia >= json_data[m]['price']:
				json_data[m]['unlock'] = "True"
				v.Economia -= json_data[m]['price']
				v.s_m_price += json_data[m]['price']
				v.s_m_act += 1
				v.CB *= json_data[m]['CB']
				canpass = True
			if json_data[m]['unlock'] == "True": canpass = True

			if canpass == True:
				v.m_users     = []
				v.u_images    = []
				v.u_birth     = []
				v.u_death     = []
				v.u_num       = []
				v.u_sum       = []
				v.u_default   = []
				v.u_eps       = []
				v.u_price     = []
				for user in json_data[m]['users']: 
					v.m_users.append(user)
					with open(f"data/bio/{user}.txt", 'r', encoding="utf-8") as mysum:
						v.u_sum.append(mysum.read())

					if json_data[m]['users'][user]['id'] == v.shopPers and v.Economia >= json_data[m]['users'][user]['default'] * (1.15**json_data[m]['users'][user]['num']):
						v.Economia -= json_data[m]['users'][user]['default'] * (1.15**json_data[m]['users'][user]['num'])
						v.s_u_price += json_data[m]['users'][user]['default'] * (1.15**json_data[m]['users'][user]['num'])
						v.s_u_tot += 1
						if json_data[m]['users'][user]['num'] == 0: v.s_u_act += 1
						v.EPS += json_data[m]['users'][user]['EPS']
						json_data[m]['users'][user]['num'] += 1
						if json_data[m]['users'][user]['num'] == 1: v.toshow = 'PopUp'
						else: v.shopPers = 0

					v.u_images.append(pygame.image.load(f"data/portraits/{user}.jpg"))
					v.u_birth.append(json_data[m]['users'][user]['birth'])
					v.u_death.append(json_data[m]['users'][user]['death'])
					v.u_num.append(json_data[m]['users'][user]['num'])
					v.u_default.append(json_data[m]['users'][user]['default'])
					v.u_eps.append(json_data[m]['users'][user]['EPS'])
					v.u_price.append(round(json_data[m]['users'][user]['default'] * 1.15**json_data[m]['users'][user]['num']))
			else: v.shop = v.oldShop

		v.m_mouvement.append(m)
		v.m_price.append(json_data[m]['price'])
		v.m_cb.append(json_data[m]['CB'])
		v.m_unlock.append(json_data[m]['unlock'])

	with open('data/prices.json', 'w', encoding='utf-8') as mw:
		json.dump(json_data, mw, indent=4)
		mw.close()