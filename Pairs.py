from itertools import combinations

numbers = [1,2,3,4,5]
groups = 2
combos = [
    x for x in combinations(numbers , groups)
]
print(combos)