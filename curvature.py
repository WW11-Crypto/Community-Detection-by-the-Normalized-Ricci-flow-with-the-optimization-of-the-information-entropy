import numpy as np
from scipy.optimize import linprog


def gamma(w):
    return w


def mu_alpha(G, x, alpha, weights):
    neighbors = list(G.neighbors(x))
    weight_sum = sum(gamma(weights[frozenset((x, z))]) for z in neighbors)
    mu = {x: alpha}
    for y in neighbors:
        w = gamma(weights[frozenset((x, y))])
        mu[y] = (1 - alpha) * w / weight_sum if weight_sum > 0 else 0
    return mu


def wasserstein_distance(mu1, mu2, support1, support2, dist_func):
    n, m = len(support1), len(support2)
    c = [dist_func(a, b) for a in support1 for b in support2]

    A_eq = []
    for i in range(n):
        row = [0] * (n * m)
        for j in range(m):
            row[i * m + j] = 1
        A_eq.append(row)
    b_eq = [mu1.get(support1[i], 0) for i in range(n)]

    for j in range(m):
        row = [0] * (n * m)
        for i in range(n):
            row[i * m + j] = 1
        A_eq.append(row)
    b_eq += [mu2.get(support2[j], 0) for j in range(m)]

    bounds = [(0, 1) for _ in range(n * m)]
    res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs")
    return res.fun if res.success else np.inf


def compute_ricci_curvature(G, x, y, weights, all_pairs_shortest_path):
    alpha = 0.5
    dist = lambda a, b: all_pairs_shortest_path.get(a, {}).get(b, np.inf)
    d_xy = dist(x, y)
    if d_xy == 0:
        return 0

    mu_x = mu_alpha(G, x, alpha, weights)
    mu_y = mu_alpha(G, y, alpha, weights)

    support_x, support_y = list(mu_x.keys()), list(mu_y.keys())
    W = wasserstein_distance(mu_x, mu_y, support_x, support_y, dist)
    return 1 - W / d_xy
