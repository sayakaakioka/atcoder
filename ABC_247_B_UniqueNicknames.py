import itertools

N=int(input())
l = list(itertools.chain.from_iterable([input().split() for i in range(N)]))

if len(set(l)) < 2*(N-1)+1:
    print('No')
else:
    print('Yes')