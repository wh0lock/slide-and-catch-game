# slide and catch game

A very simple 2D arcade-like game that demonstrates my knowledge of the pygame and simpleGE modules. 

# Overview

The premise is as follows: You are Dave, the sentient dart board. Steve appears near the bottom of the gameplay screen with a background image of a dimly lit hallway to emphasize the “house party game” environment. The player can move Dave left and right with the corresponding arrow keys on their keyboard. A number of darts fall from the top of the screen. Each dart will fall from a different and random x position and speed. If Dave catches a dart, a positive “ding” sound effect will play, and the player will get a point added to their score. If a dart leaves the bottom of the screen, it is reset to a new random position and speed. The game continues for 15 seconds for playtesting purposes but may be extended in the future.
When the game begins, you will see an introduction screen with instructions and two buttons. Clicking the play  button will start the game. The quit button will exit the game. 
Once a player has played a round of darts, they are taken back to the intro screen, and the latest score is passed in as a parameter. The player’s latest score is then displayed in the center of the screen in order to encourage the player to try again. 
 
### State Transition Diagram

*refer to State Transition.pdf*
This is a standard two-state system. It is all that is necessary for such a simple concept. Each state will be represented by a subclass of the simpleGE Scene class. The player is initially shown the Intro scene. Instructions and two buttons will be displayed. The buttons both close the scene, but before doing so, they set a response variable indicating the player’s preference. If the player chooses to play the game, they are sent to the game play scene. If they should choose to quit, the game ends. 

Game play scene always ends when the time expires and always sends the player back to the intro scene. However, it does pass back its score to the main function, which uses the score to provide feedback to the player in the intro scene. 
 
### The Instructions Scene

Controls access to the game.
*refer to Intro GDD.pdf*
This scene has four main visual elements:
•	instructions – stock simpleGE multiLable containing gameplay instructions
•	prevScore – stock label showing previous score
•	playButton – stock button indicating “play”
•	quitButton – stock button indicating “quit”
Other attributes:
•	prevScore – integer indicating the last score; passed into the class initializer and displayed on prevScore label
•	response – string representing user’s intentions; set by two buttons and read in main function 
Initializer will create all attributes and set up the sprite list:
init(score):
	set image to hallway.png
	set response to “play”
	create instructions MultiLabel
	add textLines containing instructions
	set instructions center to (320, 240)
	set instructions size to (500, 250)
	copy score parameter to prevScore attribute
	create LblScore
	set text to “Last score: {prevScore}”
	set center to (320, 400)
	create playButton
	set text to “Play”
	set center to (100, 400)
	create quitButton
	set text to “Quit”
	set center to (100, 400)
	Add lblInstructions, lblScore, quitButton, and playButton to sprites
All event-handling will happen in the scene’s process() method:
process():
	if quit button is pressed:
		response gets “quit”
		stop the scene
	if play button is pressed:
		response gets “play”
		stop the scene

### The Game Class

Primary class of the game. Subclassed from simpleGE.Scene
*refer to GDD.pdf*
Game class will have a number of visual attributes:
•	dave – an instance of the Dave class (below)
•	darts – an instance of the Dart class (below)
•	lblScore – an instance of the LblScore class (below)
•	lblTime – an instance of the LblTime class (below)
It will also contain some non-sprite assets:
•	timer – stock instance of the simpleGE.Timer class
•	score – an int containing the current score
•	dartSound – stock instance of the simpleGE.Sound class

Initializer will create all necessary components:
init:
	set image to hallway.png
	create timer
	set timer’s total time to 15 (temporarily)
	set score to 0
	initialize dartSound to dart sound effect
	create instance of Dave -> dave
	create list of (15) Dart instances -> darts
	create instance of lblScore
	create instance of lblTime
	add dave, coins, lblScore, lblTime to sprites
All event-handling will occur in the scene’s process method():
process:
	for each dart in the darts list:
		if that dart collides with dave:
			play the dart collision sound (dartSound)
			reset that arrow
			add one to score
			update lblScore to indicate new score
	update lblTimer with the current time left
	if time left is less than zero:
		print the score to console
		stop the game
 
### Components of the Game class

Each of the visual elements of the Game class is an extension of a simpleGE element.
**Dave**
	Dave is a subclass of simpleGE.Sprite
	The image is a fair use dart board
	Size should be 50x50
	Transparent background preferably
	Initial position center bottom of screen
	moveSpeed attribute is an integer, starts at 5
	init:
		set image to target.png
		set size to 50x50
		set position to (320, 400)
		set moveSpeed to 5
	All event-handling will be in process() method:
	left on left arrow key, right on right arrow key
	process:
		if left key is pressed
			subtract moveSpeed from x
		if right key is pressed
			add moveSpeed to x
**Dart**
	Dart is a subclass of simpleGE.Sprite
	Image should is a fair use dart
	Transparent background preferably
	Reset method sets dart to top of screen, random position
	Fall speed is random within limits (3 to 8 ppf for now)
	Dart falls down screen
	If dart leaves bottom of screen, reset
	Dart-dave collision handled at game level
	Dart has no special attributes, but three methods
•	init() – standard initialization
•	reset() – custom method to set speed and position
•	checkBounds() – overwrite existing checkBounds to handle bottom of screen
init():
	set image to dart.png
	set size to 25x25
	call reset()
reset():
	set y to 10
	set x to random from zero to screen width
	set dy to random between 3 and 8
checkBounds():
	if bottom of sprite is larger than screen width:
		call reset()
lblScore
	lblScore is a subclass of the simpleGE.Label
	text and center, no events
	init():
		set text to “Score: 0”
		set center to “100, 30”
lblTime
	lblTime is a subclass of simpleGE.Label
	text and center, no events
	init():
		set text to “Time Left: 15”
		set center to (500, 30)

### The main() function

The main() function will manage the state transition between intro and play states.
Standard main loop, containing four variables:
•	instructions – an instance of the Instructions class
•	game – an instance of the Game class
•	keepGoing – our favorite Boolean sentry
•	score – the current score
main():
	set keepGoing to true
	set score to 0
	while keepGoing is true:
		create an instance of Instructions -> instructions
		pass the current score to instructions as a parameter
		start instructions
		when instructions ends, 
		if instructions.repsponse is “play”:
			create an instance of Game -> game
			start game
			when game is over, copy game.score to score
		else:
			set keepGoing to False (exiting game)
 
### Milestone Plan

Strategy is to create gameplay first, then instructions screen, and finally integrate state management. Game process will be stored on GitHub, with a marked commit for each milestone reached and multiple other commits as needed. Each milestone commit will run correctly with the milestone demonstrated. Each milestone is expected to take one programming session to complete. 
1.	Game scene with background image 
2.	Add basic Dave sprite
3.	Add keyboard motion to Dave
4.	Add single dart with reset, falling and boundary behaviors
5.	Add collision effect between dave and dart, sound effect
6.	Modify for multiple (ten) darts including collision behavior
7.	Add scorekeeping, time, and appropriate labels
8.	Add instructions class and state transition

#### Asset Plan

hallway.jpg: Creative commons from https://opengameart.org/content/hallway-daynight-background-for-visual-novels 
target.png: Creative commons from https://opengameart.org/content/xbullet 
Dart.png: Creative commons from https://opengameart.org/content/arrow-1 
ding_2.wav: Creative commons from https://opengameart.org/content/dings 

