from functools import reduce
from operator import add
print(45-reduce(add, map(int, input())))