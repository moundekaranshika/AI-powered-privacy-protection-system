mixed_list = [42, "Temperature", True, [1, 2, 3]]

# Display the list
print("Mixed List Contents:")
print(mixed_list)

# Display type of each element
print("\nType of Each Element in the List:")
for i, item in enumerate(mixed_list):
    print(f"Element {i+1}: {item} --> {type(item).__name__}")