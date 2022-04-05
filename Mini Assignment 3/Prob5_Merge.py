dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {}

def MergeDict(dict):
    for key in dict:
        if key in dict3:
            continue
        else:
            dict3[key] = dict[key]


MergeDict(dict1)
MergeDict(dict2)
print(dict3)