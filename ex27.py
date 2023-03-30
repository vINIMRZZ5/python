#Software que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário.
#Mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    nm=input("Dígite seu Usuário: ")
    sn=input("Dígite sua Senha: ")
    if (nm==sn):
        print("O Usuário não pode ser igual a Senha.")
    
    else:
        print("Óla, Bem Vindo!")
        break
 