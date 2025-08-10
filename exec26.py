"""
26. Numa eleição existem três candidatos. 
Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de 
cada candidato.
"""
print("-------------------------------------------")
print(" Eleicoes 2025")
print("-------------------------------------------")
candidatos = [" Pateta - 10 ", " Tio Patinhas - 11 ", " Mickey - 12 "]
print(f" Os candidatos a Prefeito sao: {candidatos}")
print(" Para votar basta digitar o número do seu Candidato! ")

pateta = []
tio_patinhas = []
mickey = []
total_eleitores = int(input(" Quantos Eleitores Votantes? "))
eleitor = 0

for i in range(total_eleitores):
    while True:
        try:
            eleitor = int(input(" Digite o Número do seu candidato: "))
            
            if eleitor == 10:
                pateta.append(eleitor)
                break
            elif eleitor == 11:
                tio_patinhas.append(eleitor)
                break
            elif eleitor == 12:
                mickey.append(eleitor)
                break
            else:
                print(" Candidato inexistente! ")
        except ValueError:
            print(" Por favor, digite apenas números! ")

total_pateta = len(pateta)
total_tio_patinhas = len(tio_patinhas)
total_mickey = len(mickey)
        
if total_pateta > total_tio_patinhas and total_pateta > total_mickey:
    print(f"O Candidato vencedor foi Pateta com {total_pateta} Votos Válidos")
elif total_tio_patinhas > total_pateta and total_tio_patinhas > total_mickey:
    print(f"O Candidato vencedor foi Tio Patinhas com {total_tio_patinhas} Votos Válidos")
elif total_mickey > total_pateta and total_mickey > total_tio_patinhas:
    print(f" Mickey foi o Eleito com {total_mickey} votos")
else:
    print(" Votacao Terminada! ")
    
    if total_pateta == total_tio_patinhas == total_mickey:
        print("\nHouve um empate triplo entre todos os candidatos!")
    elif total_pateta == total_tio_patinhas and total_pateta > total_mickey:
        print("\nHouve um empate entre Pateta e Tio Patinhas!")
    elif total_pateta == total_mickey and total_pateta > total_tio_patinhas:
        print("\nHouve um empate entre Pateta e Mickey!")
    elif total_tio_patinhas == total_mickey and total_tio_patinhas > total_pateta:
        print("\nHouve um empate entre Tio Patinhas e Mickey!")
    elif total_pateta > total_tio_patinhas and total_pateta > total_mickey:
        print(f"\nO Candidato vencedor foi Pateta com {total_pateta} votos")
    elif total_tio_patinhas > total_pateta and total_tio_patinhas > total_mickey:
        print(f"\nO Candidato vencedor foi Tio Patinhas com {total_tio_patinhas} votos")
    elif total_mickey > total_pateta and total_mickey > total_tio_patinhas:
        print(f"\nMickey foi o Eleito com {total_mickey} votos")
    else:
        print("\nHouve um Empate!")