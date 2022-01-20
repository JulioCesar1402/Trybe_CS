def find_biggest_name(lista):
    count = 0
    result = ""
    for name in lista:
        if len(name) > count:
            result = name
            count = len(name)
    print(result)


find_biggest_name(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"])
