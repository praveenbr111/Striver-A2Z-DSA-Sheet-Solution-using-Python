url = https://www.naukri.com/code360/problems/sum-of-even-odd_624650

## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)


''' 1 way of doing it'''

n = int(input())
val1 = 0
val2 = 0

Rember you can iterate throug integers only strings and lists are iteratabel
so we convet the input number to string then take string first value and conver to int to check even or odd

for i in str(n):
    digi = int(i)
    if digi & 1 == 0:
        val1 += digi
    else:
        val2 += digi
    
print(val1,'',val2)

'''2 way of doing it
we can do this using while loop'''


number = int(input())
val1 = 0
val2 = 0

# Here we are doing floor division so when we drop the n by the last step it will be 0


# Example: n = 350
# Let?s walk through each step:

# | Step |   n   | n % 10 (last digit) | n // 10 (remaining) |
# |------|-------|----------------------|----------------------|
# |  1   |  350  |          0           |         35           |
# |  2   |   35  |          5           |          3           |
# |  3   |    3  |          3           |          0           |



while number > 0:
    n = number % 10
    if n & 1 == 0:
        val1 += n
    else:
        val2 += n
    
    number //= 10
    # or
    #number = number // 10

print(val1,'',val2)
















