salario = int(input('Salário? '))
imposto = input('Imposto em % (Ex.: 27.5)? ')

if not imposto:
    imposto = 27.5
else:
    imposto = float(imposto)


print("Valor real: {0}".format(salario-(salario*imposto*0.01)))

print("Imposto Alto" if imposto*0.01 > 0.27 else "Imposto Baixo")

print(imposto)
