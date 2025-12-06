items_list = []
list_quit = "no"

print("Please, enter the items of the shopping list, type 'quit' to finish.")
while list_quit == "no":
    add_item = input("Item: ")
    if add_item == "quit":
        list_quit = "yes"
    else:
        items_list.append(add_item)
print()
print("The shopping list whith indexes is:")
for index in range(len(items_list)):
    item = items_list[index]
    print(f"{index}. {item}")
print()
index_insert = int(input("Which item  would you lije to change? "))
new_item = input("What is the new item? ")
print()
items_list.pop(index_insert)
items_list.insert(index_insert, new_item)
print("The shoppong list whith indexes is:")
for index in range(len(items_list)):
    item = items_list[index]
    print(f"{index}. {item}")