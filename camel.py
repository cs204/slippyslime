CamelCase = input("Верблюжий стиль: ")
for symbol in CamelCase:
    if symbol.isupper():
        CamelCase = CamelCase.replace(symbol,'_' + symbol.lower())
print(CamelCase)
