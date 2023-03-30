#Faça um Programa que peça os 3 lados de um triângulo. 
#O programa deverá informar se os valores podem ser um triângulo. 
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.


n1= float(input('Dígite o valor de um lado do triângulo: '))
n2= float(input('Dígite o valor do outro lado do triângulo: '))
n3= float(input('Dígite o último valor do lado do triângulo: '))

if (n1+n2<n3) or (n1+n3<n2) or (n2+n1<n3) or (n2+n3<n1) or (n3+n1<n2) or (n3+n2<n1):
    if (n1 == n2) and (n2 == n3):
        print('Triângulo Equilátero')
    elif (n1 == n2) and (n2 != n3) or (n1 == n3) and (n3 != n2) or (n2 == n3) and (n2 != n1):
        print('Triângulo Isósceles')
    elif (n1 != n2) and (n2 != n3) or (n1 != n3) and (n3 != n2) or (n2 != n3) and (n2 != n1):
        print('Triângulo Escaleno')