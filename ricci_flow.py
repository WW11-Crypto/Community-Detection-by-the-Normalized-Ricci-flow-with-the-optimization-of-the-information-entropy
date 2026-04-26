import networkx as nx
from tqdm import tqdm
from .curvature import compute_ricci_curvature


def compute_shortest_paths(G):
    return dict(nx.all_pairs_shortest_path_length(G))


def run_ricci_flow(G, T=10, tau=5, theta=0.1, step_size=0.1, sigma0=1.0):
    weights = {frozenset((u, v)): sigma0 / G.number_of_edges() for u, v in G.edges()}
    all_pairs_shortest_path = compute_shortest_paths(G)

    for t in tqdm(range(1, T + 1), desc="Ricci Flow"):
        curvatures = {frozenset((u, v)): compute_ricci_curvature(G, u, v, weights, all_pairs_shortest_path)
                      for u, v in G.edges()}

        sigma = sum(weights.values())
        total_curvature_weight = sum(curv * weights[e] for e, curv in curvatures.items())

        new_weights = {}
        for edge in G.edges():
            fe = frozenset(edge)
            curv = curvatures[fe]
            update = step_size * (curv + total_curvature_weight / sigma) * weights[fe]
            new_weights[fe] = max(weights[fe] - update, 1e-6)
        weights = new_weights

        if t % tau == 0:
            sorted_edges = sorted(weights.items(), key=lambda x: -x[1])
            num_edges_to_remove = int(len(sorted_edges) * theta)
            for e, _ in sorted_edges[:num_edges_to_remove]:
                u, v = tuple(e)
                G.remove_edge(u, v)

    return G, curvatures, weights
