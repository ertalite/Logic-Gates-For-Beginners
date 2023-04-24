import pygame
import pygame.sprite

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

        return action
    
class Light(pygame.sprite.Sprite):

    def __init__(self, x, y, image_path, scale) -> None:

        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))
        self.rectangle = self.image.get_rect()
        self.rectangle.center = (x, y)

    def afficher(self, surface):

        surface.blit(self.image, (self.rectangle.x, self.rectangle.y))

    def enlever(self):

        self.kill()