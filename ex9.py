#Software que recebe nome, idade, sexo e receba duas notas e calcula a média aritmética e mostre o resultado

nome = input("Dígite seu nome: ")
idade = float(input("Dígite sua idade: "))
sexo = input("Qual seu sexo: ")
valor1 = float(input("Dígite sua nota: "))
valor2 = float(input("Dígite sua outra nota: "))
total = (valor1+valor2)/2
print ("Nome: ",nome)
print ("Idade: ",idade)
print ("Sexo: ",sexo)
print ("Sua nota aritmética é : ",total)
