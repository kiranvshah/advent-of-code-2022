trees = []
visibles: int = 0

with open("input.txt") as file:
    for line in file:
        trees.append([int(x) for x in list(line.strip())])

for o_row_index, o_row in enumerate(trees):
    for o_column_index, o_height in enumerate(o_row):
        
        visible_from_left: bool = True
        for i_column_index in range(0, o_column_index):
            if o_row[i_column_index] >= o_height:
                visible_from_left = False

        # also check for col indexes heigher than o_col_ind
        visible_from_right: bool = True
        for i_column_index in range(o_column_index + 1, len(o_row)):
            if o_row[i_column_index] >= o_height:
                visible_from_right = False
        
        # check lower row indexes
        visible_from_above: bool = True
        for i_row_index in range(0, o_row_index):
            if trees[i_row_index][o_column_index] >= o_height:
                visible_from_above = False
        
        # check higher row indexes
        visible_from_below: bool = True
        for i_row_index in range(o_row_index + 1, len(trees)):
            if trees[i_row_index][o_column_index] >= o_height:
                visible_from_below = False
        
        if visible_from_below or visible_from_above or visible_from_left or visible_from_right:
            visibles += 1

print(visibles)