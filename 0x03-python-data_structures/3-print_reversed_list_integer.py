def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    leng = len(my_list)
    for i in reversed(my_list):
        print('{:d}'.format(i))
