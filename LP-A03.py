# Escreva um programa em python que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade 
#de números digitados, assim como a soma e a média aritmética.

qtdNum = 0
soma = 0

while True:
    num = int(input("Digite números inteiros (digite 0 para encerrar): "))
    if num == 0:
        break
    soma += num
    qtdNum += 1
media = float(soma)/qtdNum
print(f"A quatidade de números foi de {qtdNum}, a soma deles resultou em {soma} e a média deles ficou {media}")
    
