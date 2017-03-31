import random

random.seed(1)

def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    average_x=[]
    for i in range(n):
        average_x.append(sum(x[i:i+width])/width)
    return average_x
    # To complete the function,
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.

x=[0,10,5,3,1,5]
print(moving_window_average(x, 1))

random.seed(1)  # This line fixes the value called by your function,
# and is used for answer-checking.

R=1000
x=[]
for x_index in range(R):
    x.append(random.uniform(0,1))
Y=[x]
for Y_index in range(1,10):
    Y.append(moving_window_average(x,n_neighbors=Y_index))

ranges=[]
for Y_index in range(0,10):
    ranges.append(max(Y[Y_index])-min(Y[Y_index]))

print(ranges)