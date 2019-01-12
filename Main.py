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
            
        
               
        
    

done=False
Clist= ["help","test","stop","num_guess","list"]

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
        
        
        