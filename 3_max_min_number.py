def max_min_number(arr):
    """"    This function find the man & min number from inputed array.     """
    MAX = MIN = arr[0]

    for num in arr:
        if num > MAX:
            MAX = num
        elif num < MIN:
            MIN = num

    return MAX, MIN

input = [-3,-1.05,3,61,23.5,0.5,-3.4]
MAX, MIN = max_min_number(input)
print(f"Maximum is: {MAX}")
print(f"Minimum is: {MIN}")