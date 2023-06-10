#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    count = 0
    string = []
    while count < list_length:
        try:
            res = my_list_1[count] / my_list_2[count]
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except TypeError:
            res = 0
            print("wrong type")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            count = count + 1
            string.append(res)
    return (string)
