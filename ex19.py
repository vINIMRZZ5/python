#software que leia um número e exiba o dia correpondente da semana.(1- Domingo, 2- Segunda e etc), se digitar outro valor deve aparecer valor inválido

d1 = float(input("\n1-Domingo \n2-Segunda \n3-Terça \n4-Quarta \n5-Quinta \n6-Sexta \n7-Sábado \nDígite um numero de acordo ao dia: "))
if (d1 == 1):
    print('Ótimo Domingo!')
elif (d1 == 2):
    print('Ótima Segunda!')
elif (d1 == 3):
    print('Ótima Terça!')
elif (d1 == 4):
    print('Ótima Quarta!')
elif (d1 == 5):
    print('Ótima Quinta!')
elif (d1 == 6):
    print('Ótima Sexta!')
elif (d1 == 7):
    print('Ótimo Sábado!')
else:
    print('Valor inválido')