'''1. Escrever um algoritmo que lê 5 valores para a, um de cada vez, 
e conta quantos destes valores são negativos, escrevendo esta informação.
'''
cont=0
for x in range (5):
    a=float(input("Insira o valor de A: "))
    if (a<0):
        cont+=1
print("%d numeros são negativos."%cont)