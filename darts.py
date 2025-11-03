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
        self.text = "Time Left: 30"
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
        self.timer.totalTime = 30 
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

class Introduction(simpleGE.Scene):
    def __init__(self, previousScore):
        super().__init__()

        self.previousScore = previousScore

        self.setImage("hallway.png")
        self.response = "QUIT"

        self.instructions = simpleGE.MultiLabel()
        self.instructions.textLines = [
        "You are a sentient dart board.",
        "Darts are falling from the sky.",
        "You must catch them with",
        "the left and right arrow keys",
        "in order to win back your honor and",
        "become the Lord of Dart Boards",
        "before time runs out."]

        myFont = pygame.font.Font("Jersey10-Regular.ttf", 25)

        self.instructions.center = (320, 200)
        self.instructions.size = (500, 290)
        self.instructions.font = myFont
        self.instructions.bgColor = "cornflowerblue"

        self.playButton = simpleGE.Button()
        self.playButton.text = "PLAY"
        self.playButton.center = (100, 410)
        self.playButton.font = myFont
        self.playButton.bgColor = "cornflowerblue"

        self.quitButton = simpleGE.Button()
        self.quitButton.text = "QUIT"
        self.quitButton.center = (540, 410)
        self.quitButton.font = myFont
        self.quitButton.bgColor = "cornflowerblue"

        self.lblScore = simpleGE.Label()
        self.lblScore.text = "LAST SCORE: 0"
        self.lblScore.center = (320, 410)
        self.lblScore.font = myFont
        self.lblScore.bgColor = "cornflowerblue"
        self.lblScore.fgColor = "black" 

        self.lblScore.text = f"LAST SCORE: {self.previousScore}"

        self.sprites = [self.instructions,
                        self.playButton,
                        self.quitButton,
                        self.lblScore]
        
    def process(self):
        if self.playButton.clicked:
            self.response = "PLAY"
            self.stop()
        if self.quitButton.clicked:
            self.response = "QUIT"
            self.stop()

def main():
    keepGoing = True
    lastScore = 0 

    while keepGoing:
        introduction = Introduction(lastScore)
        introduction.start()

        if introduction.response == "PLAY":
            game = Game()
            game.start()
            lastScore = game.score
        else:
            keepGoing = False

if __name__ == "__main__":
    main()