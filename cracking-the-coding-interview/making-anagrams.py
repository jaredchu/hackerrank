def number_needed(a, b):
    chars_a = str_to_chars(a)
    chars_b = str_to_chars(b)
    return len(diff(chars_a, chars_b)) + len(diff(chars_b, chars_a))


def str_to_chars(str):
    chars = []
    for char in str:
        chars.append(char)
    return sorted(chars)


def diff(a, b):
    x = a.copy()
    y = b.copy()
    for i in x:
        if i in y:
            y.remove(i)
    return y

a = input().strip()
b = input().strip()

print(number_needed(a, b))