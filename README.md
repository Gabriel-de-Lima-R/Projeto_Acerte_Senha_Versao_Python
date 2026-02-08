# 🔢 Acerte a Senha!

Um jogo de lógica e adivinhação desenvolvido em Python, onde o desafio é descobrir uma sequência numérica oculta gerada aleatoriamente pelo computador.

## 🎮 Como Funciona o Jogo

O computador escolhe **4 números distintos** entre 0 e 9. O seu objetivo é adivinhar a sequência correta na ordem exata.

A cada tentativa, o programa fornece uma dica baseada nos seus acertos:
- **Nenhum Dígito Certo:** Você não acertou nenhum número na posição correta.
- **Um/Dois/Três Dígito(s) Certo(s):** Indica quantos números você colocou na posição exata da senha secreta.
- **Parabéns!:** Você acertou todos os 4 dígitos e venceu o jogo!

### 💡 Exemplo de Lógica
Se a senha for `[1 2 3 4]` e você digitar `[1 6 7 8]`, o sistema retornará: `->> Um Dígito Certo`, pois apenas o número **1** está na posição correta.

## 🛠️ Tecnologias e Conceitos Utilizados

* **Python 3**: Linguagem base.
* **Módulo `random`**: Para gerar a senha aleatória sem repetição (`random.sample`).
* **Módulo `os`**: Para limpar o terminal e manter a interface organizada.
* **Manipulação de String/Cursor**: Uso de sequências de escape ANSI (`\033[A`) para formatar as respostas na frente do input do usuário.
* **Arte ASCII**: Para criar telas de título e vitória estilizadas.

## 🚀 Como Jogar

1.  **Certifique-se de ter o Python instalado.**
2.  **Baixe o arquivo** `seu_arquivo.py`.
3.  **Abra o terminal ou prompt de comando** e navegue até a pasta do arquivo.
4.  **Execute o comando:**
    ```bash
    python seu_arquivo.py
    ```

## 📂 Estrutura do Código

O código foi dividido em funções para facilitar a leitura:
- `titulo()`: Exibe o banner principal em arte ASCII.
- `exibir_tela_inicial()`: Mostra as instruções e regras do jogo.
- `fim_por_acerto()`: Exibe a tela de vitória e o contador de tentativas.
- `rodar_programa()`: Gerencia o loop principal, valida o input e calcula os acertos.


## 📝 Observações Técnicas

O jogo possui uma validação de entrada que garante que o usuário digite apenas **4 dígitos**. Caso o usuário tente uma quantidade diferente, o sistema emitirá um alerta visual sem interromper a partida.

**Divirta-se tentando bater o recorde de menor número de tentativas!** 🏆
