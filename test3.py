entry = open("entry4.txt")
n = int(entry.readline().strip())
#n = int(input())

for i in range(n):
    option = int(entry.readline())
    print("First" if option % 7 in [0, 1] else "Second")
