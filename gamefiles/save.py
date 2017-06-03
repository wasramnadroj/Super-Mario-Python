import pygame, data, os, sys, start,genmenu, savefile, game
from pygame.locals import *
from genmenu import *
from savefile import *


def s0(screen,saves):
    if saves != []:
        toon = saves[0]
        level = (int(saves[1][0])-1)*4+int((saves[1][2]))
        lives = int(saves[2])
        game.Game(screen,toon,level,lives)
    else:
        print 'There is no game file!'
    #initialize game as this plaer

class Save(object):

    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.image = pygame.image.load(data.filepath('save.bmp'))
        data.play_music('save.wav')
        self.font = pygame.font.Font(data.filepath('smb256.ttf'),28)
        self.font2 = pygame.font.Font(data.filepath('smb256.ttf'),24)
        self.saves = savefile.Savefile().read() #MAX read of 3 at the moment
        pygame.display.set_caption('Load Game')
        if self.makeMenu() != False:
            self.state = True
        else: self.state = self.makeMenu()
        if self.state:
            self.menu.changeFont('smb256.ttf',28)
            self.menu.position(200,120)
            self.menu.defaultColor((0,0,0))
            self.menu.choiceColor((255,0,125))
        self.main_loop()

    def makeMenu(self):
        if self.saves == []:
            return False
        else:
            saves = self.saves
            save1,save2,save3 = 'FILE OPEN','FILE OPEN', 'FILE OPEN'
            if saves[0] != []:
                save1 = saves[0][0]+' '+saves[0][1]
            if saves[1] != []:
                save2 = saves[1][0]+' '+saves[1][1]
            if saves[2] != []:
                save3 = saves[2][0]+' '+saves[2][1]
            self.menu = genmenu([save1, lambda: s0(self.screen,saves[0])],[save2, lambda: s0(self.screen,saves[1])],[save3,lambda: s0(self.screen,saves[2])])

    def main_loop(self):
        while 1:
            self.clock.tick(60)
            events = pygame.event.get()
            if self.state:
               self.menu.choose(events)
            for event in events:
                if event.type == QUIT:
                    sys.exit()
                    return
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.mixer.music.fadeout(2000)
                    start.Menu(self.screen)
                    return

            self.screen.blit(self.image,(0,0))
            if self.state:
                events = pygame.event.get()
                self.menu.create(self.screen)
                self.menu.choose(events)
            else:
                text = self.font.render('No saved games yet!',1,(0,0,0))
                self.screen.blit(text,(110,230))
            text = self.font2.render('Press         to return to title.',1,(0,0,0,0))
            self.screen.blit(text,(30,400))
            text = self.font2.render('ESCAPE',1,(255,0,0))
            self.screen.blit(text,(120, 400))
            text = self.font2.render('Press         to load saved game.',1,(0,0,0))
            self.screen.blit(text,(30,425))
            text =  self.font2.render('Enter',1,(34,139,34))
            self.screen.blit(text,(120,425))
            text= self.font.render('Highscore',1,(255,255,255))
            self.screen.blit(text,(630-text.get_width(),80))
            text=self.font.render('________',1,(255,255,255))
            self.screen.blit(text,(630-text.get_width(),85))
            if savefile.Savefile('scores.txt').readscore() == None:
                msg = 'None'
            else:
                msg = str(savefile.Savefile('scores.txt').readscore())
            distance = (630-468)/2
            text=self.font2.render(msg,1,(255,0,0))
            self.screen.blit(text,(630-distance-text.get_width()/2,115))
            pygame.display.flip()









##        