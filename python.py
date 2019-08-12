import statistics as es 

ingles_n1 = float(input('digite a primeira nota: '))
ingles_n2 = float(input('digite a segunda nota: '))

lista_notas = [ingles_n1, ingles_n2 ]

soma = sum(lista_notas)
media = es.mean(lista_notas)
 
if media >= 7:
     print('aprovado')

elif media >= 5 and media < 7:
    print('Recuperacao')

else:
    print('Reprovado')
