import pygame
import variables as v
v.init()
from ProcToPy import *

def Option():
	#    Quitter    / Statistiques
	# Réinitialiser /   Crédits
	image(v.bg, 0, 0)
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

def Stats():
	image(v.bg, 0, 0)
	# sizes
	head = 36 # "Statistiques"
	title = 26 # "Finances", "Economistes", "Mouvements", "Autres"
	body = 20 # Toutes les statistiques

	textAlign("CENTER")
	textSize(head)
	text("-- Statistiques --", v.width/2, 50)

	textAlign("LEFT")
	textSize(title)
	text("** Finances", 30, 120)
	textSize(body)
	text(f"Economia : ", 20, 160)
	text(f"{Convert(v.Economia)} ({Arrange(v.Economia)}€)", 270, 160)
	text(f"Economia cumulées : ", 20, 180)
	text(f"{Convert(v.s_eco_tot)} ({Arrange(v.s_eco_tot)}€)", 270, 180)
	text(f"Gain par seconde : ", 20, 200)
	text(f"{Convert(v.EPS)} ({Arrange(v.EPS)}€)", 270, 200)
	text(f"Gain par clics : ", 20, 220)
	text(f"x{Convert(v.CB)} (x{Arrange(v.CB)})", 270, 220)


	textSize(title)
	text("** Economistes", 30, 300)
	textSize(body)
	text(f"Débloqués : ", 20, 340)
	text(f"{v.s_u_act} / 33 ({round(v.s_u_act/33*100, 1)}%)", 270, 340)
	text(f"Achetés : ", 20, 360)
	text(f"{v.s_u_tot}", 270, 360)
	text(f"Prix d'achat cumulé : ", 20, 380)
	text(f"{Convert(v.s_u_price)} ({Arrange(v.s_u_price)}€)", 270, 380)

	textSize(title)
	text("** Mouvements", 30, 460)
	textSize(body)
	text(f"Achetés : ", 20, 500)
	text(f"{v.s_m_act} / 9 ({round(v.s_m_act/9*100, 1)}%)", 270, 500)
	text(f"Prix d'achat cumulé : ", 20, 520)
	text(f"{Convert(v.s_m_price)} ({Arrange(v.s_m_price)}€)", 270, 520)

	textSize(title)
	text("** Autres", 30, 600)
	textSize(body)
	text(f"Nombre de clics : ", 20, 640)
	text(f"{v.s_clicks}", 270, 640)
	text(f"Durée de la partie : ", 20, 660)
	text(f"{Time(v.s_time)} ({Arrange(v.s_time)}s)", 270, 660)


def Credits():
	image(v.bg, 0, 0)

	textAlign("CENTER")
	textSize(36)
	text("-- Crédits --", v.width/2, 50)

	textAlign("LEFT")
	textSize(26)
	text("• Idée du jeu : Julien C / Nathan V", 30, 120)
	text("• Chercheurs : Nathan P / Maxime T / Josué B", 30, 160)
	text("• Développeur : Nathan V", 30, 200)
	text("• Graphismes : Julien C / Nathan P / Nathan V", 30, 240)

	text("• Constitution du groupe : Nathan P / Maxime T / Josué B / Nathan V", 30, 320)
	text("• Remerciement : Mme. Constant, 2ème Année", 30, 360)

	textAlign("RIGHT")
	textSize(16)
	text("Tous droits reservés, Eco+ production", v.width-30, v.height-30)
	image(v.ecoplus, 20, v.height-70, 50, 50)