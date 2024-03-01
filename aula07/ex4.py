

from typing import Counter


def main():
    file = open("3333.txt" ,"r")
    i=0
    for line in file:
        for i in line.len:
            line.lower()
            ce = "ç"
            count =dict()
            for let in range(97,122,1):
                letter = ascii (let)
                if(line[i].isalpha(letter)):
                    if letter not in count:
                        count [letter] = 1 
                    elif True: 
                        count [letter] =+1
            if(line[i].isalpha(ce)):
                if 'ce' not in count:
                    count ['ce'] = 1 
                elif True: 
                    count ['ce'] =+1
            i=i+1






















if (__name__ == "__main__"):
    main()
