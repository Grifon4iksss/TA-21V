map = [
    [12, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [24, 1, 1, 1, 1]
]

start_pos_x = 0
start_pos_y = 0

y_rows = 5
x_columns = 5

def get_next_free_pos(current_pos_y, current_pos_x):
    if current_pos_x + 1 < x_columns and map[current_pos_y][current_pos_x + 1] == 1:
        print("can go right")
        return [current_pos_y, current_pos_x + 1]

    if current_pos_y + 1 < y_rows and map[current_pos_y + 1][current_pos_x] == 1:
        print("can go bottom")
        return [current_pos_y + 1, current_pos_x]
    
    if current_pos_x - 1 > 0 and map[current_pos_y][current_pos_x - 1] == 1:
        print("can go left")
        return [current_pos_y, current_pos_x - 1]

    if current_pos_x - 1 > 0 and map[current_pos_y - 1][current_pos_x] == 1:
        print("can go top")
        return [current_pos_y - 1, current_pos_x]

    

next_free_pos = get_next_free_pos(start_pos_y, start_pos_x)
print("Next free position is: ", next_free_pos)

while next_free_pos:
    next_free_pos = get_next_free_pos(next_free_pos[0], next_free_pos[1])
    print("Next free position is: ", next_free_pos)

