#Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, o sobrepeso e o subpeso, 
#para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. 
#O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
#Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto, do mais baixo, do cliente com sobrepeso e subpeso, além da média das alturas e dos pesos dos clientes.


maioralt=0
maiorpeso=0

maioraltcod=0
menoraltcod=0
maiorpesocod=0
menorpesocod=0

menorpeso=100000000000
menoralt=1000000000000


while True:
    print("Dígite 0 no campo Código para encerrar.")
    cod = float(input("Dígite o seu Código: "))
    if cod != 0:
        alt = float(input("Dígite sua Altura: "))
        if(alt>maioralt):
            maioralt=alt
            maioraltcod=cod
        elif (alt<menoralt):
            menoralt=alt
            menoraltcod=cod
        
        peso = float(input("Dígite seu Peso: "))
        if(peso>maiorpeso):
            maiorpeso=peso
            maiorpesocod=cod 
        elif(peso<menorpeso):
            menorpeso=peso
            menorpesocod=cod

    
    else:
        
        print("O Código do Maior Peso é: ",maiorpesocod)
        print("O Maior Peso é: ", maiorpeso)
        print("O Código do Menor Peso é: ",menorpesocod)
        print("O Menor Peso é: ", menorpeso)
        print("O Código da Maior Altura é: ", maioraltcod)
        print("A Maior Altura é: ", maioralt)
        print("O Código da Menor Altura é: ", menoraltcod)
        print("A Menor Altura é: ", menoralt)
        break



