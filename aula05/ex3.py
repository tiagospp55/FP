def inputFloatList():
    list = []
    while 1:
        x = input("Digite um número ou ENTER para terminar: ")
        if x == '': break
        x = float(x)
        list.append(x)

    return list

def countLower(lisst, v):
    count = 0
    for num in lisst:
        if num < v:
            count += 1
    return count

def minmax(list):
    mx = 0
    mn = 100000

    for i in list:
        if i > mx:
            mx = i
        if i < mn:
            mn = i
    
    return mn,mx

def main():

    list = []
    list = inputFloatList()
    print("A lista é: ", list)
    mn, mx = minmax(list)
    medium = (mn + mx) / 2
    print("O menor valor é: ", mn)
    print("O maior valor é: ", mx)
    print("A média dos valores é: ", medium)
    lower = countLower(list, medium)
    print("Os valores menores que a média são: ", lower)


main()