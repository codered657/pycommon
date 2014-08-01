#   Bit Manipulation Library
#
#   Description: A library containing bit manipulation functions.
#
#   Notes: None.
#   
#   Revision History:
#       Steven Okai     08/01/14    1) Initial revision.
# 

def slice_int(value, upper_index, lower_index):
    slice = value & ~(-1 << upper_index+1); # Mask off upper bits.
    slice = slice >> lower_index;   # Remove lower bits.
    return slice;
