'''
8. Escreva um algoritmo que calcule a média dos números digitados pelo usuário, se eles forem pares. 
Termine a leitura se o usuário digitar zero (0).
'''

numero=1
cont=0

while numero != 0:
    numero=float(input("insira aqui o numero para calcular a media: "))
    if (numero%2==0 and numero!=0):
        cont+=1
        media=numero/cont
        print("Media dos numeros pares: ",media)
    elif(numero==0):
        print("Encerrando programa.")
    else:
        print("Este numero não é par.")
print("Media dos numeros pares: ",media)
       
