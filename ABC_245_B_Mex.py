N = int(input())
s = set(list(map(int, input().split())))

counter = 0
while True:
    if counter not in s:
        print(counter)
        break
    counter = counter + 1