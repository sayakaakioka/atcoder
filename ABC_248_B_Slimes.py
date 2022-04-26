import math
A, B, K = map(int, input().split())
print(math.ceil(math.log2(B/A)/math.log2(K)))