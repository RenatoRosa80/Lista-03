"""
42. Faça um programa que leia uma quantidade indeterminada de 
números positivos e conte quantos deles estão nos seguintes intervalos:
[0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar
quando for lido um número negativo.
"""

intervalo1 = 0  # [0-25]
intervalo2 = 0 # [26-50]
intervalo3 = 0 # [51-75]
intervalo4 = 0 # [76-100]

while True:

    numero = int(input(" Informe um número positivo: Informe um número negativo para terminar a sessao. "))
    if numero < 0:
        print(" Fim do Programa! ")
        break
    if 0 <= numero <= 25:
        intervalo1 += 1
    elif 26 <= numero <= 50:
        intervalo2 += 1
    elif 51 <= numero <= 75:
        intervalo3 += 1
    elif 76 <= numero <= 100:
        intervalo4 += 1

print("\nQuantidade de números nos intervalos:")
print("----------------------------------------")
print(f"Intervalo 1 [0-25]   : {intervalo1}")
print(f"Intervalo 2 [26-50]  : {intervalo2}")
print(f"Intervalo 3 [51-75]  : {intervalo3}")
print(f"Intervalo 4 [76-100] : {intervalo4}")



