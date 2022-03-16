# author: LM (AMDG) 3/16/22
#opens and reads file


myfile = open('words.txt', 'r')
while True:
    myfile.readline().strip()
    if len(myfile) > 20:
        newfile = open('greater_than_20.txt', 'a')
        newfile.write(myfile)
        newfile.close()
        continue
    myfile.close()
