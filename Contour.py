import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#path = 'C:\Users\dlaw1\Documents\VSCode\Example_SEM_v2.bmp'
im = plt.imread("Example_SEM_v2.bmp") #converts bmp into an array of values
imnumpy = np.array(im) #convert to np.array
#imnumpy[imnumpy<100] = 0 #immediately zeros out many pixels
ranger = 2 #define number of pixels adjacent to search for max value (higher number --> longer runtime)
sizer = len(imnumpy[1]) #finds pixel length of image, assumes perfectly square image
lengther = range(0,sizer,1)
contour_array = np.zeros((sizer,sizer)) #makes a matrix of zeros for contour values to be entered
x = range(ranger-1,(sizer-ranger),1) #defines search size based on range being searched, to avoid issues with the edge of the image
y = x #square, sets y to x
i_range = range(-ranger,ranger,1)
j_range = range(-ranger,ranger,1)
ranger_sizing = range(0,2*ranger+1,1) #for looking at adjacent pixels
a_xtester = [[0 for column in ranger_sizing] for row in ranger_sizing] #storing local offsets
a_ytester = [[0 for column in ranger_sizing] for row in ranger_sizing] #storing local offsets
for g in ranger_sizing:
    for h in ranger_sizing:
        a_xtester[g][h] = h-(ranger) #defines x indicies in relation to a given i,j coordinate
        a_ytester[g][h] = g-(ranger) #defines y indicies in relation to a given i,j coordinate


for i in x:
    for j in y:
        x_adjacenter = [[i for column in ranger_sizing] for row in ranger_sizing]
        y_adjacenter = [[j for column in ranger_sizing] for row in ranger_sizing]
        x_closer = [[a_xtester[k][l] + x_adjacenter[k][l] for l in range(len(a_xtester[0]))] for k in range(len(a_xtester[0]))]
        y_closer = [[a_ytester[k][l] + y_adjacenter[k][l] for l in range(len(a_ytester[0]))] for k in range(len(a_ytester[0]))]
        local_nums = [[imnumpy[m][n] for m in range(len(x_closer[0]))] for n in range(len(y_closer[0]))]
        if imnumpy[i][j] > 0 and imnumpy[i][j] > max(max(local_nums)):
            contour_array[i][j] = 255

print(contour_array[1])
print(len(contour_array))

contour_numpy = np.array(contour_array)
plt.imshow(contour_numpy)