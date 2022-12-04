import OpenGL.GLUT as glut
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import os
import json
import random
import random as rd

play = False
w,h = 1000,720
x_time = 0 
y_time = 0 
angle_time = 0 
pos_x = 0
pos_y= 0
pos_x_pemain = 0
pos_y_pemain = 0
score_pemain = 0
x_gerak = 500
y_gerak = 100
y_rintangan=50
detik = 1
penambah_detik = 600//60

border_x = 1000
border_y = 750
pos_x_meteor = 0
pos_y_meteor = border_y
kecepatan_meteor = 10

selesai=False

x_r_player = random.randrange(300,550,10)
x_pesawat=10
y_pesawat=10
game_over = False
jumlah_bintang = 1000
jumlah_meteor=3

def drawText(ch,xpos,ypos,r,b,g):
    glPushMatrix()
    color = (r, b, g)
    font_style = glut.GLUT_BITMAP_HELVETICA_18
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))  
    glPopMatrix()  

def drawTextBold(ch,xpos,ypos):
    glPushMatrix()
    color = (0,0,0)
    font_style = glut.GLUT_BITMAP_HELVETICA_18
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+5
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))  
    glPopMatrix()  

def drawTextNum(skor,xpos,ypos,r,b,g):
    color = (r, b, g)
    font_style = glut.GLUT_BITMAP_8_BY_13
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in str(skor):
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))

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

def bg_text(x,y):
    glColor3ub(255, 0, 0)     
    glBegin(GL_QUADS)
    glVertex2f(295+x,210+y)
    glVertex2f(445+x,210+y)
    glVertex2f(445+x,260+y)
    glVertex2f(295+x,260+y)
    glEnd()

def bintang():
    glPushMatrix()
    glPointSize(3)
    glRotated(180,0,0,0)
    glColor3f(1.0, 1.0, 1.0) #RGB
    glBegin(GL_POINTS)
    y = 1000
    for i in range(jumlah_bintang):
        x = rd.randrange(-2000,2000)
        glVertex2f(x,y)
        if y != 1000:
            x = x
        y -= 100
    glEnd()
    glPopMatrix()

def meteor():
    global y_rintangan, x_r_player, pos_x_pemain, pos_y_pemain, border_x, pos_x_meteor, pos_y_meteor
    glPushMatrix()
    glScaled(0.5,0.5,0)
    glTranslated(500, 0, 0)
    pos_y_meteor-=kecepatan_meteor
    if pos_y_meteor < -border_y:
        pos_y_meteor = border_y
        pos_x_meteor = rd.randrange(pos_x_pemain-345, pos_x_pemain+200)

    glTranslated(pos_x_meteor, pos_y_meteor,0)
    glColor3ub(92, 47, 16)
    glBegin(GL_POLYGON)
    glVertex2f(500, 700)
    glVertex2f(530, 680)
    glVertex2f(550, 650)
    glVertex2f(530, 620)
    glVertex2f(500, 600)
    glVertex2f(470, 620)
    glVertex2f(450, 650)
    glVertex2f(470, 680)
    glEnd()
    glPopMatrix()    

def pesawat():
    global x_gerak, y_gerak, pos_x_pemain, pos_y_pemain, selesai, border_x, border_y
    glPushMatrix()
    # if not selesai:
    #     if pos_x_pemain > border_x+1000:
    #         pos_x_pemain = border_x+1000
    #     if pos_x_pemain < -border_x:
    #         pos_x_pemain = -border_x

    #     if pos_y_pemain > border_y-750:
    #         pos_y_pemain = border_y-750
    #     if pos_y_pemain < -border_y:
    #         pos_y_pemain = -border_y

    glTranslated(x_gerak, y_gerak, 0)
    # glTranslated(500, 100, 0)
    glScaled(0.5,0.5,0)

    #body
    glColor3ub(240, 60, 60)
    glBegin(GL_POLYGON)
    glVertex2f(0, 140)
    glVertex2f(10, 135)
    glVertex2f(15, 130)
    glVertex2f(20, 120)
    glVertex2f(20, 100)
    glVertex2f(20, 10)
    glVertex2f(20, -50)
    glVertex2f(0, -130)
    glVertex2f(-20,- 50)
    glVertex2f(-20, 50)
    glVertex2f(-20, 120)
    glVertex2f(-15, 130)
    glVertex2f(-10, 135)
    glVertex2f(0, 140)
    glEnd()

    # glass
    glColor3ub(188,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(-15, 120)
    glVertex2f(-15, 100)
    glVertex2f(15, 100)
    glVertex2f(15, 120)
    glVertex2f(10, 125)
    glVertex2f(5, 130)
    glVertex2f(0, 132)
    glVertex2f(-5, 130)
    glVertex2f(-10, 125)
    glVertex2f(-15, 120)
    glEnd()

    #right wing
    glColor3ub(182,25,25)
    glBegin(GL_POLYGON)
    glVertex2f(20, 65)
    glVertex2f(150, 60)
    glVertex2f(130, 30)
    glVertex2f(20, 20)
    glEnd()

    #left wing
    glColor3ub(182,25,25)
    glBegin(GL_POLYGON)
    glVertex2f(-20, 65)
    glVertex2f(-150, 60)
    glVertex2f(-130, 30)
    glVertex2f(-20, 20)
    glEnd()

    # back right wing
    glColor3ub(182,25,25)
    glBegin(GL_POLYGON)
    glVertex2f(16, -60)
    glVertex2f(70, -70)
    glVertex2f(80, -90)
    glVertex2f(10, -85)
    glEnd()

    # left right wing
    glColor3ub(182,25,25)
    glBegin(GL_POLYGON)
    glVertex2f(-16, -60)
    glVertex2f(-70, -70)
    glVertex2f(-80, -90)
    glVertex2f(-10, -85)
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

def tulis_json(value):
    penampung = [{'waktu':str(value)}]
    with open('waktuTerbaik.json','w') as berkas:
        json.dump(penampung, berkas, indent = 4)

def baca_json():
    penampung = [] 
    try:
        with open ('waktuTerbaik.json','r') as berkas:
                data = json.load(berkas)
                for i in data:
                    penampung.append(i)

    except:
        penampung = [{'waktu':'9999'}]
        with open('waktuTerbaik.json','w') as berkas:
            json.dump(penampung, berkas, indent = 4)

    waktu = int(penampung[0]['waktu'])
    return waktu
    
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
    for c in "TIME :":
        glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
    
    glRasterPos(920,615)
    for c in str(baca_json()):
        glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
    glRasterPos(830,615)
    for c in "BEST :":
        glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
    
    glPopMatrix()    

def mouse_play_game(button, state, x, y):
    global play
    if button == GLUT_LEFT_BUTTON:
        play = True

def input_keyboard(key,x,y):
    global x_gerak, y_gerak
    if key == GLUT_KEY_DOWN:
        if y_gerak == 0 : 
            y_gerak -= 0
        else :
            y_gerak -= 15
        # print("Tombol Atas ditekan ", "x : ", pos_x, " y : ", pos_y)
    elif key == GLUT_KEY_UP:
        if y_gerak == 950 : 
            y_gerak += 0
        else :
            y_gerak += 15
        # print("Tombol Bawah ditekan ", "x : ", pos_x, " y : ", pos_y)
    elif key == GLUT_KEY_RIGHT:
        if x_gerak == 950 : 
            x_gerak += 0
        else :
            x_gerak += 15
        # print("Tombol Kanan ditekan ", "x : ", pos_x, " y : ", pos_y)
    elif key == GLUT_KEY_LEFT:
        if x_gerak == -400 : 
            x_gerak -= 0
        else :
            x_gerak -= 15
        # print("Tombol Kiri ditekan ", "x : ", pos_x, " y : ", pos_y)

def timer(value):
    global x_time
    x_time -=1
    if x_time == -1400:
        x_time -= 0
        if x_time == -1400:
            x_time +=1400
    glutTimerFunc(2, timer, 0)

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

# def collision():
#     global pos_x_pemain, pos_y_pemain, pos_x_meteor, pos_y_meteor, start_game
#     if pos_x_pemain -500>= pos_x_meteor:
#         if pos_y_pemain -30 >= pos_y_meteor or pos_y_pemain +10 >=pos_y_meteor:
#             pos_x_pemain = 0
#             pos_y_meteor = random.randint(-100,500)
#     if pos_x_pemain -100>= pos_x_meteor:
#         if pos_y_pemain -30 >= pos_y_meteor or pos_y_pemain +10 >=pos_y_meteor:
#             pos_x_pemain = 0
#             pos_y_meteor = random.randint(-100,500)      
#     if pos_x_pemain >= 1000:
#         start_game = False      

def iterate():
    glViewport(0, 0, w, h)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def playGame():
    glPushMatrix()
    papan_score()
    landasan()
    bintang()
    meteor()
    pesawat()
    # collision()

    # if game_over==False:
    #     papan_score()
    #     meteor(x_r_player)

    if game_over==True:
        # bg_text(-40,0)
        glRasterPos(420,420)
        for c in "GAME OVER":
            glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
    glPopMatrix()

def showScreen():
    glClearColor(0, 0.7, 0.8, 0.3)
    glClear(GL_COLOR_BUFFER_BIT)
    iterate()
    bintang()
    if play == False:
        start_game()
    else:
        playGame()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(w, h)
    glutInitWindowPosition(250, 20)
    glutCreateWindow("GAME ZERO AEROSPACE")
    glutDisplayFunc(showScreen)
    glutMouseFunc(mouse_play_game)
    glutSpecialFunc(input_keyboard)
    glutTimerFunc(50, update, 0)
    timer(0)
    iterate()
    glutMainLoop()
    
if __name__ == "__main__":
    main()    