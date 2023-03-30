#Software para verificar se a letra digitada é vogal ou consoante

vogal = input("Dígite uma letra: ")
if (vogal == "a") or (vogal == "e") or (vogal == "u") or (vogal == "i") or (vogal== "o"):
    print("Sua letra é vogal")    
elif (vogal == "A") or (vogal == "E") or (vogal == "U") or (vogal == "I") or (vogal== "O"):
    print("Sua letra é vogal")  
else:
    print("sua letra é consoante")

