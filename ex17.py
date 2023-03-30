#Software que pergunte em que turno você estuda.
#Peça para digitar M-Matutino ou V-Vespertino ou N-Noturno.
#Imprima a menssagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!"
#Conforme o caso

m = input("Escreva \nM-Matutino \nV-Vespertino \nN-Noturno \nDe acordo com seu turno: ")
if(m == "M"):
    print("Matutino \nBom Dia!")
elif(m == "V"):
    print("Vespertino \nBoa Tarde!")
elif(m == "N"):
    print("Noturno \nBoa noite!")
else:
    print("Valor Inválido")
