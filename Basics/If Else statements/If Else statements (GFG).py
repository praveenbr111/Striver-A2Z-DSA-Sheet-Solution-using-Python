url = https://www.geeksforgeeks.org/problems/java-if-else-decision-making0924/0

class Solution:
    def compareNM(self, n : int, m : int) -> str:
        if n > m:
            return 'greater'
        elif n < m:
            return ('lesser')
        else:
            return ('equal')

