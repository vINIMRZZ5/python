#Software que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.


lista = []
n = 0
x=int(input("Qual o total de números: "))
for a in range(1,x+1):
    lista.append(int(input("Digite um número: ")))
    print (lista)


else:
    
    print ("O maior número é: ", max(lista))
    print ("O menor número é: ", min(lista))
    print ("A soma dos números é: ",sum(lista))
    
   
   