appname, debug, sectOne, ath, ver, goLeft, goRight, jump, start = "", "", "", "", "", "", "", "", ""
sizeW, sizeH, bgColor = 0, 0, 0

def code(line):
    global start, sectOne, ath, ver, goLeft, goRight, jump, sizeW, sizeH, bgColor, debug, appname
    if line.startswith("{SECTION ") and line.endswith("}"):
        sc = line[9:-1]
        sectOne = sc
    elif line.startswith("ver>") and line.endswith("<"):
        vr = line[4:-1]
        ver = vr
    elif line.startswith("appname>") and line.endswith("<"):
        ap = line[8:-1]
        appname = ap 
    elif line.startswith("ath>") and line.endswith("<"):
        at = line[4:-1]
        ath = at
    elif line.startswith("sizeW>") and line.endswith("<"):
        sw = line[6:-1]
        sizeW = int(sw)
    elif line.startswith("sizeH>") and line.endswith("<"):
        sh = line[6:-1]
        sizeH = int(sh)
    elif line.startswith("bgColor>") and line.endswith("<"):
        bc = line[8:-1]
        bgColor = int(bc)
    elif line.startswith("left>") and line.endswith("<"):
        gl = line[5:-1]
        goLeft = gl
    elif line.startswith("right>") and line.endswith("<"):
        gr = line[6:-1]
        goRight = gr
    elif line.startswith("jump>") and line.endswith("<"):
        jm = line[5:-1]
        jump = jm
    elif line.startswith("start>") and line.endswith("<"):
        st = line[6:-1]
        start = st
    elif line.startswith("debug_mode>") and line.endswith("<"):
        deb = line[11:-1]
        debug = deb
        
def file():
    with open("src/options.winescript") as opt:
        for line in opt:
            code(line.strip())
            
file()
