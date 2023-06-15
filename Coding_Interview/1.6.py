def string_compression(str):
    if (len(str) <= 1):
        return str
    comp_str = ""
    temp_char = str[0]
    count = 1
    for i in range(1, len(str)):
        if(temp_char != str[i]):
            comp_str += f"{temp_char}{count}"
            temp_char = str[i]
            count = 1
        else:
            count += 1
    comp_str += f"{temp_char}{count}"
    if(len(comp_str) > len(str)):
        return str
    return comp_str


print(string_compression("aaabccccaaa"))
print(string_compression("abc"))
print(string_compression("aabbcc"))
