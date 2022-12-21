s = input().upper()

l = [0] * 26
for c in s:
    l[ord(c)-65] += 1

a = max(l)
print(chr(l.index(a)+65) if l.count(a) == 1 else '?')