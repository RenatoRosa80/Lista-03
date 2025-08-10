"""
27. Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para 
cada turma. As turmas não podem ter mais de 40 alunos.

"""
import math
qtde_turmas = int(input(" Informe quantas turmas: "))
print(f" Sao {qtde_turmas} Turmas! ")
media = 0
lista = []

for i in range(qtde_turmas):
    while True:
        qtde_alunos = int(input(f" Informe a quantidade de Alunos da {i + 1}ª Turma: "))
        lista.append(qtde_alunos)
        

        if qtde_alunos > 40:
                print(" Cada Turma pode ter no máximo 40 alunos! ")
        
        break
  
media = sum(lista) / qtde_turmas
print(f" A média de alunos por turma é {media:.2f}")

    
        