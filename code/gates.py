import pygame
import pygame.sprite

class ANDgate(pygame.sprite.Sprite):

    def __init__(self, x, y, scale) -> None:

        super().__init__()
        self.image = pygame.image.load('./graphics/gates/ANDgate.png').convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))
        self.rectangle = self.image.get_rect()
        self.rectangle.center = (x, y)

    def afficher(self, surface):

        surface.blit(self.image, (self.rectangle.x, self.rectangle.y))

    def enlever(self):

        self.kill()

class NANDgate(pygame.sprite.Sprite):

    def __init__(self, x, y, scale) -> None:

        super().__init__()
        self.image = pygame.image.load('./graphics/gates/NANDgate.png').convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))
        self.rectangle = self.image.get_rect()
        self.rectangle.center = (x, y)

    def afficher(self, surface):

        surface.blit(self.image, (self.rectangle.x, self.rectangle.y))

    def enlever(self):

        self.kill()


class NORgate(pygame.sprite.Sprite):

    def __init__(self, x, y, scale) -> None:

        super().__init__()
        self.image = pygame.image.load('./graphics/gates/NORgate.png').convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))
        self.rectangle = self.image.get_rect()
        self.rectangle.center = (x, y)

    def afficher(self, surface):

        surface.blit(self.image, (self.rectangle.x, self.rectangle.y))

    def enlever(self):

        self.kill()


class NOTgate(pygame.sprite.Sprite):

    def __init__(self, x, y, scale) -> None:

        super().__init__()
        self.image = pygame.image.load('./graphics/gates/NOTgate.png').convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))
        self.rectangle = self.image.get_rect()
        self.rectangle.center = (x, y)

    def afficher(self, surface):

        surface.blit(self.image, (self.rectangle.x, self.rectangle.y))

    def enlever(self):

        self.kill()



class ORgate(pygame.sprite.Sprite):

    def __init__(self, x, y, scale) -> None:

        super().__init__()
        self.image = pygame.image.load('./graphics/gates/ORgate.png').convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))
        self.rectangle = self.image.get_rect()
        self.rectangle.center = (x, y)

    def afficher(self, surface):

        surface.blit(self.image, (self.rectangle.x, self.rectangle.y))

    def enlever(self):

        self.kill()



class XNORgate(pygame.sprite.Sprite):

    def __init__(self, x, y, scale) -> None:

        super().__init__()
        self.image = pygame.image.load('./graphics/gates/XNORgate.png').convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))
        self.rectangle = self.image.get_rect()
        self.rectangle.center = (x, y)

    def afficher(self, surface):

        surface.blit(self.image, (self.rectangle.x, self.rectangle.y))

    def enlever(self):

        self.kill()


class XORgate(pygame.sprite.Sprite):

    def __init__(self, x, y, scale) -> None:

        super().__init__()
        self.image = pygame.image.load('./graphics/gates/XORgate.png').convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))
        self.rectangle = self.image.get_rect()
        self.rectangle.center = (x, y)

    def afficher(self, surface):

        surface.blit(self.image, (self.rectangle.x, self.rectangle.y))

    def enlever(self):

        self.kill()

class WIREgate(pygame.sprite.Sprite):

    def __init__(self, x, y, scale) -> None:

        super().__init__()
        self.image = pygame.image.load('./graphics/gates/WIREgate.png').convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))
        self.rectangle = self.image.get_rect()
        self.rectangle.center = (x, y)

    def afficher(self, surface):

        surface.blit(self.image, (self.rectangle.x, self.rectangle.y))

    def enlever(self):

        self.kill()


class A_BUTTONgate(pygame.sprite.Sprite):

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

class B_BUTTONgate(pygame.sprite.Sprite):

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

class LIGHTgate(pygame.sprite.Sprite):

    def __init__(self, x, y, image_path, scale) -> None:

        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image2 = pygame.image.load(image_path).convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))
        self.rectangle = self.image.get_rect()
        self.rectangle.center = (x, y)

    def afficher(self, surface):

        surface.blit(self.image, (self.rectangle.x, self.rectangle.y))

    def enlever(self):

        self.kill()