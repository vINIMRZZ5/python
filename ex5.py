#Software para ler o nome de um produto, a quantidade comprada, o valor unitário e o percentual de desconto a ser aplicado para o pagamento.

nome = (input("Qual o nome do produto: ")) 
quantidade = float(input("Quantidade: "))
valor = float(input("Digite o valor: "))
porcentagem = float(input("Digite a porcentagem: "))
total = valor*quantidade
desconto = total*porcentagem/100
valorliquido = total-desconto
print(nome)
print(quantidade)
print(valor)
print(porcentagem)
print(desconto)
print(valorliquido)