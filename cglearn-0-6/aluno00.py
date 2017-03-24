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
def jcor(r, g, b):
    return {r/255, g/255, b/255}

def sol(c,pontos_circulo=3,raio = 0.1,center_x = 0.0,center_y = 2.0):
    angulo = 0
    glBegin(GL_TRIANGLES)
    glColor(1,1,0)
    for i in range(pontos_circulo):
        angulo = 2*pi*i/pontos_circulo
        px = raio*cos(angulo) + center_x
        py = raio*sin(angulo) + center_y
        glVertex(px, py,0)

    glEnd()

def circulo(c,pontos_circulo=50,raio = 0.1,center_x = 0.0,center_y = 0.6):
    angulo = 0
    glBegin(GL_TRIANGLE_FAN)
    glColor(1,1,0)
    for i in range(pontos_circulo):

        angulo = 2*pi*i/pontos_circulo
        px = raio*cos(angulo) + center_x
        py = raio*sin(angulo) + center_y
        glVertex(px, py,0)

    glEnd()

def telhado(c):
    glBegin(GL_TRIANGLES)
    glColor(*jcor(210,105,30))
    glVertex(0, 0.5, 0)
    glVertex(1.25, 0, 0)
    glVertex(-1.25, 0, 0)

    glEnd()

def parede(c):
    glBegin(GL_QUADS)
    glColor(*jcor(235, 199, 158))
    glVertex(-1,0,0)
    glVertex(1, 0, 0)
    glVertex(1, -1, 0)
    glVertex(-1, -1, 0)
    glEnd()

def porta(c):
    glBegin(GL_QUADS)
    #glColor(0.25, 0.7, 1.0)
    glColor(*jcor(217, 135, 25))
    glVertex(0.25,-0.1,0)
    glVertex(0.75, -0.1, 0)
    glVertex(0.75, -1.0, 0)
    glVertex(0.25, -1.0, 0)    
    glEnd()

def janela(c):
    glBegin(GL_QUADS)
    glVertex(-0.15, -0.1, 0)
    glVertex(-0.85, -0.1, 0)
    glVertex(-0.85, -0.6, 0)
    glVertex(-0.15, -0.6, 0)
    glEnd()

def compor_casa(c):
    telhado(c)
    parede(c)
    porta(c)
    janela(c)
    circulo(c)
    sol(c)

    
