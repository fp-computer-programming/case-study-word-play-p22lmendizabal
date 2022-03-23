# auhtor: LM (AMDG) 3.23.22
# question 4
def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

string = input("Enter a string of allowed letters: ").strip()
# if the letters are in the word then it is appended to words list
with open('words.txt') as infile:
    words = []
    for line in infile.readlines():
        uses_only(line, string)
        if uses_only(line, string) == True:
            words.append(line)
    print(words)
        
