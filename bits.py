#   Bit Manipulation Library
#
#   Description: A library containing bit manipulation functions.
#
#   Notes: None.
#   
#   Revision History:
#       Steven Okai     08/01/14    1) Initial revision.
#       Steven Okai     08/01/14    1) Added set_bit(), clear_bit(), assign_bit(), get_bit().
# 

# TODO: rename to slice?
def slice_int(value, upper_index, lower_index):
    slice = value & ~(-1 << upper_index+1); # Mask off upper bits.
    slice = slice >> lower_index;   # Remove lower bits.
    return slice;

# TODO: function to assign slice

def set_bit(value, index):
    return value | (1 << index);

def clear_bit(value, index):
    return value & ~(1 << index);

def assign_bit(value, bit, index):
    if (bit == 0):
        new_value = clear_bit(value, index);
    else:
        new_value = set_bit(value, index);
    return new_value;

def get_bit(value, index):
    return slice_int(value, index, index);
