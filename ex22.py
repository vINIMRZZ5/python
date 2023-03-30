#Software que peça um número correspondente a um determinado ano e em seguida informe se esta ano é ou não bissexto.

n1 = float(input('Dígite um ano: '))

if(n1%4==0):
    if(n1%100 == 0):
        if(n1%400 == 0):  
            print('O ano digitado é Bissexto')
        else:
            print('Não é Bissexto')    
    else:
        print('O ano digitado é Bissexto')
else:
    print('Não é Bissexto')
