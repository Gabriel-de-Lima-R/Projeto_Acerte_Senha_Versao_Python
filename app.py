import random
import os

# escolhe os 4 números sorteados de 0 a 9
NUMEROS_ESCOLHIDOS = random.sample(range(0, 10), 4)
tentativas = 0

def titulo():
    print("""    
░█████╗░░█████╗░███████╗██████╗░████████╗███████╗  ░█████╗░  ░██████╗███████╗███╗░░██╗██╗░░██╗░█████╗░██╗
██╔══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝  ██╔══██╗  ██╔════╝██╔════╝████╗░██║██║░░██║██╔══██╗██║
███████║██║░░╚═╝█████╗░░██████╔╝░░░██║░░░█████╗░░  ███████║  ╚█████╗░█████╗░░██╔██╗██║███████║███████║██║
██╔══██║██║░░██╗██╔══╝░░██╔══██╗░░░██║░░░██╔══╝░░  ██╔══██║  ░╚═══██╗██╔══╝░░██║╚████║██╔══██║██╔══██║╚═╝
██║░░██║╚█████╔╝███████╗██║░░██║░░░██║░░░███████╗  ██║░░██║  ██████╔╝███████╗██║░╚███║██║░░██║██║░░██║██╗
╚═╝░░╚═╝░╚════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝  ╚═╝░░╚═╝  ╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝""".strip())

def exibir_tela_inicial():
    titulo()
    print("\nBem-Vindos Ao Jogo Acerte A Senha.")
    print("\nO Objetivo Desse Jogo É Descobrir A Senha De 4 Digitos.")
    print("\nO Jogo Funciona Assim:")
    print("""
Suponha Que Nossa Senha Seje [ 1 2 3 4 ]

Se Você Colocar [ 5 6 7 8 ] Vai Aparecer ->> Nenhum Digito Certo.

Se Você Colocar [ 1 6 7 8 ] Vai Aparecer ->> Um Digito Certo.

Se Você Colocar [ 1 2 7 8 ] Vai Aparecer ->> Dois Digitos Certos.

Se Você Colocar [ 1 2 3 8 ] Vai Aparecer ->> Três Digitos Certos. 

Se Você Colocar [ 1 2 3 4 ] Vai Aparecer ->> Parabéns! Você Acertou A Senha.""")
    input("\nPressione ENTER para começar o jogo")
    os.system("cls")


def rodar_programa():
    exibir_tela_inicial()
    print("\nEscolhemos Nossa Senha, Agora Tente Adivinhar!")

if __name__ == '__main__':
    rodar_programa()