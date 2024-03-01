# Complete este programa como pedido no guião da aula.

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {}".format("Numero", "Nome"))
    for num in dic:
        print("{:>12s} : {}".format(num, dic[num]))

def filterPartName(contacts, partName):
    """Returns a new dict with the contacts whose names contain partName."""

    newContacts = {}
    for key, values in contacts.items():
        if partName in values:
            newContacts[key]=contacts[key]

    return newContacts

def addcont(dic):
    number = input("number")
    name = input("name")
    dic[number]=name
    print("done")
    return dic

def rmcont(dic):
    print(type(dic))
    while (True):
        number = input("number")
        if number == (""): break
        if number in dic.keys():
            del(dic[number])
            print("done")
            break
        else :
            print("there is no contact w that number")

def procn(dic):
    num =input("numero")
    print(dic.get(num))

def proc(dic):
    name = input("Nome ")
    if name in dic.values():
        print("Nome:",name)

#    name = input("Nome ")
#    keyls= list(dic.keys())
#    valls=list(dic.values())
#    if name in valls:
#        position =valls.index(name)
#        print ("Cont-{},{}".format(keyls[position],name)) 
#    else :
#        print("Noone with that name in contacts")
def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op


def main():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": "Universidade de Aveiro",
        "727392822": "Cristiano Aveiro",
        "387719992": "Maria Matos",
        "887555987": "Marta Maia",
        "876111333": "Carlos Martins",
        "433162999": "Ana Bacalhau",
        "1":"t"
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op=="A":
            addcont(contactos)
        elif op=="R":
            rmcont(contactos)
        elif op=="N":
            procn(contactos)
        elif op=="P":
            proc(contactos)
        elif op=="F":
            print("Filtro")
            partName = input("Parte do nome: ")
            newContacts = filterPartName(contactos, partName)
            listContacts(newContacts)
        else:
            print("Não implementado!")
    

# O programa começa aqui
main()

