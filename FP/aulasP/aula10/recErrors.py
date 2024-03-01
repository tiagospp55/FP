
# Calcula o factorial de n, baseado na recorrencia n! = n*(n-1)!.
# Mas não termina!  Detete a causa e corrija o erro.
from time import process_time_ns


def fact(n):
    if n>1:
        return n*fact(n-1)
    else : return 1


# Calcula o maximo divisor comum entre a e b.
# Baseia-se no algoritmo de Euclides.
# Mas não termina!  Detete a causa e corrija o erro.
def gcd(a, b):
    
    if b == 0:
        print(a)
        return a
        
    if a ==0:
        print(b)
        return b
    
    if a <= b :
        b -=a
    if  a>=b :
        a-=b    
    
    #if a!=0 and b!=0 :
    return gcd (a,b)
    


def main():
    print( fact(4) )    # 24
    print( fact(5) )    # 120

    x = 2*27*53*61
    y = 2*2*17*23*53
    print(x, y, gcd(x, y))

if __name__ == "__main__":
    main()

