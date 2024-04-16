def count_substring(string, sub_string):
    lst = list()
    for i in range(len(string) - 2):
        temp = string[i : len(sub_string) + i]
        if len(temp) == len(sub_string):
            lst.append(temp)

    return lst.count(sub_string)


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

# Input
# abcdcdc
# cdc

# output
# count:2
