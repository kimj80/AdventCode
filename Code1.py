import os

def main():
    f = open("input.txt", "r")
    left = []
    right = []
    for line in f:
        twoNum = line.split(' ')
        left.append(int(twoNum[0]))
        right.append(int(twoNum[3]))
        #prob best to sort while appending~~~~

    left.sort()
    right.sort()
    result = 0
    totalResult = 0
    for i in range(len(left)):
        result = float(left[i]) - float(right[i])
        totalResult += abs(result)
    print(totalResult)

    return

if __name__ == "__main__":
    main()