friends = []
keep_adding = "continue"

while keep_adding != "end":
    add_name = input("Type the name of a friend: ")
    if add_name == "end":
        keep_adding = "end"
    else:
        friends.append(add_name)
print()  
print("Your friends are:")
for names in friends:
    print(names)