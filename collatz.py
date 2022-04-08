#Author Ruth Keady 

#Need to define what value should be entered 
Num = input ("Please enter a positive integer number: ")

#Entering a limit on the number that can be entered into the loop to prevent endless loop. What the code is stating below : starts with a while loop i.e. it will take the result and input it again into the code. This loop will run as long as the value going into the loop is greater than 1 and less than 100. If a number is reached outside of this range it will not process it through the code. Once the parameters are accurante the next line of code commences (line8). If the number is even (determined by the %2 ==0 i.e. there are no remaining values left over when divided by two then the number is even ). Line 9 then divides the number by two (it is written in this way i.e /= 2 so that it will be applied to every number that comes through the loop but can also be written as Num = Num/2 .. just trying to show variety ) and line 10 prints the number. Line 11 has the else statement that redirects the code to do something different if the initial parameter of the if statement is not met i.e if the num is odd. line 12 and 13 carry out the function and print the result. 
while Num > 1 and Num <100:
    if Num %2 ==0:
        Num /= 2
        print (Num)
    else:
        Num = ((Num *3) +1)
        print (Num)

#END

#References:
#1. Lecture notes
#2. W3 schools : While loops https://www.w3schools.com/python/python_while_loops.asp
#3. W3 schools : If Else loops https://www.w3schools.com/python/python_conditions.asp