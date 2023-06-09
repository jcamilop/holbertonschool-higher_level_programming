#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replace_my_list = []
    for i in my_list:
        if i == search:
            replace_my_list.append(replace)
        else:
            replace_my_list.append(i)
    return replace_my_list
