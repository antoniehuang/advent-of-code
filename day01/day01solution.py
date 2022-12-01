with open('day01/input.txt', 'r') as f:
    input = f.read()
    input = input.split('\n\n')

list_of_elf_calories = []
for elf_calories in input:
    elf_calories = (elf_calories.split())
    sum = 0
    for elf_calorie in elf_calories:
        sum += int(elf_calorie)
    list_of_elf_calories.append(sum)

# Calories carried by the elf carrying the most
print(max(list_of_elf_calories))


list_of_elf_calories.sort(reverse=True)
# Add top 3 and print the result
sum_of_top_three = 0
for i in range(0, 3):
    sum_of_top_three += list_of_elf_calories[i]

# Sum of the calories carried by the top 3 elfs
print(sum_of_top_three)
