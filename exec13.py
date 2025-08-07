"""
13. Faça um programa que peça dois números, base e expoente, 
calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.
"""
#ENTRADA

# Solicita os valores ao usuário
base = float(input("Informe o valor da base: "))
expoente = int(input("Informe o valor do expoente (deve ser um número inteiro): "))

# Inicializa o resultado
resultado = 1

# Tratando o expoente positivo
if expoente > 0:
    for _ in range(expoente):
        resultado *= base
# Tratando o expoente negativo
elif expoente < 0:
    for _ in range(-expoente):
        resultado *= base
    resultado = 1 / resultado
# Expoente zero
else:
    resultado = 1

# Exibe o resultado
print(f"O resultado de {base} elevado ao {expoente} é: {resultado}")
