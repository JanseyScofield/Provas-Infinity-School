# Considere uma lista de números inteiros numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Utilizando as funções map(),filter() e reduce(), escreva um código que execute as seguintes operações:
# Função map() para obter uma nova lista com o quadrado de cada número da lista numeros
# Função filter() para obter uma nova lista com números pares da lista numeros
# Função reduce()  para obter a soma de todos os números da lista numeros
# Qual o resultado obtido após a execução das operações acima?

from functools import reduce


def elevar_ao_quadrado(lista : list) -> list:
    """Recebe uma lista com números e eleva todos eles ao quadrado."""
    return list(map(lambda x:  x**2, lista))

def filtrar_pares(lista : list) -> list:
    """Recebe uma lista com números e retorna apenas os pares."""
    return list(filter(lambda x: x % 2 == 0 , lista))

def somar_numeros(lista : list) -> int:
    """Recebe uma lista de números e retorna a soma deles."""
    return reduce(lambda x, y: x+y, lista)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadradosNumeros  = elevar_ao_quadrado(numeros)
print(quadradosNumeros) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

numerosPares  = filtrar_pares(numeros)
print(numerosPares) #[2, 4, 6, 8, 10]

soma = somar_numeros(numeros)
print(soma) #55
