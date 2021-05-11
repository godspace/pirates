import pygame
import os
from random import *
from gui import *

class Boat(pygame.sprite.Sprite):
    def __init__(self,boat_size,x, y, screen, tile_size, sea_tiles, font, id):
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
        self.font = font
        self.items_menu()
        self.id = id
        self.can_move = True
        self.can_battle = False
        self.skip_menu = ChoiceMenu(self.font,self.screen, self.tile_size)
        self.battle_menu = ChoiceMenu(self.font,self.screen, self.tile_size)
    def items_menu(self):
        self.items = {"Вино":0, 
                    "Сахар":0, 
                    "Оружие":0,
                    "Украшения":0,
                    "Рабы":0,
                    "Монеты":100
                    }
        self.menu = pygame.Surface((self.tile_size*3, self.tile_size*4), pygame.SRCALPHA, 32)
        self.menu.fill((0,0,0,100))
        self.menu_visible = False
        self.text_rect = []
        self.keys = list(self.items.keys())
        
    def draw_menu(self):
        self.menu_rect = self.menu.get_rect(x = 0, y = 0)
        self.screen.blit(self.menu, self.menu_rect)
        self.text = []
        for item in self.items:
            self.text.append(self.font.render(item + ": " + str(self.items[item]), True, (255,255,255)))
        for item in self.text:    
            self.text_rect.append(item.get_rect())
        for i in range(len(self.items)):
            self.text_rect[i].x = self.menu_rect.x + 5
            self.text_rect[i].y = self.menu_rect.y + 10 + i*25
            self.screen.blit(self.text[i], (self.menu_rect.x + 5, self.menu_rect.y + 10 + i*25))
        if self.skip_menu.visible:        
            self.skip_menu.draw("Завершить ход", "Да", "Нет")
        if self.battle_menu.visible:        
            self.battle_menu.draw("Начать сражение", "Да", "Нет")


    def draw_boat(self):
        self.screen.blit(self.image, self.rect)

    def control(self,game):
            if pygame.mouse.get_pressed() == (True,False,False):
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    if game.can_route:
                        self.direction = choice('NESW')
                        self.speed = randint(1,3)
                        self.sea_tiles.route(self)
                        game.can_route = False
                    else:
                        self.skip_menu.visible = True
                elif self.skip_menu.visible and not self.battle_menu.visible:
                    if self.skip_menu.frame_rect.collidepoint(pygame.mouse.get_pos()):
                        if self.skip_menu.left_btn_rect.collidepoint(pygame.mouse.get_pos()):
                            game.next_player()
                            self.skip_menu.visible = False
                            for tile in self.sea_tiles.map_list:
                                tile.image.fill(tile.color)
                                tile.point = False
                        elif self.skip_menu.right_btn_rect.collidepoint(pygame.mouse.get_pos()):
                            self.skip_menu.visible = False
                elif self.battle_menu.visible:
                    if self.battle_menu.frame_rect.collidepoint(pygame.mouse.get_pos()):
                        if self.battle_menu.left_btn_rect.collidepoint(pygame.mouse.get_pos()):
                            print("FIGHT")
                            self.battle_menu.visible = False
                            for tile in self.sea_tiles.map_list:
                                tile.image.fill(tile.color)
                                tile.point = False
                            game.next_player()
                        elif self.battle_menu.right_btn_rect.collidepoint(pygame.mouse.get_pos()):
                            print("SKIP FIGHT")
                            self.battle_menu.visible = False
                            game.next_player()
                if self.can_move:
                    for tile in self.sea_tiles.map_list:
                        if tile.rect.collidepoint(pygame.mouse.get_pos()):
                            if tile.point:
                                self.rect.center = tile.rect.center
                                for i in range(len(game.players_list)):
                                    if i != game.turn:
                                        if pygame.sprite.collide_rect(game.players_list[i], self):
                                            self.can_battle = True
                                            self.battle_menu.visible = True
                                            print("Battle")
                                            
                                if not tile.city and not self.can_battle:
                                    game.next_player()
                                    print("NEXT")
                                for tile in self.sea_tiles.map_list:
                                    tile.image.fill(tile.color)
                                    tile.point = False
                                break
            
if __name__ == "__main__":
    W = 800
    H = 800
    screen = pygame.display.set_mode((800,800))
    tile_size = 40
    boat_size = 32
    sea_tiles = None
    boat = Boat(boat_size, 10*tile_size,10*tile_size,screen, tile_size, sea_tiles, font)
    game = True
    while game:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                boat.control()
        boat.draw()
        pygame.display.update()
        pygame.time.delay(5)
