<h1 align="center">
    Fairfield College Preparatory School<br>
    Computer Programming - Mrs. Kinskey-Lebeda<br>
    Case Study - Word Play
</h1>

<h2 align="center">Due before 8:30 AM on 3/24 (25 pts.)</h2>

### Reading and Writing Files
---
Read all instructions carefully. Answer each of the following questions in a separate Python file named `word_play-#.py` where `#` is the number of the question. In your heading, put your name and the date you began working on the file. Each of the following exercises will use the list of words which can be found in the text file `words.txt`. Try to make your programs as simple and as general as possible. The solution to one exercise may be reusable as the starting point of another.

---
Remember that files can be read line by line or all at once. Regardless of which way lines are read, each line will contain a newline character `"\n"` at the end. This character should be removed so comparisons between words or other word manipulations don't include the newline character. Adding `.strip()` to `readline.()` will remove this newline character. If `readlines()` is used, iterating through the list of strings and using `.strip()` on each string will have the same effect.

---
Remember to comment through your code explaining the major steps. Solutions without comments will earn at max 3 pts per question.

Example :
``` python
infile = open('testfile.txt')
line = infile.readline().strip()
```
---
1. Write a program that reads `words.txt` and writes to a file named `greater_than_20.txt` the words from `words.txt` that are longer than 20 characters (not counting newline characters).

2. Write a program that contains a function called `no_e` that returns `True` if the given word does not contain the letter `"e"`. Use this function to read `words.txt` and write to a file named `words_without_e.txt` the words from `words.txt` that do not contain the letter `"e"`. The program should also print to the console the percentage of words in `words.txt` that do not contain the letter `"e"`.

3. Write a program that contains a function called `avoid` that takes a word and a string of forbidden letters and returns `True` if the word does not use any of the forbidden letters. The program should prompt the user to enter a string of forbidden letters and use the function to print to the console the number of words in `words.txt` that don't contain any of the forbidden letters.

4. Write a program that contains a function called `uses_only` that takes a word and a string of letters and returns `True` if the word contains only letters in the list. The program should prompt the user to enter a string of allowed letters and then use the function to print to the console the number of words in `words.txt` that contain only the allowed letters.

5. Write a program that contains a function called `is_abecedarian` that returns `True` if the letters in a word appear in alphabetical order (double letters are ok). Use this function to read `words.txt` and print to the console the number of words in `words.txt` that are in alphabetical order.

<p align="center">Be sure to commit your code before the deadline. Only the latest commit will be graded.</p>
