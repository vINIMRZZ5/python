#Calculadora que solicita qual operação desejada(multiplicação,Adição e Subtração)imprimindo um menu.
#Ultilizando "while" o menu ficara ativo até que o usuário digite um comando para interromper. 
#Verifique a partir de testes condicionais qual opção desejada, solicite dois avlores para a operação e efetue o cálculo.
#Imprima o resultado e retorne ao menu principal
while True:
    print("==CALCULADORA==")
    print("1- Multiplicação")
    print("2- Divisão")
    print("3- Adição")
    print("4- Subtração")
    print("0- Encerrar")

    n1= float(input("Dígite um número: "))
    if (n1==1):
        print("==Multiplicação==")
        vm=float(input("Dígite um valor: "))
        vm2=float(input("Dígite outro valor: "))
        total = vm*vm2
        print(total)

    elif n1==2:
        print("==Divisão==")
        vm=float(input("Dígite um valor: "))
        vm2=float(input("Dígite outro valor: "))
        total = vm/vm2
        print(total)

    elif n1==3:
        print("==Adição==")
        vm=float(input("Dígite um valor: "))
        vm2=float(input("Dígite outro valor: "))
        total = vm+vm2
        print(total)

    elif n1==4:
        print("==Subtração==")
        vm=float(input("Dígite um valor: "))
        vm2=float(input("Dígite outro valor: "))
        total = vm-vm2
        print(total)
    elif n1==0:
        print("Programa Encerrado!")
        break
    
        




        





