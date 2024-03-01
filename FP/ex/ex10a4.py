
#ex10 a4

def primos(num):        


    while True:
        i=0
        i= i+1
        divisivel = 0
        if num % i:
            if i !=num :
                print (i)
                return (True)
        if i>=100: 
            break










    return False
def main ():
    num = int (input ("introduza o numero-"))
    if primos (num):
        print("o numero não é primo")
    else :
        print("o numero e primo")
main()