def outer(n):
    def inner(x):
        nonlocal n
        n += 1
        print(n)
    return inner

f = outer(5)
print(f(1))
