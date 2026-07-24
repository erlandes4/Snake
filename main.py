import tkinter as tk
import Constant

class Game(object):
    def __init__ (self):
        self.root = tk.Tk() #Janela Principal.
        self.root.title("Olha a Cobra")
        self.root.geometry = f"{Constant.Largura}x{Constant.Altura}"
        self.canvas = tk.Canvas(
            self.root,
            width=Constant.Canvas_L, 
            height=Constant.Canvas_A, 
            bg="black"
        )
        self.canvas.pack(pady=20)
        self.snake = Snake(self.canvas)
        self.root.bind("<KeyPress>", self.snake.move)
    
    def run(self):
        self.root.mainloop()
                
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
#class enemies(object):
#class food(object):

if __name__ == "__main__":
    game = Game()
    game.run()
