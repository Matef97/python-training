import matplotlib.pyplot as plt
from math import sqrt,pow
def mean(l):
    sum = 0
    for i in l :
        sum+=i
    return sum/len(l)  
def median(l):
    l.sort()
    n =len(l)
    if n%2 != 0 :
        return (l[int(n/2)]) 
    else :
        return (l[int(n/2)]+l[int(n/2+1)] )/2
def mode(l):
    s = set(l)
    l1 =list(s)
    freq = list(l.count(i) for i in l1 )
    max_ind = freq.index(max(freq))
    return l1[max_ind]
def sd(l):
    n =len(l)
    mu = mean(l)
    sum =0
    for xi in l :
        sum+= (xi-mu)**2
    var = sum/n
    std = sqrt(var)
    return std        



grades = [10,11,12,14,15,17,13,16,15,17,18,15,17]
Mean = mean(grades)
Med = median(grades)
Mod = mode(grades)
standard_deviation = sd(grades)
print("The standard deviation of  students grades is ",standard_deviation)
print("The mode of students grades is ",Mod)
print("The median of students grades is ",Med)
print("The mean of students grades is ",Mean)
y=[0 for i  in grades]
plt.scatter(grades,y,marker='o')
plt.scatter(mean(grades),[0],marker='x',color = 'red')
plt.scatter(Med,[0],marker='s',color = 'green')
plt.scatter(Mod,[0],marker='p',color = 'yellow')
# plt.errorbar(Mean,0.1,xerr=standard_deviation,fmt='*')
# k=1
# for i in grades :
#     plt.errorbar(i+(Mean-i)/2,k,xerr=standard_deviation,fmt='^')
#     k+=0.1
plt.xlim(0,20)
# plt.boxplot(grades,vert=False) 
plt.xticks([i for i in range(1,20)]) 
plt.yticks([i for i in range(15)])  
# plt.hist(grades,color='blue',rwidth=0.5,cumulative=True,density=True,align='left')
plt.grid()
X= [i for i in range(21)]
F= [(1/(standard_deviation*sqrt(2*3.14)))*pow(2.17,(-0.5*pow((x-Mean)/standard_deviation,2)))for x in X]
plt.plot(X,F)

plt.show()
