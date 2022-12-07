from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
# Koordinat x dan y untuk posisi kotak
pos_x = 0
pos_y = 0
pos_x2 = 150
pos_y2 = 150
# Warna Kotak
hijau = 1
biru = 1
merah = 1
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)

# Membuat bentuk kotak
def kotak():
    global pos_x, pos_y
    glColor3f(merah,hijau,biru)

    glBegin(GL_POLYGON)
    # Kiri Atas
    glVertex2f(-50 + pos_x,-50 + pos_y)
    # Kanan Atas
    glVertex2f(50 + pos_x,-50 + pos_y)
    # Kanan Bawah
    glVertex2f(50 + pos_x,50 + pos_y)
    # Kiri Bawah
    glVertex2f(-50 + pos_x,50 + pos_y)
    glEnd()

def kotak2():
    global pos_x, pos_y
    glColor3f(1,0,0)

    glBegin(GL_POLYGON)
    # Kiri Atas
    glVertex2f(-50 + pos_x2,-50 + pos_y2)
    # Kanan Atas
    glVertex2f(50 + pos_x2,-50 + pos_y2)
    # Kanan Bawah
    glVertex2f(50 + pos_x2,50 + pos_y2)
    # Kiri Bawah
    glVertex2f(-50 + pos_x2,50 + pos_y2)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,1.)
    glBegin(GL_LINES)
    glVertex2f(-500.0, 0.0)
    glVertex2f(500.0, 0.0)
    glVertex2f(0.0, 500.0)
    glVertex2f(0.0, -500.0)
    glEnd()
    glPushMatrix()
    kotak2()
    glPopMatrix()

    glPushMatrix()
    kotak()
    glPopMatrix()
    glFlush()

def cekcollision():
    if (pos_x2-50<= pos_x+50 <= pos_x2+50 or pos_x2-50<= pos_x-50 <= pos_x2+50) and (pos_y2-50<= pos_y+50 <= pos_y2+50 or pos_y2-50<= pos_y-50 <= pos_y2+50):
        print("Terjadi Collision")
    elif pos_y2-50<= pos_y+50 <= pos_y2+50 or pos_y2-50<= pos_y-50 <= pos_y2+50:
        print("Terjadi Overlap pada Sumbu Y")
    elif pos_x2-50<= pos_x+50 <= pos_x2+50 or pos_x2-50<= pos_x-50 <= pos_x2+50:
        print("Terjadi Overlap pada Sumbu X")

def input_keyboard(key,x,y):
    global pos_x, pos_y
# Untuk mengubah posisi kotak
    if key == GLUT_KEY_UP:
        pos_y += 5
        cekcollision()
    elif key == GLUT_KEY_DOWN:
        pos_y -= 5
        cekcollision()
    elif key == GLUT_KEY_RIGHT:
        pos_x += 5
        cekcollision()
    elif key == GLUT_KEY_LEFT:
        pos_x -= 5
    cekcollision()

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Collision Object")
    glutDisplayFunc(display)
    glutSpecialFunc(input_keyboard)
    glutTimerFunc(50, update, 0)

    init()
    glutMainLoop()

main()