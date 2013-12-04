import pygame,sys,data,select,start,rules,save
from pygame.locals import *
from genmenu import *

def quit():
    print 'Have a nice day!'
    sys.exit()

def placeholder1(screen):
    # SHOULD EXEXCUTE PLAYER CHOOSE 
    # CHARACTER SCREEN FIRST.
    # then...
    # game should load into world 1-1
    # interface should display:
    # lives
    # world number
    # points
    # time left
    # player sprite??
    pygame.mixer.music.fadeout(1500)
    select.Character(screen)
    pass

def placeholder2(screen):
    # need to save what world and 
    # character the player was using at 
    # the last exit of the game
    # potential for saving multiple players
    # for now will just have one save file
    # not sure what i want to do with this 
    # yet
    pygame.mixer.music.fadeout(1500)
    save.Save(screen)
    pass

def placeholder3(screen):
    # the how to play basically shows instructions...
    # that's all there really is to do here.
    # currently the controls will be
    # up is jump. maybe. or spacebar.
    # left and right are move left or right
    # tentative plan to implement shift as a run 
    # this run would have to be limited though. maybe. 
    # sliding? maybe. I'm not sure of it's use or practicality in the game
    # maybe i will explain what different enemies due
    pygame.mixer.music.fadeout(1500)
    rules.Rules(screen)
    pass

class Menu(object):

    def __init__(self,screen):
        self.screen = screen
        self.title = pygame.transform.scale(data.load_image('sm3.png'),(640,460))
        self.menu = genmenu(['START', lambda: placeholder1(screen)],['RESUME', lambda: placeholder2(screen)], ['HOW TO PLAY', lambda: placeholder3(screen)], ['QUIT', lambda: quit()])
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









### placeholder
