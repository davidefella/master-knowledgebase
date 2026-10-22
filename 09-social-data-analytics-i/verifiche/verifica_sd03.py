"""Verifica per esecuzione degli esempi del capitolo 03 (Social Networks).

Ogni sezione stampa un'intestazione "== [n]" richiamata nel capitolo.
Eseguire con: python3 verifica_sd03.py   (richiede networkx, numpy, matplotlib)
"""
import math
import random
from collections import Counter, defaultdict
from itertools import combinations

import networkx as nx
import numpy as np

random.seed(42)
np.random.seed(42)

# ---------------------------------------------------------------------------
print("== [1] In-degree e out-degree (grafo della slide 'In- and Out-Degree')")
# Ricostruzione del grafo della slide 14 (SDA25). Nomi dei nodi arbitrari:
# R = nodo rosso; gli altri sono etichettati per posizione nella figura.
G = nx.DiGraph()
G.add_edges_from([
    ("A", "T"), ("A", "R"), ("A", "B"), ("B", "A"),   # A <-> B reciproco
    ("B", "G"),
    ("R", "U"), ("R", "C"), ("R", "G"),               # uscenti dal nodo rosso
    ("T", "C"), ("U", "C"), ("U", "E"), ("U", "F"),
    ("C", "E"), ("C", "G"), ("G", "C"),               # C <-> G reciproco
    ("G", "F"), ("F", "C"),
])
print("nodo rosso: in-degree =", G.in_degree("R"), " out-degree =", G.out_degree("R"))
print("vicini del nodo rosso (in+out, senza duplicati):",
      sorted(set(G.predecessors("R")) | set(G.successors("R"))))
print("in-degree per nodo :", dict(sorted(G.in_degree())))
print("out-degree per nodo:", dict(sorted(G.out_degree())))
print("somma in = somma out = numero archi:",
      sum(d for _, d in G.in_degree()), sum(d for _, d in G.out_degree()), G.number_of_edges())

# ---------------------------------------------------------------------------
print("\n== [2] Coda e testa di un arco in NetworkX")
D = nx.DiGraph([("x", "y")])          # x segue y
(u, v), = D.edges()
print(f"arco ({u}, {v}): origine (tail nella convenzione standard) = {u}, "
      f"destinazione (head) = {v}")
print("successori di x:", list(D.successors("x")), " predecessori di y:", list(D.predecessors("y")))

# ---------------------------------------------------------------------------
print("\n== [3] Grafo pesato: pesi = ritardo, archi assenti = infinito (Figura 2.1)")
INF = math.inf
W = nx.DiGraph()
W.add_weighted_edges_from([
    ("S", "A", 15), ("A", "N2", 20), ("S", "N2", 8), ("N2", "D", 30),
    ("S", "N3", 10), ("N3", "D", 14), ("N1", "N3", 6),
    ("S", "N1", INF), ("N2", "N3", INF),
])
for path in nx.all_simple_paths(W, "S", "D"):
    cost = sum(W[a][b]["weight"] for a, b in zip(path, path[1:]))
    print(" -> ".join(path), "=", cost)
best = nx.dijkstra_path(W, "S", "D")
print("Dijkstra:", " -> ".join(best), "ritardo", nx.dijkstra_path_length(W, "S", "D"))

# ---------------------------------------------------------------------------
print("\n== [4] Completezza: L = N(N-1)/2 archi non diretti")
for N in (3, 4, 10, 1000):
    L = N * (N - 1) // 2
    print(f"N={N}: L={L}  (complete_graph ha {nx.complete_graph(N).number_of_edges()} archi)"
          if N <= 10 else f"N={N}: L={L}")
print("diretto completo (N=4):", nx.complete_graph(4, create_using=nx.DiGraph).number_of_edges(), "= N(N-1)")

# ---------------------------------------------------------------------------
print("\n== [5] Legge di Metcalfe")
for n in (2, 3, 10, 100):
    print(f"n={n}: valore per utente ~ n-1 = {n-1}; valore della rete ~ n(n-1)/2 = {n*(n-1)//2}")

# ---------------------------------------------------------------------------
print("\n== [6] Snowball sampling con BFS (profondità 3)")
H = nx.barabasi_albert_graph(20000, 1, seed=7)    # grafo sintetico, solo per illustrare
center = 123
dist = nx.single_source_shortest_path_length(H, center, cutoff=3)
sample = H.subgraph(dist)                        # solo archi fra nodi inclusi
per_livello = Counter(dist.values())
print("nodi per distanza dal centro:", dict(sorted(per_livello.items())))
print("sottografo:", sample.number_of_nodes(), "nodi,", sample.number_of_edges(), "archi")
rnd = H.subgraph(random.sample(list(H.nodes()), len(dist)))
print("campione casuale della stessa taglia:", rnd.number_of_nodes(), "nodi,", rnd.number_of_edges(), "archi")

# ---------------------------------------------------------------------------
print("\n== [7] Coefficiente di clustering locale (esempio della slide, Figura 2.6)")
C = nx.DiGraph()
# i = nodo centrale; TL, TR, L, BL, BR = vicini (posizioni nella figura)
C.add_edges_from([
    ("TL", "i"), ("TR", "i"), ("i", "L"), ("i", "BR"), ("i", "BL"), ("BL", "i"),
    ("TL", "TR"), ("TR", "TL"), ("TR", "BR"), ("BL", "BR"),
])
nbrs = set(C.predecessors("i")) | set(C.successors("i"))
k = len(nbrs)
n_i = sum(1 for a, b in C.edges() if a in nbrs and b in nbrs)
print(f"k_i = {k}, n_i = {n_i}, k_i(k_i-1) = {k*(k-1)}, C_i = {n_i}/{k*(k-1)} = {n_i/(k*(k-1))}")
print("networkx nx.clustering(DiGraph) (formula di Fagiolo, diversa):", round(nx.clustering(C, "i"), 4))
U = C.to_undirected()
nu = sum(1 for a, b in combinations(nbrs, 2) if U.has_edge(a, b))
print(f"versione non diretta: {nu} archi fra vicini / {k*(k-1)//2} possibili = {nu/(k*(k-1)/2)}; "
      f"nx.clustering = {nx.clustering(U, 'i')}")

# ---------------------------------------------------------------------------
print("\n== [8] Rewiring che conserva in- e out-degree (Figura 2.9)")
edges = [("A", "C"), ("B", "D")]
def degs(es):
    g = nx.DiGraph(es)
    return dict(g.in_degree()), dict(g.out_degree())
print("prima :", edges, degs(edges))
edges = [("A", "D"), ("B", "C")]   # scambio delle destinazioni
print("dopo  :", edges, degs(edges))

# Effetto sul clustering su un grafo con molti triangoli (Holme-Kim), diretto.
HK = nx.powerlaw_cluster_graph(5000, 4, 0.9, seed=3)
DG = nx.DiGraph()
for a, b in HK.edges():
    DG.add_edge(*(a, b) if random.random() < 0.5 else (b, a))

def mean_local_clustering_book(g):
    """Formula del libro: n_i / (k_i (k_i - 1)), vicini = in U out."""
    vals = []
    out = {u: set(g.successors(u)) for u in g}
    for u in g:
        nb = set(g.predecessors(u)) | out[u]
        kk = len(nb)
        if kk < 2:
            continue
        links = sum(1 for v in nb for w in out[v] if w != u and w in nb)
        vals.append(links / (kk * (kk - 1)))
    return float(np.mean(vals))

def rewire_list(edges, rounds_factor=10, seed=0):
    """Listing 2.7 del libro: scambia le destinazioni di due archi scelti a caso.
    Come nel libro, non si evitano self-loop e archi doppi."""
    rng = random.Random(seed)
    es = [list(e) for e in edges]
    for _ in range(rounds_factor * len(es)):
        e1, e2 = rng.randrange(len(es)), rng.randrange(len(es))
        es[e1][1], es[e2][1] = es[e2][1], es[e1][1]
    return [tuple(e) for e in es]

orig = list(DG.edges())
rew = rewire_list(orig)
same_out = Counter(a for a, _ in orig) == Counter(a for a, _ in rew)
same_in = Counter(b for _, b in orig) == Counter(b for _, b in rew)
print("sulla lista di archi: out-degree identici:", same_out, " in-degree identici:", same_in)
n_self = sum(1 for a, b in rew if a == b)
n_dup = len(rew) - len(set(rew))
print(f"dopo lo scambio: {n_self} self-loop e {n_dup} archi doppi su {len(rew)} (scartati nel DiGraph)")
RW = nx.DiGraph(); RW.add_nodes_from(DG); RW.add_edges_from((a, b) for a, b in rew if a != b)
c0, c1 = mean_local_clustering_book(DG), mean_local_clustering_book(RW)
print(f"clustering medio (formula del libro): originale {c0:.4f}, rewired {c1:.4f}, rapporto {c0/c1:.0f}x")

# ---------------------------------------------------------------------------
print("\n== [9] Assortatività e 'i tuoi amici sono più popolari di te'")
BA = nx.barabasi_albert_graph(20000, 3, seed=1)
print("coefficiente di assortatività (Newman) BA:", round(nx.degree_assortativity_coefficient(BA), 4))
annd = nx.average_neighbor_degree(BA)
quota = np.mean([annd[u] > BA.degree(u) for u in BA])
print(f"quota di nodi con grado medio dei vicini > proprio grado: {quota:.3f}")
deg = np.array([d for _, d in BA.degree()])
print(f"grado: media {deg.mean():.2f}, mediana {np.median(deg):.0f}, max {deg.max()}")

# ---------------------------------------------------------------------------
print("\n== [10] Urna di Pólya / preferential attachment (Listing 2.5, porting Python 3)")

def polya_book(rounds=10000, p=0.2, seed=0):
    """Porting fedele del Listing 2.5 (xrange/iteritems -> range/items)."""
    rnd = random.Random(seed)
    bin_balls = defaultdict(int)
    bin_balls[0] = 1
    for rnd_i in range(0, rounds):
        if rnd.random() < p:
            bin_balls[len(bin_balls)] = 1
        else:
            threshold = rnd.randint(1, rnd_i + 1)
            s = 0
            for b, balls in bin_balls.items():
                s += balls
                if s >= threshold:
                    bin_balls[b] += 1
                    break
    return bin_balls

def polya_fast(rounds, p, seed=0):
    """Stesso processo in O(1) per passo: scegliere una pallina uniforme
    equivale a scegliere un cestino con probabilità proporzionale alle sue palline."""
    rnd = random.Random(seed)
    owner = [0]                 # owner[j] = cestino della pallina j
    counts = [1]
    for _ in range(rounds):
        if rnd.random() < p:
            counts.append(1)
            owner.append(len(counts) - 1)
        else:
            b = owner[rnd.randrange(len(owner))]
            counts[b] += 1
            owner.append(b)
    return np.array(counts)

def mle_alpha(x, xmin):
    """Stimatore discreto approssimato di Clauset, Shalizi, Newman (2009), eq. 3.7."""
    x = x[x >= xmin]
    return 1 + len(x) / np.sum(np.log(x / (xmin - 0.5))), len(x)

bb = polya_book()
tot = sum(bb.values())
dist_b = Counter(bb.values())
print(f"Listing 2.5 (ROUNDS=10000, P=0.2): {len(bb)} cestini, {tot} palline; "
      f"cestini con 1,2,3 palline: {dist_b[1]}, {dist_b[2]}, {dist_b[3]}; max {max(bb.values())}")

results = {}
XMINS = {0.1: (10, 100), 0.2: (10, 100), 0.5: (10, 40), 0.8: (4, 12)}
for p in (0.1, 0.2, 0.5, 0.8):
    k = polya_fast(4_000_000, p, seed=11)
    results[p] = k
    stime = ", ".join(f"xmin={xm}: {mle_alpha(k.astype(float), xm)[0]:.3f}" for xm in XMINS[p])
    print(f"p={p}: cestini={len(k)}, max={k.max()}, alpha stimato [{stime}], "
          f"teorico 1+1/(1-p)={1 + 1/(1-p):.3f}")

# Barabási-Albert (grafo non diretto, m=1): esponente atteso 3
ba = nx.barabasi_albert_graph(200000, 1, seed=5)
dba = np.array([d for _, d in ba.degree()], dtype=float)
print("Barabási-Albert m=1, n=200000: alpha stimato = %.3f (atteso 3)" % mle_alpha(dba, 10)[0])

# Uniforme (niente preferential attachment): nessuna legge di potenza
def uniform_urn(rounds, p, seed=0):
    rnd = random.Random(seed); counts = [1]
    for _ in range(rounds):
        if rnd.random() < p: counts.append(1)
        else: counts[rnd.randrange(len(counts))] += 1
    return np.array(counts)
ku = uniform_urn(4_000_000, 0.2, seed=11)
print(f"senza preferential attachment (p=0.2): max palline={ku.max()}, "
      f"con PA max={results[0.2].max()}")

# Figura
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    for p, mk in ((0.2, "o"), (0.5, "s"), (0.8, "^")):
        c = Counter(results[p]); xs = np.array(sorted(c)); ys = np.array([c[x] for x in xs]) / len(results[p])
        ax.loglog(xs, ys, mk, ms=3, alpha=.6, label=f"p={p}  (α teorico {1+1/(1-p):.2f})")
    c = Counter(ku); xs = np.array(sorted(c)); ys = np.array([c[x] for x in xs]) / len(ku)
    ax.loglog(xs, ys, "x", ms=3, color="gray", label="p=0.2 senza PA (uniforme)")
    ax.set_xlabel("palline nel cestino (in-degree)"); ax.set_ylabel("frazione di cestini (densità)")
    ax.set_title("Urna di Pólya generalizzata, 4·10⁶ passi")
    ax.legend(fontsize=8); fig.tight_layout()
    fig.savefig("/mnt/user-data/outputs/sd/lezione-03/polya_powerlaw.png", dpi=110)
    print("figura salvata: polya_powerlaw.png")
except Exception as e:  # pragma: no cover
    print("figura non salvata:", e)
