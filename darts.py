import pygame, simpleGE, random

""" darts.py
    slide and catch demo
    Emily Adams
"""
class Dave(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("target.png")
        self.setSize(50, 50)
        self.position = (320, 400)

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("hallway.png")
        self.dave = Dave(self)
        
        self.sprites = [self.dave]

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()