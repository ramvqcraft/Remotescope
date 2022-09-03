from time import sleep
import RPi.GPIO as GPIO
import pygame
import sys

EN = 25
DIR = 14
PUL = 15
#delay = 0.01 
#delay = 0.002 #works
Motor_Delay = 0.001#works
#delay = 0.0005#works
#delay = 0.0001#works

####### 2 modules init################################

pygame.init()
display = pygame.display.set_mode((300, 300))


####### 2.1 motor #1
GPIO.setmode(GPIO.BCM)
GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(EN, GPIO.OUT)

GPIO.output(DIR, GPIO.LOW)
GPIO.output(EN, GPIO.HIGH) #not needed

####### 3 Functions #################################

####### 3.1 Motor Rotate
#example Motor1_Rotate(6400,GPIO.LOW,Motor_Delay)

def Motor1_Rotate(Steps, Direction, Delay):
    
    GPIO.output(DIR, Direction)
    
    for s in range(1,Steps):
        
        GPIO.output(PUL, GPIO.HIGH)
        sleep(Delay)
        GPIO.output(PUL, GPIO.LOW)
        sleep(Delay)    


####### 3.5 Motor Control

def KeyControl(KeyLEFT_Status, KeyRIGHT_Status):
    
    print("Debug - KeyControl())"+'(%s'%KeyHold_LEFT+',%s)'%KeyHold_RIGHT)
    
    if (KeyLEFT_Status == True):
        Motor1_Rotate(10,GPIO.LOW,Motor_Delay)
    elif (KeyRIGHT_Status == True):
        Motor1_Rotate(10,GPIO.HIGH,Motor_Delay)


#####################################################

KeyHold_LEFT = False
KeyHold_RIGHT = False


while(1):
    
    # creating a loop to check events that
    # are occurring
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         
        # reading keys status
        if event.type == pygame.KEYDOWN:    
            
               
            if event.key == pygame.K_LEFT:
                #print("Key LEFT has been pressed")
                KeyHold_LEFT = True
               
            if event.key == pygame.K_RIGHT:
                #print("Key RIGHT has been pressed")
                KeyHold_RIGHT = True
              
        else:
            KeyHold_LEFT = False
            KeyHold_RIGHT = False
    
    #executting keys order
    sleep(0.1)
    if (KeyHold_LEFT == True or KeyHold_RIGHT == True):    
        print("Key status (LEFT, RIGHT, UP, DOWN)="+'(%s'%KeyHold_LEFT+',%s)'%KeyHold_RIGHT)
        KeyControl(KeyHold_LEFT,KeyHold_RIGHT)
    
    
    
    
    
    
    