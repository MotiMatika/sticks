print("\nS T I C K S")

print("\n| | | | | | | | | | |")
print("""\nYou have to remove,
      one,
      or two
      or three sticks.
      The player who takes the last stick - LOSE""")

num_of_sticks = 11
print("\nHere we have",num_of_sticks,"sticks")
print("\n")
print("|" * (num_of_sticks))

list = ["| | | | | | | | | | |"]
list = list.pop(0)
print(list)