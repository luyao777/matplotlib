import matplotlib.pyplot as plt
import numpy as np 
x = np.linspace(-3,3,50)

y1 = 2 * x + 1
y2 = x ** 2


plt.figure(num = 3, figsize=(8,5))
plt.plot(x,y2)
plt.plot(x,y1, color = 'red', linewidth = 1.0, linestyle='--')

# 取值范围
plt.xlim((-1,2))
plt.ylim((-2,3))
# 描述坐标轴
plt.xlabel('i am x')
plt.ylabel('i am y')
# 坐标单位
new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
# 坐标轴字体
plt.yticks([-2.-1.8,-1,1.22,3],['$really bad$',r'$bad \alpha$',r'$normal$','good','very good'])

# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none') # 四边的边框
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# 改变坐标轴位置
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
plt.show()