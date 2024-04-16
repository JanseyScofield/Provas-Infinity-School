# [LPIA-A04] Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo determinado pelo usuário. O programa deve solicitar ao usuário que insira dois números inteiros, representando o início e o fim do intervalo (inclusive).Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares. Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares no intervalo, caso seja o caso.
# Ao final, exiba a soma dos números pares encontrados.

inicio = int(input("Digite o número que começar o intervalo: "))
fim = int(input("Digite o número para terminar o intervalo: "))
somaPar = 0

for iCont in range(inicio, fim+1):
    if iCont % 2 == 0:
        somaPar += iCont

if somaPar > 0:
    print(f"O resultado da soma dos número pares no intervalo de {inicio} a {fim} é igual a {somaPar}.")
else:
    print("Não houve número pares no intervalo de {incio} a {fim}.")
