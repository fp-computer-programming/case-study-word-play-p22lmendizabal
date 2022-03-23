# author: LM (AMDG) 3/23/22
# question 2
# function that returns true if there is no e
def no_e(word):
    if "e" not in word:
        return True
    else: return False

#opens file words and creats new file to put in words with no e
with open('words.txt') as infile, open('words_without_e.txt', 'w') as outfile:
        for line in infile.readlines():
            if 'e' not in line:
                outfile.write(line)
                print(no_e(line))