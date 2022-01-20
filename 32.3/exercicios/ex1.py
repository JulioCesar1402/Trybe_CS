
# divisíveis por 3 -> 'Fizz' ao invés do número;
# divisíveis por 5 -> como 'Buzz' ao invés do número;
# divisíveis por 3 e 5 -> como 'FizzBuzz' ao invés do número';

def fizz_buzz(number):
    numbers = []
    for ranged_number in range(1, int(number) + 1):
        if ranged_number % 3 == 0 and ranged_number % 5 == 0:
            numbers.append('FizzBuzz')
        elif ranged_number % 3 == 0:
            numbers.append('Fizz')
        elif ranged_number % 5 == 0:
            numbers.append('Buzz')
        else:
            numbers.append(ranged_number)
    print(numbers)


if __name__ == '__main__':
    number = input('Insert your number: ')
    fizz_buzz(number)
