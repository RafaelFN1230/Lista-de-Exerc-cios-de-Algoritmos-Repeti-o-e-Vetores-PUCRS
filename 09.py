'''
9. Escreva um algoritmo que leia 50 valores e encontre o maior e o menor deles. Mostre o resultado.
'''
a=float(input("Insira um valor: "))
maior=a
menor=a
for x in range(49):
    a=float(input("Insira um valor: "))
    if (a>maior):
        maior=a
    if(a<menor):
        menor=a
print("Maior número: ", maior)
print("Menor número: ",menor)