imposto = float(input("Imposto: "))
if imposto < 10.:
	print("Imposto Baixo")
elif imposto >= 10. and imposto <= 27.:
	print("Imposto Médio")
elif imposto > 27. and imposto < 100:
	print("Imposto Alto")
else:
	print("Imposto Inválido")
