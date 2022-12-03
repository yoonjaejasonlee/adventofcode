ans = 0
X = [line for line in open('3.txt')]
i = 0

while i < len(X):
    for c in X[i]:
        if c in X[i+1] and c in X[i+2]:
            if 'a' <= c <= 'z':
                ans += ord(c) - ord('a') + 1
            else:
                ans += ord(c) - ord('A') + 1 + 26
            break
    i += 3

print(ans)

for line in open('3.txt'):
    x = line.strip()
    y = x[:len(x)//2]
    z = x[len(x)//2:]

    for a in y:
        if a in z:
            pass

