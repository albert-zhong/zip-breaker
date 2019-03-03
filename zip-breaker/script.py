def stack(current_list, dictionary):
    new_list = current_list
    for item in current_list.copy():
        for entry in dictionary:
            new_list.add(item + entry)
    return new_list


def show_all(dct, length):
    final_list = set()
    for char in dct:
        final_list.add(char)

    for x in range(1, length):
        final_list = stack(final_list, dct)

    return final_list


lst = {"a", "b", "c"}
dct = "abc"

my_list = show_all(dct, 4)

for entry in my_list:
    print(entry)
