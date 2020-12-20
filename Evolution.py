import pygame
import random
import math
pygame.init()

pygame.display.set_caption("Evolution")
win = pygame.display.set_mode((1000,600))
Mediumfont = pygame.font.SysFont('Calibri', 20, True, False)
WHITE = (255,255,255)
x = 20
y = 20
width = 30
height = 30
vel = 10
Level = 0
Check = True


def CreateBee():
    XStart = random.randint(100,1000)
    YStart = random.randint(100,600)
    XEnd = random.randint(0,1000)
    YEnd = random.randint(0,600)
    Velocity = random.randint(5,20)
    return XStart,YStart,XEnd,YEnd,Velocity

def Training(Sample):
    TotalScore = 0
    HighestScore = 0
    Scores = []
    BabyChosen = False
    for x in Sample:
        if x[4]/x[5] > HighestScore:
            HighestScore = x[5]//x[6]
            
    for x in Sample:
        Scores.append(HighestScore - (x[4]//x[5]))
        TotalScore = TotalScore + (HighestScore - (x[4]//x[5]))
    Choice1 = random.randint(0,TotalScore)
    Choice2 = random.randint(0,TotalScore)
    Temp = 0
    Chosen1 = False
    Chosen2 = False
    while not BabyChosen:
        if Choice1 - Scores[Temp] <0:
            if not Chosen1:
                Position1 = Temp
                Chosen1 = True
        if Choice2 - Scores[Temp] <0:
            if not Chosen2:
                Position2 = Temp
                Chosen2 = True       
        Choice1 = Choice1 - Scores[Temp]
        Choice2 = Choice2 - Scores[Temp]
        if Chosen1 and Chosen2:
            BabyChosen = True
        Temp = Temp + 1 
    VelocityChoice = random.randint(0,100)
    
    if VelocityChoice >= 50:
        NewBee = (Sample[Position1][0],Sample[Position2][1],Sample[Position1][2],Sample[Position2][3],Sample[Position1][4])
        VelocityChoice = random.randint(0,100)
        if VelocityChoice >= 90:
            ChangeNumber = random.randint(-200,200)
            if Sample[Position1][0] + ChangeNumber >0 and Sample[Position1][0] + ChangeNumber <1000: 
                NewBee = (Sample[Position1][0] + ChangeNumber,Sample[Position2][1],Sample[Position1][2],Sample[Position2][3],Sample[Position1][4])
        VelocityChoice = random.randint(0,100)
        if VelocityChoice >= 90:
            ChangeNumber = random.randint(-200,200)
            if Sample[Position1][1] + ChangeNumber >0 and Sample[Position1][1] + ChangeNumber <600: 
                NewBee = (Sample[Position1][0],Sample[Position2][1] + ChangeNumber,Sample[Position1][2],Sample[Position2][3],Sample[Position1][4])
        if VelocityChoice >= 90:
            ChangeNumber = random.randint(-200,200)
            if Sample[Position1][2] + ChangeNumber >0 and Sample[Position1][2] + ChangeNumber <1000: 
                NewBee = (Sample[Position1][0],Sample[Position2][1],Sample[Position1][2] + ChangeNumber,Sample[Position2][3],Sample[Position1][4])
        VelocityChoice = random.randint(0,100)
        if VelocityChoice >= 90:
            ChangeNumber = random.randint(-200,200)
            if Sample[Position1][3] + ChangeNumber >0 and Sample[Position1][3] + ChangeNumber <600: 
                NewBee = (Sample[Position1][0],Sample[Position2][1],Sample[Position1][2],Sample[Position2][3] + ChangeNumber,Sample[Position1][4])
        VelocityChoice = random.randint(0,100)
        if VelocityChoice >= 90:
            ChangeNumber = random.randint(-10,10)
            if Sample[Position1][4] + ChangeNumber >0 and Sample[Position1][4] + ChangeNumber <30: 
                NewBee = (Sample[Position1][0],Sample[Position2][1],Sample[Position1][2],Sample[Position2][3],Sample[Position1][4] + ChangeNumber)
                
    if VelocityChoice < 50:
        NewBee = (Sample[Position2][0],Sample[Position1][1],Sample[Position2][2],Sample[Position1][3],Sample[Position2][4])
        VelocityChoice = random.randint(0,100)
        if VelocityChoice >= 90:
            ChangeNumber = random.randint(-200,200)
            if Sample[Position2][0] + ChangeNumber >0 and Sample[Position2][0] + ChangeNumber <1000: 
                NewBee = (Sample[Position2][0] + ChangeNumber,Sample[Position1][1],Sample[Position2][2],Sample[Position1][3],Sample[Position2][4])
        VelocityChoice = random.randint(0,100)
        if VelocityChoice >= 90:
            ChangeNumber = random.randint(-200,200)
            if Sample[Position2][1] + ChangeNumber >0 and Sample[Position2][1] + ChangeNumber <600: 
                NewBee = (Sample[Position2][0],Sample[Position1][1] + ChangeNumber,Sample[Position2][2],Sample[Position1][3],Sample[Position2][4])
        if VelocityChoice >= 90:
            ChangeNumber = random.randint(-200,200)
            if Sample[Position2][2] + ChangeNumber >0 and Sample[Position2][2] + ChangeNumber <1000: 
                NewBee = (Sample[Position2][0],Sample[Position1][1],Sample[Position2][2] + ChangeNumber,Sample[Position1][3],Sample[Position2][4])
        VelocityChoice = random.randint(0,100)
        if VelocityChoice >= 90:
            ChangeNumber = random.randint(-200,200)
            if Sample[Position2][3] + ChangeNumber >0 and Sample[Position2][3] + ChangeNumber <600: 
                NewBee = (Sample[Position2][0],Sample[Position1][1],Sample[Position2][2],Sample[Position1][3] + ChangeNumber,Sample[Position2][4])
        VelocityChoice = random.randint(0,100)
        if VelocityChoice >= 90:
            ChangeNumber = random.randint(-10,10)
            if Sample[Position2][4] + ChangeNumber >0 and Sample[Position2][4] + ChangeNumber <30: 
                NewBee = (Sample[Position2][0],Sample[Position1][1],Sample[Position2][2],Sample[Position1][3],Sample[Position2][4] + ChangeNumber)

    return NewBee
run = True
Start = True
AmountOfBees = 10
Bees = []
BeesEvolution = []
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>=20:
        x = x-vel

    if keys[pygame.K_RIGHT] and x <= 950:
        x = x +vel

    if keys[pygame.K_UP] and y >=20:
        y = y -vel

    if keys[pygame.K_DOWN] and y <=550:
        y = y +vel

    if Start:
        for n in range(0,AmountOfBees):
            Info = CreateBee()
            Bees.append(Info)
            Info = Info + (0,0,)
            BeesEvolution.append(Info)
        Start = False

    BeesEvolutionTemp = []
    if not Bees:
        for x in range(0,AmountOfBees):
            if x != AmountOfBees-1:
                Info = Training(BeesEvolution)
                Bees.append(Info)
                Info = Info + (0,0,)
                BeesEvolutionTemp.append(Info)
            else:
                Info = CreateBee()
                Bees.append(Info)
                Info = Info + (0,0,)
                BeesEvolutionTemp.append(Info)         
        BeesEvolution = BeesEvolutionTemp
        AmountOfBees = AmountOfBees +1
    win.fill((0,0,0))
    pygame.draw.rect(win, (0,0,255),(950,550,1000,600))
    
    
    Temp = 0 
    for bee in Bees:
        if not (bee[0] - bee[2] <=10 and bee[0] - bee[2] >= -10 and bee[1] - bee[3] <=10 and bee[1] - bee[3] >= -10):
            pygame.draw.rect(win, (0,255,0),(bee[0],bee[1],width,height))
        if bee[0] > bee[2]:
            if bee[0] - (bee[4]//2) > bee[2]:
                Bees[Temp] = (Bees[Temp][0] - (bee[4]//2),Bees[Temp][1],Bees[Temp][2],Bees[Temp][3], Bees[Temp][4])
            else:
                Bees[Temp] = (Bees[Temp][2],Bees[Temp][1],Bees[Temp][2],Bees[Temp][3], Bees[Temp][4])
        if bee[1] > bee[3]:
            if bee[1] - (bee[4]//2) > bee[3]:
                Bees[Temp] = (Bees[Temp][0],Bees[Temp][1] - (bee[4]//2),Bees[Temp][2],Bees[Temp][3], Bees[Temp][4])
            else:
                Bees[Temp] = (Bees[Temp][0],Bees[Temp][3],Bees[Temp][2],Bees[Temp][3], Bees[Temp][4])
        if bee[0] < bee[2]:
            if bee[0] + (bee[4]//2) < bee[2]:
                Bees[Temp] = (Bees[Temp][0] + (bee[4]//2),Bees[Temp][1],Bees[Temp][2],Bees[Temp][3], Bees[Temp][4])
            else:
                Bees[Temp] = (Bees[Temp][2],Bees[Temp][1],Bees[Temp][2],Bees[Temp][3], Bees[Temp][4])
        if bee[1] < bee[3]:
            if bee[1] + (bee[4]//2) < bee[3]:
                Bees[Temp] = (Bees[Temp][0],Bees[Temp][1] + (bee[4]//2),Bees[Temp][2],Bees[Temp][3], Bees[Temp][4])
            else:
                Bees[Temp] = (Bees[Temp][0],Bees[Temp][3],Bees[Temp][2],Bees[Temp][3], Bees[Temp][4])
        Temp1 = 0
        for EvoBee in BeesEvolution:
            if EvoBee[2] == bee[2] and EvoBee[3] == bee[3]:
                Intial = ((bee[0] - x)**2) + ((bee[1] - y)**2)
                Distance = math.sqrt(Intial)
                BeesEvolution[Temp1] = (BeesEvolution[Temp1][0],BeesEvolution[Temp1][1],BeesEvolution[Temp1][2],BeesEvolution[Temp1][3],BeesEvolution[Temp1][4],BeesEvolution[Temp1][5]+Distance,BeesEvolution[Temp1][6]+1 )
            Temp1 = Temp1 +1
        
        Temp = Temp + 1
        

    if x >900 and y >500:
        Bees = []
        x = 20
        y = 20
        Level = Level + 1
    Collision = False
    for w in range(0,width):
        for h in range(0,height):
            Colour = win.get_at((x+w,y+h))
            if Colour == (0,255,0,255):
                Collision = True
                Bees = []
                BeesEvolution = []
                Level = 0
                
    if Collision:
        Start = True
        AmountOfBees = 10
        x = 20
        y = 20        
    else:
        pygame.draw.rect(win, (255,0,0),(x,y,width,height))
    text = Mediumfont.render("Level: "+str(Level), True, WHITE)
    win.blit(text,(900,30))    
    pygame.display.update()

pygame.quit()


