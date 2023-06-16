def sort_string(str):
    sorted_string = ''.join(sorted(str))
    return sorted_string


def check_permutation(str_1, str_2):
    if (len(str_1) == 0):
        return False
    if (len(str_2) == 0):
        return False
    if (len(str_1) != len(str_2)):
        return False
    sorted_str_1 = sort_string(str_1)
    sorted_str_2 = sort_string(str_2)
    for i in range(0, len(str_1)):
        if(sorted_str_1[i] != sorted_str_2[i]):
            return False
    return True


def main():
    str_1 = "hello"
    str_2 = "olllh"
    print(check_permutation(str_1, str_2))


main()
