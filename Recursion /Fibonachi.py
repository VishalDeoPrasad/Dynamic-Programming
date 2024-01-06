def febo(n):
    if n <= 1:
        return n
    return (febo(n-1)+febo(n-2))

print(febo(7))