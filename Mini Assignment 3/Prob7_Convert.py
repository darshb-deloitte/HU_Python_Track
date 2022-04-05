dict = {"'HuEx": [1, 3, 4], "is": [7, 6], "best": [4, 5]}
outer_list = []

for key in dict:
    inner_list = []
    inner_list.append(key)
    inner_list = inner_list + list(dict[key])

    outer_list.append(inner_list)

print(outer_list)