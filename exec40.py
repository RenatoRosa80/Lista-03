"""
40. Foi feita uma estatística em cinco cidades brasileiras para 
coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes 
dados:
- Código da cidade;
- Número de veículos de passeio (em 1999);
- Número de acidentes de trânsito com vítimas (em 1999).
Deseja-se saber:
- Qual o maior e menor índice de acidentes de transito e a que cidade
pertence;
- Qual a média de veículos nas cinco cidades juntas;
- Qual a média de acidentes de trânsito nas cidades com menos de 2.000 
veículos de passeio.
"""

#Retorno:

maior_indice_acidentes = -1
menor_indice_acidentes = float("inf")
cidade_codigo = []
media_veiculos = 0
codigo_maior_cidade_indice = 0
codigo_menor_indice_cidade = 0
total_veiculos = 0
soma_acidentes_menos_2000 = 0
contador_cidades_menos_2000 = 0

for i in range(5):
    while True:
        try:
            codigo_cidade = int(input("Informe o código da Cidade com 6 dígitos: "))
            numero_veiculos_passeio = int(input("Informe a quantidade de veículos: "))
            acidentes_transito_com_vitimas = int(input("Informe o número de acidentes com vítimas: "))
            
            cidade_codigo.append(codigo_cidade)
            total_veiculos += numero_veiculos_passeio
            
            # Calculando Maior índice
            if maior_indice_acidentes < acidentes_transito_com_vitimas:
                maior_indice_acidentes = acidentes_transito_com_vitimas
                codigo_maior_cidade_indice = codigo_cidade

            # Calculando Menor índice
            if menor_indice_acidentes > acidentes_transito_com_vitimas:
                menor_indice_acidentes = acidentes_transito_com_vitimas
                codigo_menor_indice_cidade = codigo_cidade

            # Calculando a Média de acidentes nas cidades com menos de 2000 veículos
            if numero_veiculos_passeio < 2000:
                soma_acidentes_menos_2000 += acidentes_transito_com_vitimas
                contador_cidades_menos_2000 += 1

            break
        except ValueError:
            print("Digite valores válidos!")

# Demais calculos
media_veiculos = total_veiculos / 5
media_acidentes_menos_2000 = (soma_acidentes_menos_2000 / contador_cidades_menos_2000
                              if contador_cidades_menos_2000 > 0 else 0)

print("\n===== RESULTADOS =====")

print(f"Média de veículos nas 5 cidades: {media_veiculos:.2f}")
print(f"Maior índice de acidentes: {maior_indice_acidentes} na cidade {codigo_maior_cidade_indice}")
print(f"Menor índice de acidentes: {menor_indice_acidentes} na cidade {codigo_menor_indice_cidade}")
print(f"Média de acidentes nas cidades com menos de 2000 veículos: {media_acidentes_menos_2000:.2f}")

