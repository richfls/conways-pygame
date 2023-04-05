import pygame
import random
pygame.init()
pygame.display.set_caption("conways game of life")
window = pygame.display.set_mode((800, 800))
window.fill((0,0,0))
clock = pygame.time.Clock()
cols = 16
rows = 16

grid = [[0 for i in range(cols)] for j in range(rows)]

grid[1][1] = 1
grid[1][2] = 1
grid[1][3] = 1
print(grid)



while True:
    clock.tick(60)
    event = pygame.event.get()

    for event in pygame.event.get():
        break

    for col in range(cols):
        for row in range(rows):
            counter = 0

            if col<cols-1 and grid[col+1][row] == 1:
                counter += 1
            if row<rows-1 and grid[col][row+1] == 1:
                counter += 1
            if col>=0 and grid[col-1][row] == 1:
                counter += 1
            if row>=0 and grid[col][row-1] == 1:
                counter += 1
            if col<cols-1 and row<rows-1 and grid[col+1][row+1] == 1:
                counter += 1
            if col>=0 and row>=0 and grid[col-1][row-1] == 1:
                counter += 1
            if col>=0 and row<rows-1 and grid[col-1][row+1] == 1:
                counter += 1
            if col<cols-1 and row>=0 and grid[col+1][row-1] == 1:
                counter += 1

            if grid[col][row] == 1 and counter <=1:
                grid[col][row] = 0
                print("died from lonliness")
            if grid[col][row] == 1 and counter <=3 and counter >1:
                grid[col][row] = 1
                print("Lives")
            if grid[col][row] == 1 and counter >=4:
                grid[col][row] = 0
                print("died from overcrowding")

    #pygame.time.wait(200)

    window.fill((0,0,0))
    for col in range(cols):
        for row in range(rows):
            if grid[col][row] == 0:
                pygame.draw.rect(window, (0,0,0), (col*50, row*50, 50,50))
                pygame.draw.rect(window, (255,255,255), (col*50, row*50, 50,50),1)
            if grid[col][row] == 1:
                pygame.draw.rect(window, (0,0,255), (col*50, row*50, 50, 50))

    pygame.display.flip()

pygame.quit()
