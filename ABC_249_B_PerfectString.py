import itertools

S = input()
l = list(S)

if len(S) > len(set(l)):
    print('No')
elif S.islower() or S.isupper():
    print('No')
else:
    print('Yes')