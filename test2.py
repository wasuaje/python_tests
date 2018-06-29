import sys


def largestRectangle(heights):
    # Complete this function
    heights.append(0)
    stack = []
    maxAreaSoFar = -1
    for height in heights:
        n = 0
        while(len(stack) > 0 and stack[-1] > height):
            n += 1
            maxAreaSoFar = max(maxAreaSoFar, n * stack.pop())

        for i in range(0, n+1):
            stack.append(height)
        print(height, maxAreaSoFar, n, stack)

    return maxAreaSoFar


if __name__ == "__main__":
    entry = open("entry3.txt")
    n = int(entry.readline().strip())
    h = list(map(int, entry.readline().strip().split(' ')))
    result = largestRectangle(h)
    print(result)
