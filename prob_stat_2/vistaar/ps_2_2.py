import numpy as np
import sys
import matplotlib.pyplot as plt
fil_name=sys.argv[1]
out_file=sys.argv[2]
y_cord=[]
with open(fil_name) as filename:
	for line in filename:
		y_cord.append(line.split()[0])
n=len(y_cord)
print(n)
x_arr=np.arange(0.0,100.0,0.5)
print(len(x_arr))
y_arr=np.float32(y_cord)
x_sum=np.sum(x_arr)
y_sum=np.sum(y_arr)
x_sqsum=np.sum(np.square(x_arr))
x_inn=np.inner(x_arr,y_arr)
mat=np.array(([n,x_sum],[x_sum,x_sqsum]))
mat=np.linalg.inv(mat)
mat_2=np.array(([y_sum],[x_inn]))
ans=np.matmul(mat,mat_2)
print(ans[0])
print(ans[1])
y_pred=ans[1]*x_arr + ans[0]
plt.plot(x_arr,y_pred)
plt.plot(x_arr,y_arr,'ro')
plt.show()
with open(out_file,"w") as filename:
	filename.write("INTERCEPT: " + str(ans[0])+"\n"+"SLOPE: "+str(ans[1]))
filename.close()
