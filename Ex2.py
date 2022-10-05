#Faça um programa que receba três notas de um aluno, calcule e mostre a média aritmética e a mensagem:
# entre 0 e 3, reprovado;entre 3 e 7, recuperação; acima de 7, aprovado.Aos alunos que ficaram para exame,
# calcule e mostre a nota que deverão tirar para serem aprovados, considerando que a média exigida é 6.
n1= float(input("Nota 1: "))
n2= float(input("Nota 2: "))
n3= float(input("Nota 3: "))
media= (n1+n2+n3)/3
nf=12-media

if (media>=0) and (media<3):
    print("Reprovado")
if (media>=3) and (media<7):
    print("Exame. Você precisa tirar pelo menos {} na nota final.".format(nf))
else:
    print("Aprovado")