r1 = range(0, 5)
for i in r1:
    for j in r1:
        print("*", end="")
    print("", end="\n")
# *****
# *****
# *****
# *****
# *****


cnt = 0
r1 = range(0, 5)
for i in r1:
    cnt += 1
    for j in range(cnt):
        print("*", end="")
    print("", end="\n")
# *
# **
# ***
# ****
# *****

cnt = 0
r1 = range(0, 5)
for i in r1:
    cnt += 1
    for j in range(cnt):
        print(f"{j}", end="")
    print("", end="\n")
# 0
# 01
# 012
# 0123
# 01234

cnt = 0
r1 = range(0, 5)
for i in r1:
    cnt += 1
    for j in range(cnt):
        print(f"{i}", end="")
    print("", end="\n")
# 0
# 11
# 222
# 3333
# 44444

cnt = 5
r1 = range(0, 5)
for i in r1:
    for j in range(cnt):
        print(f"*", end="")
    print("", end="\n")
    cnt -= 1
# *****
# ****
# ***
# **
# *

cnt = 5
r1 = range(0, 5)
for i in r1:
    for j in range(cnt):
        print(f"{j}", end="")
    print("", end="\n")
    cnt -= 1
# 01234
# 0123
# 012
# 01
# 0
cnt = 10
for i in range(1, 10):
    spaces = " " * cnt
    stars = "* " * i
    if i % 2 != 0:
        print(spaces + stars + spaces)
    cnt -= 1

print("-" * 30)
cnt = 10
for i in range(0, 10):
    spaces = " " * i
    stars = "* " * cnt
    if i % 2 != 0:
        print(spaces + stars + spaces)
    cnt -= 1

print("-" * 30)

cnt = 10
for i in range(0, 10):
    spaces_upr = " " * cnt
    stars_upr = "* " * i
    if i % 2 != 0:
        print(spaces_upr + stars_upr + spaces_upr, end="")
    print("", end="\n")
    cnt -= 1
cnt = 10
for i in range(0, 10):
    spaces_upr = " " * i
    stars_upr = "* " * cnt
    if i % 2 != 0:
        print(spaces_upr + stars_upr + spaces_upr, end="")
    print("", end="\n")
    cnt -= 1


print("-" * 30)
cnt = 5
for i in range(0, 5):
    spaces_upr = "" * cnt
    stars_upr = "* " * i
    print(spaces_upr + stars_upr + spaces_upr, end="")
    print("", end="\n")
    cnt -= 1
cnt = 5
for i in range(0, 5):
    spaces_upr = "" * i
    stars_upr = "* " * cnt

    print(spaces_upr + stars_upr + spaces_upr, end="")
    print("", end="\n")
    cnt -= 1


print("-" * 30)


def genreate(i):
    if i == 1:
        return 0
    else:
        return 1


cnt, start = 0, 1
for i in range(0, 5):
    if i % 2 == 0:
        start = 1
    else:
        start = 0
    cnt += 1
    for j in range(cnt):
        print(start, end=" ")
        start = 1 - start
    print("", end="\n")

print("-" * 30)
cnt = 1
for i in range(1, 5):
    cnt += 1
    for j in range(1, cnt):
        print(j, end=" ")
    print("", end="\n")
