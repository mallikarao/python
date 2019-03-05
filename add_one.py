'''
    Given a list of intergers
    return the integer with one added to the
    number represented in the list.
    For example: [1,3,5]->[1,3,6]
    [9,9]->[1,0,0]
    [0,0,0]->[1,1,1]

    Assume that the list is never empty
    The list elements are in range 0-9
'''


def add_one(array):
    '''
        example
        array = [1,3,5]
    '''
    new_array = []
    if array[-1] < 9:
        ele = array[-1]+1
        array[-1] = ele
        return array
    is_nine = False
    for ele in array:
        if ele >= 9:
            ele = 0
            is_nine = True
        else:
            ele += 1
        new_array.append(ele)
    if is_nine:
        new_array = [1]+new_array
    return new_array

print "[1,3,5]-->", add_one([1,3,5])
print "[9,9,9]-->", add_one([9,9,9])
print "[9,9,8]-->", add_one([9,9,8])
print "[8,9,8]-->", add_one([8,9,8])
print "[8,8,8]-->", add_one([8,8,8])
