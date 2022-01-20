PI = 3.14


def square(side):
    """Calculate area of square"""
    return side * side


def rectangle(length, width):
    """calculate area of rectangle"""
    return length * width


def circle(radius):
    """Calculate area of circle"""
    return PI * radius * radius


# .. se executado puro, ao realizar uma importação o teste será executado
# print("Área do quadrado:", square(10))
# print("Área do retângulo:", rectangle(2, 2))
# print("Área do círculo:", circle(3))

'''
 ao adicionar o condicional, o teste só será executado
            caso esse seja o script chamado
'''
if __name__ == "__main__":
    print("Área do quadrado:", square(10))
    print("Área do retângulo:", rectangle(2, 2))
    print("Área do círculo:", circle(3))
