#Software que verifique se uma letra digitada é "F","M" ou "O". Conforme a letra escrever: F - Feminino, M - Masculino, O - Outros ou Sexo Inválido

sexo = input("Digite F,M ou O para o sexo: ")
if(sexo == "M"):
    print("Masculino")
if(sexo == "F"):
    print("Feminino")
if(sexo == "O"):
    print("Outros")
else:
    print("Sexo Inválido")




