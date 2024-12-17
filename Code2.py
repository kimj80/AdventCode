import os


def main():
    f = open("input2.txt", "r")
    numOfSafeReports = 0
    for line in f:
        levels = line.split()
        comparedCycle = 0
        for i in range(len(levels)-1):
            difference = int(levels[i]) - int(levels[i + 1])
            if (int(levels[0]) > int(levels[1])):
                if (difference > 0 and difference < 4):
                    comparedCycle += 1
            else:
                if (difference < 0 and difference > -4):
                    comparedCycle += 1

            if (comparedCycle == len(levels)-1):
                numOfSafeReports+=1

    print(numOfSafeReports)

    return

if __name__ == "__main__":
    main()
