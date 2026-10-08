# 09 - Eccezioni, timeit e iteratori

> Fonte Notion: https://app.notion.com/p/33612abc808d814f99bfe8025d335fbe — ultima modifica 2026-04-02T15:23:05.596Z

Questo modulo copre tre strumenti fondamentali della programmazione Python avanzata: la gestione strutturata degli errori, la misurazione delle performance e il protocollo degli iteratori.
---
## Tipi di errore in Python
Python distingue tre categorie di errori:
**Errori di sintassi (SyntaxError)**
Rilevati prima dell'esecuzione, durante il parsing. Il programma non parte.
```python
if = 'alessandro'   # SyntaxError: 'if' è una keyword riservata
```
**Errori di runtime (eccezioni)**
Si verificano durante l'esecuzione. Il programma si interrompe se non gestiti.
<table header-row="true">
<tr>
<td>Eccezione</td>
<td>Causa tipica</td>
</tr>
<tr>
<td>`AttributeError`</td>
<td>Metodo o attributo inesistente su un oggetto</td>
</tr>
<tr>
<td>`IndexError`</td>
<td>Indice fuori range su sequenza</td>
</tr>
<tr>
<td>`KeyError`</td>
<td>Chiave inesistente in un dizionario</td>
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
<td>`ZeroDivisionError`</td>
<td>Divisione per zero</td>
</tr>
<tr>
<td>`StopIteration`</td>
<td>Iteratore esaurito (vedi sezione Iteratori)</td>
</tr>
</table>
**Errori semantici (logici)**
Il codice esegue senza errori ma produce risultati sbagliati. Il più insidioso dei tre.
```python
def somma():
    num1 = input('Primo addendo: ')
    num2 = input('Secondo addendo: ')
    return num1 + num2   # bug: input() restituisce str, + concatena invece di sommare

# Output: '1212' invece di 24
```
---
## Gestione eccezioni: try / except / else / finally / raise
### Struttura completa
```python
try:
    # codice che potrebbe sollevare un'eccezione
except TipoEccezione:
    # eseguito se si verifica TipoEccezione
except (AltroTipo, AncorUnAltro):
    # cattura più tipi in un'unica clausola
except:  # except default — cattura tutto
    # va messo per ultimo
else:
    # eseguito solo se NON si è verificata nessuna eccezione nel try
finally:
    # eseguito sempre, con o senza eccezione (cleanup, chiusura file, ecc.)
```
### Esempio: divisione con input utente
```python
try:
    denominatore = int(input('Denominatore = '))
    risultato = 10 / denominatore
    print(risultato)
except ZeroDivisionError:
    print('Non è possibile dividere per zero')
except ValueError:
    print('Non è possibile dividere per una lettera')
```
> **Ordine delle clausole.** Python valuta gli `except` in sequenza e cattura la prima corrispondenza. La clausola `except` senza tipo (catch-all) deve essere **l'ultima**, altrimenti cattura tutto e le clausole specifiche successive non vengono mai raggiunte.
### raise — sollevare eccezioni esplicitamente
Talvolta Python non solleva un'eccezione dove la logica del dominio lo richiederebbe. In questi casi si usa `raise`:
```python
try:
    conto = int(input('Conto = '))
    bonifico = int(input('Bonifico = '))
    if bonifico > conto:
        raise ValueError('Saldo insufficiente')
except ValueError as e:
    print(f'Errore: {e}')
else:
    conto -= bonifico
    print(f'Conto = € {conto}')
```
> `raise` può rilanciare eccezioni esistenti (`raise`) o sollevarne di nuove (`raise TipoEccezione(messaggio)`). Si possono definire eccezioni custom estendendo `Exception`.
---
## timeit — misurazione del tempo di esecuzione
`timeit` esegue un frammento di codice un numero elevato di volte (default: 1.000.000) e restituisce il tempo totale. È progettato per misurare **microperformance** in modo affidabile, isolando l'esecuzione da interferenze del GC e del sistema.
### Interfaccia funzionale
```python
import timeit

# timeit.timeit(stmt, setup, timer, number)
# - stmt: codice da misurare (stringa o callable)
# - setup: codice eseguito UNA VOLTA prima (import, ecc.)
# - number: quante volte eseguire stmt (default: 1.000.000)

t = timeit.timeit(stmt='a=10; b=10; s=a+b')
print(f"Tempo: {t:.4f} s")   # es. 0.0335 s (su 1M iterazioni)
```
### timeit.repeat — più esecuzioni per stabilità statistica
```python
import timeit

setup = 'import random'
code = '''
def test():
    return random.randint(10, 100)
test()
'''

risultati = timeit.repeat(stmt=code, setup=setup)
# Restituisce una lista di 5 valori (default: repeat=5)
# es. [1.09, 1.02, 1.07, 1.01, 1.03]
print(min(risultati))   # il minimo è la stima più affidabile
```
> **Perché usare ****`min()`****?** Secondo la documentazione ufficiale, il valore minimo è la stima più rappresentativa: i valori più alti riflettono interferenze esterne (scheduling OS, GC), non il codice misurato.
### Uso corretto con try/except
```python
import timeit

t = timeit.Timer('a=10; b=10; s=a+b')   # Timer è la classe sottostante
try:
    print(t.timeit())
except Exception:
    t.print_exc()   # stampa il traceback formattato
```
---
## Iteratori e iterabili
### Distinzione fondamentale
<table header-row="true">
<tr>
<td>Concetto</td>
<td>Descrizione</td>
<td>Esempi</td>
</tr>
<tr>
<td>**Iterabile**</td>
<td>Oggetto su cui si può iterare con `for`</td>
<td>lista, tupla, set, dict, `range()`, stringa</td>
</tr>
<tr>
<td>**Iteratore**</td>
<td>Oggetto che ricorda la posizione corrente nell'iterazione</td>
<td>`iter(lista)`, `dict_keyiterator`</td>
</tr>
</table>
Un iterabile non è necessariamente un iteratore. La distinzione è nel protocollo:
- Iterabile: implementa `__iter__()` → restituisce un iteratore
- Iteratore: implementa sia `__iter__()` che `__next__()`
### Il protocollo degli iteratori
```python
filled_dict = {'uno': 1, 'due': 2, 'tre': 3}

# dict.keys() è un iterabile, non un iteratore
our_iterable = filled_dict.keys()    # dict_keys object

# Non è subscriptable (non si accede per indice)
# our_iterable[0]  → TypeError: 'dict_keys' object is not subscriptable

# iter() crea un iteratore dall'iterabile
our_iterator = iter(our_iterable)    # dict_keyiterator

# next() avanza l'iteratore e restituisce il prossimo elemento
print(next(our_iterator))   # 'uno'
print(next(our_iterator))   # 'due'
print(next(our_iterator))   # 'tre'

# Quando l'iteratore è esaurito, solleva StopIteration
next(our_iterator)           # StopIteration!
```
> Il ciclo `for` usa internamente `iter()` e `next()` e cattura `StopIteration` automaticamente. Raramente serve chiamarli a mano, ma comprendere il protocollo è essenziale per scrivere classi iterabili custom e capire come funzionano generator e lazy evaluation.
### Materializzare un iteratore
```python
# list() consuma tutto l'iteratore e restituisce una lista
list(filled_dict.keys())   # ['uno', 'due', 'tre']
```
### Iterazione su dizionario — forma compatta
```python
for chiave in filled_dict:      # itera sulle chiavi
    print(chiave)

for k, v in filled_dict.items():  # itera su coppie (chiave, valore)
    print(k, v)
```
---
## Riferimenti
- [Python — Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [Python — timeit](https://docs.python.org/3/library/timeit.html)
- [Python — Iterator Types](https://docs.python.org/3/library/stdtypes.html#iterator-types)
