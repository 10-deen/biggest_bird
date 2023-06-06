from BirdBrain import Finch
import random

bird = Finch()

while True:
    bird.setMotors(100, 100)
    
    distance = bird.getDistance()

    if distance < 10:
        bird.setMotors(0, 0)
        bird.setBeak(255, 0, 0)
        
        turn_direction = random.choice(["left", "right"])
        if turn_direction == "left":
            bird.setTurn('L',270, 100)    
        else:
            bird.setTurn('R',90, 100)
            
        bird.setMotors(100, 100)
        
        bird.setBeak(0, 255, 0)  
        bird.setMotors(0, 0)  
        bird.playNote(50, 10) 
        
        bird.setBeak(0, 0, 0)  
