"""
41. Faça um programa que receba o valor de uma dívida e mostre uma 
tabela com os seguintes dados: valor da dívida, valor dos juros,
quantidade de parcelas e valor da parcela.

Os juros e a quantidade de parcelas seguem a tabela abaixo:

Quantidade de Parcelas % de Juros sobre o valor inicial da dívida

- 1 0
- 3 10
- 6 15
- 9 20
- 12 25

Exemplo de saída do programa:

Valor da Dívida - Valor dos Juros - Quantidade de Parcelas - 
Valor da Parcela

- R$ 1.000,00 - 0 - 1 - R$ 1.000,00
- R$ 1.100,00 - 100 - 3 - R$ 366,00
- R$ 1.150,00 - 150 - 6 - R$ 191,67
"""
valor_divida = float(input(" Informe o valor da divida: "))
qtdade_parcelas= int(input(" Quantas parcelas desjea dividir, 1, 3, 6, 9 ou 12x: "))
juros = 0
valor_divida_atual = 0
valor_parcelas =  valor_divida_atual


if qtdade_parcelas == 1:
    juros = 0
    valor_divida_atual = valor_divida + juros
    valor_parcelas = valor_divida_atual

elif qtdade_parcelas == 3:
    juros = valor_divida * 0.10
    #print(f"{juros:.2f}")
    valor_divida_atual = valor_divida + juros
    #print(f"{valor_divida_atual:.2f}")
    valor_parcelas = valor_divida_atual / 3
    #print(f"{valor_parcelas:.2f}")
elif qtdade_parcelas == 6:
    juros = valor_divida * 0.15
    valor_divida_atual = valor_divida + juros
    valor_parcelas = valor_divida_atual / 6
    #print(valor_parcelas)
elif qtdade_parcelas == 9:
    juros = valor_divida * 0.20
    valor_divida_atual = valor_divida + juros
    valor_parcelas = valor_divida_atual / 9
    #print(valor_parcelas)
elif qtdade_parcelas == 12:
    juros = valor_divida * 0.25
    valor_divida_atual = valor_divida + juros
    valor_parcelas = valor_divida_atual / 12
    #print(valor_parcelas)
else:
    print(" Quantidade de parcelas indisponivel no momento! ")
    
print(f"R$ {valor_divida:.2f} -  {juros:.2f} - {qtdade_parcelas} - R$ {valor_parcelas:.2f} ")