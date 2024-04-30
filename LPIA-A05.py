# Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina. O programa deve solicitar ao usuário o número de alunos e, em seguida, para cada 
#aluno, pedir o nome e três notas. Utilize um loop 'for' para iterar sobre os alunos e suas notas.Além disso, implemente uma estrutura condicional para verificar se cada aluno foi
#aprovado ou reprovado, considerando que a média mínima para aprovação é 7.0. Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.
# Ao final, exiba a média geral da turma.

qtdAluno = int(input("Digite quantos alunos deseja cadastrar: "))
mediaTotal = 0


for iCont in range(qtdAluno):
    mediaAluno = 0
    nomeAluno = input("Digite o nome do aluno: ")
    for jCont in range(3):
        mediaAluno += float(input(f"Digite a nota da prova {jCont + 1} de {nomeAluno}: "))
    mediaAluno /= 3
    mediaTotal += mediaAluno
    if mediaAluno >= 7.0:
        print(f"{nomeAluno} conseguiu a aprovação com {mediaAluno}!")
    else:
        print(f"{nomeAluno}  não conseguiu a aprovação!")

print(f"A média da turma foi de {mediaAluno/qtdAluno}.")
