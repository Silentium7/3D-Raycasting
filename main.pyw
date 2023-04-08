from math import cos, sin, atan, sqrt

import pygame
pygame.init()


l = [[1,1,1,1,1,1,1,1,1,1],
     [1,0,1,0,0,1,0,0,0,1],
     [1,0,1,0,0,0,0,1,0,1],
     [1,0,0,0,0,1,1,1,0,1],
     [1,1,1,1,1,1,0,1,0,1],
     [1,0,0,0,0,1,0,0,0,1],
     [1,0,1,0,0,1,0,1,1,1],
     [1,0,1,1,1,1,0,1,0,1],
     [1,0,0,0,0,0,0,0,0,1],
     [1,1,1,1,1,1,1,1,1,1]]

l = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1], [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1], [1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

def draw_map(screen, l):
    dim_l = len(l)
    dim_s = screen.get_width()
    for ligne in range(len(l)):
        for e in range(len(l[ligne])):
                        
            if l[ligne][e] == 1 :
                pygame.draw.rect(screen, (0,0,50), [e*int(100), ligne*int(100), int(100), int(100)])

def is_on_case(l, x_point, y_point):
    try :
        if l[y_point][x_point] == 1 : return True
        else : return False
    except : return False

def draw_unique_case(screen, x, y):
    pygame.draw.rect(screen, (0,0,150), [x*100, y*100, 100,100])

screen = pygame.display.set_mode([1500, 600], pygame.FULLSCREEN)

x_player = 1.5
y_player = 1.5
angle_player = 0
amplitude_player = 1

clock = pygame.time.Clock()

running = True
while running:
    
    screen.fill((0,0,0))
    """
    draw_map(screen, l)
    pygame.draw.rect(screen, (255,0,0), [int(x_player*100),int(y_player*100),10,10])
    """
    cases_a_declencher = []

    for k in range(200):
        for i in range(160):
            angle = angle_player+atan((-0.1+(k/800))/0.1)
            x_point = x_player+(0.05*i)*cos(angle)
            y_point = y_player+(0.05*i)*sin(angle)
        
            touché = is_on_case(l, int(x_point), int(y_point))
            #pygame.draw.rect(screen, (0,255,0), [int(x_point*100),int(y_point*100),2,2])
            
            if touché :
                cases_a_declencher.append((int(x_point), int(y_point)))
                
                while touché :
                    x_point = x_point-(0.01)*cos(angle)
                    y_point = y_point-(0.01)*sin(angle)
                    touché = is_on_case(l, int(x_point), int(y_point))
                    
                dist = sqrt(((x_point-x_player)**2)+((y_point-y_player)**2))
                break
            dist = 10000
        
        try : 
            dist = 200/dist
        except ZeroDivisionError : dist = 1
        try : 
            #pygame.draw.rect(screen, (dist/1.5,0,0), [600+(k*4), 300-(dist/2), 1*4, dist])
            pygame.draw.rect(screen, (dist/1.5,0,0), [(k*9), 300-(dist/2), 1*9, dist])
        except :
            #pygame.draw.rect(screen, (255,0,0), [600+(k*4), 300-(dist/2), 1*4, dist])
            pygame.draw.rect(screen, (255,0,0), [(k*9), 300-(dist/2), 1*9, dist])
    
    """
    for i in range(len(cases_a_declencher)):
        draw_unique_case(screen, cases_a_declencher[i][0], cases_a_declencher[i][1])
    """
    
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] :
        x = x_player+(0.02)*cos(angle_player)
        y = y_player+(0.02)*sin(angle_player)
        if not is_on_case(l, int(x), int(y)):
            x_player = x
            y_player = y
    if keys[pygame.K_DOWN] :
        x = x_player-(0.02)*cos(angle_player)
        y = y_player-(0.02)*sin(angle_player)
        if not is_on_case(l, int(x), int(y)):
            x_player = x
            y_player = y
    if keys[pygame.K_LEFT] : angle_player -= 0.1
    if keys[pygame.K_RIGHT] : angle_player += 0.1
    
    chain = str(int(clock.get_fps())) + ' fps'
    pygame.display.set_caption(chain)
    clock.tick(40)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False





    pygame.display.flip()
pygame.quit()