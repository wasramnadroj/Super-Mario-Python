import pygame, data,os, sys,start, save,random
from pygame.locals import *

class Load(object):

    def __init__(self,screen,start=0):
        self.screen = screen
        self.start = start
        self.clock = pygame.time.Clock()
        self.time = random.choice(xrange(4000,7000))
        self.count = 3
        self.image = pygame.image.load(data.filepath('load.bmp'))
        data.play_music('load.wav')
        self.main_loop()

    def main_loop(self):
        while 1:
            self.clock.tick(60)
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    sys.exit()
                    return
            if pygame.time.get_ticks() > self.time and self.start == 1:
                pygame.mixer.music.fadeout(2000)
                start.Menu(self.screen)

            self.screen.blit(self.image,(0,0))
            pygame.display.flip()
