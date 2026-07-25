import tkinter as tk         # Importa a biblioteca gráfica nativa do Python e a apelida de 'tk'
import Constant              # Importa um arquivo/módulo próprio (provavelmente com as configurações de tamanho)
from snake import Snake      # Importa a classe Snake de um arquivo chamado 'snake.py'
from enemies import enemies  # Importa a classe enemies de um arquivo chamado 'enemies.py'

class Game(object):
    def __init__ (self):
        # 1. Configuração da Janela Principal
        self.root = tk.Tk() # Cria a janela principal do jogo
        self.root.title("Olha a Cobra") # Define o título que aparece no topo da janela

        # Define o tamanho da janela usando variáveis do arquivo Constant
        self.root.geometry = f"{Constant.Largura}x{Constant.Altura}" 
        
        # 2. Configuração da Área de Desenho (Canvas)
        self.canvas = tk.Canvas(
            self.root,                   # Coloca o canvas dentro da janela principal (self.root)
            width=Constant.Canvas_L,     # Largura da área de jogo
            height=Constant.Canvas_A,    # Altura da área de jogo
            bg="black", # Cor de fundo preta
            highlightthickness=0 # Importante: Remove uma borda branca de 2 pixels que o tkinter coloca por padrão                  
        )
        # fill=tk.BOTH -> Diz para o fundo preto preencher tanto a largura (X) quanto a altura (Y)
        # expand=True -> Diz para o fundo preto acompanhar a janela se ela for redimensionada
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # 3. Criação da Cobra e Controles
        self.snake = Snake(self.canvas)  # Cria a cobra e passa o canvas para ela saber onde deve ser desenhada
        
        # Diz ao programa: "Sempre que uma tecla for pressionada (<KeyPress>), chame a função de mover a cobra"
        self.root.bind("<KeyPress>", self.snake.move) 

        self.enemies = [] # Cria os inimigos e passa o canvas para eles saberem onde devem ser desenhados

    def spawnner(self): 
        time_generation_enemies = 0 #variavel de tempo para spawnar o inimigo
        for i in range(10):  # Cria 10 inimigos
            if time_generation_enemies == 0:
                self.enemies.append(enemies(self.canvas))
            else:
                self.canvas.after(time_generation_enemies, self.enemies.append(enemies(self.canvas)))  #Chama a função que cria os inimigos na tela depois de tantos milissegundos
            time_generation_enemies += 100  # Incrementa o tempo de geração dos inimigos
            
    def run(self):
        # Inicia o loop principal do tkinter. É isso que mantém a janela aberta esperando por ações (como cliques ou teclas)
        self.spawnner()
        self.root.mainloop()
        
        
            
# 4. Ponto de Entrada do Programa
if __name__ == "__main__":
    game = Game() # Cria uma instância do jogo
    game.run()    # Roda o jogo