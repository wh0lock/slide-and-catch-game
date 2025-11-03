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

class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (75, 30)
        self.clearBack = True 
        self.fgColor = "white"
        
        pygame.font.init()
        myFont = pygame.font.Font("Jersey10-Regular.ttf", 25) 
        self.font = myFont
        
class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time Left: 15"
        self.center = (550, 30)
        self.clearBack = True
        self.fgColor = "white"

        pygame.font.init()
        myFont = pygame.font.Font("Jersey10-Regular.ttf", 25)
        self.font = myFont

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("hallway.png")

        self.dartSound = simpleGE.Sound("ding_2.wav")
        self.numDarts = 10
        
        self.score = 0
        self.lblScore = LblScore()

        self.timer = simpleGE.Timer()
        self.timer.totalTime = 15 
        self.lblTime = LblTime()

        self.dave = Dave(self)
        self.darts = []
        for i in range(self.numDarts):
            self.darts.append(dart(self))
        self.sprites = [self.dave,
                        self.darts,
                        self.lblScore,
                        self.lblTime]
        
    def process(self):
        for dart in self.darts:
            if dart.collidesWith(self.dave):
                dart.reset()
                self.dartSound.play()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Score: {self.score}")
            self.stop()

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()