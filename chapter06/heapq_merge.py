import heapq

a = [2, 4, 6, 9, 11, 13]
b = [1, 2, 3, 4, 9, 16, 21]
c = list(sorted(a+b))
print(c)
c = list(heapq.merge(a, b))
print(c)