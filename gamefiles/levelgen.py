import pygame,os,sys,data,math,random,sprites,artifacts
##idk what i'll need iMPORT EVERYTHING
from pygame.locals import *
from sprites import *
from artifacts import *

class Level(object):

    def __init__(self,level = 1):
        self.x = 0
        self.y = 0
        self.name = 'lvl%s.png'%level
        self.level = pygame.image.load(data.filepath(self.name)).convert()
        self.size = self.width()
        dictionary = get_sprites()

        for y in xrange(self.level.get_height()):
            self.y=y
            for x in xrange(self.level.get_width()):
                color = self.level.get_at((x,y))
                self.x=x
                key = ()
                for val in xrange(len(color)):
                    key += (color[val],)
                if dictionary[key] != None and dictionary[key] != False and key != (87, 0, 127, 255) and key != (255, 0, 220, 255):
                    dictionary[key](self.x,self.y)
                if key == (87, 0, 127, 255) or key == (255, 0, 220, 255):
                    dictionary[key](self.x,self.y,self.width())
                if dictionary[key] == False:
                    if color == ((0, 127, 127, 255)):
                        tile = 0
                        if self.check(-1,0) != color:
                            tile = 1
                        if self.check(1,0) != color:
                            tile = 2
                        if self.check(-1,0) != color and self.check(1,0) != color:
                            tile = 3
                        GrassSupport((self.x*32,self.y*32),tile)
                    if color == ((255, 127, 127, 255)):
                        tile = 0
                        if self.check(-1,0) != color:
                            tile = 1
                        if self.check(1,0) != color:
                            tile = 2
                        CrossGrass((self.x*32,self.y*32), tile)
                    if color == (10,80,10,255):
                        tile = 0
                        if self.check(0,-1) == color:
                            tile = 1
                        Lava((self.x*32,self.y*32),tile)
                    if color == (0,160,200,255):
                        orient = 0
                        if self.check(0,-1) != (255,255,255,255):
                            orient = 1
                        if orient == 1:
                            Spike((self.x*32.15,self.y*32),orient)
                        else:
                            Spike((self.x*32.15,self.y*26),orient)
                    if color == (0,0,0,255) or (0, 74, 127, 255) or (109,127,63,255) or (80,80,80,255):
                        orient = 0
                        if self.x != 0:
                            if self.check(-1,0) != color:
                                orient = 1
                        if self.x != self.width()/32-1:
                            if self.check(1,0) != color:
                                orient = 2
                        if color == (0, 74, 127, 255) or color == (109,127,63,255):
                            Brick((self.x*32,self.y*32),orient)
                        elif color == (0,0,0,255):
                            Platform((self.x*32,self.y*32),orient)
                        elif color == (80,80,80,255):
                            CastleBrick((self.x*32,self.y*32),orient)
                    if color == (214,127,255,255):
                        if self.x != 0:
                            BowserCastle((self.x*30,self.y*2))
                        else:
                            BowserCastle((-200,self.y*2))

    def width(self):
        return self.level.get_width()*32

    def check(self,dx,dy):
        return self.level.get_at((self.x+dx,self.y+dy))

#placeholder