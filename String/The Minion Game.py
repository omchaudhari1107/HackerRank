# def Generate(s):
#     str_gen = set()
#     for i in range(len(s) + 1):
#         for j in range(i, len(s) + 1):
#             if s[i:j] in str_gen:
#                 continue
#             else:
#                 str_gen.add(s[i:j])
#     return list(str_gen)


# def Check(sub_ss, s):
#     cnt, lst = list(), list()
#     for i in sub_ss:
#         for j in range(len(s)):
#             if s[j : len(i) + j] == i:
#                 lst.append(s[j : len(i) + j])
#         cnt.append(lst.count(i))
#     return sum(cnt)


# def Stuart(ele, s):
#     st = [i for i in ele if i[0] != "A"]
#     return Check(st, s)


# def Kevin(ele, s):
#     lst = [i for i in ele if i[0] == "A"]
#     return Check(lst, s)


# def minion_game(string):
#     ele = Generate(string)
#     ele.remove("")
#     count_stuart = Stuart(ele, string)
#     count_kevin = Kevin(ele, string)
#     if count_stuart > count_kevin:
#         print(f"Stuart {count_stuart}")
#     elif count_stuart < count_kevin:
#         print(f"Kevin {count_kevin}")
#     else:
#         print("Draw")


# if __name__ == "__main__":
#     s = "BAANANAS"
#     minion_game(s)


def minion_game(string):
    length = len(string)
    count_stuart = 0
    count_kevin = 0

    for i in range(length):
        if string[i] in "AEIOU":
            count_kevin += length - i
        else:
            count_stuart += length - i

    if count_stuart > count_kevin:
        print(f"Stuart {count_stuart}")
    elif count_stuart < count_kevin:
        print(f"Kevin {count_kevin}")
    else:
        print("Draw")


if __name__ == "__main__":
    s = "BAANANAS"
    minion_game(s)
