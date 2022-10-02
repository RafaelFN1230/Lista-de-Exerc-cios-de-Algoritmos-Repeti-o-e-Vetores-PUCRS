'''
5. Construir um algoritmo que calcule a média aritmética de vários valores inteiros positivos, 
lidos externamente. O final da leitura acontecerá quando for lido um valor negativo.
'''
val=0
cont=0
soma=0
while val>=0:
    val=int(input("Insira o %d valor: "%(cont+1)))
    cont+=1
    soma+=val
    total=soma/cont
    print("O valor da media é: ",total)