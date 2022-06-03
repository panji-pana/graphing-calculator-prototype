import re
# regex tester : https://www.regextester.com/
# regex cheatsheet : https://docs.rackspace.com/support/how-to/regex-cheat-sheet-basics/
# regex guide : https://regextutorial.org/

e1 = 'y+2*x=2*y+x'
e2 = 'y-2*y=x-2*x'

global r_formula
global r_aim

r_formula= '(\d*\*{0,2}(x|y)?(\+|\-)?)*=(\d*\*{0,2}(x|y)?(\+|\-)?)*'
# re for any equation with x on left or right and y on left or right
r_aim= '(\d*\*?y(\+|\-)*)+\=(\d*\*?x(\+|\-)*)+'
# re for any equation with all y on left and all x on right



# we want to get anything following r_formula to get to r_aim
def rearrange(e):
    if re.match(r_formula,e):
        print("match")
        

rearrange(e1)
rearrange(e2)

