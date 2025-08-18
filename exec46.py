"""
46. Em uma competição de salto em distância cada atleta tem direito a cinco 
saltos. No final da série de saltos de cada atleta, o melhor e o pior 
resultados são eliminados. O seu resultado fica sendo a média dos três valores
restantes. Você deve fazer um programa que receba o nome e as cinco distâncias 
alcançadas pelo atleta em seus saltos e depois informe a média dos saltos 
conforme a descrição acima informada (retirar o melhor e o pior salto e 
depois calcular a média). Faça uso de uma lista para armazenar os saltos. 
Os saltos são informados na ordem da execução, portanto não são ordenados.
O programa deve ser encerrado quando não for informado o nome do atleta. 
A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m

Segundo Salto: 6.1 m

Terceiro Salto: 6.2 m

Quarto Salto: 5.4 m

Quinto Salto: 5.3 m

Melhor salto: 6.5 m

Pior salto: 5.3 m

Média dos demais saltos: 5.9 m

Resultado final:

Rodrigo Curvêllo: 5.9 m

"""
contador = 1
while True:
    nome_atleta = input(f"Informe o nome do {contador}º Atleta (ou enter para finalizar): ").strip()
    if nome_atleta == "":
        break
    
    saltos = []
    for i in range(5):
        distancia = float(input(f"Distância do {i + 1}º salto: "))
        saltos.append(distancia)
    
    # Melhor e pior salto
    melhor_salto = max(saltos)
    pior_salto = min(saltos)

    # Remove uma ocorrência do melhor e do pior para o cálculo
    saltos_restantes = saltos.copy()
    saltos_restantes.remove(melhor_salto)
    saltos_restantes.remove(pior_salto)

    media_demais_saltos = sum(saltos_restantes) / len(saltos_restantes)

    # Saída formatada
    print(f"\nAtleta: {nome_atleta}\n")
    print(f"Primeiro Salto: {saltos[0]} m")
    print(f"Segundo Salto: {saltos[1]} m")
    print(f"Terceiro Salto: {saltos[2]} m")
    print(f"Quarto Salto: {saltos[3]} m")
    print(f"Quinto Salto: {saltos[4]} m\n")

    print(f"Melhor salto: {melhor_salto} m")
    print(f"Pior salto: {pior_salto} m")
    print(f"Média dos demais saltos: {media_demais_saltos:.1f} m\n")

    print("Resultado final:")
    print(f"{nome_atleta}: {media_demais_saltos:.1f} m\n")
