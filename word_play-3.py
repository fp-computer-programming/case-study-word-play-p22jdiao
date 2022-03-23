# Author: JD 03/23/2022
# The function will use a for loop to check if the word contains the forbidden letters

def avoid(word,string):
    # turn the entered string/letters into a list so that it is easier for checking
    li = list(string)
    for x in word:
        if x in li:
            return False
            # if the word contains any of the forbidden letters then it will return False
    
    return True

words = open("words.txt")

word = words.readlines()
num = 0
forb_w = input("Enter the forbidden letters: ")
# Use a for loop to interate through the file to check if each word contains the letters, if not, the variable num will plus 1
for y in word:
    y = y.strip()
    if avoid(y,forb_w) == True:
        num += 1

print("There are {0} words don't contain the forbidden letters.".format(num))

words.close()
