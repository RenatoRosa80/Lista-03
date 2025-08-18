"""
45. Desenvolver um programa para verificar a nota do aluno em uma prova com 10 
questões, o programa deve perguntar ao aluno a resposta de cada questão e ao 
final comparar com o gabarito da prova e assim calcular o total de acertos e a
nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema 
deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
Após todos os alunos terem respondido informar:

-Maior e Menor Acerto;
- Total de Alunos que utilizaram o sistema;
- A Média das Notas da Turma.
- Gabarito da Prova:
- 
01 - A

02 - B

03 - C

04 - D

05 - E

06 - E

07 - D

08 - C

09 - B

10 - A

Após concluir isto você poderia incrementar o programa permitindo que o 
professor digite o gabarito da prova antes dos alunos usarem o programa.
"""

# Programa de verificação de nota da prova

# --- Professor digita o gabarito ---
print("===== Cadastro do Gabarito =====")
gabarito = []
for i in range(1, 11):
    resp = input(f"Digite a resposta da questão {i} (A/B/C/D/E): ").strip().upper()
    while resp not in ["A", "B", "C", "D", "E"]:
        resp = input(f"Resposta inválida! Digite novamente a questão {i} (A/B/C/D/E): ").strip().upper()
    gabarito.append(resp)

print("\nGabarito cadastrado com sucesso!\n")

# --- Variáveis de controle ---
maior_acerto = float("-inf")
menor_acerto = float("inf")
soma_notas = 0
total_alunos = 0

# --- Loop para os alunos ---
while True:
    print(f"\n===== Aluno {total_alunos + 1} =====")
    respostas_aluno = []
    for i in range(1, 11):
        resp = input(f"Resposta da questão {i} (A/B/C/D/E): ").strip().upper()
        while resp not in ["A", "B", "C", "D", "E"]:
            resp = input(f"Resposta inválida! Digite novamente a questão {i} (A/B/C/D/E): ").strip().upper()
        respostas_aluno.append(resp)
    
    # Comparação com gabarito
    acertos = 0
    for i in range(10):
        if respostas_aluno[i] == gabarito[i]:
            acertos += 1
    
    print(f"\nVocê acertou {acertos} questões. Nota = {acertos}")

    # Atualizar estatísticas
    if acertos > maior_acerto:
        maior_acerto = acertos
    if acertos < menor_acerto:
        menor_acerto = acertos

    soma_notas += acertos
    total_alunos += 1

    # Perguntar se outro aluno vai responder
    continuar = input("\nOutro aluno vai utilizar o sistema? (S/N): ").strip().upper()
    if continuar == "N":
        break

# --- Resultado final ---
media = soma_notas / total_alunos if total_alunos > 0 else 0

print("\n===== RESULTADO FINAL =====")
print(f"Maior Acerto: {maior_acerto}")
print(f"Menor Acerto: {menor_acerto}")
print(f"Total de Alunos: {total_alunos}")
print(f"Média da Turma: {media:.2f}")
print("Gabarito da Prova:", gabarito)
