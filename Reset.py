import pygame
import json
import variables as v
v.init()
from ProcToPy import *

def Reset():
	v.toshow = 'Shop'
	v.Economia = 10000000000000000.0
	v.EPS = 0
	v.shop = 0
	v.shopPers = 0
	with open('data/prices.json', 'r', encoding="utf-8") as mf:
		json_data = json.load(mf)
	for m in json_data:
		json_data[m]['unlock'] = "False"
		for user in json_data[m]['users']: 
			json_data[m]['users'][user]['num'] = 0
			with open('data/prices.json', 'w', encoding='utf-8') as mw:
				json.dump(json_data, mw)
				mw.close()