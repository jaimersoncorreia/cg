"""
	maneiras de  instanciar diicionário
		#1
		entidades = {
					'Instituicao':[]
					}
		#2
		entidades = dict(Instituicao=[])
"""
entidades = dict()
entidades['Empreendimento'] = "EntidadeEmpreedimento"
print(entidades)
del entidades['Empreendimento']

entidades['Empreendimento2'] = "EntidadeEmpreedimento2"

print(entidades['Empreendimento2'])

import os
print()
for meta_file in os.listdir('data/meta-data'):
	print(meta_file)

def nome(name_file):
	return name_file.split('.')[0]

print()
for meta_file in os.listdir('data/meta-data'):
	print(nome(meta_file))
