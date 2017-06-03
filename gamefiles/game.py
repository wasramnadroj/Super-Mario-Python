import pygame,sys,os,data,levelgen,sprites,start, artifacts,genmenu,savefile
from pygame.locals import *
from levelgen import *
from sprites import *
from artifacts import *
from genmenu import *
from savefile import *


## NO CREDIT FOR RELRECT. CITATIONS IN CITATION.TXT
def RelRect(actor, camera):
    return Rect(actor.rect.x-camera.rect.x, actor.rect.y-camera.rect.y, actor.rect.w, actor.rect.h)
##############################


## **NOTE**
# class Camera was adapted and changed from code originally found in tutorials
# and eventually online. The code was adapted and there is a note in
# citations.txt - this is here as a citation for the camera and to get you to
# read the citations text!
class Camera(object): #SIDESCrOLLER

    def __init__(self,focus,width):
        self.player = focus
        self.view = Rect(0,0,width,460)#camera sees the entire level but only from 0 - 460. this is to give the marioesque look of the floor only being 1.5 tiles thich
        self.rect = pygame.display.get_surface().get_rect()
        self.center = self.player.rect.center

    def update(self):
        if self.player.rect.centerx > self.rect.centerx+64:
            self.rect.centerx = self.player.rect.centerx-64
        if self.player.rect.centerx < self.rect.centerx-64:
            self.rect.centerx = self.player.rect.centerx+64
        self.rect.clamp_ip(self.view)

    def create_world(self,screen,sprites):
        for sprite in sprites:
            if sprite.rect.colliderect(self.rect):
                screen.blit(sprite.image, RelRect(sprite,self))

############################

class Game(object):

    def __init__(self, screen,toon, level=1,lives=3):

        #########################################
        # SET UP SCREEN, FPS MONITOR (CLOCK), AND SPRITES
        #########################################
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.sprites = pygame.sprite.OrderedUpdates()
        self.character = pygame.sprite.OrderedUpdates()
        self.flags = pygame.sprite.OrderedUpdates()
        self.death = pygame.sprite.OrderedUpdates()
        self.platforms = pygame.sprite.OrderedUpdates()
        self.enemies = pygame.sprite.OrderedUpdates()
        self.mushrooms = pygame.sprite.OrderedUpdates()
        self.coins = pygame.sprite.OrderedUpdates()
        self.questions = pygame.sprite.OrderedUpdates()
        self.stationary = pygame.sprite.OrderedUpdates()
        self.traps = pygame.sprite.OrderedUpdates()
        self.movingplatforms = pygame.sprite.OrderedUpdates()
        self.cannons = pygame.sprite.OrderedUpdates()
        self.bases = pygame.sprite.OrderedUpdates()
        self.coinquestions = pygame.sprite.OrderedUpdates()
        self.upplat = pygame.sprite.OrderedUpdates()
        self.brickquestions = pygame.sprite.OrderedUpdates()
        self.breakable = pygame.sprite.OrderedUpdates()
        self.powerup = pygame.sprite.OrderedUpdates()
        self.starquestions = pygame.sprite.OrderedUpdates()
        self.missles = pygame.sprite.OrderedUpdates()
        self.fire = pygame.sprite.OrderedUpdates()
        self.bridges = pygame.sprite.OrderedUpdates()
        self.switches = pygame.sprite.OrderedUpdates()
        self.hazards = pygame.sprite.OrderedUpdates()
        self.flares = pygame.sprite.OrderedUpdates()

        #########################################
        # IMAGES - all images cited in citations.txt
        #########################################
        if toon == 'Mario':
            Player.move_images = [data.load_image('mario1.png'), data.load_image('mario2.png'), data.load_image('mario3.png'), data.load_image('mario4.png'), data.load_image('mario1.png'), data.load_image('mario5.png')]
        if toon == 'Luigi':
            Player.move_images = [data.load_image('luigi1.png',1.435), data.load_image('luigi2.png',1.513), data.load_image('luigi3.png',1.513), data.load_image('luigi4.png',1.47), data.load_image('luigi1.png',1.435), data.load_image('luigi5.png',1.55)]
        if toon == 'Yoshi':
            Player.move_images = [data.load_image('yoshi1.png',1.75), data.load_image('yoshi2.png',1.694), data.load_image('yoshi3.png',1.696), data.load_image('yoshi4.png',1.694), data.load_image('yoshi1.png',1.75), data.load_image('yoshirand.png',1.6)]
        if toon == 'Toad':
            Player.move_images = [data.load_image('toad1.png'), data.load_image('toad2.png'), data.load_image('toad3.png'), data.load_image('toad4.png'), data.load_image('toad1.png'), data.load_image('toad5.png')]
        Cloud.image = data.load_image('cloud.png')
        Question.images = [data.load_image('q%s.png'%image) for image in xrange(0,4)]
        MushroomQuestion.images = [data.load_image('q%s.png'%image) for image in xrange(0,4)]
        StarBox.images = [data.load_image('q%s.png'%image) for image in xrange(0,4)]
        BrickQuestion.images = [data.load_image('q%s.png'%image) for image in xrange(0,4)]
        CoinQuestion.images = [data.load_image('q%s.png'%image) for image in xrange(0,4)]
        Coin.images = [data.load_image('coin%s.png'%image) for image in xrange(1,9)]
        Platform.image = data.load_image('platform-top.png')
        Brick.image = data.load_image('platform-brick.png')
        Bush.image = data.load_image('bush-1.png')
        Goomba.images = [data.load_image('goomba%s.png'%image)for image in xrange(1,4)]
        JumpPlatform.image = data.load_image('platform-air.png')
        OneUp.image = data.load_image('1up2.png')
        Pipe.image = data.load_image('pipe.png')
        Hill.image = data.load_image('hill.png')
        Flag.images = [data.load_image('flagpole%s.png' %image) for image in xrange(1,5)]
        Castle.image = data.load_image('castle.png')
        VenusFlyTrap.images = [data.load_image('redvenus%s.png' % image) for image in xrange(1,3)]
        BigPipe.image = data.load_image('bigpipe.png')
        RedKoopa.images = [data.load_image('redkoopa%s.png'%image) for image in xrange(1,4)]
        GreenKoopa.images = [data.load_image('greenkoopa%s.png'%image) for image in xrange(1,4)]
        DoubleCloud.image = data.load_image('doublecloud.png')
        BigTree.image = data.load_image('bigtree.png')
        Tree.image = data.load_image('tree.png')
        Fence.image = data.load_image('fence.png')
        RedKoopa.images = [data.load_image('redkoopa%s.png'%image) for image in xrange(1,4)]
        GrassLeft.image = data.load_image('grassleft.png')
        GrassMiddle.image = data.load_image('grassmiddle.png')
        GrassRight.image = data.load_image('grassright.png')
        GrassSupport.images = [data.load_image('grasssupport%s.png'%image) for image in xrange(0,4)]
        CrossGrass.images = [data.load_image('grass%s.png'%image)for image in xrange(1,4)]
        Wall.image = data.load_image('wall.png')
        Moving.image = data.load_image('moving.png')
        BigMoving.image = data.load_image('bigmoving.png')
        BigCannon.images = [data.load_image('cannonbig%s.png'%image) for image in xrange(1,3)]
        SmallCannon.images = [data.load_image('smallcannon%s.png'%image) for image in xrange(1,3)]
        Cannon.images = [data.load_image('cannon%s.png' % image) for image in xrange(1,3)]
        GrabCoin.images = [data.load_image('c%s.png' % image) for image in xrange(1,4)]
        GreenVenusFlyTrap.images = [data.load_image('vblue%s.png'%image)for image in xrange(0,2)]
        GrabShroom.images = [data.load_image('c%s.png' % image) for image in xrange(1,4)]
        BrickShroom.image = data.load_image('brickbreaker.png')
        Star.images = [data.load_image('star%s.png'%image)for image in xrange(0,8)]
        Bullet.image = data.load_image('bullet.png')
        CastleBrick.image = data.load_image('cbrick.png')
        Lava.images = [data.load_image('lava%s.png'%image)for image in xrange(0,2)]
        if level == 9:
            Lava.images = [data.load_image('water%s.png'%image)for image in xrange(0,2)]
        FireBlock.image = data.load_image('qempty.png')
        Bridge.image = data.load_image('bridge.png')
        Switch.image = data.load_image('switch.png')
        Bowser.image = data.load_image('bowser.png')
        FireBall.images = [data.load_image('fireball%s.png'%image,1.5)for image in xrange(0,6)]
        GoombaDie.image = data.load_image('goomba3.png')
        BowserCastle.image = data.load_image('bigcastle.png')
        Spike.image = data.load_image('spike.png')
        PeachCastle.image = data.load_image('peach.png',1)
        Flare.images = [data.load_image('flare%s.png'%image)for image in xrange(0,4)]

        #########################################
        # SPRITE GROUPS
        #########################################
        Flare.groups = self.flares, self.sprites
        PeachCastle.groups = self.sprites
        BowserCastle.groups = self.sprites
        Player.groups = self.sprites, self.character,self.death
        Cloud.groups = self.sprites,
        Question.groups = self.sprites, self.platforms, self.questions, self.stationary
        MushroomQuestion.groups = self.sprites, self.platforms, self.questions, self.stationary, self.upplat
        CoinQuestion.groups = self.sprites, self.platforms, self.questions, self.stationary, self.coinquestions
        BrickQuestion.groups = self.sprites, self.platforms, self.questions, self.stationary, self.brickquestions
        StarBox.groups = self.sprites, self.platforms, self.questions, self.stationary, self.starquestions
        Coin.groups = self.sprites,self.coins,
        Platform.groups = self.sprites,self.platforms,self.stationary,self.bases
        CastleBrick.groups = self.sprites,self.platforms,self.stationary
        Brick.groups = self.sprites, self.platforms, self.stationary, self.breakable
        Bush.groups = self.sprites
        Goomba.groups = self.sprites, self.enemies
        JumpPlatform.groups = self.sprites, self.platforms, self.stationary
        OneUp.groups = self.sprites, self.mushrooms
        Pipe.groups = self.sprites, self.platforms, self.stationary
        Hill.groups = self.sprites
        Flag.groups = self.sprites, self.flags
        Castle.groups = self.sprites
        VenusFlyTrap.groups = self.sprites, self.traps
        BigPipe.groups = self.sprites, self.platforms, self.stationary
        RedKoopa.groups = self.sprites, self.enemies
        GreenKoopa.groups = self.sprites, self.enemies
        DoubleCloud.groups = self.sprites
        Tree.groups = self.sprites
        BigTree.groups = self.sprites
        Fence.groups = self.sprites
        RedKoopa.groups = self.sprites, self.enemies
        GrassLeft.groups = self.sprites, self.platforms, self.stationary
        GrassMiddle.groups = self.sprites, self.platforms, self.stationary
        GrassRight.groups = self.sprites, self.platforms, self.stationary
        GrassSupport.groups = self.sprites, self.platforms, self.stationary
        CrossGrass.groups = self.sprites
        Wall.groups = self.sprites
        Moving.groups = self.sprites, self.platforms, self.movingplatforms
        BigMoving.groups = self.sprites, self.platforms, self.movingplatforms
        BigCannon.groups = self.sprites, self.platforms, self.stationary, self.cannons
        Cannon.groups = self.sprites, self.platforms, self.stationary, self.cannons
        SmallCannon.groups = self.sprites, self.platforms, self.stationary, self.cannons
        Death.groups = self.sprites,self.death
        GrabShroom.groups = self.sprites
        GrabCoin.groups = self.sprites,
        GreenVenusFlyTrap.groups = self.sprites, self.traps
        BrickShroom.groups = self.sprites, self.mushrooms
        Spike.groups = self.sprites, self.hazards
        Star.groups = self.sprites, self.powerup
        Bullet.groups = self.sprites, self.missles
        Lava.groups = self.sprites
        FireBlock.groups = self.sprites,self.platforms,self.stationary
        Bridge.groups = self.sprites,self.platforms,self.stationary,self.bridges
        Switch.groups = self.sprites,self.platforms,self.stationary,self.switches
        Bowser.groups = self.sprites,self.enemies
        FireBall.groups = self.sprites,self.fire
        GoombaDie.groups = self.sprites
        GreenKoopaDeath.groups = self.sprites
        Message.groups = self.sprites
        VenusDie.groups = self.sprites
        GreenVenusDie.groups = self.sprites
        RedKoopaDeath.groups = self.sprites

        # self.sprites = sprites w/ no interactions
        # self.character = the player
        # self.flags = flags @ end of level
        # self.death = keep track of death pictures
        # self.platforms = everything that you can stand on
        # self.enemies = all the enemies
        # self.mushrooms = powerups etc
        # self.coins = coins...
        # self.questions = question blocks
        # self.stationary = sprites which do not move
        # self.traps = the plants that eat you
        # self.movingplatforms = self explanatory
        # self.cannons = cannons
        # self.bases = floors for the plants
        # self.coinquestions = questions that spit coins
        # self.upplat = questions that spit 1up
        # self.brickquestions = questions that spit brickbreater /megamushroom
        # self.breakable = sprites that can be destroyed
        # self.powerup = ... power ups
        # self.starquestions = invincibility questions
        # self.missles = bullet bills
        # self.fire = bowser fire
        # self.bridges = bowser bridge
        # self.switches = bowser switch
        # self.hazards = bowser spikes

        #########################################
        # SOUNDS
        #########################################
        self.coinsound = data.load_sound('coin.wav',1)
        self.power = data.load_sound('getshroom.wav',1)
        self.complete = data.load_sound('flag.wav',1)

        #########################################
        # MENUS
        #########################################
        self.menu = genmenu(['Resume', lambda: self.placeholder()],['Save Game', lambda: self.placeholder1()],['Quit Game',lambda: self.placeholder2(self.screen)])
        self.menu.changeFont('Raleway Thin.ttf',28)
        self.menu.position(320,200)
        self.menu.defaultColor((255,255,255))
        self.menu.choiceColor((0,255,0))
        self.menu2 = genmenu(['FILE OPEN', lambda: self.save1(self.toon,self.lvl,self.lives)],['FILE OPEN', lambda: self.save2(self.toon,self.lvl,self.lives)],['FILE OPEN',lambda: self.save3(self.toon,self.lvl,self.lives)])
        self.save_menu()
        self.menu2.changeFont('smb256.ttf',28)
        self.menu2.position(320,200)
        self.menu2.defaultColor((0,0,0))
        self.menu2.choiceColor((255,0,125))

        #########################################
        # FONTS
        #########################################
        self.font = pygame.font.Font(data.filepath('smb256.ttf'),20)
        self.font4 = pygame.font.Font(data.filepath('smb256.ttf'),36)
        self.font2 = pygame.font.Font(data.filepath('Raleway Thin.ttf'),14)
        self.font3 = pygame.font.Font(data.filepath('Raleway Thin.ttf'),24)

        #########################################
        # FLAGS / GAME VALUES
        #########################################
        self.start = 1
        self.saving = 0
        self.diefix = 0
        self.paused = 0
        self.toon = toon
        self.score = 000
        self.chill = 0
        self.record = ''
        self.flagged = 0
        self.lives = lives
        self.powertracker = 0
        self.cheat_enabled = 0

        #########################################
        # LEVEL CREATION
        #########################################
        self.lvl = level
        self.bgcolor = get_bg()
        self.level = Level(self.lvl)
        self.player = Player((000,00),toon)
        self.bg = self.bgcolor[self.lvl][0]
        data.play_music(self.bgcolor[self.lvl][1])
        self.camera = Camera(self.player,self.level.width())

        #########################################
        # LOAD SCORES
        #########################################
        if Savefile('scores.txt').readscore() == None:
            self.highscore = 0
        else:
            self.highscore = int(Savefile('scores.txt').readscore())

        #########################################
        # AESTHETIC CHANGES
        #########################################
        self.mworld = 1 + (self.lvl-1)/4
        self.stage = (self.lvl-1)%4+1
        if level != 9:
            pygame.display.set_caption('World %s-%s'%(self.mworld,self.stage))
        else:
            pygame.display.set_caption('Princess Peach\'s Castle')

        #########################################
        # INITIALIZE GAME
        #########################################
        self.main_loop()

    def save_menu(self):
        saves = Savefile().read()
        save1,save2,save3 = 'FILE OPEN','FILE OPEN', 'FILE OPEN'
        if saves != []:
            if saves[0] != []:
                save1 = saves[0][0]+' '+saves[0][1]
            if saves[1] != []:
                save2 = saves[1][0]+' '+saves[1][1]
            if saves[2] != []:
                save3 = saves[2][0]+' '+saves[2][1]
        self.menu3 = genmenu([save1, lambda: self.save1(self.toon,self.lvl,self.lives)],[save2, lambda: self.save2(self.toon,self.lvl,self.lives)],[save3,lambda: self.save3(self.toon,self.lvl,self.lives)])
        self.menu3.changeFont('smb256.ttf',28)
        self.menu3.position(320,200)
        self.menu3.defaultColor((0,0,0))
        self.menu3.choiceColor((255,0,125))

    def clear_level(self):
        #########################################
        # KILLS ALL SPRITES ON LEVEL
        #########################################
        for sprite in self.sprites:
            pygame.sprite.Sprite.kill(sprite)

    def playerdie(self):
        data.stop_music()
        if len(self.death) == 0:
            self.lives -= 1
            if self.lives >= 0:
                pygame.time.wait(2000)
                self.flagged = 0
                self.redo()
            else:
                if len(self.character) == 0:
                    pygame.time.wait(2000)
                    self.gameOver()

    def gameOver(self):
        choice = 1
        lose = data.load_sound('gameover.wav',1)
        lose.play()
        while choice:
            self.clear_level()
            self.screen.fill((0,0,0))
            text = self.font4.render('G A M E  O V E R',1,(255,255,255))
            self.screen.blit(text,(320-text.get_width()/2,230-text.get_height()/2))
            if self.score >= 3000:
                text = self.font3.render('Press R to restart! (3000 points)',1,(255,255,255))
                self.screen.blit(text,(320-text.get_width()/2,260))
            text = self.font.render('Press Enter to quit.',1,(255,255,255))
            self.screen.blit(text,(320-text.get_width()/2,290))
            events = pygame.event.get()
            for event in events:
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        lose.stop()
                        if self.score > self.highscore:
                            Savefile('scores.txt').writescore(self.score)
                        start.Menu(self.screen)
                    if event.key == K_r:
                        lose.stop()
                        if self.score >= 3000:
                            self.score -= 3000
                            self.lives = 3
                            choice = 0
                            self.redo()

            pygame.display.flip()

    def redo(self):
        #########################################
        # REINITIALIZES THE GAME WITH 1 LESS LIFE.
        #########################################
        pygame.display.flip()
        self.clear_level()
        self.level = Level(self.lvl)
        self.bg = self.bgcolor[self.lvl][0]
        self.player = Player((0,0),self.toon)
        self.camera = Camera(self.player,self.level.width())
        self.screen.fill((0,0,0))
        pygame.display.flip()
        data.play_music(self.bgcolor[self.lvl][1])
        self.mworld = 1 + (self.lvl-1)/4
        if self.lvl != 9:
            pygame.display.set_caption('World %s-%s'%(self.mworld,self.lvl))
        else:
            pygame.display.set_caption('Princess Peach\'s Castle')
        self.info()
        self.diefix = 0
        self.flagged = 0

    def finish(self):
        #########################################
        # HANDLES LEVEL COMPLETION
        #########################################
        pygame.time.wait(3000)
        pygame.display.flip()
        try: self.lvl += 1 #i'm sorry <3
        except: self.lvl = self.lvl
        #########################################
        # CHANGES LAVA TO WATER!
        #########################################
        if self.lvl == 9:
            Lava.images = [data.load_image('water%s.png'%image)for image in xrange(0,2)]
        self.clear_level()
        self.level = Level(self.lvl)
        self.bg = self.bgcolor[self.lvl][0]
        self.player = Player((0,0),self.toon)
        self.camera = Camera(self.player,self.level.width())
        self.screen.fill((0,0,0))
        pygame.display.flip()
        data.play_music(self.bgcolor[self.lvl][1])
        self.mworld = 1 + (self.lvl-1)/4
        if self.lvl != 9:
            pygame.display.set_caption('World %s-%s'%(self.mworld,(self.lvl-1)%4+1))
        else:
            pygame.display.set_caption('Princess Peach\'s Castle')
        self.info()

    def info(self):
        self.powertracker += 1
        if self.bgcolor[self.lvl][2] == 2:
            color = (255,255,255)
        else:
            color = (0,0,0)
        colorlist = [(255,0,0),(0,255,0),(0,0,255)]
        if self.cheat_enabled != 1:
            if self.lvl != 9:
                height = self.font2.get_height()
                text = self.font.render('%s'%self.toon,1,color)
                self.screen.blit(text,(10,10))
                score = text.get_width()
                score1 = text.get_height()
                text = self.font.render('Lives: %s'%self.lives,1,color)
                self.screen.blit(text,(630-text.get_width(),10))
                text = self.font.render('Powerups:',1,color)
                self.screen.blit(text,(630/2-text.get_width(),10))
                text = self.font3.render('%s'%self.score,1,color)
                self.screen.blit(text,(score+20,7))
                if self.player.breaker:
                    text = self.font2.render('Brickbreaking',1,color)
                    self.screen.blit(text,(640/2,0))
                if self.player.invuln:
                    text = self.font2.render('Invulnerability',1,colorlist[self.powertracker/10%3])
                    self.screen.blit(text,(640/2,height))
                if self.score > self.highscore:
                    text = self.font.render('High Score!',1,colorlist[self.powertracker/10%3])
                    self.screen.blit(text,(10,10+score1))
        else:
            text = self.font.render('No Clip Enabled',1,color)
            self.screen.blit(text,(10,10))
            text = self.font.render('God Mode Enabled',1,color)
            self.screen.blit(text,(630-text.get_width(),10))
            text = self.font.render('Press tilde to deactivate cheats.',1,color)
            self.screen.blit(text,(320-text.get_width()/2,30))

    def win_game(self):
        s = 1
        self.clear_level()
        while s:
            winscreen = pygame.image.load(data.filepath('%swin.png'%self.toon.lower()))
            self.screen.blit(winscreen,(0,0))
            events = pygame.event.get()
            for event in events:
                if event.type == KEYDOWN:
                    s = 0
                    self.drawstats()
                if event.type == QUIT:
                    sys.exit()
                    return
            pygame.display.flip()

    def drawstats(self):
        s = 1
        while s:
            self.screen.fill((0,0,0))
            text = self.font.render('W I N N E R    W I N N E R    W I N N E R    W I N N E R',1,(255,255,255))
            self.screen.blit(text,(320-text.get_width()/2,20))
            text = self.font.render('Played as %s!'%self.toon,1,(255,255,255))
            self.screen.blit(text,(320-text.get_width()/2,60))
            text = self.font.render('Lives left - %s'%str(self.lives),1,(255,255,255))
            self.screen.blit(text,(320-text.get_width()/2,100))
            text = self.font.render('Scored %s points!'%str(self.score),1,(255,255,255))
            self.screen.blit(text,(320-text.get_width()/2,140))
            text = self.font.render('With those points you could have . . .',1,(255,255,255))
            self.screen.blit(text,(320-text.get_width()/2,180))
            text = self.font.render('Killed %s Goombas!'%str(self.score/100),1,(255,255,255))
            self.screen.blit(text,(320-text.get_width()/2,200))
            text = self.font.render('Destroyed %s Bricks!'%str(self.score/10),1,(255,255,255))
            self.screen.blit(text,(320-text.get_width()/2,220))
            text = self.font.render('Restarted %s times!'%str(self.score/3000),1,(255,255,255))
            self.screen.blit(text,(320-text.get_width()/2,240))
            text = self.font.render('Killed %s Bowsers!'%str(self.score/500),1,(255,255,255))
            self.screen.blit(text,(320-text.get_width()/2,260))
            text = self.font.render('Entered Peach\'s Castle %s time!'%str(self.score/1000),1,(255,255,255))
            self.screen.blit(text,(320-text.get_width()/2,280))
            text = self.font.render('Killed %s Red Koopas!'%str(self.score/195),1,(255,255,255))
            self.screen.blit(text,(320-text.get_width()/2,300))
            text = self.font.render('Killed %s Green Koopas!'%str(self.score/165),1,(255,255,255))
            self.screen.blit(text,(320-text.get_width()/2,320))
            text = self.font.render('Collected %s MegaMushrooms!'%str(self.score/45),1,(255,255,255))
            self.screen.blit(text,(320-text.get_width()/2,340))
            text = self.font.render('Collected %s One Ups!'%str(self.score/30),1,(255,255,255))
            self.screen.blit(text,(320-text.get_width()/2,360))
            text = self.font.render('Done %s other things with your time!'%str(self.score/13),1,(255,255,255))
            self.screen.blit(text,(320-text.get_width()/2,380))
            text = self.font.render('Press any key to contine.',1,(255,255,255))
            self.screen.blit(text,(320-text.get_width()/2,430))
            events = pygame.event.get()
            if self.score > self.highscore:
                Savefile('scores.txt').writescore(self.score)
            for event in events:
                if event.type == KEYDOWN:
                    start.Menu(self.screen)
                if event.type == QUIT:
                    sys.exit()
                    return
            pygame.display.flip()


    def main_loop(self):
        while self.start:
            if not self.paused:
                self.clock.tick(60)
                self.camera.update()

                # for guy in self.character:
                #     guy.update()

                #########################################
                # HANDLES NO CLIPPING TOGGLING
                #########################################
                if self.cheat_enabled:
                    self.player.no_clip = 1
                    self.player.clear_collisions()
                else:
                    self.player.no_clip = 0

                #########################################
                # DEALS WITH NO CLIP INVICIBILITY
                #########################################
                if self.record == 'konami' and not self.chill and self.lvl != 9:
                    print 'C H E A T    E N A B L E D'
                    self.cheat_enabled = 1
                    self.chill = 1
                    data.stop_music()
                    data.play_music('winner.wav')

                if self.lvl == 9 and self.cheat_enabled:
                    self.cheat_enabled = 0
                    print 'C H E A T    D I S A B L E D'
                    print 'You no longer need to cheat. You cannot die in this sanctuary.'

                #########################################
                # FIX FOR MULTIPLE DYING SOUNDS, DYING IN GENERAL
                #########################################
                if self.flagged:
                    if self.diefix == 0:
                        die = data.load_sound('die.wav')
                        die.play()
                        self.diefix += 1
                    self.playerdie()

                #########################################
                # PRECAUTION IF FLAG DOES NOT CATCH YOU FOR SOME REASON
                #########################################
                if self.player.rect.right > self.level.size:
                    self.player.rect.right = self.level.size

                #########################################
                # KILLS YOU/SAVES YOU IF YOU FALL
                #########################################
                if self.player.rect.top > 460 and not self.player.invuln:
                    self.player.life -= 1
                    self.flagged = 1
                    self.playerdie()
                elif self.player.rect.bottom > 460 and self.player.invuln and not self.cheat_enabled:
                    self.player.rect.bottom = 460
                    self.player.save = 1

                #########################################
                # HANDLES INVULNERABILITY
                #########################################
                for toon in self.sprites:
                    toon.update()
                    if not self.cheat_enabled:
                        if self.player.invuln:
                            self.player.timer += 1
                            if self.player.timer > 250000:
                                self.player.invuln = 0
                                self.player.timer = 0
                                self.player.save = 0

                #########################################
                # CANNOT LOSE VICTORY LEVEL
                #########################################
                if self.lvl == 9 or self.cheat_enabled:
                    self.player.invuln = 1

                for platform in self.platforms:
                    platform.update()

                if self.player.no_clip != 1:
                    self.player.collide(self.platforms)

                for banner in self.flags:
                    banner.update()
                    if self.player.rect.centerx >= banner.rect.centerx and self.lvl !=9:
                        pygame.mixer.music.stop()
                        self.complete.play()
                        self.score += 460-self.player.rect.bottom
                        self.finish()
                    elif self.player.rect.centerx >= banner.rect.centerx:
                        self.score += 1000
                        self.win_game()


                #########################################
                # HANDLES CANNON FIRING
                #########################################
                for weapon in self.cannons:
                    if abs(weapon.rect.centerx-self.player.rect.centerx) < 400:
                        if self.player.rect.centerx < weapon.rect.centerx:
                            weapon.chance()

                #########################################
                # COIN EXTRACTION
                #########################################
                for block in self.coinquestions:
                    if block.rect.bottom == self.player.rect.top and (block.rect.left-15 < self.player.rect.centerx < block.rect.right+15):
                        block.bing()

                #########################################
                # HANDLES BULLET BILLS
                #########################################
                for bomb in self.missles:
                    if (bomb.rect.left - 20 < self.player.rect.centerx < bomb.rect.right + 20) and (0 < bomb.rect.top-self.player.rect.bottom < 5):
                            self.score += 245
                            self.player.up = -6
                            GrabCoin((bomb.rect.left,bomb.rect.top))
                            bomb.kill()
                            self.player.rect.bottom = bomb.rect.top-1
                    elif self.player.rect.colliderect(bomb.rect):
                        if self.player.invuln:
                            self.score += 20
                            GrabCoin((bomb.rect.left,bomb.rect.top))
                            bomb.kill()
                        else:
                            self.player.life -= 1
                            self.flagged = 1
                            self.playerdie()
                    bomb.update()

                #########################################
                # HANDLES BOWSER FIRE AND FLARES
                #########################################
                for heat in self.fire:
                    heat.update()
                    if self.player.rect.colliderect(heat.rect):
                        if self.player.invuln != 1:
                            self.player.life -= 1
                            self.flagged = 1
                            self.playerdie()
                        else:
                            heat.kill()

                for flare in self.flares:
                    if self.player.rect.colliderect(flare.rect):
                        if self.player.invuln:
                            flare.kill()
                        else:
                            self.player.life -= 1
                            self.flagged = 1
                            self.playerdie()

                #########################################
                # HANDLES QUESTIONBLOCK EXTRACTION
                #########################################
                for block in self.upplat:
                    if block.rect.bottom == self.player.rect.top and (block.rect.left-15 < self.player.rect.centerx < block.rect.right+15):
                        block.bing()

                for block in self.brickquestions:
                    if block.rect.bottom == self.player.rect.top and (block.rect.left-15 < self.player.rect.centerx < block.rect.right+15):
                        block.bing()

                for block in self.starquestions:
                    if block.rect.bottom == self.player.rect.top and (block.rect.left-15 < self.player.rect.centerx < block.rect.right+15):
                        block.bing()

                #########################################
                # HANDLES BRICK DEMOLITION
                #########################################
                for block in self.breakable:
                    if block.rect.bottom == self.player.rect.top and (block.rect.left-15 < self.player.rect.centerx < block.rect.right+15):
                        if self.player.breaker == 1:
                            block.bing()
                        if block.hits >= 9:
                            block.kill()
                            self.score += 10

                #########################################
                # HANDLES MUSHROOMS
                #########################################
                for shroom in self.mushrooms:
                    shroom.update()
                    shroom.collide(self.platforms)
                    if self.player.rect.colliderect(shroom.rect):
                        shroom.kill()
                        self.power.play()
                        if shroom.name == 'brick':
                            self.player.breaker = 1
                            self.score += 45
                            #self.player.magic()
                        if shroom.name == 'life':
                            self.lives += 1
                            self.score += 30
                        GrabShroom(shroom.rect.topleft,shroom.name)

                #########################################
                # HANDLES STARS
                #########################################
                for star in self.powerup:
                    star.update()
                    if self.player.rect.colliderect(star.rect):
                        star.kill()
                        self.power.play()
                        if self.player.invuln == 0:
                            self.player.invuln = 1
                        GrabShroom(star.rect.topleft,star.name)

                #########################################
                # HANDLES COINS
                #########################################
                for coin in self.coins:
                    if self.player.rect.colliderect(coin.rect):
                        coin.kill()
                        self.score += 50
                        self.coinsound.play()
                        GrabCoin(coin.rect.topleft)

                #########################################
                # HANDLES SPIKES
                #########################################
                for dagger in self.hazards:
                    if self.player.rect.colliderect(dagger.rect):
                        if self.player.invuln != 1:
                            self.player.life -= 1
                            self.flagged = 1
                            self.playerdie()
                        else:
                            dagger.kill()

                #########################################
                # HANDLES ENEMY COLLISIONS AND BOWSER BEHAVIOR
                #########################################
                for enemy in self.enemies:
                    enemy.update()
                    enemy.collide(self.stationary)
                    if enemy.name == 'Bowser':
                        if self.player.rect.centerx+3000 >= enemy.x:
                            if self.player.rect.right - enemy.rect.left < -75:
                                enemy.play((self.player.rect.right,self.player.rect.top))
                            elif self.player.rect.right - enemy.rect.left > -75:
                                enemy.defeat()
                        if self.player.rect.colliderect(enemy.rect):
                            if not self.player.invuln:
                                self.player.life -=1
                                self.flagged = 1
                                self.playerdie()
                    if enemy.name != 'Bowser':
                        if (enemy.rect.left - 17 < self.player.rect.centerx < enemy.rect.right + 17) and (0 < enemy.rect.top-self.player.rect.bottom < 8):
                            if enemy.name == 'Goomba':
                                self.score += 100
                            if enemy.name == 'RedKoopa':
                                self.score += 195
                            if enemy.name == 'GreenKoopa':
                                self.score += 165
                            self.player.up = -6
                            enemy.flag()
                            self.player.rect.bottom = enemy.rect.top-1
                        elif self.player.rect.colliderect(enemy.rect):
                            if self.player.invuln:
                                self.score += 20
                                enemy.flag()
                            else:
                                if self.player.breaker == 0:
                                    self.player.life -= 1
                                    self.flagged = 1
                                    self.playerdie()
                                else:
                                    enemy.flag()
                                    self.player.rect.bottom = enemy.rect.top-1
                                    self.player.breaker = 0
                                    #self.player.magic()

                #########################################
                # HANDLES BOWSER SWITCH KILLER
                #########################################
                for operator in self.switches:
                    if self.player.rect.bottom == operator.rect.top and (operator.rect.left-16 < self.player.rect.centerx < operator.rect.right+16):
                        for piece in self.bridges:
                            piece.kill()
                            for enemy in self.enemies:
                                if enemy.name == 'Bowser':
                                    enemy.die()
                    if self.player.rect.centerx > operator.rect.right:
                        for piece in self.bridges:
                            piece.kill()
                        for enemy in self.enemies:
                            if enemy.name == 'Bowser':
                                enemy.die()
                    if self.player.rect.left > operator.rect.right+50 and operator.dead == 0:
                        x = operator.x
                        y = operator.y
                        for mult in xrange(0,8):
                            CastleBrick((x,y-32*mult),None)
                        win = data.load_sound('break.wav',1)
                        win.play()
                        self.score += 500
                        operator.dead += 1

                #########################################
                # HANDLES PLANTS
                #########################################
                for venus in self.traps:
                    venus.update()
                    venus.collide(self.bases)
                    if self.player.rect.colliderect(venus.rect):
                        die = data.load_sound('stomp.wav',1)
                        if self.player.invuln:
                            venus.die()
                        else:
                            if self.player.breaker == 0:
                                self.player.life -= 1
                                self.flagged = 1
                                self.playerdie()
                            else:
                                self.player.breaker = 0
                                venus.die()

                #########################################
                # HANDLES EVENTS AND CHEAT CODES
                #########################################
                events = pygame.event.get()
                for event in events:
                    if event.type == QUIT:
                        sys.exit()
                        return
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            self.paused = 1
                        if event.key == K_SPACE:
                            if not self.player.no_clip:
                                self.player.jump()
                        if self.record == '':
                            if event.key == K_k:
                                self.record += 'k'
                        if event.key == K_o and self.record == 'k':
                            self.record += 'o'
                        if event.key == K_n and self.record == 'ko':
                            self.record += 'n'
                        if event.key == K_a and self.record == 'kon':
                            self.record += 'a'
                        if event.key == K_m and self.record == 'kona':
                            self.record += 'm'
                        if event.key == K_i and self.record == 'konam':
                            self.record += 'i'
                        if self.record == 'konami':
                            if event.key == K_BACKQUOTE:
                                okay = 1
                                for sprite in self.platforms:
                                    if self.player.rect.colliderect(sprite.rect):
                                        okay = 0
                                if okay:
                                    self.record = ''
                                    self.chill = 0
                                    self.cheat_enabled = 0
                                    self.player.invuln = 0
                                    print 'C H E A T    D I S A B L E D'
                                    data.stop_music()
                                    data.play_music(self.bgcolor[self.lvl][1])
                                else:
                                    print 'This is not a valid location to turn on clipping!'

            #########################################
            # HANDLES SCREEN CREATION
            #########################################
            if not self.paused:
                self.screen.blit(self.bg, ((-self.camera.rect.x/1)%640, 0))
                self.screen.blit(self.bg, ((-self.camera.rect.x/1)%640 + 640, 0))
                self.screen.blit(self.bg, ((-self.camera.rect.x/1)%640 - 640, 0))
                self.camera.create_world(self.screen, self.sprites)
                self.info()
                pygame.display.flip()

            #########################################
            # HANDLES PAUSE SCREEN
            #########################################
            elif self.paused and not self.saving:
                events = pygame.event.get()
                pause = data.load_image('pausescreen.png',1)
                self.screen.blit(pause,(0,0))
                self.menu.create(self.screen)
                self.menu.choose(events)
                text = self.font.render('NOTE :',1,(255,0,0))
                self.screen.blit(text,(320-text.get_width()/2,360))
                text = self.font.render('If you quit without saving,',1,(255,255,255))
                self.screen.blit(text,(320-text.get_width()/2,390))
                text = self.font.render('your progress will be lost.',1,(255,255,255))
                self.screen.blit(text,(320-text.get_width()/2,420))
                for event in events:
                    if event.type == QUIT:
                        sys.exit()
                        return
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            self.paused = 0
                pygame.display.flip()

            #########################################
            # HANDLES SAVES ETC.
            #########################################
            elif self.paused and self.saving:
                events = pygame.event.get()
                save = data.load_image('save.bmp',1)
                self.screen.blit(save,(0,0))
                saves = Savefile().read()
                if saves == []:
                    self.menu2.create(self.screen)
                    self.menu2.choose(events)
                else:
                    self.menu3.create(self.screen)
                    self.menu3.choose(events)
                for event in events:
                    if event.type == QUIT:
                        sys.exit()
                        return
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            self.saving = 0
                pygame.display.flip()

            if self.lvl == 9:
                if self.player.rect.top < 100:
                    self.player.save = 0

    def placeholder(self):
        self.paused = 0

    def placeholder1(self):
        self.saving = 1

    def placeholder2(self,screen):
        self.player.woo.stop()
        pygame.mixer.music.stop()
        start.Menu(self.screen)

    def save1(self,toon,level,lives):
        saves = Savefile().read()
        if saves == []:
            Savefile().write(toon,level,lives,1,True)
        else:
            Savefile().write(toon,level,lives,1)
        self.save_menu()
        if self.score > self.highscore:
            Savefile('scores.txt').writescore(self.score)

    def save2(self,toon,level,lives):
        saves = Savefile().read()
        if saves == []:
            Savefile().write(toon,level,lives,2,True)
        else:
            Savefile().write(toon,level,lives,2)
        self.save_menu()
        if self.score > self.highscore:
            Savefile('scores.txt').writescore(self.score)

    def save3(self,toon,level,lives):
        saves = Savefile().read()
        if saves == []:
            Savefile().write(toon,level,lives,3,True)
        else:
            Savefile().write(toon,level,lives,3)
        self.save_menu()
        if self.score > self.highscore:
            Savefile('scores.txt').writescore(self.score)











#
