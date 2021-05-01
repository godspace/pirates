import pygame
from game_map import MapTiles
from city import City
from boat import Boat
from random import *
#test comment

pygame.font.init()
font = pygame.font.Font(None, 30)

W = 800
H = 800
tile_size = 40
boat_size = 30
screen = pygame.display.set_mode((800,800))

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

spawn_tile = choice(sea_tiles.city_list)
x = spawn_tile.rect.centerx
y = spawn_tile.rect.centery
boat = Boat(boat_size,x,y,screen,tile_size,sea_tiles)

game = True
while game:
    screen.fill("black")
    for tile in sea_tiles.map_list:
        tile.draw()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        boat.control(e)
        for port in port_list:
            port.menu_draw(e) 
    for port in port_list:
        port.draw() 
    boat.draw()
    pygame.display.update()
    pygame.time.delay(5)