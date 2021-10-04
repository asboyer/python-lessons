import pgzrun
import random as rnd

WIDTH=800
HEIGHT=600

tank=Actor('tank_blue')
tank.y=575
tank.x=400
tank.angle=90

enemies=[]
enemy_colors=['tank_red','tank_green','tank_sand','tank_dark']

for i in range(3):
    enemy_color_choice=rnd.choice(enemy_colors)
    enemy_colors.remove(enemy_color_choice)
    enemy=Actor(enemy_color_choice)
    enemy.y=25
    enemy.x=i*200+100
    enemy.angle=270
    enemy.move_count=0
    enemies.append(enemy)

background=Actor('grass')

walls=[]
for x in range(16):
    for y in range(10):
        if rnd.randint(0,100)<50:
            wall=Actor('wall')
            wall.x=x*50+25
            wall.y=y*50+25+50
            walls.append(wall)

bullets=[]
bullet_holdoff=0

enemy_bullets=[]

game_over=False

rail_bullet=[]

def update():
    global bullet_holdoff, game_over
    original_x=tank.x
    original_y=tank.y

    if keyboard.left:
        tank.x-=2
        tank.angle=180
    elif keyboard.right:
        tank.x+=2
        tank.angle=0
    elif keyboard.up:
        tank.y-=2
        tank.angle=90
    elif keyboard.down:
        tank.y+=2
        tank.angle=270
    if tank.collidelist(walls) !=-1:
        tank.x=original_x
        tank.y=original_y
    if tank.x<25 or tank.x>775 or tank.y<25 or tank.y>575:
        tank.x=original_x
        tank.y=original_y
    if bullet_holdoff==0:
        if keyboard.space:
            bullet=Actor('bulletblue2')
            bullet.angle=tank.angle
            bullet.x=tank.x
            bullet.y=tank.y
            bullets.append(bullet)
            bullet_holdoff=50
    else:
        bullet_holdoff-=1
    for bullet in bullets:
        if bullet.angle==0:
            bullet.x+=5
        elif bullet.angle==90:
            bullet.y-=5
        elif bullet.angle==180:
            bullet.x-=5
        elif bullet.angle==270:
            bullet.y+=5
    for bullet in bullets:
        wall_index=bullet.collidelist(walls)
        if wall_index!=-1:
            del walls[wall_index]
            bullets.remove(bullet)
            bullet_holdoff=0
        if bullet.x<0 or bullet.x>800 or bullet.y<0 or bullet.y>600:
            bullets.remove(bullet)
        enemy_index=bullet.collidelist(enemies)
        if enemy_index!=-1:
            del enemies[enemy_index]
            bullets.remove(bullet)
    if keyboard.r:
        rail_bullet=Actor('explosion3')
    for enemy in enemies:
        choice=rnd.randint(0,2)
        if enemy.move_count>0:
            enemy.move_count-=1
            original_x=enemy.x
            original_y=enemy.y
            if enemy.angle==0:
                enemy.x+=2
            elif enemy.angle==90:
                enemy.y-=2
            elif enemy.angle==180:
                enemy.x-=2
            elif enemy.angle==270:
                enemy.y+=2
            if enemy.collidelist(walls)!=-1:
                enemy.x=original_x
                enemy.y=original_y
                enemy.move_count=0
            if enemy.x<25 or enemy.x>775 or enemy.y<25 or enemy.y>600:
                enemy.x=original_x
                enemy.y=original_y
                enemy.move_count=0
        
        elif choice==0:
            enemy.move_count=20
            #print('Move')
        elif choice==1:
            enemy.angle=rnd.randint(0,3)*90
        else:
            if enemy.image=='tank_red':
                bullet=Actor('bulletred2')
            elif enemy.image=='tank_green':
                bullet=Actor('bulletgreen2')
            elif enemy.image=='tank_sand':
                bullet=Actor('bulletsand2')
            elif enemy.image=='tank_dark':
                bullet=Actor('bulletdark2')
                
            bullet.angle=enemy.angle
            bullet.x=enemy.x
            bullet.y=enemy.y
            enemy_bullets.append(bullet)
 
        for bullet in enemy_bullets:
            if bullet.angle==0:
                bullet.x+=5
            elif bullet.angle==90:
                bullet.y-=5
            elif bullet.angle==180:
                bullet.x-=5
            elif bullet.angle==270:
                bullet.y+=5
        for bullet in enemy_bullets:
            wall_index=bullet.collidelist(walls)
            if wall_index !=-1:
                del walls[wall_index]
                enemy_bullets.remove(bullet)
            if bullet.colliderect(tank):
                game_over=True
            if bullet.x<25 or bullet.x>775 or bullet.y<25 or bullet.y>600:
                enemy_bullets.remove(bullet)

def draw():
    if len(enemies)==0:
        screen.fill((0,0,0))
        screen.draw.text('YOU WIN!',(260,250),color=(255,255,255),fontsize=100)
    elif game_over:
        screen.fill((0,0,0))
        screen.draw.text('YOU LOSE!!!:(',(230,250),color=(255,255,255),fontsize=100)
    else:
        background.draw()
        tank.draw()
        for wall in walls:
            wall.draw()
        for bullet in bullets:
            bullet.draw()
        for enemy in enemies:
            enemy.draw()
        for bullet in enemy_bullets:
            bullet.draw()

pgzrun.go()