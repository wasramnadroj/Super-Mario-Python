import sprites
from sprites import *

def get_sprites():
    sprites = {}
    sprites[(0,0,0,255)] = False #platform
    sprites[(0,19,127,255)] = lambda x,y: GrassMiddle((x*32,y*32))
    sprites[(109,127,63,255)] = False #brick
    sprites[(255,200,0,255)] = lambda x,y: JumpPlatform((x*32,y*32))
    sprites[(127, 51, 0, 255)] = lambda x,y: Question((x*32,y*32))
    sprites[(65,115,30,255)] = lambda x,y: CoinQuestion((x*32,y*32))
    sprites[(107,133,170,255)] = lambda x,y: MushroomQuestion((x*32,y*32))
    sprites[(146,147,29,255)] = lambda x,y: BrickQuestion((x*32,y*32))
    sprites[(40,60,130,255)] = lambda x,y: Bowser((x*32,y*30))
    sprites[(50,100,70,255)] = lambda x, y: Bridge((x*32,y*32))
    sprites[(0, 74, 127, 255)] = False #brick
    sprites[(91, 127, 0, 255)] = lambda x,y: Pipe((x*32,y*28))
    sprites[(87, 0, 127, 255)] = lambda x,y,width: Cloud((x*32,y*32), width)
    sprites[(127, 0, 55, 255)] = lambda x,y: Bush((x*32,y*32))
    sprites[(80, 63, 127, 255)] = lambda x,y: Castle((x*32,y*16))
    sprites[(0,160,200,255)] = False #spike
    sprites[(190,220,200,255)] = lambda x,y: Switch((x*32,y*32))
    sprites[(100,120,140,255)] = lambda x,y: PeachCastle((x*28.95,y*4.92))
    sprites[(10,80,10,255)] = False #lava
    sprites[(80,80,80,255)] = False #lambda x,y: CastleBrick((x*32,y*32))
    sprites[(255, 233, 127, 255)] = lambda x,y: Hill((x*32,y*27))
    sprites[(130,180,150,255)] = lambda x,y: FireBlock((x*32,y*32))
    sprites[(0, 255, 255, 255)] = lambda x,y: Goomba((x*32,y*32))
    sprites[(166,215,166,255)] = lambda x,y: StarBox((x*32,y*32))
    sprites[(76, 255, 0, 255)] = lambda x,y: Cannon((x*32 + 1, y*28.3))
    sprites[(63, 73, 127, 255)] = lambda x, y: BigCannon((x*32, y*24.5  + 4))
    sprites[(255, 127, 182, 255)] = lambda x,y: SmallCannon((x*32, y*32))
    sprites[(127, 0, 110, 255)] = lambda x,y: VenusFlyTrap((x*32.48, y*29))
    sprites[(72, 0, 255, 255)] = lambda x,y: GreenVenusFlyTrap((x*32.05, y*28.25))
    sprites[(255, 0, 0, 255)] = lambda x,y: Moving((x*32,y*32))
    sprites[(82, 127, 63, 255)] = lambda x,y: BigMoving((x*32,y*32))
    sprites[(255, 255, 0, 255)] = lambda x,y: Coin((x*32, y*31.8))
    sprites[(0, 255, 0, 255)] = lambda x,y: Flag((x*31.9, y*12))
    sprites[(0, 200, 0, 255)] = None
    sprites[(0, 127, 70, 255)] = lambda x,y: OneUp((x*32,y*31.85))
    sprites[(178, 0, 255, 255)] = lambda x,y: BigPipe((x*32,y*25))
    sprites[(64, 64, 64, 255)] = lambda x,y: Fence((x*32,y*32))
    sprites[(182, 255, 0, 255)] = lambda x,y: BigTree((x*32,y*27))
    sprites[(0,55,0,255)] = lambda x,y: Message((x*32,y*2))
    sprites[(255, 0, 220, 255)] = lambda x,y,width: DoubleCloud((x*32,y*32),width)
    sprites[(255, 106, 0, 255)] = lambda x,y: RedKoopa((x*32, y*29))
    sprites[(38, 127, 0, 255)] = lambda x,y: Tree((x*32,y*29.7))
    sprites[(0, 127, 127, 255)] = False #'Special'
    sprites[(255, 0, 110, 255)] = lambda x,y: GrassLeft((x*32,y*32))
    sprites[(165, 255, 127, 255)] = lambda x,y: GrassRight((x*32,y*32))
    sprites[(255, 127, 127, 255)] = False #'Special'
    sprites[(127, 255, 197, 255)] = lambda x,y: Wall((x*32,y*24))
    sprites[(214, 127, 255, 255)] = False #'big castle',
    sprites[(0, 0, 255, 255)] = lambda x,y: GreenKoopa((x*32, y*30.3))
    sprites[(95,115,135,255)] = lambda x,y: Flare((x*32.5,(y+1)*32))
    sprites[(255,255,255,255)] = None
    return sprites

def get_bg():
    a = data.load_image('bgup.png')
    b = data.load_image('bgdown.png')
    c = 'maintheme.wav'
    d = 'castletheme.wav'
    e = 'winner.wav'
    bg = {}
    bg[1] = [a,c,1]
    bg[2] = [b,c,2]
    bg[3] = [a,c,1]
    bg[4] = [b,d,2]
    bg[5] = [a,c,1]
    bg[6] = [a,c,1]
    bg[7] = [b,c,2]
    bg[8] = [b,d,2]
    bg[9] = [a,e,1]
    return bg














#place holder