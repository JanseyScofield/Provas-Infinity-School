# [LPIA-A03]Você está criando um programa em Python para simular um jogo simples de adivinhação. O programa deve gerar um número aleatório entre 1 e 10 e pedir ao jogador para 
#adivinhar o número. O jogador terá até 3 tentativas para acertar. Implemente o jogo utilizando um loop 'while' para permitir que o jogador faça múltiplas tentativas até 
#acertar ou atingir o limite de tentativas. Utilize a estrutura 'else' para exibir uma mensagem de encorajamento caso o jogador acerte e uma mensagem de consolo caso as 
#3 tentativas se esgotem sem sucesso.

import random

numSecreto = random.randint(1,10)
tentativas = 3
chute = 0

while tentativas > 0:
    chute = int(input(f"Chute um número de 1 a 10 para acertar o númerosecreto. Você tem {tentativas} tentativas: "))
    if (chute != numSecreto):
        print("Ainda não acertou!")
    else:
        print(f"Parabéns! Você acertou o número secreto!")
        break
    tentativas -= 1
else:
        print(f"Você perdeu! O número secreto era {numSecreto}.")
