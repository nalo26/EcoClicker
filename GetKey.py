import pygame
import variables as v
from ProcToPy import *
v.init()

#Si une touche est appuyé, faire ce qui est demandé en fonction du menu affiché
# https://www.pygame.org/docs/ref/key.html

def keyPressed(keyCode, keyUnicode):
	v.keyCode = keyCode

	if v.toshow == 'Option':
		if v.keyCode == pygame.K_ESCAPE: v.toshow = 'Shop'

	if v.toshow == 'PopUp':
		if v.keyCode == pygame.K_ESCAPE:
			v.toshow = 'Shop'
			v.shopPers = 0

	if v.toshow == 'Game':
		if keyCode == pygame.K_ESCAPE: v.toshow = 'Option'



def mousePressed(pos):
	v.mouseX = pos[0]
	v.mouseY = pos[1]

	if v.toshow == 'Game':
		if v.mouseX > 20 and v.mouseX < 368 and v.mouseY > 270 and v.mouseY < 450: # Billet
			v.Economia += 1

		if v.mouseX > 387 and v.mouseX < 590: # Différents Mouvements
			v.toshow = 'Shop'
			v.oldShop = v.shop
			if v.mouseY > 80*0 and v.mouseY < 80*1: # Mercantilistes
				v.shop = 1
			if v.mouseY > 80*1 and v.mouseY < 80*2: # Physiocrates
				v.shop = 2
			if v.mouseY > 80*2 and v.mouseY < 80*3: # Classiques
				v.shop = 3
			if v.mouseY > 80*3 and v.mouseY < 80*4: # Marxistes
				v.shop = 4
			if v.mouseY > 80*4 and v.mouseY < 80*5: # Néoclassiques
				v.shop = 5
			if v.mouseY > 80*5 and v.mouseY < 80*6: # Keynesiens
				v.shop = 6
			if v.mouseY > 80*6 and v.mouseY < 80*7: # Néoliberaux
				v.shop = 7
			if v.mouseY > 80*7 and v.mouseY < 80*8: # Néokeynesiens
				v.shop = 8
			if v.mouseY > 80*8 and v.mouseY < 80*9: # Autres
				v.shop = 9

		if v.mouseX > 590: # Différents Personnages
			v.toshow = 'Shop'
			if v.mouseY > 120*0 and v.mouseY < 120*1: 
				v.shopPers = 1
			if v.mouseY > 120*1 and v.mouseY < 120*2: 
				v.shopPers = 2
			if v.mouseY > 120*2 and v.mouseY < 120*3: 
				v.shopPers = 3
			if v.mouseY > 120*3 and v.mouseY < 120*4: 
				v.shopPers = 4
			if v.mouseY > 120*4 and v.mouseY < 120*5: 
				v.shopPers = 5
			if v.mouseY > 120*5 and v.mouseY < 120*6: 
				v.shopPers = 6
	if v.toshow == 'Option':
		if v.mouseX > 120 and v.mouseX < 480 and v.mouseY > 147 and v.mouseY < 237: # Quitter
			v.MainGameMaster = False

		if v.mouseX > 800 and v.mouseX < 1160 and v.mouseY > 147 and v.mouseY < 237: # Statistiques
			pass

		if v.mouseX > 120 and v.mouseX < 480 and v.mouseY > 463 and v.mouseY < 553: # Réinitialiser
			v.toshow = "Reset"

		if v.mouseX > 800 and v.mouseX < 1160 and v.mouseY > 463 and v.mouseY < 553: # Crédits
			pass