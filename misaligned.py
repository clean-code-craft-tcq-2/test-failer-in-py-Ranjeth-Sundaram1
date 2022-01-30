major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
pair_number_color_mapping =[]

def PrintPairnumberWithColors(pair_number:int, major_color:str, minor_color:str) ->str:
    return("{0:<4}| {1:<10}| {2:<10}".format(pair_number, major_color, minor_color))

def GetPairnumberColorMapping(major_colors:list, minor_colors:list):
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            pair_number_color_mapping.append([i * 5 + j + 1, major, minor])
    return pair_number_color_mapping

def ValidatePairNumber(pair_number):
    try:
        assert(pair_number>0 and pair_number<(len(major_colors)*(minor_colors)))
    except AssertionError:
        print(f"The entered pair_number({pair_number}) is not a valid pair_number")

def ValidateAlignment(pair_number:int, major_color:str,minor_color:str):
    try:
        assert(PrintPairnumberWithColors(pair_number,major_color,minor_color) == "{0:<4}| {1:<10}| {2:<10}".format(pair_number, major_color, minor_color))
    except AssertionError :
        print (f"Alignment validation for {pair_number} , {major_color}, {minor_color} is failed")

def PrintAllPairnumberWithColors(pair_number_color_mapping):
    for onePair in (pair_number_color_mapping):
        print(PrintPairnumberWithColors(pair_number=onePair[0], major_color=onePair[1], minor_color=onePair[2]))

pair_number_color_mapping = (GetPairnumberColorMapping(major_colors,minor_colors))
PrintAllPairnumberWithColors(pair_number_color_mapping)
ValidateAlignment(10, "Red", "Slate")
ValidateAlignment(1, "Red", "Slate")
ValidateAlignment(25, "Violet", "Slate")
ValidatePairNumber(0)
assert(1 in pair_number_color_mapping[0])
assert(len(major_colors)*len(minor_colors) in pair_number_color_mapping[-1])

print("All is well (maybe!)\n")
