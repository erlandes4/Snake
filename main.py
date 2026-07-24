import tkinter as tk
import Constant

class Game(object):
    def __init__ (self):
        self.root = tk.Tk()
        self.root.title("Olha a Cobra")
        self.root.geometry = f"{Constant.Largura}x{Constant.Altura}"
                
#class Snake(object):
#class enemies(object):
#class food(object):

if __name__ == "__main__":
    game = Game()
    game.root.mainloop()
