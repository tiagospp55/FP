import sys

def count_letter(text):
    num_caracteres = []
    for letter in text:
        if letter.isalpha():
            num_caracteres.append(ord(letter.lower()))
    cnt = []
    for i in range(97,123):
        cnt.append(num_caracteres.count(i))
    dict = {}
    for i in range(97,123):
        dict[chr(i)] = cnt[i-97]

    return dict

def main():
    file_name = sys.argv[1]
    dict = {}
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            dict = count_letter(text)
    except FileNotFoundError:
        print('Arquivo não encontrado')

    for key, value in dict.items():
        print(f'{key}: {value}')
main()

    