#
#
#

import pygame,os,sys,start,data,easter
from pygame.locals import *

class Rules(object):

    def __init__(self,screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.rulesheet = pygame.transform.scale(data.load_image('rules.bmp'),(640,460))
        self.font = pygame.font.Font(data.filepath('smb256.ttf'),28)
        self.font2 = pygame.font.Font(None,14)
        pygame.display.set_caption('Super Mario Bros. 3 Help')
        self.main_loop()

    def main_loop(self):
        while 1:
            self.clock.tick(60)
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    pygame.quit()
                    return
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    start.Menu(self.screen)
                    return
                if event.type == KEYDOWN and event.key == K_RETURN:
                    easter.Egg(self.screen)
                    return


            self.screen.blit(self.rulesheet,(0,0))
            text = self.font.render('--How to play--',1,(255,255,255))
            self.screen.blit(text,(180,50))
            text = self.font.render('Left and Right',1,(255,255,255))
            self.screen.blit(text,(200,100))
            text = self.font.render('Arrow keys to',1,(255,255,255))
            self.screen.blit(text,(200,140))
            text = self.font.render('move',1,(255,255,255))
            self.screen.blit(text,(280,180))
            text = self.font.render('Space to jump',1,(0,255,0))
            self.screen.blit(text,(200,240))
            text = self.font.render('Jump on enemies',1,(255,255,255))
            self.screen.blit(text,(260,300))
            text = self.font.render('to kill them!',1,(255,255,255))
            self.screen.blit(text,(275,340))
            text = self.font.render('ESC to return',1,(255,0,0))
            self.screen.blit(text,(260,400))
            text = self.font.render('to title screen',1,(255,0,0))
            self.screen.blit(text,(260,430))
            text = self.font2.render('Press Enter for Easter Egg!',1,(45,45,45))
            self.screen.blit(text,(80,30))
            pygame.display.flip()






#placeholder