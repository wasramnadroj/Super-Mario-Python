#
#CRISTIAN VALLEJO CDV SECTION E
#
import os,pygame,data,start,loading,game
from pygame.locals import *

def main():
    pygame.init()
    pygame.time.Clock
    pygame.mouse.set_visible(0)
    pygame.display.set_icon(pygame.image.load(data.filepath("luigi.png")))
    pygame.display.set_caption('Super Mario Bros. 3')
    screen = pygame.display.set_mode((640,460))
    loading.Load(screen,1)

#i used to do something to make this run here
#and then tooooooo many files to look at in one folder
#swag
#yolo
#no one will read these comments
#gucci

#placeholder