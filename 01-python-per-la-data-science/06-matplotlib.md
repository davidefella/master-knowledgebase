# 06 - Matplotlib

> Fonte Notion: https://app.notion.com/p/33212abc808d8168a61ef67bfd934a27 — ultima modifica 2026-03-29T23:54:07.424Z

Matplotlib è la libreria di visualizzazione base di Python. È il punto di partenza per qualsiasi grafico nel mondo data science prima di passare a strumenti più avanzati come seaborn o plotly.
---
## Importazione
```python
import matplotlib.pyplot as plt
import numpy as np
```
> La convenzione `import matplotlib.pyplot as plt` è universale — troverai questo alias in qualsiasi codice.
---
## Primo contatto — distribuzione empirica
Esempio dal corso: generare 1000 valori casuali e visualizzarne la distribuzione.
```python
import random
import matplotlib.pyplot as plt

N = 1000
valori = [random.randint(0, N) for _ in range(N)]

my_min = min(valori)
my_max = max(valori)
print(f"min={my_min}  max={my_max}  range={my_max - my_min}")

# Istogramma — distribuzione dei valori
plt.hist(valori)
plt.show()

# Grafico a linea — indice vs valore
plt.plot(range(N), valori)
plt.show()
```
> **Cosa mostra l'istogramma:** divide il range dei valori in bin e conta quante osservazioni cadono in ciascuno. Con dati uniformi i bin hanno altezze simili — se la distribuzione fosse normale vedremmo una campana.
---
## Grafici principali
### Scatter plot
```python
x = np.array([1000, 1500, 2000, 2500, 3000])
y = np.array([150000, 180000, 210000, 250000, 280000])

plt.scatter(x, y, color='blue', alpha=0.5, label='Dati reali')
plt.xlabel('Superficie (mq)')
plt.ylabel('Prezzo ($)')
plt.title('Prezzo vs Superficie')
plt.legend()
plt.show()
```
### Line plot
```python
plt.plot(x, y, color='red', linewidth=2, label='Linea di regressione')
plt.legend()
plt.show()
```
### Histogram
```python
dati = np.random.normal(50, 10, size=1000)
plt.hist(dati, bins=30, color='steelblue', edgecolor='white')
plt.xlabel('Valore')
plt.ylabel('Frequenza')
plt.title('Distribuzione normale')
plt.show()
```
### Scatter + regressione insieme
```python
plt.scatter(x, y, color='blue', alpha=0.5, label='Dati reali')
plt.plot(x, predicted_y, color='red', linewidth=2, label='Regressione')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Titolo')
plt.legend()
plt.show()
```
---
## Parametri comuni
<table header-row="true">
<tr>
<td>Parametro</td>
<td>Valori esempio</td>
<td>Effetto</td>
</tr>
<tr>
<td>`color`</td>
<td>`'blue'`, `'red'`, `'#378ADD'`</td>
<td>Colore</td>
</tr>
<tr>
<td>`alpha`</td>
<td>`0.0` – `1.0`</td>
<td>Trasparenza</td>
</tr>
<tr>
<td>`linewidth`</td>
<td>`1`, `2`, `3`</td>
<td>Spessore linea</td>
</tr>
<tr>
<td>`linestyle`</td>
<td>`'-'`, `'--'`, `':'`</td>
<td>Stile linea</td>
</tr>
<tr>
<td>`label`</td>
<td>stringa</td>
<td>Etichetta per la legenda</td>
</tr>
<tr>
<td>`bins`</td>
<td>intero</td>
<td>Numero di bin (istogramma)</td>
</tr>
<tr>
<td>`marker`</td>
<td>`'o'`, `'x'`, `'s'`</td>
<td>Forma dei punti</td>
</tr>
</table>
---
## Note critiche sul materiale del corso
Il corso usa `plt.show()` dopo ogni grafico separatamente. In Jupyter Notebook questo funziona, ma è buona pratica usare `plt.figure()` per creare figure separate esplicitamente quando si vogliono più grafici distinti:
```python
# Pattern corretto per più grafici
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].hist(dati, bins=30)
axes[0].set_title('Istogramma')
axes[1].scatter(x, y)
axes[1].set_title('Scatter')
plt.tight_layout()
plt.show()
```
---
## Riferimenti
- [Matplotlib — documentazione](https://matplotlib.org/stable/)
- [Matplotlib — gallery](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn](https://seaborn.pydata.org) — wrapper di alto livello su matplotlib, più usato in data science
