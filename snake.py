class Snake(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.segments = []
        self.create_snake()

    def create_snake(self):
            x, y = 100, 100
            tamanho = 20
            head = self.canvas.create_rectangle(
            x, y, x + tamanho, y + tamanho, 
            fill="green", tag="snake"
        )
            self.segments.append(head)
    def move(self, event):
        tamanho = 20
        dx, dy = 0, 0
        if event.keysym == "Up":
            dy = -tamanho
        elif event.keysym == "Down":
            dy = tamanho
        elif event.keysym == "Left":
            dx = -tamanho
        elif event.keysym == "Right":
            dx = tamanho

        self.canvas.move("snake", dx, dy)


