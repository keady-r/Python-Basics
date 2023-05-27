#Author Ruth Keady 

#Requirements:
#1. allow user to input values use input function
#2. need to assign a type - in this case it's a float. Decimal point needed 
#3. define the calculation for the BMI (weight kg / height meters squared )
#4. Use print function to display value..

def my_function(x,y):
    return ((y)/((x/100)**2))

weight3 = float(input("Enter weight in kg: "))
height3 = float(input("Enter height in cm: "))
convert3 = my_function(height3,weight3)
BMI3 = round((convert3),2)

print(BMI3)
