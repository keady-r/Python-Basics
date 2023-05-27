#Author Ruth Keady 

#Need to define what value should be entered 
Num = input ("Please enter a positive integer greater than 1: ")

# If the number is even then divide the number by two until it can not longer be devided by 2. If the result of the devide is uneven multiple it by 3 and add 1. If one is entered then return nothing 
while Num > 1 and Num <100:
    if Num %2 ==0:
        Num /= 2
        print (Num)
    else:
        Num = ((Num *3) +1)
        print (Num)
