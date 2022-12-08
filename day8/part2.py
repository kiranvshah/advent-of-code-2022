trees = []
highest_scenic_score: int = 0

with open("input.txt") as file:
    for line in file:
        trees.append([int(x) for x in list(line.strip())])

for o_row_index, o_row in enumerate(trees):
    for o_column_index, o_height in enumerate(o_row):

        trees_visible_to_left: int = 0
        tallest_tree_so_far: int = -1
        for i_column_index in range(o_column_index-1, -1, -1):
            TREE_HEIGHT = o_row[i_column_index]
            trees_visible_to_left += 1
            if TREE_HEIGHT >= o_height:
                break

        trees_visible_to_right: int = 0
        tallest_tree_so_far: int = -1
        for i_column_index in range(o_column_index+1, len(o_row)):
            TREE_HEIGHT = o_row[i_column_index]
            trees_visible_to_right += 1
            if TREE_HEIGHT >= o_height:
                break

        trees_visible_above: int = 0
        tallest_tree_so_far: int = -1
        for i_row_index in range(o_row_index-1, -1, -1):
            TREE_HEIGHT = trees[i_row_index][o_column_index]
            trees_visible_above += 1
            if TREE_HEIGHT >= o_height:
                break

        trees_visible_below: int = 0
        tallest_tree_so_far: int = -1
        for i_row_index in range(o_row_index+1, len(trees)):
            TREE_HEIGHT = trees[i_row_index][o_column_index]
            trees_visible_below += 1
            if TREE_HEIGHT >= o_height:
                break


        SCENIC_SCORE = trees_visible_to_left * trees_visible_to_right * \
            trees_visible_above * trees_visible_below
        if SCENIC_SCORE > highest_scenic_score:
            highest_scenic_score = SCENIC_SCORE

print(highest_scenic_score)
