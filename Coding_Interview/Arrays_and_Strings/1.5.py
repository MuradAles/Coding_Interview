def one_way(str_1, str_2):
    if(len(str_1) == 0):
        return False
    if(len(str_2) == 0):
        return False
    if(str_1 == str_2):
        return True
    if(abs(len(str_1) - len(str_2)) > 1):
        return True
    if(len(str_1) >= len(str_2)):
        s1, s2 = str_1, str_2
    else:
        s2, s1 = str_1, str_2
    index_1 = 0
    index_2 = 0
    count_diff = 0
    while(len(s1) > index_1 and len(s2) > index_2):
        if(s1[index_1] != s2[index_2]):
            count_diff += 1
            if count_diff > 1:
                return False
            if len(s1) == len(s2):
                index_2 += 1
        else:
            index_2 += 1
        index_1 += 1
    return True


print(one_way("pale", "ple"))
print(one_way("pales", "pale"))
print(one_way("pale", "bale"))
print(one_way("pale", "bake"))
