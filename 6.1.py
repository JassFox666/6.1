import string


def get_range(char_range):

    letters = string.ascii_letters


    start, end = char_range.split('-')


    start_index = letters.index(start)
    end_index = letters.index(end) + 1


    return letters[start_index:end_index]



print(get_range("a-c"))
print(get_range("a-a"))
print(get_range("s-H"))
print(get_range("a-A"))