# Author: JD 03/23/2022

# this time it is easier to check if the letters within the "use only" string is within the word.
# so we use a if not conditional this time
def uses_only(word,letters):
    l = list(letters)
    w = list(word)
    for x in letters:
        if x not in w:
            return False
    
    return True

words = open("words.txt")

word = words.readlines()
num = 0
u_w = input("Enter the uses only letters: ")
# the variable num will record the number of words with use only letters
for y in word:
    y = y.strip()
    if uses_only(y,u_w) == True:
        num += 1

print("There are {0} words contain the use only letters.".format(num))

words.close()