


def  main():
    lstsize = int(input("lst size"))
    list =[]
    for i in range (lstsize) :
        lst=int(input("type the array"))
        list . append(lst) 
                
    list = sorted(list)
    print (medianas(list))



def medianas (lst):
    midle = len(lst)/2
    if midle%1!=0:
        mediana = lst[ int (midle)]
        return mediana

    for i in range (len(lst)):
        if i >= midle:

            mediana=(lst[i]+lst[i-1])/2
            return mediana
    


main()