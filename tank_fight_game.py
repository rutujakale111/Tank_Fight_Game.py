import pygame
import time
import random


pygame.init()

width = 800
height = 600

gameWin = pygame.display.set_mode((width, height))
pygame.display.set_caption('DataFlair Tanks Game')
clock = pygame.time.Clock()

tankWidth = 40
tankHeight = 20
turretWidth = 5
wheelWidth = 5
groundHeight = 35

def tank(x, y, turPos,tank):
    x = int(x)
    y = int(y)
    locs=[[27,2],[26,5],[25,8],[23,12],[20,14],[18,15],[15,17],[13,19],[11,21]]
    possibleTurrets=[]
    for i in locs:
        possibleTurrets.append((x-tank*i[0],y-i[1]))

    pygame.draw.circle(gameWin, '#000000', (x, y), int(tankHeight / 2))
    
    for i in range(-15,16,5):
        pygame.draw.circle(gameWin,'#000000', (x+i, y + 20), wheelWidth)

    return possibleTurrets[turPos]

def textObjects(text, color, size="small"):
    if size == "vsmall":
        font=pygame.font.SysFont("Calibre", 15)
        textSurf = font.render(text, True, color)
    if size == "small":
        font=pygame.font.SysFont("Calibre", 25)
        textSurf = font.render(text, True, color)
    if size == "medium":
        font=pygame.font.SysFont("Calibre", 35)
        textSurf = font.render(text, True, color)
    if size == "large":
        font=pygame.font.SysFont("Calibre", 50)
        textSurf = font.render(text, True, color)
    return textSurf, textSurf.get_rect()

def show_message(msg, color, y_displace=0, size="small"):
    textSurf, textRect = textObjects(msg, color, size)
    textRect.center = (int(width / 2), int(height / 2) + y_displace)
    gameWin.blit(textSurf, textRect)

class Button:
    """Create a button, then blit the surface in the while loop"""
 
    def __init__(self, text,pos, font, bg="blue"):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        self.text=text
        self.text = self.font.render(self.text, 1, pygame.Color("blue"))
        self.change_text(bg)
 
    def change_text(self, bg="blue"):
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        
 
    def show(self):
        gameWin.blit(self.text , (self.x, self.y))
 
    def click(self, event,action):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    if action == "quit":
                        pygame.quit()
                        quit()

                    if action == "controls":
                        controlsWin()

                    if action == "play":
                        mainGame()

                    if action == "main":
                        mainWindow()


def controlsWin():
    
    button1 = Button("Play", (150, 500),  font=30)

    button2 = Button("Main", (350, 500), font=30)

    button3 = Button("Quit", (550, 500), font=30)
    

    while True:
        gameWin.fill('#ffffff')
        Green = (0, 255, 0)
        show_message("DataFlair Tank Game", '#000000', -200, size="large")
        show_message("Here are the instructions to play:", 'red', -100, size="medium")
        show_message("The objective is to shoot and destroy the enemy tank before they destroy you.", Green, -30)
        show_message("Fire using the Spacebar", 'gray', 0)
        show_message("Move Turret using the Up and Down arrows", Green, 30)
        show_message("Move Tank using the  Left and Right arrows", 'gray', 60)
        show_message("Press D to raise Power AND Press A to reduce Power ", Green, 90)
        show_message("Finally press P to pause", 'gray', 120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            button1.click(event,'play')
            button2.click(event,'main')
            button3.click(event,'quit')
        button1.show()
        button2.show()
        button3.show()
    
        clock.tick(30)
        pygame.display.update()

def mainWindow ():
    button1 = Button("Play", (350, 350),  font=30)

    button2 = Button("Controls", (350, 430), font=30)

    button3 = Button("Quit", (350, 510), font=30)
    

    while True:
        gameWin.fill('#ffffff')
        Green = (0, 255, 0)
        show_message("DataFlair Tank Game", '#000000', -200, size="large")
        show_message("Welcome to the game!", 'red', -100, size="medium")
        show_message("Choose any of the following to move forward", 'red', -50, size="medium")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            button1.click(event,'play')
            button2.click(event,'controls')
            button3.click(event,'quit')
        button1.show()
        button2.show()
        button3.show()
    
        clock.tick(30)
        pygame.display.update()

def game_over(winner):
    button1 = Button("Play Again", (350, 350),  font=30)

    button2 = Button("Controls", (350, 430), font=30)

    button3 = Button("Quit", (350, 510), font=30)
    while True:
            gameWin.fill('#ffffff')
            Green = (0, 255, 0)
            Red=(255,0,0)
            text=''
            color=''
            if(winner == 1):
                text="Contratulations, You Won!"
                color=Green
            else:
                text="Sorry, game over. Better luck next time!"
                color=Red
            show_message("DataFlair Tank Game", '#000000', -200, size="large")
            show_message(text, color, -100, size="medium")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                button1.click(event,'play')
                button2.click(event,'controls')
                button3.click(event,'quit')
            button1.show()
            button2.show()
            button3.show()
        
            clock.tick(30)
            pygame.display.update()

def pause():
    paused = True
    show_message("Paused", 'white', -100, size="large")
    show_message("Press C to continue playing or Q to quit", 'wheat', 25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        clock.tick(5)

def explosion(x, y, size=50):
    explode = True

    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        startPoint = x, y

        colorChoices = ['red', 'brown2', 'yellow', 'gold1']

        magnitude = 1

        while magnitude < size:
            exploding_bit_x = x + random.randrange(-1 * magnitude, magnitude)
            exploding_bit_y = y + random.randrange(-1 * magnitude, magnitude)

            pygame.draw.circle(gameWin, colorChoices[random.randrange(0, 4)], (exploding_bit_x, exploding_bit_y),
                               random.randrange(1, 5))
            magnitude += 1

            pygame.display.update()
            clock.tick(100)

        explode = False
def show_health_bars(player_health, enemy_health):
    if player_health > 75:
        player_color = 'green'
    elif player_health > 50:
        player_color = 'yellow'
    else:
        player_color = 'red'

    if enemy_health > 75:
        enemy_color = 'green'
    elif enemy_health > 50:
        enemy_color = 'yellow'
    else:
        enemy_color = 'red'

    pygame.draw.rect(gameWin, player_color, (680, 25, player_health, 25))
    pygame.draw.rect(gameWin, enemy_color, (20, 25, enemy_health, 25))


           
def fireShell(xy, tankx, tanky, turPos, gun_power, xlocation, barrier_width, randomHeight, enemyTankX, enemyTankY):
    fire = True
    damage = 0

    startingShell = list(xy)

    print("FIRE!", xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.circle(gameWin, 'red', (startingShell[0], startingShell[1]), 5)

        startingShell[0] -= (12 - turPos) * 2

        startingShell[1] += int(
            (((startingShell[0] - xy[0]) * 0.015 / (gun_power / 50)) ** 2) - (turPos + turPos / (12 - turPos)))

        if startingShell[1] > height - groundHeight:
            print("Last shell:", startingShell[0], startingShell[1])
            hit_x = int((startingShell[0] * height - groundHeight) / startingShell[1])
            hit_y = int(height - groundHeight)
            print("Impact:", hit_x, hit_y)

            if enemyTankX + 10 > hit_x > enemyTankX - 10:
                print("Critical Hit!")
                damage = 25
            elif enemyTankX + 15 > hit_x > enemyTankX - 15:
                print("Hard Hit!")
                damage = 18
            elif enemyTankX + 25 > hit_x > enemyTankX - 25:
                print("Medium Hit")
                damage = 10
            elif enemyTankX + 35 > hit_x > enemyTankX - 35:
                print("Light Hit")
                damage = 5

            explosion(hit_x, hit_y)
            fire = False

        check_x_1 = startingShell[0] <= xlocation + barrier_width
        check_x_2 = startingShell[0] >= xlocation

        check_y_1 = startingShell[1] <= height
        check_y_2 = startingShell[1] >= height - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            print("Last shell:", startingShell[0], startingShell[1])
            hit_x = int((startingShell[0]))
            hit_y = int(startingShell[1])
            print("Impact:", hit_x, hit_y)
            explosion(hit_x, hit_y)
            fire = False

        pygame.display.update()
        clock.tick(60)
    return damage

def compfireShell(xy, tankx, tanky, turPos, gun_power, xlocation, barrier_width, randomHeight, ptankx, ptanky):
    damage = 0
    currentPower = 1
    power_found = False

    while not power_found:
        currentPower += 1
        if currentPower > 100:
            power_found = True

        fire = True
        startingShell = list(xy)

        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


            startingShell[0] += (12 - turPos) * 2
            startingShell[1] += int(
                (((startingShell[0] - xy[0]) * 0.015 / (currentPower / 50)) ** 2) - (turPos + turPos / (12 - turPos)))

            if startingShell[1] > height - height:
                hit_x = int((startingShell[0] * height - height) / startingShell[1])
                hit_y = int(height - height)
                if ptankx + 15 > hit_x > ptankx - 15:
                    print("target acquired!")
                    power_found = True
                fire = False

            check_x_1 = startingShell[0] <= xlocation + barrier_width
            check_x_2 = startingShell[0] >= xlocation

            check_y_1 = startingShell[1] <= height
            check_y_2 = startingShell[1] >= height - randomHeight

            if check_x_1 and check_x_2 and check_y_1 and check_y_2:
                hit_x = int((startingShell[0]))
                hit_y = int(startingShell[1])
                fire = False

    fire = True
    startingShell = list(xy)
    print("FIRE!", xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.circle(gameWin, 'red', (startingShell[0], startingShell[1]), 5)

        startingShell[0] += (12 - turPos) * 2

        gun_power = random.randrange(int(currentPower * 0.90), int(currentPower * 1.10))

        startingShell[1] += int(
            (((startingShell[0] - xy[0]) * 0.015 / (gun_power / 50)) ** 2) - (turPos + turPos / (12 - turPos)))

        if startingShell[1] > height - groundHeight:
            print("last shell:", startingShell[0], startingShell[1])
            hit_x = int((startingShell[0] * height - groundHeight) / startingShell[1])
            hit_y = int(height - groundHeight)
            print("Impact:", hit_x, hit_y)

            if ptankx + 10 > hit_x > ptankx - 10:
                print("Critical Hit!")
                damage = 25
            elif ptankx + 15 > hit_x > ptankx - 15:
                print("Hard Hit!")
                damage = 18
            elif ptankx + 25 > hit_x > ptankx - 25:
                print("Medium Hit")
                damage = 10
            elif ptankx + 35 > hit_x > ptankx - 35:
                print("Light Hit")
                damage = 5

            explosion(hit_x, hit_y)
            fire = False

        check_x_1 = startingShell[0] <= xlocation + barrier_width
        check_x_2 = startingShell[0] >= xlocation

        check_y_1 = startingShell[1] <=height
        check_y_2 = startingShell[1] >= height - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            print("Last shell:", startingShell[0], startingShell[1])
            hit_x = int((startingShell[0]))
            hit_y = int(startingShell[1])
            print("Impact:", hit_x, hit_y)
            explosion(hit_x, hit_y)
            fire = False

        pygame.display.update()
        clock.tick(60)
    return damage
def mainGame():
    gameExit = False
    gameOver = False

    player_health = 100
    enemy_health = 100

    barrier_width = 50

    mainTankX = width * 0.9
    mainTankY = height * 0.9
    tankMove = 0
    currentTurPos = 0
    changeTur = 0

    enemyTankX = width * 0.1
    enemyTankY = height * 0.9

    fire_power = 50
    power_change = 0

    xlocation = (width / 2) + random.randint(int(-0.1 * width),int( 0.1 * width))
    randomHeight = random.randint(int(height * 0.1), int(height * 0.6))

    while True:
        gameWin.fill('#ffffff')
        Green = (0, 255, 0)
        Red=(255,0,0)
        text=''
        color=''
        show_message("DataFlair Tank Game", '#000000', -200, size="large")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5

                elif event.key == pygame.K_RIGHT:
                    tankMove = 5

                elif event.key == pygame.K_UP:
                    changeTur = 1

                elif event.key == pygame.K_DOWN:
                    changeTur = -1

                elif event.key == pygame.K_p:
                    pause()
                elif event.key == pygame.K_SPACE:
                    gameWin.fill('white')
                    show_message("DataFlair Tank Game", '#000000', -200, size="large")
                    show_health_bars(player_health, enemy_health)
                    gun = tank(mainTankX, mainTankY, currentTurPos,1)
                    enemy_gun = tank(enemyTankX, enemyTankY, 8,-1)
                    fire_power += power_change
                    font=pygame.font.SysFont("Calibre", 30)
                    text = font.render("Power: " + str(fire_power) + "%", True, 'black')
                    gameWin.blit(text, [width / 2, 0])
                    text = font.render("Height: " + str(currentTurPos) + "%", True, 'black')
                    gameWin.blit(text, [width / 2, 20])
                    pygame.draw.rect(gameWin, 'green', [xlocation, height - randomHeight, barrier_width, randomHeight])
                    gameWin.fill('green',
                                        rect=[0,height - groundHeight, width, height])
                    pygame.display.update()

                    clock.tick(30)
                    
                    damage = fireShell(gun, mainTankX, mainTankY, currentTurPos, fire_power, xlocation, barrier_width,
                                       randomHeight, enemyTankX, enemyTankY)
                    enemy_health -= damage

                    possibleMovement = ['f', 'r']
                    moveIndex = random.randrange(0, 2)

                    for x in range(random.randrange(0, 10)):

                        if width * 0.3 > enemyTankX > width * 0.03:
                            if possibleMovement[moveIndex] == "f":
                                enemyTankX += 5
                            elif possibleMovement[moveIndex] == "r":
                                enemyTankX -= 5

                            gameWin.fill('white')
                            show_message("DataFlair Tank Game", '#000000', -200, size="large")
                            show_health_bars(player_health, enemy_health)
                            gun = tank(mainTankX, mainTankY, currentTurPos,1)
                            enemy_gun = tank(enemyTankX, enemyTankY, 8,-1)
                            fire_power += power_change
                            font=pygame.font.SysFont("Calibre", 30)
                            text = font.render("Power: " + str(fire_power) + "%", True, 'black')
                            gameWin.blit(text, [width / 2, 0])
                            text = font.render("Height: " + str(currentTurPos) + "%", True, 'black')
                            gameWin.blit(text, [width / 2, 20])
                            pygame.draw.rect(gameWin, 'green', [xlocation, height - randomHeight, barrier_width, randomHeight])
                            gameWin.fill('green',
                                             rect=[0,height - groundHeight, width, height])
                            pygame.display.update()

                            clock.tick(30)

                    damage = compfireShell(enemy_gun, enemyTankX, enemyTankY, 8, 50, xlocation, barrier_width,
                                         randomHeight, mainTankX, mainTankY)
                    player_health -= damage
                
                elif event.key == pygame.K_a:
                    power_change = -1
                elif event.key == pygame.K_d:
                    power_change = 1
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0
            

        mainTankX += tankMove

        currentTurPos += changeTur

        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0

        if mainTankX - (tankWidth / 2) < xlocation + barrier_width:
            mainTankX += 5
    
        show_health_bars(player_health, enemy_health)
        gun = tank(mainTankX, mainTankY, currentTurPos,1)
        enemy_gun = tank(enemyTankX, enemyTankY, 8,-1)

        fire_power += power_change

        if fire_power > 100:
            fire_power = 100
        elif fire_power < 1:
            fire_power = 1
                
        font=pygame.font.SysFont("Calibre", 30)
        text = font.render("Power: " + str(fire_power) + "%", True, 'black')
        gameWin.blit(text, [width / 2, 0])
        text = font.render("Height: " + str(currentTurPos) + "%", True, 'black')
        gameWin.blit(text, [width / 2, 20])
        pygame.draw.rect(gameWin, 'green', [xlocation, height - randomHeight, barrier_width, randomHeight])
        gameWin.fill('green',rect=[0,height - groundHeight, width, height])
        if player_health < 1 :
            game_over(0)
        elif enemy_health < 1:
            game_over(1)

        pygame.display.update()
        clock.tick(30)
    

mainWindow()