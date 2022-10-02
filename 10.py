'''
10. Escreva um algoritmo que leia o código de um aluno e suas três notas. 
Calcule a média ponderada do aluno, considerando que o peso para a maior nota seja 4 e para as
duas restantes, 3. Mostre o código do aluno, suas três notas, 
a média calculada e uma mensagem "APROVADO" se a média for maior ou igual a 5 e "REPROVADO" se a
média for menor que 5. Repita a operação até que o código lido seja negativo.
'''

cod=int(input("Insira o codigo do aluno: "))
while (cod>=0):
    av1=float(input("Insira a nota 1: "))
    av2=float(input("Insira a nota 2: "))
    av3=float(input("Insira a nota 3: "))

    if (av1>=av2 and av1>=av3):
        media=((av1*4)+(av2*3)+(av3*3))/10
    elif (av2>av1 and av2>av3):
        media=((av2*4)+(av1*3)+(av3*3))/10
    elif (av3>av2 and av3>av1):
        media=((av3*4)+(av2*3)+(av1*3))/10
    if (media>=5):
        print("APROVADO")
    elif(media<5):
        print("REPROVADO")
    cod=int(input("Insira o codigo do aluno: "))
print("PROGRAMA ENCERRADO.")
