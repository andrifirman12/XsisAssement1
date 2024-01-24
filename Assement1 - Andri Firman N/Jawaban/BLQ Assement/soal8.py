
arr = []
n = 4
deret = [1, 2, 4, 7, 8, 6, 9]

for x in range(len(deret)):
    if x < len(deret) - (n-1):
        ttl = 0
        for y in range(x, x+(n)):
            ttl = ttl + deret[y]
        arr.append(ttl)

lowest = min(arr)
highest = max(arr)

div = "----------------------------------------"
print(div)
print(f'''Sequence: {deret} \nCombination is {n}''')
print(f'''Lowest Combination is {lowest} \nHighest combination is {highest}  ''')
print(div)