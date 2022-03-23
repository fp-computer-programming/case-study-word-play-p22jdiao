# Author: JD 03/23/2022
# the function use <= to check if the letters within a word are in order
def is_abecedarian(word):
    w = list(word)
    # x starts with 1 so the while loop will check letter at x index and x - 1
    x = 1
    while x < len(word):
        # if any of the letters are not in order the function will return False
        if not w[x] >= w[x-1]:
            return False
        
        x += 1

    return True

words = open("words.txt")

word = words.readlines()
num = 0
# it is important to use .strip() method to get rid of escape characters
# if the word is abecedarian, variable num will plus one
for y in word:
    y = y.strip()
    if is_abecedarian(y) == True:
        num += 1

print(num)

words.close()