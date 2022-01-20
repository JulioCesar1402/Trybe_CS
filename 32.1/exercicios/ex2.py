def mean(lista):
    sum = 0
    n = len(lista)
    for item in lista:
        sum += item
    print(sum / n)


mean([1, 2, 3])
