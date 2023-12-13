digits_in_line = []
list_of_numbers = []

with open("input.txt", "r") as input_file:
    for line in input_file.readlines():
        for char in line:
            if char.isnumeric():
                digits_in_line.append(char)

        first_and_last_digit_combinded = int(f"{digits_in_line[0]}{digits_in_line[-1]}")
        digits_in_line = []

        list_of_numbers.append(first_and_last_digit_combinded)

total = sum(list_of_numbers)
print(f"total: {total}")
