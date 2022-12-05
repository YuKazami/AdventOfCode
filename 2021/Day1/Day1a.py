inputLines = []
with open('./Input.txt') as inputFile:
    inputLines = inputFile.readlines()

increasments = 0

for i in range(0, len(inputLines)):

    print(inputLines[i])

    if inputLines[i] > inputLines[i-1]:
        increasments += 1

        print("increased")

    print("----")


print(increasments)