import numpy as np
import matplotlib.pyplot as plt
import sys

if len(sys.argv) != 2:
	print ('Pass the data file name\n')
	sys.exit(0)

arr =  [] 

with open(sys.argv[1]) as fp:
    for line in fp.readlines():
        arr.append(int(line))
    
x = np.linspace(start = 0, stop = 10000, num = len(arr) + 1)

x_label = []
for i in range(len(x) - 1):
    x_label.append(f'{format(x[i], ".0f")} ~ {format(x[i+1], ".0f")}')


plt.bar(x_label , height = arr)
plt.xticks(rotation=90)
plt.tight_layout()
plt.yscale('log')
plt.title("Floating-point numbers distribution")
plt.xlabel('bins')
plt.ylabel('Quantity of floating-point numbers')
plt.show() 