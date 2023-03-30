#Software tabela Padaria


pao=0

for c in range(1,51):
    print(c, end = " ")
    print("-"*1, end = " ")
    pao = pao + 0.18
    print(f"{pao:.2f}")