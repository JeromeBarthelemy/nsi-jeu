import pygame
from pygame.locals import *

# Initialisation
pygame.init()
pygame.mixer.init()
i=0

# create the window

screen = pygame.display.set_mode((1280,720), RESIZABLE)

#creating the clock
message_end_time = 0


#Title and Icon
pygame.display.set_caption("Cyberpunk style game")
icon = pygame.image.load("assets/detective-hat.png")
pygame.display.set_icon(icon)

progress = 0 #Progress is going to be the save state of the game. When a scene is finished there will be progress+=1 and the scene will change with an if progress ==.
#Assets:
dialogueFont = pygame.font.Font("assets/fonts/8-BIT WONDER.TTF", 10)





#Characters
playerImg = pygame.image.load("assets/detective-hat.png").convert_alpha()
playerX = 370
playerY = 480





#PoliceImg = pygame.image.load("police.png")
PoliceX = 400
PoliceY = 480






#Backgrounds
crimeSceneBG = pygame.image.load("assets/backgrounds/Game_First_Scene_bigger_res.png").convert()


#Button:
button = pygame.image.load("assets/backgrounds/First_Scene.png").convert()





#sound
#def m_buzzing():
    #pygame.mixer.music.load("assets/sound/SFX/Neon_light_Buzzing.mp3")
#def m_investigation():
    #pygame.mixer.music.load("assets/sound/Music/SFX/Neon_light_Buzzing.mp3")
#def m_explosion():
    #pygame.mixer.music.load("assets/sound/SFX/small-explosion.mp3")






keys = pygame.key.get_pressed()
def player(x, y):
    screen.blit(playerImg, (x, y))
    if keys[pygame.K_RIGHT]:
        playerX += 5
    if keys[pygame.K_LEFT]:
        playerY += 5







#dialogues:
Dialogue1p=["Policeman ;I am sorry to have warned you  this late but the matter is urgent !", "some other text"]
explanation1= dialogueFont.render("Policeman: Good evening Detective, press any key to continue", True, (255, 255, 255))





def cutscene1():
    cscene1d=["Flicker", "Flicker", "Flicker", "You're a goner"]
    m_buzzing()
    pygame.mixer.music.set_volume(0.7)
    for i in range(4): #Makes the screen blink

        pygame.time.delay(1 * 3000)
        screen.fill((128, 0, 128))
        pygame.mixer.music.play()
        pygame.display.update()
        screen.fill((0, 0, 0))
        pygame.time.delay(1 * 3000)
        pygame.display.update()
        dialogue = dialogueFont.render(cscene1d[i], True, (255, 255, 255))
        screen.blit(dialogue, (0, 0))
    m_explosion()
    pygame.mixer.music.play()
    pygame.time.delay(1 * 5000)



#Game loop
running = True
while running:
    for event in pygame.event.get(): #checks if cross is clicked.
        if event.type == pygame.QUIT:
            
            running = False
            print("croix")
            
    
    while progress == 0:
        screen.blit(crimeSceneBG,(0,0))
        #screen.blit(button,(0,0))
        pygame.display.update()
        screen.blit(explanation1, (640,360))
        pygame.display.update()
        pressed = pygame.key.get_pressed()
        
    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                toprint= dialogueFont.render("yay works", True, (255, 255, 255))
                screen.blit(toprint, (0,0))
                pygame.display.update()
                i+=1
                print("click")
            
            
    

    