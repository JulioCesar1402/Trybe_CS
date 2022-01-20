numbers = input("Insira valores aqui, separados por espaço: ")

array_of_numbers = numbers.split(" ")

sum = 0
for number in array_of_numbers:
    if not number.isdigit():
        print(f"Erro ao somar valores, {number} não é um dígito.")
    else:
        sum += int(number)

print(f"A soma dos valores válidos é: {sum}")
