
def divisores(n):
    sum = 0
    for i in range(1, n+1):
        if n %i == 0:
            print(i)   
            sum = sum + i
    
    if sum > n:
        return "Abundant"
    elif sum == n:
        return "Perfect"
    else:
        return "Deficient"
    
print(divisores(12))