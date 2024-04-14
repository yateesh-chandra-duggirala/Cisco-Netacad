'''
As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. 

The player has to fill the board in a very specific way:
- each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
- each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
- each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.

Your task is to write a program which:
- reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
- outputs Yes if the Sudoku is valid, and No otherwise.

Test your code using the data we've provided.

1. Sample input:
    295743861
    431865927
    876192543
    387459216
    612387495
    549216738
    763524189
    928671354
    154938672

   Sample output:
    Yes

2. Sample input:
    195743862
    431865927
    876192543
    387459216
    612387495
    549216738
    763524189
    928671354
    254938671

   Sample output:
    No
'''

# Define a function that checks whether a list passed contains nine digits or not.
def checkDigits(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]

# Create an empty list "rows"
rows = []
for r in range(9):
    ok = False

    # Run the loop and enter the values into row
    while not ok :
        row = input(f"Enter row #{r+1} : ")
        
        # update the ok variable with the conditional
        ok = len(row) == 9 or row.isdigit()
        if not ok:
            print("Incorrect Rows Data - 9 digits required")
    
    # Append the row into the list
    rows.append(row)

# Set the ok flag to True
ok = True

# Check if all rows are good.
for r in range(9):
    if not checkDigits(rows[r]):
        ok = False
        break

# Do the same for the columns
if ok:
    for c in range(9):

        # Create a col list
        col = []
        for r in range(9):
            col.append(rows[r][c])
        if not checkDigits(col):
            ok = False
            break

# Check if all the subsquares are good.
if ok :
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            square = ''
            
            # make a string containing all digits from a sub-square
            for i in range(3):
                square += rows[r+i][c:c+3]
            if not checkDigits(list(square)):
                ok = False
                break

# Print the result
if ok : 
    print("Yes")
else :
    print("No")