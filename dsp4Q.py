import numpy as np
from matplotlib import pyplot as plt
input_signal=[-1,1,2]
output_signal=[]
factor=3
for i in input_signal:
	output_signal.append(i)
	for j in range(0,factor-1):
		output_signal.append(0)
		
print(output_signal)
plt.subplot(2,1,1)
plt.stem(input_signal)
plt.subplot(2,1,2)
plt.stem(output_signal)
plt.show()
