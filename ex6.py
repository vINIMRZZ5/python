#Software para ler um valor em reais e calcular o valor equivalente em dólares. O usuário deve informar, além do valor em reais da compra, o valor da cotação do dolar

real = float(input("Digite o valor em real: "))
cotacao = float(input("Digite a cotação do dolar: "))
total = real*cotacao 
print(total)