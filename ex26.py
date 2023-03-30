#Software que peça uma nota, entre zero e dez.
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido

while True:
    n1 = float(input("Dígite sua nota: "))
    if n1>10 or n1<0:
        print("Valor invalido")
    else:
        break

