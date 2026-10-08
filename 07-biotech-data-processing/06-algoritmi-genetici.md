# 06 - Algoritmi genetici

> Fonte Notion: https://app.notion.com/p/3e912abc808d8160b313e76796ef3136 — ultima modifica 2026-09-28T18:32:02.434Z

**Registrazione:** `BT-06` (portale, edizione 2025), durata 01:01:23. Giornata: **Day 7** (slide "Biologia per la ricerca di soluzioni ottime: Algoritmi Genetici, Matteo Rucco - Day 7").
**Materiale:** nessun PDF delle slide e nessun notebook fra i materiali (portale e Teams): slide e codice di `tsp_genetic_algorithm_with_comments.ipynb` sono ricostruiti dai fotogrammi. Le celle di selezione, crossover e mutazione scorrono in pochi secondi (`BT-06 @ 00:58:46`): sono state lette da fotogrammi estratti apposta dal video.
**Teams 2026:** nessuna registrazione 2026 copre gli algoritmi genetici (vedi Divergenze). La lettura della traccia del test annunciata a fine lezione non è nella registrazione; per il test 2026 vedi **Assessment**.
> **Nota sul codice.** Il codice del notebook è verificato per esecuzione (`verifica_bt06.py`), insieme all'ottimo esatto per forza bruta sulle stesse 10 città. I risultati numerici del GA dipendono dal modulo `random`, che nel notebook non ha seed: non sono riproducibili (sezione 9).
## Indice
1. Obiettivo della lezione
2. Basi biologiche
3. Ottimo globale e locale, metaeuristiche
4. Gli algoritmi genetici: definizione e schema
5. Rappresentazione delle soluzioni
6. Selezione, crossover, mutazione, aggiornamento
7. La funzione di fitness
8. Quando usare e quando non usare un GA; applicazioni
9. Il problema del commesso viaggiatore (TSP) in Colab
10. Collegamento con il test finale
11. Glossario, punti incerti, materiale usato
---
## 1. Obiettivo della lezione
`BT-06 @ 00:00:09`
Lezione volutamente compatta, per lasciare tempo al notebook Python e alla lettura della traccia del test finale (`BT-06 @ 00:00:40`). Tema: usare i principi dell'**evoluzione biologica** per risolvere problemi complessi di **ottimizzazione**, in particolare gli algoritmi genetici applicati al **problema del commesso viaggiatore** (`BT-06 @ 00:01:11`). Rispetto alla lezione precedente (capitolo 05), dove l'informatica risolveva problemi biologici, qui è la biologia a ispirare metodi informatici (`BT-06 @ 00:01:49`).
Slide "Argomenti della lezione" (`BT-06 @ 00:02:23`): introduzione, caratteristiche della procedura, i passi della procedura (in pseudocodice), considerazioni generali su efficacia e applicazioni; poi esercitazione in Colab.
## 2. Basi biologiche
`BT-06 @ 00:02:53`
Slide "Basi biologiche degli algoritmi genetici":
- l'evoluzione di una popolazione è legata al processo di **riproduzione**: gli individui (genitori) si accoppiano e producono nuovi individui (figli) il cui patrimonio genetico è una **combinazione** di quello dei genitori (`BT-06 @ 00:03:27`);
- i figli subiscono **mutazioni** rispetto al patrimonio ereditato, per effetto della vita di relazione e delle influenze dell'ambiente;
- la **selezione naturale** si basa sul principio che, fra gli individui generati, hanno maggiori probabilità di sopravvivere quelli con una **fitness** migliore (`BT-06 @ 00:04:41`).
Il figlio non è un clone: eredita componenti dei due genitori, più ricombinazioni e mutazioni che gli danno un'identità genetica propria. Le mutazioni non sono per forza dannose: sono un fenomeno naturale; la maggior parte avviene nella fase iniziale, altre durante la vita (`BT-06 @ 00:04:02`). La fitness, nell'algoritmo, è ciò che lo personalizza sul problema da risolvere (`BT-06 @ 00:05:18`).
## 3. Ottimo globale e locale, metaeuristiche
`BT-06 @ 00:05:52`
I problemi complessi che interessano qui sono **problemi di ottimo**: ricerca di massimi e minimi globali e locali. Slide "Massimo/Minimo globale e locale" (`BT-06 @ 00:06:29`):
- per problemi computazionalmente complessi (**NP-hard**) servono tecniche **euristiche**;
- le tecniche **costruttive** individuano (costruiscono) una soluzione ammissibile;
- le tecniche **migliorative** (ricerca locale) partono da una soluzione ammissibile e la migliorano applicando iterativamente una mossa; convergono in un **ottimo locale**;
- per migliorare la qualità delle soluzioni si usano le **metaeuristiche**.
> **Correzione:** a voce i problemi "NP" sono "non polinomiali" (`BT-06 @ 00:05:52`). NP sta per *nondeterministic polynomial time*: problemi le cui soluzioni si verificano in tempo polinomiale. Per i problemi **NP-hard**, come il TSP, non è noto un algoritmo esatto in tempo polinomiale.
Le metaeuristiche, come gli algoritmi genetici, esplorano più ampiamente lo spazio delle soluzioni e aumentano la probabilità di trovare l'ottimo globale; generano iterativamente soluzioni, e quelle che non soddisfano i criteri non vengono scartate ma fanno da punto di partenza (`BT-06 @ 00:07:09`). Come in Darwin, si parte dal passato per procedere nella scala evolutiva.
Slide "Tecniche di ricerca di soluzioni ottime" (`BT-06 @ 00:07:44`), albero:
- *calculus-based techniques*: metodi diretti (Fibonacci) e indiretti (Newton);
- *guided random search techniques*: *evolutionary algorithms* (evolutionary strategies, **genetic algorithms**: parallel, centralized o distributed; sequential, steady-state o generational) e *simulated annealing*;
- *enumerative techniques*: *dynamic programming*.
(Sulla slide "Finonacci" per Fibonacci.) Gli algoritmi genetici rientrano fra le strategie evolutive e le tecniche di ricerca guidata casuale, efficaci per la capacità di combinare ed esplorare soluzioni diverse (`BT-06 @ 00:08:19`). Altre tecniche: simulated annealing, programmazione dinamica; se il problema si scompone in sottosoluzioni indipendenti, gli algoritmi **greedy** (`BT-06 @ 00:08:58`).
> **Correzione:** a voce il simulated annealing è fra gli approcci "implementati attraverso il quantum computing" (`BT-06 @ 00:08:19`). Il simulated annealing è un algoritmo classico (Kirkpatrick, Gelatt e Vecchi, 1983), ispirato alla ricottura dei metalli. Con il quantum computing si discute di *quantum annealing*, una tecnica diversa.
Invito del docente, valido anche per la modellazione ad agenti (`BT-06 @ 00:09:28`): **non partire dall'algoritmo o dalla soluzione, ma decomporre e capire il problema**. Se il problema è risolvibile in tempo polinomiale, magari con un grado stimato in notazione O grande, probabilmente un algoritmo genetico non serve (`BT-06 @ 00:10:10`).
## 4. Gli algoritmi genetici: definizione e schema
`BT-06 @ 00:10:40`
Slide "Gli algoritmi genetici (GA)": algoritmi di ricerca basati sulla meccanica dell'evoluzione biologica.
- Sviluppati da **John Holland**, Università del Michigan (anni '70), per comprendere i processi adattivi dei sistemi naturali e progettare software per sistemi artificiali che ne mantengano la robustezza.
- Sono una tecnica **metaeuristica** basata sull'analogia con la selezione naturale.
- Idea di base: una **popolazione di soluzioni** che evolve con un meccanismo di selezione, per produrre soluzioni con buoni valori della funzione obiettivo.
Non si genera una soluzione alla volta ma un insieme; quelle con fitness maggiore sono più vicine all'ottimo, le altre vengono scartate; le soluzioni intermedie evolvono e si ricombinano (`BT-06 @ 00:11:15`).
Slide "I passi della procedura" (`BT-06 @ 00:11:47`), flusso iterativo: generazione della popolazione iniziale → selezione → riproduzione (crossover) → mutazione → controllo della fitness; se il controllo non è superato si ripete, altrimenti termine dell'ottimizzazione. Elementi chiave: la **codifica** delle soluzioni, la generazione della popolazione iniziale con la sua valutazione di fitness (`BT-06 @ 00:12:19`), il confronto della fitness con una soglia o un criterio di arresto (`BT-06 @ 00:12:55`), la selezione di coppie a cui applicare gli **operatori genetici** crossover e mutazione, la rivalutazione dei figli (`BT-06 @ 00:13:25`).
Slide "Simple Genetic Algorithm" (`BT-06 @ 00:13:59`):
```plain text
initialize population;
evaluate population;
while TerminationCriteriaNotSatisfied
    select parents for reproduction;
    perform recombination and mutation;
    evaluate population;
```
Pochi passi. Per il docente i GA, che alcuni tengono fuori dal machine learning e altri includono, esprimono comunque una forma di apprendimento automatico per i meccanismi di ricombinazione, mutazione e selezione (`BT-06 @ 00:14:34`).
## 5. Rappresentazione delle soluzioni
`BT-06 @ 00:15:51`
Ogni soluzione è un **cromosoma** (o individuo); la rappresentazione dipende dal problema (`BT-06 @ 00:16:21`):
- **binaria**: sequenza di bit, fra le più diffuse, per variabili discrete o booleane. Esempio: per ottimizzare $`f(x)`$, $`x = 13`$ si codifica come `1101` (`BT-06 @ 00:16:58`; verificato). Cambiare uno o pochi bit può produrre una grande variazione del numero codificato (`BT-06 @ 00:17:30`);
- **numeri reali**: per variabili continue, ogni gene è un valore numerico (`BT-06 @ 00:18:02`);
- **permutazioni**: per problemi combinatori come il TSP; il cromosoma è una sequenza ordinata. Con cinque città A, B, C, D, E un cromosoma è `(C, A, B, E, D)`; scambiare due lettere scambia l'ordine di visita (`BT-06 @ 00:18:36`);
- **stringhe simboliche**: ogni gene è un simbolo che rappresenta una regola o un'azione (per esempio `R1 R2 R5`); utili per sistemi di classificazione (`BT-06 @ 00:19:40`);
- **alberi**: liste di regole o alberi che codificano un programma o una funzione (`BT-06 @ 00:20:52`);
- rappresentazioni **ibride**, secondo la complessità (`BT-06 @ 00:21:25`).
Le più diffuse sono binaria e per permutazione. Terminologia (`BT-06 @ 00:21:25`): il **gene** è un elemento della soluzione (bit, numero, regola, simbolo); il **cromosoma** è la sequenza completa di geni che rappresenta una soluzione (es. `0010011`); la **popolazione** è l'insieme dei cromosomi. Slide "Generazione di nuove soluzioni" (`BT-06 @ 00:24:59`): "Genotipo: generalmente una stringa binaria di lunghezza fissa", con l'esempio `0010011` e un vettore reale `x[0]=0.9, x[1]=1.5, ..., x[N]=0.3`.
Una buona rappresentazione (`BT-06 @ 00:22:31`) è semplice da manipolare, sia per chi segue l'evoluzione sia per gli operatori di crossover e mutazione, e copre bene lo spazio delle soluzioni. Esempio: con più di 21-22 città l'alfabeto non basta e servirebbero coppie di lettere, che complicano gli operatori (`BT-06 @ 00:23:01`); una codifica binaria per il TSP richiederebbe sottostringhe di lunghezza uguale per ogni città, complicando le cose (`BT-06 @ 00:24:08`). In sintesi: dal problema e dal suo spazio delle soluzioni si sceglie la codifica (`BT-06 @ 00:24:42`).
## 6. Selezione, crossover, mutazione, aggiornamento
`BT-06 @ 00:25:18`
**Selezione dei genitori** (slide: "I genitori vengono selezionati in modo casuale e le probabilità di selezione sono influenzate dalle valutazioni cromosomiche", `BT-06 @ 00:25:50`):
- **roulette**: probabilità di selezione proporzionale alla fitness (`BT-06 @ 00:26:29`);
- **tournament selection**: si estrae un sottoinsieme di individui e il migliore diventa genitore (`BT-06 @ 00:27:00`);
- **rank selection**: individui ordinati per fitness, probabilità proporzionale al rango e non al valore assoluto;
- **elitismo**: alcuni individui passano direttamente alla generazione successiva per preservare le soluzioni migliori; per il docente è più rischioso perché espone agli ottimi locali (`BT-06 @ 00:27:36`). Le più usate sono roulette e torneo, soprattutto la roulette (`BT-06 @ 00:28:11`).
> **Correzione:** a voce la pallina cade su "37 o 38 quadranti, in base se giochiamo alla roulette russa o a quella francese" (`BT-06 @ 00:26:29`). La roulette **francese/europea** ha 37 caselle (0-36), quella **americana** 38 (con il doppio zero); la "roulette russa" non è un gioco da casinò.
> **Nota aggiunta:** l'elitismo riduce la diversità se applicato a molti individui, ma con uno o pochi individui garantisce che la migliore soluzione trovata non vada persa. Il notebook della sezione 9 non lo usa, e la miglior distanza oscilla da una generazione all'altra: con un solo individuo elitario raggiunge l'ottimo (verificato).
**Crossover** (`BT-06 @ 00:28:41`): combina il materiale genetico di due genitori, simulando la riproduzione sessuata:
- **a punto singolo**: un punto casuale; i geni prima vengono da un genitore, quelli dopo dall'altro;
- **a due punti**: il segmento fra due punti viene scambiato fra i genitori;
- **uniforme**: per ogni gene si sceglie a caso il genitore che lo fornisce (`BT-06 @ 00:29:16`);
- **personalizzato**: operatori che rispettano la natura della soluzione, spesso basati su permutazioni, come quello usato per il TSP (`BT-06 @ 00:29:46`).
**Mutazione** (`BT-06 @ 00:30:18`): senza, dopo poche iterazioni i figli avrebbero tutti lo stesso cromosoma (quanto presto dipende da popolazione e genitori); la mutazione introduce variazioni casuali per garantire **diversità** e prevenire la **convergenza prematura** verso un ottimo locale (`BT-06 @ 00:30:49`). Immagine del docente: una pallina ferma in un minimo locale, a cui si danno "martellate" per farla uscire dalla gola e raggiungere il minimo globale (`BT-06 @ 00:31:24`). Tecniche simili di perturbazione esistono nel machine learning, per esempio sul learning rate delle reti neurali (`BT-06 @ 00:31:54`). Tipi:
- **binaria**: si inverte un bit;
- **continua**: si aggiunge un piccolo valore casuale ai geni reali (`BT-06 @ 00:32:28`);
- **per permutazione**: si scambiano di posizione due o più geni; è quella usata per il TSP.
**Aggiornamento della popolazione** (`BT-06 @ 00:33:00`): sostituzione **generazionale** completa (utile se le soluzioni precedenti non devono influenzare le successive), sostituzione **parziale** (*steady-state*, solo alcuni membri sostituiti), **elitismo** (i migliori passano senza modifiche) (`BT-06 @ 00:33:32`).
## 7. La funzione di fitness
`BT-06 @ 00:34:03`
La parte che richiede più sforzo ingegneristico. La fitness è una **misura numerica della qualità di una soluzione** rispetto al problema: quanto un individuo soddisfa gli obiettivi (`BT-06 @ 00:34:03`). Guida la selezione: gli individui con fitness più alta hanno più probabilità di riprodursi e passare le proprie caratteristiche (`BT-06 @ 00:34:38`). Dipende dalla **funzione di valutazione**, l'algoritmo che analizza ciascun individuo e gli assegna un punteggio secondo i criteri del problema.
Slide "Valutazione" (`BT-06 @ 00:36:00`): "Il valutatore decodifica un cromosoma e gli assegna una misura di fitness. Il valutatore è l'unico collegamento tra un GA classico e il problema che sta risolvendo."
Nel TSP, per il docente, la fitness "potrebbe essere proporzionale alla lunghezza del percorso: percorsi più brevi hanno fitness più alta" (`BT-06 @ 00:35:12`).
> **Correzione:** le due affermazioni sono incompatibili: se i percorsi più brevi devono avere fitness più alta, la fitness è **inversamente** proporzionale alla lunghezza. Nel notebook è $`1/d`$ (sezione 9), come il docente dice più avanti ("diversamente proporzionale", `BT-06 @ 00:58:16`).
Una fitness mal definita porta a soluzioni subottimali, ottimi locali o inefficaci: di qui l'invito a riflettere a lungo sul problema (`BT-06 @ 00:36:19`).
## 8. Quando usare e quando non usare un GA; applicazioni
`BT-06 @ 00:36:55`
**Quando usarli** (a voce e slide "Quando usare GA", `BT-06 @ 00:41:44`):
- problemi complessi o **NP-hard** con spazio delle soluzioni molto ampio: TSP, pianificazione e scheduling, ottimizzazione combinatoria come **bin packing** e **graph coloring** (`BT-06 @ 00:37:28`);
- problemi **multiobiettivo**: minimizzare i costi e massimizzare l'efficienza, ottimizzare consumo energetico e prestazioni (`BT-06 @ 00:37:58`);
- spazi troppo grandi per metodi esaustivi: sbroglio di circuiti, topologia di reti di comunicazione (`BT-06 @ 00:38:33`);
- superfici di ricerca **irregolari**, con molti massimi e minimi locali; ottimizzazione non lineare, dati rumorosi, assenza di modelli matematici precisi, come nella progettazione aerodinamica (`BT-06 @ 00:39:10`);
- vincoli complicati: logistica con limiti di tempo e risorse, rotte di veicoli con vincoli geografici e temporali (`BT-06 @ 00:39:41`);
- esplorazione iniziale dello spazio delle soluzioni; problemi simili già risolti con un GA, riusandone le popolazioni come una sorta di "transfer learning" (`BT-06 @ 00:40:13`);
- bisogno di una soluzione spiegabile, modulare, flessibile: se il problema cresce basta intervenire sui vettori che rappresentano gli individui (`BT-06 @ 00:41:19`).
Slide "Quando usare GA": le alternative sono troppo lente o complicate; serve uno strumento esplorativo; il problema è simile a uno già risolto con un GA; si vuole ibridare con una soluzione esistente; i vantaggi dei GA soddisfano i requisiti chiave del problema.
**Quando non usarli** (la seconda slide ha lo stesso titolo "Quando usare GA", errore segnalato dal docente, `BT-06 @ 00:41:49`):
- serve una **soluzione esatta**: i GA danno soluzioni approssimate e non garantiscono l'ottimo globale in tempo finito (`BT-06 @ 00:42:23`);
- ottimizzazione lineare o intera risolvibile esattamente con **programmazione lineare** o **branch and bound**; cammini minimi con **Dijkstra** o **Floyd-Warshall** (`BT-06 @ 00:42:57`);
- esistono algoritmi deterministici più veloci per problemi strutturati, come routing con vincoli semplici (greedy);
- serve **interpretabilità completa**, requisito dell'intelligenza artificiale affidabile (*trustworthy AI*): spiegare end-to-end perché una mutazione è stata preferita a un'altra non è sempre possibile (`BT-06 @ 00:43:29`).
Contenuto della stessa slide: scelte di implementazione (rappresentazione; dimensione della popolazione, tasso di mutazione; selezione e politiche di eliminazione; operatori di crossover e mutazione), criteri di terminazione, prestazioni e scalabilità; "la soluzione è valida solo quanto la funzione di valutazione (spesso la parte più difficile)".
**Applicazioni** (`BT-06 @ 00:44:41`; slide "Alcune applicazioni di GA", tabella dominio → esempi):
<table header-row="true">
<tr>
<td>Dominio</td>
<td>Esempi</td>
</tr>
<tr>
<td>Control</td>
<td>gas pipeline, pole balancing, missile evasion, pursuit</td>
</tr>
<tr>
<td>Design</td>
<td>semiconductor layout, aircraft design, keyboard configuration, communication networks</td>
</tr>
<tr>
<td>Scheduling</td>
<td>manufacturing, facility scheduling, resource allocation</td>
</tr>
<tr>
<td>Robotics</td>
<td>trajectory planning</td>
</tr>
<tr>
<td>Machine Learning</td>
<td>designing neural networks, improving classification algorithms, classifier systems</td>
</tr>
<tr>
<td>Signal Processing</td>
<td>filter design</td>
</tr>
<tr>
<td>Game Playing</td>
<td>poker, checkers, prisoner's dilemma</td>
</tr>
<tr>
<td>Combinatorial Optimization</td>
<td>set covering, travelling salesman, routing, bin packing, graph colouring and partitioning</td>
</tr>
</table>
A voce: set covering in logistica (coprire requisiti con il minor numero di risorse), routing e bin packing (`BT-06 @ 00:45:14`); progettazione aerodinamica di carene, layout di circuiti integrati, strutture meccaniche più resistenti e leggere (`BT-06 @ 00:45:44`); ottimizzazione della topologia di reti neurali (numero di strati e di neuroni) e **TPOT**, libreria di AutoML che con un GA sceglie l'algoritmo di machine learning e ne ottimizza l'architettura, con una fitness legata all'accuratezza sul test set (`BT-06 @ 00:46:18`). Il docente ipotizza una fitness come distanza o errore quadratico da un'accuratezza obiettivo (95%, 92%) (`BT-06 @ 00:47:56`). Altre: strategie per poker e dilemma del prigioniero, allocazione di risorse, bioinformatica (ricostruzione di sequenze di DNA, pattern genetici, progettazione di proteine), ecosistemi (`BT-06 @ 00:48:56`); reti fisiche, sistemi distribuiti, traiettorie di robot, strategie di trading, composizione musicale con fitness come distanza da melodie di riferimento (`BT-06 @ 00:50:03`).
> **Nota aggiunta:** TPOT usa la **programmazione genetica** (individui ad albero che rappresentano pipeline di preprocessing e modelli) e come fitness il punteggio in cross-validation, in versione multiobiettivo con la complessità della pipeline; non l'accuratezza sul test set.
## 9. Il problema del commesso viaggiatore (TSP) in Colab
`BT-06 @ 00:51:14`
Slide "Avete mai pianificato un viaggio in più tappe? Quale metodo avete usato per minimizzare la distanza totale percorsa?" e "Cartina alla mano non sembra così difficile... per poche tappe" (una cartina del Nord Italia) (`BT-06 @ 00:51:59`). Con poche tappe bastano poche addizioni; con molte il calcolo manuale diventa lungo e soggetto a errori. Il docente cita un articolo del 2008-2009 sullo staff di Barack Obama che avrebbe usato algoritmi genetici per pianificare la campagna elettorale nei 49 stati visitati (`BT-06 @ 00:52:30`).
Slide "Traveling Salesman's Problem (TSP)" (`BT-06 @ 00:53:10`): un commesso viaggiatore deve visitare un certo numero di città, conosce le distanze fra di esse, vuole il percorso più breve che parta da casa e vi ritorni dopo aver visitato **ogni città una sola volta**.
Slide "Caratteristiche del problema" (`BT-06 @ 00:53:44`): il TSP è fra i problemi matematici più studiati in informatica; è **NP-hard**; la prima formulazione risale al **1857**, con l'*icosian game* di **William Hamilton**: trovare un giro lungo gli spigoli di un dodecaedro. Slide "Forma generale TSP" (`BT-06 @ 00:54:18`): forme geometriche e distanze qualsiasi; introdotta fra gli anni '40 e '50; applicazioni in logistica e trasporti, circuiti stampati (percorso del trapano), protocolli di routing, sequenziamento del DNA.
> **Nota aggiunta:** il numero di giri distinti su $`n`$ città (simmetrico, partenza fissata) è $`(n-1)!/2`$: con 10 città sono 181.440, enumerabili; con 20 città circa $`6 \times 10^{16}`$.
### 9.1 Il codice
`BT-06 @ 00:56:03`
Notebook `tsp_genetic_algorithm_with_comments.ipynb`, ultima esercitazione del corso. Librerie: NumPy, Matplotlib, `random` (`BT-06 @ 00:56:35`). **Città e distanza** (10 città con coordinate casuali nel quadrato unitario, distanza euclidea):
```python
import numpy as np
import matplotlib.pyplot as plt
import random

NUM_CITIES = 10  # Numero di città da visitare
np.random.seed(42)  # Fissiamo un seed per ottenere risultati riproducibili
cities = np.random.rand(NUM_CITIES, 2)  # coordinate (x, y) in un quadrato unitario

def euclidean_distance(city1, city2):
    # La distanza è calcolata come la norma L2 (distanza euclidea)
    return np.linalg.norm(city1 - city2)

# grafico delle città: plt.scatter(...) con le etichette 0-9, titolo 'Mappa delle città'
```
A ogni esecuzione la disposizione cambierebbe perché le coordinate sono casuali (`BT-06 @ 00:57:44`); con il seed 42 di NumPy resta la stessa.
**Lunghezza del percorso, popolazione iniziale, fitness** (`BT-06 @ 00:57:44`): 100 percorsi casuali; la fitness è l'inverso della distanza (`BT-06 @ 00:58:16`).
```python
def calculate_path_distance(path, cities):
    # somma delle distanze tra città consecutive, con ritorno alla prima
    distance = 0
    for i in range(len(path)):
        city1 = cities[path[i]]
        city2 = cities[path[(i + 1) % len(path)]]  # ciclo chiuso
        distance += euclidean_distance(city1, city2)
    return distance

POP_SIZE = 100
def initialize_population(num_cities, pop_size):
    population = [np.random.permutation(num_cities) for _ in range(pop_size)]
    return np.array(population)

population = initialize_population(NUM_CITIES, POP_SIZE)
fitness_scores = np.array([1 / calculate_path_distance(ind, cities) for ind in population])
print(f"Popolazione iniziale creata con {len(population)} individui.")
```
**Selezione a roulette** (`BT-06 @ 00:58:46`): probabilità = fitness / somma delle fitness.
```python
def roulette_wheel_selection(population, fitness_scores):
    probabilities = fitness_scores / np.sum(fitness_scores)
    selected_indices = np.random.choice(len(population), size=len(population), p=probabilities)
    return population[selected_indices]
```
**Crossover ordinato, mutazione a scambio, nuova popolazione** (`BT-06 @ 00:58:46`):
```python
# Operatore di crossover ordinato (Ordered Crossover)
def ordered_crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))   # due punti di taglio
    child = [-1] * size
    child[start:end] = parent1[start:end]                # porzione centrale dal primo genitore
    pointer = 0
    for city in parent2:                                 # il resto dal secondo, in ordine
        if city not in child:
            while child[pointer] != -1:
                pointer += 1
            child[pointer] = city
    return np.array(child)

# Operatore di mutazione (swap di due città)
def mutate(individual, mutation_rate=0.1):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

def generate_new_population(selected_population):
    new_population = []
    for i in range(0, len(selected_population), 2):
        parent1 = selected_population[i]
        parent2 = selected_population[(i + 1) % len(selected_population)]
        child1 = ordered_crossover(parent1, parent2)
        child2 = ordered_crossover(parent2, parent1)
        new_population.append(mutate(child1))
        new_population.append(mutate(child2))
    return np.array(new_population[:len(selected_population)])
```
Il crossover ordinato conserva la validità della permutazione: il figlio contiene ogni città una volta, con un segmento del primo genitore e le altre città nell'ordine in cui compaiono nel secondo.
**Ciclo evolutivo** (`BT-06 @ 00:59:28`):
```python
NUM_GENERATIONS = 200
mutation_rate = 0.1   # non usata: mutate() usa il suo default, anch'esso 0.1
best_distances = []

for generation in range(NUM_GENERATIONS):
    fitness_scores = np.array([1 / calculate_path_distance(ind, cities) for ind in population])
    selected_population = roulette_wheel_selection(population, fitness_scores)
    population = generate_new_population(selected_population)
    best_distance = 1 / np.max(fitness_scores)
    best_distances.append(best_distance)
    if generation % 20 == 0:
        print(f"Generazione {generation}: Miglior distanza = {best_distance:.2f}")

best_path = population[np.argmax(fitness_scores)]
best_distance = 1 / np.max(fitness_scores)
print(f"Miglior percorso trovato: {best_path} con distanza = {best_distance:.2f}")
```
Poi due grafici (`BT-06 @ 01:00:05`): il percorso sulla mappa ("Percorso ottimale con distanza = ...") e la convergenza (`best_distances` per generazione, "Convergenza della distanza migliore").
Output a schermo: miglior distanza 4.20 (gen. 0), 3.55, 3.45, 3.61, 3.73, **3.19** (gen. 100), 3.91, 3.61, 3.75, 4.02 (gen. 180); "Miglior percorso trovato: \[4 8 3 0 7 9 5 1 2 6\] con distanza = 4.10". Il docente: su 200 generazioni "arriveremo a trovare il miglior percorso alla generazione 180, dove ci siamo arrestati" (`BT-06 @ 00:59:28`). Le operazioni sono somme e divisioni, codice semplice; invito a sperimentare variando individui iniziali e generazioni (`BT-06 @ 01:00:37`).
> **Correzione:** il ciclo esegue tutte le **200** generazioni; 180 è solo l'ultima stampata (una ogni 20). E il risultato non è il miglior percorso: la miglior distanza a schermo oscilla (3.19 alla generazione 100, 4.10 alla fine) perché senza elitismo la soluzione migliore può andare persa. Inoltre `best_path` è preso dalla popolazione **nuova** con l'indice calcolato sulle fitness della **vecchia**: il percorso stampato non è quello a cui si riferisce la distanza. Verificato per esecuzione: sulle stesse 10 città il percorso a schermo `[4 8 3 0 7 9 5 1 2 6]` è lungo **5.71**, non 4.10 (infatti nel grafico si incrocia più volte); l'**ottimo esatto** per forza bruta è **2.903** (`0 5 3 8 2 7 9 6 1 4`). Il GA del notebook tocca l'ottimo durante le 200 generazioni in tutte e cinque le esecuzioni di prova, ma lo perde; con un solo individuo elitario (il migliore copiato nella nuova popolazione) termina sull'ottimo in tutte e cinque.
> **Nota aggiunta:** il seed di NumPy fissa città e popolazione iniziale, ma crossover e mutazione usano il modulo `random`, senza seed: i risultati cambiano a ogni esecuzione (serve anche `random.seed(...)`). La variabile `mutation_rate = 0.1` del ciclo non è passata a `mutate`. `mutate` modifica il figlio sul posto, senza effetti collaterali perché il figlio è un array nuovo. Una correzione minima: calcolare le fitness della popolazione finale prima di `argmax`, oppure tenere traccia del migliore di sempre.
## 10. Collegamento con il test finale
La lezione si chiude annunciando la lettura della traccia del test (`BT-06 @ 00:56:03`), che non è nella registrazione. Il test finale 2026 (vedi **Assessment**) non contiene domande sugli algoritmi genetici: la teoria riguarda ABMS, ODE ed epidemiologia computazionale, la pratica un modello Mesa preda-predatore o il modello di Gompertz.
## 11. Glossario, punti incerti, materiale usato
### Glossario
- **Algoritmo genetico (GA):** metaeuristica che evolve una popolazione di soluzioni con selezione, crossover e mutazione.
- **Gene, cromosoma, popolazione:** elemento della soluzione; soluzione completa; insieme delle soluzioni.
- **Fitness, funzione di valutazione:** misura della qualità di una soluzione; l'algoritmo che la calcola.
- **Selezione a roulette, a torneo, per rango:** probabilità proporzionale alla fitness; migliore di un sottoinsieme; probabilità proporzionale al rango.
- **Elitismo:** i migliori individui passano invariati alla generazione successiva.
- **Crossover (a un punto, a due punti, uniforme, ordinato):** combinazione dei geni di due genitori; l'ordinato preserva le permutazioni.
- **Mutazione:** variazione casuale di un figlio (inversione di bit, rumore su reali, scambio di geni).
- **Convergenza prematura:** popolazione uniforme bloccata in un ottimo locale.
- **Metaeuristica:** strategia generale che guida euristiche di ricerca oltre gli ottimi locali.
- **NP-hard:** classe di problemi almeno difficili quanto ogni problema in NP; nessun algoritmo polinomiale noto.
- **TSP:** percorso chiuso più breve che visita ogni città una volta.
### Punti incerti
- Articolo del 2008-2009 sulla campagna di Obama pianificata con algoritmi genetici "nei 49 stati" (`BT-06 @ 00:52:30`): non verificato \[?\].
- Tournament selection "vengono selezionati con sette insieme di individui" (`BT-06 @ 00:27:00`): letto come "un sottoinsieme".
- Nomi trascritti male e corretti nel testo: "big packing" → bin packing; "da extra o floyd workshop" → Dijkstra, Floyd-Warshall; "gridi" → greedy; "trasporti artificial intelligence" → trustworthy AI; "t pot" → TPOT; "icosian" (1857) e "hamilton william" → William Rowan Hamilton.
### Materiale usato
- Fotogrammi `BT-06` delle slide (`00:00:10`, `00:02:19`, `00:06:06`, `00:07:11`, `00:10:01`, `00:11:40`, `00:13:40`, `00:15:20`, `00:24:59`, `00:27:59`, `00:31:16`, `00:36:00`, `00:41:44`, `00:44:15`, `00:49:36`, `00:51:21`, `00:52:48`, `00:53:12`, `00:53:53`, `00:54:30`) e del notebook (`00:55:30`-`01:00:55`), più fotogrammi estratti dal video a `00:58:48`, `00:59:12`, `00:59:24`, `01:00:20`
- Verifica: `verifica_bt06.py` (codice del notebook, forza bruta sulle 10 città, prove con e senza elitismo)
