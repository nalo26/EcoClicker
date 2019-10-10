import pygame
import variables as v
from ProcToPy import *
from Game import Coin, Click
v.init()

#Si une touche est appuyé, faire ce qui est demandé en fonction du menu affiché
# https://www.pygame.org/docs/ref/key.html

def keyPressed(keyCode, keyUnicode):
	v.keyCode = keyCode

	if v.toshow == 'Option':
		if v.keyCode == pygame.K_ESCAPE: v.toshow = 'Shop'

	if v.toshow == 'Stats':
		if v.keyCode == pygame.K_ESCAPE: v.toshow = 'Option'

	if v.toshow == 'Credits':
		if v.keyCode == pygame.K_ESCAPE: v.toshow = 'Option'

	if v.toshow == 'PopUp':
		if v.keyCode == pygame.K_ESCAPE:
			v.toshow = 'Shop'
			v.shopPers = 0

	if v.toshow == 'Game':
		if keyCode == pygame.K_ESCAPE: v.toshow = 'Option'

	if v.keyCode == pygame.K_KP9: v.Economia += 500000000000000000



def mousePressed(pos):
	v.mouseX = pos[0]
	v.mouseY = pos[1]

	if v.toshow == 'Game':
		if v.mouseX > 20 and v.mouseX < 368 and v.mouseY > 270 and v.mouseY < 450: # Billet
			v.Economia += v.CB
			v.s_clicks += 1
			v.cCoins.append(Coin())
			v.cClicks.append(Click(v.mouseX, v.mouseY))
			if v.BilletState == 'low': 
				v.BilletState = 'high'
				v.timeStateBillet = 0
			if v.BilletState == 'high': v.BilletState = 'low'

		if v.mouseX > 387 and v.mouseX < 590: # Différents Mouvements
			v.toshow = 'Shop'
			v.oldShop = v.shop
			if v.mouseY > 80*0 and v.mouseY < 80*1: v.shop = 1 # Mercantilistes
			if v.mouseY > 80*1 and v.mouseY < 80*2: v.shop = 2 # Physiocrates
			if v.mouseY > 80*2 and v.mouseY < 80*3: v.shop = 3 # Classiques
			if v.mouseY > 80*3 and v.mouseY < 80*4: v.shop = 4 # Marxistes
			if v.mouseY > 80*4 and v.mouseY < 80*5: v.shop = 5 # Néoclassiques
			if v.mouseY > 80*5 and v.mouseY < 80*6: v.shop = 6 # Keynesiens
			if v.mouseY > 80*6 and v.mouseY < 80*7: v.shop = 7 # Néoliberaux
			if v.mouseY > 80*7 and v.mouseY < 80*8: v.shop = 8 # Néokeynesiens
			if v.mouseY > 80*8 and v.mouseY < 80*9: v.shop = 9 # Autres
				

		if v.mouseX > 590: # Différents Personnages
			v.toshow = 'Shop'
			if v.mouseY > 120*0 and v.mouseY < 120*1: v.shopPers = 1
			if v.mouseY > 120*1 and v.mouseY < 120*2: v.shopPers = 2
			if v.mouseY > 120*2 and v.mouseY < 120*3: v.shopPers = 3
			if v.mouseY > 120*3 and v.mouseY < 120*4: v.shopPers = 4
			if v.mouseY > 120*4 and v.mouseY < 120*5: v.shopPers = 5
			if v.mouseY > 120*5 and v.mouseY < 120*6: v.shopPers = 6
				
	if v.toshow == 'Option':
		if v.mouseX > 120 and v.mouseX < 480 and v.mouseY > 147 and v.mouseY < 237: # Quitter
			v.MainGameMaster = False

		if v.mouseX > 800 and v.mouseX < 1160 and v.mouseY > 147 and v.mouseY < 237: # Statistiques
			v.toshow = 'Stats'

		if v.mouseX > 120 and v.mouseX < 480 and v.mouseY > 463 and v.mouseY < 553: # Réinitialiser
			v.toshow = 'Reset'

		if v.mouseX > 800 and v.mouseX < 1160 and v.mouseY > 463 and v.mouseY < 553: # Crédits
			v.toshow = 'Credits'