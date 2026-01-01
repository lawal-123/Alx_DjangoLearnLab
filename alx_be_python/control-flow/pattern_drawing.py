size = int(input("enter the size of the pattern: "))
if size <= 0:
    print("please enter a positive integer")
else:
    row = 0
while size > row:
    for _ in range(size):
        print("*", end="")
        print()
        row += 1