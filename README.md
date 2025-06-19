# Junk Attack

## 👤 Desenvolvedor
**Nome:** Luiza Eduarda Luza Neckel 
**RA:** 1137716

## Testador do jogo
**Nome:** Vinicius Hoffelder Colussi
**RA:** 137833

## 🎮 Sobre o jogo
**Junk Attack** é um jogo desenvolvido como parte do curso de Ciência da Computação, com o objetivo de testar e aplicar, de forma lúdica, os conhecimentos adquiridos em Python durante a disciplina. No jogo, o personagem precisa comer apenas comidas saudáveis que caem do céu. A cada alimento saudável ingerido, ele ganha pontos. Já ao comer alimentos não saudáveis, ele perde uma vida e vai ganhando peso — visualmente refletido no personagem. O jogador começa com 3 vidas e precisa acumular a maior pontuação possível antes que acabem.

## 🛠️ Tecnologias utilizadas

- **Python 3.10+**  
  Linguagem de programação principal utilizada para o desenvolvimento de toda a lógica do jogo, manipulação de eventos, estruturas condicionais, controle de fluxo e integração com bibliotecas externas.
- **Pygame**  
  Biblioteca utilizada para criar jogos em 2D com Python. Responsável por:
  - Renderização de imagens e sprites na tela;
  - Detecção de colisões;
  - Controle de animações e movimentação;
  - Manipulação de eventos do teclado e mouse;
  - Execução de efeitos sonoros e música de fundo.
- **Tkinter**  
  Biblioteca nativa do Python usada para criar janelas gráficas. Neste projeto, foi utilizada para exibir uma janela inicial de entrada, onde o jogador informa seu nome por texto ou por voz.
- **Bibliotecas auxiliares personalizadas (`utils.py`)**  
  Arquivo próprio criado para centralizar funções auxiliares, como pausas entre eventos (`aguarde()`), comandos de voz (`ouvir()`), registro de partidas (`salvar_partida()`), e exibição de logs das últimas partidas.
- **Assets externos (imagens e sons)**  
  - Imagens no formato `.png` para representar personagens, comidas, fundo, botões, entre outros;
  - Arquivos de áudio `.mp3` e `.wav` para trilha sonora, efeitos de interação, e feedbacks sonoros.
