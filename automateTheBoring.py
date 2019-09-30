#### AUTOMATE THE BORING STUFF #####
#end changes the last character (in this case from newline to "")
print("Hello", end="")
print(" world")

#Ch.3 Collatz_Conjecture challenge
#https://en.wikipedia.org/wiki/Collatz_conjecture
def collatz(nbr=0):
    nbr = int(nbr)
    while(nbr != 1):
        if(nbr == 0):
            print('Choose a number to run the Collatz Sequence on ')
            nbr = input()
            nbr = int(nbr)
            
        elif(nbr != 0 | 1):
            
            if(nbr % 2 == 0):
                nbr = nbr/2
                print(' was even: nbr = ' + str(nbr))
                collatz(nbr)
                break
            elif(nbr % 2 == 1):
                nbr = 3*nbr + 1
                print(' was odd: nbr = ' + str(nbr))
                collatz(nbr)
                break
    
    #Seems to work. If i didnt have the breaks..
    #..I think it was running residually like nested recursions or something
        
    
collatz()