from ggame import App, RectangleAsset, ImageAsset, SoundAsset, Sprite, Sound
from ggame import LineStyle, Color

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 700

yellow = Color(0xfff400, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
white = Color(0xffffff, 1.0)
black = Color(0, 1)
noline = LineStyle(0, black)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, yellow)
bg = Sprite(bg_asset, (0,0))

bunny_asset = ImageAsset("images/bunny.png")
bunny = Sprite(bunny_asset, (0,0))
bunny.scale = 1.5
bunny.dir = 2.5
bunny.go = True

beachball_asset = ImageAsset("images/beach-ball-575425_640.png")
beachball = Sprite(beachball_asset, (20,200))
beachball.scale = .2
beachball.dir = 2.5
beachball.go = True

sun_asset = ImageAsset("images/sun.png")
sun = Sprite(sun_asset, (20,375))
sun.scale = 1.5
sun.dir = 2.5
sun.go = True

marble_asset = ImageAsset("images/orb-150545_640.png")
marble = Sprite(marble_asset, (0,500))
marble.scale = .2
marble.dir = 2.5
marble.go = True

def reverse(b):
    b.dir *= -1

def reverse(c):
    c.dir *= -1
   
def reverse(s):
    s.dir *= -1
    
def reverse(m):
    m.dir *= -1

def step():
    if bunny.go:
        bunny.y += bunny.dir
        if bunny.y + bunny.width > SCREEN_HEIGHT or bunny.y < 0:
            bunny.y -= bunny.dir
            bunny.dir *= -1
    if beachball.go:
        beachball.x += beachball.dir
        if beachball.x + beachball.width > SCREEN_WIDTH or beachball.x < 0:
            beachball.x -= beachball.dir
            beachball.dir *= -1
    if sun.go:
        sun.x += sun.dir
        if sun.x + sun.width > SCREEN_WIDTH or sun.x < 20:
            sun.x -= sun.dir
            sun.dir *= -1
    if marble.go:
        marble.x += marble.dir
        if marble.x + marble.width > SCREEN_WIDTH or marble.x < 0:
            marble.x -= marble.dir
            marble.dir *= -1
    

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
        
def cKey(event):
    bunny.dir /= 2
    
def vKey(event):
    bunny.dir = -2.5
    
def bKey(event):
    bunny.dir /= 2
    
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
        
def aKey(event):
    sun.go = not sun.go

def dKey(event):
    reverse(sun)

def gKey(event):
    if sun.scale > 1 and sun.scale < 2.5:
        sun.scale -= .1

def hKey(event):
    if sun.scale > .5 and sun.scale < 2:
        sun.scale += .1
        
def fKey(event):
    if sun.dir >= 1.5 and sun.dir <= 5:
        sun.dir -= .25
        
def sKey(event):
    if sun.dir >= 1 and sun.dir <= 5:
        sun.dir += .25

def lKey(event):
    marble.go = not marble.go
    
def iKey(event):
    reverse(marble)
    
def jKey(event):
    marble.scale = .01

def kKey(event):
    marble.scale = .325

def oKey(event):
    if marble.dir >= .5 or marble.dir <= -.5:
        marble.dir *= -.5
    
def pKey(event):
    if marble.dir <= 4.5:
        marble.dir /= -.75


myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenKeyEvent('keydown', 'space', spaceKey)
myapp.listenKeyEvent('keydown', 'r', rKey)
myapp.listenKeyEvent('keydown', 'z', zKey)
myapp.listenKeyEvent('keydown', 'x', xKey)
myapp.listenKeyEvent('keydown', 'm', mKey)
myapp.listenKeyEvent('keydown', 'n', nKey)
myapp.listenKeyEvent('keydown', 'c', cKey)
myapp.listenKeyEvent('keydown', 'v', vKey)
myapp.listenKeyEvent('keydown', 'b', bKey)
myapp.listenKeyEvent('keydown', 't', tKey)
myapp.listenKeyEvent('keydown', 'e', eKey)
myapp.listenKeyEvent('keydown', 'w', wKey)
myapp.listenKeyEvent('keydown', 'q', qKey)
myapp.listenKeyEvent('keydown', 'y', yKey)
myapp.listenKeyEvent('keydown', 'u', uKey)
myapp.listenKeyEvent('keydown', 'a', aKey)
myapp.listenKeyEvent('keydown', 'd', dKey)
myapp.listenKeyEvent('keydown', 'g', gKey)
myapp.listenKeyEvent('keydown', 'h', hKey)
myapp.listenKeyEvent('keydown', 'f', fKey)
myapp.listenKeyEvent('keydown', 's', sKey)
myapp.listenKeyEvent('keydown', 'l', lKey)
myapp.listenKeyEvent('keydown', 'i', iKey)
myapp.listenKeyEvent('keydown', 'j', jKey)
myapp.listenKeyEvent('keydown', 'k', kKey)
myapp.listenKeyEvent('keydown', 'o', oKey)
myapp.listenKeyEvent('keydown', 'p', pKey)
myapp.run(step)
