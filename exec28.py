"""
28. Faça um programa que calcule o valor total investido por um 
colecionador em sua coleção de CDs e o valor médio gasto em cada um 
deles. O usuário deverá informar a quantidade de CDs e o valor pago
em cada um.
"""
qtde_cd = int(input(" Qual a  quantidade cd comprado? "))
total_investido = 0

for i in range(1, qtde_cd + 1): # Informar o valor gasto por cada CD
    valor_cd = float(input(f"Informe o valor do CD {i}: R$ "))
    #print(f"Valor do CD {i}: R$ {valor_cd:.2f}")

    total_investido += valor_cd
    
media = total_investido / valor_cd

print(f" O valor Total investido foi de {total_investido:.2f} R$. ")





