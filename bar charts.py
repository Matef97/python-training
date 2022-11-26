import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn')
fig,ax = plt.subplots(nrows=2,ncols=2)
x = [25,26,27,28,29,30,31,32,33,34,35]
y = [38496,42000,46752,49320,53200,56000,62316,64928,73752,76333,80000]

ax[0,0].plot(x,y,label = 'mean sal',color = 'r')
ax[0,0].set_xlabel('age')
ax[0,0].set_ylabel('salary')
ax[0,0].set_title('salaries for developers')
plt.grid()
x1 = [25,26,27,28,29,30,31,32,33,34,35]
y1 = [45372,48876,53850,57825,63016,65998,70003,70000,71496,75490,83460]
ax[0,1].plot(x1,y1,label = 'mean eng',color = 'g')
ax[0,1].set_xlabel('age')
ax[0,1].set_ylabel('salary')
ax[0,1].set_title('salaries for engineers')
ax[1,1].bar(x,y,label = 'mean sal',color = 'b')
ax[1,1].set_xlabel('age')
ax[1,1].set_ylabel('salary')
ax[1,1].set_title('salaries for developers')
ax[1,0].bar(x1,y1,label = 'mean eng',color = 'g')
ax[1,0].set_xlabel('age')
ax[1,0].set_ylabel('salary')
ax[1,0].set_title('salaries for engineers')
ax[0,0].legend()
ax[0,1].legend()
ax[1,1].legend()
ax[1,0].legend()


plt.tight_layout()

plt.show()

