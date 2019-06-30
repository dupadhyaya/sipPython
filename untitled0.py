#
#-----------------------------
#%
# library
import matplotlib.pyplot as plt
import numpy as np
# Create bars
barWidth = 0.9
bars1 = [3, 3, 1]
bars2 = [4, 2, 3]
bars3 = [4, 6, 7, 10, 4, 4]
bars4 = bars1 + bars2 + bars3
bars4
# The X position of bars
r1 = [1,5,9]
r2 = [2,6,10]
r3 = [3,4,7,8,11,12]
r4 = r1 + r2 + r3

# Create barplot
plt.bar(r1, bars1, width = barWidth, color = (0.3,0.1,0.4,0.6), label='Alone')
plt.bar(r2, bars2, width = barWidth, color = (0.3,0.5,0.4,0.6), label='With Himself')
plt.bar(r3, bars3, width = barWidth, color = (0.3,0.9,0.4,0.6), label='With other genotype')
# Note: the barplot could be created easily. See the barplot section for other examples.

# Create legend
plt.legend()

# Text below each barplot with a rotation at 90°
plt.xticks([r + barWidth for r in range(len(r4))], ['DD', 'with himself', 'with DC', 'with Silur', 'DC', 'with himself', 'with DD', 'with Silur', 'Silur', 'with himself', 'with DD', 'with DC'], rotation=90)

# Create labels
label = ['n = 6', 'n = 25', 'n = 13', 'n = 36', 'n = 30', 'n = 11', 'n = 16', 'n = 37', 'n = 14', 'n = 4', 'n = 31', 'n = 34']

# Text on the top of each barplot
for i in range(len(r4)):
    plt.text(x = r4[i]-0.5 , y = bars4[i]+0.1, s = label[i], size = 6)

# Adjust the margins
plt.subplots_adjust(bottom= 0.2, top = 0.98)

# Show graphic
plt.show()

#simple
xval = ['Gear1', 'Gear2', 'Gear3']
yval = [9, 5, 10]
plt.bar(x=xval, height=yval)

#more options
plt.bar(x=xval, height=yval, color=['b','g','r'])
barWidth = 0.8
#
plt.bar(x=xval, height=yval, width = barWidth, color = (.4,.7, .9), label='Cars : Gear Types')

#labels
label = yval
len(yval)
plt.bar(x=xval, height=yval, color=['b','g','r'])
plt.text(x = 0 , y = 9 +0.1, s = yval[i], size = 10)

#put this in a loop
plt.bar(x=xval, height=yval, color=['b','g','r'])
for i in range(len(yval)):
    plt.text(x = i , y = yval[i]+0.1, s = label[i], size = 10)
plt.legend() #no effect as there is no third dim
#

#
#Tick labels
plt.bar(x=xval, height=yval, color=['b','g','r'])
plt.xticks([i for i in range(len(xval))], ['Car-Gear1', 'Car-Gear2', 'Car-Gear3'], rotation=90)
plt.yticks(np.arange(0,12,1))

#Axis Labels
plt.bar(x=xval, height=yval, color=['b','g','r'])
plt.xlabel('Cars with Gear Types')
plt.ylabel('Count of Cars')
plt.title(" Summary of Cars : Gear Types", loc='center', y=1.2 , fontsize=18)
plt.suptitle("Subtitle - Sample Cars", y=1.0, fontsize=14)
