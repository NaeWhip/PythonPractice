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