list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
final_list = list()

for word in list1:
    for word1 in list2:
        final_list.append(word+word1)

print(final_list)