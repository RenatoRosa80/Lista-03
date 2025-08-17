"""
# 38. Um funcionário de uma empresa recebe aumento salarial anualmente: 
# Sabe-se que:

# - Esse funcionário foi contratado em 1995, com salário inicial 
# de R$ 1.000,00;
# - Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# - A partir de 1997 (inclusive), os aumentos salariais sempre 
# correspondem ao dobro do percentual do ano anterior. Faça um programa 
# que determine o salário atual desse funcionário. Após concluir isto, 
# altere o programa permitindo que o usuário digite o salário inicial do 
# funcionário.
# """

salario_inicial = float(input("\nDigite o salário inicial do funcionário: "))
salario = salario_inicial
percentual = 1.5
reajuste_salarial = 0
aumento_salarial = 0

salario *= (1 + percentual / 100)
print(f"Ano 1996: aumento de {percentual:.2f}%,\n salário = R$ {salario:.2f}")


for ano in range( 1997,2025,):
    percentual *= 2  # Dobra o percentual a cada ano
    salario *= (1 + percentual / 100)
    print(f"Ano {ano}: aumento de {percentual:.2f}%,\n salário = R$ {salario:.2f}")
    

       
    print(f"\nSalário em 2025 =\n R$ {salario:.2f}")






