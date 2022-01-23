major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
pair_number_color_mapping =[]

def print_color_map():
    pair_number_color_mapping = get_pair_number_color_mapping()
    for pair in pair_number_color_mapping:
        print(f'{pair[0]} | {pair[1]} | {pair[2]}')
    return len(major_colors) * len(minor_colors) , pair_number_color_mapping

def get_pair_number_color_mapping():
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            pair_number_color_mapping.append([i * 5 + j, major, minor])
    return pair_number_color_mapping


result, pair_number_color_mapping = print_color_map()
assert(result == 25)
assert(1 in pair_number_color_mapping[0])
assert(len(major_colors)*len(minor_colors) in pair_number_color_mapping[-1])

print("All is well (maybe!)\n")
