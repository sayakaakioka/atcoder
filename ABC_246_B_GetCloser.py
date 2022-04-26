import math
A, B = map(int, input().split())
r = math.sqrt(A*A+B*B)
print('{} {}'.format(A/r, B/r))