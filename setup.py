"""
========================================
Teste de python 3.5.3
========================================.
"""
import sys

param = sys.argv[1:]

if 0 == len(param):
    print("--help   para mais informações")
elif "Sofia" == param[0]:
    print("Mãe: Gabriela Bastão")
    print("Pai: Jaimerson Correia")
elif "--help" == param[0]:
    print("Sofia")
else:
    print("Pais não cadastrado")



