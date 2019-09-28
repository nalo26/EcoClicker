import pygame
import variables as v
from ProcToPy import *
v.init()

#Si une touche est appuyé, faire ce qui est demandé en fonction du menu affiché
# https://www.pygame.org/docs/ref/key.html

def keyPressed(keyCode, keyUnicode):
	v.keyCode = keyCode

	if v.toshow == 'Menu':
		if v.keyCode == pygame.K_ESCAPE: v.MainGameMaster = False

	if v.toshow == 'Shop':
		if v.keyCode == pygame.K_ESCAPE: v.toshow = 'Game'

	if v.toshow == 'Option':
		if v.keyCode == pygame.K_ESCAPE: v.toshow = 'Game'

	if v.toshow == 'Game':
		if keyCode == pygame.K_ESCAPE: v.toshow = 'Option'
		if keyCode == pygame.K_TAB : v.toshow = 'Shop'



def mousePressed(pos):
	v.mouseX = pos[0]
	v.mouseY = pos[1]

	if v.toshow == 'Game':
		if v.mouseX > 20 and v.mouseX < 368 and v.mouseY > 270 and v.mouseY < 450: # Billet
			v.Economia += 1

		if v.mouseX > 387 and v.mouseX < 590: # Différents Mouvements
			v.toshow = 'LoadData'
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
			if v.mouseY > 80*0 and v.mouseY < 80*1: 
				# v.shop = 1
				pass
			if v.mouseY > 80*1 and v.mouseY < 80*2: 
				# v.shop = 2
				pass
			if v.mouseY > 80*2 and v.mouseY < 80*3: 
				# v.shop = 3
				pass
			# if v.mouseY > 80*3 and v.mouseY < 80*4: 
			# 	v.shop = 4
			# if v.mouseY > 80*4 and v.mouseY < 80*5: 
			# 	v.shop = 5
			# if v.mouseY > 80*5 and v.mouseY < 80*6: 
			# 	v.shop = 6
			# if v.mouseY > 80*6 and v.mouseY < 80*7: 
			# 	v.shop = 7
			# if v.mouseY > 80*7 and v.mouseY < 80*8: 
			# 	v.shop = 8
			# if v.mouseY > 80*8 and v.mouseY < 80*9: 
			# 	v.shop = 9
