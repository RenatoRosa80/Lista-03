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

def main():
    # Gabarito da prova
    gabarito = ["A", "B", "C", "D", "E", "E", "D", "C", "B", "A"]

    notas = []  # Lista para armazenar as notas dos alunos
    continuar = "S"

    while continuar.upper() == "S":
        print("\n--- Respostas do aluno ---")
        acertos = 0

        # Pergunta as 10 questões
        for i in range(10):
            resposta = input(f"Digite a resposta da questão {i+1}: ").strip().upper()
            if resposta == gabarito[i]:
                acertos += 1

        notas.append(acertos)
        print(f"Você acertou {acertos} de 10 questões. Nota = {acertos}")

        # Pergunta se outro aluno vai usar o sistema
        continuar = input("\nOutro aluno vai utilizar o sistema? (S/N): ")

    # Após todos os alunos responderem:
    if notas:
        maior_acerto = max(notas)
        menor_acerto = min(notas)
        total_alunos = len(notas)
        media = sum(notas) / total_alunos

        print("\n=== RESULTADOS FINAIS ===")
        print(f"Maior acerto: {maior_acerto}")
        print(f"Menor acerto: {menor_acerto}")
        print(f"Total de alunos: {total_alunos}")
        print(f"Média da turma: {media:.2f}")
    else:
        print("\nNenhum aluno respondeu à prova.")


# Executa o programa
if __name__ == "__main__":
    main()
