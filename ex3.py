nome = input("Digite seu nome: ")
print(nome)

idade = input("Digite sua idade: ")
print(type(idade))

salario = int(input('Salario?='))
imposto = float(input('Digite o imposto= '))

valor1 = float(input("Digite o valor 1 = "))
valor2 = float(input("Digite o valor 2 = "))
total = valor1 * valor2
print("O total de %.2f x %.2f foi %.2f" % (valor1, valor2, total) )
print("O total de", valor1, "X", valor2, "foi = ", total)
