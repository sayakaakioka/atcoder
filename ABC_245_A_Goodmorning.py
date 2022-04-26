def f(x, y):
    return x*60+y

A, B, C, D = map(int, input().split())
t = f(A, B)
a = f(C, D) + 1

if t < a:
    print('Takahashi')
else:
    print('Aoki')
