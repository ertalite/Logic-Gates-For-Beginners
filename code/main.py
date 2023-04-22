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

# Polices

Nexa = com.Affichage.chargementPolice('./font/Nexa-Heavy.ttf', 30)

# Textes 

title_surface = com.Affichage.creerTexte(Nexa, 'Apprends les portes logiques !', True, 'black')
title_rectangle = com.Collision.creerRectangle(title_surface, 'center', (640, 160))

cours_surface = com.Affichage.creerTexte(Nexa, 'Les portes logiques c est quoi ?', True, 'black')
cours_rectangle = com.Collision.creerRectangle(cours_surface, 'center', (640, 160))

cours_contenu_surface = com.Affichage.creerTexte(Nexa, 'Une porte logique (gate) est un circuit électronique réalisant des opérations logiques (booléennes) sur une séquence de bits. Cette séquence est donnée par un signal d"'"entrée modulé en créneau (signal carré), et cadencé de façon précise par un circuit d'horloge, ou quartz. Les opérations logiques sont réalisées électriquement par une combinaison de bascules ou inverseurs, à base de transistors. Étant donné les capacités d"'"intégration en électronique, un circuit intégré comporte généralement plusieurs portes à la fois4.', True, 'black')
cours_contenu_rectangle = com.Collision.creerRectangle(cours_contenu_surface, 'center', (640, 260))

and_surface = com.Affichage.creerTexte(Nexa, 'AND', True, 'black')
and_rectangle = com.Collision.creerRectangle(and_surface, 'center', (640, 160))

or_surface = com.Affichage.creerTexte(Nexa, 'OR', True, 'black')
or_rectangle = com.Collision.creerRectangle(or_surface, 'center', (640, 160))

not_surface = com.Affichage.creerTexte(Nexa, 'NOT', True, 'black')
not_rectangle = com.Collision.creerRectangle(not_surface, 'center', (640, 160))

xor_surface = com.Affichage.creerTexte(Nexa, 'XOR', True, 'black')
xor_rectangle = com.Collision.creerRectangle(xor_surface, 'center', (640, 160))

nand_surface = com.Affichage.creerTexte(Nexa, 'NAND', True, 'black')
nand_rectangle = com.Collision.creerRectangle(nand_surface, 'center', (640, 160))

nor_surface = com.Affichage.creerTexte(Nexa, 'NOR', True, 'black')
nor_rectangle = com.Collision.creerRectangle(nor_surface, 'center', (640, 160))

xnor_surface = com.Affichage.creerTexte(Nexa, 'XNOR', True, 'black')
xnor_rectangle = com.Collision.creerRectangle(xnor_surface, 'center', (640, 160))

# Boutons de menu

cours_img = com.Affichage.chargementFichier('./graphics/buttons/menu_buttons/button_cours.png')
cours_button = misc.Bouton(640, 300, cours_img, 1)

circuit_img = com.Affichage.chargementFichier('./graphics/buttons/menu_buttons/button_circuit.png')
circuit_button = misc.Bouton(640, 400, circuit_img, 1)

quitter_img = com.Affichage.chargementFichier('./graphics/buttons/menu_buttons/button_quitter.png')
quitter_button = misc.Bouton(640, 500, quitter_img, 1)

retour_img = com.Affichage.chargementFichier('./graphics/buttons/menu_buttons/button_retour.png')
retour_button = misc.Bouton(150, 620, retour_img, 1)

# Boutons de circuit

a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a.png')
a_button = misc.Bouton(350, 300, a_button_img, 1)

a_button_pressed_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a_pressed.png')
a_button_pressed = misc.Bouton(350, 300, a_button_pressed_img, 1)

b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b.png')
b_button = misc.Bouton(350, 500, b_button_img, 1)

b_button_pressed_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b_pressed.png')
b_button_pressed = misc.Bouton(350, 500, b_button_pressed_img, 1)

fleche_de_droite_button_img = com.Affichage.chargementFichier('./graphics/buttons/cours_buttons/fleche-droite.png')
fleche_de_droite_button = misc.Bouton(1180, 360, fleche_de_droite_button_img, 0.1)

fleche_de_gauche_button_img = com.Affichage.chargementFichier('./graphics/buttons/cours_buttons/fleche-gauche.png')
fleche_de_gauche_button = misc.Bouton(100, 360, fleche_de_gauche_button_img, 0.1)

# Portes logiques


#-----------------------------[ Game Loop ]------------------

SYSTEM_STATE ='main' #Initialisation du menu principal au démarage du programme
COURS_STATE = 'cours_un' #Initalisation du menu "cours" sur la page "cours_un"

run = True 
while run:

    com.Affichage.afficher(screen, main_menu_surface, (0, 0)) #Affichage du fond 

# Menu principal

    if SYSTEM_STATE == 'main': 

        com.Affichage.afficher(screen, title_surface, title_rectangle)

        if cours_button.afficher(screen) == True:
            
            SYSTEM_STATE = 'cours'

        if circuit_button.afficher(screen) == True:
            
            SYSTEM_STATE = 'circuit'

        if quitter_button.afficher(screen) == True:
            run = False

# Menu cours           

    if SYSTEM_STATE == 'cours':

        if retour_button.afficher(screen) == True:

            SYSTEM_STATE = 'main'
            COURS_STATE = 'cours_un'

    # Onglet "cours_un"

        if COURS_STATE == 'cours_un':

            com.Affichage.afficher(screen, cours_surface, cours_rectangle)
            com.Affichage.afficher(screen, cours_contenu_surface, cours_contenu_rectangle)

            if fleche_de_droite_button.afficher(screen) == True:

                COURS_STATE = 'and'

    # Onglet "and"

        if COURS_STATE == 'and':

            com.Affichage.afficher(screen, and_surface, and_rectangle)
            #com.Collision.dessinerRectangle()          #Erreur ici, manque argument

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] and keys[pygame.K_b]:
                  print("OK")

            if keys[pygame.K_a]:

                a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a_pressed.png')
                a_button = misc.Bouton(350, 300, a_button_img, 1)

            if keys[pygame.K_b]:

                b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b_pressed.png')
                b_button = misc.Bouton(350, 500, b_button_img, 1)

            a_button.afficher(screen)
   
            b_button.afficher(screen)

            if fleche_de_gauche_button.afficher(screen) == True:

                COURS_STATE = 'cours_un'

            if fleche_de_droite_button.afficher(screen) == True:

                COURS_STATE = 'or'

            a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a.png')
            a_button = misc.Bouton(350, 300, a_button_img, 1)

            b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b.png')
            b_button = misc.Bouton(350, 500, b_button_img, 1)

    # Onglet "or"

        if COURS_STATE == 'or':

            com.Affichage.afficher(screen, or_surface, or_rectangle)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] or keys[pygame.K_b]:
                print("OK")

            if keys[pygame.K_a]:

                a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a_pressed.png')
                a_button = misc.Bouton(350, 300, a_button_img, 1)

            if keys[pygame.K_b]:

                b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b_pressed.png')
                b_button = misc.Bouton(350, 500, b_button_img, 1)

            a_button.afficher(screen)
   
            b_button.afficher(screen)

            if fleche_de_gauche_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'and'
                clicked = True

            if fleche_de_droite_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'not'
                clicked = True

            a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a.png')
            a_button = misc.Bouton(350, 300, a_button_img, 1)

            b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b.png')
            b_button = misc.Bouton(350, 500, b_button_img, 1)

    # Onglet "not"

        if COURS_STATE == 'not':

            com.Affichage.afficher(screen, not_surface, not_rectangle)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:

                a_button_pressed.afficher(screen)
                print("B")

            if keys[pygame.K_b]:

                b_button_pressed.afficher(screen)
                print("A")

            a_button.afficher(screen)
   
            b_button.afficher(screen)

            if fleche_de_gauche_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'or'
                clicked = True

            if fleche_de_droite_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'xor'
                clicked = True

    # Onglet "xor"

        if COURS_STATE == 'xor':

            com.Affichage.afficher(screen, xor_surface, xor_rectangle)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] and keys[pygame.K_b]:
                print("OK")

            if keys[pygame.K_a]:

                a_button_pressed.afficher(screen)

            if keys[pygame.K_b]:

                b_button_pressed.afficher(screen)

            a_button.afficher(screen)
   
            b_button.afficher(screen)

            if fleche_de_gauche_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'not'
                clicked = True

            if fleche_de_droite_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'nand'
                clicked = True

    # Onglet "nand"

        if COURS_STATE == 'nand':

            com.Affichage.afficher(screen, nand_surface, nand_rectangle)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] and keys[pygame.K_b]:
                print("OK")

            if keys[pygame.K_a]:

                a_button_pressed.afficher(screen)

            if keys[pygame.K_b]:

                b_button_pressed.afficher(screen)

            a_button.afficher(screen)
   
            b_button.afficher(screen)

            if fleche_de_gauche_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'xor'
                clicked = True

            if fleche_de_droite_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'nor'
                clicked = True

        # Onglet "nor"

        if COURS_STATE == 'nor':

            com.Affichage.afficher(screen, nor_surface, nor_rectangle)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] and keys[pygame.K_b]:
                print("OK")

            if keys[pygame.K_a]:

                a_button_pressed.afficher(screen)

            if keys[pygame.K_b]:

                b_button_pressed.afficher(screen)

            a_button.afficher(screen)
   
            b_button.afficher(screen)

            if fleche_de_gauche_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'nand'
                clicked = True

            if fleche_de_droite_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'xnor'
                clicked = True

         # Onglet "xnor"

        if COURS_STATE == 'xnor':

            com.Affichage.afficher(screen, xnor_surface, xnor_rectangle)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] and keys[pygame.K_b]:
                print("OK")

            if keys[pygame.K_a]:

                a_button_pressed.afficher(screen)

            if keys[pygame.K_b]:

                b_button_pressed.afficher(screen)

            a_button.afficher(screen)
   
            b_button.afficher(screen)

            if fleche_de_gauche_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'nor'
                clicked = True

    # Menu circuit

    if SYSTEM_STATE == 'circuit':

        if retour_button.afficher(screen) == True:
     

            SYSTEM_STATE = 'main'


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False

    pygame.display.update()
    clock.tick(60)