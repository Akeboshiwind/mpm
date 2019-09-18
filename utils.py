def concatPaths(a, b):
    if a[-1] == "/":
        a = a[:-1]

    if b[0] == "/":
        b = b[1:]

    return a + "/" + b
