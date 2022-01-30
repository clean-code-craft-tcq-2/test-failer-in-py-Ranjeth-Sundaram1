def GetSizeName(cms:int):
    if cms>34 and cms <= 38:
        return 'S'
    elif cms > 38 and cms <= 42:
        return 'M'
    elif cms >42 and cms <= 46:
        return 'L'
   
def ValidateSizeNamewithCms(cms: int, size: str):
    try:
        assert(GetSizeName(cms) == size)
    except AssertionError:
         print(f"Assertion error : The entered size({cms}) is not matched with {size}. Please refer 'Size Reference Manual \n {PrintReferenceManual()}")
         

def PrintReferenceManual():
    ''' This will return the cms and size mapping '''
    return('''
         Range\t| Size\n
         35-38\t| S\n
         39-42\t| M\n
         43-46\t| L\n
    ''')

ValidateSizeNamewithCms(37, 'S')
ValidateSizeNamewithCms(40, 'M')
ValidateSizeNamewithCms(43, 'L')
ValidateSizeNamewithCms(38, 'S')
ValidateSizeNamewithCms(42, 'M')
ValidateSizeNamewithCms(0, 'S')
ValidateSizeNamewithCms(50, 'L')

print("All is well (maybe!)\n")
