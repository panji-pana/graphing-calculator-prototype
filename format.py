import re
# regex tester : https://www.regextester.com/
# regex cheatsheet : https://docs.rackspace.com/support/how-to/regex-cheat-sheet-basics/
# regex guide : https://regextutorial.org/
# from sympy import *

e1 = 'y+2*x=2*y+x'
e2 = 'y-21y+302y=x-2x+89x-4x'
  
global r_formula
global r_aim

r_formula= r'(\d*\*{0,2}(x|y)?(\+|\-)?)*=(\d*\*{0,2}(x|y)?(\+|\-)?)*'
# re for any equation with x on left or right and y on left or right
r_aim= r'(\d+\*?y?(\+|\-)*)*=?(\d+\*?x?(\+|\-)*)+'
# re for any equation with all y on left and all x on right


def format(eq,pattern,sub):
    i=0
    for match in re.finditer(pattern, eq):
        e = match.end()-1+i
        eq = eq[:e]+sub+eq[e:]
        i+=1
    return eq


pattern1=r'(?<!\d)[a-z]'
pattern2=r'\d+(?!\*)[a-z]'
e2=format(format(e2,pattern1,'1'),pattern2,'*')

print(e2)