# 12 - Pipeline e pd.pipe

> Fonte Notion: https://app.notion.com/p/33b12abc808d81f6a2cfc39995d72107 — ultima modifica 2026-04-07T00:20:18.745Z

Il concetto di **pipeline** è trasversale a tutto il ciclo di vita del dato: compare nell'ETL/ELT, nel preprocessing per il machine learning, nell'EDA automatizzata. In questo modulo si tratta il pattern pipeline in Python e lo strumento `pd.pipe` di Pandas come implementazione concreta.
---
## Cos'è una pipeline
Una pipeline è una serie di **step sequenziali** in cui l'output di uno step diventa l'input del successivo. Il dato scorre attraverso le fasi come in una catena di montaggio.
I benefici principali rispetto al codice procedurale piatto:
- **Modularità** — ogni fase è una funzione indipendente, testabile e riusabile
- **Leggibilità** — la sequenza delle operazioni è esplicita e lineare
- **Manutenibilità** — modificare una fase non richiede di toccare le altre
- **Riproducibilità** — lo stesso input produce sempre lo stesso output
Le pipeline sono il pattern standard in ETL/ELT, ML preprocessing (scikit-learn `Pipeline`), e data science workflow.
### Struttura tipica
```javascript
INPUT → [Extract] → [Transform] → [Load/Analyze] → OUTPUT
```
Esempio minimo in Python puro:
```python
def extract(path):
    return pd.read_csv(path)

def transform(df):
    df['name'] = df['name'].str.title()
    df = df.dropna()
    return df

def load(df, dest):
    df.to_csv(dest, index=False)
    print("Pipeline completata.")

def pipeline(src, dest):
    df = extract(src)
    df = transform(df)
    load(df, dest)

pipeline('raw_data.csv', 'clean_data.csv')
```
Ogni funzione ha una sola responsabilità. La funzione `pipeline` orchestra il flusso senza contenere logica di business.
---
## Tipi di pipeline per dati
### Batch processing
Elabora i dati in **blocchi** a intervalli programmati (es. ogni notte, ogni settimana). È il modello classico ETL: si raccolgono i dati accumulati, si trasformano e si caricano.
Caratteristiche:
- Lavora su grandi volumi in una volta sola
- Ottimale quando l'analisi non richiede aggiornamento in tempo reale (es. report mensili, contabilità)
- I job sono sequenze di comandi: l'output di uno è l'input del successivo
- Più affidabile dello streaming (nessun messaggio perso)
- Più associato a ETL
### Streaming (event-driven)
Elabora gli eventi **continuamente**, man mano che si generano. Ogni azione utente, lettura di sensore o transazione è un "evento".
Caratteristiche:
- Latenza bassa rispetto al batch
- Meno affidabile (i messaggi possono essere persi o accodarsi a lungo)
- I message broker (es. **Apache Kafka**) gestiscono gli acknowledgement per ridurre le perdite
- Tipico nei sistemi di inventario real-time, feed social, monitoraggio IoT
> **Apache Kafka** è il sistema open-source più diffuso per lo streaming di eventi. I messaggi sono organizzati in **topic** (argomenti); i produttori pubblicano messaggi, i consumatori li leggono.
### Data integration pipeline
Focalizzata sul **merge** di dati da sorgenti multiple (CSV, API, database, cloud storage) in una vista unificata. Spesso include processi ETL/ELT che normalizzano formati e strutture incompatibili prima del caricamento in un data warehouse.
### Cloud-native pipeline
Platform moderna che usa servizi cloud (es. AWS S3, BigQuery, Snowflake) per ingestione, storage, processing e trasformazione. Riduce i data silo, abilita il self-service analytics e migliora la qualità del dato.
---
## Data lineage
All'interno di qualsiasi pipeline, il **data lineage** traccia il percorso del dato dalla sorgente alla destinazione: da dove viene, come è stato modificato, dove arriva.
Serve a:
- **Validare accuratezza e consistenza** — si può ripercorrere ogni trasformazione applicata
- **Debug** — si traccia un errore fino alla sorgente
- **Audit e compliance** — documentazione del flusso per requisiti regolatori
- **Contesto storico** — capire come il dato è cambiato nel tempo
Strumenti di data lineage registrano metadata su ogni step: sorgente, timestamp, tipo di trasformazione, destinazione.
---
## `pd.pipe` — pipeline con Pandas
`DataFrame.pipe(func, *args, **kwargs)` applica una funzione al DataFrame e restituisce il risultato. L'utilità emerge quando si concatenano più `pipe` in sequenza: il codice diventa una lista ordinata di trasformazioni, leggibile come una pipeline esplicita.
### Senza pipe — codice procedurale
```python
import pandas as pd

df = pd.read_csv('data/Online Sales Data.csv')

# Cleaning
df = df.drop_duplicates()
df = df.dropna()
df = df.reset_index(drop=True)

# Type conversion
df['Product Category'] = df['Product Category'].astype('str')
df['Product Name'] = df['Product Name'].astype('str')
df['Date'] = pd.to_datetime(df['Date'])

# Analysis
df['month'] = df['Date'].dt.month
new_df = df.groupby('month')['Units Sold'].mean()

# Visualization
new_df.plot(kind='bar', figsize=(10, 5), title='Average Units Sold by Month')
```
Funziona, ma le fasi sono mescolate. Aggiungere un nuovo step o cambiare l'ordine richiede di modificare il blocco procedurale.
### Con pipe — refactoring in funzioni
Si incapsula ogni fase in una funzione, poi si usa `pipe` per concatenarle:
```python
def load_data(path):
    return pd.read_csv(path)

def data_cleaning(data):
    data = data.drop_duplicates()
    data = data.dropna()
    data = data.reset_index(drop=True)
    return data

def convert_dtypes(data, types_dict=None):
    data = data.astype(dtype=types_dict)
    return data

def data_analysis(data):
    data['month'] = data['Date'].dt.month
    new_df = data.groupby('month')['Units Sold'].mean()
    return new_df

def data_visualization(new_df, vis_type='bar'):
    new_df.plot(kind=vis_type, figsize=(10, 5), title='Average Units Sold by Month')
    return new_df
```
Esecuzione della pipeline:
```python
path = "data/Online Sales Data.csv"

df = (
    pd.DataFrame()
    .pipe(lambda x: load_data(path))          # lambda perché load_data non accetta un df
    .pipe(data_cleaning)
    .pipe(convert_dtypes, {'Product Category': 'str', 'Product Name': 'str'})
    .pipe(data_analysis)
    .pipe(data_visualization, 'line')          # argomento posizionale extra
)
```
### Come funziona `pipe`
`df.pipe(func, *args, **kwargs)` è equivalente a `func(df, *args, **kwargs)`. Quindi:
```python
df.pipe(data_cleaning)
# equivale a:
data_cleaning(df)

df.pipe(convert_dtypes, {'Product Category': 'str'})
# equivale a:
convert_dtypes(df, {'Product Category': 'str'})
```
L'output di ogni `.pipe()` viene passato come primo argomento alla funzione successiva nella catena.
> **Nota su ****`lambda x: load_data(path)`**: il primo `pipe` parte da un `pd.DataFrame()` vuoto. Siccome `load_data` non accetta un DataFrame in input (accetta un `path`), serve una lambda che ignori `x` e chiami `load_data(path)`. In alternativa si può saltare il DataFrame vuoto e scrivere la pipeline partendo direttamente da `load_data(path).pipe(data_cleaning)...`
### Vantaggi rispetto ad `.apply()`
Alcuni utenti riportano che `pipe` risulta più veloce di `.apply()` per trasformazioni complesse su DataFrame interi, perché opera sull'intero DataFrame invece che riga per riga. `.apply()` è pensato per trasformazioni elemento per elemento o per riga.
---
## Dataset — Online Sales Data
Il dataset usato negli esempi è **Online Sales Dataset - Popular Marketplace Data** di Kaggle. Contiene transazioni di vendita online con le seguenti colonne principali:
<table header-row="true">
<tr>
<td>Colonna</td>
<td>Tipo</td>
<td>Descrizione</td>
</tr>
<tr>
<td>`Transaction ID`</td>
<td>int64</td>
<td>Identificatore univoco transazione</td>
</tr>
<tr>
<td>`Date`</td>
<td>object → datetime</td>
<td>Data della transazione</td>
</tr>
<tr>
<td>`Product Category`</td>
<td>object</td>
<td>Categoria prodotto (Electronics, Clothing, ...)</td>
</tr>
<tr>
<td>`Product Name`</td>
<td>object</td>
<td>Nome prodotto</td>
</tr>
<tr>
<td>`Units Sold`</td>
<td>int64</td>
<td>Quantità venduta</td>
</tr>
<tr>
<td>`Unit Price`</td>
<td>float64</td>
<td>Prezzo unitario</td>
</tr>
<tr>
<td>`Total Revenue`</td>
<td>float64</td>
<td>Ricavo totale</td>
</tr>
</table>
La pipeline eseguita sull'esempio:
1. **Load** — lettura CSV
2. **Clean** — rimozione duplicati e NA, reset indice
3. **Convert** — `Product Category` e `Product Name` a `str`, `Date` a `datetime`
4. **Analyze** — estrazione mese, media `Units Sold` per mese con `groupby`
5. **Visualize** — line chart delle vendite medie mensili
---
## Riferimenti
- [Dataset — Kaggle Online Sales Dataset](https://www.kaggle.com/datasets/shreyanshverma27/online-sales-dataset-popular-marketplace-data)
- [pandas — DataFrame.pipe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pipe.html)
- [IBM — What is a data pipeline?](https://www.ibm.com/topics/data-pipeline)
- [Apache Kafka — documentazione](https://kafka.apache.org/documentation/)
