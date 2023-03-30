#Software que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida

while True:
    d = int(input('Dígite o Dia: '))
    m = int(input('Dígite o mês: '))
    a = int(input('Dígite o ano: '))

    if (d>=0) and (d<=30):
        if (m>=1) and (m<=12):
            print('A data é valida: ',d,'/',m,'/',a,) 
            break
    else:
        print('Data Inválida')