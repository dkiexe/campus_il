def numz(symbol, range):
    return ", ".join(list(map(lambda num: symbol + str(num), range)))

print(numz('$',range(10)))