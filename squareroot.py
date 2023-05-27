#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.You should create a function called <tt>sqrt</tt> that does this.

def sqrt(n, l) :
    x = n
    count = 0
 
    while (1) :
        count += 1
        answer = 0.5 * (x + (n / x))
 
        # Determine if the answer is within the tolerance level - if the absolute value of teh answer - x is less than the tolerance define then break 
        if (abs(answer - x) < l) :
            break
        x = answer
 
    return round (answer,1)

if __name__ == "__main__" :
 
    n = float(input("please enter a positive number: "))
    l = 0.00001
 
    print("The approximate square root of", n, "using Newtons Method is", sqrt(n, l))
