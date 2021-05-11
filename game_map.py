import pygame
from random import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y, color, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size - 1, size - 1))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = color
        self.screen = screen
        self.point = False
        self.city = False
        self.image.fill(self.color)
    def draw(self):
        self.screen.blit(self.image, self.rect)

class MapTiles():
    def __init__(self,W,H,tile_size,screen):
        self.map_list = []
        self.city_N = []
        self.city_E = []
        self.city_S = []
        self.city_W = []
        self.city_list = []
        self.tile_size = tile_size
        self.w = round(W/tile_size)
        self.h = round(H/tile_size)
        self.size = tile_size
        for j in range(self.h):
            for i in range(self.w):
                if randrange(3) < i < self.w - randrange(4) and randrange(3) < j < self.h - randrange(4):
                    self.color = (0, 100, 200)
                else:
                    self.color = (randint(100, 150), randint(100, 150), randint(50, 100))
                if self.w//2 - randint(1,3) < i < self.w//2 + randint(1,3) and self.h//2 - randint(1,3) < j < self.h//2 + randint(1,3):
                    self.color = (randint(100, 150), randint(100, 150), randint(50, 100))
                self.map_list.append(Tile(tile_size, i*tile_size, j*tile_size, self.color, screen))
    def route(self, boat):
        for tile in self.map_list:
            if tile.color == (0, 100, 200):
                tile.image.fill(tile.color)
                tile.point = False
                if tile.rect.center != boat.rect.center:
                    if boat.direction == "N":
                        if tile.rect.centerx == boat.rect.centerx:
                            if tile.rect.centery < boat.rect.centery and tile.rect.centery >= boat.rect.centery - boat.speed * self.size * 2:
                                pygame.draw.circle(tile.image, (255,0,0), (tile.rect.width/2,tile.rect.height/2), self.size/4)
                                tile.point = True
                        if tile.rect.centery == boat.rect.centery: 
                            if tile.rect.centerx >= boat.rect.centerx - boat.speed * self.size and tile.rect.centerx <= boat.rect.centerx + boat.speed * self.size:
                                pygame.draw.circle(tile.image, (255,0,0), (tile.rect.width/2,tile.rect.height/2), self.size/4)
                                tile.point = True
                    if boat.direction == "S":
                        if tile.rect.centerx == boat.rect.centerx:
                            if tile.rect.centery > boat.rect.centery and tile.rect.centery <= boat.rect.centery + boat.speed * self.size * 2:
                                pygame.draw.circle(tile.image, (255,0,0), (tile.rect.width/2,tile.rect.height/2), self.size/4)
                                tile.point = True
                        if tile.rect.centery == boat.rect.centery: 
                            if tile.rect.centerx >= boat.rect.centerx - boat.speed * self.size and tile.rect.centerx <= boat.rect.centerx + boat.speed * self.size:
                                pygame.draw.circle(tile.image, (255,0,0), (tile.rect.width/2,tile.rect.height/2), self.size/4)
                                tile.point = True
                    if boat.direction == "E":
                        if tile.rect.centery == boat.rect.centery:
                            if tile.rect.centerx > boat.rect.centerx and tile.rect.centerx <= boat.rect.centerx + boat.speed * self.size * 2:
                                pygame.draw.circle(tile.image, (255,0,0), (tile.rect.width/2,tile.rect.height/2), self.size/4)
                                tile.point = True
                        if tile.rect.centerx == boat.rect.centerx: 
                            if tile.rect.centery >= boat.rect.centery - boat.speed * self.size and tile.rect.centery <= boat.rect.centery + boat.speed * self.size:
                                pygame.draw.circle(tile.image, (255,0,0), (tile.rect.width/2,tile.rect.height/2), self.size/4)
                                tile.point = True
                    if boat.direction == "W":
                        if tile.rect.centery == boat.rect.centery:
                            if tile.rect.centerx < boat.rect.centerx and tile.rect.centerx >= boat.rect.centerx - boat.speed * self.size * 2:
                                pygame.draw.circle(tile.image, (255,0,0), (tile.rect.width/2,tile.rect.height/2), self.size/4)    
                                tile.point = True
                        if tile.rect.centerx == boat.rect.centerx: 
                            if tile.rect.centery >= boat.rect.centery - boat.speed * self.size and tile.rect.centery <= boat.rect.centery + boat.speed * self.size:
                                pygame.draw.circle(tile.image, (255,0,0), (tile.rect.width/2,tile.rect.height/2), self.size/4)
                                tile.point = True
    def set_city(self):
        for tile in self.map_list:
            if tile.color == (0, 100, 200):
                if tile.rect.x == self.size * 2 and tile.rect.y > self.size * 2 and tile.rect.y < (self.h - 3) * self.size:
                    self.city_W.append(tile)
                if tile.rect.x == (self.w - 3) * self.size and tile.rect.y > self.size * 2 and tile.rect.y < (self.h - 3) * self.size:
                    self.city_E.append(tile)
                if tile.rect.y == self.size * 2 and tile.rect.x > self.size * 2 and tile.rect.x < (self.w - 3) * self.size:
                    self.city_N.append(tile)
                if tile.rect.y == (self.h - 3) * self.size and tile.rect.x > self.size * 2 and tile.rect.x < (self.w - 3) * self.size:
                    self.city_S.append(tile)
        self.city_list = [self.city_W[len(self.city_W)//4],
                            self.city_W[-len(self.city_W)//4],
                            self.city_E[len(self.city_E)//4],
                            self.city_E[-len(self.city_E)//4],
                            self.city_N[len(self.city_N)//4],
                            self.city_N[-len(self.city_N)//4],
                            self.city_S[len(self.city_S)//4],
                            self.city_S[-len(self.city_S)//4]]
        for city in self.city_list:
            city.city = True
if __name__ == "__main__":
    W = 800
    H = 800
    tile_size = 40
    screen = pygame.display.set_mode((800,800))

    sea_tiles = MapTiles(W,H,tile_size,screen)
    game = True
    while game:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game = False
        for tile in sea_tiles.map_list:
            tile.draw()
        if pygame.mouse.get_pressed()[0]:
            for tile in sea_tiles.map_list:
                if tile.rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.circle(tile.image, (255,0,0), (tile.rect.width/2,tile.rect.height/2), tile_size/4)
        pygame.display.update()
        pygame.time.delay(5)
