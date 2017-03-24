from math import sin, cos, pi
from OpenGL.GL import *

# Aqui voce deve definir o corpo desta funcao de modo a incluir as
# transofmacoes, repeticoes, condicionais, etc. necessarias para concluir
# os exercicios.
#
# Pequena referencia rapida das funcoes mais usadas:
#
# - Translacao: glTranslate(dx, dy, dz)
#
# - Rotacao: glRotate(angle, axis_x, axis_y, axis_z)
#
# - Escala: glScale(sx, sy, sz)
#
# - Espelhamento: Usar escala com fator de -1.0 no eixo em relacao ao qual a
#   escala deve ocorrer.


def compor_cena(c):

    glBegin(GL_QUADS)

    glColor(0.3, 0.7, 1.0)
    glVertex(-0.5, -0.5, 0.1)
    glVertex(-0.5, 0.5, 0.1)
    glVertex(0.5, 0.5, 0.1)
    glVertex(0.5, -0.5, 0.1)

    glEnd()

def compor_cena2(c):
    glBegin(GL_TRIANGLES)


    glVertex(0.5, 0, 0)
    glVertex(0, 0.5, 0)
    glVertex(-0.5, -0.5, 0)

    glEnd()

def compor_casa(c):
    glBegin(GL_LINE_LOOP)

    glVertex(0, 0.5, 0)
    glVertex(1.25, 0, 0)
    glVertex(-1.25, 0, 0)

    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex(-1,0,0)
    glVertex(1, 0, 0)
    glVertex(1, -1, 0)
    glVertex(-1, -1, 0)
    glEnd()

    glBegin(GL_LINES)
    #glColor(0.25, 0.7, 1.0)
    glColor(255, 0, 0)

    glVertex(0.25,-0.1,0)
    glVertex(0.75, -0.1, 0)

    glVertex(0.75, -0.1, 0)
    glVertex(0.75, -1, 0)

    glVertex(0.25, -0.1, 0)
    glVertex(0.25, -1, 0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex(-0.15, -0.1, 0)
    glVertex(-0.85, -0.1, 0)
    glVertex(-0.85, -0.6, 0)
    glVertex(-0.15, -0.6, 0)
    glEnd()
