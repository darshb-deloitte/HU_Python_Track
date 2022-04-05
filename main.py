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
        l = StringClass.str_list(self)
        groups = 2
        combos = [
            x for x in combinations(l, groups)
        ]
        print(*combos)


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


obj = StringClass("12314532")
print(obj.strlen())
print(obj.str_list())

Demo = PairsPossible("12389764")
Demo.Possible_pairs()

obj3 = SearchCommonElements(obj.str,Demo.str)
print(obj3.find_common())
