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

'''
transform-1.json
def compor_cena(c):
	glTranslate(3, 0, 0)
	c.draw()
'''
#transform-2.json
#def compor_cena(c):
#	glScale(3,3,1)
#	c.draw()

#transform-3.json
#def compor_cena(c):
#	glScale(0.5,2,1)
#	c.draw()

#transform-4.json
#def compor_cena(c):
#	glTranslate(2,0,0)
#	glScale(0.5,0.5,1)
#	c.draw()

#transform-5.json
#def compor_cena(c):
#	glTranslate(3,0,0)
#	glRotate(60,0,0,1)
#	c.draw()

#transform-6.json
#def compor_cena(c):
#	glRotate(60,0,0,1)
#	glTranslate(3,0,0)
#	c.draw()

#transform-7.json
#def compor_cena(c):
#	glRotate(60,0,0,1)	#3
#	glTranslate(3,0,0)	#2
#	glRotate(-60,0,0,1)	#1
#	c.draw()

#transform-7.json
def compor_cena(c):
	glRotate(60,0,0,1)	#3
	glTranslate(3,0,0)	#2
	glRotate(-30,0,0,1)	#1
	c.draw()

def processar_teclado():
    pass
