import pygame
import os
from random import *
from gui import *



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
        self.menu = pygame.Surface((self.tile_size*4, self.tile_size*4), pygame.SRCALPHA, 32)
        self.choice_menu = ChoiceMenu(self.font,self.screen, self.tile_size)
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
        self.text = []
        self.text_rect = []
        self.keys = list(self.buy.keys())
        for item in self.buy:
            self.text.append(self.font.render(item + ": " + str(self.buy[item]) + " / " + str(self.sell[item]), True, (255,255,255)))
        for item in self.text:    
            self.text_rect.append(item.get_rect())

    def draw(self):
        self.screen.blit(self.image, self.rect)
        if self.menu_visible:
            self.screen.blit(self.menu, self.menu_rect)
            for i in range(len(self.buy)):
                self.text_rect[i].x = self.menu_rect.x + 5
                self.text_rect[i].y = self.menu_rect.y + 10 + i*25
                self.screen.blit(self.text[i], (self.menu_rect.x + 5, self.menu_rect.y + 10 + i*25))
                if self.text_rect[i].collidepoint(pygame.mouse.get_pos()):
                    current_line = self.font.render(self.keys[i] + ": " + str(self.buy[self.keys[i]]) + " / " + str(self.sell[self.keys[i]]), True, (200,0,0))
                    self.screen.blit(current_line, (self.menu_rect.x + 5, self.menu_rect.y + 10 + i*25))
        if self.choice_menu.visible:
            self.choice_menu.draw(self.item, "Купить", "Продать")
            
    def menu_draw(self,boat):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed() == (False,False,True):                
                self.menu_visible = True
                boat.can_move = False
                boat.skip_menu.visible = False
            if pygame.mouse.get_pressed() == (True,False,False):
                self.choice_menu.visible = False
        elif self.menu_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.sprite.collide_rect(self, boat):
                if self.menu_visible:
                    for i in range(len(self.buy)):
                        if self.text_rect[i].collidepoint(pygame.mouse.get_pos()):
                            if pygame.mouse.get_pressed() == (True,False,False):
                                self.item = self.keys[i]
                                self.menu_visible = False
                                boat.skip_menu.visible = False
                                self.choice_menu.visible = True
        elif self.choice_menu.frame_rect.collidepoint(pygame.mouse.get_pos()):
            if self.choice_menu.visible:
                if pygame.sprite.collide_rect(self, boat):
                    if self.choice_menu.left_btn_rect.collidepoint(pygame.mouse.get_pos()):
                        if boat.items["Монеты"] >= self.sell[self.item]:
                            boat.items[self.item] += 1
                            boat.items["Монеты"] -= self.sell[self.item]
                            print(boat.items["Монеты"])
                    elif self.choice_menu.right_btn_rect.collidepoint(pygame.mouse.get_pos()):
                        if boat.items[self.item] >0:
                            boat.items[self.item] -= 1
                            boat.items["Монеты"] += self.buy[self.item]
                            print(boat.items["Монеты"])
                    else:
                        self.choice_menu.visible = False
        else:
            self.menu_visible = False
            self.choice_menu.visible = False
            if pygame.sprite.collide_rect(self, boat):
                boat.can_move = True


        

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
