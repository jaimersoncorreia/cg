from math import sin, cos, pi, sqrt
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
#   escala deve ocorrer
#
# - Salvar transformacao atual: glPushMatrix()
#
# - Recuperar ultima transformacao salva: glPopMatrix()


def compor_cena_ex0(c):
	
	glPushMatrix()
	glRotate(45,0,0,1)
	glTranslate(2, 2, 0)
	c.draw("TG1")
	glPopMatrix()
	
	glPushMatrix()
	glRotate(3*45,0,0,1)
	glTranslate(2,2,0)
	c.draw("TG2")
	glPopMatrix()

	glPushMatrix()
	glTranslate(2*cos(-45*pi/180),2*sin(-45*pi/180),0)
	glRotate(45,0,0,1)
	c.draw("TM")
	glPopMatrix()

	glPushMatrix()
	glTranslate(sqrt(2),0,0)
	glRotate(45,0,0,1)
	c.draw("Q")
	glPopMatrix()
	
	glPushMatrix()
	glTranslate(2*cos(-135*pi/180),2*sin(-135*pi/180),0)
	glTranslate(cos(-45*pi/180),sin(-45*pi/180),0)
	glRotate(3*45,0,0,1)
	c.draw("P")
	glPopMatrix()

	glPushMatrix()
	glRotate(-135,0,0,1)
	glTranslate(1,1,0)
	c.draw("TP1")
	glPopMatrix()
	
	glPushMatrix()
	glTranslate(2*cos(45*pi/180),2*sin(45*pi/180),0)
	glRotate(-45,0,0,1)
	glTranslate(1,1,0)
	c.draw("TP2")
	glPopMatrix()

def compor_cena_ex1(c):
	glPushMatrix()
	glTranslate(-2,2,0)
	c.draw("TG1")
	glPopMatrix()
	
	glPushMatrix()
	#glTranslate(-2*sqrt(2),0,0)
	#glRotate(45,0,0,1)
	glTranslate(4*cos(-135*pi/180),4*sin(-135*pi/180),0)
	glRotate(45,0,0,1)
	glTranslate(2,2,0)
	c.draw("TG2")
	glPopMatrix()

	glPushMatrix()
	glTranslate(2*cos(-135*pi/180),2*sin(-135*pi/180),0)
	glRotate(45,0,0,1)
	c.draw("TM")
	glPopMatrix()
	
	glPushMatrix()
	glTranslate(1,1,0)
	c.draw("Q")
	glPopMatrix()

	glPushMatrix()
	glTranslate(2,3,0)
	glScale(-1,1,1)
	glRotate(-90,0,0,1)
	c.draw("P")
	glPopMatrix()


	glPushMatrix()
	glTranslate(4,4,0)
	glRotate(-45,0,0,1)
	glTranslate(1,-1,0)
	c.draw("TP1")
	glPopMatrix()

	glPushMatrix()
	glRotate(-90,0,0,1)
	glTranslate(1,1,0)
	c.draw("TP2")
	glPopMatrix()

def compor_cena_ex2(c):
	glPushMatrix()
	glTranslate(-1,2*sqrt(2),0)
	glRotate(-135,0,0,1)
	glTranslate(2,2,0)
	c.draw("TG1")
	glPopMatrix()

	glPushMatrix()
	glRotate(-135,0,0,1)
	glTranslate(2,2,0)
	c.draw("TG2")
	glPopMatrix()
	'''
    c.draw("TM")
    c.draw("Q")
    c.draw("P")
    c.draw("TP1")
    c.draw("TP2")
	'''

def compor_cena_ex3(c):
    c.draw("TG1")
    c.draw("TG2")
    c.draw("TM")
    c.draw("Q")
    c.draw("P")
    c.draw("TP1")
    c.draw("TP2")


def compor_cena_ex4(c):
    c.draw("TG1")
    c.draw("TG2")
    c.draw("TM")
    c.draw("Q")
    c.draw("P")
    c.draw("TP1")
    c.draw("TP2")


def compor_cena_ex5(c):
    c.draw("TG1")
    c.draw("TG2")
    c.draw("TM")
    c.draw("Q")
    c.draw("P")
    c.draw("TP1")
    c.draw("TP2")


def compor_cena_ex6(c):
    c.draw("TG1")
    c.draw("TG2")
    c.draw("TM")
    c.draw("Q")
    c.draw("P")
    c.draw("TP1")
    c.draw("TP2")


def compor_cena_ex7(c):
    c.draw("TG1")
    c.draw("TG2")
    c.draw("TM")
    c.draw("Q")
    c.draw("P")
    c.draw("TP1")
    c.draw("TP2")


def compor_cena_ex8(c):
    c.draw("TG1")
    c.draw("TG2")
    c.draw("TM")
    c.draw("Q")
    c.draw("P")
    c.draw("TP1")
    c.draw("TP2")
