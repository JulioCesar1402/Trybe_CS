# Exercício 1: Faça um programa que receba um nome e
# imprima o mesmo na vertical em escada invertida. Exemplo:

def inverted_ladder(name):
    for removed_letters in range(len(name)):
        for letter in range(len(name) - removed_letters):
            print(name[letter], end="")
        print()


if __name__ == '__main__':
    name = input('Digite seu nome: ')
    inverted_ladder(name)
