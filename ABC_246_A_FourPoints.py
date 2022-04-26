S = [input().split() for i in range(3)]

if S[0][0] == S[1][0]:
    x = S[2][0]
elif S[0][0] == S[2][0]:
    x = S[1][0]
else:
    x = S[0][0]

if S[0][1] == S[1][1]:
    y = S[2][1]
elif S[0][1] == S[2][1]:
    y = S[1][1]
else:
    y = S[0][1]

print('{} {}'.format(x, y))