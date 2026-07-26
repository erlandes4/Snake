class Entity: #Definiçãoes padrões para todos os objetos do jogo (Cobra, Inimigos, etc)
    def __init__(self, canvas):
        self.canvas = canvas
        self.segments = []

    def restringe_move(self, dx, dy, ind_segmento=0):
            cabeca = self.segments[ind_segmento]  # Pega a parte especificada (a cabeça por padrão)
            x1, y1, x2, y2 = self.canvas.coords(cabeca)  # Pega as coordenadas da cabeça (topo-esquerdo e fundo-direito)
        
            #Pegamos a largura e altura REAIS do quadro negro
            largura_real = self.canvas.winfo_width()
            altura_real = self.canvas.winfo_height()
            
            # Verifica se a cabeça saiu da tela (fora dos limites do canvas)
            bateu_cima = y1 <= 0
            bateu_esquerda = x1 <= 0
            bateu_direita = x2 >= largura_real
            bateu_baixo = y2 >= altura_real
            
            if bateu_cima and dy < 0:
                dy = 0  
            elif bateu_baixo and dy > 0:
                dy = 0
            elif bateu_esquerda and dx < 0:
                dx = 0
            elif bateu_direita and dx > 0:
                dx = 0
                
            return dx, dy  # Retorna os valores de dx e dy para serem usados no movimento