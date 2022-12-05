import string
with open("input.txt", "r") as file:
    priorities = list(string.ascii_letters)
    data = file.readlines()
    priority_sum_a = 0

    group_set = set(priorities)
    priority_sum_b = 0
    elf_counter = 0

    for line in data:
        rucksack = line.strip()
        compartment_size = len(rucksack)//2
        compartment_a, compartment_b = set(rucksack[:compartment_size]), set(rucksack[compartment_size:])
        misplaced_item = compartment_a.intersection(compartment_b)
        priority_sum_a += priorities.index(list(misplaced_item)[0]) + 1

        # b
        group_set = group_set.intersection(set(rucksack))
        if elf_counter == 2:
            priority_sum_b += priorities.index(list(group_set)[0]) + 1
            group_set = set(priorities)
            elf_counter = 0
        else:
            elf_counter+=1

print("a:", priority_sum_a)
print("b:", priority_sum_b)