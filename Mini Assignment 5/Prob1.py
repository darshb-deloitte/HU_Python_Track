lis1 = [-1000, 500, -600, 700, 5000, -90000, -17500]

filt = list(filter(lambda x: x, map(lambda x: -x if x < 0 else None, lis1)))

print(filt)