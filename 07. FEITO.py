'''
7. Escreva um algoritmo que calcule a média aritmética das 3 notas dos alunos de uma classe. O algoritmo deverá ler, além das notas, o código do aluno e deverá ser
encerrado quando o código for igual a zero.
'''
Cod_aluno=int(input("Insira o codigo do aluno: "))
while Cod_aluno > 0 :
    Media_1=int(input("Insira a media 1 do aluno: "))
    Media_2=int(input("Insira a media 2 do aluno: "))
    Media_3=int(input("Insira a media 3 do aluno: "))
    Media_Final=(Media_1+Media_2+Media_3)/3
    print("A media final do aluno", Cod_aluno,"é",Media_Final)
    Cod_aluno=int(input("Insira o codigo do aluno: "))