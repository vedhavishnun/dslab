#importing numpy commands
import numpy as np
np.random.seed(0)
#here seed funtion is used for reproducabilty it will give same random number when we rerun the program
#experiment 1 array indexing
#single dimensional array
x1=np.random.randint(10,size=6)
print("single dimension array :",x1)
print(x1[3])
print(x1[4])
#two dimensional array
x2=np.random.randint(10,size=(3,3))
print("two dimensional array:",x2)
print(x2[2,2])
print(x2[0,1])
print(x2[2,0])
#experiment 2 slicing
#single dimensional array
print(x1[2:5])
print(x1[2:])
print(x1[:4])
#two dimensional array
print(x2[0:,2:])
#here first index 0: refers to row and 2:refers to coloumn
print(x2[:1,2:])
#experiment 3 sub array can be derived by slicing method same process