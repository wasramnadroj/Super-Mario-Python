import pygame,os,sys,data,charMenu,start,game
from pygame.locals import *
from charMenu import *

def playMario(screen):
    data.play_music('pickmario.wav',1,1)
    game.Game(screen, 'Mario')
    pass

def playLuigi(screen):
    data.play_music('pickluigi.wav',1,1)
    game.Game(screen, 'Luigi')
    pass

def playToad(screen):
    data.play_music('picktoad.wav',1,1)
    game.Game(screen, 'Toad')
    pass

def playPokemonTrainer(screen):
    data.play_music('pickyoshi.wav',1,1)
    game.Game(screen, 'Yoshi')
    pass

class Character():

    def __init__(self,screen):
        self.screen = screen
        self.title = pygame.transform.scale(data.load_image('select.png'),(640,460))
        self.menu = charMenu(['Mario', lambda: playMario(screen)],['Luigi', lambda: playLuigi(screen)], ['Toad', lambda: playToad(screen)], ['Yoshi', lambda: playPokemonTrainer(screen)])
        self.menu.changeFont('smb256.ttf',28)
        self.menu.position(100,375)
        self.menu.setSpace(15)
        self.menu.choiceColor((255,0,125))
        self.font = pygame.font.Font(data.filepath('smb256.ttf'),28)
        self.clock = pygame.time.Clock()
        events = pygame.event.get()
        data.play_music('characterselect.wav')
        event = pygame.event.get()
        pygame.display.set_caption('Character Selection')
        self.menu.create(self.screen)
        self.menu.choose(event)
        self.main_loop()

    def main_loop(self):
        while 1:
            self.clock.tick(60)
            events = pygame.event.get()
            self.menu.choose(events)
            for event in events:
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.mixer.music.fadeout(1000)
                    start.Menu(self.screen)
                    return

            self.screen.blit(self.title, (0, 0))

            text = self.font.render('Choose your character!',1,(255,255,255))
            self.screen.blit(text,(120,140))
            mario = pygame.transform.scale(data.load_image('mchar.png'),(125,125))
            self.screen.blit(mario,(105,215))
            luigi = pygame.transform.scale(data.load_image('lchar.png'),(75,125))
            self.screen.blit(luigi,(220,215))
            toad = pygame.transform.scale(data.load_image('tchar.png'),(120,125))
            self.screen.blit(toad,(315,215))
            yoshi = pygame.transform.scale(data.load_image('yoshi.png'),(75,125))
            self.screen.blit(yoshi,(440,215))
            self.menu.create(self.screen)
            pygame.display.flip()
