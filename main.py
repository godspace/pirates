import pygame
from game_map import MapTiles
from city import City
from boat import Boat
from random import *

pygame.font.init()
font = pygame.font.SysFont("Arial",15)

W = 800
H = 800
tile_size = 40
boat_size = 30
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
sea_tiles = MapTiles(W,H,tile_size, screen)
sea_tiles.set_city()

water = []
for tile in sea_tiles.map_list:
    if tile.color == (0, 100, 200):
        water.append(tile)
port_list = []
for city in sea_tiles.city_list:
    x = city.rect.centerx
    y = city.rect.centery
    port = City(boat_size,x,y,screen,tile_size,sea_tiles,font)
    port_list.append(port)

class Game():
    def __init__(self, players):
        self.players = players
        self.run = True
        self.turn = 0
        self.can_route = True
        self.players_list = []
    def next_player(self):
        self.turn += 1
        self.can_route = True
        if self.turn == self.players:
            self.turn = 0
game = Game(2)
spawn_city = sea_tiles.city_list.copy()

for i in range(game.players):
    spawn_tile = choice(spawn_city)
    spawn_city.remove(spawn_tile)
    x = spawn_tile.rect.centerx
    y = spawn_tile.rect.centery
    boat = Boat(boat_size,x,y,screen,tile_size,sea_tiles,font,i)
    game.players_list.append(boat)
while game.run:
    screen.fill("black")
    for tile in sea_tiles.map_list:
        tile.draw()
    for port in port_list:
        port.draw()
    for player in game.players_list:
        player.draw_boat()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game.run = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            game.players_list[game.turn].control(game)
            for port in port_list:
                port.menu_draw(game.players_list[game.turn]) 
    
    game.players_list[game.turn].draw_menu()
    pygame.display.update()
    clock.tick(24)