import random
def test():
    ''' prints out test 50 times'''
    for x in range(0,50):
        print("test")
        
def comand_list():
    print(Clist)
    ''' prints out list of commands'''
def number_guess():
    ''' runs number guess game '''
    print("numGame")
    score = 0
    
    rand_num = random.randint(0,100)
    
    game = True
    
    while game:
        
        score +=1
        numG = int(input("input number "))
        
        if numG == rand_num:
            print("you win! ")
            print("your score is:") 
            print(score)
            break
        
        elif numG <= rand_num:
            print("Too low! ")
            
        elif numG >= rand_num:
            print("Too High! ")
def Help(): 
    '''provides help on most commands '''
    Done = False
    print("to exit help use the stoph command")
    while not Done:
        x = input("Help Ready? ")
        if x == "help":
            print("prints out help for the command in question ")
        elif x == "test":
            print("prints out test 50 times" )
        elif x == "stop":
            print("exits any program in the os ecept help") 
        elif x == "num_guess":
            print("runs the built in game num_guess")  
        elif x == "list":
            print("lists out all commands ")
        elif x== "stoph":
            break
        elif x == "SuperNova":
            print("runs the built in game SuperNova")
        elif x == "self_destruct":
            print("classified ")
        elif x == "flip":
            print("flips an coin x amount of times")
        elif x == "blackJack":
            print("runs the game black jack")
            
def SuperNova():
    ''' the (still in devlopment) rpg by startSpace Interactive.'''
    
 
    import pygame
 
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
 
 
    def draw_stick_figure(screen, x, y):
        '''draws a stick figure, big surprise'''
        # Head
        pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
 
        # Legs
        pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
        pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
 
        # Body
        pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [5 + x, 7 + y], 2)
 
        # Arms
        pygame.draw.line(screen, BLACK, [5 + x, 7 + y], [9 + x, 17 + y], 2)
        pygame.draw.line(screen, BLACK, [5 + x, 7 + y], [1 + x, 17 + y], 2)
    

 
    # Setup
    pygame.init()
 
    # Set the width and height of the screen [width,height]
    size = [700, 500]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("SuperNova")
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # Hide the mouse cursor
    pygame.mouse.set_visible(0)
 
    # Speed in pixels per frame
    x_speed = 0
    y_speed = 0
 
    # Current position
    x_coord = 10
    y_coord = 10
 
    # -------- Main Program Loop -----------
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            # User pressed down on a key
 
            elif event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.
                if event.key == pygame.K_a:
                    x_speed = -3
                elif event.key == pygame.K_d:
                    x_speed = 3
                elif event.key == pygame.K_w:
                    y_speed = -3
                elif event.key == pygame.K_s:
                    y_speed = 3
 
            # User let up on a key
            elif event.type == pygame.KEYUP:
                
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_speed = 0
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    y_speed = 0
 
        # --- Game Logic
 
        # Move the object according to the speed vector.
        x_coord = x_coord + x_speed
        y_coord = y_coord + y_speed
 
        # --- Drawing Code
 
        # First, clear the screen to WHITE. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)
 
        draw_stick_figure(screen, x_coord, y_coord)
    
 
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
        # Limit frames per second
        clock.tick(60)
 
        # Close the window and quit.
    pygame.quit()          
def self_destruct():
    ''' self destructs the program or at least it tries to '''
    import time
    def countdown(n):
        while n > 0:
            time.sleep(1)
            n -= 1
            print(n)


    print("initiating self destruct sequence ")
    countdown(11)
    print("hmm , something was supposed to happen there ")
    time.sleep(1)
    print("oh well") 
def flip(times):
    ''' flips a coin'''
    while times > 0:
        rnum = random.randint(1,2)
        print(rnum)
        times -= 1    
def blackJack():
    ''' the card game bakc jack '''
    print("not implmented yet ")

done=False
Clist= ["help","test","stop","num_guess","list","yes","no","SuperNova","self_destruct","flip","blackJack"]
print("we recomend that you use the list command first, as it gives you a list of all the commands in this OS,")
#main loop
while not done:
    ans= input("Ready? ")
    
    if ans == "test":
        test()
    elif ans == "list":
        comand_list()
    elif ans == "stop":
        done = True
    elif ans =="num_guess":
        number_guess()
    elif ans == "help":
        Help()
    elif ans == "SuperNova":
        SuperNova() 
    elif ans == "no":
        print("yes, yes you are")
    elif ans == "yes":
        print("are you sure?")
    elif ans == "self_destruct":
        self_destruct()
    elif ans == "flip":
        flip(int(input("times to flip the coin ")))  
    elif ans == "blackJack":
        blackJack() 