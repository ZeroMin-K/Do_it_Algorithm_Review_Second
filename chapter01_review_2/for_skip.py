for i in range(1, 13):
    if i == 8:
        continue
    print(i, end=' ')

print()

for i in list(range(1, 8)) + list(range(9, 13)):
    print(i, end=' ')
print()