with open("input.txt", "r") as file:
    data = file.readlines()
    fully_contained = 0
    overlaps = 0
    for pair in data:
        sector_1, sector_2 = [range(int(x.split("-")[0]), int(x.split("-")[1])+1) for x in pair.strip().split(",")]

        if (sector_1[0] in sector_2 and sector_1[-1] in sector_2) or (sector_2[0] in sector_1 and sector_2[-1] in sector_1):
            fully_contained += 1

        for x in sector_1:
            if x in sector_2:
                overlaps += 1
                break

print("a:", fully_contained)
print("b:", overlaps)