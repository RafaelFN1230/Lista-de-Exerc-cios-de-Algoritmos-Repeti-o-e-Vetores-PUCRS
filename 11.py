'''
11. Escreva um algoritmo que leia um número n (número de termos de uma progressão aritmética), 
a1 ( o primeiro termo da progressão) e r (a razão da progressão) e
escreva os n termos desta progressão, bem como a soma dos elementos.
'''

n=int(input("Insira o número de termos de uma progressão aritmética: "))
a1=float(input("Insira o primeiro termo da progressão: "))
r=int(input("Insira a razão da progressão: "))
progre=[a1]

for x in range (n):
    valor=a1+r*x
    print(valor)
    progre.append(valor)
print(progre)
    