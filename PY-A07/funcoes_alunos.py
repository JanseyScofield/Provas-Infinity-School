from alunos_model import dicionario_alunos

def validar_num_matricula_nova() -> str:
    """Essa função valida se a matrícula é nova."""
    nova_matricula = input("Digite o número da nova matrícula: ")
    while True:
        matricula_existente = False
        for num_matricula in dicionario_alunos["matricula"]:
            if num_matricula == nova_matricula:
                matricula_existente = True
                break
        if matricula_existente:
            nova_matricula = input("Matrícula existente. Digite outra: ")
        else:
            return nova_matricula 


def validar_num_matricula_existente() -> int:
    """Essa função valida se a matrícula existe."""
    while True:
        try:
            num_matricula = input("Digite o número de matrícula desejado: ")
            index = dicionario_alunos["matricula"].index(num_matricula)
        except Exception:
            print("Valor de matrícula não existe. Digite um existente.")
        else:            
            return index

def ver_alunos() -> None:
    """Essa função mostra todos os alunos cadastrados."""
    if len(dicionario_alunos["matricula"]) == 0:
        print("Ainda não há alunos cadastrados.")
    else:
        print("------------------------------------------------------------------")   
        for iCont in range(len(dicionario_alunos["nome"])):
            print(f"Nome: {dicionario_alunos["nome"][iCont]}")
            print(f"Número de matrícula: {dicionario_alunos["matricula"][iCont]}")
            print("------------------------------------------------------------------")   

def adicionar_aluno() -> None:
    """Essa função adiciona um aluno no dicionário de alunos."""
    nome_aluno = input("Digite o nome do(a) novo(a) aluno(a): ")
    num_matricula = validar_num_matricula_nova()
    dicionario_alunos["nome"].append(nome_aluno) 
    dicionario_alunos["matricula"].append(num_matricula) 

def atulizar_aluno() -> None:
    """Essa função atualiza o nome do aluno pelo número de matrícula."""
    index = validar_num_matricula_existente()
    novo_nome = input("Qual será o novo nome? ")
    dicionario_alunos["nome"][index] = novo_nome

def remover_aluno() -> None:
    """Essa função remove um aluno pelo número de matrícula."""
    index = validar_num_matricula_existente()
    del dicionario_alunos["nome"][index]
    del dicionario_alunos["matricula"][index]
 