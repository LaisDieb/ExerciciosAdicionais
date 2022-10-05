#Faça um algoritmo que recebe duas notas, calcule a média aritmética e mostre mensagem de
# Aprovado ou Reprovado, considerando para aprovação média de, no mínimo, 7.
n1= float(input("Nota 1: "))
n2= float(input("Nota 2: "))
media= (n1+n2)/2

if (media>=7):
    print("Aprovado.")
else:
    print("Reprovado.")