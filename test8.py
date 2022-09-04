from time import sleep
import RPi.GPIO as GPIO
import pygame
import sys

####### 1 variables ###################################

####### 1.1 motor1 pins
EN = 25
DIR = 14
PUL = 15

####### 1.2 motor2 pins
DIR2 = 20
PUL2 = 21

###### delay for steppers
Motor_Delay_LowSpeed = 0.001#works
Motor_Delay_HighSpeed = 0.00001#works

####### 2 modules init################################

pygame.init()
display = pygame.display.set_mode((300, 300))
GPIO.setmode(GPIO.BCM)


####### 2.1 motor #1
GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(EN, GPIO.OUT)

####### 2.2 motor #2
GPIO.setup(PUL2, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)


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

####### 3.2 Motor Rotate
#example Motor2_Rotate(6400,GPIO.LOW,Motor_Delay)

def Motor2_Rotate(Steps, Direction, Delay):
    
    GPIO.output(DIR2, Direction)
    
    for s in range(1,Steps):
        
        GPIO.output(PUL2, GPIO.HIGH)
        sleep(Delay)
        GPIO.output(PUL2, GPIO.LOW)
        sleep(Delay)

####### 3.3 Motor Test
def MotorTest():        
    Motor1_Rotate(500,GPIO.LOW,Motor_Delay_HighSpeed)
    Motor2_Rotate(500,GPIO.LOW,Motor_Delay_HighSpeed) 
 
 
####### 3.5 Motor Control

def KeyControl(KeyLEFT_Status, KeyRIGHT_Status, KeyUP_Status,KeyDOWN_Status,MotorDelay):
    
    print("Debug - KeyControl())"+'(%s'%KeyHold_LEFT+',%s)'%KeyHold_RIGHT+'(%s'%KeyHold_UP+',%s)'%KeyHold_DOWN)
    
    if (KeyLEFT_Status == True):
        Motor1_Rotate(10,GPIO.LOW,MotorDelay)
    elif (KeyRIGHT_Status == True):
        Motor1_Rotate(10,GPIO.HIGH,MotorDelay)

    if (KeyUP_Status == True):
        Motor2_Rotate(10,GPIO.LOW,MotorDelay)
    elif (KeyDOWN_Status == True):
        Motor2_Rotate(10,GPIO.HIGH,MotorDelay)
        

#####################################################




KeyHold_LEFT = False
KeyHold_RIGHT = False
KeyHold_UP = False
KeyHold_DOWN = False

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
  
            if event.key == pygame.K_UP:
                #print("Key LEFT has been pressed")
                KeyHold_UP = True
               
            if event.key == pygame.K_DOWN:
                #print("Key RIGHT has been pressed")
                KeyHold_DOWN = True  
  
  
        else:
            KeyHold_LEFT = False
            KeyHold_RIGHT = False
            KeyHold_UP = False
            KeyHold_DOWN = False
    
    #executting keys order
    sleep(0.1)
    if (KeyHold_LEFT == True or KeyHold_RIGHT == True or KeyHold_UP == True or KeyHold_DOWN == True):    
        print("Key status (LEFT, RIGHT, UP, DOWN)="+'(%s'%KeyHold_LEFT+',%s)'%KeyHold_RIGHT+'(%s'%KeyHold_UP+',%s)'%KeyHold_DOWN)
        KeyControl(KeyHold_LEFT,KeyHold_RIGHT,KeyHold_UP,KeyHold_DOWN,Motor_Delay_HighSpeed)
    
    
    
    
    
    
    