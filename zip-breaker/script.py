def stack(current_set, chars):
    new_set = set()
    for item in current_set:
        for char in chars:
            new_set.add(item + char)
    return new_set


lst = {"a", "b", "c"}
dct = "abc"

