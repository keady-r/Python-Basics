#Author Ruth Keady - Determine if weekday or weekend

import datetime

weekNumber = datetime.datetime.today().weekday()

if weekNumber < 5:
   print ("Yes, unfortunately today is a weekday")
else:
   print ("It is the weekend, yay!")
