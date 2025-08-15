"""
37. Uma academia deseja fazer um senso entre seus clientes para 
descobrir o mais alto, o mais baixo, o mais gordo e o mais magro, 
para isto você deve fazer um programa que pergunte a cada um dos 
clientes da academia seu código, sua altura e seu peso. O final da 
digitação de dados deve ser dada quando o usuário digitar 0 (zero) no 
campo código. Ao encerrar o programa também deve ser informados os 
códigos e valores do clente mais alto, do mais baixo, do mais gordo e 
do mais magro, 
além da média das alturas e dos pesos dos clientes
"""


maior_altura = float("-inf")
codigo_altura_maior = 0

menor_altura = float ("inf")
codigo_menor_altura = 0

maior_peso = float("-inf")
codigo_maior_peso = 0

mais_magro = float("inf")
codigo_mais_magro = 0

soma_altura = 0
soma_peso = 0
qtde_cliente = 0

while True:
    codigo = int(input(" Informe o seu código de 6 dígitos: Digite 0 para encerrar o programa. ")) 

    if codigo == 0:
       break
    altura = int(input(" Informe sua altura em centímetros: "))
    peso = float(input(" Informe o seu peso: "))
    
    soma_altura += altura
    soma_peso += peso
    qtde_cliente += 1
    
    if altura > maior_altura:
            maior_altura = altura
            codigo_altura_maior = codigo 
            
    if altura < menor_altura:
            menor_altura = altura
            codigo_menor_altura = codigo
            
    if  peso > maior_peso:
            maior_peso = peso
            codigo_maior_peso = codigo
            
    if peso < mais_magro:
            mais_magro = peso
            codigo_mais_magro = codigo
            
            
print("\n===== RESULTADOS =====")

print(f"Cliente mais alto: código {codigo_altura_maior}, altura {maior_altura} cm")
print(f"Cliente mais baixo: código {codigo_menor_altura}, altura {menor_altura} cm")
print(f"Cliente mais pesado: código {codigo_maior_peso}, peso {maior_peso} kg")
print(f"Cliente mais magro: código {codigo_mais_magro}, peso {mais_magro} kg")

if qtde_cliente > 0:
    media_altura = soma_altura / qtde_cliente
    media_peso = soma_peso / qtde_cliente
    print(f"Média de altura dos clientes: {media_altura:.2f} cm")
    print(f"Média de peso dos clientes: {media_peso:.2f} kg")
else:
    print("Nenhum cliente foi registrado.")
            
            

        