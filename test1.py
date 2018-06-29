
import sys


if __name__ == "__main__":
    entry = open("entry.txt")
    n, inputs = [int(n) for n in entry.readline().strip().split(' ')]
    list = [0]*(n+1)
    for _ in range(inputs):
        x, y, incr = [int(n) for n in entry.readline().strip().split(' ')]
        list[x-1] += incr
        if((y) <= len(list)):
            list[y] -= incr
        print(x, y, incr, list)
    max = x = 0
    for i in list:
        x = x+i
        if(max < x):
            max = x

    print(max)
