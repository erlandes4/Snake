import random
import Constant
import snake
from Entity import Entity

class enemies(Entity):
    # 1. Construtor (O que acontece quando o inimigo nasce)
    def __init__(self, canvas):
        super().__init__(canvas)
        self.enemy = None
        self.create_enemies()     # Chama a função que desenha o inimigo na tela
        self.move_randomly()      # Inicia o ciclo de movimento assim que o inimigo nasc  
        
             
    # 2. Criação do Inimigo
    def create_enemies(self):

        self.tamanho = 20 # Define o tamanho do inimigo (Atenção a esse valor!)
       # 2. randrange sorteia um número de 0 até a Largura, mas pulando de 20 em 20 (0, 20, 40, 60...)
        x = random.randrange(0, Constant.Largura, self.tamanho)
        y = random.randrange(0, Constant.Altura, self.tamanho)     # Posição onde o inimigo vai nascer (100 pixels para direita, 100 para baixo)   
        self.enemy = self.canvas.create_rectangle(
            x, y, x + self.tamanho, y + self.tamanho,
            fill="red",           # Pinta o quadrado de vermelho
            tag="enemies"         # Dá a etiqueta "enemies" para podermos movê-lo ou apagá-lo depois
        )
        self.segments.append(self.enemy)# Guarda a referência desse inimigo na lista de segmentos
        
        
    def move_randomly(self):
            # 1. Lista com as 4 direções possíveis (dx, dy)
        direcoes = [
            (0, -self.tamanho),  # Cima (Y diminui)
            (0, self.tamanho),   # Baixo (Y aumenta)
            (-self.tamanho, 0),  # Esquerda (X diminui)
            (self.tamanho, 0)    # Direita (X aumenta)  
        ]
        #2. Sorteia uma das direções da lista
        
        dx, dy = random.choice(direcoes)
        print = (f"Movimento sorteado: dx={dx}, dy={dy}")  # Debug: Mostra o movimento sorteado no console
        ind_enemy = self.segments.index(self.enemy)
        new_dx, new_dy = self.restringe_move(dx, dy, ind_enemy)  # Chama a função para garantir que o inimigo não saia da tela
        
        # 3. Move o inimigo no Canvas
        self.canvas.move("enemies", new_dx, new_dy)
        
        # 4. Recursivamente chama esta função de novo após 500 milissegundos (meio segundo)
        self.canvas.after(100, self.loop, dx, dy)   #after == espera um pouco e roda essa parada.    
        
        
    def loop(self,dx, dy):
        print (f"Movimento sorteado: dx={dx}, dy={dy}")  # Debug: Mostra o movimento sorteado no console
        self.move_randomly()