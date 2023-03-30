#Escreva uma função que receba uma lista e retorne uma nova lista com todos os elementos originais, exceto o primeiro e o último elemento.
#Por exemplo:
#t=[1,2,3,4]
#Resultado: [2,3]

t = [1,2,3,4]
del t[0]
del t[-1]#Tirar um numero
print(t)
