from logic import conversion as convert
from logic import evaluate
from animation import animate

f = 'e^x'
x = []
y = []

for i in range(10):
    x.append(i)
    y.append(evaluate(f,x[i]))

animate(x,y)