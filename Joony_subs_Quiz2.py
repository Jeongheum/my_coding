import numpy as np
from datetime import datetime

x=int(input('숫자 얼마까지 뺄셈을 할까요? '))
#print("\n")

score = 0
ts=datetime.now()

for i in range(10):
    a=np.random.randint(1,x+1)
    b=np.random.randint(1,x+1)

    if b>a:
        a, b = b, a
    
    #print("%2d + %2d = %2d" %(a,b,a+b))
    y=int(input("%2d) %2d - %2d = " %(i+1,a,b)))

    if y == (a-b):
        score = score +10
        print("Excellent !  %2d - %2d = %2d\n" %(a,b,a-b))
    else:
        print("Think again ! %2d - %2d = %2d\n" %(a,b,a-b))

te=datetime.now()-ts
print ("\n Your score is %d \n"%(score))
print ("It took %d minutes %d seconds \n\n"%(te.seconds//60, te.seconds%60))
