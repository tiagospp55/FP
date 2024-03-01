def polinomium(x):
    return x**2 + 2*x +3

def max(x,y):
    if x > y:
        return x
    else:
        return y
    
def max3(x,y,z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z
    
def tax(r):
    assert r > 0, "Tax rate must be positive"

    if r <= 1000:
        return 0.1 * r
    elif r <= 2000 and r >= 2000:
        return 0.2 * r
    else:
        return 0.3 * r
    
def intersepts(a,b,c,d):
    assert a < b and c < d, "Invalid interval"
    if b < c:
        return True    
    return False

def hms2sec(h,m,s):
    return h*3600 + m*60 + s

def sec2hms(s):
    h = s // 3600
    s = s % 3600
    m = s // 60
    s = s % 60
    return h,m,s

def countdown(N):
    for i in range(N,0,-1):
        print(i)
    print("Fogo!")

def main():
    menu = input("Escolha o exercicio: ")

    if menu == '1':
        print("Polinômio")
        for i in range(0,3):
            print("f(",i,") = ",polinomium(i))
        print("f(f(1)) = ",polinomium(polinomium(1)))
    elif menu == '2':
        print("Maximo")
        x = int(input("Digite o valor de x: "))
        y = int(input("Digite o valor de y: "))
        print("O maior valor é: ",max(x,y))
    elif menu == '3':
        print("Máximo 3 ")
        x = int(input("Digite o valor de x: "))
        y = int(input("Digite o valor de y: "))
        z = int(input("Digite o valor de z: "))
        print("O maior valor é:", max3(x,y,z))
    elif menu == '4':
        print("Taxa")
        r = float(input("Digite o valor da taxa: "))
        print("O valor do imposto é: ",tax(r))
    elif menu == '5':
        print("Intervalo")
        a = int(input("Digite o valor de a: "))
        b = int(input("Digite o valor de b: "))
        c = int(input("Digite o valor de c: "))
        d = int(input("Digite o valor de d: "))
        print("Os intervalos se interceptam? ",intersepts(a,b,c,d))
    elif menu == '6':
        print("Conversão de tempo")
        h = int(input("Digite a hora: "))
        m = int(input("Digite os minutos: "))
        s = int(input("Digite os segundos: "))
        print("O tempo em segundos é: ",hms2sec(h,m,s))
        print("O tempo em horas, minutos e segundos é: ",sec2hms(hms2sec(h,m,s)))
    elif menu == '7':
        print("Countdown")
        N = int(input("Digite o valor de N: "))
        countdown(N)
    


if __name__ == "__main__":
    main()
