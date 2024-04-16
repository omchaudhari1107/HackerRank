alphanum = input()
if alphanum.isalnum:
    lower_case = [i for i in alphanum if i.islower()]
    upper_case = [i for i in alphanum if i.isupper()]
    digit = [x for x in alphanum if x.isdigit()]
    odd_digit = [i for i in digit if int(i) % 2 != 0]
    even_digit = [i for i in digit  if int(i) % 2 == 0]
    print("".join(sorted(lower_case)+sorted(upper_case)+sorted(odd_digit)+sorted(even_digit)))

