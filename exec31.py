"""
31. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios
de 1,99 e agora possui uma loja de conveniências. Faça um programa
que implemente uma caixa registradora rudimentar. O programa deverá 
receber um número desconhecido de valores referentes aos preços das 
mercadorias. Um valor zero deve ser informado pelo operador para 
indicar o final da compra. O programa deve então mostrar o total da 
compra e perguntar o valor em dinheiro que o cliente forneceu, para 
então calcular e mostrar o valor do troco. Após esta operação, 
o programa deverá voltar ao ponto inicial, para registrar a próxima
compra. A saída deve ser conforme o exemplo abaixo:

Lojas Tabajara

- Produto 1: R$ 2.20
- Produto 2: R$ 5.80
- Produto 3: R$ 0
- Total: R$ 9.00
- Dinheiro: R$ 20.00
- Troco: R$ 11.00 """
print(" Mercearia Sr. Manoel Joaquim ")
final_compra = 0
troco = 0
lista = []
valor_a_pagar = 0
total = 0


valor_produto =float(input(" Informe o valor do 1º produto: "))


if valor_produto == 0:
    print(" Compra Finalizada! ")
   
else:
    lista.append(valor_produto)
    i = 2

    while True:
        valor_produto = float(input(f" Informe o valor do {i}º produto : "))
        if valor_produto == 0:
            break
        lista.append(valor_produto)
        i+=1

total = sum(lista)
print(f" Valor Total das Compras: {total:.2f} R$")

dinheiro = float(input(" Valor fornecido: "))
valor_a_pagar = dinheiro - total
print(f"Seu troce é {valor_a_pagar:.2f} R$.")
