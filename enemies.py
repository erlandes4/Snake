import random
import Constant
from Entity import Entity

class enemies(Entity):
    # 1. Construtor (O que acontece quando o inimigo nasce)
    def __init__(self, canvas):
        super().__init__(canvas)
        self.enemy = None
        self.tamanho = 20
        self.create_enemies()     # Desenha o inimigo na tela
        self.move_randomly()      # Inicia o ciclo de movimento automático
        
    # 2. Criação do Inimigo
    def create_enemies(self):
        x = random.randrange(0, Constant.Largura, self.tamanho)
        y = random.randrange(0, Constant.Altura, self.tamanho)    
        
        self.enemy = self.canvas.create_rectangle(
            x, y, x + self.tamanho, y + self.tamanho,
            fill="red",           
            tag="enemies"         
        )
        self.segments.append(self.enemy) # Guarda na lista herdada de Entity
        
    def move_randomly(self):
        # 1. Lista com as 4 direções possíveis
        direcoes = [
            (0, -self.tamanho),  # Cima
            (0, self.tamanho),   # Baixo
            (-self.tamanho, 0),  # Esquerda
            (self.tamanho, 0)    # Direita  
        ]
        
        dx, dy = random.choice(direcoes)
        
        # CORREÇÃO 1: Removido o '=' para o print funcionar de verdade
        print(f"Movimento sorteado: dx={dx}, dy={dy}")  
        
        # Como o inimigo guarda apenas 1 elemento em segments, o índice é 0
        new_dx, new_dy = self.restringe_move(dx, dy, 0)  
        
        # CORREÇÃO 2: Move apenas ESTE inimigo específico usando self.enemy
        # (Em vez de "enemies", que moveria todos os inimigos juntos)
        self.canvas.move(self.enemy, new_dx, new_dy)
        
        # 3. Agenda o próximo movimento (aumentei para 500ms para o inimigo não voar pela tela, ajuste se quiser)
        self.canvas.after(500, self.move_randomly)