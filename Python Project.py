import pygame
import random
import math
import sys
import random
from Target import Target
from Target import Shooter
from pygame.locals import *


pygame.init()
 
screen = pygame.display.set_mode((640, 460))
font = pygame.font.SysFont(None, 36)
target = pygame.image.load("images/target.png").convert_alpha()
target = pygame.transform.scale(target,(90, 90))
#shooter = pygame.image.load("images/shooter.png").convert_alpha()
#shooter = pygame.transform.scale(shooter,(260, 260))
GameOver = pygame.image.load("images/game_over.jpg").convert_alpha()
GameOver = pygame.transform.scale(GameOver, (640, 460))
screen.fill((205, 133, 63))
collision = False
collision2 = False
num_Target = 0
life = 5
bar = pygame.Rect(0, 300, 640, 160)
hello = " "
timer = 0.0
invulTimer = 0.0
TargetTimer = 0.0
Timer3 = 0.0
targetnumber = 0
second = 0.5
second2 = 0
minute = 0
score = 0
hi = 0
start = 0
#rectangle = pygame.Rect(x, y, 90, 90)
main_clock = pygame.time.Clock()
target1 = Target(random.randint(1, 640),random.randint(1, 250))
shooter1 = Shooter(0, 200)
targets = pygame.sprite.Group()
initTarget = pygame.sprite.Group()
targets.add(target1)
shooters = pygame.sprite.Group()
shooters.add(shooter1)

def draw_text(display_string, font, surface, x_pos, y_pos, color):
    text_display = font.render(display_string, 1, color)
    surface.blit(text_display, (x_pos, y_pos))
def create_target(num_Target):
    validPlacement = False
    if num_Target <= 4:
        while not validPlacement:
            attempts = 0
            z = random.randint(1, 2)
            
            if z == 1:
                new_target = Target(random.randint(280, 590),random.randint(1, 250))
                initTarget.add(new_target)
                collideTarget = pygame.sprite.spritecollideany(new_target,targets)
                if collideTarget:
                    
                    initTarget.remove(new_target)
                    validPlacement = False
                        
                else:
                    targets.add(new_target)
                    initTarget.remove(new_target)
                    validPlacement = True
                    
            if z == 2:
                new_target = Target(random.randint(1, 220),random.randint(1, 110))
                initTarget.add(new_target)
                collideTarget = pygame.sprite.spritecollideany(new_target,targets)
                if collideTarget:
                    
                    
                    initTarget.remove(new_target)
                    validPlacement = False
                        
                else:
                    targets.add(new_target)
                    initTarget.remove(new_target)
                    validPlacement = True
            attempts +=1

            if attempts > 20:
                break
    else:
        print ("too many targets")


while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((205, 133, 63))

    draw_text('Shooting Gallery',   font, screen, 100, 100, (0,0,0))
    draw_text('Press Spacebar to Start',  font, screen, 280, 400, (0,0,0))
    screen.blit(target, (450, 200))
    screen.blit(target, (300, 200))
    screen.blit(target, (150, 200))
    if event.type == KEYDOWN:
        if event.key == K_SPACE:
            start += 1
    if start >= 1:
        if life <= 0:
            break
        #collision_hit_list = pygame.sprite.spritecollide(target, targets, False)
        timer += main_clock.get_time()
        TargetTimer += main_clock.get_time()
        invulTimer += main_clock.get_time()
        Timer3 += main_clock.get_time()
        if Timer3 >= 1000:
            second2 = second2 + 1
            Timer3 = 0
            if second2 >= 60:
                minute += 1
                second2 = 0
        if score >= 0 and score < 10:
            if timer >= 500:
                second = second + 0.5
                timer = 0
            if second >= 2.0:
                second = 0.0
                create_target(num_Target)
                
        if score >= 10 and score < 20:
            if timer >= 500:
                second = second + 0.5
                timer = 0
            if second >= 1.5:
                second = 0.0
                create_target(num_Target)
                
                
                
        if score >= 20 and score < 35:
            if timer >= 500:
                second = second + 0.5
                timer = 0
            if second >= 1.0:
                second = 0.0
                create_target(num_Target)
                
        if score >= 35:
            if timer >= 500:
                second = second + 0.5
                timer = 0
            if second >= 0.5:
                second = 0.0
                create_target(num_Target)
        
        if event.type == MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()
            clicked_sprites = [s for s in targets if s.rect.collidepoint(pos)]
            for aTarget in targets:
                if not clicked_sprites:
                    if invulTimer > 1000:
                        #print(clicked_sprites)
                        life -= 1
                        clicked_sprites.clear()
                        invulTimer = 500
                            
                elif clicked_sprites:
                    score = score + 1
                    targets.remove(clicked_sprites)
                    invulTimer = 850
                    clicked_sprites.clear()

                    
    #if life <= 0:
       # screen.blit(GameOver, (100, 200))
                        
            #collision = pygame.sprite.spritecollide(new_target, targets, True)
            #collision2 = pygame.sprite.spritecollide(new_target, shooters, True)
            #for new_target in collision:
                #print(collision)
                #collision.clear()
                #print(collision)
                #break
            #for new_target in collision2:
                #print(collision2)
                #collision2.clear()
                #print(collision2)
                #break
                
           # if collision_hit_list == False:
               # create_target(random.randint(200, 640), random.randint(1, 300))
           #elif collision_hit_list == True:
                #create_target.clear(x, y)
        for aTarget in targets:
            aTarget.lifeSpan += main_clock.get_time()
            aTarget.update(life)
            
        main_clock.tick(50)
        screen.fill((205, 133, 63))
        bar1 = pygame.draw.rect(screen, (139, 69, 19), bar)
        #screen.blit(shooter, (0, 200))
        targets.draw(screen)
        shooters.draw(screen)
        num_Target = len(targets)
        draw_text('Score: %s' % (score), font, screen, 460, 400, (0,0,0))
        draw_text('Life: %s' % (life), font, screen, 340, 400, (0,0,0))
        if second2 < 10:
            draw_text("{}:0{}".format(minute,second2), font, screen, 260, 400, (0,0,0))
        else:
            draw_text("{}:{}".format(minute,second2), font, screen, 260, 400, (0,0,0))
        if life <= 0:
            screen.blit(GameOver, (0, 0))
            draw_text('Score: %s' % (score), font, screen, 460, 400, (255, 255, 255))
            if second2 < 10:
                draw_text("{}:0{}".format(minute,second2), font, screen, 260, 400, (255, 255, 255))
            else:
                draw_text("{}:{}".format(minute,second2), font, screen, 260, 400, (255, 255, 255))

    pygame.display.update()


