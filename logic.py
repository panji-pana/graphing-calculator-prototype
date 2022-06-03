import numpy as np

f = open("operators.txt", "r")
data = f.read()
operators = eval(data)
f.close()

equation = "((3^2 + 8*9 - 26/2)/sin(52.8 deg)) ^s inh(5)"

def conversion(e,x):
    for i in range(int(len(operators))):
        e = e.replace(operators[i][0],operators[i][1])
        e = e.replace('x','('+str(x)+')')

    return e

def evaluate(e,x):
    return eval(conversion(e,x))