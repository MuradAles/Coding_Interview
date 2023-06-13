def unique_characters(unique):
    arr = []
    for i in unique:
        if(i in arr):
            print("String is not unique")
            return False
        else:
            arr.append(i)
    print("String is unique")
    return True


unique_characters("Helo")
