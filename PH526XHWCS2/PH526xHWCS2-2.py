import numpy


def more_frequent(distribution):
    counts = list(distribution.keys())
    frequency_of_counts = list(distribution.values())
    cumsum = numpy.cumsum(frequency_of_counts)
    cumulative = dict(zip(counts, 1 - cumsum / max(cumsum)))
    return cumulative


cumulative = more_frequent(distribution)