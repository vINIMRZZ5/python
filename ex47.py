#Software que numa eleição existem três candidas. Faça um programa que peça o número total de eleitores.
#Peça para cada eletor votar e ao final mostrar o número de votos de cada candidato.

n1=0
n2=0
n3=0


eleitor = int(input("Digite o número de Eleitores: "))
print(" つ ◕_◕ ༽つ Eleitor 1")
print(" つ ◕_◕ ༽つ Eleitor 2")
print(" つ ◕_◕ ༽つ Eleitor 3")




for ele in range(0, eleitor):  
    voto = int(input("Dígite o número do seu candidato: "))
    if voto == 1:
        n1 = n1+1
        print("Voto para Eleitor 1!")

    elif voto == 2:
        n2 = n2+1
        print("Voto para Eleitor 2!")

    if voto == 3:
        n3 = n3+1
        print("Voto para Eleitor 3!")

else:
    voto == 0
    print("Tota de votos para Eleitor 1: ",n1)
    print("Tota de votos para Eleitor 2: ",n2)
    print("Tota de votos para Eleitor 3: ", n3)

