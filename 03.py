'''
A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário 
e número de filhos. A prefeitura deseja saber:
a) média do salário da população;
b) média do número de filhos;
c) maior salário;
d) percentual de pessoas com salário até R$100,00.
O final da leitura de dados se dará com a entrada de um salário negativo. (Use o comando ENQUANTO-FAÇA)
'''
cont=0
cont_sal=0
salario=0
media_sal=0
media_filho=0
maior=0

while (salario>=0):
    salario=float(input("Insira o salário: "))
    if(salario>=0):
        n_filhos=int(input("Insira o número de filhos: "))
        media_sal+=salario
        media_filho+=n_filhos
        cont+=1
        if (salario>maior):
            maior=salario
        if (salario>100):
            cont_sal+=1

mediaf_filho=media_filho/cont
mediaf_sal =media_sal/cont
total_percent=cont_sal/cont*100

print("Média do salário da população: R$",mediaf_sal)
print("Média do número de filhos: ",mediaf_filho)
print("Maior salário: R$",maior)
print("Percentual de pessoas com salário até R$100,00: %.2f%"%total_percent)