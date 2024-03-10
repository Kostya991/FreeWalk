sectPl = ""
can_jump = True
player_Y, player_X, player_speed, jumpheight = 0, 0, 0, 0
spritePlayer = ""

def code(line):
    global sectPl, can_jump, player_Y, player_X, player_speed, jumpheight, spritePlayer
    if line.startswith("{SECTION ") and line.endswith("}"):
        sc = line[9:-1]
        sectPl = sc
    elif line.startswith("player_X>") and line.endswith("<"):
        xp = line[9:-1]
        player_X = int(xp)
    elif line.startswith("player_Y>") and line.endswith("<"):
        yp = line[9:-1]
        player_Y = int(yp)
    elif line.startswith("player_speed>") and line.endswith("<"):
        sp = line[13:-1]
        player_speed = int(sp)
    elif line.startswith("jump_height>") and line.endswith("<"):
        jh = line[12:-1]
        jumpheight = int(jh)
    elif line.startswith("can_jump>") and line.endswith("<"):
        cj = line[9:-1]
        can_jump = cj
    elif line.startswith("player_sprite>") and line.endswith("<"):
        sprite = line[14:-1]
        spritePlayer = sprite
        
def file():
    with open("src/player.winescript") as plp:
        for line in plp:
            code(line.strip())
            
file()
