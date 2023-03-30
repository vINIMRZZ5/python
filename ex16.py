#Software que lê três números e mostre-os em ordem decrescente 

n1 = float(input("Dígite um número: "))
n2 = float(input("Dígite outro número: "))
n3 = float(input("Dígite o último número: "))

if n1<n2 and n2<n3: 
 print(n3, ("-"), n2, ("-"), n1)
if n1<n3 and n3<n2:
    print(n2, ("-"), n3, ("-"), n1)
if n2<n1 and n1<n3:
    print(n3, ("-"), n1,("-"), n2)
if n2<n3 and n3<n1:
    print(n1, ("-"), n3, ("-"), n2)
if n3<n1 and n2<n1:
    print(n1, ("-"), n2, ("-"), n3)
if n3<n1 and n1<n2:
    print(n2, ("-"), n1, ("-"), n3)