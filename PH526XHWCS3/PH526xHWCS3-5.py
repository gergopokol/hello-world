def accuracy(predictions, outcomes):
    return np.mean(predictions == outcomes)

x = np.array([1,2,3])
y = np.array([1,2,4])

print(accuracy(x,y))
