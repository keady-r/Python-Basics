# Program to get letter count in a text file

fileName = 'mobydick.txt'
character = raw_input('Enter the character you wish to count:')

def function(fileName, character):
    file = open(fileName, 'r')
    content = file.read()
    occurance = content.count(character)
    return occurance

print("The Number of times  the character",character, "is used in the file is", function(fileName, character))


