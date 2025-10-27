import pygame, simpleGE, random

""" darts.py
    slide and catch demo
    Emily Adams
"""
class dart(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Dart.png")
        self.setSize(20, 75)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()

    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(self.minSpeed, self.maxSpeed)

    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()

class Dave(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("target.png")
        self.setSize(50, 50)
        self.position = (320, 400)
        self.moveSpeed = 5

    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("hallway.png")
        self.dave = Dave(self)
        self.dart = dart(self)
        self.sprites = [self.dave,
                        self.dart]

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()