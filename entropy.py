import numpy as np
import itertools
import networkx as nx


def compute_community_entropy(G, community, T=10):
    t = 0.1 * T
    n = len(community)
    m = sum([1 for u, v in itertools.combinations(community, 2) if G.has_edge(u, v)])

    A = nx.to_numpy_array(G, nodelist=community)
    D = np.diag([d for _, d in G.degree(community)])
    Delta = A - D
    Delta2 = Delta @ Delta

    A2 = np.sum(Delta2)
    A1 = -2 * m
    B1 = 2 * m

    return (1 / n) * (A1 * t * np.log(t) + B1 * t + A2 * t**2 * np.log(t))
