import pygame, sys, random
pygame.init()
#последняя прверка времени
last1 = pygame.time.get_ticks()
last2 = pygame.time.get_ticks()
last_a = pygame.time.get_ticks()
#скорость персонажа
speed = 15
in_speed = 15
#направление движения 0-вверх 1-вправо 2-вниз 3-влево
direction = None
#достижение границ
borders = [False]*4
#скорость снаряда
b_speed = 25
shooting = False
#массив с координатами зарядов
bullets = []
#массив с пришельцами
aliens = []
#флаг движения
moving = False
#установка дисплея
screen = pygame.display.set_mode((720,1280))
#функция стрельбы
class hero():
    def __init__(self,x,y,hp):
        self.h_x = x
        self.h_y = y
        self.h_hp = hp
    def move_r():
        h_x+=speed
    def move_l():
        h_x-=speed
    def move_u():
        h_y-=speed
    def move_d():
        h_y+=speed
    
class bullet():
    def __init__(self,x,y,time):
        self.b_x = x
        self.b_y = y
        self.time = time

class alien():
    def __init__(self,hp):
        self.a_x = random.randint(200,650)
        self.a_y = random.randint(200,520)
        self.hp = hp

#загрузка изображения
bg = pygame.image.load('E:\Python\Projects\python\pygame\pics\imgonline-com-ua-pixelizationxjFkebxIVyri.jpg')
#snd = pygame.mixer.Sound('E:\Python\Projects\python\pygame\sounds\xwing_shot1.wav')
bg = pygame.transform.scale(bg, (720,1280))
img = pygame.image.load('E:\Python\Projects\python\pygame\pics\Xwing_img.png')
img = pygame.transform.scale(img, (120,120))
bullet_img = pygame.image.load('E:\Python\Projects\python\pygame\pics\Xwing_bullet.png') 
bullet_img = pygame.transform.scale(bullet_img, (16,16))
Alien_img = pygame.image.load('E:\Python\Projects\python\pygame\pics\Tie interceptor_img.png')
Alien_img = pygame.transform.scale(Alien_img, (120,120))
hpbar = pygame.image.load('E:\Python\Projects\python\pygame\pics\hp bar clear.png')
hpbar = pygame.transform.scale(hpbar,(160,35))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
#определение границ    
    if x<0:
        borders[0] = True
    else:
        borders[0] = False
    if x>640:
        borders[1] = True
    else:
        borders[1] = False
    
    if y<0:
        borders[2] = True
    else:
        borders[2] = False
    if y>1220:
        borders[3] = True
    else:
        borders[3] = False
    
#отбрабатываниее нажатия клавиш
    keys = pygame.key.get_pressed()
    if keys.count(1)>0:
        moving= True
    else:
        moving = False
    if keys[pygame.K_LEFT] and not borders[0]:
        in_speed = 5
        direction = 3
        x-=speed
    if keys[pygame.K_RIGHT] and not borders[1]:
        in_speed = 5
        direction = 1
        x+=speed
    if keys[pygame.K_UP] and not borders[2]:
        in_speed = 5
        direction = 0
        y-=speed
    if keys[pygame.K_DOWN] and not borders[3]:
        in_speed = 5
        direction = 2
        y+=speed
    if keys[pygame.K_a]:
        if pygame.time.get_ticks() - last1 > 100:
            last1 = pygame.time.get_ticks()
            bullets.append(bullet(x-2,y,last1))
            #snd.play()
    if keys[pygame.K_d]:
        if pygame.time.get_ticks() - last2 > 100:
            last2 = pygame.time.get_ticks()
            bullets.append(bullet(x+110,y,last2))
            #snd.play()
    
    #создание новых пришельцев
    if  pygame.time.get_ticks()-last_a > 1000 and len(aliens)<7:
        last_a = pygame.time.get_ticks()
        aliens.append(alien(3))
    #обработка попаданий
    for k in aliens:
        for i in bullets:
            if i.b_x>=k.a_x and i.b_x<=k.a_x+120 and i.b_y>=k.a_y and i.b_y<=k.a_y+120:
                k.hp-=1
                try:
                    bullets.remove(i)
                except(ValueError):
                    print(i.b_x, i.b_y, bullets)
                if k.hp == 0:
                    aliens.remove(k)
                
                
    #полет снаряда
    for j in bullets:
        if pygame.time.get_ticks()-j.time<5000:
            j.b_y-=b_speed
        else:
            bullets.remove(j)
    
    #инерция
    if in_speed>0 and moving == False:
        if direction == 0:
            y-=in_speed
            in_speed-=0.5
        elif direction == 1:
            x+=in_speed
            in_speed-=0.5
        elif direction == 2:
            y+=in_speed
            in_speed-=0.5
        elif direction == 3:
            x-=in_speed
            in_speed-=0.5
    #смена кадра    
    screen.blit(bg, (0,0))
    screen.blit(img, (x,y))
    print((x,y))
    for i in bullets:
        screen.blit(bullet_img, (i.b_x, i.b_y))
    for k in aliens:
        screen.blit(Alien_img, (k.a_x, k.a_y))
    screen.blit(hpbar, (0,1000))
    pygame.time.delay(20)
    pygame.display.update()
    print('enemies:',len(aliens))
