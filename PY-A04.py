#Desenvolva um programa em Python que permita ao usuário digitar várias notas. Em seguida, crie uma função chamada "calcular_media" que irá receber as notas digitadas e 
#calcular a média do aluno. Também crie uma função chamada "verificar_situacao" que, com base na média calculada, irá exibir a situação do aluno: "Reprovado" se a média for
#menor que 7, "Aprovado" se a média for maior ou igual a 7, e "Parabéns, sua média é 10" se a média for igual a 10.

def calcular_media(notas : float) -> float:
    """Recebe uma lista de notas e calcula a média entre elas."""
    somaNotas = sum(notas)
    return somaNotas/len(notas)

def verificar_situacao(media : float) -> str:
    """Recebe um média e retorna um resultado de acordo com o desempenho do aluno."""
    if media  > 7 and media < 10:
        return  f'Aprovado com {media}!'
    elif media ==  10:
        return "Parabéns! Sua média foi 10!"
    return f'Reprovado com {media}.' 

notas = []
iCont = 1

while True:
    while True:    
        try:
            nota = float(input(f"Digite a nota {iCont}: "))
            if nota < 0 or nota > 10:
                raise ValueError
        except Exception:
            print("Valor inválido. Por favor, digite apenas número reais e entre 0 e 10.")
        else:
            break
    
    notas.append(nota)
    
    opcao = input(f"Deseja adicionar a {iCont + 1}º nota? Sim (S) ou não (N)?").upper()
    while opcao != 'S' and opcao !=  "N":
        opcao = input("Opção inválida. Digite novamente: ")
    if opcao == 'N':
        break

    iCont += 1

media = calcular_media(notas)
print(verificar_situacao(media))
