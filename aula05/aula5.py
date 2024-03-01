def countDigits(string):
    digits = []
    for s in string:
        if s.isdigit():
            digits.append(s)

    return digits

def shorten(string):
    abr = ""
    for s in string:
        if s.isupper():
            abr = abr + s

    return abr

def polindromo(s):
    for i in range(len(s)):
        if s[i] != s[-1-i]:
            return False
    else: return True

def evenThenOdd(string):
    even = ""
    odd = ""
    for i,s in enumerate(string):
        if i % 2 == 0:
            even = even + s
        else:
            odd = odd + s
    
    return even+odd

def mississipi(string):
    char = string[0]
    for i in range(1,len(string)-1):
        if string[i] != string[i+1]:
            char = char + string[i]

    if string[-1] != char[-1]:
        char = char + string[-1]
    return char

def repeat(N):
    list = []
    for i in range(1,N+1):
        for j in range(1,i+1):
            list.append(i)
    return list

def max(list):
    mx = 0
    for i in list:
        if i > mx:
            mx = i
    for i in range(len(list)):
        if list[i] == mx:
            return i

print(countDigits("1234567890"))
print(shorten("Universidade Federal do Rio de Janeiro"))
print(polindromo("arara"))
print(polindromo("ararar"))
print(evenThenOdd("abcd"))
print(mississipi("mississipi"))
print(repeat(6))
print(max([1,2,3,4,10,6,7,8,9,10]))

