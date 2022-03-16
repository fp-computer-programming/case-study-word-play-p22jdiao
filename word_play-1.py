# Author: JD 03/16/2022

# open the files, new file created "file.txt" will be opened as append mode
words = open("words.txt")
file = open("file.txt","a")

word = words.readlines()
for x in word:
# Interate through the list "words", use .strip() format to remove the escape characters, then check if the word is longer than 20

    if len(x.strip()) > 20:
        file.write(x)

words.close()
file.close()