#!/usr/bin/python
__author__ = 'Mayank'


class SumList(object):
    def __init__(self, this_list):
        self.list = this_list

    # Override add method
    def __add__(self, other):
        new_list = [x + y for x, y in zip(self.list, other.list)]

        # Elaborating above code :
        # new_list = []
        # zipped_list = zip(self.list, other.list)
        # for tup in zipped_list:
        #   new_list.append(tup[0] + tup[1])

        return SumList(new_list)

    # Overridden method
    def __repr__(self):
        return str(self.list)


listA = SumList([1, 2, 3, 4, 5])
listB = SumList([100, 200, 300, 400, 500])

listC = listA + listB
print listC
