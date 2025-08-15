"""
32. Faça um programa que calcule o fatorial de um número inteiro 
fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser 
conforme o exemplo abaixo:

Fatorial de: 5
- 5! = 5 . 4 . 3 . 2 . 1 = 120
"""
numero_inteiro = int(input(" Informe um número numero_inteiro"))
fatorial = 1
lista = []

for i in range(numero_inteiro, 0, -1):
    fatorial *= i
    lista.append(i)

print(f"{numero_inteiro}! = {' . '.join(map(str, lista))} = {fatorial}")
"""
map(str, lista) → convertendo todos os números da lista para texto.

' . '.join(...) → junta esses textos usando " . " como separador
(para ficar no formato n . n-1 . ... . 1).

O f-string (f"") monta a frase final, mostrando:

O número com ! (símbolo de fatorial).

A multiplicação passo a passo.

O resultado final.
"""
