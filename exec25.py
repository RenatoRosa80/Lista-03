"""
25. Faça um programa que peça para n pessoas a sua idade, 
ao final o programa devera verificar se a média de idade da turma 
varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma 
é jovem, adulta ou idosa, conforme a média calculada.
"""
import math
soma = 0
idade_media = 0
lista = []
qtde_pessoas = int(input(" Quantas pessoas deseja informar a Idade? "))

while True:
    for i in range (0, qtde_pessoas):
        idade = int(input(f" Digite a {i + 1}º idade:"))
        lista.append(idade)
        idade_media = sum(lista) / qtde_pessoas
        
    break
print(f" As idades sao: {lista}")
print(f" A idade Média é {idade_media}")

if idade_media >= 0 and idade_media <= 25:
    print(" A Turma é Jovem! ")
    print("""     
      __( )_                
     (      (o____
      |          |          
      |      (__/            
        \     /   ___        
        /     \  \___/
      /    ^    /     \
     |   |  |__|_HUNNY |
     |    \______)____/
      \         //
        \     //_
         |  ( __)
         (____) 
         """)
elif idade_media >= 26 and idade_media <= 60:
    print(" A Turma é Adulta! ")
    print("""                  
    .-.-.=\-.
    (_)=='(_)        
          """)
else:
    print(" A Turma é Idosa! ")
    print("""         
                      '-.               .-'
_______________'-._________.-'______________
'-.           _    '-. .-'   _           .-'
   '-.       (_)  /      \  (_)       .-'
      '-.        /        \        .-'
         '-.____/          \____.-'
                \_ _ _ _ _ /
            //////////\\\\\\\\\
           ///////////\\\\\\\\\\
          |||| .-----------._||||
          |||| '-|___|___|-' ||||
          \\\\  '---------'  ////
            \\\|||||||||||||///
              \\\\\\\\///////
                \\\\\\///// """)


    
