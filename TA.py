import OpenGL.GLUT as glut
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import os
import random as rd

w,h =1000,750
x_time = 0 
y_time = 0 
angle_time = 0 
pos_x = 0
pos_y= 0
pos_x_pemain = 0
pos_y_pemain = 0
gerak = 0

x_meteor1=750
y_meteor1=100
x_meteor2=750
y_meteor2=450
x_meteor3=750
y_meteor3=800

x_pesawat=0
y_pesawat=0
game_over = False

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

def bg_text(x,y):
    glColor3ub(255, 0, 0)     
    glBegin(GL_QUADS)
    glVertex2f(295+x,210+y)
    glVertex2f(445+x,210+y)
    glVertex2f(445+x,260+y)
    glVertex2f(295+x,260+y)
    glEnd()

def efek_turun():
    global gerak
    if gerak <= -1500:
        gerak = 0
    else:
        gerak -= 0.5
    print(gerak)
    return gerak

def meteor1():
    # global gerak
    # efek_turun()
    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(150, 700+gerak)
    glVertex2f(182, 678+gerak)
    glVertex2f(200, 650+gerak)
    glVertex2f(180, 620+gerak)
    glVertex2f(150, 600+gerak)
    glVertex2f(120, 620+gerak)
    glVertex2f(100, 650+gerak)
    glVertex2f(120, 680+gerak)
    glEnd()

def meteor2():
    # global gerak
    # efek_turun()
    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(500, 700+gerak)
    glVertex2f(530, 680+gerak)
    glVertex2f(550, 650+gerak)
    glVertex2f(530, 620+gerak)
    glVertex2f(500, 600+gerak)
    glVertex2f(470, 620+gerak)
    glVertex2f(450, 650+gerak)
    glVertex2f(470, 680+gerak)
    glEnd()

def meteor3():
    # global gerak
    # efek_turun()
    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(850, 700+gerak)
    glVertex2f(880, 680+gerak)
    glVertex2f(900, 650+gerak)
    glVertex2f(880, 620+gerak)
    glVertex2f(850, 600+gerak)
    glVertex2f(820, 620+gerak)
    glVertex2f(800, 650+gerak)
    glVertex2f(820, 680+gerak)
    glEnd()

def pesawat():
    # glPushMatrix()
    # global pos_x_pemain, pos_y_pemain, gerak, game_over
    # if pos_x_pemain >= 440:
    #     pos_x_pemain = 440
    # if pos_x_pemain <=-480:
    #     pos_x_pemain = -480
    # if pos_y_pemain >= 400:
    #     pos_y_pemain = 400
    # if pos_y_pemain <= 0:
    #     pos_y_pemain = 0

    # if pos_x_pemain in range(x_meteor1 - 8, x_meteor1 + 200) and pos_y_pemain in range(y_meteor1 - 40, y_meteor1 + 60):
    #     pos_x_pemain = 0
    #     pos_y_pemain = 0
    #     game_over = True

    # if pos_x_pemain in range(x_meteor2 - 8, x_meteor2 + 200) and pos_y_pemain in range(y_meteor2 - 40, y_meteor2 + 60):
    #     pos_x_pemain = 0
    #     pos_y_pemain = 0
    #     game_over = True

    # if pos_x_pemain in range(x_meteor3 - 0, x_meteor3 + 200) and pos_y_pemain in range(y_meteor3 - 40, y_meteor3 + 65):
    #     pos_x_pemain = 0
    #     pos_y_pemain = 0
    #     game_over = True
    # print("pos pemain: ",pos_x_pemain, pos_y_pemain)

    #badan
    glTranslated(x_pesawat + gerak, y_pesawat + gerak,0)
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(500, 170)
    glVertex2f(512, 160)
    glVertex2f(517, 150)
    glVertex2f(520,140)
    glVertex2f(520,120)
    glVertex2f(520,80)
    glVertex2f(517.2854179081743,68.1157751633107)
    glVertex2f(512.3597885653206,60.10339418436206)
    glVertex2f(500,40)
    glVertex2f(500.0414598267785,90.2434770334071)
    glVertex2f(477.6589898385615,59.3641611084844)
    glVertex2f(477.5909998541945,71.5842194592896)
    glVertex2f(480,80)
    glVertex2f(480,120)
    glVertex2f(480,140)
    glVertex2f(483.5, 150)
    glVertex2f(488, 160)
    glEnd()

    #kepala
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(500, 166)
    glVertex2f(502, 160)
    glVertex2f(506, 150)
    glVertex2f(508, 140)
    glVertex2f(510, 130)
    glVertex2f(490, 130)
    glVertex2f(492, 140)
    glVertex2f(494, 150)
    glVertex2f(498, 160)
    glEnd()

    #sayap belakang atas
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(500.0414598267785,90.2434770334071)
    glVertex2f(477.6589898385615,59.3641611084844)
    glVertex2f(472.3374871735562,52.0214995225147)
    glVertex2f(460,35)
    glVertex2f(460,25)
    glVertex2f(470,20)
    glVertex2f(500,40)
    glEnd()

    #sayap kanan atas
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(520,140)
    glVertex2f(540, 132)
    glVertex2f(560.4, 128)
    glVertex2f(580, 124)
    glVertex2f(584, 110)
    glVertex2f(560.4, 111.6)
    glVertex2f(540, 115.5)
    glVertex2f(520,120)
    glEnd()

    #sayap kiri atas
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(480,140)
    glVertex2f(460, 132)
    glVertex2f(440, 128)
    glVertex2f(420, 124)
    glVertex2f(416, 110)
    glVertex2f(440, 111.6)
    glVertex2f(460, 115.5)
    glVertex2f(480, 120)
    glEnd()

    #sayap kiri bawah
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(480,80)
    glVertex2f(460.7036100049402, 67.1596824220173)
    glVertex2f(440, 60)
    glVertex2f(441.7376000257295, 47.6475735965235)
    glVertex2f(456.3908454635123, 46.0815779008825)
    glVertex2f(472.3374871735362,52.0214995225148)
    glVertex2f(477.6589898385615, 59.3641611084844)
    glVertex2f(477.5909998541945, 71.5842194592896)
    glEnd()

    #sayap kanan bawah
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(520, 80)
    glVertex2f(540.3953288511068, 66.2158082734088)
    glVertex2f(560, 60)
    glVertex2f(557.9568520093655, 47.8712872673293)
    glVertex2f(543.9747475840003, 46.3052915716884)
    glVertex2f(527.4859562208875, 52.2434051031018)
    glVertex2f(512.3597885653206,60.10339418436206)
    glEnd()

def jalan():
    glColor3ub(219, 219, 219)
    glBegin(GL_QUADS)
    glVertex2f(50, 0)
    glVertex2f(50, 750)
    glVertex2f(250, 750)
    glVertex2f(250, 0)
    glEnd()

def jalan1():
    glColor3ub(219, 219, 219)
    glBegin(GL_QUADS)
    glVertex2f(400, 0)
    glVertex2f(400, 750)
    glVertex2f(600, 750)
    glVertex2f(600, 0)
    glEnd()

def jalan2():
    glColor3ub(219, 219, 219)
    glBegin(GL_QUADS)
    glVertex2f(750, 0)
    glVertex2f(750, 750)
    glVertex2f(950, 750)
    glVertex2f(950, 0)
    glEnd()

def landasan():
    glColor3ub(166, 166, 166)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0, 200)
    glVertex2f(1000, 200)
    glVertex2f(1000, 0)
    glEnd()

def nyawa():
    #kerangka nyawa
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(880, 70)
    glVertex2f(990, 70)
    glVertex2f(990, 10)
    glVertex2f(880, 10)
    glEnd()

    #nyawa 1
    glColor3ub(255, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(889, 60)
    glVertex2f(900, 60)
    glVertex2f(900, 20)
    glVertex2f(889, 20)
    glEnd()

    #nyawa 2
    glColor3ub(255, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(909, 60)
    glVertex2f(920, 60)
    glVertex2f(920, 20)
    glVertex2f(909, 20)
    glEnd()

    #nyawa 3
    glColor3ub(255, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(930, 60)
    glVertex2f(940, 60)
    glVertex2f(940, 20)
    glVertex2f(930, 20)
    glEnd()

    #nyawa 4
    glColor3ub(255, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(950, 60)
    glVertex2f(960, 60)
    glVertex2f(960, 20)
    glVertex2f(950, 20)
    glEnd()

    #nyawa 5
    glColor3ub(255, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(970, 60)
    glVertex2f(980, 60)
    glVertex2f(980, 20)
    glVertex2f(970, 20)
    glEnd()

def input_mouse(button, state, x, y):
    global hijau, kuning, merah
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        if merah< 1:
            hijau = 0
            kuning = 1
            merah = 0
        else:
            hijau = 0
            kuning = 0
            merah = 1
            print("Klik kanan ditekan ", "(", x, ",", y, ")")

    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if hijau < 1:
            hijau = 1
            kuning = 0
            merah = 0
        elif merah < 1:
            hijau = 0
            kuning = 0
            merah = 0
            print("Klik Kiri ditekan ", "(", x, ",", y, ")")

def input_keyboard(key,x,y):
    global pos_x_pemain, pos_y_pemain, gerak
    gerak = 10
    if key == GLUT_KEY_UP:
        pos_y_pemain += gerak
        print("Tombol Atas ditekan ", "x : ", pos_x, " y : ", pos_y)
    elif key == GLUT_KEY_DOWN:
        pos_y_pemain -= gerak
        print("Tombol Bawah ditekan ", "x : ", pos_x, " y : ", pos_y)
    elif key == GLUT_KEY_RIGHT:
        pos_x_pemain += gerak
        print("Tombol Kanan ditekan ", "x : ", pos_x, " y : ", pos_y)
    elif key == GLUT_KEY_LEFT:
        pos_x_pemain -= gerak
        print("Tombol Kiri ditekan ", "x : ", pos_x, " y : ", pos_y)

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

def iterate():
    glViewport(0, 0, w, h)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, w, 0.0, h)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT)
    iterate()
    jalan()
    jalan1()
    jalan2()
    landasan()
    pesawat()
    meteor1()
    meteor2()
    meteor3()
    nyawa()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(w, h)
    glutInitWindowPosition(250,20)
    glutCreateWindow("GAME")
    glutDisplayFunc(showScreen)
    glutMouseFunc(input_mouse)
    glutSpecialFunc(input_keyboard)
    glutTimerFunc(50, update, 0)
    timer(0)
    iterate()
    glutMainLoop()
    
if __name__ == "__main__":
    main()    