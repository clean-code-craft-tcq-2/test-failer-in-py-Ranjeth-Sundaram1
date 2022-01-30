def GetSizeName(cms:int):
    if cms>34 and cms <= 38:
        return 'S'
    elif cms > 38 and cms <= 42:
        return 'M'
    elif cms >42 and cms <= 46:
        return 'L'
   
def ValidateSizeNameWithCms(cms: int, size: str):
    try:
        assert(GetSizeName(cms) == size)
    except AssertionError:
         print(f"The entered size({cms}) is not matched with {size}. Please enter the valid size")



ValidateSizeNameWithCms(37, 'S')
ValidateSizeNameWithCms(40, 'M')
ValidateSizeNameWithCms(43, 'L')
ValidateSizeNameWithCms(38, 'S')
ValidateSizeNameWithCms(42, 'M')
ValidateSizeNameWithCms(0, 'S')
ValidateSizeNameWithCms(50, 'L')

print("All is well (maybe!)\n")
