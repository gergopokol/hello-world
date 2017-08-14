import time

results = []
start_time = time.time()
for game in range(999):
    results += [play_game()]
end_time = time.time()
print((end_time-start_time)/1000.)

plot = plt.hist(results)
plt.show()
