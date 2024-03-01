

def main():
    file = open("demofile.txt" ,"r", encoding="utf-8")
    i=0
    letterss= {}
    for line in file:
        for i in range(len(line)):
            line = line.lower()
            if line[i].isalpha() == False:
                continue
            if line[i] in letterss.keys():
                letterss[line[i]] = letterss[line[i]]+1
            else:
                letterss[line[i]] =1
    letters = letterss.items()
    letters = sorted(letters , reverse=True , key= lambda t:(t[1]) )          
    print (letters)
    

                
            
           






















if (__name__ == "__main__"):
    main()
