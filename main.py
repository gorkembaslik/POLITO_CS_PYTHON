continue_asking = True
while continue_asking:
    val = input()
        if val.upper() == 'Q':
            continue_asking = False
        else:
            values.append(float(val))


# foo daki 0 ı nasıl değiştiricem?
foo = [[2, 0], 456, 64]
foo[0][0] = 3
print(foo)

a = set()

a.add(42)
print(a)
