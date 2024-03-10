from options import *
from playerProperties import *

xp = player_X
yp = player_Y
spdp = player_speed
jumping = False
jump_height = jumpheight
gravity = 1
camera_x = 0
treeX = -20
treeY = 0
treeSpeed = 0.10
treeXflip, treeYflip = 300, 0
flowerX, flowerXs, flowerXt = 100, 300, 550

def setup():
    size(640, 480)
    #size(1280, 720)
    
    
    #SPRITES
    global tileOne, tileBg, version, tileTwo, tileThree, tileThreeFlip, tileFour, tileOneClone, tileFive, tileOneC, player
    tileOne = loadImage("src/tile1.png")
    tileTwo = loadImage("src/tile1.png")
    tileBg = loadImage("src/tile2.png")
    version = loadImage("src/ver.png")
    version.resize(version.width / 6, version.height / 7)
    tileThree = loadImage("src/tile3.png")
    tileThreeFlip = loadImage("src/tile3Flip.png")
    tileFour = loadImage("src/tile4.png")
    tileOneClone = loadImage("src/tile1A.png")
    tileFive = loadImage("src/tile5.png")
    tileOneC = loadImage("src/tile1C.png")
    player = loadImage("src/player/idle.png")
    
def draw():
    global xp, yp, spdp, jumping, jump_height, gravity, treeX, treeY, treeXflip, treeYflip, spritePlayer
    background(255)
    translate(-camera_x, 0)
    noSmooth()
    image(tileBg, 0, 0)
    sprite_width, sprite_height = tileOne.width / 1, tileOne.height / 2
    image(tileOne, -30, 300, sprite_width, sprite_height, 0, 0, sprite_width, sprite_height)
    image(tileFour, flowerX, 200)
    image(tileFour, flowerXs, 220)
    image(tileFour, flowerXt, 215)
    image(tileThree, treeX, treeY)
    image(tileThreeFlip, treeXflip, treeYflip)
    image(tileOneC, 900, 290)
    image(tileFive, 700, 340)
    
    ##PLAYER##
    if jumping:
        yp -= jump_height
        jump_height -= gravity
        if yp >= player_Y: 
            yp = player_Y
            jump_height = 10
            jumping = False
            

    if spritePlayer == 'img':
        image(player, xp, yp)
    elif spritePlayer == 'rect':
        fill(255)
        rect(xp, yp, 64, 64)
    else:
        fill(255)
        rect(xp, yp, 64, 64)
        
    resetMatrix()
    image(version, 0, 0)



def keyPressed():
    from options import goLeft, goRight, jump
    global flowerXt, flowerX, flowerXs, treeXflip, treeYflip, xp, yp, spdp, jumping, jump_height, gravity, camera_x, jump, goLeft, goRight, treeX, treeSpeed
    if key == jump:
        if not jumping:
            jumping = True
            jump_height = 15  
    if key == goRight:
        xp += spdp
        if xp - camera_x > width * 0.6:  
            camera_x += spdp
    if key == goLeft:
        xp -= spdp
        if xp - camera_x < width * 0.4:  
            camera_x -= spdp
            
            
if debug == 'enabled':
    #DEBUG
    print('debug is enabled.')
    print(sectOne)
    print("version: ", ver)
    print("author: ", ath)
    print("")
    print("leftButton: ", goLeft)
    print("rightButton: ", goRight)
    print("jumpButton: ", jump)
    print("")
    print("windowWidth: ", sizeW)
    print("windowHeight: ", sizeH)
    print("backgroundColor: ", bgColor)
    print("")
    print(sectPl)
    print("playerY: ", player_Y)
    print("playerX: ", player_X)
    print("playerSpeed: ", player_speed)
    print("jumpHeight: ", jumpheight)
    print("player: ", spritePlayer)
if debug == 'disabled':
    print('debug is disabled.')
            
