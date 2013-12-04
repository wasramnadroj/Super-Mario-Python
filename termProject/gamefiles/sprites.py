#
#
#
import pygame,os,sys,data,math,levelgen, random
from pygame.locals import *

def find_hit(x,y):
    if abs(x) > abs(y):
        if x< 0:
            return 'right'#right
        elif x > 0:
            return 'left'#left
    elif abs(y) > abs(x):   
        if y < 0:
            return 'top'#top
        elif y > 0:
            return 'bottom'#bottom              
    else:
        return None

class gameObject(pygame.sprite.Sprite):

    def __init__(self, *groups):
        pygame.sprite.Sprite.__init__(self, groups)
        self.collisions = []

    def collide(self, group):
        if group not in self.collisions:
            self.collisions.append(group)

    def clear_collisions(self):
        self.collisions = []

    def place(self, screen):
        screen.blit(self.image,(self.rect[0],self.rect[1]))

    def move(self,x,y,collision=1):
        if collision == 1:
            if x != 0:
                self.__move(x,0)
            if y != 0:
                self.__move(0,y)
        else:
            self.rect.move_ip(x,y)

    def fix(self,sprite,side):
        #acts as collision detection and prevents sprites from moving on top of each other
        if side == 'top':
            self.rect.top = sprite.rect.bottom
        if side == 'bottom':
            self.rect.bottom = sprite.rect.top
        if side == 'right':
            self.rect.left = sprite.rect.right
        if side == 'left':
            self.rect.right = sprite.rect.left

    def __move(self,x,y): #protects the method, but still allows use for subclass
        self.rect.move_ip(x,y)
        collide = find_hit(x,y)

        for collision in self.collisions:
            for sprite in collision:
                if sprite.rect.colliderect(self.rect):
                    self.collided(collide,sprite,collision)

    def collided(self, location, sprite, group):
        self.fix(sprite, location)

class Player(gameObject):

    def __init__(self, position,toon):
        gameObject.__init__(self, self.groups)
        self.toon = toon
        self.image = self.move_images[0]
        self.left = []
        for image in self.move_images:
            self.left.append(pygame.transform.flip(image,1,0))
        self.rect = self.image.get_rect(topleft=position)
        self.jumping = 0
        self.breaker = 0
        self.up = 0
        self.direction = 1
        self.pic = 0
        self.save = 0
        self.dead = 0
        self.life = 1
        self.invuln = 0
        self.star = 0
        self.no_clip = 0
        self.woo = data.load_sound('star.wav')
        self.timer = 0
        self.inc = .3
        self.jumps = data.load_sound('jump.wav')
        self.bounces = data.load_sound('jump2.wav')
        self.hits = data.load_sound('hit.wav')

    def collided(self, location, sprite, group):
        self.fix(sprite, location)
        if location == 'top':
            self.up = 0
        if location == 'bottom':
            self.up = 0
            self.jumping = 0

    #fix for moving platforms
    def fix(self,sprite,side):
        if type(sprite) != Moving and type(sprite) != BigMoving:
            if side == 'top':
                self.rect.top = sprite.rect.bottom
            if side == 'bottom':
                self.rect.bottom = sprite.rect.top
            if side == 'right':
                self.rect.left = sprite.rect.right
            if side == 'left':
                self.rect.right = sprite.rect.left
        else:
            if side == 'bottom':
                self.rect.bottom = sprite.rect.top

    def jump(self):
        if not self.jumping:
            self.up = -9.4
            if self.breaker:
                self.up = -11
            self.jumping = True
            self.jumps.play()
            self.move(0,-4)

    # def magic(self):
    #     if self.breaker:
    #         if self.toon == 'Mario':
    #             Player.move_images = [data.load_image('mario1.png',2.4), data.load_image('mario2.png',2.4), data.load_image('mario3.png',2.4), data.load_image('mario4.png',2.4), data.load_image('mario1.png',2.4), data.load_image('mario5.png',2.4)]
    #         if self.toon == 'Luigi':
    #             Player.move_images = [data.load_image('luigi1.png'), data.load_image('luigi2.png'), data.load_image('luigi3.png'), data.load_image('luigi4.png'), data.load_image('luigi1.png'), data.load_image('luigi5.png')]
    #         if self.toon == 'Yoshi':
    #             Player.move_images = [data.load_image('yoshi1.png'), data.load_image('yoshi2.png'), data.load_image('yoshi3.png'), data.load_image('yoshi4.png'), data.load_image('yoshi1.png'), data.load_image('yoshirand.png')]
    #         if self.toon == 'Toad':
    #             Player.move_images = [data.load_image('toad1.png',2.4), data.load_image('toad2.png',2.4), data.load_image('toad3.png',2.4), data.load_image('toad4.png',2.4), data.load_image('toad1.png',2.4), data.load_image('toad5.png',2.4)]
    #         self.image = self.move_images[0]
    #         self.left = []
    #         for image in self.move_images:
    #             self.left.append(pygame.transform.flip(image,1,0))
    #         self.rect = self.image.get_rect(topleft=(self.rect.left,self.rect.top))
    #     else:
    #         if self.toon == 'Mario':
    #             Player.move_images = [data.load_image('mario1.png'), data.load_image('mario2.png'), data.load_image('mario3.png'), data.load_image('mario4.png'), data.load_image('mario1.png'), data.load_image('mario5.png')]
    #         if self.toon == 'Luigi':
    #             Player.move_images = [data.load_image('luigi1.png',1.435), data.load_image('luigi2.png',1.513), data.load_image('luigi3.png',1.513), data.load_image('luigi4.png',1.47), data.load_image('luigi1.png',1.435), data.load_image('luigi5.png',1.55)]
    #         if self.toon == 'Yoshi':
    #             Player.move_images = [data.load_image('yoshi1.png',1.75), data.load_image('yoshi2.png',1.694), data.load_image('yoshi3.png',1.696), data.load_image('yoshi4.png',1.694), data.load_image('yoshi1.png',1.75), data.load_image('yoshirand.png',1.6)]
    #         if self.toon == 'Toad':
    #             Player.move_images = [data.load_image('toad1.png'), data.load_image('toad2.png'), data.load_image('toad3.png'), data.load_image('toad4.png'), data.load_image('toad1.png'), data.load_image('toad5.png')]
    #         self.image = self.move_images[0]
    #         self.left = []
    #         for image in self.move_images:
    #             self.left.append(pygame.transform.flip(image,1,0))
    #         self.rect = self.image.get_rect(topleft=(self.rect.left,self.rect.top))


    def update(self):
        self.pic += 1
        direction = 0
        dy=0
        move = pygame.key.get_pressed()
        if self.life > 0:
            if self.no_clip == 0:
                if self.save == 0:
                    if self.up < 8:
                        self.up += self.inc
                    if self.up > 2:
                        self.jumping = 1

                    if move[K_LEFT]:
                        direction = -1
                        self.direction = -1
                    if move[K_RIGHT]:
                        direction = 1
                        self.direction = 1

                    if self.direction < 0:
                        self.image = self.left[0]
                    if self.direction > 0:
                        self.image = self.move_images[0]
                    if direction < 0:
                        self.image = self.left[self.pic/6%5]
                    if direction > 0:
                        self.image = self.move_images[self.pic/6%5]
                    if self.direction < 0 and self.jumping:
                        self.image = self.left[5]
                    if self.direction > 0 and self.jumping:
                        self.image = self.move_images[5]

                    if self.rect.left < 0:
                        self.rect.left = 0
                    self.move(5*direction, self.up)

                else:
                
                        self.move(0,-1)
            else:
                if move[K_LEFT]:
                    direction = -1
                    self.direction = -1
                if move[K_RIGHT]:
                    direction = 1
                    self.direction = 1
                if move[K_DOWN]:
                    dy = 1
                if move[K_UP]:
                    dy = -1
                if self.direction < 0:
                    self.image = self.left[0]
                if self.direction > 0:
                    self.image = self.move_images[0]
                if direction < 0:
                    self.image = self.left[self.pic/6%5]
                if direction > 0:
                    self.image = self.move_images[self.pic/6%5]
                if self.direction < 0 and self.jumping:
                    self.image = self.left[5]
                if self.direction > 0 and self.jumping:
                    self.image = self.move_images[5]

                if self.rect.left < 0:
                    self.rect.left = 0
                if self.rect.top < 0:
                    self.rect.top = 0
                if self.rect.bottom > 460:
                    self.rect.bottom = 460
                self.move(5*direction, 5*dy)
        else:
            Death((self.rect.left,self.rect.top),self.toon)
            self.kill()

class Death(gameObject):

    def __init__(self,position,toon):
        gameObject.__init__(self, self.groups)
        self.y = position[1]
        self.up = 0
        self.gone = 0
        if toon == 'Mario':
            mult = 2
        elif toon == 'Luigi':
            mult = 1.425
        elif toon == 'Yoshi':
            mult = 1.75
        elif toon == 'Toad':
            mult = 2
        self.image = data.load_image('%sdie.png'%toon,mult)
        self.rect = self.image.get_rect(topleft=position)

    def update(self):
        if self.up == 0:
            self.move(0,-2)
        else:
            self.move(0,3)
            if self.rect.top >= 460:
                self.kill()
                self.gone = 1
        if self.rect.top < self.y-60:
            self.up += 1

class Cloud(gameObject):

    def __init__(self,position,width):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)
        self.lvlwidth = width

    def update(self):
        if self.rect.right < 0:
            self.kill()
            Cloud((self.lvlwidth-64,self.rect.top),self.lvlwidth)
        self.move(-1,0, False)

class Question(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=position)
        self.pic = 0
        self.orientation = None

    def update(self):
        self.pic += 1
        self.image = self.images[self.pic/15%4]

class CoinQuestion(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=position)
        self.pic = 0
        self.x = position[0]
        self.y = ((position[1]-32)/32)*31.8
        self.coined = 0
        self.hit = data.load_sound('bump.wav')
        self.done = data.load_image('qempty.png')

    def update(self):
        self.pic += 1
        if self.coined < 1:
            self.image = self.images[self.pic/15%4]
        else:
            self.image = self.done

    def bing(self):
        if self.coined == 0:
            Coin((self.x,self.y))
            self.hit.play()
        self.coined +=1

class BrickQuestion(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=position)
        self.pic = 0
        self.x = position[0]
        self.y = ((position[1]-32)/32)*31
        self.coined = 0
        self.hit = data.load_sound('shroom.wav')
        self.done = data.load_image('qempty.png')
        self.orientation = None

    def update(self):
        self.pic += 1
        if self.coined < 1:
            self.image = self.images[self.pic/15%4]
        else:
            self.image = self.done

    def bing(self):
        if self.coined == 0:
            BrickShroom((self.x,self.y))
            self.hit.play()
        self.coined +=1

class Coin(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=position)
        self.pic = 0

    def update(self):
        self.pic += 1
        self.image = self.images[self.pic/9%8]

class GrabCoin(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=position)
        self.killtime = 0

    def update(self):
        self.killtime += 1
        if self.killtime < 12:
            self.image = self.images[self.killtime/4%3]
        else:
            self.kill()

class GrabShroom(gameObject):

    def __init__(self,position,name):
        gameObject.__init__(self, self.groups)
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=position)
        self.killtime = 0
        self.type = name

    def update(self):
        self.killtime += 1
        if self.killtime < 12:
            self.image = self.images[self.killtime/4%3]
        else:
            self.kill()

class Platform(gameObject):

    def __init__(self,position,orient):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)
        self.orientation = orient

class Brick(gameObject):

    def __init__(self,position,orient):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)
        self.orientation = orient
        self.hits = -1
        self.breaking = [data.load_image('break%s.png'%image)for image in xrange(1,4)]
        self.breaknoise = data.load_sound('break.wav')

    def bing(self):
        self.breaknoise.play()
        self.kill()
        
class Bush(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)

class GoombaDie(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)
        self.pic = 0

    def update(self):
        self.pic += 1
        if self.pic > 50:
            self.kill()

class Goomba(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=position)
        self.x = position[0]
        self.y = position[1]
        self.speed = 1
        self.pic = 0
        self.name = 'Goomba'
        self.flagged = 0

    def flag(self):
        self.flagged += 1

    def update(self):
        if self.flagged == 0:
            self.pic+=1
            self.image = self.images[self.pic/16%2]
            if self.rect.y > 460:
                self.kill()
            if self.rect.left < 0:
                self.rect.left = 0
                self.speed = 1
            self.move(self.speed,1)
            if self.speed == 1:
                self.x += 1
            else:
                self.x -= 1
        else:
            GoombaDie((self.rect.left,self.rect.top+14))
            stomp = data.load_sound('stomp.wav')
            stomp.play()
            self.kill()

    def collided(self, location, sprite, group):
        self.fix(sprite, location)
        if location == 'left':
            self.speed = -1
        if location == 'right':
            self.speed = 1
        if sprite.orientation == 1:
            if self.rect.left <= sprite.rect.left:
                self.speed = 1
        if sprite.orientation == 2:
            self.speed = -1

class GoombaDeath(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=position)    

class JumpPlatform(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)
        self.orientation = None

class OneUp(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)
        self.speed = 3
        self.frame = 0
        self.name = 'life'

    def update(self):
        self.frame += 1
        if self.frame%2 == 0:
            self.move(self.speed,3)
        if self.rect.top > 460:
            self.kill()

    def collided(self,location,sprite,group):
        self.fix(sprite,location)
        if self.rect.bottom != sprite.rect.top:
            if location == 'left':
                self.speed = -3
            if location == 'right':
                self.speed = 3

class BrickShroom(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)
        self.speed = 1
        self.frame = 0
        self.name = 'brick'

    def update(self):
        self.frame += 1
        self.move(self.speed,2)
        if self.rect.top > 460:
            self.kill()

    def collided(self,location,sprite,group):
        self.fix(sprite,location)
        if self.rect.bottom != sprite.rect.top:
            if location == 'left':
                self.speed = -1
            if location == 'right':
                self.speed = 1

class MushroomQuestion(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=position)
        self.pic = 0
        self.x = position[0]
        self.y = ((position[1]-32)/32)*31
        self.orientation = None
        self.coined = 0
        self.hit = data.load_sound('shroom.wav')
        self.done = data.load_image('qempty.png')

    def update(self):
        self.pic += 1
        if self.coined < 1:
            self.image = self.images[self.pic/15%4]
        else:
            self.image = self.done

    def bing(self):
        if self.coined == 0:
            OneUp((self.x,self.y-1))
            self.hit.play()
        self.coined +=1

class Pipe(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)
        self.orientation = 'gameObject'

class Flag(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.wind = []
        for picture in self.images:
            self.wind.append(pygame.transform.flip(picture,1,0))
        self.image = self.wind[0]
        self.rect = self.image.get_rect(topleft=position)
        self.pic = 0

    def update(self):
        self.pic += 1
        self.image = self.wind[self.pic/35%4]

class Message(gameObject):

    def __init__(self,position):
        gameObject.__init__(self,self.groups)
        self.rect = self.image.get_rect(topleft=position)

class Hill(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)

class Castle(gameObject):
    
    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)

class BowserCastle(gameObject):
    
    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)

class PeachCastle(gameObject):
    
    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)

class VenusDie(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.image = data.load_image('reddie.png')
        self.rect = self.image.get_rect(topleft=position)
        self.pic = 0

    def update(self):
        self.pic += 1
        if self.pic > 50:
            self.kill()

class GreenVenusDie(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.image = data.load_image('greendie.png')
        self.rect = self.image.get_rect(topleft=position)
        self.pic = 0

    def update(self):
        self.pic += 1
        if self.pic > 50:
            self.kill()

class VenusFlyTrap(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.image = self.images[1]
        self.rect = self.image.get_rect(topleft=position)
        self.pic = 0
        self.speed = 1

    def update(self):
        self.pic+=1
        self.image = self.images[self.pic/40%2]
        if self.speed == 0:
            up = random.choice(xrange(1,30))
            if up%17 == 0 and self.rect.bottom == 336:
                self.speed = 1
            elif up%17 == 0:
                self.speed = -1
        if self.pic%3 == 0:
            self.move(0,self.speed)
        if self.rect.bottom == 336:
            self.speed = 0

    def collided(self, location, sprite, group):
        self.fix(sprite,location)
        if location == 'bottom':
            self.speed = 0

    def die(self):
        VenusDie((self.rect.left,self.rect.top))
        self.kill()

class GreenVenusFlyTrap(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.image = self.images[1]
        self.rect = self.image.get_rect(topleft=position)
        self.pic = 0
        self.speed = 1

    def update(self):
        self.pic+=1
        self.image = self.images[self.pic/40%2]
        if self.speed == 0:
            up = random.choice(xrange(1,30))
            if up%17 == 0 and self.rect.bottom == 300:
                self.speed = 1
            elif up%17 == 0:
                self.speed = -1
        if self.pic%3 == 0:
            self.move(0,self.speed)
        if self.rect.bottom == 300:
            self.speed = 0

    def collided(self, location, sprite, group):
        self.fix(sprite,location)
        if location == 'bottom':
            self.speed = 0
        
    def die(self):
        GreenVenusDie((self.rect.left,self.rect.top))
        self.kill()

class BigPipe(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)
        self.orientation = None

class RedKoopa(gameObject):  

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=position)
        self.right = []
        for picture in self.images:
            self.right.append(pygame.transform.flip(picture,1,0))
        self.name = 'RedKoopa'
        self.speed = 1
        self.pic = 0
        self.flagged = 0

    def flag(self):
        self.flagged = 1

    def update(self):
        self.pic +=1
        if self.flagged == 0:
            if self.speed > 0:
                self.image = self.right[self.pic/20%2]
            if self.speed < 0:
                self.image = self.images[self.pic/20%2]
            if self.pic%2 == 0:
                self.move(self.speed,1)
        else:
            RedKoopaDeath((self.rect.left,self.rect.top+22))
            self.kill()
            death = data.load_sound('stomp.wav')
            death.play()

    def collided(self,location,sprite,group):
        self.fix(sprite,location)
        if location == 'right':
            self.speed = 1
        if location == 'left':
            self.speed = -1
        if self.rect.left < 0:
            self.speed = 1
        if sprite.orientation == 1:
            if self.rect.left <= sprite.rect.left:
                self.speed = 1
        if sprite.orientation == 2:
            self.speed = -1

class GreenKoopaDeath(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.image = data.load_image('greenkoopa3.png')
        self.rect = self.image.get_rect(topleft=position)
        self.pic = 0

    def update(self):
        self.pic += 1
        if self.pic > 50:
            self.kill()

class RedKoopaDeath(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.image = data.load_image('redkoopa3.png')
        self.rect = self.image.get_rect(topleft=position)
        self.pic = 0

    def update(self):
        self.pic += 1
        if self.pic > 50:
            self.kill()

class GreenKoopa(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.image = self.images[0]
        self.right = []
        for picture in self.images:
            self.right.append(pygame.transform.flip(picture,1,0))
        self.rect = self.image.get_rect(topleft=position)
        self.name = 'GreenKoopa'
        self.speed = 1
        self.pic = 0
        self.flagged = 0

    def flag(self):
        self.flagged += 1

    def update(self):
        self.pic+= 1
        if self.flagged == 0:
            if self.speed > 0:
                self.image = self.right[self.pic/20%2]
            if self.speed < 0:
                self.image = self.images[self.pic/20%2]
            if self.pic%2 == 0:
                self.move(self.speed,1)
        else:
            GreenKoopaDeath((self.rect.left,self.rect.top+24))
            self.kill()
            death = data.load_sound('stomp.wav')
            death.play()

    def collided(self,location,sprite,group):
        self.fix(sprite,location)
        if location == 'right':
            self.speed = 1
        if location == 'left':
            self.speed = -1
        if self.rect.left < 0:
            self.speed = 1
        if sprite.orientation == 1:
            if self.rect.left <= sprite.rect.left:
                self.speed = 1
        if sprite.orientation == 2:
            self.speed = -1

class DoubleCloud(gameObject):

    def __init__(self,position, width):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)
        self.lvlwidth = width
        self.slow = 0

    def update(self):
        self.slow += 1
        if self.rect.right < 0:
            self.kill()
            DoubleCloud((self.lvlwidth-96,self.rect.top),self.lvlwidth)
        if self.slow%2 == 0:
            self.move(-1,0, False)

class Tree(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)

class BigTree(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)

class Fence(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)

class Flare(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=position)
        self.pic = 0
        self.speed = random.choice(xrange(1,4))
        self.y = position[1]

    def update(self):
        self.pic += 1
        self.image = self.images[self.pic/10%4]
        self.move(0,self.speed)
        if self.rect.top < self.y-200:
            self.speed = -self.speed
        elif self.rect.top > self.y+random.choice(xrange(0,500)):
            self.speed = -self.speed

class GrassLeft(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)
        self.orientation = 1

class GrassMiddle(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)
        self.orientation = None

class GrassRight(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)
        self.orientation = 2

class GrassSupport(gameObject):

    def __init__(self,position, tile):
        gameObject.__init__(self, self.groups)
        self.image = self.images[tile]
        self.rect = self.image.get_rect(topleft=position)

class CrossGrass(gameObject):

    def __init__(self,position,tile):
        gameObject.__init__(self, self.groups)
        self.image = self.images[tile]
        self.rect = self.image.get_rect(topleft=position)

class Wall(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)

class Moving(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)
        self.pic = 0
        self.speed = 1
        self.y = position[1]

    def update(self):
        if self.rect.centery > self.y + 80:
            self.speed = -1
        if self.rect.centery < self.y-80:
            self.speed = 1
        self.move(0,self.speed)
        

class BigMoving(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)
        self.pic = 0
        self.speed = -1
        self.y = position[1]

    def update(self):
        if self.rect.centery > self.y + 80:
            self.speed = -1
        if self.rect.centery < self.y-80:
            self.speed = 1
        self.move(0,self.speed)

class Cannon(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=position)
        self.orientation = None
        self.x = (position[0]/32-.95)*32
        self.y = position[1]
        self.pic = 0

    def chance(self):
        self.pic += 1
        if (self.pic)%90 == 0:
            Bullet((self.x,self.y))

class BigCannon(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=position)
        self.orientation = None
        self.x = (position[0]/32-.95)*32
        self.y = position[1]
        self.pic = 0

    def chance(self):
        self.pic += 1
        if (self.pic)%random.choice([120,150,160,200,250]) < 3:
            Bullet((self.x,self.y))

class SmallCannon(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=position)
        self.orientation = None
        self.x = (position[0]/32-.95)*32
        self.y = position[1]
        self.pic = 0

    def chance(self):
        self.pic += 1
        if (self.pic)%90 == 0:
            Bullet((self.x,self.y))

class Star(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=position)
        self.orientation = None
        self.pic = 0
        self.name = 'Star'

    def update(self):
        self.pic += 1
        self.image = self.images[self.pic/26%8]

class StarBox(gameObject):

    def __init__(self,position):
        gameObject.__init__(self, self.groups)
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=position)
        self.pic = 0
        self.x = position[0]
        self.y = ((position[1]-32)/32)*31.8
        self.coined = 0
        self.hit = data.load_sound('shroom.wav')
        self.done = data.load_image('qempty.png')

    def update(self):
        self.pic += 1
        if self.coined < 1:
            self.image = self.images[self.pic/15%4]
        else:
            self.image = self.done

    def bing(self):
        if self.coined == 0:
            Star((self.x,self.y))
            self.hit.play()

        self.coined +=1

class Bullet(gameObject):

    def __init__(self,position):
        gameObject.__init__(self,self.groups)
        self.rect = self.image.get_rect(topleft=position)
        self.pic = 0
        self.x = position[0]
        self.y = position[1]

    def update(self):
        self.pic += 1
        if self.x-self.rect.centerx > 600:
            self.kill()
            GrabShroom((self.x,self.y),'none')
        self.move(-1,0)

class CastleBrick(gameObject):

    def __init__(self,position,orient):
        gameObject.__init__(self, self.groups)
        self.rect = self.image.get_rect(topleft=position)
        self.orientation = orient

class Lava(gameObject):

    def __init__(self,position,tile):
        gameObject.__init__(self, self.groups)
        self.image = self.images[tile]
        self.rect = self.image.get_rect(topleft=position)

class FireBlock(gameObject):

    def __init__(self,position):
        gameObject.__init__(self,self.groups)
        self.rect = self.image.get_rect(topleft=position)

class Bridge(gameObject):

    def __init__(self,position):
        gameObject.__init__(self,self.groups)
        self.rect = self.image.get_rect(topleft=position)

class Switch(gameObject):

    def __init__(self,position):
        gameObject.__init__(self,self.groups)
        self.rect = self.image.get_rect(topleft=position)
        self.x = position[0]
        self.y = position[1]
        self.dead = 0

class Bowser(gameObject):

    def __init__(self,position):
        gameObject.__init__(self,self.groups)
        self.rect = self.image.get_rect(topleft=position)
        self.name = 'Bowser'
        self.x = position[0]
        self.y = position[1]-2 #temp fix -.-
        self.up = data.load_image('bowserjump.png')
        self.down = data.load_image('bowser.png')
        self.shoot = data.load_image('bowserfire.png')
        self.pic = 0
        self.dead = data.load_image('bowserdie.png')
        self.winner = data.load_sound('win.wav')
        self.ping = data.load_sound('bowserfire.wav')
        self.fall = data.load_sound('bowserdie.wav')
        self.fallsound = -1
        self.victory = -1

    def play(self,coord):
        self.pic += 1
        y = coord[1]
        x = coord[0]
        dif = y-self.rect.top
        if abs(x-self.rect.left) > 0:
            self.move(0,dif)
            if self.rect.bottom > 320:
                self.rect.bottom = 320
        if self.rect.top < self.y:
            self.image = self.up
        else:
            self.image = self.down
        if self.pic%130 == 0 or self.pic % 290 == 0:
            FireBall((self.rect.left-10,self.rect.top+15))
            self.ping.play()
        if self.pic%130 > 110 or self.pic%130 < 20:
            self.image = self.shoot

    def defeat(self):
        self.move(0,1)

    def die(self):
        if self.fallsound < 0:
            pygame.mixer.music.stop()
            self.fall.play()
            self.fallsound += 1
        self.image = self.dead
        self.move(0,2)
        if self.rect.top > 460:
            self.kill()
            self.go()

    def go(self):
        if self.victory < 0:
            #pygame.mixer.music.stop()
            self.winner.play()
            self.victory +=1


class FireBall(gameObject):

    def __init__(self,position):
        gameObject.__init__(self,self.groups)
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=position)
        self.pic = 0
        self.x = position[0]
        self.travel = 0

    def update(self):
        self.pic += 1
        self.image = self.images[self.pic/20%6]
        if self.travel > 1312:
            self.kill()
            GrabCoin((self.rect.left,self.rect.top))
        self.move(-1,0)
        self.travel += 1

class Spike(gameObject):

    def __init__(self,position,orient):
        gameObject.__init__(self,self.groups)
        self.orientation = orient
        self.y = position[1]
        if orient == 0:
            self.image = pygame.transform.flip(self.image,0,1)
        self.rect = self.image.get_rect(topleft=position)
        self.pic = 0

    def update(self):
        self.pic += 1
        if self.orientation == 0:
            if self.rect.top <= self.y+2:
                self.speed = 1
            if self.rect.top >= self.y+random.choice(xrange(120,250)):
                self.speed = -1
            self.move(0,self.speed)





















#