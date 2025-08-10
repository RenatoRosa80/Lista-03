#24. Faça um programa que calcule e mostre a média aritmética de 
# N notas.
qtde_notas = int(input(" Quantas notas deseja inserir no Sistema? "))
soma_nota = 0
for i in range(1,qtde_notas + 1):
    nota = int(input(f"Digite a {i}º : "))
    soma_nota += nota 
    
    media_nota = soma_nota / qtde_notas
    
print(f" A Média das notas é: {media_nota} ")