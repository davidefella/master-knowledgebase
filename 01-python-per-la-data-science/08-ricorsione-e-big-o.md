# 08 - Ricorsione e Big O

> Fonte Notion: https://app.notion.com/p/33612abc808d817e832df851add2386c — ultima modifica 2026-04-02T15:22:17.923Z

La ricorsione è una tecnica in cui una funzione chiama se stessa, direttamente o indirettamente tramite altre funzioni. Emerge naturalmente quando un problema ha una struttura auto-simile: il caso base risolve il caso triviale, il passo ricorsivo riduce il problema a una versione più piccola di se stesso.
---
## Ricorsione
### Fattoriale — versione iterativa vs ricorsiva
Il corso introduce la ricorsione partendo dal fattoriale con un'implementazione **iterativa**:
```python
def my_fact(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result

print(my_fact(5))  # 120
```
La versione **ricorsiva** equivalente — che il corso non mostra ma che è la forma canonica — è:
```python
def fact_recursive(n):
    if n == 0:          # caso base
        return 1
    return n * fact_recursive(n - 1)   # passo ricorsivo

print(fact_recursive(5))  # 120
```
> **Caso base obbligatorio.** Ogni funzione ricorsiva deve avere almeno un caso base (condizione di uscita). Senza di esso la ricorsione procede all'infinito fino al `RecursionError: maximum recursion depth exceeded`.
### Stack delle chiamate
Ogni chiamata ricorsiva occupa un frame nello stack. Per `fact_recursive(5)`:
```javascript
fact(5) → 5 * fact(4)
               fact(4) → 4 * fact(3)
                              fact(3) → 3 * fact(2)
                                             fact(2) → 2 * fact(1)
                                                            fact(1) → 1 * fact(0)
                                                                           fact(0) → 1  ← caso base
```
Il risultato viene propagato verso l'alto mentre lo stack si svuota.
> **Limite di Python.** Il limite di default dello stack in CPython è 1000 frame (`sys.getrecursionlimit()`). Per problemi grandi conviene usare la versione iterativa o tecniche come la tail recursion (non ottimizzata da CPython) o la memoizzazione.
### Quando usare la ricorsione
La ricorsione è utile quando la struttura del problema è intrinsecamente ricorsiva: alberi, grafi, divide-et-impera, backtracking. Per sequenze lineari semplici (come il fattoriale), l'approccio iterativo è preferibile in Python per ragioni di efficienza e leggibilità.
---
## Big O — notazione asintotica
### Cos'è
La notazione Big O descrive come cresce il tempo di esecuzione (o lo spazio in memoria) di un algoritmo **al crescere della dimensione dell'input** `n`. Si ignora tutto ciò che non è dominante:
- **Costanti:** `3n` → `O(n)`
- **Termini di ordine inferiore:** `n² + n` → `O(n²)`
L'obiettivo è caratterizzare il comportamento nel **caso peggiore** (worst case) al tendere di `n` a infinito.
### Complessità comuni
<table header-row="true">
<tr>
<td>Notazione</td>
<td>Nome</td>
<td>Esempio tipico</td>
</tr>
<tr>
<td>`O(1)`</td>
<td>Costante</td>
<td>Accesso a elemento per indice</td>
</tr>
<tr>
<td>`O(log n)`</td>
<td>Logaritmica</td>
<td>Binary search</td>
</tr>
<tr>
<td>`O(n)`</td>
<td>Lineare</td>
<td>Iterazione su lista</td>
</tr>
<tr>
<td>`O(n log n)`</td>
<td>Linearitmica</td>
<td>Merge sort, Heap sort</td>
</tr>
<tr>
<td>`O(n²)`</td>
<td>Quadratica</td>
<td>Selection sort, Bubble sort</td>
</tr>
<tr>
<td>`O(2ⁿ)`</td>
<td>Esponenziale</td>
<td>Subset enumeration</td>
</tr>
</table>
### Esempio — Selection Sort: O(n²)
Il corso mostra il Selection Sort. L'implementazione contiene **un bug**: il parametro di `swapPositions` dovrebbe essere l'indice `jpos`, non il valore `SmallestElement`. Versione corretta con analisi:
```python
def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):                # ciclo esterno: n-1 iterazioni
        min_idx = i
        for j in range(i + 1, n):         # ciclo interno: n-i-1 iterazioni
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]   # swap
    return lst

lst = [1, 5, 3, 78, 6, 9, 14, 0, 15]
print(selection_sort(lst))   # [0, 1, 3, 5, 6, 9, 14, 15, 78]
```
**Analisi della complessità:**
Il ciclo interno esegue `(n-1) + (n-2) + ... + 1 = n(n-1)/2` operazioni.
```javascript
n(n-1)/2 = n²/2 - n/2
```
Si scartano il coefficiente `1/2` e il termine `n/2` (ordine inferiore) → **`O(n²)`**.
> **Confronto con ****`list.sort()`****.** Il metodo built-in di Python usa Timsort (ibrido merge sort + insertion sort), con complessità `O(n log n)` nel caso medio/peggiore. Per qualsiasi uso pratico, `list.sort()` è sempre da preferire al Selection Sort.
### Come calcolare il Big O in pratica
1. Identifica i loop e le loro dipendenze da `n`.
2. Loop annidati indipendenti → **moltiplica** le complessità.
3. Loop sequenziali → **somma** e tieni il termine dominante.
4. Ricorsione → applica il **Master Theorem** o espandi l'albero delle chiamate.
---
## Note critiche sul materiale del corso
> Il codice di `SelectionSort` nel notebook contiene un errore: `swapPositions(List, SmallestElement, i)` passa il **valore** `SmallestElement` invece dell'**indice** `jpos`. Il risultato stampato nel notebook è parzialmente ordinato per coincidenza dei valori, non per logica corretta.
---
## Riferimenti
- [Python — sys.getrecursionlimit](https://docs.python.org/3/library/sys.html#sys.getrecursionlimit)
- [Big O — freeCodeCamp](https://www.freecodecamp.org/news/big-o-notation-why-it-matters-and-why-it-doesnt-1674cfa8a23c/)
- [Timsort — Wikipedia](https://en.wikipedia.org/wiki/Timsort)
