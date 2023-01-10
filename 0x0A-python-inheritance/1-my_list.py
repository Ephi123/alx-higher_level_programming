#!/usr/bin/python3
''' Module: 1-my_list
'''


class MyList(list):
    ''' Represents a MyList
    '''

    def print_sorted(self):
        '''
        prints the list, but in way sorted
        '''
        print(sorted(self))
