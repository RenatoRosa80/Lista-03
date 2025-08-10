# 10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input(" Informe um número inteiro:"))
num2 = int(input(" Informe um segundo número inteiro:"))

for i in range(num1 + 1, num2 ):
    print(i, end= " ")
"""
range(início, fim) gera uma sequência de números começando em início 
e parando antes de fim.

Aqui o início é num1 + 1, ou seja, começa logo após o primeiro número
informado.

O fim é num2, mas como o range não inclui o último valor, ele vai até
um antes do segundo número informado.

Assim, o for percorre todos os números entre num1 e num2, excluindo os
dois.
"""
"""i é a variável que assume cada valor do range.

print(i, end=" ") imprime os valores na mesma linha, separados
por um espaço, em vez de pular linha a cada impressão 
(que é o comportamento padrão do print). """