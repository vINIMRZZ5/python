#Faça um programa que leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo: 
#Média de Aproveitamento Conceito 
#Entre 9.0 e 10.0 A 
#Entre 7.5 e 9.0 B 
#Entre 6.0 e 7.5 C 
#Entre 4.0 e 6.0 D 
#Entre 4.0 e zero E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

n1 = float(input('Dígite sua nota: '))
n2 = float(input('Dígite sua segunda nota: '))
total = (n1+n2)/2
print('Média: ', total)

if  (total>=9) and (total<=10):
    print('Nota A \nAPROVADO(a)')
elif  (total>=7.5) and (total<9):
    print('Nota B \nAPROVADO(A)')
elif  (total>=4) and (total<6):
    print('Nota C \nREPROVADO(A)')
elif  (total<4) and (total>=0):
    print('Nota E \nREPROVADO(A)')


