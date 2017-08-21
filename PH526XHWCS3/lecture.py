import numpy as np
import random
import scipy.stats as ss
import matplotlib.pyplot as plt

p1 = np.array([1, 1])
p2 = np.array([4, 4])


def distance(p1, p2):
    """Find distance between points p1 and p2."""
    return np.sqrt(np.sum(np.power(p2-p1, 2)))

distance(p1, p2)


def majority_vote(votes):
    """Calculate randomized maximum vote."""
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1

    winners = []
    max_counts = max(vote_counts.values())
    for vote, count in vote_counts.items():
        if count == max_counts:
            winners.append(vote)
    return random.choice(winners)

votes = [1,2,1,3,4,3,2,1,2,3]
winner = majority_vote(votes)

def majority_vote_short(votes):
    mode, count = ss.mstats.mode(votes)
    return mode


votes = [1,2,1,3,4,3,2,1,2,3]
winner = majority_vote_short(votes)


def find_nearest_neighbors(p, points, k=5):
    """Find the k nearest neighbors of p and return their indices"""
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]


def knn_predict(p, points, outcomes, k=5):
    """x"""
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote(outcomes[ind])


def generate_synthetic_data(n=50):
    """Create two sets of points from bivariate normal distributions."""
    points = np.concatenate((ss.norm(0, 1).rvs((n, 2)), ss.norm(0, 1).rvs((n, 2))), axis=0)
    outcomes = np.concatenate((np.repeat(0, n), np.repeat(0, n)))
    return (points, outcomes)


points, outcomes = generate_synthetic_data()

n=20
plt.figure()
plt.plot(points[:n,0], points[:n,1], "ro")
plt.plot(points[n:,0], points[n:,1], "bo")
plt.savefig("bivariate_data.pdf")



def make_prediction_grid(predictors, outcomes, limits, h, k):
    """Classify each point in the prediction grid."""
    (x_min, x_max, y_min, y_max) = limits
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys)

    prediction_grid = np.zeros(xx.shape, dtype=int)
    for i,x in enumerate(xs):
        for j,y in enumerate(ys):
            p = np.array([x, y])
            prediction_grid[j,i] = knn_predict(p, predictors, outcomes, k)
    return (xx, yy, prediction_grid)


from sklearn import datasets
iris = datasets.load_iris()

predictors = iris.data[:, 0:2]
outcomes = iris.target
plt.plot(predictors[outcomes == 0][:,0], predictors[outcomes == 0][:,1], "ro")
plt.plot(predictors[outcomes == 1][:,0], predictors[outcomes == 1][:,1], "go")
plt.plot(predictors[outcomes == 2][:,0], predictors[outcomes == 2][:,1], "bo")
plt.savefig("iris.pdf")