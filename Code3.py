import os


def main():
    f = open("input3.txt", "r")
    totalNumber = 0
    for line in f:
        startIndex = 0
        possibleNumber = line.count("mul(")
        print("new line")
        for i in range(possibleNumber):
            # if (line.find("mul(", startIndex) == -1):
            #     break
            startIndex = line.find("mul(", startIndex)
            comma = line.find(",", startIndex)
            end = line.find(")", comma)

            print(line[startIndex:comma] + line[comma:end+1])

            if (line[startIndex+4:comma].isnumeric() and line[comma+1:end].isnumeric()):
                print(line[startIndex+4:comma], line[comma+1:end])
                firstNumber = int(line[startIndex+4:comma])
                secondNumber = int(line[comma+1:end])
                totalNumber += (firstNumber * secondNumber)
            startIndex += 4

    print(totalNumber)

    return


if __name__ == "__main__":
    main()