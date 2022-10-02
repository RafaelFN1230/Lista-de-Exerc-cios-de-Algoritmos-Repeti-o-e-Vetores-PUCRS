'''
12. Escrever um algoritmo que leia 20 valores para uma variável n e, para cada um deles, 
calcule a tabuada de 1 até n. Mostre a tabuada na forma:
1 x n = n
2 x n = 2n
3 x n = 3n
.......
n x n = n2
'''
for x in range(20):
    n=int(input("Insira o valor de N: "))
    cont=0
    for y in range(1,n+1):
        total=y*n
        cont+=1
        print("%d X %d = "%(cont,n),total)
