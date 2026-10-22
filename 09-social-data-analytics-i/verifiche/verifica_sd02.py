"""Verifica per esecuzione dei calcoli e degli esempi del capitolo 02 (SD-02, User Activity).

Sezioni:
  A. calcoli delle slide (rapporti fra periodi, giorni, bot)
  B. esponente gamma ricavato dai numeri del libro [1]
  C. esempio: fit di una power law in scala log-log (dati sintetici)
  D. esempio: CDF e CCDF, esponente della coda gamma + 1
  E. esempio: r2_bar(r1) e R21 su utenti simulati
Eseguire con: python3 verifica_sd02.py
"""
import numpy as np

print("=== A. Calcoli delle slide ===")
print(f"(31+28)/31    = {(31 + 28) / 31:.3f}")
print(f"(31+28+31)/31 = {(31 + 28 + 31) / 31:.3f}")
print(f"mesi ideali da 30 giorni: 60/30 = {60 / 30:.1f}, 90/30 = {90 / 30:.1f}")
U1, U2 = 134_804, 219_604          # utenti attivi in Period 1 e 2 (libro [1], p. 20)
print(f"C21 = U2/U1 = {U2 / U1:.3f}  (slide: 1.6)")
sec_gennaio = 31 * 24 * 3600
for nome, edit in [("ClueBot NG", 80003), ("EmausBot", 79357), ("Addbot", 63136)]:
    print(f"{nome:10s}: {edit} edit in gennaio -> un edit ogni {sec_gennaio / edit:.1f} s")

print("\n=== B. Esponente gamma dai numeri del libro ===")
R21 = 1.75                          # pendenza del fit di r2 contro r1 (libro [1], p. 20)
gamma = -(1 + np.log(U2 / U1) / np.log(R21))
print(f"gamma = -(1 + ln(U2/U1)/ln R21) = {gamma:.3f}  (libro: -1.87)")

print("\n=== C. Fit di una power law in log-log (dati sintetici) ===")
rng = np.random.default_rng(42)
N, alpha = 134_804, 1.87            # stessi ordini di grandezza di Wikipedia, gennaio 2013
edits = rng.zipf(alpha, size=N)     # P(r) proporzionale a r^-alpha, r = 1, 2, ...
print(f"media = {edits.mean():.1f}, mediana = {np.median(edits):.0f}, max = {edits.max()}")
r, U = np.unique(edits, return_counts=True)   # U(r): numero di utenti con r edit
# 1) regressione lineare di ln U(r) su ln r, solo sulla "testa" (r <= 50)
testa = r <= 50
g_testa, lnK = np.polyfit(np.log(r[testa]), np.log(U[testa]), 1)
print(f"OLS su r<=50:        gamma = {g_testa:.3f}, K = {np.exp(lnK):.0f}")
# 2) stessa regressione su tutti i punti: la coda rumorosa ("fanning out") distorce la stima
g_tutto, _ = np.polyfit(np.log(r), np.log(U), 1)
print(f"OLS su tutti i punti: gamma = {g_tutto:.3f}  (distorta dalla coda)")
# 3) binning logaritmico: bucket di ampiezza crescente, conteggio diviso per l'ampiezza
bordi = np.unique(np.floor(np.logspace(0, np.log10(edits.max() + 1), 30)).astype(int))
cont, _ = np.histogram(edits, bins=bordi)
largh = np.diff(bordi)
centro = np.sqrt(bordi[:-1] * (bordi[1:] - 1).clip(min=bordi[:-1]))
ok = cont > 0
g_bin, _ = np.polyfit(np.log(centro[ok]), np.log(cont[ok] / largh[ok]), 1)
print(f"OLS con binning log: gamma = {g_bin:.3f}")

print("\n=== D. CDF, CCDF ed esponente della coda ===")
cdf = np.cumsum(U) / N               # P(r <= rho) per rho = r
ccdf = 1 - cdf                       # P(r > rho)
for rho in (1, 10, 100):
    i = np.searchsorted(r, rho, side="right") - 1
    print(f"rho={rho:3d}: CDF = {cdf[i]:.3f}, CCDF = {ccdf[i]:.3f}, somma = {cdf[i] + ccdf[i]:.1f}")
sel = (r >= 2) & (r <= 200) & (ccdf > 0)
g_coda, _ = np.polyfit(np.log(r[sel]), np.log(ccdf[sel]), 1)
print(f"pendenza della CCDF in log-log = {g_coda:.3f}  (atteso gamma+1 = {1 - alpha:.2f})")

print("\n=== E. r2_bar(r1) e R21 su utenti simulati ===")
# Ogni utente ha un tasso personale di edit al giorno (distribuzione a coda lunga),
# i conteggi nei periodi sono Poisson. Periodo 2 = gennaio + febbraio (sovrapposto al periodo 1).
M = 300_000
tasso = 0.02 * (rng.pareto(0.9, size=M) + 1)
gen = rng.poisson(tasso * 31)
feb = rng.poisson(tasso * 28)
p1, p2 = gen, gen + feb
print(f"utenti attivi: periodo 1 = {np.count_nonzero(p1)}, periodo 2 = {np.count_nonzero(p2)}, "
      f"rapporto = {np.count_nonzero(p2) / np.count_nonzero(p1):.3f}  (rapporto dei giorni = 1.903)")
# r2_bar(r1) = sum_i I(r_i1 = r1) r_i2 / sum_i I(r_i1 = r1)
r1_vals = np.arange(1, 101)
r2_bar = np.array([p2[p1 == k].mean() for k in r1_vals])
R21_sim = np.polyfit(r1_vals, r2_bar, 1)[0]
print(f"r2_bar(r1) per r1 = 1, 10, 50, 100: {np.round(r2_bar[[0, 9, 49, 99]], 1)}")
print(f"pendenza R21 stimata = {R21_sim:.3f}  (tassi costanti: atteso 59/31 = 1.903; Wikipedia: 1.75)")
