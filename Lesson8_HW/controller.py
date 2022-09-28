from input_data import *
from get_data import *
from search_data import *
from logger import *

def start():

    hlp_n = int(input('Enter number:\n1 - to find user \n2 - to add user\n'))
    if hlp_n == 1:
        found = get_data()
        fnd = search(found)
        log_search(fnd)

    if hlp_n == 2:
        new_data = input_data()
        log_added(new_data)