import pygame, sys

#-----------------------------[ Fonctions jeu ]------------------
class Affichage:

    def chargementPolice(chemin:str, taille):
        '''
        Permet de charger une police.
        '''
        return pygame.font.Font(chemin, taille)

    def creerTexte(police, texte:str, AA:bool, couleur:str):
        '''
        Permet de créer un texte pour pouvoir l'afficher.
        '''
        return police.render(str(texte), AA, str(couleur))

    def chargementFichier(chemin:str):
        '''
        Permet de charger une image, un ficher.
        '''
        return pygame.image.load(str(chemin)).convert_alpha()

    def afficher(screen, surface, pos, scale):
        '''
        Affiche une surface sur l'écran.
        '''
        return screen.blit(surface, pos)
    
    def redimensionner(objet, scale):
        '''
        Redimensionne un objet passé en paramètres.
        '''
        width = objet.get_width()
        height = objet.get_height()
        return pygame.transform.scale(objet, (int(width * scale), int(height * scale)))

class Collision:

    def creerRectangle(surface, direction, pos:tuple):
        '''
        Permet de creer un rectangle que l'on applique à une surface.
        '''
        if direction == 'center':

            return surface.get_rect(center = pos)

        if direction == 'midbottom':

            return surface.get_rect(midbottom = pos)
        
        if direction == 'topleft':

            return surface.get_rect(topleft = pos)

    def dessinerRectangle(screen, couleur, pos, taille):
        '''
        Permet de dessiner un rectangle.
        '''
        return pygame.draw.rect(screen, couleur, pos, taille)

    def collisionRectangle():
        '''
        Renvoie un booléen correspondant à:
            1: pour une collision.
            0: dans le cas échéant.
        '''
        pass

    def collisionSouris():
        '''
        Renvoie un booléen correspondant à la collision entre la souris et un objet:
            1: pour une collision.
            0: dans le cas échéant.
        '''
        pass

class Position:

    def mouvementSouris():
        '''
        Renvoie un booléen si la souris est en mouvement.
        '''
        return event.type == pygame.MOUSEMOTION

    def positionSourisEvent():
        '''
        Renvoie un tuple contenant la position de la souris (pour la boucle de jeu) (x, y).
        '''
        return event.pos

    def positionSouris():
        '''
        Renvoie un tuple contenant la position de la souris (x, y).
        '''
        return pygame.mouse.get_pos()


#-----------------------------[ Keyboard inputs ]------------------

class Keyboard:

    def pressed(key):

        keys = pygame.key.get_pressed()

        if keys[key]:

             return True



    def release(key):
        
        pass

#-----------------------------[ Paramètres ]------------------

def setKey(newKey):
    pass