# 05 - Dataset

> Fonte Notion: https://app.notion.com/p/33212abc808d8117975fe5a13c026e3c — ultima modifica 2026-04-02T14:43:12.946Z

Un dataset è una collezione di dati organizzata in modo strutturato. È il punto di partenza di qualsiasi analisi o modello.
---
## Struttura
Un dataset tabellare è organizzato in:
- **Righe** = osservazioni (record, esempi)
- **Colonne** = feature (attributi, variabili)
Esempio:
<table header-row="true">
<tr>
<td>ID</td>
<td>Nome</td>
<td>Età</td>
<td>Altezza (cm)</td>
<td>Città</td>
</tr>
<tr>
<td>1</td>
<td>Alice</td>
<td>25</td>
<td>165</td>
<td>New York</td>
</tr>
<tr>
<td>2</td>
<td>Bob</td>
<td>30</td>
<td>175</td>
<td>London</td>
</tr>
<tr>
<td>3</td>
<td>Charlie</td>
<td>22</td>
<td>180</td>
<td>Paris</td>
</tr>
</table>
---
## Tipi di dataset
**Strutturato (tabellare)**
Organizzato in righe e colonne. Facile da interrogare con SQL o pandas.
Esempi: dati di vendita, record medici, prezzi azionari.
**Non strutturato**
Nessun formato fisso. Richiede preprocessing specifico (NLP, computer vision).
Esempi: post social, email, immagini, audio.
**Semi-strutturato**
Contiene sia elementi strutturati che liberi.
Esempi: JSON, XML, HTML.
---
## Dove trovare dataset
<table header-row="true">
<tr>
<td>Fonte</td>
<td>URL</td>
<td>Note</td>
</tr>
<tr>
<td>Kaggle</td>
<td>[https://www.kaggle.com](https://www.kaggle.com)</td>
<td>Il più usato in data science, molti dataset pronti</td>
</tr>
<tr>
<td>Google Dataset Search</td>
<td>[https://datasetsearch.research.google.com](https://datasetsearch.research.google.com)</td>
<td>Motore di ricerca di dataset</td>
</tr>
<tr>
<td>UCI ML Repository</td>
<td>[https://archive.ics.uci.edu](https://archive.ics.uci.edu)</td>
<td>Classici dell'ML accademico</td>
</tr>
<tr>
<td>OpenML</td>
<td>[https://www.openml.org](https://www.openml.org)</td>
<td>Integrato con scikit-learn</td>
</tr>
</table>
---
## DataFrame pandas
Un DataFrame è una struttura dati **bidimensionale** con righe e colonne etichettate. Puoi pensarci come a una tabella SQL o a un foglio Excel — ma con tutta la potenza di Python.
```javascript
Colonne
  ↓       ↓
+--------+--------+--------+
| Regd.  | Name   | Marks% |  ← riga
+--------+--------+--------+
| 1000   | Steve  | 86.29  |
| 1001   | Mathew | 91.63  |
+--------+--------+--------+
```
### Costruttore
```python
pandas.DataFrame(data, index, columns, dtype, copy)
```
<table header-row="true">
<tr>
<td>Parametro</td>
<td>Descrizione</td>
</tr>
<tr>
<td>`data`</td>
<td>Dati in input: lista, dict, ndarray, Series, altro DataFrame</td>
</tr>
<tr>
<td>`index`</td>
<td>Etichette delle righe (default: 0, 1, 2...)</td>
</tr>
<tr>
<td>`columns`</td>
<td>Etichette delle colonne</td>
</tr>
<tr>
<td>`dtype`</td>
<td>Tipo dati (attenzione: in pandas 1.3+ si usa `.astype()` per colonna)</td>
</tr>
<tr>
<td>`copy`</td>
<td>Se copiare i dati (default: False)</td>
</tr>
</table>
### Creazione da lista
```python
import pandas as pd

# Lista semplice — una colonna
df = pd.DataFrame([1, 2, 3, 4, 5])

# Lista di liste con colonne
df = pd.DataFrame(
    [['Alex', 10], ['Bob', 12], ['Clarke', 13]],
    columns=['Name', 'Age']
)
print(df)
#      Name  Age
# 0    Alex   10
# 1     Bob   12
# 2  Clarke   13

# Conversione di tipo per colonna (modo corretto)
df['Age'] = df['Age'].astype(float)
```
> **Attenzione:** passare `dtype=float` a `pd.DataFrame()` con colonne miste (str + int) genera `ValueError` perché non può convertire le stringhe. Il modo corretto è convertire colonna per colonna con `.astype()`.
### Creazione da dizionario
```python
data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28, 34, 29, 42]}
df = pd.DataFrame(data)

# Con indice personalizzato
df = pd.DataFrame(data, index=['rank1', 'rank2', 'rank3', 'rank4'])
print(df)
#        Name  Age
# rank1   Tom   28
# rank2  Jack   34
```
### Selezione, aggiunta e rimozione di colonne
```python
import pandas as pd

d = {
    'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
}
df = pd.DataFrame(d)
# Quando le Series hanno lunghezze diverse, pandas allinea per indice
# e inserisce NaN dove mancano valori
#      one  two
# a    1.0    1
# b    2.0    2
# c    3.0    3
# d    NaN    4

# Selezione colonna
print(df['one'])   # Series con valori di 'one'

# Aggiunta colonna
df['three'] = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
df['four'] = df['one'] + df['three']   # operazione tra colonne

# Rimozione colonna
del df['one']       # rimuove in-place
df.pop('two')       # rimuove e restituisce la colonna rimossa
```
> **NaN (Not a Number):** quando pandas allinea Series con indici diversi, i valori mancanti vengono riempiti con `NaN`. È il modo di pandas per rappresentare dati assenti — equivalente a `NULL` in SQL.
---
## Caricamento con pandas
```python
import pandas as pd

# Da CSV locale
df = pd.read_csv('data.csv')

# Da URL
url = 'https://raw.githubusercontent.com/.../insurance.csv'
df = pd.read_csv(url)

# Ispezione rapida
print(df.shape)        # (righe, colonne)
print(df.dtypes)       # tipo di ogni colonna
print(df.head())       # prime 5 righe
print(df.describe())   # statistiche descrittive
print(df.isnull().sum())  # valori mancanti per colonna
```
---
## Preprocessing base
**Variabili categoriche → numeriche (one-hot encoding)**
```python
# 'sex': male/female, 'smoker': yes/no, 'region': northeast/...
data = pd.get_dummies(data, drop_first=True)
# drop_first=True evita la trappola della multicollinearità
```
**Split train/test**
```python
from sklearn.model_selection import train_test_split

X = data.drop('target', axis=1)
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# 80% training, 20% test — random_state per riproducibilità
```
---
## Riferimenti
- [pandas — read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
- [scikit-learn — train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
- [Kaggle](https://www.kaggle.com)
