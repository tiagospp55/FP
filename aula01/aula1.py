import math
def temperatura(temperatura):
    fahrenheit = 9*temperatura/5 + 32
    return fahrenheit

def idade(ano_nascimento):
    idade = 2024 - ano_nascimento
    return idade

def formatar_data(segundos):
    minutos = segundos//60
    segundos = segundos%60
    horas = minutos//60
    minutos = minutos%60
    dias = horas//24
    horas = horas%24
    return "{:02d}:{:02d}:{:02d}:{:02d}".format(dias, horas, minutos, segundos)

def elevador():
    for i in range(0,4):
        trips = i * 4 * 3
    distance = trips*365
    print("O elevador fez ",distance," tempo em viagem")
    distance = distance/1000
    print("O elevador fez ",distance," km em viagem")

def pitagoras(a,b):
    c = (a**2 + b**2)**0.5
    a = math.atan(b/a)
    return (c,a) #retorna a hipotenusa e o cateto a

def livros(PF,PC, IMP,SPA, exemplares):
    lucro = (0-PF) + (PC-SPA)/(1+IMP/100)
    impostos = PC * 0.23 * exemplares
    taxas = exemplares * 0.2
    return (lucro * 500, impostos, taxas)

def main():
    print("Temperatura a 100ºCelsius é ",temperatura(100))
    print("Idade de uma pessoa nascida em 1990 é ",idade(2001))
    print("Formatar 100000 segundos é ",formatar_data(1000))
    elevador()
    print("Pitagoras de 3 e 4 é ",pitagoras(3,4)[0], " e o angulo é ",pitagoras(3,4)[1])
    print("Lucro de um livro é ",livros(20,24.95,23,0.2, 500)[0], " impostos ",livros(20,24.95,23,0.2, 500)[1], " e taxas ",livros(20,24.95,23,0.2, 500)[2])
    

if __name__ == "__main__":
    main()
