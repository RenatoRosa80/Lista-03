"""
4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que
 a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o 
 número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação.

"""
popa = float(input(" Quantos Habitantes são na população A: "))
taxa_a = float(input(" Qual a Taxa de crescimento de A: "))
taxa_a=  3  / 100

popb = float(input(" Quantos Habitantes são na população B: "))
taxa_b = float(input(" Qual a Taxa de crescimento de B: "))
taxa_b =  1.5 / 100
ano = 0

while popa <= popb:
    popa += popa * taxa_a
    popb += popb * taxa_b
    ano += 1
    print(f'Ano {ano} : Pop a = {int(popa)}   , Pop b = {int(popb)}')
print(f'A população A ultrapossou ou igualou B em {ano}')
