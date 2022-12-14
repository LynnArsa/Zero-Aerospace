import OpenGL.GLUT as glut
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import json
import random as rd

play = False
w,h = 1000,720

xPosition = 500
yPosition = 100

x_time = 0 
detik = 1
penambah_detik = 600//60

xBorder = 1000
yBorder = 720

xMeteorPos = 0
yMeteorPos = yBorder
kecepatan_meteor = 5

crash = False

def drawTextBold(ch,xpos,ypos):
    glPushMatrix()
    font_style = glut.GLUT_BITMAP_HELVETICA_18
    glColor3ub(0, 0, 0)
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+5
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))  
    glPopMatrix()  

def start_game():
    glPushMatrix()
    glColor3b(10, 30, 40)
    glBegin(GL_LINES)
    #W
    glVertex2f(100, 700)
    glVertex2f(100, 600)
    glVertex2f(100, 600)
    glVertex2f(147.0753101402632, 647.8066849179667)
    glVertex2f(147.0753101402632, 647.8066849179667)
    glVertex2f(200, 600)
    glVertex2f(200, 600)
    glVertex2f(200, 700)
    glEnd()
    glColor3b(10, 30, 40)
    glBegin(GL_LINES)
    #E
    glVertex2f(233.1210229861111, 696.2745538452275)
    glVertex2f(239.3217068894451, 603.0811592213937)
    glVertex2f(239.3217068894451, 603.0811592213937)
    glVertex2f(300, 600)
    glVertex2f(233.1210229861111, 696.2745538452275)
    glVertex2f(300, 700)
    glVertex2f(235.9107135871987, 654.3468018232652)
    glVertex2f(293.8309413321435, 649.2043575959846)
    glEnd()
    glColor3b(10, 30, 40)
    glBegin(GL_LINES)
    #L
    glVertex2f(342.3064724474077, 700.174034183131)
    glVertex2f(338.5564670287166, 603.0811592213937)
    glVertex2f(338.5564670287166, 603.0811592213937)
    glVertex2f(400, 600)
    glEnd()
    glColor3b(10, 30, 40)
    glBegin(GL_LINES)
    #C
    glVertex2f(439.1888998460058, 698.1229013266112)
    glVertex2f(500, 700)
    glVertex2f(439.1888998460058, 698.1229013266112)
    glVertex2f(441.9842452020417, 603.0811592213937)
    glVertex2f(441.9842452020417, 603.0811592213937)
    glVertex2f(500, 600)
    glEnd()
    glColor3b(10, 30, 40)
    glBegin(GL_LINES)
    #O
    glVertex2f(539.8213326632952, 700.918246682647)
    glVertex2f(539.8213326632952, 603.0811592213937)
    glVertex2f(539.8213326632952, 603.0811592213937)
    glVertex2f(600, 600)
    glVertex2f(600, 600)
    glVertex2f(600, 700)
    glVertex2f(600, 700)
    glVertex2f(539.8213326632952, 700.918246682647)
    glEnd()
    glColor3b(10, 30, 40)
    glBegin(GL_LINES)    
    #M
    glVertex2f(637.3671513487684, 702.7736877417333)
    glVertex2f(641.8514381586025, 603.0811592213937)
    glVertex2f(637.3671513487684, 702.7736877417333)
    glVertex2f(678.1909277870681, 668.7717750882352)
    glVertex2f(678.1909277870681, 668.7717750882352)
    glVertex2f(718.7234354495873, 699.5205740046291)
    glVertex2f(718.7234354495873, 699.5205740046291)
    glVertex2f(718.7234354495873, 604.4788318994116)
    glEnd()
    glColor3b(10, 30, 40)
    glBegin(GL_LINES) 
    #E
    glVertex2f(757.8582704340888, 699.5205740046291)
    glVertex2f(800, 700)
    glVertex2f(760.5573598761853, 652.2865087679437)
    glVertex2f(808.1744868427335, 653.3973756300383)
    glVertex2f(757.8582704340888, 699.5205740046291)
    glVertex2f(763.4489611461604, 601.6834865433758)
    glVertex2f(763.4489611461604, 601.6834865433758)
    glVertex2f(813.7651775548051, 605.8765045774295)
    glEnd()
    glColor3b(10, 30, 40)
    glBegin(GL_LINES) 
    #T
    glVertex2f(387.4750107593433, 515.0277805062658)
    glVertex2f(439.1888998460058, 524.8114892523912)
    glVertex2f(408.4401009296118, 558.3556335248209)
    glVertex2f(414.0307916416835, 477.2906181997824)
    glVertex2f(414.0307916416835, 477.2906181997824)
    glVertex2f(454.5632993042028, 481.4836362338361)
    glEnd()
    glColor3b(10, 30, 40)
    glBegin(GL_LINES)    
    #O
    glVertex2f(476.9260621524894, 530.4021799644628)
    glVertex2f(489.5051162546505, 478.6882908778003)
    glVertex2f(489.5051162546505, 478.6882908778003)
    glVertex2f(524.4469332050982, 482.881308911854)
    glVertex2f(524.4469332050982, 482.881308911854)
    glVertex2f(510.4702064249191, 530.4021799644628)
    glVertex2f(510.4702064249191, 530.4021799644628)
    glVertex2f(476.9260621524894, 530.4021799644628)
    glEnd()
    glColor3b(36, 150, 127)
    glBegin(GL_LINES)    
    #Z
    glVertex2f(73.8462278703461, 467.8486133872073)
    glVertex2f(162.3325937345938, 490.2132992649841)
    glVertex2f(162.3325937345938, 490.2132992649841)
    glVertex2f(66.0672066954672, 352.1356734108841)
    glVertex2f(66.0672066954672, 352.1356734108841)
    glVertex2f(171.0839925563326, 350.1909181171644)
    glEnd()
    glColor3b(36, 150, 127)
    glBegin(GL_LINES)    
    #E
    glVertex2f(202.2000772558482, 424.0916192785136)
    glVertex2f(211.9238537244469, 350.1909181171644)
    glVertex2f(211.9238537244469, 350.1909181171644)
    glVertex2f(266.3770019485993, 361.8594498794827)
    glVertex2f(202.2000772558482, 424.0916192785136)
    glVertex2f(251.3185978963272, 420.7112766333858)
    glVertex2f(251.3185978963272, 420.7112766333858)
    glVertex2f(256.6532254800006, 391.0307792852785)
    glVertex2f(256.6532254800006, 391.0307792852785)    
    glVertex2f(206.0895878432877, 390.0584016384186)
    glEnd()
    glColor3b(36, 150, 127)
    glBegin(GL_LINES)    
    #R
    glVertex2f(280, 420)
    glVertex2f(287.7693101795163, 358.9423169389031)
    glVertex2f(282.0291610115913, 404.0531698358076)
    glVertex2f(323.7472831133313, 414.3678428099151)
    glEnd()
    glColor3b(36, 150, 127)
    glBegin(GL_LINES)     
    #O
    glVertex2f(348.0567242848279, 412.4230875161953)
    glVertex2f(330.5539266413504, 352.1356734108841)
    glVertex2f(330.5539266413504, 352.1356734108841)
    glVertex2f(382.0899419249232, 352.1356734108841)
    glVertex2f(382.0899419249232, 352.1356734108841)
    glVertex2f(385.0070748655028, 413.3954651630552)
    glVertex2f(385.0070748655028, 413.3954651630552)
    glVertex2f(348.0567242848279, 412.4230875161953)
    glEnd()
    glColor3b(36, 150, 127)
    glBegin(GL_LINES)
    glVertex2f(441.404978383375, 427.9811298659531)
    glVertex2f(361.670011340866, 249.0636428437391)
    glVertex2f(465.0596953844256, 313.1871854072186)
    glVertex2f(384.1637617819391, 299.5374243212681)
    glVertex2f(441.404978383375, 427.9811298659531)
    glVertex2f(477.0028219080322, 252.902832478538)
    glEnd()
    glColor3b(36, 150, 127)
    glBegin(GL_LINES)    
    glVertex2f(490.996238373228, 336.5776310611263)
    glVertex2f(490.0238607263682, 306.4339240084707)
    glVertex2f(490.0238607263682, 306.4339240084707)
    glVertex2f(505.581903076126, 263.6493075466369)
    glVertex2f(505.581903076126, 263.6493075466369)
    glVertex2f(534.4435732834737, 273.9454839725115)
    glVertex2f(490.996238373228, 336.5776310611263)
    glVertex2f(524.7753280024588, 331.9549556586003)
    glVertex2f(524.7753280024588, 331.9549556586003)
    glVertex2f(533.7808548350621, 307.4063016553306)
    glVertex2f(533.7808548350621, 307.4063016553306)
    glVertex2f(490.0238607263682, 306.4339240084707)
    glEnd()
    glColor3b(36, 150, 127)
    glBegin(GL_LINES)     
    glVertex2f(558.0902960065587, 330.7433651799672)
    glVertex2f(564.8969395345778, 259.7597969591975)
    glVertex2f(560.6114625941032, 304.4511993384326)
    glVertex2f(597.9577795278132, 324.909099298808)
    glEnd()
    glColor3b(36, 150, 127)
    glBegin(GL_LINES)      
    glVertex2f(611.5710665838512, 309.3510569490503)
    glVertex2f(617.4053324650105, 262.6769298997771)
    glVertex2f(617.4053324650105, 262.6769298997771)
    glVertex2f(649.493794811386, 282.1244828369743)
    glVertex2f(649.493794811386, 282.1244828369743)
    glVertex2f(632.9633748147683, 326.8538545925277)
    glVertex2f(632.9633748147683, 326.8538545925277)
    glVertex2f(611.5710665838512, 309.3510569490503)
    glEnd()
    glColor3b(36, 150, 127)
    glBegin(GL_LINES)  
    #S  
    glVertex2f(706.864075976118, 330.7433651799672)
    glVertex2f(664.0794595142839, 329.7709875331074)
    glVertex2f(664.0794595142839, 329.7709875331074)
    glVertex2f(673.8032359828826, 301.5720357741714)
    glVertex2f(673.8032359828826, 301.5720357741714)
    glVertex2f(714.6430971509969, 305.4615463616109)
    glVertex2f(714.6430971509969, 305.4615463616109)
    glVertex2f(714.6430971509969, 275.3178393089552)
    glVertex2f(714.6430971509969, 275.3178393089552)
    glVertex2f(672.8308583360227, 257.8150416654778)
    glEnd()
    glColor3b(36, 150, 127)
    glBegin(GL_LINES)
    #P
    glVertex2f(742.8420489099329, 235.450355787701)
    glVertex2f(739.9249159693534, 328.7986098862475)
    glVertex2f(739.9249159693534, 328.7986098862475)
    glVertex2f(786.5990430186268, 326.8538545925277)
    glVertex2f(786.5990430186268, 326.8538545925277)
    glVertex2f(785.626665371767, 290.875881658713)
    glVertex2f(785.626665371767, 290.875881658713)
    glVertex2f(741.0813338732775, 291.7932369606774)
    glEnd()
    glColor3b(36, 150, 127)
    glBegin(GL_LINES)
    #A
    glVertex2f(807.9980427051219, 326.836472862769)
    glVertex2f(855.6378559456773, 328.7986098862475)
    glVertex2f(855.6378559456773, 328.7986098862475)
    glVertex2f(853.6931006519575, 259.7597969591975)
    glVertex2f(853.6931006519575, 259.7597969591975)
    glVertex2f(801.1847077215249, 256.8426640186179)
    glVertex2f(801.1847077215249, 256.8426640186179)
    glVertex2f(800.2123300746649, 285.0416157775538)
    glVertex2f(800.2123300746649, 285.0416157775538)
    glVertex2f(854.5141767224477, 288.9079974615992)
    glEnd()
    glColor3b(36, 150, 127)
    glBegin(GL_LINES)
    #C
    glVertex2f(898.4224724075115, 327.8262322393876)
    glVertex2f(873.140653589155, 325.8814769456679)
    glVertex2f(873.140653589155, 325.8814769456679)
    glVertex2f(880.919674764034, 253.9255310780384)
    glVertex2f(880.919674764034, 253.9255310780384)
    glVertex2f(927.5938018133074, 266.5664404872165)
    glEnd()
    glColor3b(36, 150, 127)
    glBegin(GL_LINES)    
    #E
    glVertex2f(981.0745723906, 269.4835734277961)
    glVertex2f(949.9584876910843, 263.6493075466369)
    glVertex2f(949.9584876910843, 263.6493075466369)
    glVertex2f(943.1518441630653, 325.8814769456679)
    glVertex2f(943.1518441630653, 325.8814769456679)
    glVertex2f(974.2679288625809, 341.4395192954257)
    glVertex2f(974.2679288625809, 341.4395192954257)
    glVertex2f(980.1021947437401, 304.489168714751)
    glVertex2f(980.1021947437401, 304.489168714751)
    glVertex2f(946.0301219212485, 299.5657945851367)
    glEnd()
    glColor3b(36, 150, 127)
    glBegin(GL_QUADS)
    glVertex2f(300, 200)
    glVertex2f(300, 100)
    glVertex2f(700, 100)
    glVertex2f(700, 200)
    glEnd()
    glColor3ub(0,0,0)
    glLineWidth(10)
    glBegin(GL_LINE_LOOP)
    glVertex2f(300, 200)
    glVertex2f(300, 100)
    glVertex2f(700, 100)
    glVertex2f(700, 200)
    glEnd()
    glPopMatrix()
    drawTextBold(" P  L  A  Y   G  A  M  E ",410,145)

def meteor():
    global  xBorder, xMeteorPos, yMeteorPos
    glPushMatrix()
    yMeteorPos -= kecepatan_meteor
    if yMeteorPos < -yBorder:
        yMeteorPos = yBorder
        xMeteorPos = rd.randrange(50, xBorder)

    glTranslated(xMeteorPos, yMeteorPos, 0)
    glColor3ub(92, 47, 16)
    glBegin(GL_POLYGON)
    glVertex2f(0, 30)
    glVertex2f(20, 20)
    glVertex2f(30, 0)
    glVertex2f(20, -20)
    glVertex2f(0, -30)
    glVertex2f(-20, -20)
    glVertex2f(-30, 0)
    glVertex2f(-20, 20)
    glVertex2f(0, 30)
    glEnd()
    glPopMatrix()    

def pesawat():
    global xPosition, yPosition, xBorder, yBorder
    glPushMatrix()

    glTranslated(xPosition, yPosition, 0)

    #body
    glColor3ub(240, 60, 60)
    glBegin(GL_POLYGON)
    glVertex2f(0, 60)
    glVertex2f(7.5, 57.5)
    glVertex2f(10, 50)
    glVertex2f(10, -40)
    glVertex2f(5, -60)
    glVertex2f(-5, -60)
    glVertex2f(-10, -40)
    glVertex2f(-10, 50)
    glVertex2f(-7.5, 57.5)
    glVertex2f(0, 60)
    glEnd()

    # glass
    glColor3ub(188,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(0, 55)
    glVertex2f(7.5, 52.5)
    glVertex2f(7.5, 42.5)
    glVertex2f(-7.5, 42.5)
    glVertex2f(-7.5, 52.5)
    glVertex2f(0, 55)
    glEnd()

    #right wing
    glColor3ub(182,25,25)
    glBegin(GL_POLYGON)
    glVertex2f(10, 30)
    glVertex2f(60, 30)
    glVertex2f(50, 10)
    glVertex2f(10, 5)
 
    glEnd()

    #left wing
    glColor3ub(182,25,25)
    glBegin(GL_POLYGON)
    glVertex2f(-10, 30)
    glVertex2f(-60, 30)
    glVertex2f(-50, 10)
    glVertex2f(-10, 5)
    glEnd()

    # back right wing
    glColor3ub(182,25,25)
    glBegin(GL_POLYGON)
    glVertex2f(10, -30)
    glVertex2f(30, -35)
    glVertex2f(35, -50)
    glVertex2f(8.75, -45)
    glEnd()

    # left right wing
    glColor3ub(182,25,25)
    glBegin(GL_POLYGON)
    glVertex2f(-10, -30)
    glVertex2f(-30, -35)
    glVertex2f(-35, -50)
    glVertex2f(-8.75, -45)
    glEnd()
    glPopMatrix()

def landasan():
    glPushMatrix()
    glColor3ub(166, 166, 166)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0, 200)
    glVertex2f(1280, 200)
    glVertex2f(1280, 0)
    glEnd()
    glPopMatrix()

def baca_json():
    global detik

    try:
        with open ('waktuTerbaik.txt',mode='r') as f:
            line = int(f.readline())
            if detik//1000 > line:    #jika lebih besar dari sebelumnya isi dgn yg baru
                with open('waktuTerbaik.txt',mode='w') as f:
                    line = f.write(str(detik//1000))        
    except:
        with open('waktuTerbaik.txt',mode='w') as f:
            line = f.write(str(detik//1000))
            return 0
    return line
    
def papan_score():
    global detik, penambah_detik
    glPushMatrix()
    detik += penambah_detik
    glColor3ub(166, 166, 166) 
    glBegin(GL_QUADS)
    glVertex2f(800, 700) 
    glVertex2f(800, 600)  
    glVertex2f(1000, 600)
    glVertex2f(1000, 700)
    glEnd()
    glColor3ub(0,0,0)
    glRasterPos(920,660)
    for c in str(detik//1000):
        glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
    glRasterPos(830,660)
    for c in "TIMES :":
        glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
    
    glRasterPos(920,615)
    for c in str(baca_json()):
        glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
    glRasterPos(830,615)
    for c in "BEST :":
        glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
    
    glPopMatrix()

def playButton(button, state, x, y):
    global play, crash
    if button == GLUT_LEFT_BUTTON:
        if (x >= 300 and x <= 700) and (y >= 525 and y <= 625):
            play = True
        elif (x >= 300 and x <= 700) and (y >= 880 and y <= 925):
            play = False
            crash = False

def playGame():
    global xMeteorPos,yMeteorPos,xPosition,yPosition,crash
    glPushMatrix()
    papan_score()
    landasan()
    meteor()
    pesawat()
    #------------------------collision--------------------------#
    x_player_topLeft = xPosition -60
    x_player_topRight = xPosition +60

    xMeteorPos_bottomLeft = xMeteorPos  - 30
    xMeteorPos_bottomRight = xMeteorPos  + 30
    if  yPosition-20 <= yMeteorPos <= yPosition+20 :
        if x_player_topLeft < xMeteorPos_bottomLeft < x_player_topRight or\
            x_player_topLeft < xMeteorPos_bottomRight < x_player_topRight:
            print('Pesawat Menabrak Meteor')
            crash = True
            game_over()
            baca_json()
    #------------------------------------------------------------#
    glPopMatrix()

def game_over():
    global kecepatan_meteor, kecepatan_pesawat
    glPushMatrix()
    
    if crash == True:
        kecepatan_meteor = 0
        kecepatan_pesawat = 0
        glColor3b(36, 150, 127)
        glBegin(GL_QUADS)
        glVertex2f(300, 355)
        glVertex2f(300, 500)
        glVertex2f(700, 500)
        glVertex2f(700, 355)
        glEnd()
        glColor3ub(0,0,0)
        glLineWidth(10)
        glBegin(GL_LINE_LOOP)
        glVertex2f(300, 355)
        glVertex2f(300, 500)
        glVertex2f(700, 500)
        glVertex2f(700, 355)
        glEnd()
        drawTextBold(" G A M E   O V E R ",420,420)
    glPopMatrix()

kecepatan_pesawat = 15
def input_keyboard(key,x,y):
    global xPosition, yPosition
    if key == GLUT_KEY_DOWN:
        if yPosition > 10 : 
            yPosition -= kecepatan_pesawat
    elif key == GLUT_KEY_UP:
        if yPosition < 700 : 
            yPosition += kecepatan_pesawat
    elif key == GLUT_KEY_RIGHT:
        if xPosition < 950 : 
            xPosition += kecepatan_pesawat
    elif key == GLUT_KEY_LEFT:
        if xPosition > 50 : 
            xPosition -= kecepatan_pesawat

def timer(value):
        global x_time
        x_time -=1
        if x_time == -1400:
            x_time -= 0
            if x_time == -1400:
                x_time +=1400
        glutTimerFunc(2, timer, 0)

def update(value):
    if not crash : 
        glutPostRedisplay()
        glutTimerFunc(10,update,0)

def iterate():
    glViewport(0, 0, w, h)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClearColor(0, 0.7, 0.8, 0.3)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    iterate()
    if play == False:
        start_game()
    else:
        playGame()

    glutSwapBuffers()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(w, h)
    glutInitWindowPosition(250, 20)
    glutCreateWindow("GAME ZERO AEROSPACE 'Boeing777'")
    glutDisplayFunc(showScreen)
    glutMouseFunc(playButton)
    glutSpecialFunc(input_keyboard)
    glutTimerFunc(50, update, 0)
    timer(0)
    iterate()
    glutMainLoop()
    
if __name__ == "__main__":
    main()   