# 3.4.1.6 LAB: The basics of lists

# List of numbers in the hat.
import time
print("The current numbers hiding in the hat are:")
hat_list = [1, 2, 3, 4, 5]
print(hat_list, "\n")

# Step 1 - code that prompts the user
# to replace the middle number with an integer number entered by the user.
time.sleep(0.5)
hat_list[2] = int(input("Middle number requires replacement, please enter a new integer number: "))
print(hat_list, "\n")

# Step 2 - Removes the last element from the hat_list.
print("The last number hiding in the hat has escaped and will be removed from our list:")
time.sleep(0.5)
del hat_list[-1]
print(hat_list, "\n")

# Step 3 - Prints the length of the existing hat_list.
time.sleep(0.5)
print("Length of hat list is: ", len(hat_list), "\n")

# Step 4 - Adds a new number to the hat_list.
time.sleep(0.5)
print("A new number has come to hide in the the hat:")
# Inserts number '23' at the 3rd position on the hat_list.
# This "pushes" the 3rd element to the 4th position.
# Be aware that postions begin at '0' not '1', so: [0-1-2-3-4-etc...] 
# Also, when 'inserting' a new element at a position higher than original length 
# it will appear as the last element.
hat_list.insert(3,23)
print(hat_list, "\n")

# Step 5 - Prints the length of the existing list.
time.sleep(0.5)
print("Length of hat list is: ", len(hat_list), "\n")

# Step 6 - Adds a number to the hat-list.
# Simply adds '72' to the end of the hat_list.
time.sleep(0.5)
hat_list.append(72)
print("Another new number has come to hide in the the hat:")
print(hat_list, "\n")

# Step 7 - Prints the length of the existing list.
time.sleep(0.5)
print("Length of hat list is: ", len(hat_list), "\n")
