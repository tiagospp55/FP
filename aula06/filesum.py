from tkinter import filedialog

def main():
    # 1) Pedir nome do ficheiro (experimente cada alternativa):
   # name = input("File? ")                                  #A
    #name = filedialog.askopenfilename(title="Choose File") #B
    fileSum()
    # 2) Calcular soma dos números no ficheiro:
    total = fileSum(nums.txt)
    
    # 3) Mostrar a soma:
    print("Sum:", total)


def fileSum():
    # Complete a função para ler números do ficheiro e devolver a sua soma.
    f= open("nums.txt" ,"r")
    i =0
    # numbers[100] = 0
    for line in f:
        fline = f.readline
        print(fline)

if __name__ == "__main__":
    main()

