import pygame
import random
import time

pygame.init()
clock = pygame.time.Clock()
width = 700
height = 500

green = (0,255,0)
red = (213,50,80)
pink = (255,105,180)
blue = (65,105,225)
black = (0,0,0)

dis = pygame.display.set_mode((width,height))

pygame.display.set_caption('Python Snake Game')

snake_size = 10
snake_speed = 10
snake_pos = []

def snake(snake_size,snake_pos):
    for x in snake_pos:
        pygame.draw.rect(dis,green,[x[0],x[1],snake_size,snake_size])

def snakegame():
    x1 = width/2;
    y1 = height/2;
    x1_new = 0
    y1_new = 0

    snake_list = []
    leng_of_snake = 1

    foodx = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    gameover = False
    gameend = False

    while not gameover:
        while gameend == True:
            dis.fill(pink)
            font_style = pygame.font.SysFont('comicsansms',30)
            mesg = font_style.render("You Lost! Press P-Play Again or Q-Quit",True,red)
            dis.blit(mesg,[width/6,height/3])

            score = leng_of_snake - 1
            score_food = pygame.font.SysFont('comicsansms',35)
            value = score_food.render("Your Score : "+str(score),True,blue)
            dis.blit(value,[width/3,height/5])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameover = True
                        gameend = False
                    if event.key == pygame.K_p:
                        snakegame()
                    if event.type == pygame.QUIT:
                        gameover=True
                        gameend=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover=True
            kd = False
            kl = False
            kr = False
            ku = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                   x1_new = -snake_size
                   y1_new = 0
                elif event.key == pygame.K_RIGHT:
                    x1_new = snake_size
                    y1_new = 0
                elif event.key == pygame.K_UP:
                    x1_new = 0
                    y1_new = -snake_size

                elif event.key == pygame.K_DOWN:
                    x1_new = 0
                    y1_new = snake_size

        if x1 >= width or y1 >= height or x1<0 or y1<0:
            gameend = True
        x1 += x1_new
        y1 += y1_new
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_size, snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > leng_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                gameend=True

        snake(snake_size,snake_list)

        score = leng_of_snake - 1
        score_food = pygame.font.SysFont('comicsansms', 35)
        value = score_food.render("Your Score : " + str(score), True, blue)
        dis.blit(value, [0,0])
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0,width-snake_size)/10.0)*10.0
            foody = round(random.randrange(0,height-snake_size)/10.0)*10.0
            leng_of_snake += 1

        clock.tick(snake_speed+(leng_of_snake**0.25))

    pygame.quit()
    quit()

snakegame()