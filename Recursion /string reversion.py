def reverse(s):
    if s == "":
        return s
    return s[-1]+reverse(s[:-1])

print(reverse("dog"))