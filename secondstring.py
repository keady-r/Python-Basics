#Author Ruth Keady 
#Task 3 

#Here we are defining a function x, splicing it and returning every second number#
#What happens if we take the '-' sign away = Every second letter is returned but it is not reversed#
#What happens if I do return x[-2]. All that is returned is g i.e. the second element. 
#What happends if I do return x[:-2]. Whole sentence is printed in order but the 'g' is removed


#defining the function using the def command - naming the function - in brackets are the values that are to be entered into the function - return statement defines what you want to happen to the value inputted into the function - (1.2)

def my_function(x):
  return x[::-2]

mytxt = my_function("The quick brown fox jumps over the lazy dog ")

print(mytxt)

#END

#References:
#1. Lecture Notes 
#2. w3 Schools - How to reverse a string in python https://www.w3schools.com/python/python_howto_reverse_string.asp