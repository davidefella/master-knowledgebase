# 00 - Ripasso Python

> Fonte Notion: https://app.notion.com/p/33212abc808d81388576c5cf5d7c0480 — ultima modifica 2026-04-08T19:57:10.150Z

Prerequisiti minimi Python per il corso considerati un ripasso e non teoria da studiare
---
## Argomenti
- Ricorsione (caso base, caso ricorsivo)
- Errori e gestione delle eccezioni (`try/except/else/finally`, `raise`)
- Iterabili e iteratori
- Strutture dati: tuple, liste, set, dict
- List comprehension
- Modulo `array` (stdlib)
- Funzioni built-in: `sum`, `min`, `max`, `zip`, `range`
- Input/output e validazione
- Mutabilità e immutabilità
- Misurazione del tempo: `timeit` e `datetime`
- Logging
- Programmazione funzionale — riduzioni
> **Nota:** Ricerca lineare/binaria, Big O e Selection Sort sono trattati nel modulo **08 — Ricorsione e Big O**, dove trovano il contesto algoritmico più appropriato.
---
## Ricorsione
> 💡 *💡 *In AI la ricorsione appare negli alberi decisionali (Decision Tree, Random Forest) e nel backpropagation — l'algoritmo che allena una rete neurale è concettualmente una discesa ricorsiva attraverso i layer del grafo computazionale.
Una funzione ricorsiva chiama se stessa direttamente o indirettamente. È utile quando la soluzione iterativa non è immediata o quando il problema ha una struttura naturalmente ricorsiva.
Ogni funzione ricorsiva ha due parti obbligatorie:
- **Caso base:** la condizione che ferma la ricorsione (senza di essa il programma va in loop infinito)
- **Caso ricorsivo:** la chiamata a se stessa su un input più piccolo
### Esempio: fattoriale
```python
# Versione iterativa
def my_fact_iter(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result

# Versione ricorsiva
def my_fact_rec(n):
    if n == 0 or n == 1:  # caso base
        return 1
    return n * my_fact_rec(n - 1)  # caso ricorsivo

print(my_fact_iter(5))  # 120
print(my_fact_rec(5))   # 120
```
> **Come funziona la ricorsione:** `my_fact_rec(5)` chiama `my_fact_rec(4)`, che chiama `my_fact_rec(3)`... fino a `my_fact_rec(1)` che restituisce 1. Poi i risultati si "ripiegano" all'indietro: 1 × 2 × 3 × 4 × 5 = 120.
>
> **Attenzione allo stack:** ogni chiamata ricorsiva occupa spazio sullo stack. Python ha un limite di circa 1000 chiamate ricorsive per default (`sys.getrecursionlimit()`). Per input molto grandi, la versione iterativa è sempre preferibile.
---
## Errori e gestione delle eccezioni
> *💡 *In produzione un modello AI che crasha senza gestione degli errori è inutile. I pipeline ML hanno `try/except` ovunque: batch con dati corrotti, file mancanti, connessioni API che cadono, tensori con shape inattese.
Python distingue tre tipi di errori.
**Errori di sintassi (SyntaxError):** il codice non è scritto correttamente. Python li rileva prima ancora di eseguire il programma.
```python
if = 'nome'  # SyntaxError: 'if' è una keyword riservata
```
**Errori runtime (Exceptions):** il codice è sintatticamente corretto ma qualcosa va storto durante l'esecuzione.
<table header-row="true">
<tr>
<td>**Eccezione**</td>
<td>**Causa**</td>
</tr>
<tr>
<td>`ZeroDivisionError`</td>
<td>Divisione per zero</td>
</tr>
<tr>
<td>`IndexError`</td>
<td>Indice fuori range in una sequenza</td>
</tr>
<tr>
<td>`KeyError`</td>
<td>Chiave non esistente in un dizionario</td>
</tr>
<tr>
<td>`NameError`</td>
<td>Variabile non definita</td>
</tr>
<tr>
<td>`TypeError`</td>
<td>Operazione su tipi incompatibili</td>
</tr>
<tr>
<td>`ValueError`</td>
<td>Tipo giusto ma valore non valido</td>
</tr>
<tr>
<td>`AttributeError`</td>
<td>Metodo o attributo non esistente</td>
</tr>
<tr>
<td>`StopIteration`</td>
<td>Iteratore esaurito</td>
</tr>
</table>
**Errori semantici (logic errors):** il codice gira senza errori ma produce risultati sbagliati. Python non può rilevarli.
```python
# Errore semantico classico: input() restituisce str, non int
def somma():
    num1 = input('Primo: ')   # '12'
    num2 = input('Secondo: ') # '8'
    return num1 + num2        # '128' — concatenazione, non somma!
```
### try / except / else / finally
```python
try:
    denominatore = int(input('Denominatore: '))
    risultato = 10 / denominatore
except ZeroDivisionError:
    print('Non puoi dividere per zero')
except ValueError:
    print('Devi inserire un numero')
else:
    print(f'Risultato: {risultato}')  # eseguito solo se non ci sono eccezioni
finally:
    print('Eseguito sempre, con o senza eccezioni')
```
> **`else`** viene eseguito solo se il blocco `try` non ha sollevato eccezioni. **`finally`** viene eseguito sempre — utile per chiudere file o connessioni.
### Sollevare eccezioni personalizzate: *raise*
```python
try:
    conto = int(input('Conto: '))
    bonifico = int(input('Bonifico: '))
    if bonifico > conto:
        raise ValueError('Fondi insufficienti')
except ValueError as e:
    print(f'Errore: {e}')
else:
    conto -= bonifico
    print(f'Conto aggiornato: €{conto}')
```
> **Intercettare tutto:** `except:` senza specificare il tipo cattura qualsiasi eccezione. Non è una best practice — nasconde errori inattesi.
---
## Iterabili e iteratori
> 💡 In AI il collegamento è diretto: un dataset di training è un iterabile. In PyTorch il `DataLoader` è esattamente un iteratore su batch di dati — avanza un pezzo alla volta con `next()` implicito ad ogni step di training.
In Python, qualsiasi oggetto che può essere percorso con un `for` è un **iterabile**: `liste`, `tuple`, `set`, `stringhe`, `dizionari`, `range`.
Un **iteratore** è un oggetto che mantiene il suo stato mentre si percorre la sequenza. Si ottiene da un iterabile chiamando `iter()`.
Se un iterabile è come un libro, l'iteratore è il segnalibro: sa esattamente a che pagina sei, avanza di una posizione alla volta e non può tornare indietro. È l'equivalente Python di un cursore in un database — punta a un elemento alla volta e avanza solo in avanti.
```python
# Iterabile: una tupla di linguaggi di programmazione
linguaggi = ('Python', 'Java', 'JavaScript', 'C++')
for lang in linguaggi:
    print(lang)

# Dizionario studenti: iterare su chiavi, valori o coppie
studenti = {'Alice': 28, 'Bob': 24, 'Carlo': 31}
for nome in studenti:               # itera sulle chiavi
    print(nome)
for nome, eta in studenti.items():  # itera su coppie (chiave, valore)
    print(f"{nome} ha {eta} anni")

# dict_keys non è subscriptable
keys = studenti.keys()
# keys[0]  # TypeError: 'dict_keys' object is not subscriptable
# 'subscriptable' significa che l'oggetto supporta l'operatore []
# (come liste e tuple). dict_keys non lo supporta: va convertito in lista prima.
list(keys)[0]  # 'Alice' — OK
```
```python
# Iteratore esplicito su una tupla di linguaggi
it = iter(('Python', 'Java', 'C++'))

print(next(it))  # 'Python'
print(next(it))  # 'Java'
print(next(it))  # 'C++'
print(next(it))  # StopIteration — iteratore esaurito
```
> L'iteratore **ricorda la sua posizione** (come un cursore). Una volta esaurito non può essere riavvolto — bisogna crearne uno nuovo con `iter()`. Il `for` loop fa tutto questo automaticamente.
```python
# Convertire in lista
list(studenti.keys())  # ['Alice', 'Bob', 'Carlo']
```
---
## Modulo `array` (stdlib)
> 💡 I tensori di NumPy, PyTorch e TensorFlow sono l'evoluzione diretta di `array.array`: dati numerici dello stesso tipo in memoria contigua, senza l'overhead degli oggetti Python. La differenza di velocità tra un loop su una lista e un'operazione vettorizzata su un tensore — che può essere 100x o più — nasce esattamente da questo principio.
`array.array` è una struttura dati della libreria standard Python che offre array tipizzati monodimensionali. Più efficiente di una lista per dati numerici omogenei.
```python
import array

arr = array.array('i', [1, 2, 3, 4, 5])  # 'i' = signed int (32-bit)
print(arr)  # array('i', [1, 2, 3, 4, 5])
```
**Codici di tipo comuni:**
<table header-row="true">
<tr>
<td>**Codice**</td>
<td>**Tipo C**</td>
<td>**Dimensione**</td>
<td>**Esempio**</td>
</tr>
<tr>
<td>`'b'`</td>
<td>signed char</td>
<td>1 byte</td>
<td>`array.array('b', [-1, 0, 1])`</td>
</tr>
<tr>
<td>`'i'`</td>
<td>signed int</td>
<td>2–4 byte</td>
<td>`array.array('i', [10, 20, 30])`</td>
</tr>
<tr>
<td>`'l'`</td>
<td>signed long</td>
<td>4–8 byte</td>
<td>`array.array('l', [1000000, 2000000])`</td>
</tr>
<tr>
<td>`'q'`</td>
<td>signed long long</td>
<td>8 byte</td>
<td>`array.array('q', range(10**6))`</td>
</tr>
<tr>
<td>`'f'`</td>
<td>float</td>
<td>4 byte</td>
<td>`array.array('f', [1.5, 2.5, 3.14])`</td>
</tr>
<tr>
<td>`'d'`</td>
<td>double</td>
<td>8 byte</td>
<td>`array.array('d', [3.141592653589793])`</td>
</tr>
</table>
> **Attenzione all'overflow:** `'i'` su molte piattaforme è 32-bit. Elevare al quadrato 10\^6 interi produce valori \> 2\^31 — overflow garantito. Usare `'q'` (64-bit).
```python
# Overflow con 'i'
arr = array.array('i', range(10**6))
arr_squared = array.array('i', [x * x for x in arr])  # OverflowError!

# Corretto con 'q'
arr = array.array('q', range(10**6))
arr_squared = array.array('q', [x * x for x in arr])  # OK
```
> Il confronto con `numpy.array` e il relativo benchmark sono trattati nel **modulo 02 — NumPy**, dove NumPy viene introdotto in modo completo.
---
## Liste
Le liste sono sequenze ordinate **mutabili**. A differenza delle tuple, possono essere modificate dopo la creazione.
```python
L = ['I did it all', 4, 'love']
for e in L:
    print(e)

# Append muta la lista in-place
L.append(42)  # restituisce None, non una nuova lista
```
> **Attenzione all'aliasing:** `L.append(L)` aggiunge L a se stessa creando una lista ricorsiva `[..., [...]]`. Non è un errore ma raramente è quello che si vuole.
### List comprehension
> 💡 In data science è onnipresente: costruire feature set, filtrare campioni, applicare trasformazioni inline su colonne di un DataFrame.
La list comprehension è un modo conciso per costruire una lista applicando un'espressione a ogni elemento di un iterabile, con un filtro opzionale. È equivalente a un `for` loop con `append`, ma più leggibile e in molti casi più veloce.
Struttura generale:
```javascript
[espressione  for elemento in iterabile  if condizione]
```
- **`espressione`**: cosa mettere nella lista (può trasformare l'elemento)
- **`for elemento in iterabile`**: da dove prendere i valori
- **`if condizione`** (opzionale): filtro — solo gli elementi per cui la condizione è `True`
```python
# Equivalenza: loop classico vs comprehension
nomi = ['alice', 'bob', 'carlo']

# Loop classico
risultato = []
for n in nomi:
    risultato.append(n.upper())

# Comprehension — equivalente, più concisa
risultato = [n.upper() for n in nomi]  # ['ALICE', 'BOB', 'CARLO']
```
```python
# Filtro: solo i pari
pari = [x for x in range(20) if x % 2 == 0]

# Trasformazione + filtro
quadrati_pari = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]

# Loop annidato: tutte le coppie (x, y)
coppie = [(x, y) for x in range(3) for y in range(3)]

# Uso di _ per variabile ignorata
matrice = [[] for _ in range(5)]  # 5 liste vuote DISTINTE (non aliases)
```
> **Perché non ****`[[]] * 5`****?** `[[]] * 5` crea 5 riferimenti alla stessa lista — modificarne una modifica tutte. La comprehension crea 5 oggetti distinti. È uno degli errori più comuni tra i principianti Python.
---
## Set
> 💡 In NLP i set servono a costruire e deduplicare vocabolari — il vocabolario di un modello linguistico è un insieme di token unici. Nel preprocessing si usano per tracciare le categorie uniche di una variabile prima dell'encoding.
Collezioni non ordinate di elementi **unici** e **hashable**.
```python
baseball = {'Dodgers', 'Giants', 'Padres', 'Rockies'}
football = {'Giants', 'Eagles', 'Cardinals', 'Cowboys'}

baseball.add('Yankees')
football.update(['Patriots'])

print(baseball | football)    # unione
print(baseball & football)    # intersezione
print(baseball - football)    # differenza
print({'Padres'} <= baseball) # subset
```
> **Cos'è un oggetto hashable?** Un oggetto è hashable se ha un valore hash — un numero intero calcolato dal suo contenuto — che rimane costante per tutta la sua vita. Gli oggetti hashable sono sempre **immutabili**: `int`, `float`, `str`, `bool`, `tuple` (se contiene solo elementi hashable). Gli oggetti **mutabili** come `list` e `dict` non sono hashable perché il loro contenuto può cambiare. Se provi `{[1, 2]}` ottieni `TypeError: unhashable type: 'list'`.
---
## Funzioni built-in rilevanti
```python
# sum — solo su iterabili di numeri
sum([1, 2, 3])        # 6
sum((1, 2, 3), 10)    # 16 (start=10)

# zip — combina iterabili element-wise
names = ['Alice', 'Bob']
ages = [25, 30]
list(zip(names, ages))  # [('Alice', 25), ('Bob', 30)]

# min / max
min(3, 7, 1)    # 1
max([4, 2, 9])  # 9
```
---
## Ricerca lineare e binaria
> 💡 La complessità degli algoritmi di ricerca è direttamente rilevante in AI: KNN (K-Nearest Neighbors) fa una ricerca lineare su tutto il dataset per ogni predizione, il che lo rende inutilizzabile su dataset grandi senza strutture dati apposite come KD-tree o ball tree.
> Questa sezione introduce gli algoritmi di ricerca come primo esempio pratico del modulo `array`. L'analisi della complessità (O(n), O(log n)) e il confronto con Selection Sort sono approfonditi nel **modulo 08 — Ricorsione e Big O**.
### Ricerca lineare
Scorre l'array dall'inizio alla fine. Funziona su qualsiasi array, ordinato o no.
```python
import array

arr = array.array('i', [10, 20, 30, 50, 60, 80, 110, 130, 140, 170])

def linear_search(seq, target):
    for i in range(len(seq)):
        if seq[i] == target:
            return i
    return -1

print(linear_search(arr, 140))  # 8
print(linear_search(arr, 130))  # 7
```
### Ricerca binaria
Richiede un array **ordinato**. Ad ogni passo dimezza lo spazio di ricerca confrontando con il valore centrale.
**Versione iterativa:**
```python
def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

arr = [2, 3, 4, 10, 40]
print(binary_search(arr, 10))  # 3
```
**Versione ricorsiva:**
```python
def binary_search_rec(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_rec(arr, low, mid - 1, x)
        else:
            return binary_search_rec(arr, mid + 1, high, x)
    return -1

print(binary_search_rec(arr, 0, len(arr) - 1, 10))  # 3
```
---
## Input e validazione
```python
name = input("Come ti chiami? ")
print(type(name))  # <class 'str'>

anni = int(input("Quanti anni hai? "))  # ValueError se non numerico
```
**Pattern robusto con validazione:**
```python
def chiedi_intero(prompt, min_val, max_val):
    while True:
        try:
            valore = int(input(prompt))
            if min_val <= valore <= max_val:
                return valore
            print(f"Inserisci un valore tra {min_val} e {max_val}.")
        except ValueError:
            print("Inserisci un numero intero valido.")
```
---
## Misurazione del tempo
> 💡 In AI la latenza di inferenza è un requisito reale: quanto tempo impiega il modello a fare una predizione? Questi strumenti servono esattamente a misurarlo e ottimizzarlo prima di mandare un modello in produzione.
### `datetime` — semplice ma impreciso
```python
from datetime import datetime

init_time = datetime.now()
a = 0
for i in range(10000):
    a += i
fin_time = datetime.now()
print("Execution time:", fin_time - init_time)
```
> `datetime.now()` misura il **wall clock** — cioè il tempo reale trascorso "sull'orologio a muro", come lo vedi tu. Il problema è che il sistema operativo può interrompere il tuo processo in qualsiasi momento per eseguire altri task, aggiungendo rumore alla misurazione. Va bene per misurazioni grossolane, non per benchmark precisi.
### `timeit` — il modo corretto
`timeit` esegue il codice più volte e restituisce il tempo minimo, eliminando il rumore del sistema operativo.
```python
from timeit import repeat
from random import randint

def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""
    stmt = f"{algorithm}({array})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    print(f"Algorithm: {algorithm}. Minimum time: {min(times):.6f}s")

array = [randint(0, 1000) for _ in range(10000)]
run_sorting_algorithm(algorithm="sorted", array=array)
# Algorithm: sorted. Minimum time: 0.007718s
```
`repeat(setup, stmt, repeat, number)` esegue `stmt` per `number` volte di fila, ripete l'intera misurazione `repeat` volte, e restituisce una lista di `repeat` valori — ciascuno è il tempo totale delle `number` esecuzioni. I parametri principali:
- **`stmt`**: il codice da misurare (stringa)
- **`setup`**: codice eseguito una volta prima di ogni blocco di misurazioni — tipicamente un import o la definizione della funzione da testare
- **`number`**: quante volte eseguire `stmt` per ogni misurazione (default 1.000.000 — abbassarlo per codice lento)
- **`repeat`**: quante misurazioni indipendenti fare (default 5) — produce una lista di `repeat` valori
> **Perché il minimo e non la media?** Le misurazioni sono rumorose perché il sistema esegue altri processi in parallelo. Il tempo minimo è il meno rumoroso e il più rappresentativo del runtime reale dell'algoritmo.
---
## Logging
> 💡 Qualsiasi training run seria usa logging strutturato per tracciare loss, accuracy e learning rate ad ogni epoch. Tool come MLflow, Weights & Biases e TensorBoard si appoggiano tutti su questo pattern.
Il modulo `logging` della stdlib è la soluzione standard per scrivere log strutturati su file o console. Preferibile ai `print` in qualsiasi codice che va in produzione.
```python
import logging

Log_Format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(
    filename="logfile.log",
    filemode="w",
    format=Log_Format,
    level=logging.ERROR
)

logger = logging.getLogger()
logger.error("Messaggio di errore")
logger.warning("Questo non viene scritto se level=ERROR")
```
**Livelli di log (dal meno al più grave):**
<table header-row="true">
<tr>
<td>**Livello**</td>
<td>**Uso**</td>
</tr>
<tr>
<td>`DEBUG`</td>
<td>Informazioni dettagliate per il debug</td>
</tr>
<tr>
<td>`INFO`</td>
<td>Conferma che le cose funzionano</td>
</tr>
<tr>
<td>`WARNING`</td>
<td>Qualcosa di inatteso, ma il programma continua</td>
</tr>
<tr>
<td>`ERROR`</td>
<td>Un errore serio, funzionalità compromessa</td>
</tr>
<tr>
<td>`CRITICAL`</td>
<td>Errore grave, il programma potrebbe non continuare</td>
</tr>
</table>
---
## Big O notation
> 💡* In AI la complessità algoritmica guida scelte concrete: KNN è O(n) per ogni predizione e scala male su dataset grandi; K-Means ha complessità che dipende dal numero di iterazioni e cluster. Scegliere l'algoritmo giusto per la scala del problema richiede di conoscere la sua Big O.*
> Approfondimento completo nel **modulo 08 — Ricorsione e Big O**, insieme a Selection Sort e al confronto con il Timsort built-in.
La **Big O** esprime come cresce il numero di operazioni di un algoritmo al crescere dell'input n, indipendentemente dall'hardware.
<table header-row="true">
<tr>
<td>**Notazione**</td>
<td>**Nome**</td>
<td>**Esempio**</td>
</tr>
<tr>
<td>O(1)</td>
<td>Costante</td>
<td>Accesso a un elemento per indice</td>
</tr>
<tr>
<td>O(log n)</td>
<td>Logaritmica</td>
<td>Binary search</td>
</tr>
<tr>
<td>O(n)</td>
<td>Lineare</td>
<td>Linear search, scansione lista</td>
</tr>
<tr>
<td>O(n log n)</td>
<td>Linearitmica</td>
<td>Merge sort, Timsort (built-in Python)</td>
</tr>
<tr>
<td>O(n²)</td>
<td>Quadratica</td>
<td>Bubble sort, Insertion sort</td>
</tr>
</table>
---
## Programmazione funzionale — riduzioni
> 💡 I framework ML moderni sono costruiti su questo paradigma. JAX (Google) è fondato interamente su trasformazioni funzionali pure. `map`, `filter` e `reduce` sono i mattoni del preprocessing in tutto l'ecosistema data science.
La **programmazione funzionale** è uno stile che privilegia funzioni pure, senza effetti collaterali. Un pattern fondamentale è la **riduzione**: collassare una sequenza in un singolo valore.
```python
import random
from functools import reduce

valori = [random.randint(0, 100) for _ in range(10)]

print(min(valori))
print(max(valori))
print(sum(valori))

prodotto = reduce(lambda a, b: a * b, valori)

import statistics
print(statistics.mean(valori))
print(statistics.variance(valori))
print(statistics.stdev(valori))
```
> `min`, `max`, `sum`, `mean`, `variance`, `stdev` sono tutti esempi di **riduzione** — un concetto della programmazione funzionale. Questo stile rende il codice più conciso e più facile da debuggare rispetto ai loop espliciti.
---
## Riferimenti
- [Python docs — array](https://docs.python.org/3/library/array.html)
- [Python docs — built-in functions](https://docs.python.org/3/library/functions.html)
- [Python docs — data structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Python docs — logging](https://docs.python.org/3/library/logging.html)
- [Python docs — timeit](https://docs.python.org/3/library/timeit.html)
- [Sorting algorithms in Python](https://realpython.com/sorting-algorithms-python/)
