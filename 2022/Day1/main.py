
with open("input.txt", "r") as file:
    data = file.readlines()
    summe = 0
    max0 = 0
    max1 = 0
    max2 = 0
    for line in data:
        line = line.strip()
        if line == "":
            if summe > max0:
                max2 = max1
                max1 = max0
                max0 = summe
            elif summe > max1:
                max2 = max1
                max1 = summe
            elif summe > max2:
                max2 = summe
            summe = 0
        else:
            summe += int(line)

print("a: ", max0)
print(max0, max1, max2)
print("b: ", max0+max1+max2)
