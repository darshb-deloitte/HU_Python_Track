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


Demo = PairsPossible("12314532")
Demo.Possible_pairs()

