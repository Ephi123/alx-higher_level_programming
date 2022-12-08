#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    Blist = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            Blist[count] = True
        else:
            Blist[count] = False
    return(Blist)
