import pygame,sys,data,select,start,rules,save
from pygame.locals import *
from genmenu import *

def quit():
    sys.exit()

def placeholder1(screen):
    pygame.mixer.music.fadeout(1500)
    select.Character(screen)
    pass

def placeholder2(screen):
    pygame.mixer.music.fadeout(1500)
    save.Save(screen)
    pass

def placeholder3(screen):
    pygame.mixer.music.fadeout(1500)
    rules.Rules(screen)
    pass

class Menu(object):

    def __init__(self,screen):
        self.screen = screen
        self.title = pygame.transform.scale(data.load_image('sm3.png'),(640,460))
        self.menu = genmenu(['START', lambda: placeholder1(screen)],['RESUME', lambda: placeholder2(screen)], ['QUIT', lambda: quit()])
        self.menu.changeFont('smb256.ttf',28)
        self.menu.position(430,260)
        self.menu.defaultColor((0,0,0))
        self.menu.choiceColor((255,0,125))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Super Mario Bros. 3')
        data.play_music('title.wav')
        event = pygame.event.get()
        self.menu.create(self.screen)
        self.menu.choose(event)
        self.main_loop()

    def main_loop(self):
        while 1:
            self.clock.tick(60)
            events = pygame.event.get()
            self.menu.choose(events)
            for event in events:
                if event.type == QUIT:
                    sys.exit()
                    return
            self.screen.blit(self.title, (0, 0))
            self.menu.create(self.screen)
            pygame.display.flip()
