url = https://www.geeksforgeeks.org/problems/java-switch-case-statement3529/1


#User function Template for python3
import math
class Solution:
    def switchCase(self, choice, arr):
        match choice:
            case 1:
                return math.pi * (arr[0]) ** 2
            case 2:
                return arr[0] * arr[1]