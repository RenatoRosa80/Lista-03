"""
3.	Faça um programa que leia e valide as seguintes informações:
⦁	Nome: maior que 3 caracteres;
⦁	Idade: entre 0 e 150;
⦁	Salário: maior que zero;
⦁	Sexo: 'f' ou 'm';
⦁	Estado Civil: 's', 'c', 'v', 'd';

"""

while True:
    sexo = input("Digite seu sexo (f/m): ").strip().lower()
    if sexo in ['f', 'm']:
        break
    else:
        print("Sexo deve ser 'f' ou 'm'.")


while True:
      
    sexo = input("Digite seu sexo (f) ou (m): ").lower().strip()

    if sexo == "f":
          sexo_formatado = "feminino"
          print("Sexo: feminino")
          break
      
    elif sexo == "m":
          sexo_formatado = "masculino"
          print("Sexo: masculino")
          break        
    else:
          print("Digite (F) para feminino e (M) para masculino")   


sexo = input('Digite o sexo [f/m] ')
sexo.lower() 
while sexo != 'f' and sexo != 'm':
    print('Sexo inválido! Redigite o sexo')
    sexo = input('Digite seu sexo [f/m]').lower().strip()