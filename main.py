from itertools import combinations


class StringClass:

    def __init__(self, str):
        self.str = str

    def strlen(self):
        length = len(self.str)
        return length

    def str_list(self):
        characters = list(self.str)
        return characters


class PairsPossible(StringClass):

    def Possible_pairs(self):
        lis = StringClass.str_list(self)
        groups = 2
        combos = [
            x for x in combinations(lis, groups)
        ]
        print(*combos)
        return combos


class SearchCommonElements:

    def __init__(self, a, b):
        self.StringClass_string = a
        self.PossiblePair_string = b
        self.common_list = list()

    def find_common(self):
        dict = {}

        for ele in self.StringClass_string:
            if ele in self.PossiblePair_string:
                if ele in dict:
                    continue
                else:
                    dict[ele] = 1

        for key in dict:
            self.common_list.append(key)

        return self.common_list


class EqualSumPairs():

    def print_equal_sum_pairs(self, lis):

        dict1 = {}

        for pair in lis:
            pairs_list = list(pair)
            sum = 0
            for num in pairs_list:
                sum = sum + int(num)

            if sum in dict1:
                dict1[sum] = dict1[sum] + 1
            else:
                dict1[sum] = 1

        for key in dict1:
            if dict1[key] == 1:
                print(key, end=" ")


obj = StringClass("12314532")
print("length of the string is:")
print(obj.strlen())
print("String converted into list are")
print(obj.str_list())

Demo = PairsPossible("1357357")
print("Possible pairs are:")
lis = Demo.Possible_pairs()

obj1 = SearchCommonElements(obj.str, Demo.str)
print("Common Elements are:")
print(obj1.find_common())

obj2 = EqualSumPairs()
print("Equal sum pairs are:")
obj2.print_equal_sum_pairs(lis)
