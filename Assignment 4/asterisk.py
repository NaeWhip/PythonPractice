#prompts user to enter rows
rows = int(input('How many rows? '))

#prompts user to enter columns
cols = int(input('How many columns? '))

#outputs the rows
for r in range(rows):
    print(end='')

    #outputs the decreasing columns
    for c in range(cols - r):
        print('*', end='')

    #moves to the next line
    print()


# ----- Instructor's solution -----

while (base_size := int(input('Enter a number for the height: '))) <= 0:
    print('Error: height must be positive integer.')

# outer loop controls the number of rows
# inner loop controls the number of columns

for r in range(base_size, 0, -1):
    for c in range(r):
        print('*', end=' ')
    print()