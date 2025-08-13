"""
33. O Departamento Estadual de Meteorologia lhe contratou para 
desenvolver um programa que leia um conjunto indeterminado de 
temperaturas, e informe ao final a menor e a maior temperaturas 
informadas, bem como a média das temperaturas.
"""
import math
celsius = 0
maior_temperatura = ()
menor_temperatura = ()
media_temperatura = ()
lista = []

temperatura = int(input("Quantos dados deseja informar?"))



for i in range(temperatura):
    celsius = float(input(f" Informe a {i+1}ª Temperatura: "))
    lista.append(celsius)
menor_temperatura = min(lista)
maior_temperatura = max(lista)
media_temperatura = (menor_temperatura + maior_temperatura) / 2    
print(f" Tempraturas informadas: {lista}")
print(f" A menor temperatura é: {menor_temperatura}")
print(f" A maior Tempreatura é: {maior_temperatura}")
print(f" Média da Temperatura: {media_temperatura}")
    
    
    
