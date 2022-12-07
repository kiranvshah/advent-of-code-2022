tree = {}
TOTAL_SPACE_ON_SYSTEM = 70_000_000
FREE_SPACE_REQUIRED_ON_SYSTEM = 30_000_000

with open("input.txt") as file:
    current_path: str = ""
    for line in file:
        line = line.strip()
        if line.startswith("$ cd "):
            arg = line.split(" ")[-1]
            if arg == "..":
                current_path = "/".join(current_path.split("/")[:-2]) + "/"
            elif arg == "/":
                current_path = "/"
            else:
                current_path += arg + "/"
        elif not line.startswith("$ ls"):
            current_path_in_tree_dict = tree
            for the_dir in [e for e in current_path.split("/") if e != ""]:
                current_path_in_tree_dict = current_path_in_tree_dict[the_dir]
            if line.startswith("dir"):
                current_path_in_tree_dict[line.split(" ")[-1]] = {}
            else:
                current_path_in_tree_dict[line.split(" ")[1]] = int(line.split(" ")[0])

def get_size_of_dir(dir_tree: dict):
    size = 0
    for value in dir_tree.values():
        if str(type(value)) == "<class 'int'>":
            # is file
            size += value
        else:
            # is dir
            size += get_size_of_dir(value)
    return size

MIN_SPACE_TO_BE_CLEARED = abs(TOTAL_SPACE_ON_SYSTEM - get_size_of_dir(tree) - FREE_SPACE_REQUIRED_ON_SYSTEM)

possible_deletion_options = [] # size of each dir that is at least MIN_SPACE_TO_BE_CLEARED

def search_dir_for_deletion_options(dir_tree: dict):
    for value in dir_tree.values():
        if str(type(value)) == "<class 'dict'>":
            if get_size_of_dir(value) >= MIN_SPACE_TO_BE_CLEARED:
                possible_deletion_options.append(get_size_of_dir(value))
            search_dir_for_deletion_options(value)

search_dir_for_deletion_options(tree)
print(min(possible_deletion_options))
