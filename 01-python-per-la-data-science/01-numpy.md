# 01 - NumPy

> Fonte Notion: https://app.notion.com/p/32f12abc808d817cac79c86db12dc12b — ultima modifica 2026-04-13T21:38:26.823Z

> 💡 NumPy è il fondamento di tutto l'ecosistema ML/AI in Python. I tensori di PyTorch e TensorFlow sono array NumPy potenziati. Capire NumPy significa capire come i dati fluiscono dentro un modello.
---
## L'ecosistema: stdlib → NumPy → SciPy
Python per la data science non è una libreria monolitica — è uno stack a strati, dove ogni livello aggiunge capacità che il precedente non ha.
<table header-row="true">
<tr>
<td>**Livello**</td>
<td>**Libreria**</td>
<td>**Cosa fa**</td>
<td>**Quando usarla**</td>
</tr>
<tr>
<td>Stdlib</td>
<td>`statistics`, `math`</td>
<td>Calcoli su liste Python native</td>
<td>Dati piccoli, nessuna dipendenza esterna</td>
</tr>
<tr>
<td>Array layer</td>
<td>`numpy`</td>
<td>Array contigui in memoria, operazioni vettorizzate in C</td>
<td>Qualsiasi elaborazione numerica su dati reali</td>
</tr>
<tr>
<td>Scientific layer</td>
<td>`scipy`</td>
<td>Algoritmi statistici, ottimizzazione, algebra lineare</td>
<td>Quando NumPy non ha la funzione che ti serve</td>
</tr>
</table>
La relazione è gerarchica: **SciPy dipende da NumPy**, che lavora su array costruibili da liste Python. Tutte le funzioni SciPy accettano `ndarray` e restituiscono `ndarray`.
```python
import statistics
import numpy as np
from scipy.stats import trim_mean

data = [1, 2, 3, 4, 5, 100]  # outlier a 100

statistics.mean(data)                    # 19.17 — stdlib
np.mean(data)                            # 19.17 — NumPy, vettorizzata
trim_mean(data, proportiontocut=0.1)     # 3.0   — SciPy, algoritmo avanzato
```
> In pratica: parti sempre da NumPy. Aggiungi SciPy solo quando hai bisogno di qualcosa che NumPy non ha.
---
## Perché i loop Python sono lenti
Python è un linguaggio a tipizzazione dinamica. Ogni variabile è un oggetto "boxed" sull'heap con metadati annessi. Un semplice `x + y` è in realtà una sequenza di operazioni:
1. **Lookup di ****`x`**** nel namespace** — il namespace è il dizionario delle variabili attive nel tuo scope. Python cerca la chiave `"x"` e recupera il riferimento all'oggetto heap.
2. **Lookup di ****`y`** — stessa cosa.
3. **Dispatch dinamico** — Python non sa a compile time che `x` è un intero. Lo scopre a runtime guardando `type(x)`, poi cerca `int.__add__` nella classe. Questo è il dispatch dinamico: la funzione viene decisa a runtime in base al tipo, non a compile time.
4. **Allocazione di un nuovo oggetto** — il risultato `49` non esiste in memoria. Python alloca un nuovo `PyObject` sull'heap con `type=int`, `value=49`, `refcount=1`.
5. **Reference counting** — Python aggiorna i contatori di riferimento per il garbage collector.
Su un singolo `x + y` è trascurabile. Su 10\^6 elementi in un loop, si moltiplica un milione di volte.
---
## Come NumPy bypassa tutto questo
NumPy aggira il problema operando su **array contigui in memoria** con **dtype omogeneo e fisso**. Le operazioni vengono eseguite da routine C che operano direttamente sul buffer di byte, senza mai toccare l'interprete Python per ogni elemento.
Il **dtype** è il tipo degli elementi dell'array, fisso per tutti — niente boxing, niente reference counting per ogni elemento. Python fa solo da controller, il lavoro viene delegato a C.
> Il punto chiave: con NumPy **scrivi Python, ma esegui C**. Il guadagno tipico è **10x–100x** su operazioni numeriche.
---
## Come NumPy sa quanti byte allocare
Quando crei un array, NumPy guarda i valori nella lista Python, inferisce il dtype migliore (es. `int64` = 8 byte per elemento) e alloca un buffer contiguo di esattamente `n × size` byte.
```python
a = np.array([1, 2, 3, 4, 5])  # dtype inferito: int64
# NumPy alloca: 5 × 8 = 40 byte contigui
# elemento all'indice i → indirizzo_base + i × 8
```
Il trucco è che **tutti gli elementi hanno lo stesso dtype**, quindi la formula per trovare l'elemento `i` è banale: `base + i × size`. Nessuna dereferenziazione, nessun lookup — accesso O(1) diretto.
Se i tipi fossero misti, NumPy risolve con l'**upcast automatico**: se metti insieme `int` e `float`, tutto viene convertito al tipo più capiente.
```python
np.array([1, 2.5, 3])                   # dtype: float64 — int promosso a float
np.array([1, 2, 3])                     # dtype: int64
np.array([1, 2, 3], dtype=np.float32)  # dtype esplicito: 4 byte/elem
```
---
## ndarray — il tipo fondamentale
```python
import numpy as np

# Creazione
a = np.array([1, 2, 3, 4, 5])          # da lista Python
b = np.arange(0, 10, 2)                # [0, 2, 4, 6, 8]
c = np.linspace(0, 1, 5)               # [0.0, 0.25, 0.5, 0.75, 1.0]
d = np.zeros((3, 4))                   # matrice 3x4 di zeri
e = np.ones((2, 3), dtype=np.float32)  # dtype esplicito
```
Ogni `ndarray` ha tre attributi fondamentali — la sua "carta d'identità":
```python
print(a.shape)   # (5,)    — dimensioni: 1D vector
print(d.shape)   # (3, 4)  — 3 righe, 4 colonne
print(a.dtype)   # int64   — tipo di ogni elemento
print(a.ndim)    # 1       — numero di dimensioni
print(d.size)    # 12      — elementi totali
print(d.nbytes)  # byte occupati in memoria = size × bytes_per_element
```
A differenza delle liste Python, un `ndarray` può contenere **un solo tipo**. Se mescoli tipi, NumPy fa upcast automatico al tipo più generale (`int + float → float64`, `numeri + stringhe → stringhe`).
---
## dtype e memoria — astype()
I dtype più comuni in data science:
<table header-row="true">
<tr>
<td>**dtype**</td>
<td>**Dimensione**</td>
<td>**Uso tipico**</td>
</tr>
<tr>
<td>`float64`</td>
<td>8 byte</td>
<td>Default per decimali, massima precisione</td>
</tr>
<tr>
<td>`float32`</td>
<td>4 byte</td>
<td>ML/AI — stessa precisione pratica, metà memoria</td>
</tr>
<tr>
<td>`int64`</td>
<td>8 byte</td>
<td>Interi grandi</td>
</tr>
<tr>
<td>`int32`</td>
<td>4 byte</td>
<td>Interi medi</td>
</tr>
<tr>
<td>`bool`</td>
<td>1 byte</td>
<td>Maschere booleane</td>
</tr>
<tr>
<td>`U10`, `U50`</td>
<td>variabile</td>
<td>Stringhe a lunghezza fissa</td>
</tr>
</table>
`astype()` converte un array a un dtype diverso. Uso tipico: passare da `float64` a `float32` per ridurre la memoria usata dai modelli ML:
```python
X = np.column_stack([weights, reps, volumes])  # float64, 8 byte/elem
X_f32 = X.astype(np.float32)                   # float32, 4 byte/elem — metà memoria
```
> In ML si usa quasi sempre `float32` invece di `float64`. La perdita di precisione è trascurabile per l'addestramento, ma si risparmia il 50% di memoria — rilevante quando i modelli hanno milioni di parametri.
---
## Operazioni vettorizzate
```python
arr = np.array([1, 2, 3, 4, 5])

# Operazioni element-wise — nessun loop
print(arr * 2)       # [2, 4, 6, 8, 10]
print(arr + 10)      # [11, 12, 13, 14, 15]
print(arr ** 2)      # [1, 4, 9, 16, 25]
print(np.sqrt(arr))  # radice quadrata element-wise

# Tra due array (stessa lunghezza)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)         # [5, 7, 9]
print(a * b)         # [4, 10, 18]  — prodotto element-wise, NON scalare
print(np.dot(a, b))  # 32           — prodotto scalare
```
Qualsiasi operazione tra due `ndarray` (`+`, `*`, `/`, `**`) viene automaticamente dispatched a codice C compilato. Non serve scrivere loop — NumPy li esegue internamente per te, in C.
---
## column_stack e feature matrix
> 💡 In ML, i dati di input vengono sempre organizzati come una **feature matrix** — una tabella dove ogni riga è un campione e ogni colonna è una caratteristica (feature). La notazione standard è `X` (maiuscola), da `y = f(X)`.
`np.column_stack()` affianca array separati come colonne di una singola matrice:
```python
# Tre array separati
weights = np.array([80.0, 60.0, 70.0, ...])   # kg sollevati per set
reps    = np.array([10,    8,   12,   ...])    # ripetizioni per set
volumes = weights * reps                        # volume per set (element-wise)

# Costruzione della feature matrix
X = np.column_stack([weights, reps, volumes])
# X → | 80.0  10  800.0 |   ← set 1
#     | 60.0   8  480.0 |   ← set 2
#     | 70.0  12  840.0 |   ← set 3
#     | ...  ...  ...   |

print(X.shape)   # (3628, 3) — 3628 campioni, 3 feature
print("Colonne: [weight_kg, reps, volume]")
```
Requisiti: tutti gli array devono avere la **stessa lunghezza** e lo **stesso dtype** (o compatibile). Per dati misti (stringhe + numeri) si usa `pandas.DataFrame`.
---
## Axis — direzione di aggregazione
Quando fai un'operazione su una matrice 2D, devi specificare **lungo quale asse** aggregare:
```javascript
         weight  reps  volume
set 1  |  80     10    800  |  →  axis=1  → (aggrega per riga)
set 2  |  60      8    480  |  →
set 3  |  70     12    840  |  →
          ↓      ↓     ↓
        axis=0
  (aggrega per colonna)
```
- **`axis=0`** — "per ogni colonna, aggrega tutte le righe" → un risultato per feature
- **`axis=1`** — "per ogni riga, aggrega tutte le colonne" → un risultato per campione
```python
# axis=0: una statistica per feature (uso più comune)
X.mean(axis=0)   # [media_weight, media_reps, media_volume]
X.min(axis=0)    # [min per colonna]
X.max(axis=0)    # [max per colonna]

# axis=1: una statistica per campione
X.mean(axis=1)   # media delle 3 feature per ogni set
```
> NumPy supporta fino a 32 dimensioni: 1D = vettore, 2D = tabella, 3D = cubo (es. batch di immagini: `batch × altezza × larghezza`).
---
## Indexing e boolean indexing
**Indexing standard 2D:**
```python
mat = np.arange(12).reshape(3, 4)

print(mat[1, :])     # seconda riga — tutti i valori
print(mat[:, 2])     # terza colonna — tutti i valori
print(mat[0:2, 1:3]) # sottomatrice righe 0-1, colonne 1-2
```
**Boolean indexing — il filtro fondamentale di NumPy:**
```python
# Step 1: crea una maschera booleana
bench_mask = exercise_names == "Barbell Bench Press"
# → [True, False, False, True, False, ...]  (stesso shape di exercise_names)

# Step 2: usa la maschera per filtrare
bench_weights = weights[bench_mask]
# NumPy sovrappone maschera e array posizione per posizione:
# True → tieni, False → scarta
```
In Python puro `lista == "valore"` non funziona così — servirebbe un loop. NumPy sovraccrica `==` per confrontare ogni elemento automaticamente, in C.
```python
# Combinare condizioni
heavy_bench = weights[(exercise_names == "Barbell Bench Press") & (weights > 100)]
# & → AND element-wise (non 'and' Python, che non funziona su array)
# | → OR element-wise

# Contare i True
bench_mask.sum()   # True=1, False=0 → conta i set di panca
```
> **Attenzione:** lo slicing NumPy restituisce una **view**, non una copia. Modificare la slice modifica l'array originale. Usare `.copy()` se serve un array indipendente.
---
## Statistiche descrittive
```python
col = X[:, 0]  # estrai la prima colonna (weights)

col.mean()     # media — "qual è il valore tipico?"
col.std()      # deviazione standard — "quanto variano i valori?"
col.min()      # minimo
col.max()      # massimo
col.sum()      # somma totale
```
**`argmax()`**** e ****`argmin()`** restituiscono l'**indice** del massimo/minimo, non il valore:
```python
vol_array = np.array([4500, 3200, 5100, 2800])
vol_array.argmax()   # → 2  (posizione di 5100)
vol_array.argmin()   # → 3  (posizione di 2800)

# Utile per trovare il campione corrispondente
weeks[vol_array.argmax()]   # settimana con volume massimo
exercise_names[intensity_scores.argmax()]  # esercizio più intenso
```
---
## Broadcasting
> 💡 Broadcasting è il meccanismo che permette operazioni tra array di forme diverse **senza copiare dati**. È la base della normalizzazione in ML.
NumPy "allunga" automaticamente l'array più piccolo per adattarlo a quello più grande:
```python
a = np.array([[1, 2, 3],
              [4, 5, 6]])    # shape (2, 3)
b = np.array([10, 20, 30])  # shape (3,)

print(a + b)
# b viene applicato a OGNI riga di a:
# [[11, 22, 33],
#  [14, 25, 36]]
```
**Regole di broadcasting** (applicate da destra a sinistra):
1. Se le forme hanno lunghezze diverse, quella più corta viene padded con 1 a sinistra
2. Dimensioni di size 1 vengono espanse per corrispondere all'altra
3. Se nessuna dimensione è 1 e le size non coincidono → `ValueError`
---
## Normalizzazione — Min-Max e Z-score
> 💡 Prima di addestrare un modello ML, le feature vanno normalizzate. Senza normalizzazione, feature con scale diverse (es. `volume` 0–4000 vs `reps` 1–30) renderebbero il modello instabile o distorto.
**Min-Max scaling** — scala ogni valore in `[0, 1]`:
```python
# formula: z = (x - min) / (max - min)
X_min = X.min(axis=0)   # min per ogni colonna, shape (3,)
X_max = X.max(axis=0)   # max per ogni colonna, shape (3,)

X_norm = (X - X_min) / (X_max - X_min)
# Broadcasting: X_min e X_max (shape 3,) vengono applicati a ogni riga di X (shape 3628, 3)

# Verifica
X_norm.min(axis=0)   # → [0, 0, 0]
X_norm.max(axis=0)   # → [1, 1, 1]
```
Interpretazione: un peso di 70kg su un range \[0, 140\] → valore normalizzato 0.5.
**Z-score standardization** — scala rispetto alla media e alla deviazione standard:
```python
# formula: z = (x - mean) / std
X_mean = X.mean(axis=0)
X_std  = X.std(axis=0)

X_scaled = (X - X_mean) / X_std

# Verifica: dopo z-score, ogni colonna ha media ≈ 0 e std ≈ 1
X_scaled.mean(axis=0).round(6)   # → [0, 0, 0]
X_scaled.std(axis=0).round(6)    # → [1, 1, 1]
```
Interpretazione: `z = +1.0` significa "1 deviazione standard sopra la media"; `z = -2.0` significa "2 std sotto la media".
**Quando usare quale:**
- **Min-Max** → quando vuoi un range preciso \[0,1\], non ci sono outlier forti
- **Z-score** → quando la distribuzione è approssimativamente normale, standard in ML
---
## Prodotto matriciale `@` — il cuore delle reti neurali
> 💡 L'operatore `@` esegue il prodotto matriciale. È l'operazione fondamentale di un neurone artificiale: `output = X @ W + b`. Capire `@` significa capire cosa succede dentro una rete neurale.
```python
# Vettore di pesi (importanza di ogni feature)
W = np.array([0.5, 0.3, 0.2])  # [weight_kg, reps, volume]

# Prodotto matrice × vettore: per ogni riga di X_norm, moltiplica
# element-wise per W e somma tutto → uno score per set
# (3628, 3) @ (3,) → (3628,)
intensity_scores = X_norm @ W
```
Cosa fa esattamente per ogni riga:
```javascript
row = [0.57, 0.33, 0.19]   (weight_norm, reps_norm, volume_norm)
score = 0.5*0.57 + 0.3*0.33 + 0.2*0.19
      = 0.285 + 0.099 + 0.038
      = 0.422
```
Questo è esattamente ciò che fa un neurone artificiale: riceve input normalizzati, li moltiplica per pesi appresi, somma tutto. L'unica differenza è che in un vero modello i pesi `W` vengono **appresi** tramite backpropagation — qui li abbiamo fissati a mano.
```python
top_idx = intensity_scores.argmax()
print(f"Set più intenso: {exercise_names[top_idx]}, "
      f"{weights[top_idx]}kg × {reps[top_idx]} reps")
```
> **Nota sulle dimensioni:** in `A @ B`, il numero di colonne di `A` deve coincidere con il numero di righe di `B`. `(3628, 3) @ (3,)` → OK perché 3 == 3. Mismatch → `ValueError`.
---
## Seed e riproducibilità
> 💡 In ML la riproducibilità è un requisito: stesso codice, stessi risultati. Il seed garantisce che sequenze "casuali" siano identiche ad ogni esecuzione — fondamentale per debug e confronto di modelli.
```python
rng = np.random.default_rng(seed=42)  # generatore moderno (preferire a np.random.seed)

# Campionamento senza rimpiazzo: 10 indici casuali da 0 a n-1
sample_idx = rng.choice(n, size=10, replace=False)
# → sempre gli stessi 10 indici con seed=42

# Usare gli indici per estrarre i campioni corrispondenti
sample_exercises = exercise_names[sample_idx]
sample_volumes   = volumes_arr_np[sample_idx]
```
**`default_rng`**** vs ****`np.random.seed`****:** il vecchio `np.random.seed(42)` è globale e può creare problemi in codice parallelo. `default_rng` crea un generatore locale, isolato — la pratica moderna raccomandata.
---
## Benchmark
```python
import timeit
import numpy as np

setup = "import numpy as np; a = list(range(10**6)); na = np.arange(10**6)"

t_list  = timeit.timeit("[x*2 for x in a]", setup=setup, number=10)
t_numpy = timeit.timeit("na * 2",           setup=setup, number=10)

print(f"List:    {t_list:.4f}s")
print(f"NumPy:   {t_numpy:.4f}s")
print(f"Speedup: {t_list/t_numpy:.0f}x")
```
> Usare `timeit` e non `time.time()` per i benchmark: `time.time()` misura il **wall clock** soggetto a interruzioni OS. `timeit` esegue più ripetizioni e isola il codice da overhead esterni.
---
## array.array vs numpy.array
<table header-row="true">
<tr>
<td>**Feature**</td>
<td>**`array.array`**</td>
<td>**`numpy.array`**</td>
</tr>
<tr>
<td>Tipi supportati</td>
<td>Solo primitivi C</td>
<td>int, float, complex, bool...</td>
</tr>
<tr>
<td>Multidimensionale</td>
<td>No (1D only)</td>
<td>Sì (1D, 2D, 3D, ...)</td>
</tr>
<tr>
<td>Operazioni matematiche</td>
<td>No</td>
<td>Sì (vettorizzate)</td>
</tr>
<tr>
<td>Performance su grandi dataset</td>
<td>Lento (loop Python)</td>
<td>Molto più veloce</td>
</tr>
<tr>
<td>Richiede installazione</td>
<td>No (stdlib)</td>
<td>Sì (`pip install numpy`)</td>
</tr>
</table>
`array.array` è utile solo quando non puoi installare NumPy (ambiente ristretto, embedded). In qualsiasi contesto data science si usa sempre `numpy`.
---
## Riferimenti
- [NumPy — Quickstart](https://numpy.org/doc/stable/user/quickstart.html)
- [NumPy — Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)
- [NumPy — Indexing](https://numpy.org/doc/stable/user/basics.indexing.html)
- [NumPy — Linear algebra](https://numpy.org/doc/stable/reference/routines.linalg.html)
- [NumPy — Random Generator](https://numpy.org/doc/stable/reference/random/generator.html)
