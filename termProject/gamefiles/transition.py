import os,sys,pygame,select,data,game,levelgen
from pygame.locals import *

class TransitionScreen(object):

    def __init__(self,character,screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.player = character
        self.msg = 'You chose to play as %s!' % character
        pygame.display.set_caption(self.msg)
        self.font = pygame.font.Font(data.filepath('smb256.ttf'),28)
        self.image = 't%s.jpg' % character.lower()
        self.tscreen = pygame.transform.scale(data.load_image(self.image),(640,460))
        self.main_loop()

    def main_loop(self):
        while 1:
            self.clock.tick(60)
            events = pygame.event.get()
            for event in events:
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    select.Character(self.screen)    
                    return
                if event.type == KEYDOWN and event.key == K_RETURN:
                    game.Game(self.screen,self.player)
            self.screen.blit(self.tscreen,(0,0))
            pygame.display.flip()

