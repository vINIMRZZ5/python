#Faça um programa que leia 5 números e informe a soma e a méia dos números. 


lista=[]
s = 0
for c in range(1,6):    lista.append(int(input("Valor:")))
for c in lista:  s = s + c
print(f"soma = {s} Média = {s/5}")

   