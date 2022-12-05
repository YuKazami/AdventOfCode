def result(a, x):
    if (a == "A" and x == "X") or (a == "B" and x == "Y") or (a == "C" and x == "Z"):
        return 3
    elif (a == "A" and x == "Y") or (a == "B" and x == "Z") or (a == "C" and x == "X"):
        return 6
    elif (a == "A" and x == "Z") or (a == "B" and x == "X") or (a == "C" and x == "Y"):
        return 0

def choice(a, r):
    if (a == "A" and r == "X") or (a == "B" and r == "Z") or (a == "C" and r == "Y"):
        return 3
    elif (a == "A" and r == "Y") or (a == "B" and r == "X") or (a == "C" and r == "Z"):
        return 1
    elif (a== "A" and r == "Z")or (a == "B" and r == "Y") or (a == "C" and r == "X"):
        return 2

with open("input.txt", "r") as file:
    data = file.readlines()
    score_a = 0
    score_b = 0
    for line in data:
        opponent, response = line.strip().split(" ")
        if response == "X":
            score_a += 1
            score_b += 0
        elif response == "Y":
            score_a += 2
            score_b += 3
        elif response == "Z":
            score_a += 3
            score_b += 6
        score_a += result(opponent, response)
        score_b += choice(opponent, response)

print("a:", score_a)
print("b:", score_b)