#Software com menu infinito e opção para sair que leia e valide as seguintes informações
#Idade: entre 0 e 150
#Salário: maior que zero; Sexo: 'f' ou m' 'ou 'o' 
#Estado Civil: 's', 'c', 'v', 'd'

while True:
    idade=float(input("Dígite sua Idade: "))
    sal=float(input("Dígite seu Salário: "))
    sexo=input("Dígite F- Feminino, M- Masculino ou O- Outro: ")
    sc=input("Dígite S-Solteiro(a), C- Casado(a), V- Viúvo(a), D- Divorciado(a): ")
    
    if (idade<0 or idade>150):
        print("Idade Inválida!")
        
    elif sal<0:
        print("Salário Inválido!")
    
    elif sexo != 'F' or sexo != 'M' or sexo != 'O':
        print("Gênero Inválido!")
    
    elif sc != 'S' or sc != 'C' or sc != 'V' or sc != 'D':
        print("Estado Civil Inválido!")

   
    