# Multiplication Table (Col V Rows >)

def printTable(start: int, end: int) -> None:
    for col in range(1, 11): # Column tracker (Starts at 1, Ends at 10)
        for row in range(start, end + 1):
            # Prints each table of values (a x b = c) + Space formatting
            print(f"{row:2,d} x {col:2,d} = {row * col:3,d}", end="   ") 
        print() # Spacing for each row
    print() # Spacing for each table

if __name__ == "__main__":
    printTable(1, 5)
    printTable(6, 10)