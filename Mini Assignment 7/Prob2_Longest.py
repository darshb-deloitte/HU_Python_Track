# To find the longest  word
with open("read.txt", "r") as file:
    f = file.read().split()
print(max(f, key=len))

