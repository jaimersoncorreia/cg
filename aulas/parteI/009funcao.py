"""
    Autor:	Jaimerson Correia
    Descrição:Como é definido uma função em python
"""


def salario_descontado_imposto(salario, imposto=27.):
    return salario - (salario * imposto * 0.01)


print("Salário com imposto descontado: {0}".format(salario_descontado_imposto(5000)))
print("Salário com imposto descontado: {0}".format(salario_descontado_imposto(5000, 50.)))
