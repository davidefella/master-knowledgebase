# 10 - EDA e ETL

> Fonte Notion: https://app.notion.com/p/33812abc808d81bc9e07e1626cffdf9e — ultima modifica 2026-04-07T00:19:23.974Z

EDA (Exploratory Data Analysis) ed ETL (Extract-Transform-Load) sono i due processi fondamentali nella gestione dei dati prima e dopo la modellazione.
---
## EDA — Exploratory Data Analysis
**Obiettivo:** capire la struttura del dataset, individuare pattern, anomalie e relazioni tra variabili *prima* di costruire modelli formali.
**Step tipici:**
- Visualizzazione dei dati (istogrammi, scatter plot, box plot)
- Statistiche descrittive (media, mediana, correlazione, distribuzione)
- Individuazione di valori mancanti e outlier
**Librerie Python:** `pandas`, `matplotlib`, `seaborn`
---
## ETL — Extract, Transform, Load
**Obiettivo:** raccogliere dati da sorgenti eterogenee, normalizzarli e caricarli in una destinazione strutturata per l'analisi.
<table header-row="true">
<tr>
<td>Fase</td>
<td>Descrizione</td>
<td>Strumenti Python</td>
</tr>
<tr>
<td>**Extract**</td>
<td>Lettura da CSV, API, DB, web scraping</td>
<td>`pandas`, `requests`, `BeautifulSoup`</td>
</tr>
<tr>
<td>**Transform**</td>
<td>Pulizia, deduplicazione, normalizzazione, join</td>
<td>`pandas`</td>
</tr>
<tr>
<td>**Load**</td>
<td>Scrittura su DB, data warehouse</td>
<td>`SQLAlchemy`, Apache Airflow</td>
</tr>
</table>
> **Posizione nel workflow:** ETL viene *prima* dell'analisi. EDA viene *dopo* il caricamento, sui dati già puliti.
---
## Esempio pratico — Sales data (Store CSV)
### ETL: unire più CSV, pulire e salvare
```python
import pandas as pd
import glob

# --- Extract ---
# glob.glob trova tutti i file che matchano il pattern
file_paths = glob.glob("data/Store_*.csv")

# List comprehension per leggere tutti i file in una lista di DataFrame
# encoding='latin1' necessario per file con caratteri non-UTF8 (es. byte 0x84)
df_list = [pd.read_csv(file, encoding='latin1') for file in file_paths]

# pd.concat combina verticalmente i DataFrame; ignore_index rigenera l'indice
combined_df = pd.concat(df_list, ignore_index=True)

# --- Transform ---
combined_df.drop_duplicates(inplace=True)
combined_df.fillna({"SALES": combined_df["SALES"].mean()}, inplace=True)

# Standardizzare i nomi colonna: lowercase + underscore al posto degli spazi
combined_df.columns = combined_df.columns.str.lower().str.replace(" ", "_")

# --- Load ---
combined_df.to_csv("cleaned_sales_data.csv", index=False)
```
> **UnicodeDecodeError:** `pd.read_csv` usa UTF-8 di default. Se il file contiene caratteri latin1/windows-1252 (comune nei CSV da Windows), si passa `encoding='latin1'` oppure `encoding='cp1252'`. In alternativa `encoding_errors='replace'` per ignorare i byte non validi.
### EDA: analisi e visualizzazione
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_sales_data.csv")

# Struttura e statistiche
print(df.head())       # prime 5 righe
print(df.describe())   # count, mean, std, min, quartili, max

# Distribuzione delle vendite (istogramma + KDE)
sns.histplot(df['sales'], bins=20, kde=True)
plt.title("Sales Distribution")
plt.show()
# La distribuzione risultante è asimmetrica a destra (right-skewed):
# la maggior parte delle vendite è tra 2000-4000, con una coda lunga fino a 14000

# Top 5 prodotti per fatturato
top_products = df.groupby("productcode")["sales"].sum().sort_values(ascending=False).head(5)
top_products.plot(kind='barh', color='green')
plt.title("Top 5 Best-Selling Products")
plt.gca().invert_yaxis()   # prodotto con vendite maggiori in cima
plt.show()
```
---
## Esempio avanzato — Global Peace Index
Dataset: `global_peace_index.csv` — indice di pace per paese, anni 2008–2022.
### ETL: parsing corretto e reshape in formato long
```python
import pandas as pd

# Il CSV usa tab come separatore — sep='\t' necessario per un parsing corretto
peace_df = pd.read_csv("global_peace_index.csv", sep='\t')

# Il dataset è in formato wide (una colonna per anno)
# pd.melt lo converte in formato long (una riga per paese/anno)
peace_df_long = peace_df.melt(
    id_vars=['Country', 'Country_Code'],
    var_name='Year',
    value_name='Peace_Index'
)
peace_df_long['Year'] = peace_df_long['Year'].astype(int)
```
**Formato wide vs long:**
<table header-row="true">
<tr>
<td>Formato</td>
<td>Struttura</td>
<td>Uso tipico</td>
</tr>
<tr>
<td>Wide</td>
<td>Una colonna per anno</td>
<td>Dati grezzi, pivot table</td>
</tr>
<tr>
<td>Long (tidy)</td>
<td>Una riga per osservazione</td>
<td>Analisi, visualizzazione con seaborn/matplotlib</td>
</tr>
</table>
> `pd.melt()` è la trasformazione chiave per passare da wide a long. È l'equivalente pandas di `UNPIVOT` in SQL.
### EDA: trend globale e per paese
```python
import matplotlib.pyplot as plt

# Trend medio globale anno per anno
global_trend = peace_df_long.groupby('Year')['Peace_Index'].mean()
global_trend.plot(marker='o', color='gold')
plt.title("Global Peace Index Trend (2008-2022)")
plt.ylabel("Average Global Peace Index")
plt.show()
# Osservazione: l'indice medio globale è in aumento (peggioramento),
# da ~1.97 nel 2008 a ~2.06 nel 2022

# Top 5 paesi più pacifici nel 2022
top_countries = (
    peace_df_long[peace_df_long['Year'] == 2022]
    .nsmallest(5, 'Peace_Index')['Country']
    .tolist()
)

# Trend storico per i top 5
filtered = peace_df_long[peace_df_long['Country'].isin(top_countries)]
for country in top_countries:
    data = filtered[filtered['Country'] == country]
    plt.plot(data['Year'], data['Peace_Index'], marker='o', label=country)

plt.title("Peace Index Trends of Top 5 Most Peaceful Countries (2022)")
plt.legend()
plt.show()
# Iceland si conferma il paese più pacifico in quasi tutti gli anni
```
---
## ELT — Extract, Load, Transform
ELT è una variante di ETL con ordine diverso delle fasi: i dati vengono prima caricati grezzi nel sistema di destinazione (tipicamente un database o data warehouse), e la trasformazione avviene **dentro** il database tramite SQL.
<table header-row="true">
<tr>
<td></td>
<td>ETL</td>
<td>ELT</td>
</tr>
<tr>
<td>Ordine</td>
<td>Extract → Transform → Load</td>
<td>Extract → Load → Transform</td>
</tr>
<tr>
<td>Dove si trasforma</td>
<td>In memoria, lato applicazione</td>
<td>Nel database, lato SQL</td>
</tr>
<tr>
<td>Quando usarlo</td>
<td>Dati sensibili, trasformazioni complesse</td>
<td>Grandi volumi, sistemi scalabili (cloud DW)</td>
</tr>
<tr>
<td>Strumenti tipici</td>
<td>Pandas, Python</td>
<td>SQL, dbt, PostgreSQL</td>
</tr>
</table>
> ETL è più vecchio e consolidato. ELT è diventato comune con l'adozione dei data warehouse cloud (BigQuery, Snowflake, Redshift) che hanno potenza computazionale sufficiente per trasformare internamente grandi volumi.
### Connessione a PostgreSQL con SQLAlchemy
Per interagire con PostgreSQL da Python si usa **SQLAlchemy** come layer di astrazione. La libreria di basso livello è `psycopg2` (il driver), ma SQLAlchemy fornisce un'API più comoda e compatibile con Pandas.
```python
pip install psycopg2  # o psycopg2-binary per versione precompilata
```
```python
from sqlalchemy import create_engine, text

# Connection string PostgreSQL
DB_USER = 'postgres'
DB_PASSWORD = 'password'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'mda_2025'

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)
```
> **`create_engine`** non apre subito la connessione — crea un pool lazy. La connessione effettiva avviene al primo uso. **`text()`** è necessario per eseguire SQL raw con SQLAlchemy 2.x: le stringhe SQL nude non sono più accettate direttamente.
### ELT in tre step su database healthcare
Il dataset è `healthcare_dataset.csv` (55.500 righe, 15 colonne). I nomi nel campo `Name` arrivano con maiuscole casuali tipo `"BobbY JacKsoN"` — il cleanup si fa lato SQL con `INITCAP` e `TRIM`.
```python
import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine(DATABASE_URL)
TABLE_NAME = 'healthcare_raw'
csv_file_path = './healthcare_dataset.csv'

# Step 1 — Extract
df = pd.read_csv(csv_file_path)

# Step 2 — Load (carica i dati grezzi nel DB senza trasformare)
df.to_sql(TABLE_NAME, engine, if_exists='replace', index=False)

# Step 3 — Transform (dentro PostgreSQL con SQL)
with engine.connect() as conn:
    conn.execute(text(f"""
        DROP TABLE IF EXISTS {TABLE_NAME}_cleaned;
        CREATE TABLE {TABLE_NAME}_cleaned AS
        SELECT
            INITCAP(TRIM("Name"))           AS name,
            "Age",
            INITCAP("Gender")               AS gender,
            "Blood Type"                    AS blood_type,
            INITCAP("Medical Condition")    AS medical_condition,
            "Date of Admission"::DATE       AS date_of_admission,
            INITCAP("Doctor")               AS doctor,
            INITCAP("Hospital")             AS hospital,
            INITCAP("Insurance Provider")   AS insurance_provider,
            "Billing Amount"::FLOAT         AS billing_amount,
            "Room Number"::INT              AS room_number,
            INITCAP("Admission Type")       AS admission_type,
            "Discharge Date"::DATE          AS discharge_date,
            INITCAP("Medication")           AS medication,
            INITCAP("Test Results")         AS test_results
        FROM {TABLE_NAME};
    """))
```
Note sulle operazioni SQL usate:
- **`INITCAP`** — converte in title case: prima lettera maiuscola, resto minuscolo. Risolve il problema dei nomi inconsistenti come `"bobbY jacKsoN"` → `"Bobby Jackson"`
- **`TRIM`** — rimuove spazi iniziali e finali dalla stringa
- **`::DATE`**** / ****`::FLOAT`**** / ****`::INT`** — cast di tipo in PostgreSQL (equivalente a `CAST(col AS DATE)`). Necessario perché `df.to_sql` carica le date come `object` (stringa)
- **`if_exists='replace'`** su `df.to_sql` — se la tabella esiste già, la ricrea da zero. Alternative: `'append'` (aggiunge righe) e `'fail'` (errore se esiste)
### Versione a funzione (pattern pipeline)
La stessa logica ELT incapsulata in una funzione, che è il modo raccomandato quando il processo verrà riusato o schedulato:
```python
def run_elt_pipeline(csv_path, table_name, engine):
    # Step 1: Extract
    print("Extracting data...")
    df = pd.read_csv(csv_path)

    # Step 2: Load
    print("Loading into PostgreSQL...")
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Loaded into table: {table_name}")

    # Step 3: Transform
    print("Running SQL transformations...")
    with engine.connect() as conn:
        conn.execute(text(f"""
            DROP TABLE IF EXISTS {table_name}_cleaned;
            CREATE TABLE {table_name}_cleaned AS
            SELECT
                INITCAP(TRIM("Name")) AS name,
                "Age",
                INITCAP("Gender") AS gender,
                -- ... resto delle colonne
            FROM {table_name};
        """))
    print(f"Cleaned table created: {table_name}_cleaned")

if __name__ == "__main__":
    run_elt_pipeline(csv_file_path, 'healthcare_raw_elt', engine)
```
> Il blocco `if __name__ == "__main__":` assicura che la pipeline venga eseguita solo quando il file è lanciato direttamente, non quando viene importato come modulo da un altro script. È una buona pratica standard in Python.
---
## Riferimenti
- [pandas — read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
- [pandas — DataFrame.melt](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.melt.html)
- [pandas — ](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html)[DataFrame.to](http://DataFrame.to)[_sql](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html)
- [seaborn — histplot](https://seaborn.pydata.org/generated/seaborn.histplot.html)
- [SQLAlchemy — create_engine](https://docs.sqlalchemy.org/en/20/core/engines.html)
- [psycopg2 — documentazione](https://www.psycopg.org/docs/)
