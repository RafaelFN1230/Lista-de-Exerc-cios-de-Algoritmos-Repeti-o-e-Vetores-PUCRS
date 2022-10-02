'''
13. Escrever um algoritmo que leia um número n que indica quantos valores devem ser lidos a seguir. 
Para cada número lido, mostre uma tabela contendo o valor lido e o
fatorial deste valor.
'''

n=int(input("Insira quantos numeros devem ser lidos: "))

for x in range(n):
    a=int(input("Insira o valor do fatorial: "))
    resp=a
    for y in range (2,a+1):
        resp*=y-1
    print("Valor lido:",a)
    print("Fatorial de %d:"%a,resp)

