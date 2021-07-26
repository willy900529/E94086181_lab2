import pygame
import time

WIN_WIDTH = 1024
WIN_HEIGHT = 600
BTN_WIDTH = 80
BTN_HEIGHT = 80
HP_WIDTH = 40
HP_HEIGHT = 40
FPS = 30

# color (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# initialization
pygame.init()
# load image (background, enemy, buttons)
# ...(to be done)
#construct various picture
background_image = pygame.transform.scale(pygame.image.load("images/Map.png"), (WIN_WIDTH, WIN_HEIGHT))
background_enemy = pygame.transform.scale(pygame.image.load("images/enemy.png"), (60, 60))
background_myself_HP_have= pygame.transform.scale(pygame.image.load("images/hp.png"), (HP_WIDTH, HP_HEIGHT))
background_myself_HP_loss= pygame.transform.scale(pygame.image.load("images/hp_gray.png"), (HP_WIDTH, HP_HEIGHT))
background_continue= pygame.transform.scale(pygame.image.load("images/continue.png"), (BTN_WIDTH, BTN_WIDTH))
background_muse= pygame.transform.scale(pygame.image.load("images/muse.png"), (BTN_WIDTH, BTN_WIDTH))
background_pause= pygame.transform.scale(pygame.image.load("images/pause.png"), (BTN_WIDTH, BTN_WIDTH))
background_sound= pygame.transform.scale(pygame.image.load("images/sound.png"), (BTN_WIDTH, BTN_WIDTH))
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# set the title
# ... (to be done)
pygame.display.set_caption("My first game")

class Game:
    def __init__(self):
        # window
        # ...(to be done)

        # hp
        self.hp = 7
        self.max_hp = 10
        pass

    def game_run(self):
        # game loop
        run = True
        while run:
            # event loop
                # ... (to be done)
            for event in pygame.event.get(): #can make my code over
                if event.type == pygame.QUIT:
                    run = False
            # draw background
            # ...(to be done)
            win.blit(background_image, (0, 0))
            # draw enemy and health bar
            # ...(to be done)
            #win.blit(background_image, (0, 0))
            pygame.draw.rect(win, RED, [40, 250, 50, 5]) #construct  background
            win.blit(background_enemy, (35, 250))  #construct  background_enemy
            # draw menu (and buttons)
            # (... to be done)
            pygame.draw.rect(win, BLACK, [0, 0, 1024, 80])
            #construct buttons
            win.blit(background_muse, (700, 0))
            win.blit(background_sound, (780, 0))
            win.blit(background_continue, (860, 0))
            win.blit(background_pause, (940, 0))
            #construct myself HP
            for i in range(412,573,40):
                win.blit(background_myself_HP_have, (i, 0))
            for i in range(412,453,40):
                win.blit(background_myself_HP_have, (i, 40))
            for i in range(492, 573, 40):
                win.blit(background_myself_HP_loss, (i, 40))
            # draw time
            # ...(to be done)=
            game_second=pygame.time.get_ticks()//1000 #calculate the time when code is running
            game_minute=game_second//60  #convert second to minute
            self.font=pygame.font.SysFont("simhei", 50)  #set up 字體 and 大小
            #set up the information of time
            text_surface = self.font.render("  "+str(game_minute)+":"+str(game_second%60).zfill(2)+"  ",True,(255,255,255),BLACK)
            win.blit(text_surface,(0,566))  #put text_surface to windows

            pygame.display.update()

if __name__ == "__main__":
    covid_game = Game()
    covid_game.game_run()



