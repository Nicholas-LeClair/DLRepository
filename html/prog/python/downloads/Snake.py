import pygame
import time
import random

#initializing pygame
pygame.init()

#display
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake')



#fps
clock = pygame.time.Clock()
FPS = 30

block_size = 10

font = pygame.font.SysFont(None, 25)


#making the snake
def snake(block_size, snakeList):
    for XnY in snakeList:
        
        pygame.draw.rect(gameDisplay, blue, [XnY[0],XnY[1],block_size,block_size])

#screen text
def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])


#logic and event handling (telling where the snake is moving)
def gameLoop():
    gameExit = False
    gameOver = False

    #x and y location for snake head
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1
    #food location
    randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0

    
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(black)
            message_to_screen("Game Over, press R to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_r:
                        gameLoop()
                    

        #whatever event is called, tell it what to do (directions)    
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

                    
        #borders if snake crashes
        if lead_x >= display_width  or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
              
            

        lead_x += lead_x_change
        lead_y += lead_y_change
                    

        gameDisplay.fill(black)
        
        #food
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size])
        
        #defining variables for snake
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        
        snake(block_size,snakeList)
        
        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
            randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
            snakeLength += 1

        clock.tick(FPS)
            

    pygame.quit()
    quit()

gameLoop()
#code was learned using codecombat
#snake features and pygame learning from youtube channel, thenewboston
