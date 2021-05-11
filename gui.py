import pygame

class ChoiceMenu(pygame.sprite.Sprite):
    def __init__(self, font, screen, tile_size):
        super().__init__()
        self.frame = pygame.Surface((tile_size*4, tile_size*4), pygame.SRCALPHA, 32)
        self.font = font
        self.screen = screen
        self.frame_rect = self.frame.get_rect(center = self.screen.get_rect().center)
        self.frame.fill((0,0,0,100))
        self.visible = False
    def draw(self, title, lb_text, rb_text):
        self.title = self.font.render(title, True, (255,255,255))
        self.left_btn = self.font.render(lb_text, True, (255,255,255))
        self.right_btn = self.font.render(rb_text, True, (255,255,255))
        self.title_rect = self.title.get_rect(centerx = self.frame_rect.centerx, centery = self.frame_rect.centery - self.frame_rect.height//4)
        self.left_btn_rect = self.left_btn.get_rect(centerx=self.frame_rect.centerx - self.frame_rect.width//4, y = self.frame_rect.centery)
        self.right_btn_rect = self.right_btn.get_rect(centerx=self.frame_rect.centerx + self.frame_rect.width//4, y = self.frame_rect.centery)
        self.screen.blit(self.frame, self.frame_rect)
        self.screen.blit(self.title, self.title_rect)
        self.screen.blit(self.left_btn, self.left_btn_rect)
        self.screen.blit(self.right_btn, self.right_btn_rect)
        if self.left_btn_rect.collidepoint(pygame.mouse.get_pos()):
            self.left_btn = self.font.render(lb_text, True, (200,0,0))
            self.screen.blit(self.left_btn, self.left_btn_rect)
        elif self.right_btn_rect.collidepoint(pygame.mouse.get_pos()):
            self.right_btn = self.font.render(rb_text, True, (200,0,0))
            self.screen.blit(self.right_btn, self.right_btn_rect)
        



if __name__ == "__main__":
    W = 800
    H = 800
    screen = pygame.display.set_mode((800,800))
    clock = pygame.time.Clock()
    tile_size = 40
    pygame.font.init()
    font = pygame.font.SysFont("Arial",15)
    menu = ChoiceMenu(font,screen, tile_size)
    game = True
    while game:
        screen.fill("light blue")
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                pass
        menu.draw("Переход хода", "Да", "Нет")
        pygame.display.update()
        clock.tick(24)