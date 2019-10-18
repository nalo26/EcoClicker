import pygame
import json
from Shop import Shop
import variables as v
v.init()
from ProcToPy import *

def Reset():
	v.toshow = 'Loading'
	v.Economia = 0.0
	v.EPS = 0
	v.shop = 0
	v.shopPers = 0
	v.cCoins = []
	v.cClicks = []
	v.pourcStep = 0.0
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
	with open('data/prices.json', 'r', encoding="utf-8") as mf:
		json_data = json.load(mf)
	for m in json_data:
		json_data[m]['unlock'] = "False"
		for user in json_data[m]['users']: 
			json_data[m]['users'][user]['num'] = 0
			with open('data/prices.json', 'w', encoding='utf-8') as mw:
				json.dump(json_data, mw)
				mw.close()
	Shop()