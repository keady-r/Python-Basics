#Author Ruth Keady - 


# Import Module
import datetime

# To Get the Week Number
weekNumber = datetime.datetime.today().weekday()
#weekNumber = 6 test to see if it changes manually 

if weekNumber < 5:
   # return commance for weekday 
   print ("Yes, unfortunately today is a weekday")
else:
   # return command for weekend
   print ("It is the weekend, yay!")

#END

#References 
#1. Lecture
#2. https://www.tutorialsrack.com/articles/324/how-to-find-the-current-day-is-weekday-or-weekends-in-python
#3. w3schools : if/else https://www.w3schools.com/python/python_conditions.asp 
#4. w3schools: Dates https://www.w3schools.com/python/python_datetime.asp
