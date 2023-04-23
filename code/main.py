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

cours_surface = com.Affichage.creerTexte(Nexa, "Les portes logiques c'est quoi ?", True, 'black')
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
a_button = misc.Bouton(280, 300, a_button_img, 1)

a_button_pressed_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a_pressed.png')
a_button_pressed = misc.Bouton(280, 300, a_button_pressed_img, 1)

b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b.png')
b_button = misc.Bouton(280, 480, b_button_img, 1)

b_button_pressed_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b_pressed.png')
b_button_pressed = misc.Bouton(280, 480, b_button_pressed_img, 1)

fleche_de_droite_button_img = com.Affichage.chargementFichier('./graphics/buttons/cours_buttons/fleche-droite.png')
fleche_de_droite_button = misc.Bouton(1180, 360, fleche_de_droite_button_img, 0.1)

fleche_de_gauche_button_img = com.Affichage.chargementFichier('./graphics/buttons/cours_buttons/fleche-gauche.png')
fleche_de_gauche_button = misc.Bouton(100, 360, fleche_de_gauche_button_img, 0.1)

# Portes logiques

ANDgate_img = com.Affichage.chargementFichier('./graphics/gates/ANDgate.png')
ANDgate_img = com.Affichage.redimensionner(ANDgate_img, 0.65)
ANDgate_rectangle = com.Collision.creerRectangle(ANDgate_img, 'center', (640, 370))

NANDgate_img = com.Affichage.chargementFichier('./graphics/gates/NANDgate.png')
NANDgate_img = com.Affichage.redimensionner(NANDgate_img, 0.55)
NANDgate_rectangle = com.Collision.creerRectangle(NANDgate_img, 'center', (640, 360))

NORgate_img = com.Affichage.chargementFichier('./graphics/gates/NORgate.png')
NORgate_img = com.Affichage.redimensionner(NORgate_img, 0.518)
NORgate_rectangle = com.Collision.creerRectangle(NORgate_img, 'center', (640, 360))

NOTgate_img = com.Affichage.chargementFichier('./graphics/gates/NOTgate.png')
NOTgate_img = com.Affichage.redimensionner(NOTgate_img, 0.35)
NOTgate_rectangle = com.Collision.creerRectangle(NOTgate_img, 'center', (640, 360))

ORgate_img = com.Affichage.chargementFichier('./graphics/gates/ORgate.png')
ORgate_img = com.Affichage.redimensionner(ORgate_img, 0.65)
ORgate_rectangle = com.Collision.creerRectangle(ORgate_img, 'center', (640, 360))

XNORgate_img = com.Affichage.chargementFichier('./graphics/gates/XNORgate.png')
XNORgate_img = com.Affichage.redimensionner(XNORgate_img, 0.55)
XNORgate_rectangle = com.Collision.creerRectangle(XNORgate_img, 'center', (640, 360))

XORgate_img = com.Affichage.chargementFichier('./graphics/gates/XORgate.png')
XORgate_img = com.Affichage.redimensionner(XORgate_img, 0.325)
XORgate_rectangle = com.Collision.creerRectangle(XORgate_img, 'center', (640, 360))

# Lumières

light_on_img = com.Affichage.chargementFichier('./graphics/lights/light-bulb-on.png')
light_on_img = com.Affichage.redimensionner(light_on_img, 0.1)
light_on_rectangle = com.Collision.creerRectangle(light_on_img, 'center', (1025, 360))

light_off_img = com.Affichage.chargementFichier('./graphics/lights/light-bulb-off.png')
light_off_img = com.Affichage.redimensionner(light_off_img, 0.1)
light_off_rectangle = com.Collision.creerRectangle(light_off_img, 'center', (1025, 360))


#-----------------------------[ Game Loop ]------------------

SYSTEM_STATE ='main' #Initialisation du menu principal au démarage du programme
COURS_STATE = 'cours_un' #Initalisation du menu "cours" sur la page "cours_un"

run = True 
while run:

    com.Affichage.afficher(screen, main_menu_surface, (0, 0), 1) #Affichage du fond 

# Menu principal

    if SYSTEM_STATE == 'main': 

        com.Affichage.afficher(screen, title_surface, title_rectangle, 1)

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

            com.Affichage.afficher(screen, cours_surface, cours_rectangle, 1)
            com.Affichage.afficher(screen, cours_contenu_surface, cours_contenu_rectangle, 1)

            if fleche_de_droite_button.afficher(screen) == True and clicked == False:
                clicked = True
                COURS_STATE = 'and'

    # Onglet "and"

        if COURS_STATE == 'and':

            com.Affichage.afficher(screen, and_surface, and_rectangle, 1)
        
            com.Affichage.afficher(screen, ANDgate_img, ANDgate_rectangle, 1)

            com.Affichage.afficher(screen, light_off_img, light_off_rectangle, 1)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] and keys[pygame.K_b]:
                  
                  com.Affichage.afficher(screen, light_on_img, light_on_rectangle, 1)

            if keys[pygame.K_a]:

                a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a_pressed.png')
                a_button = misc.Bouton(280, 300, a_button_img, 1)

            if keys[pygame.K_b]:

                b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b_pressed.png')
                b_button = misc.Bouton(280, 435, b_button_img, 1)

            a_button.afficher(screen)
   
            b_button.afficher(screen)

            a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a.png')
            a_button = misc.Bouton(280, 300, a_button_img, 1)

            b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b.png')
            b_button = misc.Bouton(280, 435, b_button_img, 1)

            if fleche_de_gauche_button.afficher(screen) == True and clicked == False:
                clicked = True
                COURS_STATE = 'cours_un'

            if fleche_de_droite_button.afficher(screen) == True and clicked == False:
                clicked = True
                COURS_STATE = 'or'

    # Onglet "or"

        if COURS_STATE == 'or':

            com.Affichage.afficher(screen, or_surface, or_rectangle, 1)

            com.Affichage.afficher(screen, ORgate_img, ORgate_rectangle, 1)

            com.Affichage.afficher(screen, light_off_img, light_off_rectangle, 1)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] or keys[pygame.K_b]:
                  
                  com.Affichage.afficher(screen, light_on_img, light_on_rectangle, 1)

            if keys[pygame.K_a]:

                a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a_pressed.png')
                a_button = misc.Bouton(280, 300, a_button_img, 1)

            if keys[pygame.K_b]:

                b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b_pressed.png')
                b_button = misc.Bouton(280, 435, b_button_img, 1)

            a_button.afficher(screen)
   
            b_button.afficher(screen)

            a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a.png')
            a_button = misc.Bouton(280, 300, a_button_img, 1)

            b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b.png')
            b_button = misc.Bouton(280, 435, b_button_img, 1)

            if fleche_de_gauche_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'and'
                clicked = True

            if fleche_de_droite_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'not'
                clicked = True

    # Onglet "not"

        if COURS_STATE == 'not':

            com.Affichage.afficher(screen, not_surface, not_rectangle, 1)

            com.Affichage.afficher(screen, NOTgate_img, NOTgate_rectangle, 1)

            com.Affichage.afficher(screen, light_off_img, light_off_rectangle, 1)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] and keys[pygame.K_b]:
                  
                  com.Affichage.afficher(screen, light_on_img, light_on_rectangle, 1)

            if keys[pygame.K_a]:

                a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a_pressed.png')
                a_button = misc.Bouton(280, 300, a_button_img, 1)

            if keys[pygame.K_b]:

                b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b_pressed.png')
                b_button = misc.Bouton(280, 435, b_button_img, 1)

            a_button.afficher(screen)
   
            b_button.afficher(screen)

            a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a.png')
            a_button = misc.Bouton(280, 300, a_button_img, 1)

            b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b.png')
            b_button = misc.Bouton(280, 435, b_button_img, 1)

            if fleche_de_gauche_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'or'
                clicked = True

            if fleche_de_droite_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'xor'
                clicked = True

    # Onglet "xor"

        if COURS_STATE == 'xor':

            com.Affichage.afficher(screen, xor_surface, xor_rectangle, 1)

            com.Affichage.afficher(screen, XORgate_img, XORgate_rectangle, 1)

            com.Affichage.afficher(screen, light_off_img, light_off_rectangle, 1)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] and keys[pygame.K_b]:
                  
                  com.Affichage.afficher(screen, light_on_img, light_on_rectangle, 1)

            if keys[pygame.K_a]:

                a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a_pressed.png')
                a_button = misc.Bouton(280, 300, a_button_img, 1)

            if keys[pygame.K_b]:

                b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b_pressed.png')
                b_button = misc.Bouton(280, 435, b_button_img, 1)

            a_button.afficher(screen)
   
            b_button.afficher(screen)

            a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a.png')
            a_button = misc.Bouton(280, 300, a_button_img, 1)

            b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b.png')
            b_button = misc.Bouton(280, 435, b_button_img, 1)

            if fleche_de_gauche_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'not'
                clicked = True

            if fleche_de_droite_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'nand'
                clicked = True


    # Onglet "nand"

        if COURS_STATE == 'nand':

            com.Affichage.afficher(screen, nand_surface, nand_rectangle, 1)

            com.Affichage.afficher(screen, NANDgate_img, NANDgate_rectangle, 1)

            com.Affichage.afficher(screen, light_on_img, light_on_rectangle, 1)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] and keys[pygame.K_b]:
                  
                  com.Affichage.afficher(screen, light_off_img, light_off_rectangle, 1)

            if keys[pygame.K_a]:

                a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a_pressed.png')
                a_button = misc.Bouton(280, 300, a_button_img, 1)

            if keys[pygame.K_b]:

                b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b_pressed.png')
                b_button = misc.Bouton(280, 435, b_button_img, 1)

            a_button.afficher(screen)
   
            b_button.afficher(screen)

            a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a.png')
            a_button = misc.Bouton(280, 300, a_button_img, 1)

            b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b.png')
            b_button = misc.Bouton(280, 435, b_button_img, 1)

            if fleche_de_gauche_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'xor'
                clicked = True

            if fleche_de_droite_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'nor'
                clicked = True

        # Onglet "nor"

        if COURS_STATE == 'nor':

            com.Affichage.afficher(screen, nor_surface, nor_rectangle, 1)

            com.Affichage.afficher(screen, NORgate_img, NORgate_rectangle, 1)

            com.Affichage.afficher(screen, light_off_img, light_off_rectangle, 1)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] and keys[pygame.K_b]:
                  
                  com.Affichage.afficher(screen, light_on_img, light_on_rectangle, 1)

            if keys[pygame.K_a]:

                a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a_pressed.png')
                a_button = misc.Bouton(280, 300, a_button_img, 1)

            if keys[pygame.K_b]:

                b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b_pressed.png')
                b_button = misc.Bouton(280, 435, b_button_img, 1)

            a_button.afficher(screen)
   
            b_button.afficher(screen)

            a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a.png')
            a_button = misc.Bouton(280, 300, a_button_img, 1)

            b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b.png')
            b_button = misc.Bouton(280, 435, b_button_img, 1)

            if fleche_de_gauche_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'nand'
                clicked = True

            if fleche_de_droite_button.afficher(screen) == True and clicked == False:

                COURS_STATE = 'xnor'
                clicked = True

         # Onglet "xnor"

        if COURS_STATE == 'xnor':

            com.Affichage.afficher(screen, xnor_surface, xnor_rectangle, 1)

            com.Affichage.afficher(screen, XNORgate_img, XNORgate_rectangle, 1)

            com.Affichage.afficher(screen, light_off_img, light_off_rectangle, 1)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] and keys[pygame.K_b]:
                  
                  com.Affichage.afficher(screen, light_on_img, light_on_rectangle, 1)

            if keys[pygame.K_a]:

                a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a_pressed.png')
                a_button = misc.Bouton(280, 300, a_button_img, 1)

            if keys[pygame.K_b]:

                b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b_pressed.png')
                b_button = misc.Bouton(280, 435, b_button_img, 1)

            a_button.afficher(screen)
   
            b_button.afficher(screen)

            a_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_a.png')
            a_button = misc.Bouton(280, 300, a_button_img, 1)

            b_button_img = com.Affichage.chargementFichier('./graphics/buttons/circuit_buttons/button_b.png')
            b_button = misc.Bouton(280, 435, b_button_img, 1)

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