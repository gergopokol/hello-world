import numpy as np
import random
import scipy.stats as ss

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