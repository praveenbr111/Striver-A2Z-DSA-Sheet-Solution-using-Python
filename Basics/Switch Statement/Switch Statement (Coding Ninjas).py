url = https://www.naukri.com/code360/problems/switch-case-statement_8357244

import math
from typing import *

def areaSwitchCase(ch: int, a: List[float]):
    # Write your code here
    pass
    match ch:
     case 1: 
        area = math.pi *(a[0]) ** 2 
     case 2: 
        area = a[0] * a[1]
   # return "{:.5f}".format(area)

   # or you can write like this
    return format(area, ".5f") 