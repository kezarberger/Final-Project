

from ggame import App, RectangleAsset, ImageAsset, SoundAsset, Sprite, Sound
from ggame import LineStyle, Color

SCREEN_WIDTH = 1358
SCREEN_HEIGHT = 600

yellow = Color(0xfff400, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
white = Color(0xffffff, 1.0)
black = Color(0, 1)
noline = LineStyle(0, black)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, red)
bg = Sprite(bg_asset, (0,0))

bunny_asset = ImageAsset("images/bunny.png")
bunny = Sprite(bunny_asset, (0,0))
bunny.scale = 1.5
bunny.dir = 5
bunny.go = True

beachball_asset = ImageAsset("images/beach-ball-575425_640.png")
beachball = Sprite(beachball_asset, (0,200))
beachball.scale = .2
beachball.dir = 5
beachball.go = True


def reverse(b):
    b.dir *= -1
    pop.play()
    
def reverse(c):
    c.dir *= -1
    pop.play()


def step():
    if bunny.go:
        bunny.x += bunny.dir
        if bunny.x + bunny.width > SCREEN_WIDTH or bunny.x < 0:
            bunny.x -= bunny.dir
            bunny.dir *= -1
    if beachball.go:
        beachball.x += beachball.dir
        if beachball.x + beachball.width > SCREEN_WIDTH or beachball.x < 0:
            beachball.x -= beachball.dir
            beachball.dir *= -1


def spaceKey(event):
    bunny.go = not bunny.go

def rKey(event):
    reverse(bunny)
    
def zKey(event):
    bunny.scale = 1

def xKey(event):
    bunny.scale = 1.5    

def mKey(event):
    if bunny.dir > 2.5 or bunny.dir < -2.5:
        bunny.dir /= 2

def nKey(event):
    if bunny.dir < 5 and bunny.dir > -5:
        bunny.dir *= 2 
    
def tKey(event):
    beachball.go = not beachball.go
    
def eKey(event):
    reverse(beachball)
    
def wKey(event):
    if beachball.scale >= .025:
        beachball.scale /= 2

def qKey(event):
    if beachball.scale <= .2:
        beachball.scale *= 2
    
def yKey(event):
     if beachball.dir > 2.5 or beachball.dir < -2.5:
        beachball.dir /= 2
        
def uKey(event):
    if beachball.dir < 5 and beachball.dir > -5:
        beachball.dir *= 2 

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenKeyEvent('keydown', 'space', spaceKey)
myapp.listenKeyEvent('keydown', 'r', rKey)
myapp.listenKeyEvent('keydown', 'z', zKey)
myapp.listenKeyEvent('keydown', 'x', xKey)
myapp.listenKeyEvent('keydown', 'm', mKey)
myapp.listenKeyEvent('keydown', 'n', nKey)
myapp.listenKeyEvent('keydown', 't', tKey)
myapp.listenKeyEvent('keydown', 'e', eKey)
myapp.listenKeyEvent('keydown', 'w', wKey)
myapp.listenKeyEvent('keydown', 'q', qKey)
myapp.listenKeyEvent('keydown', 'y', yKey)
myapp.listenKeyEvent('keydown', 'u', uKey)
myapp.run(step)
