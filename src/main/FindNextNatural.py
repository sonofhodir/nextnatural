def find_next(digits):
    arr = list(map(int, digits))
    n = len(digits)
    if ignore_array_of_same_numbers(arr):
        return -1

    # for storing 4 regions
    a1 = []  # 1st: Trailing zeros .
    a2 = []  # 2nd: The next digit not in Region 1.
    a3 = []  # 3rd: Consecutive 9s starting with the digit above Region 2.
    a4 = []  # 4th: All remaining digits.

    # trailing zeros region1
    i = n - 1  # last index
    while arr[i] == 0:
        a1.append(0)
        i -= 1

    # lowest region(region 2) not in region 1
    a2.append(arr[i])
    i -= 1

    # Consecutive 9's (region 3)
    while arr[i] == 9 and i >= 0:
        a3.append(9)
        i -= 1

    j = 0
    while j <= i:  # 4th region
        a4.append(arr[j])
        j += 1

    # formula for finding elements
    # [Region 4 + 1][Region1] [Region 2 - 1][Region3]
    # Calculating the result

    magic_value = convert_array_into_one_string(a4)
    val1 = ''
    if magic_value != '':
        val1 = int(convert_array_into_one_string(a4)) + 1
    val2 = convert_array_into_one_string(a1)

    val3 = ''
    magic_value = convert_array_into_one_string(a2)
    if magic_value != '':
        val3 = int(convert_array_into_one_string(a2)) - 1

    val4 = convert_array_into_one_string(a3)

    result = str(val1) + str(val2) + str(val3) + str(val4)
    if len(str(int(result))) != n:  # as could be trailing 0 at the beginning
        return -1
    else:
        return int(result)


def convert_array_into_one_string(num_list):
    s = ''.join(map(str, num_list))
    return s


def ignore_array_of_same_numbers(arr):
    return len(set(arr)) <= 1
