# 03 - Distribuzioni di probabilità

> Fonte Notion: https://app.notion.com/p/32f12abc808d81798b60f3c83b01cf7f — ultima modifica 2026-03-26T15:03:23.243Z

Le distribuzioni di probabilità descrivono come si distribuiscono i valori di una variabile casuale. Sono il fondamento di statistica inferenziale, ML e simulazione.
---
## Variabile casuale e distribuzione
Una **variabile casuale** è una variabile il cui valore dipende dall'esito di un fenomeno aleatorio. La sua **distribuzione di probabilità** descrive la probabilità associata a ciascun valore (o intervallo di valori).
- **Discreta:** prende valori in un insieme numerabile (es. numero di click, numero di difetti)
- **Continua:** prende valori in un intervallo reale (es. altezza, temperatura, tempo di risposta)
---
## Distribuzione normale (Gaussiana)
La più importante in statistica. Descrive fenomeni naturali dove i valori si concentrano attorno a una media con simmetria.
**Parametri:** μ (media) e σ (deviazione standard)
```python
import numpy as np
from scipy.stats import norm
import random

# Generare campioni
rng = np.random.default_rng(seed=42)
campione = rng.normal(loc=50, scale=10, size=1000)  # μ=50, σ=10

# Proprietà della distribuzione
print(norm.pdf(50, loc=50, scale=10))   # densità in x=50 (picco)
print(norm.cdf(60, loc=50, scale=10))   # P(X ≤ 60) ≈ 0.84
print(norm.ppf(0.95, loc=50, scale=10)) # quantile 95° ≈ 66.4
```
**Regola empirica (68-95-99.7):**
- 68% dei valori cade in \[μ-σ, μ+σ\]
- 95% in \[μ-2σ, μ+2σ\]
- 99.7% in \[μ-3σ, μ+3σ\]
> Il modulo `random` stdlib offre `random.gauss(mu, sigma)` per generare singoli valori. Per campioni numerosi preferire `np.random.default_rng().normal()` — più efficiente e statisticamente più robusto.
---
## Distribuzione esponenziale
Descrive il tempo tra eventi in un processo di Poisson — es. tempo tra arrivi, durata di vita di componenti, intervalli tra richieste a un server.
**Parametro:** λ (tasso, rate). Media = 1/λ.
```python
from scipy.stats import expon

# λ = 1.5 → media attesa = 1/1.5 ≈ 0.67
campione_expo = rng.exponential(scale=1/1.5, size=1000)

# Con scipy
print(expon.mean(scale=1/1.5))          # media = 0.667
print(expon.cdf(1, scale=1/1.5))        # P(X ≤ 1)

# Con random stdlib (singolo valore)
print(random.expovariate(lambd=1.5))    # attenzione: parametro è λ, non scale
```
> **Attenzione all'interfaccia:** `random.expovariate(lambd)` vuole il rate λ, mentre `scipy.stats.expon(scale)` e `numpy.exponential(scale)` vogliono la scala (1/λ). È una delle incoerenze più comuni.
---
## Altre distribuzioni rilevanti
<table header-row="true">
<tr>
<td>Distribuzione</td>
<td>Uso tipico</td>
<td>scipy</td>
</tr>
<tr>
<td>**Uniforme**</td>
<td>Campionamento casuale equiprobabile</td>
<td>`uniform`</td>
</tr>
<tr>
<td>**Binomiale**</td>
<td>n prove Bernoulli, conta i successi</td>
<td>`binom`</td>
</tr>
<tr>
<td>**Poisson**</td>
<td>Numero di eventi in un intervallo</td>
<td>`poisson`</td>
</tr>
<tr>
<td>**Beta**</td>
<td>Probabilità, proporzioni (valori in \[0,1\])</td>
<td>`beta`</td>
</tr>
<tr>
<td>**Chi-quadro**</td>
<td>Test statistici, bontà di adattamento</td>
<td>`chi2`</td>
</tr>
<tr>
<td>**t di Student**</td>
<td>Inferenza su piccoli campioni</td>
<td>`t`</td>
</tr>
</table>
---
## Seed e riproducibilità
```python
import numpy as np
import random

# stdlib random
random.seed(42)
print(random.randint(1, 100))  # sempre 82

# NumPy — pattern moderno (da 1.17)
rng = np.random.default_rng(seed=42)  # Generator PCG64
sample = rng.normal(50, 10, size=100)

# ❌ Vecchio stile — deprecato, non thread-safe
np.random.seed(42)
```
> `np.random.default_rng()` usa il generatore PCG64, statisticamente superiore al vecchio Mersenne Twister e thread-safe. Da preferire sempre in nuovo codice.
---
## Riferimenti
- [SciPy — distribuzioni continue](https://docs.scipy.org/doc/scipy/reference/stats.html#continuous-distributions)
- [SciPy — distribuzioni discrete](https://docs.scipy.org/doc/scipy/reference/stats.html#discrete-distributions)
- [NumPy — Random Generator](https://numpy.org/doc/stable/reference/random/generator.html)
- [Python — random](https://docs.python.org/3/library/random.html)
