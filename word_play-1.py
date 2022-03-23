# author: LM (AMDG) 3/16/22
#opens and reads file


#question 1
# opens words.text file. and creates words greater than 20 file with ability to write
with open('words.txt') as infile, open('greater_than_20.txt', 'w') as outfile:
    # line is equal to the actual word
    for line in infile.readlines():
        if len(line) > 21:
            # Writes word in new file if word length is greater than 20 
            outfile.write(line)

