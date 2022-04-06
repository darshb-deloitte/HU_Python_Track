def prob(a, b, c, x):
    solution = lambda a, b, c, x: (a * (x ^ 2)) + (b * x) + c

    return solution(a, b, c, x)


def Occurances():
    lst1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

    result = list(map(lambda x: (x.count("a") + x.count("A")), lst1))

    return result


print("Solution : ", prob(2, 1, 3, 2))

print("The number of occurrences of 'a'or 'A' is : ", Occurances())