import random
import os

# escolhe os 4 números sorteados de 0 a 9
NUMEROS_ESCOLHIDOS = random.sample(range(0, 10), 4)
tentativas = 0

def titulo():
    os.system("cls")
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
    input("\nPressione ENTER para começar o jogo ")
    os.system("cls")

def fim_por_acerto():
    os.system("cls")
    print("""
██████╗░░█████╗░██████╗░░█████╗░██████╗░███████╗███╗░░██╗░██████╗██╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝████╗░██║██╔════╝██║
██████╔╝███████║██████╔╝███████║██████╦╝█████╗░░██╔██╗██║╚█████╗░██║
██╔═══╝░██╔══██║██╔══██╗██╔══██║██╔══██╗██╔══╝░░██║╚████║░╚═══██╗╚═╝
██║░░░░░██║░░██║██║░░██║██║░░██║██████╦╝███████╗██║░╚███║██████╔╝██╗
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝""")
    print("\nParabéns! Você Acertou A Senha ->> ", *NUMEROS_ESCOLHIDOS, sep="")
    print(f"\nE Levou {tentativas} tentativa(s) para acertar!\n")

def rodar_programa():
    global tentativas
    exibir_tela_inicial()
    print("\nEscolhemos Nossa Senha, Agora Tente Adivinhar!")
    while True:
        senha_chutada = input("\nQual Senha Você Acha Que Escolhemos: ")
        print("\033[A\033[42C", end="") # O cursor sobe uma linha e anda 42 colunas
        if len(senha_chutada) == 4:
            acertos = sum(1 for i in range(4) if int(senha_chutada[i]) == NUMEROS_ESCOLHIDOS[i])
            tentativas += 1
            if acertos == 0:
                print("->> Nenhum Digito Certo.")
            elif acertos == 1:
                print("->> Um Digito Certo.")
            elif acertos == 2:
                print("->> Dois Digitos Certos.")
            elif acertos == 3:
                print("->> Três Digitos Certos.")
            else:
                fim_por_acerto()
                break
        else:
            print("\n\033[37C", end="")
            print("└──>> Só 4 Dígitos! Tente Novamente.")

if __name__ == '__main__':
    rodar_programa()