string1 = "Hello, world!"
string2 = "Hello, lkjld!"

if len(string1) != len(string2):
    print("The strings have different lengths.")
else:
    differences = []
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            differences.append((i, string1[i], string2[i]))
    if differences:
        print(differences)                                      # 调试语句
        print("The following characters are different:")
        for i, char1, char2 in differences:
            print("index {}: {} vs {}".format(i, char1, char2))
    else:
        print("The strings are equal.")
