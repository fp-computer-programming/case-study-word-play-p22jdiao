# Author: JD 03/23/2022
# use for loop to check if a word contains e
def no_e(a_word):
    for x in a_word:
        if x == "e":
            # if the word contains e then the function will return false
            return False

    return True

words = open("words.txt")
file = open("words_without_e.txt","a")

word = words.readlines()
# this variable will record the total number of words
w_num = 0
# this variable will record the total number of no e words
ne_num = 0
for y in word:
    y = y.strip()
    # for each loop w_num will plus 1 so eventually it will be equal to the total number of words
    w_num += 1
    if no_e(y) == True:
        file.write(y)
        ne_num += 1
        # if the word does not contain e then ne_num will plus one, and the newly created file will be appended the word


# p will calculate the percentage of no e words
p = ne_num / w_num * 100
print("{:.4f} percent of words do not contain e".format(p))
words.close()
file.close()