import os,sys,pygame,data
from pygame.locals import *
from Spritesheet import Spritesheet

class Level():
    tilesize = 15
    numxtiles = 43
    numytiles = 31
    def __init__(self):
        self.background = pygame.Surface((640,480)).convert()
    def drawtile(self,tile,x,y):
        self.background.blit(tile,(x*self.tilesize,y*self.tilesize))
    def makebg(self,tilenum):
        for x in xrange(self.numxtiles):
            for y in xrange(self.numytiles):
                self.drawtile(self.tiles[tilenum],x,y)
        self.world()
    def world(self):
        for x1 in xrange(self.numxtiles):
            self.background.blit(self.tiles[1],(x1*self.tilesize,435))
            self.background.blit(self.tiles[1],(x1*self.tilesize,450))
        self.background.blit(self.hills[0],(0,420))
        self.background.blit(self.hills[1],(15,405))
        self.background.blit(self.hills[2],(30,403))
        self.background.blit(self.hills[3],(45,405))
        self.background.blit(self.hills[4],(60,420))
        self.background.blit(self.tiles[2],(30,420))

def main():
    pygame.init()
    pygame.time.Clock
    pygame.mixer.music.load(data.filepath('title.wav'))
    pygame.mixer.music.play(-1)
    pygame.mouse.set_visible(1)
    pygame.display.set_caption('Super Mario Bros.')
    screen = pygame.display.set_mode((640,460))
    spritesheet = Spritesheet('mario.png')
    level = Level()
    Level.tiles = spritesheet.imgsat([(48,336,15,15),
                                      (0, 0, 15, 15),
                                      (144,144,15,15)])
    Level.hills = spritesheet.imgsat([(128,128,15,15),
                                      (128,128,15,30),
                                      (144,141,15,18),
                                      (160,128,15,31),
                                      (160,128,15,15)],-1)
    level.makebg(0)
    screen.blit(level.background,(0,0))
    while 1:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return



if __name__ == '__main__': main()