def print_line(char):
    print(char * 30)


def print_line_times(n, char):
    """
    :param n: times
    :param char: split char
    :return:
    """
    i = 1
    while i <= n:
        print_line(char)
        i += 1

print_line_times(3,"!")