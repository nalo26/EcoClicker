import pygame
import variables as v
v.init()
from ProcToPy import *

def Option():
	#    Quitter    / Statistiques
	# Réinitialiser /   Crédits
	background(0)
	image(v.option_bg, 120, 147) # Quitter
	image(v.option_bg, 800, 147) # Statistiques
	image(v.option_bg, 120, 463) # Réinitialiser
	image(v.option_bg, 800, 463) # Crédits
	textSize(40)
	textAlign("CENTER")
	fill(255)
	text("Quitter", 300, 200)
	text("Statistiques", 980, 200)
	text("Réinitialiser", 300, 520)
	text("Crédits", 980, 520)