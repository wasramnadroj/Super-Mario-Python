import os, pygame
from pygame.locals import *

data_py = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.normpath(os.path.join(data_py, '..', 'data'))

def filepath(filename):
    return os.path.join('data', filename)

def load(filename, mode='rb'):
    return open(os.path.join(data_dir, filename), mode)

def load_image(filename,mult=2):
    print filename
    filename = filepath(filename)
    f = open(filename, 'rb')
    f.seek(0)
    image = pygame.image.load(f, filename)
    image = pygame.transform.scale(image, (int(image.get_width()*mult),int(image.get_height()*mult)))
    return image.convert_alpha()

def load_sound(filename, volume=0.5):
    filename = filepath(filename)
    print filename
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
