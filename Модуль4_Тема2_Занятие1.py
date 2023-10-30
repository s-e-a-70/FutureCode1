import pygame  
pygame.init()  
scr = pygame.display.set_mode((500, 500))
scr.fill((255,255,255))
pygame.draw.circle(scr,(0,0,255),(250,250),40)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
