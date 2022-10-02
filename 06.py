'''
6. Em uma eleição presidencial existem quatro candidatos. Os votos são informados através de códigos. 
Os dados utilizados para a contagem dos votos obedecem à seguinte
codificação:
- 1,2,3,4 = voto para os respectivos candidatos;
- 5 = voto nulo;
- 6 = voto em branco;
Elabore um algoritmo que leia o código do candidado em um voto. Calcule e escreva:
- total de votos para cada candidato;
- total de votos nulos;
- total de votos em branco;
Como finalizador do conjunto de votos, tem-se o valor 0.
'''
candidato1=0
candidato2=0
candidato3=0
candidato4=0
nulo=0
branco=0
voto=1

while (voto!=0):
    print("- 1,2,3,4 = voto para os respectivos candidatos;")
    print("- 5 = voto nulo;")
    print("- 6 = voto em branco;")
    voto=int(input("Insira seu voto:"))
    if (voto==1):
        candidato1+=1
    elif (voto==2):
        candidato2+=1
    elif (voto==3):
        candidato3+=1
    elif (voto==4):
        candidato4+=1
    elif (voto==5):
        nulo+=1
    elif (voto==6):
        branco+=1

print("O candidato %d, tem: "%candidato1)
print("O candidato %d, tem: "%candidato2)
print("O candidato %d, tem: "%candidato3)
print("O candidato %d, tem: "%candidato4)
print("%d votos foram nulos"%nulo)
print("%d votos foram em branco"%branco)
