# HEALTH POTION PROGRAM


#Here, I have created a simple little program where we have an imaginary
#Playable character that is in a video game. While playing, the character
#comes across a health potion that will automatically increase his/her health
#The AMOUNT varies based on the difficulty setting of the game.

import random


health = 100

#1 Being EASY, and 3 Being HARD
difficulty = random.randint(1, 3)

potion_health = int(random.randint(25, 50) / difficulty)

health = health + potion_health

print("Current health after consuming health potion: " + str(health) + " HP")
print("The health potion restored: " + str(potion_health) + " HP")
print("Difficulty Level:" + str(difficulty))



