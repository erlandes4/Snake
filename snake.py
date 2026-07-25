class Snake(object):
    # 1. Construtor (O que acontece quando a cobra nasce)
    def __init__(self, canvas):
        self.canvas = canvas      # Salva a referência da tela de desenho passada pelo arquivo principal
        self.segments = []        # Cria uma lista vazia que vai guardar as partes do corpo da cobra
        self.create_snake()       # Chama a função que desenha a cobra na tela pela primeira vez

    # 2. Criação da Cobra
    def create_snake(self):
        x, y = 100, 100           # Posição inicial da cobra (100 pixels para a direita, 100 para baixo)
        tamanho = 20              # Tamanho do quadrado da cobra (20x20 pixels)
        
        # Desenha um retângulo (quadrado) na tela. 
        # Passa as coordenadas do topo-esquerdo (x, y) e fundo-direito (x+20, y+20)
        head = self.canvas.create_rectangle(
            x, y, x + tamanho, y + tamanho, 
            fill="green",         # Preenche com a cor verde
            tag="snake"           # Dá uma "etiqueta" chamada "snake" para esse desenho
        )
        # Adiciona esse quadrado na lista de partes do corpo
        self.segments.append(head)

    # 3. Lógica de Movimento
    def move(self, event):
        tamanho = 20              # O tamanho do passo é igual ao tamanho da cobra (20 pixels)
        dx, dy = 0, 0             # dx (diferença no eixo X) e dy (diferença no eixo Y) começam zerados
        
        # Verifica o nome da tecla que foi pressionada ('event.keysym')
        if event.keysym == "Up":
            dy = -tamanho         # Se for para Cima, o Y diminui (vai para o topo da tela)
        elif event.keysym == "Down":
            dy = tamanho          # Se for para Baixo, o Y aumenta (vai para o fundo da tela)
        elif event.keysym == "Left":
            dx = -tamanho         # Se for para a Esquerda, o X diminui
        elif event.keysym == "Right":
            dx = tamanho          # Se for para a Direita, o X aumenta

        # Pega TUDO no canvas que tiver a etiqueta "snake" e move dx pixels pro lado e dy pixels pra cima/baixo
        self.canvas.move("snake", dx, dy)