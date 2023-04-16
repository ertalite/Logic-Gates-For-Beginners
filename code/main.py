import pygame, sys #Importation des modules
import commands as com
import misc

#-----------------------------[ Initialisation ]------------------

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Les portes logiques')
clock = pygame.time.Clock()

#-----------------------------[ Chargement des fichiers ]------------------

main_menu_surface = com.Affichage.chargementFichier('./graphics/backgrounds/esthetique-minimal-violet.jpg')
Nexa = com.Affichage.chargementPolice('./font/Nexa-Heavy.ttf', 30)
title_surface = com.Affichage.creerTexte(Nexa, 'Apprends les portes logiques !', True, 'black')
title_rectangle = com.Collision.creerRectangle(title_surface, 'center', (640, 160))

# Boutons de menu

cours_img = com.Affichage.chargementFichier('./graphics/buttons/menu_buttons/button_cours.png')
cours_button = misc.Bouton(640, 300, cours_img, 1)

circuit_img = com.Affichage.chargementFichier('./graphics/buttons/menu_buttons/button_circuit.png')
circuit_button = misc.Bouton(640, 400, circuit_img, 1)

quitter_img = com.Affichage.chargementFichier('./graphics/buttons/menu_buttons/button_quitter.png')
quitter_button = misc.Bouton(640, 500, quitter_img, 1)

retour_img = com.Affichage.chargementFichier('./graphics/buttons/menu_buttons/button_retour.png')
retour_button = misc.Bouton(200, 100, retour_img, 1)

# Boutons de circuit

a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a.png')
a_button = misc.Bouton(350, 300, a_button_img, 1)

a_button_pressed_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a_pressed.png')
a_button_pressed = misc.Bouton(350, 300, a_button_pressed_img, 1)

b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b.png')
b_button = misc.Bouton(350, 500, b_button_img, 1)

b_button_pressed_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b_pressed.png')
b_button_pressed = misc.Bouton(350, 500, b_button_pressed_img, 1)



#-----------------------------[ Game Loop ]------------------

SYSTEM_STATE ='main'
COURS_STATE = 'and'

run = True
while run:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    com.Affichage.afficher(screen, main_menu_surface, (0, 0))

    if SYSTEM_STATE == 'main':

        com.Affichage.afficher(screen, title_surface, title_rectangle)

        if cours_button.afficher(screen) == True:
            SYSTEM_STATE = 'cours'

        if circuit_button.afficher(screen) == True:
            SYSTEM_STATE = 'circuit'

        if quitter_button.afficher(screen) == True:
            run = False

    if SYSTEM_STATE == 'cours':

        if retour_button.afficher(screen) == True:

            SYSTEM_STATE = 'main'


        if COURS_STATE == 'and':

            if com.Keyboard.pressed(a_button) and com.Keyboard.pressed(b_button):
                print("OK")

            if com.Keyboard.pressed(a_button) == True:

                a_button_pressed.afficher()
   

            if b_button.afficher(screen) == True:

                b_button_pressed.afficher()  


    if SYSTEM_STATE == 'circuit':

        if retour_button.afficher(screen) == True:

            SYSTEM_STATE = 'main'



    pygame.display.update()
    clock.tick(60)