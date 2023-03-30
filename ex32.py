#Software de Estoque



print("Dígite o numero de itens no Estoque: ")
#Váriaveis do Estoque
est1=float(input("(Código:10)Caderno: "))
est2=float(input("(Código:20)Caneta: "))
est3=float(input("(Código:30)Lápis: "))
est4=float(input("(Código:40)Borracha: "))
est5=float(input("(Código:50)Régua: "))
print("Estoque Registrado! ")
print("______________________")




while True:  #Menu do Estoque
    print("E - Entrada no Estoque. ")
    print("S - Saída no Estoque. ")
    print("R - Relatório. ")
    print("X - Sair. ")


    esto=input("Dígite o que Deseja: ")


    if esto == 'E':   #Entrada No Estoque
        cod=float(input("Qual o Código do Produto? "))


        if cod==10:
             entrada=float(input("Quantos Itens Deseja Adicionar? "))
             est1=est1+entrada
             print("Tem ",est1," Caderno no Estoque.")
   
        if cod==20:
             entrada=float(input("Quantos Itens Deseja Adicionar? "))
             est2=est2+entrada
             print("Tem ",est2,"Caneta no Estoque.")

        if cod==30:
             entrada=float(input("Quantos Itens Deseja Adicionar? "))
             est3=est3+entrada
             print("Tem ",est3,"Lápis no Estoque.")
      
    
        if cod==40:
             entrada=float(input("Quantos Itens Deseja Adicionar? "))
             est4=est4+entrada
             print("Tem ",est4,"Borracha no Estoque.")

        if cod==50:
             entrada=float(input("Quantos Itens Deseja Adicionar? "))
             est5=est5+entrada
             print("Tem ",est5,"Réguas no Estoque.")
        
    elif esto == "S":  #Sáida Do Estoque
        cod=float(input("Qual o Código do Produto? "))        
        
        if  cod==10:
            entrada=float(input("Quantos Itens Deseja Remover? "))
            est1=est1-entrada
            print("Tem ",est1,"Caderno no Estoque.")

        if  cod==20:
            entrada=float(input("Quantos Itens Deseja Remover? "))
            est2=est2-entrada
            print("Tem ",est2,"Caderno no Estoque.")

        if  cod==30:
            entrada=float(input("Quantos Itens Deseja Remover? "))
            est3=est3-entrada
            print("Tem ",est3,"Caderno no Estoque.")
        
        if  cod==40:
            entrada=float(input("Quantos Itens Deseja Remover? "))
            est4=est4-entrada
            print("Tem ",est4,"Caderno no Estoque.")
        
        if  cod==50:
            entrada=float(input("Quantos Itens Deseja Remover? "))
            est5=est5-entrada
            print("Tem ",est5,"Caderno no Estoque.")
    
    elif esto == 'R':   #Relatório do Estoque
        print("Caderno: ",est1,".")
        print("Caneta: ",est2,".")
        print("Lápis: ",est3,".")
        print("Borracha: ",est4,".")
        print("Régua: ",est5,".")

    else:   #Saída do Estoque 
        esto == "X"
        print("Estoque Finalizado! ")
        break

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
      




   

      
               

