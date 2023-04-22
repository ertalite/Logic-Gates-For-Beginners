import pygame

class Bouton:

    def __init__(self, x, y, image, scale) -> None:

        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def afficher(self, surface):

        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))


        print(self.clicked)
        return action
    