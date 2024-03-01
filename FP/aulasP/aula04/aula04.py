def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def leibniz(n):
    pi = 0
    for i in range(n):
        pi += (-1)**i/(2*i+1)
    return 4*pi

def real():
    sum = 0
    cnt = 0
    while 1:
        x = input("Enter a number: ")
        if x == '': break
        sum = sum + int(x)
        cnt = cnt + 1

    sum = sum/cnt
    print("The average is", sum)

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

print("fatorial",factorial(3))
print("leibniz",leibniz(1000000))
real()
print("Prime",isPrime(4))

