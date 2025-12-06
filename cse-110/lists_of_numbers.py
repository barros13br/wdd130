numbers_list = []
continue_asking = "yes"

print("Enter a list of numbers, type '0' when finished.")
while continue_asking == "yes":
    new_number = float(input("Enter number: "))
    if new_number == 0:
        continue_asking = "no"
    else:
        numbers_list.append(new_number)

