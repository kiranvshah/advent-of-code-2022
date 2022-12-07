tree = {}

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

total_dir_sizes_less_than_100_000: int = 0

def get_size_of_dir(dir_tree: dict):
    global total_dir_sizes_less_than_100_000
    size = 0
    for value in dir_tree.values():
        if str(type(value)) == "<class 'int'>":
            # is file
            size += value
        else:
            # is dir
            size += get_size_of_dir(value)
    if size <= 100_000:
        total_dir_sizes_less_than_100_000 += size
    return size

get_size_of_dir(tree)
print(total_dir_sizes_less_than_100_000)
