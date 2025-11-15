# multiplication_table.py
# Prompt the user for a number
number = int(input("Enter a number to generate its multiplication table: "))
# use a for loop to generate the multiplication table fron 1 to 10
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
    