""""
# Title of Your Project Here



## Functional Specification

This document should become the functional specification of the project you are working on.

A functional specification describes in great detail how a device or program will appear to an
outside user. That is, it treats all hardware as a "black box", the contents of which are completely
unknown to the user. The functional specification should include sections with the following information:

Your specification **should include** the following types of information:

* A title. Replace the title at the beginning of this document.
* Summary or introduction. In general, in a few lines or less, what is your program about or what is it about?
* How does the user access your program? Is it shared via http://runpython.com? Is a web site? Embedded in 
  a single board computer? 
* If there are graphics screens involved, describe every screen that the user will experience: what is it for? 
  What did the user have to do to get there and how does she move on to the next?
* For each graphics screen, describe every active control input and what it does. What elements on the screen will
  change in response to user input?
* Does the program respond to mouse input? What, exactly, does the mouse do?
* Does the program respond to keyboard input? How?
* What graphical assets will be used?
* Does the user have to do anything to install the program?

Your specification should **not** include the following types of information:

* The language you will use to create it.
* Names of any specific files in the project.
* How you will structure the classes, functions and code in your program.
* The name of any files or tools that you will use to design the program.
"""

from ggame import App, RectangleAsset, ImageAsset, SoundAsset, Sprite, Sound
from ggame import LineStyle, Color

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

yellow = Color(0xfff400, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
white = Color(0xffffff, 1.0)
black = Color(0, 1)
noline = LineStyle(0, black)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, green)
bg = Sprite(bg_asset, (0,0))

bunny_asset = ImageAsset("images/bunny.png")
bunny = Sprite(bunny_asset, (0,0))
bunny.scale = 2
bunny.dir = 5
bunny.go = True

def reverse(b):
    b.dir *= -1
    pop.play()


def step():
    if bunny.go:
        bunny.x += bunny.dir
        if bunny.x + bunny.width > SCREEN_WIDTH or bunny.x < 0:
            bunny.x -= bunny.dir
            bunny.dir *= -1
            
def spaceKey(event):
    bunny.go = not bunny.go

# Handle the "reverse" key
def rKey(event):
    reverse(bunny)
    
def zKey(event):
    bunny.scale = 1

def xKey(event):
    bunny.scale = 2    

def mKey(event):
    if bunny.dir > 2.5 or bunny.dir < -2.5:
        bunny.dir /= 2

def nKey(event):
    if bunny.dir < 5 and bunny.dir > -5:
        bunny.dir *= 2 
    


myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenKeyEvent('keydown', 'space', spaceKey)
myapp.listenKeyEvent('keydown', 'r', rKey)
myapp.listenKeyEvent('keydown', 'z', zKey)
myapp.listenKeyEvent('keydown', 'x', xKey)
myapp.listenKeyEvent('keydown', 'm', mKey)
myapp.listenKeyEvent('keydown', 'n', nKey)
myapp.run(step)
