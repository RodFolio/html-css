lista_notas = [5.6,7.9,8.6,4.4,9.8,10]
print('Imprimindo a lista de notas :',lista_notas)
print(len(lista_notas))
for i in range(len(lista_notas)):
    if lista_notas[i] >= 7:
        print('Aprovado com nota:', lista_notas[i])
    elif 6.9 < lista_notas[i] < 5:
        print('Recuperação com nota:', lista_notas[i])
    else:
        print('Reprovado com nota:', lista_notas[i]) 
