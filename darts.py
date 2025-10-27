import pygame, simpleGE, random

""" darts.py
    slide and catch demo
    Emily Adams
"""

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("hallway.png")
        self.sprites = []

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()