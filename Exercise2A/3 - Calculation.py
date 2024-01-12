from math import floor


n, k = map(int, input().split())
print(floor(n / (2 ** k)))
