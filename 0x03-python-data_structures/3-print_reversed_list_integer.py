def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    leng = len(my_list)
    for i in  my_list:
        leng = leng -1
        print('{:d}'.format(my_list[leng]))
