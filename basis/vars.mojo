def vars():
    pass
    # The List in row can contain only Int values
    # row = List[Int]()
    # The List in names can contain only String values
    # names = List[String]()

    # Create a List[Int] with the List constructor, inferring the type
    # nums1 = List(12, -7, 64)

    # Create a List[Int] with the list literal syntax, inferring the type
    nums = [12, -7, 64]
    nums.append(-937)
    print("Number of elements in the list:", len(nums))
    print("Popping last element off the list:", nums.pop())
    print("First element of the list:", nums[0])
    print("Second element of the list:", nums[1])
    print("Last element of the list:", nums[-1])
    print("12 -7 = ", nums[1] + nums[-3])

    grid = [
        [11, 22],
        [33, 44],
    ]
    print("Row 0, Column 0:", grid[0][0])
    print("Row 0, Column 1:", grid[0][1])
    print("Row 1, Column 0:", grid[1][0])
    print("Row 1, Column 1:", grid[1][1])


def game():
    num_rows = 8
    num_cols = 8
    glider = [
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    
    rep = String()
    rep += grid_str(num_rows, num_cols, glider)
    print(rep)


def grid_str(rows: Int, cols: Int, grid: List[List[Int]]) -> String:
    # Create an empty String
    str = String()

    # Iterate through rows 0 through rows-1
    for row in range(rows):
        # Iterate through columns 0 through cols-1
        for col in range(cols):
            if grid[row][col] == 1:
                str += "*"  # If cell is populated, append an asterisk
            else:
                str += " "  # If cell is not populated, append a space
        if row != rows - 1:
            str += "\n"  # Add a newline between rows, but not at the end
    return str


def main():
    vars()
    var age: Int = 47
    var greeting = "Hi, You!"
    print(greeting, age)
    print ('-'*77)
    
    game()
