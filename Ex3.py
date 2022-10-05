#Receber dois números e mostrar o maior.
n1= int(input("Informe o primeiro número: "))
n2= int(input("Informe o segundo número: "))

if n1>n2:
    print("O primeiro número, {}, é maior que o segundo, {}.". format(n1,n2))
if n2>n1:
    print("O segundo número, {}, é maior que o primeiro, {}.".format(n2,n1))
else:
    print("Os números digitados são iguais.")