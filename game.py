import tkinter as tk
import Constant
from snake import Snake

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
         

if __name__ == "__main__":
    game = Game()
    game.run()
