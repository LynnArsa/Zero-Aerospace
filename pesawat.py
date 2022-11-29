import OpenGL.GLUT as glut
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import os
import random
import random as rd

def pesawat():
    #body
    glColor3ub(135,206,235)
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

    #right wing
    glColor3ub(135,206,235)
    glBegin(GL_POLYGON)
    glVertex2f(20, 65)
    glVertex2f(150, 60)
    glVertex2f(130, 30)
    glVertex2f(20, 20)
    glEnd()

    #left wing
    glColor3ub(135,206,235)
    glBegin(GL_POLYGON)
    glVertex2f(-20, 65)
    glVertex2f(-150, 60)
    glVertex2f(-130, 30)
    glVertex2f(-20, 20)
    glEnd()

    # back right wing
    glColor3ub(135,206,235)
    glBegin(GL_POLYGON)
    glVertex2f(16, -60)
    glVertex2f(70, -70)
    glVertex2f(80, -90)
    glVertex2f(10, -85)
    glEnd()

    # left right wing
    glColor3ub(135,206,235)
    glBegin(GL_POLYGON)
    glVertex2f(-16, -60)
    glVertex2f(-70, -70)
    glVertex2f(-80, -90)
    glVertex2f(-10, -85)
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
    glColor3f(1.0, 0.0, 2.0)
    pesawat()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("Mitsubishi")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()