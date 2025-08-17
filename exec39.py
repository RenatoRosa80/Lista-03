"""
39. Faça um programa que leia dez conjuntos de dois valores,
o primeiro representando o número do aluno e o segundo representando
a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo.
Mostre o número do aluno mais alto e o número do aluno mais baixo, 
junto com suas alturas.
"""


maior_altura = float("-inf")
codigo_altura_maior = 0

menor_altura = float ("inf")
codigo_menor_altura = 0

soma_altura = 0

qtde_cliente = 0

for i in range (1, 10):
    codigo = int(input(" Informe o seu código de 6 dígitos: ")) 
    altura = int(input(" Informe sua altura em centímetros: "))
    soma_altura += altura
    qtde_cliente += 1
    
    
    if altura > maior_altura:
        maior_altura = altura
        codigo_altura_maior = codigo 
            
    if altura < menor_altura:
        menor_altura = altura
        codigo_menor_altura = codigo
            
    
            
            
print("\n===== RESULTADOS =====")
print(f"Cliente mais alto: código {codigo_altura_maior}, altura {maior_altura} cm")
print(f"Cliente mais baixo: código {codigo_menor_altura}, altura {menor_altura} cm")

if qtde_cliente > 0:
    media_altura = soma_altura / qtde_cliente
    print(f"Média de altura dos clientes: {media_altura:.2f} cm")
else:
    print("Nenhum cliente foi registrado.")