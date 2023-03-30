#Software que ao receber um salário atual de um funcionário, calcule o valor do novo salário reajustado de acordo com a tabela

sal = float(input("Dígite seu salário atual: "))
if sal<500:
    total = sal+((sal*15)/100)
    print(total)
if sal>=500 and sal<=1000:
    total = sal+((sal*10)/100)
    print(total)
if sal>1000:
    total = sal+((sal*5)/100)
    print(total)

 
