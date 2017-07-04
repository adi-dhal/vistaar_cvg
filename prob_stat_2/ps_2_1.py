import numpy as np
import sys
import matplotlib.pyplot as plt
fil_nam=sys.argv[1]
out_file=sys.argv[2]
x_cord=[]
y_cord=[]
with open(fil_nam) as filename:
	for line in filename:
		x_cord.append(line.split()[0])
		y_cord.append(line.split()[1])
n=len(x_cord)
x_arr=np.float32(x_cord)
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
