# 11 - EDA sistematica

> Fonte Notion: https://app.notion.com/p/33a12abc808d814b8607f1b3baaa0c2d — ultima modifica 2026-04-07T00:18:07.415Z

Il dataset usato in questo modulo è **Customer Personality Analysis** di Kaggle: [https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)
È un dataset reale con 2240 clienti e 29 colonne (dati demografici, acquisti, campagne marketing). Scaricarlo richiede un account Kaggle gratuito; il file si chiama `marketing_campaign.csv` con separatore tab (`\t`).
---
## Cos'è l'EDA e perché farla
L'**Exploratory Data Analysis** (EDA) è la fase di esplorazione del dataset *prima* di costruire qualsiasi modello. L'obiettivo non è ancora predire nulla — è capire cosa c'è nei dati, che forma hanno, dove ci sono problemi e quali relazioni emergono.
In pratica si fa sempre EDA per:
- capire la struttura del dataset (quante righe, quante colonne, che tipi)
- individuare valori mancanti, duplicati, outlier
- esplorare le distribuzioni delle singole variabili
- scoprire relazioni tra coppie o gruppi di variabili
- formulare ipotesi prima della modellazione
Una buona EDA riduce le sorprese in fase di training e spesso rivela problemi nel dato che avrebbero silenziosamente corrotto il modello.
### Struttura tipica di un'analisi EDA
1. Caricamento librerie e dati
2. Ispezione iniziale (shape, dtypes, head)
3. Lettura della documentazione/dizionario dati
4. **Analisi univariata** — una variabile alla volta
5. **Analisi bivariata** — relazioni tra coppie di variabili
6. **Analisi multivariata** — struttura di insieme
7. Insight e passi successivi
---
## Setup iniziale
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caricamento del dataset (separatore tab)
data = pd.read_csv('data/marketing_campaign.csv', sep='\t')
print(data.shape)  # (2240, 29)
data.head()
```
> **Perché ****`sep='\t'`****?** Pandas usa la virgola come separatore di default. Questo file usa il tab — abbastanza comune nei dataset di origine accademica o da sistemi Windows. Senza specificarlo, tutto il contenuto finirebbe in una sola colonna.
### Piccola utility: conversione hex → RGB
Nel notebook della docente compare questo snippet per definire un colore personalizzato per i grafici:
```python
color = '#4e6c50'
rgb_color = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
# → (78, 108, 80)
```
Cosa fa passo per passo:
1. `lstrip('#')` rimuove il `#` iniziale → `'4e6c50'`
2. `[i:i+2] for i in (0, 2, 4)` estrae tre coppie: `'4e'`, `'6c'`, `'50'`
3. `int(..., 16)` converte ogni coppia da esadecimale a intero
4. `tuple(...)` assembla il risultato
Matplotlib però accetta colori RGB nel range 0–1, non 0–255. Per usarlo:
```python
normalized_rgb = tuple(c / 255 for c in rgb_color)
# → (0.306, 0.424, 0.314)
```
---
## Dizionario dati
Prima di guardare i numeri, è fondamentale capire cosa rappresenta ogni colonna. Qui sotto il dizionario completo del dataset.
**Persone**
<table header-row="true">
<tr>
<td>Colonna</td>
<td>Significato</td>
</tr>
<tr>
<td>`ID`</td>
<td>Identificatore univoco del cliente</td>
</tr>
<tr>
<td>`Year_Birth`</td>
<td>Anno di nascita</td>
</tr>
<tr>
<td>`Education`</td>
<td>Livello di istruzione</td>
</tr>
<tr>
<td>`Marital_Status`</td>
<td>Stato civile</td>
</tr>
<tr>
<td>`Income`</td>
<td>Reddito annuo familiare (float, con 24 NA)</td>
</tr>
<tr>
<td>`Kidhome`</td>
<td>N° bambini piccoli in casa</td>
</tr>
<tr>
<td>`Teenhome`</td>
<td>N° adolescenti in casa</td>
</tr>
<tr>
<td>`Dt_Customer`</td>
<td>Data di iscrizione al programma</td>
</tr>
<tr>
<td>`Recency`</td>
<td>Giorni dall'ultimo acquisto</td>
</tr>
<tr>
<td>`Complain`</td>
<td>1 se ha reclamato negli ultimi 2 anni</td>
</tr>
</table>
**Prodotti** (spesa negli ultimi 2 anni)
`MntWines`, `MntFruits`, `MntMeatProducts`, `MntFishProducts`, `MntSweetProducts`, `MntGoldProds`
**Promozioni**
`NumDealsPurchases`, `AcceptedCmp1`–`AcceptedCmp5`, `Response` (ultima campagna)
**Canali d'acquisto**
`NumWebPurchases`, `NumCatalogPurchases`, `NumStorePurchases`, `NumWebVisitsMonth`
> **Nota:** Il dataset contiene anche `Z_CostContact` (sempre 3) e `Z_Revenue` (sempre 11). Sono costanti e quindi inutili per l'analisi esplorativa — ma potrebbero servire in un task di classificazione per costruire una funzione di costo basata su falsi positivi/negativi.
---
## Analisi univariata
L'analisi univariata esamina ogni variabile *individualmente*: distribuzione, valori mancanti, outlier, tipo. È il punto di partenza obbligatorio.
### Tipi di dato
```python
data.dtypes
```
Alcune osservazioni critiche:
- `Dt_Customer` è letto come `object` (stringa) — va convertito in `datetime`
- `Education` e `Marital_Status` potrebbero essere `category` invece di `object` (più efficiente in memoria)
- `Income` è `float64` con valori mancanti — in produzione si convertirebbe in `int64` dopo imputazione
```python
# Conversione della data — formato giorno-mese-anno
data['Dt_Customer'] = pd.to_datetime(data['Dt_Customer'], format='%d-%m-%Y')
```
### Duplicati
```python
data.duplicated(subset=['ID']).sum()  # → 0
```
Nessun duplicato. Basta controllare la colonna chiave (`ID`) invece dell'intera riga.
### Valori mancanti
```python
data.isna().sum()
```
L'unica colonna con NA è `Income`: 24 valori mancanti (\~1%). Per ora si nota e si va avanti. Strategie possibili in seguito: imputazione con media/mediana, o rimozione delle righe se la percentuale è trascurabile.
### Distribuzioni numeriche — boxplot
Per le variabili continue, i boxplot sono il modo più rapido per vedere distribuzione, mediana, range e outlier:
```python
continuous_vars = [
    'Year_Birth', 'Income', 'Kidhome', 'Teenhome',
    'Recency', 'MntWines', 'MntFruits', 'MntMeatProducts',
    'MntFishProducts', 'MntSweetProducts', 'MntGoldProds',
    'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases',
    'NumStorePurchases', 'NumWebVisitsMonth'
]

fig, axes = plt.subplots(4, 4)
for i, col in enumerate(continuous_vars):
    data.boxplot(col, ax=axes.flatten()[i], fontsize='large')
fig.set_size_inches(18.5, 14)
plt.tight_layout()
plt.show()
```
Cosa emerge:
- `Year_Birth`: la maggior parte tra 1960–1980, ma ci sono outlier vicino al 1900 — dati palesemente errati
- `Income`: un outlier sopra 600k che comprime tutto il resto nella parte bassa
- `MntWines`, `MntMeatProducts` e simili: distribuzioni skewed a destra (coda lunga verso valori alti)
- `Recency`: distribuzione simmetrica tra 0 e 100, nessun outlier
- `Kidhome`, `Teenhome`: discrete (0, 1, 2), il boxplot non è il tool ideale ma funziona
### Distribuzioni categoriche — barplot
```python
categorical_vars = [
    'Education', 'Marital_Status', 'AcceptedCmp1',
    'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4',
    'AcceptedCmp5', 'Complain', 'Response'
]

fig, axes = plt.subplots(3, 3)
for i, col in enumerate(categorical_vars):
    counts = data[col].value_counts()
    counts.plot(
        kind='barh',
        ax=axes.flatten()[i],
        fontsize='large',
        color='#4e6c50'
    ).set_title(col)
fig.set_size_inches(15, 7)
plt.tight_layout()
plt.show()
```
Osservazioni interessanti:
- `Education`: molti PhD nel campione — insolito, suggerisce un campione biased o risposte non veritiere
- `Marital_Status`: compaiono valori come `"YOLO"` e `"Absurd"` — dati sporchi da gestire
- `AcceptedCmp1`–`5`: fortemente sbilanciati (molti 0, pochi 1) — tipico nelle campagne marketing. `AcceptedCmp2` è ancora più sbilanciato degli altri
- `Complain`: quasi tutti 0 (0.9% ha reclamato) — variabile di scarsa utilità predittiva
### Variabile data — trend di registrazione
```python
data.groupby(
    pd.Grouper(key='Dt_Customer', freq='ME')
).count().ID.plot(color='#4e6c50')
plt.title('Clienti registrati per mese')
plt.show()
```
> **`pd.Grouper`** è lo strumento giusto per raggruppare su colonne datetime con una frequenza (qui `'ME'` = month end). Alternativa: `resample()` che funziona solo se la colonna è l'indice del DataFrame.
Il grafico mostra registrazioni concentrate tra luglio 2012 e luglio 2014, con pochi clienti nei 6 mesi prima e dopo. Questo potrebbe indicare un periodo specifico di raccolta dati.
---
## Analisi bivariata
L'analisi bivariata esplora le relazioni tra **coppie** di variabili. Permette di identificare correlazioni, potenziali predittori e pattern interessanti.
<table header-row="true">
<tr>
<td>Tipo di variabili</td>
<td>Tecniche comuni</td>
</tr>
<tr>
<td>Numerica vs Numerica</td>
<td>Scatter plot, correlazione di Pearson, regressione</td>
</tr>
<tr>
<td>Numerica vs Categorica</td>
<td>Box plot, violin plot, bar plot</td>
</tr>
<tr>
<td>Categorica vs Categorica</td>
<td>Tabelle di contingenza, heatmap, test chi-quadro</td>
</tr>
</table>
### Numerica vs Numerica — scatter matrix
Per vedere tutte le relazioni tra variabili continue in un colpo solo, si usa la scatter matrix:
```python
sm = pd.plotting.scatter_matrix(
    data[continuous_vars],
    color='#4e6c50', figsize=(12, 12), alpha=0.2
)
# Nasconde tick e ruota le label per leggibilità
for subaxis in sm:
    for ax in subaxis:
        ax.xaxis.set_ticks([])
        ax.yaxis.set_ticks([])
        ax.xaxis.label.set_rotation(45)
        ax.yaxis.label.set_rotation(0)
        ax.yaxis.label.set_ha('right')
# Nasconde il triangolo superiore e la diagonale (ridondanti)
for i in range(np.shape(sm)[0]):
    for j in range(np.shape(sm)[1]):
        if i <= j:
            sm[i, j].set_visible(False)
plt.show()
```
Il problema con gli outlier è che comprimono i punti e rendono le relazioni difficili da vedere. Si rimuovono usando lo **z-score**:
```python
from scipy import stats

data_subset = data[continuous_vars].dropna()
# Filtra le righe dove TUTTE le colonne hanno z-score < 2
data_subset = data_subset[(np.abs(stats.zscore(data_subset)) < 2).all(axis=1)]
```
> **Z-score come filtro outlier**: `stats.zscore()` restituisce, per ogni valore, quante deviazioni standard dista dalla media della sua colonna. Tenere solo i valori con `|z| < 2` significa escludere ciò che sta oltre 2σ dalla media — una soglia ragionevole per un'esplorazione rapida. Non è il metodo più sofisticato, ma è veloce e applicabile uniformemente a tutte le colonne.
Dopo la rimozione degli outlier emergono pattern chiari:
- `Income` è fortemente correlato con la maggior parte delle variabili `Mnt...`
- `Income` è **negativamente** correlato con `NumWebVisitsMonth` (i clienti più ricchi visitano meno il sito — acquistano direttamente)
- Le variabili `Mnt...` sono positivamente correlate tra loro
- `Year_Birth` non mostra correlazioni forti con nulla
### Numerica vs Categorica — boxplot
Per confrontare distribuzioni tra gruppi, il boxplot per categoria è lo strumento classico:
```python
sns.boxplot(x='Department', y='Salary', data=df)
```
La differenza di mediana e spread tra i box indica differenze reali tra categorie.
### Categorica vs Categorica — crosstab e chi-square
```python
# Tabella di contingenza normalizzata per colonna
pd.crosstab(
    index=data['Marital_Status'],
    columns=data['Response'],
    normalize='columns'
).round(2)
```
Interpretazione: i valori rappresentano la proporzione *all'interno di ogni categoria* di `Response`. Esempio: il 32% di chi ha accettato l'ultima offerta è single, contro il 20% di chi non ha accettato → i single tendono di più ad accettare.
Analologo per `Education` vs `Response`: i clienti con PhD o Master accettano proporzionalmente di più.
**Test chi-quadro** — verifica statistica dell'indipendenza tra due variabili categoriche:
```python
from scipy.stats import chi2_contingency

table = pd.crosstab(df['Gender'], df['Brand'])
chi2, p, dof, expected = chi2_contingency(table)
print(f'Chi2: {chi2:.2f}, p-value: {p:.4f}')
```
> **Come leggere il p-value**: se `p < 0.05`, le due variabili **non** sono indipendenti — c'è una relazione statisticamente significativa. Se `p > 0.05`, non si può concludere che ci sia associazione. Nel caso del dataset marketing, Gender vs Brand con 6 osservazioni dà `p ≈ 0.135` — non significativo, ma il campione è troppo piccolo per concludere qualcosa.
### Trend temporali — `groupby` con `pd.Grouper`
Per le variabili in relazione alla data di registrazione:
```python
# Trend mensile di Kidhome e Teenhome
data[['Dt_Customer', 'Kidhome', 'Teenhome']].groupby(
    pd.Grouper(key='Dt_Customer', freq='ME')
).mean().plot()
```
Osservazioni:
- `Kidhome` e `Teenhome` sono stabili nel tempo — nessun trend
- Le vendite dei prodotti (`Mnt...`) tendono a diminuire nel tempo
- `Response` e `AcceptedAnyCmp` (unione delle 5 campagne) mostrano trend opposti — controintuitivo e merita approfondimento
**Attenzione a ****`SettingWithCopyWarning`**: quando si crea un subset di un DataFrame e poi si aggiunge una colonna, Pandas avverte che si sta modificando una copia e non l'originale:
```python
# Genera SettingWithCopyWarning
data_subset = data[['Dt_Customer', 'AcceptedCmp1', ...]]
data_subset['AcceptedAnyCmp'] = ...  # ⚠️

# Forma corretta — .copy() rende esplicito che è un nuovo DataFrame
data_subset = data[['Dt_Customer', 'AcceptedCmp1', ...]].copy()
data_subset['AcceptedAnyCmp'] = ...  # ✅
```
---
## Analisi multivariata
L'analisi multivariata esplora le relazioni tra **tre o più variabili contemporaneamente**. È utile per la feature selection, la riduzione della dimensionalità e la comprensione della struttura del dataset.
<table header-row="true">
<tr>
<td>Tecnica</td>
<td>Scopo</td>
<td>Libreria</td>
</tr>
<tr>
<td>Pairplot</td>
<td>Relazioni a coppie con gruppi colorati</td>
<td>seaborn</td>
</tr>
<tr>
<td>Correlation matrix + heatmap</td>
<td>Correlazioni lineari tra tutte le numeriche</td>
<td>pandas, seaborn</td>
</tr>
<tr>
<td>PCA</td>
<td>Riduzione dimensionalità</td>
<td>scikit-learn</td>
</tr>
<tr>
<td>Factor Analysis</td>
<td>Identificazione di fattori latenti</td>
<td>scikit-learn</td>
</tr>
<tr>
<td>KMeans clustering</td>
<td>Raggruppamento per similarità</td>
<td>scikit-learn</td>
</tr>
</table>
### Correlation matrix
```python
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
```
Valori vicini a +1 o -1 indicano forte correlazione positiva o negativa. Valori vicini a 0 indicano assenza di relazione lineare.
### PCA — Principal Component Analysis
La PCA riduce la dimensionalità trovando le direzioni dello spazio dei dati che spiegano la maggior varianza. Con `n_components=2` si proiettano tutti i dati su un piano 2D visualizzabile:
```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Standardizzare prima — la PCA è sensibile alla scala
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df.iloc[:, :-1])

pca = PCA(n_components=2)
components = pca.fit_transform(X_scaled)

pca_df = pd.DataFrame(components, columns=['PC1', 'PC2'])
pca_df['species'] = df['species']
sns.scatterplot(data=pca_df, x='PC1', y='PC2', hue='species')
plt.title('PCA — 2 componenti principali')
plt.show()
```
> **Perché standardizzare?** La PCA massimizza la varianza spiegata. Se le colonne hanno scale diverse (es. `Income` in migliaia vs `Kidhome` tra 0 e 2), quelle con varianza più alta dominerebbero i componenti. `StandardScaler` porta tutto a media 0 e deviazione standard 1.
### Factor Analysis
La Factor Analysis è simile alla PCA ma parte da un'ipotesi diversa: che le variabili osservate siano *generate* da un numero inferiore di **fattori latenti** non osservabili. È comune in psicometria e scienze sociali.
```python
from sklearn.decomposition import FactorAnalysis

fa = FactorAnalysis(n_components=2)
fa.fit(X_scaled)

# fa.components_ ha shape (n_factors, n_features)
# Trasposto: ogni riga è una feature, ogni colonna è un fattore
fa_components = pd.DataFrame(fa.components_.T, index=continuous_vars)

# Scatter plot: ogni punto è una feature, posizionata secondo il suo
# peso sui due fattori
ax = fa_components.plot.scatter(x=0, y=1, alpha=0.5)
for i, txt in enumerate(fa_components.index):
    ax.annotate(txt, (fa_components[0].iat[i] + 0.05, fa_components[1].iat[i]))
plt.show()
```
Dal grafico emergono due fattori interpretabili:
- **Fattore 1 (asse X)**: riassume le variabili `Mnt...` — un fattore di "propensione alla spesa"
- **Fattore 2 (asse Y)**: riassume le variabili legate al numero di acquisti per canale
Proiettando i clienti sugli stessi assi si vedono due cluster distinti — separati principalmente per reddito:
```python
fa_transformed = pd.DataFrame(fa.transform(X_scaled))
ax = fa_transformed.plot.scatter(
    x=0, y=1,
    c=data_subset['Income'],
    colormap='viridis'
)
plt.show()
```
> **`colormap='viridis'`** è una scala di colore percettivamente uniforme (blu scuro = basso, giallo = alto). È la scelta predefinita raccomandata per variabili continue perché non introduce bias visivi.
### KMeans clustering
KMeans raggruppa i dati in `k` cluster minimizzando la distanza intra-cluster:
```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(df.iloc[:, :-2])

sns.scatterplot(
    x='sepal_length', y='sepal_width',
    hue='cluster', data=df, palette='Set1'
)
plt.title('KMeans Clustering')
plt.show()
```
> La scelta di `k` non è banale. In pratica si usa il metodo **elbow**: si plotta l'inerzia (somma delle distanze quadratiche intra-cluster) al variare di `k` e si sceglie il punto in cui la curva smette di scendere bruscamente.
---
## Analisi di regressione — OLS con statsmodels
Dopo l'esplorazione, si può formalizzare una relazione con la regressione lineare. Qui si usa `statsmodels` invece di `sklearn` perché restituisce un summary statistico completo:
```python
import statsmodels.api as sm

# Preparazione dati (dopo rimozione outlier)
data_subset = data_subset.dropna()
X = data_subset.drop('Income', axis=1)
y = data_subset['Income']

# OLS = Ordinary Least Squares
model = sm.OLS(y, X)
results = model.fit()
print(results.summary())
```
Il summary include p-value per ogni coefficiente, R², F-statistic e molto altro. Un secondo fit rimuove le variabili non significative:
```python
X_reduced = data_subset.drop([
    'Income', 'Recency', 'MntFruits', 'MntFishProducts',
    'MntSweetProducts', 'MntGoldProds', 'NumCatalogPurchases'
], axis=1)
results_reduced = sm.OLS(y, X_reduced).fit()
print(results_reduced.summary())
```
> **`statsmodels`**** vs ****`sklearn`**: `sklearn` è ottimizzato per il machine learning (pipeline, cross-validation, predict). `statsmodels` è ottimizzato per l'inferenza statistica (p-value, intervalli di confidenza, test di ipotesi). Per l'EDA e la comprensione del modello, `statsmodels` è più informativo.
---
## Hexbin plot
Lo scatter plot con molti punti sovrapposti è illeggibile. L'hexbin risolve il problema aggregando i punti in celle esagonali e colorandole per densità:
```python
ax = data_subset.plot.hexbin(
    x='Income', y='Year_Birth',
    gridsize=10  # granularità della griglia
)
```
Il colore più scuro indica maggiore concentrazione di punti. Dal grafico emerge che la maggior parte dei clienti ha reddito tra 20k–60k e anno di nascita tra 1955 e 1985.
---
## EDA con Plotly — visualizzazioni interattive
Finora si è usato Matplotlib/Seaborn per visualizzare i dati. **Plotly** è un'alternativa che produce grafici interattivi (zoom, hover, tooltip) particolarmente utili in Jupyter Notebook. Funziona bene con Pandas e si integra con Seaborn come complemento, non come sostituto.
Plotly si divide in due sottolibrerie principali:
- `plotly.express` (alias `px`) — API di alto livello, concisa, adatta alla maggior parte dei casi
- `plotly.graph_objects` (alias `go`) — API di basso livello, più verbosa ma più flessibile per grafici personalizzati
```python
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')
```
> `warnings.filterwarnings('ignore')` sopprime i warning di deprecazione che Plotly e Pandas generano spesso nelle versioni non aggiornate. Utile nei notebook, sconsigliato in produzione.
### Istogramma con Plotly Express
Esempio su un dataset healthcare (`healthcare_dataset.csv`, 55.500 righe, 15 colonne con dati demografici e medici di pazienti ospedalizzati):
```python
fig = px.histogram(df, x='Age', title='Age Distribution', nbins=30)
fig.show()
```
A differenza di Matplotlib, il grafico è interattivo: hovering mostra i valori esatti, si può fare zoom, e si può esportare come PNG.
### Barplot categorici multipli con `go.Figure`
Per visualizzare la distribuzione di più variabili categoriche in un loop, si costruisce una figura `go` traccia per traccia:
```python
object_columns = ['Gender', 'Blood Type', 'Medical Condition',
                  'Admission Type', 'Insurance Provider',
                  'Medication', 'Test Results']

pastel_palette = px.colors.qualitative.Pastel

for col in object_columns:
    fig = go.Figure()
    for i, (category, count) in enumerate(df[col].value_counts().items()):
        fig.add_trace(go.Bar(
            x=[col], y=[count],
            name=category,
            marker_color=pastel_palette[i]
        ))
    fig.update_layout(
        title=f'Distribution of {col}',
        xaxis_title=col,
        yaxis_title='Count'
    )
    fig.show()
```
Pattern da notare:
- Si itera su `value_counts().items()` — restituisce coppie `(categoria, conteggio)` già ordinate per frequenza
- Ogni categoria diventa una traccia `go.Bar` separata con colore dalla palette Pastel
- `enumerate()` fornisce l'indice `i` per accedere alla palette
### Analisi bivariata con `groupby` + `size` + Plotly
Per esplorare relazioni tra due variabili categoriche si combina `groupby` con `size()` per contare le occorrenze di ogni combinazione:
```python
# Età media per condizione medica
age_by_condition = df.groupby('Medical Condition')['Age'].mean().reset_index()

fig = px.bar(
    age_by_condition,
    x='Medical Condition', y='Age',
    color='Medical Condition',
    title='Average Age by Medical Condition',
    labels={'Age': 'Average Age'},
    color_discrete_sequence=px.colors.qualitative.Pastel
)
fig.show()
```
Per relazioni tra due categoriche (conteggi):
```python
# Farmaci per condizione medica
grouped_df = df.groupby(['Medical Condition', 'Medication']).size().reset_index(name='Count')

fig = px.bar(
    grouped_df,
    x='Medical Condition', y='Count',
    color='Medication',
    barmode='group',  # barre affiancate, non impilate
    title='Medication Distribution by Medical Condition'
)
fig.show()
```
> **`barmode='group'`** vs **`barmode='stack'`**: `group` affianca le barre per categoria (più leggibile per confrontare proporzioni), `stack` le impila (più leggibile per confrontare totali). Default di Plotly è `relative` (equivalente a stack).
Altre combinazioni utili sullo stesso dataset:
- `groupby(['Blood Type', 'Medical Condition'])` — distribuzione patologie per gruppo sanguigno
- `groupby(['Admission Type', 'Gender'])` — tipo di accesso per genere
- `groupby(['Test Results', 'Admission Type'])` — esiti test per tipo di accesso
---
## Query analitiche sul DataFrame
Dopo la visualizzazione, spesso si vogliono rispondere a domande specifiche con codice conciso. Alcuni pattern ricorrenti:
### Trovare il valore modale di una colonna categorica
```python
# Gruppo sanguigno più comune
most_common = df['Blood Type'].value_counts().idxmax()
print(f'Il gruppo sanguigno più comune è {most_common}.')
# → A-
```
`value_counts()` conta le occorrenze per categoria (ordinate discendente), `.idxmax()` restituisce l'indice (cioè il nome della categoria) con il valore massimo.
### Contare valori unici
```python
unique_hospitals = df['Hospital'].nunique()
print(f'Ospedali unici nel dataset: {unique_hospitals}.')
```
`nunique()` conta i valori distinti in una colonna, equivalente a `len(df['Hospital'].unique())`.
### Trovare il record con valore estremo
```python
oldest_age = df['Age'].max()
oldest_name = df[df['Age'] == oldest_age]['Name'].iloc[0]
print(f'Paziente più anziano: {oldest_name}, {oldest_age} anni.')
```
Pattern: filtra le righe dove la condizione è vera, poi `.iloc[0]` prende il primo risultato (nel caso di parità).
### Analisi di frequenza con top-N
```python
top3_conditions = df['Medical Condition'].value_counts().head(3)
print(top3_conditions)
```
`.head(n)` su una Series restituisce i primi `n` elementi — poiché `value_counts()` ordina già per frequenza decrescente, questo dà le categorie più comuni.
### Trend temporale mensile
```python
monthly_admissions = df['Date of Admission'].dt.month.value_counts().sort_index()
monthly_df = pd.DataFrame({
    'Month': monthly_admissions.index,
    'Admissions': monthly_admissions.values
})

fig = px.line(monthly_df, x='Month', y='Admissions',
              title='Monthly Admissions Trend')
fig.show()
```
> `.dt.month` estrae il mese come intero (1–12) da una colonna datetime. Alternativa più flessibile: `pd.Grouper` come visto nella sezione precedente, che consente raggruppamenti per settimana, trimestre, anno, ecc.
---
## Differenza tra bar chart e istogramma
Un errore comune è confondere bar chart e istogramma — sembrano simili ma rappresentano cose diverse:
<table header-row="true">
<tr>
<td>Caratteristica</td>
<td>Bar chart</td>
<td>Istogramma</td>
</tr>
<tr>
<td>Tipo di dato</td>
<td>Categorico</td>
<td>Continuo / numerico</td>
</tr>
<tr>
<td>Barre</td>
<td>Separate (gap visibile)</td>
<td>Adiacenti (nessun gap)</td>
</tr>
<tr>
<td>Asse X</td>
<td>Categorie (etichette)</td>
<td>Intervalli numerici (bin)</td>
</tr>
<tr>
<td>Asse Y</td>
<td>Conteggio o valore</td>
<td>Frequenza (quanti valori cadono nel bin)</td>
</tr>
<tr>
<td>Esempio</td>
<td>Distribuzione per genere</td>
<td>Distribuzione dell'età</td>
</tr>
</table>
In Matplotlib: `df['Gender'].value_counts().plot(kind='bar')` → bar chart; `df['Age'].hist()` → istogramma. In Plotly: `px.bar()` vs `px.histogram()`.
---
## Riferimenti
- [Dataset — Kaggle Customer Personality Analysis](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)
- [Dataset — Kaggle Healthcare Dataset](https://www.kaggle.com/datasets/prasad22/healthcare-dataset)
- [pandas — groupby con Grouper](https://pandas.pydata.org/docs/reference/api/pandas.Grouper.html)
- [pandas — crosstab](https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html)
- [pandas — value_counts](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html)
- [statsmodels — OLS](https://www.statsmodels.org/stable/regression.html)
- [scikit-learn — FactorAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html)
- [scipy — stats.zscore](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.zscore.html)
- [Plotly Express — documentazione](https://plotly.com/python/plotly-express/)
- [Plotly Graph Objects — Bar](https://plotly.com/python/bar-charts/)
