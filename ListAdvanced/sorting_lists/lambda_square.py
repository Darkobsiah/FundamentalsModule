def ascii_representation(a):
    return chr(a)


some_list = [32, 35, 67, 34, 886]

ascii_nums = list(map(ascii_representation, some_list))
print(ascii_nums)