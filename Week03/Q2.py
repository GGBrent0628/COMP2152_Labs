#Q2
cart = ["apple","banana", "milk", "bread", "apple", "eggs"]
apple_count = cart.count("apple")
print(f"Number of apples: {apple_count}")
milk_position = cart.index("milk")
print(f"Position of milk is: {milk_position}")
cart.remove("apple")#using remove
removed_item = cart.pop()
print(f"Removed item using pop: {removed_item}")
print("Is banana in the shopping cart? ", "banana" in cart)
print(cart)