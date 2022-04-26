def f(x, y, z, X):
    cycles = X // (x+z)
    m = X % (x+z)
    return x*y*cycles + min(x, m)*y


A, B, C, D, E, F, X = map(int, input().split())

t = f(A, B, C, X)
a = f(D, E, F, X)

if t>a:
    print('Takahashi')
elif t<a:
    print('Aoki')
else:
    print('Draw')

