"""
13. Faça um programa que peça dois números, base e expoente, 
calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.
"""
# Entrada de dados
base = float(input("Informe o valor da base: "))
expoente = int(input("Informe o valor do expoente (inteiro): "))

# Inicializa o resultado como 1
resultado = 1

# Contador para repetição
contador = 0

print("\n📊 Passo a passo do cálculo:\n")

# Expoente positivo
if expoente > 0:
    while contador < expoente:
        print(f"Passo {contador+1}: {resultado} * {base} = {resultado * base}")
        resultado *= base
        contador += 1

# Expoente negativo
elif expoente < 0:
    while contador < abs(expoente):
        print(f"Passo {contador+1}: {resultado} * {base} = {resultado * base}")
        resultado *= base
        contador += 1
    resultado = 1 / resultado
    print(f"Passo final: 1 / {resultado ** -1} = {resultado}")

# Expoente zero
else:
    print("Qualquer número elevado a 0 é 1.")

# Exibe o resultado final
print(f"\n✅ Resultado final: {base} elevado a {expoente} é igual a {resultado}")
