# Program to get letter count in a text file
 
# input fileName variable - mobydick.txt'used for this test. Confirmed that the count was correct by converting the txt file to word and through ctrl f replaced all the 'e's . A total of 58820 e's were removed, confirming count - (1. 2. 3. )
fileName = raw_input('Enter a filename: ') 
character = raw_input('Enter the character you wish to count:')

#Define a function that requires two inputs (the file and the letter to search for), will open the file in readonly, store the data of the file as a variable called 'content', in order to count the frequency of the letter - use the data stored in content and count the letter. Return this as the variable occurance. - (1. 4. 5. )
def function(fileName, character):
    file = open(fileName, 'r')
    content = file.read()
    occurance = content.count(character)
    return occurance

print("The Number of times  the character",character, "is used in the file is", function(fileName, character))

#END
#References:
#1. Lecture 
#2. input the filename in the commandline as an argument https://askubuntu.com/questions/1059579/input-the-filename-in-the-commandline-as-an-argument-in-python
#3. Python count occurances https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/
#4. Python read text files https://pythonexamples.org/python-read-text-file/
#5. Python tutorial https://www.pythontutorial.net/python-basics/python-read-text-file/




