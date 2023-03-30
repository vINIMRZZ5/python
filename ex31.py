#Em uma eleição presidencial existem quatro candidatos. 
#Os votos são informados através de códigos. Os dados utilizados para a contagem dos votos obedecem à seguinte codificação: 
#1,2,3,4 = voto para os respectivos candidatos; 
#5 = voto nulo; 
#6 = voto em branco; 

#Elabore um programa que leia o código votado por vários eleitores. Como finalizador da entrada de dados, considere o código zero. 
#Ao final, calcule e escreva: 
#total de votos para cada candidato; 
#- total de votos nulos; 
#- total de votos em branco;

print("-Vote 1 para Elo-")
print("-Vote 2 para Ele-")
print("-Vote 3 para Ela-")
print("-Vote 4 para Elu-")
print("-Vote 5 para Nulo-")
print("-Vote 6 para Branco-")
print("_____________________________")

totalelo= 0 
totalele=0
totalela=0
totalelu=0
totalnulo=0
totalbranco=0


while True:
    votos = int(input("Digite seu voto: "))
    if votos == 1:
        totalelo = totalelo+1
        print("Voto Confirmado!")
        
    
    elif votos == 2:
        totalele = totalele+1
        print("Voto Confirmado!")
    
    elif votos == 3:
        totalela = totalela+1
        print("Voto Confirmado!")
    
    elif votos == 4:
        totalelu = totalelu+1
        print("Voto Confirmado!")
    

    elif votos == 5:
        totalnulo = totalnulo+1
        print("Voto Confirmado!") 

    elif votos == 6:
        totalbranco = totalbranco+1
        print("Voto Confirmado!")
    
    else:
        if votos == 0:
            print("Votação Encerrado! ")
    
            break
print("Total de Votos Candidato 1: ", totalelo)
print("Total de Votos Candidato 2: ", totalele)
print("Total de Votos Candidato 3: ", totalela)
print("Total de Votos Candidato 4: ", totalelu)
print("Total de Votos Nulo: ", totalnulo)
print("Total de Votos Branco: ", totalbranco)



    
