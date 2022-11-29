from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 1000,1000
def square():
    glBegin(GL_POLYGON)
    glTranslated(1000, 0, 0)
    glRotated(0.5,0.5,0)
    glScaled(90,0,0,1)
    glColor(255, 0, 0)

    glVertex2f(00, 00)
    glVertex2f(250, 500)
    glVertex2f(250, 500)
    glVertex2f(00, 1000)
    glVertex2f(00, 1000)
    glVertex2f(-250, 500)
    glVertex2f(-250, 500)
    glVertex2f(0, 0)

    glVertex2f(0, 0)
    glVertex2f(500, 0)
    glVertex2f(500, 0)
    glVertex2f(750, -500)
    glVertex2f(750, -500)
    glVertex2f(250, -500)
    glVertex2f(250, -500)
    glVertex2f(0, 0)

    glVertex2f(0, 0)
    glVertex2f(-500, 0)
    glVertex2f(-500, 0)
    glVertex2f(-750, -500)
    glVertex2f(-750, -500)
    glVertex2f(-250, -500)
    glVertex2f(-250, -500)
    glVertex2f(0, 0)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1000, 1000, -1000, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    square()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("Mitsubishi")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()