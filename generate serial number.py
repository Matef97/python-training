import string
import random

def set_serial(count):
    my_char = string.ascii_letters+string.digits
    limit = len(my_char)
    my_list =[]
    while count > 0 :
       index = random.randint(0,limit)
       my_ser =my_char[index]
       my_list.append(my_ser)
       count-=1
    print("".join(my_list))


set_serial(7)