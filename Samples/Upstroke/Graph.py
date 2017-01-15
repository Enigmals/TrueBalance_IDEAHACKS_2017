import pickle
import matplotlib.pyplot as plt

vectorDataL = []
timeDataL = []
startTimeL = 0

vectorDataR = []
timeDataR = []
startTimeR = 0

# Reading in Left Data
with open('vectorDataL.txt', 'r') as f:
    startTimeL = float(f.readline())
    vectorDataL = [float(line.rstrip('\n')) for line in f]
with open('timeDataL.txt', 'r') as f:
    timeDataL = [float(line.rstrip('\n'))/1000 for line in f]
offset = timeDataL[0]
count = 0
for t in timeDataL:
    timeDataL[count] = t - offset
    count = count + 1

# Reading in Right Data    
with open('vectorDataR.txt', 'r') as f:
    startTimeR = float(f.readline())
    vectorDataR = [float(line.rstrip('\n')) for line in f]
with open('timeDataR.txt', 'r') as f:
    timeDataR = [float(line.rstrip('\n'))/1000 for line in f]

offset = timeDataR[0]
count = 0
for t in timeDataR:
    timeDataR[count] = t - offset
    count = count + 1
#print("VectorData:")
#print (vectorData)
#print("TimeData:")
#print (timeData)

fig = plt.figure()
ax1 = fig.add_subplot(111)

offset = startTimeR - startTimeL
count = 0
for t in timeDataR:
    timeDataR[count] = t + offset
    count = count + 1

#print "Rsizes: ", len(startTimeR), len(vectorDataR)
#print "Lsizes: ", len(startTimeL), len(vectorDataL)

ax1.scatter(timeDataL, vectorDataL, s=10, c='b', marker="s", label='Left')
ax1.scatter(timeDataR, vectorDataR, s=10, c='r', marker="o", label='Right')

plt.legend(loc='upper left')
plt.show()
