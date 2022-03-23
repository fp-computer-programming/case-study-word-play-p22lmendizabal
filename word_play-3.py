# author: LM (AMDG) 3/23/22
# question 3
# if the letter is in the word then it returns false
def avoid(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True
# user inputs forbidden letters
string = input("Enter a string of forbidden letters: ")

with open('words.txt') as infile:
    words = []
    for line in infile.readlines():
        # if fucntion is True then the word is appended to words list
        avoid(line, string)
        if avoid(line, string) == True:
            words.append(line)
    print(words)