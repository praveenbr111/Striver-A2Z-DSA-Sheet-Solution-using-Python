url = https://www.naukri.com/code360/problems/data-type_8357232


from typing import *


"""1 way of doing this"""

def dataTypes(type: str):
    pass
    if type == 'Long':
        return 8
    elif type == 'Integer':
        return 4
    elif type == "Float":
        return 4
    elif type == "Double":
        return 8
    else:
        return 1

# --------------------------------------------------------------

""" 2 way of doing this"""

data = {'Long':8,'Integer':4,'Float':4,'Double':8,'Character':1}

def dataTypes(type:str):
    pass
    return data[type]