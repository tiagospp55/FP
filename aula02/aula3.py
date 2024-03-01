# coding: utf-8
# This program finds the maximum of two numbers.
# It uses the built-in max function.
# Can you do it with a conditional statement (if / if-else) instead?
def max3():
    x1 = float(input("number? "))
    x2 = float(input("number? "))
    x3 = float(input("number? "))
    # Use a conditional statement instead of max function!
    #mx = max(x1, x2)

    if x1 > x2 and x1 > x3:
        mx = x1
    elif x2 > x1 and x2 > x3:
        mx = x2
    else:
        mx = x3


    print("Maximum:", mx)

def par():
    x = int(input("number? "))
    if x % 2 == 0:
        print("Par")
    else:
        print("Impar")

def gasolineira():
    l = float(input("Litros? "))

    if l > 40:
        print("Total: ", l*1.4*0.9)
    else:
        print("Total: ", l*1.4)

def grades():
    grade = int(input("Nota? "))
    

#max3()
#par()
gasolineira()