import os,pygame,start,data,game
from pygame.locals import *

def main():
    pygame.init()
    pygame.time.Clock
    pygame.mouse.set_visible(0)
    pygame.display.set_icon(pygame.image.load(data.filepath("luigi.png")))
    pygame.display.set_caption('Super Mario Bros. 3')
    screen = pygame.display.set_mode((640,460))
    start.Menu(screen)

if __name__ == "__main__":
    main()
