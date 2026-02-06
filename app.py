import random

# escolhe os 4 números sorteados de 0 a 9
num_escolhido = random.sample(range(0, 10), 4)
tentativas = 0

def rodar_programa():
    print(num_escolhido)

if __name__ == '__main__':
    rodar_programa()