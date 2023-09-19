a = [2, 3, 6, 4, 9, 8, 9, 9, 6]

sort_a = []
max_value = 0
for i in range(len(a)):
    if a[i]>max_value:
        max_value = a[i]

for i in range(max_value+1):
    for j in range(len(a)):
        if i==a[j] and a[j]not in sort_a:
            sort_a+=[a[j]]

c = sort_a[::-1]
print(c[1])











