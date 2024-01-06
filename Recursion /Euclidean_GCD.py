def GCD(a,b):
    #base case: if b/a(without a remainder) then b is gcd
    if a%b==0:
        return b
    
    return GCD(b, a%b)

print(GCD(24,9))

def gcd_iter(a,b):
    while a%b != 0:
        a,b = b, a%b
    return b
print(gcd_iter(24,9))