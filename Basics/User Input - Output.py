url = https://www.naukri.com/code360/problems/find-character-case_58513?leftPanelTabValue=PROBLEM

""" 1 way of doing it"""

ch = input()

asci_value = ord(ch)

if 65 <= asci_value <= 90:
   print(1)
elif 97 <= asci_value <= 122:
    print(0)
else:
    print(-1)

# --------------------------------------------

""" 2 way of doing it """

ch = input()

upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_case = 'abcdefghijklmnopqrstuvwxyz'

# remember you wrote for loop here insted of if
# so rember use if, you wrote like this
# for ch in upper_case:
#     print(1)

if ch in upper_case:
    print(1)
elif ch in lower_case:
    print(0)
else:
    print(-1)


# ---------------------------------------------

""" 3 way of doing it using in built functions """

ch = input()

if ch.isupper():
    print(1)
elif ch.islower():
    print(0)
else:
    print(-1)



""" 4 way of doint it"""

ch = input()

if (ch >= 'A') and (ch <= 'Z'):
    print(1)
elif (ch >= 'a') and (ch <= 'z'):
    print(0)
else:
    print(-1)

