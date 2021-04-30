import pygame
import os
from random import *

class Boat(pygame.sprite.Sprite):
    def __init__(self,boat_size,x, y, screen, tile_size, sea_tiles):
        file_dir = os.path.join(os.getcwd(),"PNG")
        fileobj = os.path.join(file_dir,"boat_icon_01.png")
        self.image = pygame.image.load(fileobj)
        self.image = pygame.transform.scale(self.image, (boat_size,boat_size))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.screen = screen
        self.tile_size = tile_size
        self.sea_tiles = sea_tiles
    def draw(self):
        self.screen.blit(self.image, self.rect)
    def control(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.direction = choice('NESW')
                    self.speed = randrange(3)
                    self.sea_tiles.route(self)
            for tile in self.sea_tiles.map_list:
                if tile.rect.collidepoint(pygame.mouse.get_pos()):
                    if tile.point:
                        self.rect.center = tile.rect.center
                        for tile in self.sea_tiles.map_list:
                            tile.image.fill(tile.color)
            

if __name__ == "__main__":
    W = 800
    H = 800
    screen = pygame.display.set_mode((800,800))
    tile_size = 40
    boat_size = 32
    sea_tiles = None
    boat = Boat(boat_size, 10*tile_size,10*tile_size,screen, tile_size, sea_tiles)
    game = True
    while game:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game = False
            boat.control(e)
        boat.draw()
        pygame.display.update()
        pygame.time.delay(5)
