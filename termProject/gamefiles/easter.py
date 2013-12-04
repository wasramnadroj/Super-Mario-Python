import os,sys,rules,pygame,data
from pygame.locals import *

class Egg(object):

    def __init__(self,screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.fox = pygame.transform.scale(data.load_image('fox.bmp'),(640,460))
        self.font = pygame.font.Font(data.filepath('smb256.ttf'),28)
        data.play_music('fox.wav')
        pygame.display.set_caption('WHAT DOES THE FOX SAY?!')
        self.main_loop()


    def main_loop(self):
        while 1:
            self.clock.tick(60)
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    sys.exit()
                    return
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.mixer.music.fadeout(2000)
                    rules.Rules(self.screen)
                    return

            self.screen.blit(self.fox,(0,0))
            pygame.display.flip()