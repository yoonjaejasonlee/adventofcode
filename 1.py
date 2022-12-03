X = [l.strip() for l in open('1.ex')]

q = []
ans = 0
for x in ('\n'.join(X)).split('\n\n'):
    y = 0
    for x in x.split('\n'):
        y += int(x)
    q.append(y)

q = sorted(q)
print(q)
for i in q[-3:]:
    ans += i

print(ans)