#importing numpy commands
import numpy as np
np.random.seed(0)
#here seed funtion is used for reproducabilty it will give same random number when we re run the program
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