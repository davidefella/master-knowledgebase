# 07 - Pandas e correlazione

> Fonte Notion: https://app.notion.com/p/33612abc808d81bcb634f39abf23b488 — ultima modifica 2026-04-02T14:43:46.029Z

La correlazione misura la relazione lineare tra due variabili numeriche. Va da -1 (relazione inversa perfetta) a +1 (relazione diretta perfetta). 0 indica assenza di relazione lineare.
---
## Matrice di correlazione con pandas
Data un DataFrame, `df.corr()` calcola la correlazione tra tutte le coppie di colonne numeriche.
```python
import pandas as pd

# Esempio con dati manuali
technologies = {
    'b_len': [1.0, -0.235053, 0.656181, 0.595110],
    'b_dep': [-0.235053, 1.0, -0.583851, -0.471916],
    'f_len': [0.656181, -0.583851, 1.0, 0.871202],
    'f_dep': [0.595110, -0.471916, 0.871202, 1.0]
}
df = pd.DataFrame(technologies)
matrix = df.corr()
print(matrix)
```
> **La matrice di correlazione è essa stessa un DataFrame.** Questo significa che puoi applicare tutti i metodi pandas normali: `.round()`, `.unstack()`, filtering, ecc.
```python
# Arrotondare per leggibilità
matrix = df.corr().round(2)
```
---
## Dataset reale — pinguini (Seaborn)
Seaborn include dataset di esempio pronti all'uso. Il dataset `penguins` contiene misurazioni fisiche di 344 pinguini di tre specie.
```python
import pandas as pd
import seaborn as sns

df = sns.load_dataset('penguins')

# Rinominare le colonne per comodità
df.columns = ['species', 'island', 'b_len', 'b_dep', 'f_len', 'f_dep', 'sex']
print(df.head())
#   species     island  b_len  b_dep  f_len   f_dep     sex
# 0  Adelie  Torgersen   39.1   18.7  181.0  3750.0    Male
# 1  Adelie  Torgersen   39.5   17.4  186.0  3800.0  Female
# 3  Adelie  Torgersen    NaN    NaN    NaN     NaN     NaN  # valori mancanti

matrix = df.corr().round(2)
print(matrix)
#        b_len  b_dep  f_len  f_dep
# b_len   1.00  -0.24   0.66   0.60
# b_dep  -0.24   1.00  -0.58  -0.47
# f_len   0.66  -0.58   1.00   0.87
# f_dep   0.60  -0.47   0.87   1.00
```
---
## Visualizzazione — heatmap con Seaborn
Una heatmap rappresenta la matrice di correlazione con colori: più il colore è intenso, più forte è la correlazione.
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Heatmap base
sns.heatmap(matrix, annot=True)
plt.show()
```
> **Problema della heatmap base:** se non si specificano i limiti, la colormap viene inferita dai dati. Se le correlazioni negative non scendono sotto -0.5, i colori possono far sembrare le relazioni negative meno forti di quanto siano.
### Heatmap corretta — con parametri espliciti
```python
sns.heatmap(
    matrix,
    annot=True,     # mostra i valori nelle celle
    vmax=1,         # ancora il massimo a +1
    vmin=-1,        # ancora il minimo a -1
    center=0,       # i colori divergono da 0
    cmap='vlag'     # palette che va da blu (negativo) a rosso (positivo)
)
plt.show()

# Salvare il grafico su file
plt.savefig('heatmap.png')
```
<table header-row="true">
<tr>
<td>Parametro</td>
<td>Effetto</td>
</tr>
<tr>
<td>`annot=True`</td>
<td>Mostra i valori numerici in ogni cella</td>
</tr>
<tr>
<td>`vmin`, `vmax`</td>
<td>Ancora la colormap a -1 e +1</td>
</tr>
<tr>
<td>`center=0`</td>
<td>I colori divergono simmetricamente da 0</td>
</tr>
<tr>
<td>`cmap='vlag'`</td>
<td>Palette divergente blu-rosso</td>
</tr>
</table>
---
## Filtrare correlazioni forti
Una correlazione si considera forte quando il suo valore assoluto è ≥ 0.7.
```python
matrix = df.corr()
matrix_unstacked = matrix.unstack()    # trasforma la matrice in Serie con indice multiplo
forti = matrix_unstacked[abs(matrix_unstacked) >= 0.7]
print(forti)
# flipper_length_mm  body_mass_g    0.871202
# body_mass_g        flipper_length_mm  0.871202
# (più le auto-correlazioni = 1.0)
```
> **`unstack()`** trasforma le righe della matrice in un secondo livello di indice, producendo una Serie con coppie `(colonna1, colonna2)` come indice. Questo permette di filtrare le coppie direttamente.
---
## Interpretazione
<table header-row="true">
<tr>
<td>Valore assoluto</td>
<td>Interpretazione</td>
</tr>
<tr>
<td>1.0</td>
<td>Correlazione perfetta (o auto-correlazione)</td>
</tr>
<tr>
<td>0.7 – 1.0</td>
<td>Correlazione forte</td>
</tr>
<tr>
<td>0.4 – 0.7</td>
<td>Correlazione moderata</td>
</tr>
<tr>
<td>0.0 – 0.4</td>
<td>Correlazione debole o assente</td>
</tr>
<tr>
<td>Negativo</td>
<td>Relazione inversa (uno sale, l'altro scende)</td>
</tr>
</table>
> **Attenzione:** correlazione ≠ causalità. Due variabili possono essere correlate senza che una causi l’altra. La correlazione è uno strumento esplorativo, non una prova di relazione causale.
---
## Riferimenti
- [pandas — DataFrame.corr](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html)
- [Seaborn — heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html)
- [Seaborn — load_dataset](https://seaborn.pydata.org/generated/seaborn.load_dataset.html)
