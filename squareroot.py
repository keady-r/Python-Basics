#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.You should create a function called <tt>sqrt</tt> that does this.

#Please enter a positive number: 14.5
#The square root of 14.5 is approx. 3.8.

#Newtons square root. Let n be any number then the square root of N can be given by the formula: root =0.5*(x+(n/x)) where x is any guess which can be assumned to be N or 1.  n = number, l= tolerance.  

#Define the function (1.2.3.4)
def sqrt(n, l) :
 
    # define varialbe x. As per newtons method - x is any guess which can be assumned to be N or 1
    x = n
 
    # To count the number of iterations need to include a while loop to add subsequent counting. Define the count starts at 0. 
    count = 0
 
    while (1) :
        count += 1
        #Newtons method
        answer = 0.5 * (x + (n / x))
 
        # Determine if the answer is within the tolerance level - if the absolute value of teh answer - x is less than the tolerance define then break 
        if (abs(answer - x) < l) :
            break
 
        # Updated root
        x = answer
 
    return round (answer,1)
 
# Driver code (5.)
if __name__ == "__main__" :
 
    n = float(input("please enter a positive number: "))

    l = 0.00001
 
    print("The approximate square root of", n, "using Newtons Method is", sqrt(n, l))

#END 
#References:
#1. Lecture Notes 
#2. Newtons Method - https://en.wikipedia.org/wiki/Newton%27s_method
#3. Real Python - https://realpython.com/python-square-root-function/
#4. Geeks for Geeks - Maths functions https://www.geeksforgeeks.org/python-math-function-sqrt/#:~:text=sqrt()%20function%20is%20an,number%20passed%20in%20the%20parameter.
#5. How to incorporate driver code https://stackoverflow.com/questions/19044558/creating-and-using-a-driver-function-how-does-it-work

