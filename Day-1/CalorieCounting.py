import os, sys

### Part 1 ###
print("### Part 1 ###")

group_totals = []
with open(f"{os.path.dirname(sys.argv[0])}\input", "r") as elf_food:
    group_total = 0
    for line in elf_food:
        calories = line.strip()

        if calories != "":
            calories = int(calories)
            group_total += calories
        else:
            group_totals.append(group_total)
            group_total = 0

group_totals.sort(reverse=True)

print(f"{group_totals[0]}")

### Part 2 ###
print("### Part 2 ###")

print(f"1: {group_totals[0]}")
print(f"2: {group_totals[1]}")
print(f"3: {group_totals[2]}")


grand_total = group_totals[0] + group_totals[1] + group_totals[2]

print(f"TOTAL: {grand_total}")
