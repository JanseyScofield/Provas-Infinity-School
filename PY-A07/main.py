import funcoes_alunos as fa

opcoes = {
    1 : fa.ver_alunos,
    2 : fa.adicionar_aluno,
    3: fa.atulizar_aluno,
    4: fa.remover_aluno
}

print("---------------Sistemas de Alunos---------------")
while True:
    print("""          1 - Ver alunos;
          2 - Adicionar aluno(a);
          3 - Atualizar aluno(a);
          4 - Remover aluno(a);
          5 - Sair.""")
    while True:
        try:
            escolha = int(input("Digite a opção desejada:"))
            if escolha < 1 or escolha > 5:
                raise ValueError
        except Exception:
            print("Opção inválida. Tente novamente.")
        else:
            if escolha == 5:
                print("Obrigado! Até breve!")
                exit()
            break
    opcoes[escolha]()