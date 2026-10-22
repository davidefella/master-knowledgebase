"""Verifica per esecuzione degli esempi del capitolo 05 (Text Similarity).

Eseguito con Python 3, numpy, scipy, scikit-learn (versioni stampate in testa).
Ogni sezione corrisponde a un blocco di codice del capitolo.
"""
import numpy as np
import scipy
import sklearn
from collections import Counter, defaultdict

print("numpy", np.__version__, "| scipy", scipy.__version__, "| sklearn", sklearn.__version__)

# ---------------------------------------------------------------------------
# 1. Cosine similarity: le tre forme della formula in slide coincidono
# ---------------------------------------------------------------------------
print("\n=== 1. Cosine similarity, tre forme ===")
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

u = np.array([3, 2, 0, 1])   # conteggi u_t (es. star, trek, ring, ship)
v = np.array([2, 3, 0, 0])
s_sum = (u * v).sum() / (np.sqrt((u ** 2).sum()) * np.sqrt((v ** 2).sum()))
s_dot = u @ v / (np.linalg.norm(u) * np.linalg.norm(v))
s_unit = (u / np.linalg.norm(u)) @ (v / np.linalg.norm(v))
print(round(s_sum, 4), round(s_dot, 4), round(s_unit, 4))
print("prodotto scalare NON normalizzato:", u @ v)
print("distanza d = 1 - S:", round(1 - s_sum, 4))

# ---------------------------------------------------------------------------
# 2. String matching: doc1/doc2 della slide hanno similarita' 0
# ---------------------------------------------------------------------------
print("\n=== 2. Esempio string matching della slide ===")
docs = ["Today's soccer match was amazing!",
        "The right player could have scored that goal"]
cv = CountVectorizer(stop_words="english")
X = cv.fit_transform(docs)
print("vocabolario:", cv.get_feature_names_out().tolist())
print("cosine(doc1, doc2) =", cosine_similarity(X)[0, 1])

# ---------------------------------------------------------------------------
# 3. "Good morning!" in uno spazio a 1M dimensioni: 2 componenti non nulle
# ---------------------------------------------------------------------------
print("\n=== 3. Good morning! come vettore sparso ===")
from scipy.sparse import csr_matrix
V = 1_000_000
idx = {"good": 4211, "morning": 15873}       # posizioni arbitrarie nel vocabolario
vec = csr_matrix((np.ones(2), ([0, 0], list(idx.values()))), shape=(1, V))
print("dimensione:", vec.shape[1], "| non zero:", vec.nnz,
      "| frazione non nulla:", vec.nnz / V)

# ---------------------------------------------------------------------------
# 4. 1 - cos non e' una metrica: controesempio alla disuguaglianza triangolare
# ---------------------------------------------------------------------------
print("\n=== 4. Disuguaglianza triangolare con d = 1 - cos ===")
a, b, c = np.array([1, 0]), np.array([1, 1]), np.array([0, 1])
d = lambda x, y: 1 - x @ y / (np.linalg.norm(x) * np.linalg.norm(y))
print("d(a,c) =", round(d(a, c), 4), " d(a,b)+d(b,c) =", round(d(a, b) + d(b, c), 4))

# ---------------------------------------------------------------------------
# 5. Clustering gerarchico agglomerativo su un corpus giocattolo
# ---------------------------------------------------------------------------
print("\n=== 5. Clustering gerarchico (scipy) ===")
from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
from scipy.spatial.distance import pdist, squareform

corpus = [
    "tennis racket ball court serve match",          # 0 tennis
    "ping pong table racket ball serve",             # 1 ping pong
    "golf ball club course hole",                    # 2 golf
    "soccer ball goal player match team",            # 3 calcio
    "rugby ball team player try match",              # 4 rugby
    "government election minister vote parliament", # 5 politica
    "foreign minister embassy treaty government",    # 6 affari esteri
    "church pope christian faith prayer",            # 7 religione
]
labels = ["tennis", "pingpong", "golf", "soccer", "rugby",
          "politics", "foreign", "religion"]
Xc = CountVectorizer().fit_transform(corpus).toarray()
D = pdist(Xc, metric="cosine")                       # d = 1 - cos
print("matrice delle distanze (arrotondata):")
print(np.round(squareform(D), 2))
for method in ["average", "single", "complete"]:
    Z = linkage(D, method=method)
    print(f"\n{method} linkage: {Z.shape[0]} merge per N={len(corpus)} documenti")
    for i, (p, q, h, n) in enumerate(Z):
        name = lambda k: labels[int(k)] if k < len(labels) else f"C{int(k)}"
        print(f"  passo {i+1}: {name(p)} + {name(q)} -> C{len(labels)+i}  altezza={h:.3f}  size={int(n)}")

Z = linkage(D, method="average")
print("\nTaglio del dendrogramma (average linkage):")
for h in [0.5, 0.7, 0.9, 0.99]:
    lab = fcluster(Z, t=h, criterion="distance")
    sizes = sorted(Counter(lab).values(), reverse=True)
    print(f"  cut height {h}: {len(sizes)} cluster, dimensioni {sizes}")
dn = dendrogram(Z, labels=labels, no_plot=True)
print("ordine delle foglie nel dendrogramma:", dn["ivl"])

# Stesso risultato con scikit-learn
from sklearn.cluster import AgglomerativeClustering
ag = AgglomerativeClustering(n_clusters=3, metric="cosine", linkage="average").fit(Xc)
print("sklearn AgglomerativeClustering (3 cluster):", dict(zip(labels, ag.labels_.tolist())))

# ---------------------------------------------------------------------------
# 6. Taglio a diverse altezze su dati sintetici piu' grandi:
#    piu' alto il taglio, cluster piu' grandi e meno numerosi
# ---------------------------------------------------------------------------
print("\n=== 6. Distribuzione delle dimensioni dei cluster al variare del taglio ===")
rng = np.random.default_rng(42)
n_topics, vocab, ndocs = 30, 400, 1500
topic_word = rng.dirichlet(np.full(vocab, 0.05), size=n_topics)
pop = rng.zipf(1.8, size=ndocs) % n_topics             # topic con popolarita' long-tail
docs_counts = np.array([rng.multinomial(15, topic_word[t]) for t in pop])
tfidf = TfidfVectorizer().fit_transform(
    [" ".join(f"w{j}" for j, c in enumerate(row) for _ in range(c)) for row in docs_counts])
Zs = linkage(pdist(tfidf.toarray(), metric="cosine"), method="average")
print("altezze di merge: min %.3f  max %.3f  (N-1 = %d merge)" % (Zs[:, 2].min(), Zs[:, 2].max(), len(Zs)))
for h in [0.5, 0.7, 0.9]:
    lab = fcluster(Zs, t=h, criterion="distance")
    sizes = np.array(list(Counter(lab).values()))
    dist = Counter(sizes.tolist())
    print(f"  cut {h}: {len(sizes)} cluster | singleton {dist.get(1, 0)} | max size {sizes.max()} | media {sizes.mean():.1f}")

# ---------------------------------------------------------------------------
# 7. User interests (procedura della Listing 4.6 del libro, in Python)
# ---------------------------------------------------------------------------
print("\n=== 7. Interessi per utente: frequenze relative per rank ===")
posts = [  # (utente, tag del post)
    ("ann", ["star-trek"]), ("ann", ["star-trek"]), ("ann", ["star-trek", "star-wars"]),
    ("ann", ["story-identification"]),
    ("bob", ["lord-of-the-rings"]), ("bob", ["lord-of-the-rings"]), ("bob", ["harry-potter"]),
    ("cid", ["story-identification"]),
]
user_tags = defaultdict(list)
for user, tags in posts:
    user_tags[user].extend(tags)
by_rank = defaultdict(float)
for user, tags in user_tags.items():
    freqs = sorted((c / len(tags) for c in Counter(tags).values()), reverse=True)
    print(f"  {user}: {[round(f, 3) for f in freqs]}")
    for r, f in enumerate(freqs, start=1):
        by_rank[r] += f
tot = sum(by_rank.values())
print("  media per rank:", {r: round(f / tot, 3) for r, f in sorted(by_rank.items())})

# ---------------------------------------------------------------------------
# 8. LDA su corpus giocattolo (scikit-learn), soft e hard clustering
# ---------------------------------------------------------------------------
print("\n=== 8. LDA (sklearn) su corpus giocattolo ===")
from sklearn.decomposition import LatentDirichletAllocation

news = [
    "parliament minister election vote referendum democracy",
    "minister parliament vote election government",
    "referendum vote democracy parliament election",
    "rain storm flooding water weather river",
    "flooding water rain people storm country",
    "weather storm rain flooding people",
    "shooting bomb police victims terrorism",
    "police terrorism bomb attack victims gun",
    "bomb shooting police gun terrorism",
    "minister police terrorism parliament vote",      # misto politica/cronaca
    "storm flooding minister government water",       # misto disastro/politica
]
cvn = CountVectorizer()
Xn = cvn.fit_transform(news)
vocab_n = cvn.get_feature_names_out()
for seed in [0, 1]:
    lda = LatentDirichletAllocation(n_components=3, random_state=seed, max_iter=200)
    theta = lda.fit_transform(Xn)                       # per-document topic distribution
    print(f"\nrandom_state={seed}")
    for k, row in enumerate(lda.components_):
        top = [vocab_n[i] for i in row.argsort()[::-1][:5]]
        print(f"  topic {k}: {top}")
    print("  theta (prime 3 righe e due documenti misti):")
    for i in [0, 3, 6, 9, 10]:
        print(f"    doc {i:2d}: {np.round(theta[i], 2)}")
    hard = theta.argmax(axis=1)
    soft = [np.where(t >= 0.3)[0].tolist() for t in theta]
    print("  hard (argmax):", hard.tolist())
    print("  soft (soglia 0.3):", soft)
