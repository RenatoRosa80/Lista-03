"""
44. Faça um programa que leia o código dos itens pedidos e as quantidades
desejadas e o valor dos itens. Calcule e mostre o valor a ser pago por item (preço * quantidade)
e o total geral do pedido. Considere que o cliente deve informar quando o 
pedido deve ser encerrado."""


valor_total_item = 0
valor_a_ser_pago = 0
valor_item = 0

valor_a_ser_pago = 0
while True:
    codigo_item = int(input(" Código do item: "))
    quantidade = int(input(" Qual a quantidade do item? "))
    valor_item = float(input(" Valor do item: "))
    valor_total_item = valor_item * quantidade
    print(f" Valor total do item {codigo_item}: R$ {valor_total_item} ")
    valor_a_ser_pago += valor_total_item

    
    finalizar = int(input(" Mais algum item - Informe 1 - para continuar ou 2 - para finalizar? "))

    if finalizar == 2:
        
        break

print(f" Valor Total da sua compra é R$ {valor_a_ser_pago:.2f} ")
print(" Obrigado e volte sempre! ")
        

    
   
