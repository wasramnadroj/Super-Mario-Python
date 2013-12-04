#
#code found around the web, examples are everywhere
#http://stackoverflow.com/questions/8328290/strange-pygame-image-error
#
#Not exact place where all these were found. ALL were found on stackoverflow
#CODE IS NOT MINE! :( i wish it was though
#
import os, pygame
from pygame.locals import *

data_py = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.normpath(os.path.join(data_py, '..', 'data'))

def filepath(filename):
    return os.path.join('data', filename)

def load(filename, mode='rb'):
    return open(os.path.join(data_dir, filename), mode)

def load_image(filename,mult=2):
    filename = filepath(filename)
    try:
        image = pygame.image.load(filename)
        image = pygame.transform.scale(image, (int(image.get_width()*mult),int(image.get_height()*mult)))
    except pygame.error:
        raise SystemExit, "Unable to load: " + filename
    return image.convert_alpha()

def load_sound(filename, volume=0.5):
    filename = filepath(filename)
    try:
        sound = pygame.mixer.Sound(filename)
        sound.set_volume(volume)
    except:
        raise SystemExit, "Unable to load: " + filename
    return sound

def play_music(filename, volume=0.5, loop=-1):
    filename = filepath(filename)
    try:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loop)
    except:
        raise SystemExit, "Unable to load: " + filename

def stop_music():
    pygame.mixer.music.stop()
