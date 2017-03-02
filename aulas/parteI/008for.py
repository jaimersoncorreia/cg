impostos = ['MEI','Simples']

for imposto in impostos:
    if imposto.startswith("S"):
        continue

    print(imposto)

lista = [0,1,2,3,4,5,6,7,8,9]

for i in lista:
    print(i)

for j in range(10):
    print(j)

for i, imposto in enumerate(impostos):
    print(i,imposto)

for i,letras in enumerate("Jaimerson"):
    print(i+1,letras)

for enume in enumerate("Sofia"):
    print(enume)


