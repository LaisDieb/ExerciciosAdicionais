#Faça um algoritmo que receba os três lados de um triângulo e mostre sua classificação (escaleno, isósceles ou equilátero.
l1= float(input("Informe o primeiro lado do triângulo: "))
l2= float(input("Informe o segundo lado do triângulo: "))
l3= float(input("Informe o segundo lado do triângulo: "))

if l1==l2 and l2==l3:
    print("Triângulo equilátero, pois possui os três lados iguais.")
if (l1!=l2!=l3!=l1):
    print("Triângulo escaleno, pois possui os três lados diferentes.")
if ((l1==l2) and (l2!=l3)) or ((l2==l3) and (l3!=l1)) or ((l3==l1) and (l1!=l2)):
    print("Triângulo isósceles, pois possui dois lados iguais.")