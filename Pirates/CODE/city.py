import pygame
import os
from random import *

class City(pygame.sprite.Sprite):
    def __init__(self,boat_size,x, y, screen, tile_size, sea_tiles, font):
        file_dir = os.path.join(os.getcwd(),"PNG")
        fileobj = os.path.join(file_dir,"anchor.png")
        self.image = pygame.image.load(fileobj)
        self.image = pygame.transform.scale(self.image, (boat_size,boat_size))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.screen = screen
        self.tile_size = tile_size
        self.sea_tiles = sea_tiles
        self.font = font
        self.city_menu()
    def city_menu(self):
        self.menu = pygame.Surface((200, 200), pygame.SRCALPHA, 32)
        self.menu.fill((0,0,0,100))
        self.menu_visible = False
        self.menu_rect = self.menu.get_rect(center = self.rect.center)
        self.buy = {"Вино":randint(1, 7)*5, 
                    "Сахар":randint(5, 9)*5, 
                    "Оружие":randint(3, 12)*5,
                    "Украшения":randint(5, 18)*5,
                    "Рабы":randint(4, 15)*5,
                    }
        self.sell = {"Вино":self.buy["Вино"]+randint(1, 7)*5, 
                    "Сахар":self.buy["Сахар"]+randint(1, 7)*5, 
                    "Оружие":self.buy["Оружие"]+randint(1, 7)*5,
                    "Украшения":self.buy["Украшения"]+randint(1, 7)*5,
                    "Рабы":self.buy["Рабы"]+randint(1, 7)*5,
                    }
        self.text_vine = self.font.render("Вино: " + str(self.buy["Вино"]) + " / " + str(self.sell["Вино"]), True, (200,200,200))
        self.text_sugar = self.font.render("Сахар: " + str(self.buy["Сахар"]) + " / " + str(self.sell["Сахар"]), True, (200,200,200))
        self.text_armor = self.font.render("Оружие: " + str(self.buy["Оружие"]) + " / " + str(self.sell["Оружие"]), True, (200,200,200))
        self.text_gold = self.font.render("Украшения: " + str(self.buy["Украшения"]) + " / " + str(self.sell["Украшения"]), True, (200,200,200))
        self.text_slave = self.font.render("Рабы: " + str(self.buy["Рабы"]) + " / " + str(self.sell["Рабы"]), True, (200,200,200))
    def draw(self):
        self.screen.blit(self.image, self.rect)
        if self.menu_visible:
            self.screen.blit(self.menu, self.menu_rect)
            self.screen.blit(self.text_vine, (self.menu_rect.x + 5, self.menu_rect.y + 15))
            self.screen.blit(self.text_sugar, (self.menu_rect.x + 5, self.menu_rect.y + 50))
            self.screen.blit(self.text_armor, (self.menu_rect.x + 5, self.menu_rect.y + 85))
            self.screen.blit(self.text_gold, (self.menu_rect.x + 5, self.menu_rect.y + 120))
            self.screen.blit(self.text_slave, (self.menu_rect.x + 5, self.menu_rect.y + 155))
    def menu_draw(self,event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                if self.menu_rect.collidepoint(pygame.mouse.get_pos()):
                    self.menu_visible = True
            if not self.menu_rect.collidepoint(pygame.mouse.get_pos()):
                self.menu_visible = False
                    
            

if __name__ == "__main__":
    W = 800
    H = 800
    pygame.font.init()
    font = pygame.font.Font(None, 20)
    screen = pygame.display.set_mode((800,800))
    tile_size = 40
    boat_size = 32
    sea_tiles = None
    city = City(boat_size, 10*tile_size,10*tile_size,screen, tile_size, sea_tiles, font)
    game = True
    while game:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game = False
        city.draw()
        pygame.display.update()
        pygame.time.delay(5)
