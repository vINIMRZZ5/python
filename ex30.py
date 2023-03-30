#Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
#Faça um programa que determine o salário atual desse funcionário. 
#Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.


salário = 1000
porcentagem = 1.5
novosal = salário+salário*porcentagem/100

ano = 1997
anonovo = 2023

while ano<=anonovo:
    porcentagem=porcentagem*2
    novosal = novosal+novosal*porcentagem/100
    ano=ano+1
print("Atual Salário é: ", novosal)





