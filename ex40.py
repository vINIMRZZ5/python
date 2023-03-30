#Software que imprima na tela apenas números ímpares entre 1 e 50

#for i in range(1,51,2):
    #print(i)


#Faça um programa que receba dois números inteiros e gere os números que estão no intervalo compreendidos por eles.


n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
k=0
for n3 in range(n1+1,n2):
    lista = [n3]
    print(n3)
    k=k+n3
print("Soma dos Itens: ",k) 
    

    