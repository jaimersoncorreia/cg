from math import sin, cos, pi
from OpenGL.GL import *


def sol(c,pontos_circulo=3*81,raio = 0.3,center_x = 0.0,center_y = 0.0):
    vini = []
    vfim = []
    angulo = 0
    glBegin(GL_LINE_STRIP)
    glColor(1,1,0)
    for i in range(pontos_circulo):
        angulo = 2*pi*i/pontos_circulo

        if i%3==0:
            px = raio * cos(angulo) + center_x
            py = raio * sin(angulo) + center_y
            glVertex(2 * px, 2 * py, 0)
            if i == 0:
                vini = [2 * px, 2 *py]
            elif i == pontos_circulo - 1:
                vfim = [2 * px, 2 * py]
        else:
            px = raio * cos(angulo) + center_x
            py = raio * sin(angulo) + center_y
            glVertex(px, py, 0)
            if i == 0:
                vini = [px, py]
            elif i == pontos_circulo - 1:
                vfim = [px, py]
    glEnd()


    glBegin(GL_LINES)
    glColor(1,0,0)
    glVertex(vini[0], vini[1], 0)
    glVertex(vfim[0], vfim[1], 0)
    glEnd()

    #print(vini)
    #print(vfim)





def compor_sol(c):
    sol(c)
    #ini_fim(c)
