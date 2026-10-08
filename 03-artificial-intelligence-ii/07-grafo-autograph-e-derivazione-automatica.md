# 07 - Grafo, autograph e derivazione automatica
> Fonte Notion: https://app.notion.com/p/3d612abc808d819b9910eab39ad3e6a0 — ultima modifica 2026-09-09T23:31:22.149Z

> Giornata 2 del corso · video `TF-03` e `TF-04`
---
## 14. Il grafo: che cos'è, e come si guarda — `TF-03 @ 01:21:00`
**Perché servono le funzioni TensorFlow e non quelle di Python.** `TF-03 @ 01:20:00`: «se io lo faccio solo `print`, `print` è una funzione di Python, e su TensorFlow tutte le cose dovrebbero essere **serializzabili**, che possiamo scrivere dentro un \[grafo\]… perché la trasformazione che fa TensorFlow… se noi vogliamo usare TensorFlow dobbiamo trasformare tutte le funzioni che ci servono per la rete e l'addestramento in un **autografo**».
Apre un **secondo notebook**, `notebooks/12-06-2025-autograph.ipynb`. Cella `[0]`:
```python
import tensorflow as tf
import numpy as np
import timeit
```
**Che cos'è una «funzione TensorFlow».** `TF-03 @ 01:22:30`: «è infatti una funzione che usa le funzioni di TensorFlow». L'esempio è la concatenazione di due stringhe — in Python basterebbe la somma, qui si usa `tf.strings.join`. Celle `[1]` e `[2]`:
```python
def concat_string(x, y):
    return tf.strings.join([x, y], separator=" ")
```
```python
tf.print(concat_string(tf.constant("hello"), tf.constant("world!")))
```
```javascript
hello world!
```
**Il decoratore.** `TF-03 @ 01:24:30`: «come trasformare una funzione in un autografo? Basta definire la stessa funzione qua e aggiungere un decorator… chiocciola, `tf.function`. E lui sa già che questo è infatti un autografo di TensorFlow». Cella `[3]`:
```python
@tf.function
def graph_string(x, y):
    return tf.strings.join([x, y], separator=" ")
```
**Guardare il grafo.** È il passaggio che dà sostanza alla parola. Cella `[4]`:
```python
graph_string.get_concrete_function(
    tf.constant("hello"), tf.constant("world!")
).graph.as_graph_def()
```
L'output è la definizione del grafo in Protocol Buffer, e il docente la legge nodo per nodo (`TF-03 @ 01:26:30`): «vedete ad esempio che noi abbiamo un operatore, un **placeholder**, e poi il tipo è una string; poi c'è un altro nodo, poi l'altro nodo, `separator` — che noi abbiamo detto che le operazioni sono in tutti i nodi». E il collegamento all'introduzione della giornata 1: «questo è quello che abbiamo visto nell'introduzione, che infatti TensorFlow fa questa rappresentazione di un grafo, data flow di un grafo, è proprio questo».
Nell'output salvato si riconoscono i tre nodi: due `Placeholder` di tipo `DT_STRING` (`x` e `y`), il nodo `StringJoin`, e il nodo `Identity` che porta fuori il risultato.
**La seconda forma.** `TF-03 @ 01:28:00`: «possiamo anche trasformare senza definire \[il decoratore\]: se noi abbiamo già definito una funzione… possiamo fare `tf.function` invece di fare il decorator». Cella `[5]`:
```python
# other mode to transform function into autpgraph
def py_func(x, y):
    return tf.reduce_mean(x**2 + y**2)

graph_py_func = tf.function(py_func)

graph_py_func.get_concrete_function(
    tf.constant([3.0, 6.0]),
    tf.constant([1.0, 2.0])
).graph.as_graph_def()
```
Il grafo che ne esce è più lungo — ci sono i due `Pow`, l'`AddV2`, il `Mean` — e serve a mostrare che il meccanismo è lo stesso su una funzione qualunque.
E il riepilogo, `TF-03 @ 01:32:30`: «ritorniamo sull'autografo. Noi abbiamo visto che ci sono **due modi** per trasformare un grafo: usando il decorator, oppure lo applichiamo direttamente `tf.function`».
> **Qui cade il taglio fra i due file.** TF-03 finisce pochi secondi dopo; TF-04 riprende con l'esempio che misura il guadagno.
---
## 15. Quanto fa guadagnare `@tf.function` — `TF-04 @ 00:00:00`
**La funzione da misurare**: elevare a potenza una matrice moltiplicandola ripetutamente per sé stessa, partendo dall'identità. Cella `[6]`:
```python
# comparaison
def norm_power(x, y):
    res = tf.eye(
        10, dtype=tf.int32
    )
    for _ in range(y):
        res = tf.matmul(x, res)
    return res

auto_power = tf.function(norm_power)
x = tf.random.uniform(
    shape=[10, 10],
    minval=2,
    maxval=4,
    dtype=tf.int32
)
```
Il docente spiega la scelta: «ricordate, quella che vorrei avere è una matrice di identità. Io vorrei fare una funzione che fa la potenza di una matrice: per questo devo fare una moltiplicazione di questa `x` con questa identità». E il vincolo: «matrice quadrata, perché non possiamo fare una potenza se non è quadrata».
Sui valori del random, `TF-04 @ 00:03:00`: «intanto non serve a noi di sapere il valore, però potete usare quello che volete».
**La misura.** Su `timeit`: «più o meno calcola una media dei tempi lanciando questa funzione»; e a `TF-04 @ 00:03:30`: «lo faccio un confronto dei tempi lanciando questa funzione **mille volte**». Celle `[7]` e `[8]`:
```python
timeit.timeit(lambda: norm_power(x, 100), number=1000)
```
```javascript
4.696285682002781
```
```python
timeit.timeit(lambda: auto_power(x, 100), number=1000)
```
```javascript
0.5833920000004582
```
**Il commento a voce** (`TF-04 @ 00:05:00`): «prima lanciamo quello normale, che prende più o meno **4 secondi**; e quello autografo invece lo fa solo **0.5 secondi**. Allora, potete vedere che l'autografo è molto molto veloce, più o meno **10 volte**».
I numeri del notebook confermano il parlato: 4.70 s contro 0.58 s, un fattore **8**. Il «10 volte» è l'arrotondamento a voce.
E la conclusione operativa: «questa è la prima ragione per cui noi dobbiamo usare sempre la `tf.function` quando facciamo l'addestramento di un modello».
> **Punto risolto dal materiale ufficiale.** Nei frame disponibili le celle di output dei due `timeit` non sono mai inquadrate: erano **\[illeggibile\]**, e i valori riportati venivano solo dal parlato. Il notebook ufficiale li fissa.
---
## 16. Le tre regole dell'autograph — `TF-04 @ 00:05:30`
«Ci sono alcune regole per le funzioni, per trasformarle in un autografo.»
### Regola 1 — non usare altre librerie dentro un autografo
`TF-04 @ 00:06:00`: «la prima regola è che non possiamo usare una funzione di altre librerie di Python dentro un autografo, perché vi dà un comportamento che è molto strano». Celle `[9]` e `[10]`:
```python
# rules for autograph
# 1. cant use other library inside an autograph
@tf.function
def numpy_random():
    a = np.random.randn(4, 4)
    tf.print("NUMPY: ", a)
```
```python
@tf.function
def auto_random():
    a = tf.random.normal((4, 4))
    tf.print("TF: ", a)
```
**La dimostrazione** sta nel chiamarle due volte a testa, in alternanza — celle `[11]`, `[12]`, `[13]`, `[14]`. Il notebook salvato conserva i quattro output, e sono la prova:
<table header-row="true">
<tr>
<td>Cella</td>
<td>Chiamata</td>
<td>Primo valore stampato</td>
</tr>
<tr>
<td>`[11]`</td>
<td>`numpy_random()`</td>
<td>`-0.52343125`</td>
</tr>
<tr>
<td>`[12]`</td>
<td>`auto_random()`</td>
<td>`-2.63253069`</td>
</tr>
<tr>
<td>`[13]`</td>
<td>`numpy_random()`</td>
<td>`-0.52343125` ← **identico a ****`[11]`**</td>
</tr>
<tr>
<td>`[14]`</td>
<td>`auto_random()`</td>
<td>`-0.787021339` ← diverso da `[12]`</td>
</tr>
</table>
`TF-04 @ 00:08:30`: «adesso, se richiamo di nuovo il NumPy, vedete che avrò **sempre lo stesso valore**, lo stesso valore. Invece quello che io voglio è che quando chiamo questo mi dia un nuovo random — e vedete che questo adesso è cambiato».
Il motivo: la chiamata NumPy viene eseguita **una volta sola**, durante il tracing, e il suo risultato resta congelato nel grafo come costante. La chiamata TensorFlow diventa invece un nodo del grafo, e viene rieseguita a ogni invocazione.
### Regola 2 — non creare variabili dentro un autografo
`TF-04 @ 00:09:30`: «non possiamo creare una variabile dentro un autografo». Cella `[15]`:
```python
# never creare una variable 
@tf.function
def create_variable():
    x = tf.Variable(1.0)
    x.assign_add(3.0)
    return x
```
Cella `[16]`, l'errore che il docente vuole far vedere — e che il notebook salvato conserva per intero:
```javascript
ValueError: in user code:

    File "/tmp/ipykernel_341776/50979080.py", line 4, in create_variable  *
        x = tf.Variable(1.0)

    ValueError: tf.function only supports singleton tf.Variables created on the first
    call. Make sure the tf.Variable is only created once or created outside tf.function.
    See https://www.tensorflow.org/guide/function#creating_tfvariables for more
    information.
```
«Se io chiamo questa funzione vi dà un errore — comunque questo ci aiuta già, perché lui vi dice anche che nella `tf.function` non possiamo creare una variabile dentro.»
**La via d'uscita** (`TF-04 @ 00:12:00`): «quello che possiamo fare è qualcosa del genere… è come una variabile globale. Per definirlo dobbiamo definirlo **fuori**, ma dentro l'autografo possiamo comunque usare quella variabile». Cella `[17]`:
```python
var = tf.Variable(1.0)

@tf.function
def create_variable():
    var.assign_add(3.0)
    return var
```
E le due chiamate successive, celle `[18]` e `[19]`, mostrano che lo stato **persiste** fra un'invocazione e l'altra: `4.0`, poi `7.0`.
Il docente collega esplicitamente questo punto alla giornata 1: «ricorda la stessa cosa che abbiamo visto quando abbiamo fatto le prove per il TPU: noi dobbiamo mandare il grafo nel worker, e a volte il worker non riesce ad aggiornare la CPU per farci vedere il valore dell'accuratezza» (`TF-04 @ 00:12:30`).
### Regola 3 — non modificare oggetti Python dentro un autografo
`TF-04 @ 00:13:30`: «un'altra cosa è che non possiamo fare un'operazione di lista Python… **never update Python list**». Cella `[20]`:
```python
# never update python list
ll = []

@tf.function
def add_element(x):
    ll.append(x) # not safe
    return ll
```
Il commento `# not safe` è aggiunto dal docente durante la lezione, dopo essere andato a controllare la documentazione (`TF-04 @ 00:16:30`–`00:18:00`): «sto usando la **2.19**… solo per vedere se c'è un aggiornamento su questo… mi sembra che è stabile, che si può usare, ma a volte dà un comportamento in cui non fa l'aggiornamento della lista Python».
**La dimostrazione, in due tempi.** Prima chiamandola con **interi Python** — celle `[21]`, `[22]`, `[24]`, `[25]` con argomenti `6`, `7`, `4`, `65`. La funzione restituisce la lista, che cresce; e la cella `[23]`, che ispeziona `ll` direttamente, mostra `[6, 7]`: valori veri.
Poi chiamandola con un **tensore**, cella `[26]`:
```python
add_element(tf.constant(4))
```
```javascript
WARNING:tensorflow:5 out of the last 5 calls to <function add_element at 0x7c55406f7010>
triggered tf.function retracing. Tracing is expensive and the excessive number of
tracings could be due to (1) creating @tf.function repeatedly in a loop, (2) passing
tensors with different shapes, (3) passing Python objects instead of tensors. …
```
E infine la cella `[27]`, che è il punto di tutta la sezione:
```python
ll
```
```javascript
[6, 7, 4, 65, <tf.Tensor 'x:0' shape=() dtype=int32>]
```
`TF-04 @ 00:19:00`: «guarda che non è più un valore… nella lista non vedo il valore, mi dà un valore strano… e questo è il problema: **non possiamo fare l'append di un tensore a una lista Python dentro** \[un autografo\]».
Nella lista resta un **tensore simbolico** (`'x:0'`), il segnaposto del grafo, non un valore. E le celle `[28]` e `[29]` chiudono la dimostrazione: una nuova chiamata con `tf.constant(6)` restituisce una lista che *sembra* aggiornata, ma `ll` è rimasta **identica a prima** — il quinto elemento è sempre lo stesso segnaposto. L'append non è mai avvenuto davvero.
E conclude: «dobbiamo anche evitare di fare questo, perché a volte non fa l'aggiornamento… perché qua per esempio funziona, ma quando diventa un'altra situazione questo non funziona».
---
## 17. Derivazione automatica con `GradientTape` — `TF-04 @ 00:20:00`
«Questo è più o meno il **core** dell'addestramento, perché noi usiamo TensorFlow e la derivazione automatica.»
**Perché serve.** `TF-04 @ 00:21:30`: «per un singolo layer abbiamo la variabile `weight` e il `bias`, e durante la backpropagation dobbiamo calcolare la loss rispetto al `weight` per aggiornare il `weight`, e poi la loss rispetto al `bias` per aggiornare il `bias`. E si fa la stessa cosa fino alla fine: iniziamo dall'output e poi torniamo fino all'input».
**L'esempio.** Una parabola, `y = a·x² + b·x + c`. Cella `[30]` — e il commento che il docente scrive contiene già il risultato atteso:
```python
# Automatic derivation

## y = a*x^2 + b*x + c => dy/dx = 2*x + b => dy2/dx2 = 2

x = tf.Variable(0.0)
a = tf.constant(1.0)
b = tf.constant(2.0)
c = tf.constant(-1.0)
```
Il docente insiste: «sempre dobbiamo inizializzare una variabile».
Celle `[31]` e `[32]`:
```python
with tf.GradientTape() as tape:
    y = a*x**2 + b*x + c
dy_dx = tape.gradient(y, x)
```
```python
dy_dx
```
```javascript
<tf.Tensor: shape=(), dtype=float32, numpy=2.0>
```
**La verifica a mano** (`TF-04 @ 00:25:00`). Il docente calcola la derivata: «la derivata di questo rispetto a `x` è `2·a·x + b`… e adesso `x` è 0, perché noi dobbiamo fare una derivazione **numerica**, per valore. Allora `2 · 0` fa 0, il `b` è 2. Questa derivazione deve darmi **2**». E controlla a schermo: «vedi, era il 2».
**Derivata seconda con tape annidati** (`TF-04 @ 00:26:00`): «supponiamo che vogliamo fare la derivata seconda… è sempre 2, perché questo è 0 e questo è 2». Celle `[33]` e `[34]`:
```python
with tf.GradientTape() as tape2:
    with tf.GradientTape() as tape:
        y = a*x**2 + b*x + c
    dy_dx = tape.gradient(y, x)
dy2_dx2 = tape2.gradient(dy_dx, x)
```
```python
dy2_dx2
```
```javascript
<tf.Tensor: shape=(), dtype=float32, numpy=2.0>
```
La regola: il tape esterno deve **contenere** il calcolo del gradiente interno, altrimenti non ha nulla da derivare.
**Il significato geometrico**, `TF-04 @ 00:55:00`, ripreso più avanti mentre scrive `assign_sub`: «se pensiamo che siamo su una montagna, e quella montagna potrebbe essere a tre dimensioni perché l'altezza e poi `x` e `y`, e se noi calcoliamo il derivato parziale a questo punto e facciamo la freccetta che rappresenta quel vettore, vi dà una direzione per arrivare in alto, al massimo della montagna. E poi anche il **modulo** di questi vettori ti dà anche quanto devi fare per arrivare al massimo». E la conseguenza: «noi vogliamo arrivare al **minimo** del loss. Allora, cosa dobbiamo fare? Dobbiamo fare una sottrazione… perché il gradient mi dà il massimo, ma io vorrei andare al minimo».
---
## 18. Regressione lineare scritta a mano — `TF-04 @ 00:28:30`
«Adesso vediamo come si applica questo a una **linear regression**.»
**Che cos'è, nelle parole del docente** (`TF-04 @ 00:29:00`): «una linear regression è che dobbiamo generalizzare una funzione che mappa due valori — abbiamo `x` e `y` — e la linear regression sta cercando il valore di `a` e `b` tali che `y = a·x + b`».
### I dati sintetici
Celle `[35]` e `[36]`, `TF-04 @ 00:30:00`–`00:36:00`:
```python
# application

# [x, y] => a e b s.t y = a*x + b
# tf.random.set_seed(12)
import tensorflow as tf
import numpy as np

size = 400
```
```python
X = tf.random.uniform([size, 2], minval=-5, maxval=5)

A = tf.constant([[1.0], [-2.0]])
B = tf.constant([[3.0]])

###
noise = tf.random.normal([size, 1], mean=0.0, stddev=2.0)
Y = tf.matmul( X, A) + B + noise
```
Sul seed (`TF-04 @ 00:31:00`): «`tf.random.set_seed`… per tutte le chiamate in cui userò `random`, lui usa questo seed. Così, quando faccio lo stesso random e lo lancio nella stessa applicazione, posso avere sempre lo stesso random».
> **Il seed è commentato nel notebook salvato.** Il docente lo scrive e lo spiega, poi lo disattiva: nel file resta `# tf.random.set_seed(12)`. Chi rilancia il notebook ottiene dati diversi a ogni esecuzione, e quindi coefficienti stimati leggermente diversi da quelli stampati negli output salvati.
Sulle forme: «visto che abbiamo due \[colonne\], quando facciamo la moltiplicazione… abbiamo due righe, perché facciamo `A·X`».
Sul rumore: «l'idea è che aggiungiamo un po' di rumore, così non è proprio \[allineato\]… possiamo generare una linear regression come questa anche se aggiungiamo quel rumore».
I coefficienti veri da ritrovare sono quindi `A = [[1.0], [-2.0]]` e `B = [[3.0]]`, sepolti sotto un rumore gaussiano di deviazione standard 2.
### Il generatore di batch
Cella `[37]`, `TF-04 @ 00:36:30`–`00:40:00`:
```python
def dataset(inputs, labels, batch_size):
    length = len(inputs)
    indexes = list(range(length))
    np.random.shuffle(indexes)
    for i in range(0, length, batch_size):
        index = indexes[i: min(i + batch_size, length)]
        yield tf.gather(inputs,index), tf.gather(labels, index)
```
Il docente spiega ogni pezzo: «questo dataset è un **generatore** che chiamiamo quando facciamo l'addestramento… poi facciamo un random shuffling, perché anche durante l'addestramento vogliamo fare uno shuffling degli input. Così, per ogni epoca, abbiamo più o meno diverse distribuzioni dei dati: ecco perché è meglio fare lo shuffling».
E il motivo del `min(...)` (`TF-04 @ 00:40:00`): «vedete il problema qua? Se abbiamo 5 elementi ma il batch size era 2, quando lui arriva al 4 abbiamo solo \[un elemento residuo\]». È il caso del batch incompleto in coda.
> **Nota.** Nei frame il corpo di questa funzione è sempre parzialmente coperto — era uno degli **\[illeggibile\]** della versione precedente di questo manuale. Il notebook ufficiale lo risolve.
### Parametri e modello
Celle `[38]`, `[39]`, `[40]`, `TF-04 @ 00:48:29`:
```python
weight = tf.Variable(
    tf.random.normal(A.shape),
    name='weight'
)
bias = tf.Variable(
    tf.zeros_like(
        B,
        dtype=tf.float32
    ),
    name='bias'
)
```
```javascript
<tf.Variable 'weight:0' shape=(2, 1) dtype=float32, numpy=
array([[ 0.27520117],
       [-0.6709022 ]], dtype=float32)>

<tf.Variable 'bias:0' shape=(1, 1) dtype=float32, numpy=array([[0.]], dtype=float32)>
```
I pesi partono casuali, il bias da zero — con la forma presa dai tensori veri `A` e `B`. Celle `[41]` e `[42]`:
```python
class Regression:
    def __call__(self, x):
        return x @ weight + bias

    def loss(self, y_true, y_pred):
        return tf.reduce_mean((y_true - y_pred) ** 2 / 2)
        
```
```python
model = Regression()
```
La loss è l'errore quadratico medio diviso 2: la divisione serve solo a semplificare la derivata. Il modello non eredita da nulla — è una classe Python con `__call__`, e legge `weight` e `bias` come variabili globali. È la versione più spoglia possibile, e nella giornata 3 diventerà `tf.Module`.
### Il passo di addestramento
Cella `[43]`, `TF-04 @ 00:57:00`:
```python
@tf.function
def train_step(model, inputs, labels, learning_rate=0.01):
    with tf.GradientTape() as tape:
        predictions = model(inputs)
        loss = model.loss(labels, predictions)
    dloss_dw, dloss_db = tape.gradient(loss, [weight, bias])
    weight.assign_sub(learning_rate*dloss_dw)
    bias.assign_sub(learning_rate*dloss_db)
    return loss
```
È la sintesi di tutto: il tape registra il forward, `tape.gradient` restituisce le due derivate, `assign_sub` aggiorna le variabili sottraendo il gradiente moltiplicato per il learning rate.
Il docente lo detta mentre lo scrive (`TF-04 @ 00:57:00`): «facciamo prima il learning rate, perché noi non vogliamo andare direttamente a uno step molto grande, allora moltiplichiamo questo al \[gradiente della\] loss rispetto al weight. E la stessa cosa per il bias… E questo lo teniamo in `loss`, solo per mostrare che abbiamo una convergenza o no».
### Il ciclo esterno
Cella `[44]`, `TF-04 @ 00:57:30`–`00:59:30`:
```python
@tf.function
def train_loop(model, epochs):
    for epoch in tf.range(1, epochs + 1):
        for inputs, labels in dataset(X, Y, batch_size=10):
            loss = train_step(model, inputs, labels)
        if epoch % 10 == 0:
            tf.print("Epoch: ", epoch, "Loss: ", loss)
            tf.print("Weight: ", weight)
            tf.print("Bias: ", bias)
```
«Visto che abbiamo l'autografo per ogni step, per ogni batch, allora qua posso chiamare questa funzione… adesso facciamo solo un piccolo debug: per ogni 10 epoche facciamo una stampa, ad esempio il valore dell'epoca, e poi il loss… possiamo mostrare anche il weight.»
### I tre errori, e cosa erano davvero
`TF-04 @ 00:59:30`: «mi sa che ci siamo adesso». Lancia `train_loop(model, epochs=200)` — e non parte. Seguono tre esecuzioni fallite in un minuto, tutte con un traceback lunghissimo che riempie lo schermo:
```javascript
File /tmp/__autograph_generated_filez82f_2ac.py:51, in outer_factory.<locals>.inner_factory.<locals>.tf__train_loop
     49     loss = ag__.Undefined('loss')
     50     inputs = ag__.Undefined('inputs')
---> 51     ag__.for_stmt(ag__.converted_call(ag__.ld(tf).range, (1, ag__.ld(epochs) + 1), None, fscope), None, loop_bo…
```
**Non è un limite dell'autograph.** Le righe `ag__.Undefined` sono il **preambolo che l'autograph genera sempre** per le variabili assegnate dentro un ciclo, e compaiono nel traceback solo perché il traceback attraversa il file riscritto. La causa vera è in fondo, e sono **tre refusi di battitura** nella cella `train_step`, visibili nei frame:
<table header-row="true">
<tr>
<td>Frame</td>
<td>Scritto</td>
<td>Errore sollevato</td>
</tr>
<tr>
<td>`TF-04 @ 00:59:29`</td>
<td>`with tf.GradiantTape() as tape:`</td>
<td>manca la `e` di *Gradient*</td>
</tr>
<tr>
<td>`TF-04 @ 00:59:29`</td>
<td>`dloss_dw, dloss_db = tf.gradient(loss, …)`</td>
<td>`tf.gradient` non esiste: è `tape.gradient`</td>
</tr>
<tr>
<td>`TF-04 @ 01:00:43`</td>
<td>`ag__.ld(tf).gradiant`</td>
<td>terzo tentativo, ancora sbagliato</td>
</tr>
</table>
Il primo lancio dà un `NameError` (`TF-04 @ 00:59:29`, cella `In[58]`), i successivi un `AttributeError` (`In[61]`, `In[64]`, `In[67]`). A `TF-04 @ 01:01:00` il docente lo trova: «ah, non è `tf`, questo deve essere `tape`». Corregge, rilancia, e a `TF-04 @ 01:01:51` gira in **1.4 secondi**:
```javascript
EPoch:  10 Loss:  2.87516093
Weight:  [[1.00762606]
 [-2.01179361]]
Bias:  [[2.78198981]]
EPoch:  20 Loss:  2.88873339
...
```
> **Correzione a una versione precedente di questo manuale**
>
> La versione composta prima che il materiale ufficiale fosse disponibile leggeva quel traceback come una **limitazione dell'autograph** — un generatore Python dentro un ciclo di grafo — e ne concludeva che l'errore «non si riproduce più su TensorFlow 2.21». **Era una lettura sbagliata**, e il notebook ufficiale la smentisce in modo diretto: la cella `[45]`, salvata dal docente sulla **sua** TensorFlow 2.19, contiene `train_loop` decorato che gira e converge. Non c'era nessuna differenza fra le due versioni di TensorFlow: c'erano tre refusi, corretti in aula in novanta secondi.
>
> Il ciclo esterno decorato **funziona**, generatore Python compreso. Il generatore viene però eseguito **una volta sola**, in fase di tracing: è la regola 1 della sezione 16, e resta il motivo per cui in produzione al suo posto si usa `tf.data` — che è precisamente l'argomento con cui si apre la giornata 3.
### La convergenza che non arriva — `TF-04 @ 01:01:30`–`01:11:00`
Il programma gira, ma il docente non è soddisfatto: «comunque il loss è un po' male». Quello che segue è **dieci minuti di debug dal vivo**, ed è la parte più istruttiva della giornata, perché non finisce bene.
Le mosse, in ordine:
1. **Alza il learning rate** (`01:01:30`): «forse devo aumentare un po' il learning rate… ci provo. No, è peggio».
2. **Cambia la dimensione del batch** (`01:02:00`): «oppure possiamo dare un po' di batch, tipo 100? Ah no, ma quanti? Abbiamo 400, allora… forse usiamo 20». Poi scende ancora, fino a `batch_size=2` (`01:07:00`).
3. **Aumenta le epoche** (`01:03:00`): «vedete che se io faccio più o meno 1000, vediamo… no, non cambia nulla». E la diagnosi: «mi sa che l'aggiornamento è proprio molto piccolo».
4. **Riparte da zero in un notebook pulito** (`01:04:00`) per isolare il problema: «facciamo la pelle \[dello\] start… import tensorflow as tf, import numpy». Controlla a mano il valore iniziale di `weight`, del bias, di `A` e `X`.
5. **Stampa il gradiente** (`01:06:30`): «`tf.print`, `dloss_dw`… solo per fare un po' di debug».
6. **Prova un ****`break`**** dentro il ciclo** (`01:08:00`) — e scopre subito perché non funziona: «forse non funziona il `break` perché questo è una cosa di **Python**». È la regola 3 che torna sotto un'altra forma: dentro un autografo, il controllo di flusso Python non è quello che sembra.
**E finisce non risolto** (`01:10:30`): «c'è qualcosa che non mi torna, che non fa l'aggiornamento — ma infatti è fatto l'aggiornamento, ma **troppo poco**… forse devo studiare un po' la parte come faccio questo». E lo dice esplicitamente (`TF-04 @ 01:11:00`): «infatti, quello che è il nostro lavoro: fare il debug di una rete neurale».
<callout icon="➕">
	**Nota aggiunta:** il problema è il rapporto fra `learning_rate` e scala dei dati. Con `X` uniforme in `[−5, 5]` e batch da 10, il gradiente medio è piccolo rispetto alla distanza fra il bias iniziale (0) e quello vero (3): il bias risale lentamente, e a 200 epoche è ancora a 2.78. Il notebook salvato usa 100 epoche e arriva a 3.106 con loss 1.306 — cioè il docente ha continuato a lavorarci **dopo** la fine della registrazione. Questa spiegazione non è nel video: è un'aggiunta, ed è marcata.
</callout>
**Lo stato finale**, cella `[45]` del notebook ufficiale, quello che gli studenti hanno ricevuto:
```python
train_loop(model, epochs=100)
```
```javascript
Epoch:  10 Loss:  1.30693078
Weight:  [[0.969277382]
 [-2.01665497]]
Bias:  [[3.09724307]]
...
Epoch:  100 Loss:  1.30588841
Weight:  [[0.969495773]
 [-2.01696491]]
Bias:  [[3.10597825]]
```
`weight ≈ [0.969, −2.017]` contro il vero `[1.0, −2.0]`; `bias ≈ 3.106` contro il vero `3.0`. Con rumore di deviazione standard 2 su 400 punti, è la stima corretta.
---
## Esercizi lasciati aperti
**Nel notebook, come commento senza soluzione:**
- `12-06-2025.ipynb` cella `[23]`: `# exo: combination of map reduce and map fn`.
**A voce:**
- `TF-03 @ 00:26:30`: «potete anche provare a cambiare l'`axis` \[del `concat`\], ma questo rimane come un esercizio se volete vedere come funziona».
- `TF-04 @ 01:11:00`, l'ultimo assegnato della giornata: «vi chiedo se potete fare solo un plot di questo dataset rispetto alla funzione lineare che abbiamo generato».
> Nessuno dei tre viene risolto nelle due registrazioni.
E l'annuncio della giornata successiva (`TF-04 @ 01:11:30`): «speriamo che la prossima volta iniziamo a vedere un po' altri progetti, perché più o meno abbiamo finito adesso per vedere un po' come usare TensorFlow e possiamo entrare in un vero progetto».
---
## Glossario dei termini introdotti
<table header-row="true">
<tr>
<td>Termine</td>
<td>Definizione data nella lezione</td>
</tr>
<tr>
<td>**`tensor_scatter_nd_add`**</td>
<td>Somma valori in posizioni date da una lista di indici, lasciando invariato il resto. `TF-03 @ 00:10:00`</td>
</tr>
<tr>
<td>**`tensor_scatter_nd_update`**</td>
<td>Come sopra, ma **sostituisce** invece di sommare. `TF-03 @ 00:15:00`</td>
</tr>
<tr>
<td>**`tf.minimum`**</td>
<td>Minimo elemento per elemento fra due tensori; con uno scalare fa broadcast. Usata per imporre un tetto. `TF-03 @ 00:12:30`</td>
</tr>
<tr>
<td>**`tf.where`**</td>
<td>Con un argomento restituisce gli **indici** che soddisfano la condizione; con tre, sceglie fra due tensori elemento per elemento. `TF-03 @ 00:19:00`</td>
</tr>
<tr>
<td>**`concat`**** vs ****`stack`**</td>
<td>`concat` unisce lungo un asse esistente e richiede compatibilità solo su quell'asse; `stack` crea un **asse nuovo** e richiede shape identiche. `TF-03 @ 00:26:30`</td>
</tr>
<tr>
<td>**Dimensione di batch**</td>
<td>La prima dimensione che nasce facendo `stack` di una lista di input. `TF-03 @ 00:28:30`</td>
</tr>
<tr>
<td>**`reduce_sum(keepdims=True)`**</td>
<td>Somma conservando il rango del tensore. `TF-03 @ 00:34:12`</td>
</tr>
<tr>
<td>**`map_fn`**</td>
<td>L'equivalente TensorFlow di `map` di Python, ma eseguito nel grafo. `TF-03 @ 00:36:12`</td>
</tr>
<tr>
<td>**Broadcasting**</td>
<td>Estensione automatica delle dimensioni compatibili; `broadcast_to` la rende esplicita. `TF-03 @ 00:40:12`</td>
</tr>
<tr>
<td>**Dense layer**</td>
<td>`outputs = tf.matmul(input, weights) + bias`: da 10 feature a 5 uscite su 64 esempi. `TF-03 @ 00:44:12`</td>
</tr>
<tr>
<td>**`max_pool2d`**</td>
<td>Finestra scorrevole che tiene il massimo. `ksize` e `strides` hanno **quattro** componenti, una per asse: sbagliarle su un asse di lunghezza 1 produce un tensore vuoto. `TF-03 @ 01:02:50`</td>
</tr>
<tr>
<td>**`softmax`**</td>
<td>Trasforma punteggi grezzi in probabilità che sommano a 1. `TF-03 @ 01:06:34`</td>
</tr>
<tr>
<td>**`one_hot(depth=n)`**</td>
<td>Codifica binaria delle etichette; `depth` è il numero di classi. `TF-03 @ 01:11:00`</td>
</tr>
<tr>
<td>**`dropout(rate)`**</td>
<td>Azzera una frazione casuale dei valori e **riscala** i sopravvissuti di `1/(1−rate)`. `TF-03 @ 01:12:00`</td>
</tr>
<tr>
<td>**Batch normalization**</td>
<td>Normalizza gli attivi **a ogni batch**, non solo l'input all'inizio; nata con MobileNet per reti leggere. `TF-03 @ 01:14:30`</td>
</tr>
<tr>
<td>**Grafo (****`as_graph_def`****)**</td>
<td>La rappresentazione serializzata di una funzione decorata: nodi `Placeholder` per gli input, un nodo per operazione, un `Identity` in uscita. `TF-03 @ 01:26:00`</td>
</tr>
<tr>
<td>**Autografo (****`@tf.function`****)**</td>
<td>Trasforma una funzione Python in un grafo TensorFlow. Due forme: il decoratore, o `tf.function(f)`. Sull'esempio della potenza di matrice: 4.70 s → 0.58 s. `TF-04 @ 00:05:00`</td>
</tr>
<tr>
<td>**Regola 1 dell'autograph**</td>
<td>Non usare altre librerie (NumPy) dentro: la chiamata viene eseguita una volta sola, in fase di tracing, e il risultato resta congelato. `TF-04 @ 00:06:00`</td>
</tr>
<tr>
<td>**Regola 2 dell'autograph**</td>
<td>Non creare `tf.Variable` dentro: vanno definite fuori e usate dentro. `TF-04 @ 00:09:30`</td>
</tr>
<tr>
<td>**Regola 3 dell'autograph**</td>
<td>Non modificare oggetti Python (liste) dentro: nella lista resta un tensore simbolico, non un valore. Vale anche per il `break`. `TF-04 @ 00:13:30`</td>
</tr>
<tr>
<td>**Retracing**</td>
<td>Il warning `triggered tf.function retracing`: il grafo viene ricostruito a ogni chiamata con firma nuova. `TF-04 @ 00:14:30`</td>
</tr>
<tr>
<td>**`GradientTape`**</td>
<td>Registra le operazioni sul forward per poterle derivare; `tape.gradient(y, x)` restituisce la derivata **numerica nel punto**. `TF-04 @ 00:21:00`</td>
</tr>
<tr>
<td>**Tape annidati**</td>
<td>Per la derivata seconda: il tape esterno deve contenere il calcolo del gradiente interno. `TF-04 @ 00:26:00`</td>
</tr>
<tr>
<td>**`assign_sub`**</td>
<td>Aggiornamento in loco di una variabile: `w ← w − lr·∂loss/∂w`. La sottrazione perché il gradiente punta al **massimo**. `TF-04 @ 00:56:30`</td>
</tr>
<tr>
<td>**Shuffling per epoca**</td>
<td>Rimescolare gli indici a ogni epoca, così ogni epoca vede distribuzioni diverse dei batch. `TF-04 @ 00:38:00`</td>
</tr>
<tr>
<td>**Batch incompleto**</td>
<td>Con 5 elementi e batch 2 l'ultimo batch ha 1 elemento: da qui il `min(i + batch_size, length)`. `TF-04 @ 00:40:00`</td>
</tr>
</table>
---
## Punti a bassa confidenza
**56 segmenti segnalati** su 965 (TF-03: 28 su 506, TF-04: 28 su 459), più **10 segmenti di boilerplate rimossi** (frasi da sottotitoli mai pronunciate: «Grazie.», «Grazie per la visione!»). Elenco completo con i motivi in **`day-02-bassa-confidenza.md`**.
### Testo a schermo non leggibile `[illeggibile]`
Il materiale ufficiale ha **risolto cinque** dei sette punti che la versione precedente di questo manuale segnalava come illeggibili. Restano:
<table header-row="true">
<tr>
<td>Dove</td>
<td>Punto</td>
<td>Perché resta aperto</td>
</tr>
<tr>
<td>`TF-03 @ 00:22:58`</td>
<td>Il messaggio dell'`InvalidArgumentError` sul tipo di `tf.fill` è tagliato a destra</td>
<td>L'errore non è nel notebook salvato: la cella contiene già la versione corretta</td>
</tr>
<tr>
<td>`TF-04 @ 01:04:00`–`01:10:30`</td>
<td>Il notebook di debug improvvisato non è mai inquadrato per intero</td>
<td>Non è stato salvato né distribuito: esiste solo nei frame</td>
</tr>
</table>
**Risolti dal notebook ufficiale:** gli argomenti di `tf.minimum` (`TF-03 @ 00:13:12`), la comprensione che costruisce `sidx` (`TF-03 @ 00:10:12`), i tempi misurati dai due `timeit` (`TF-04 @ 00:04:30`–`00:05:30`), il warning di retracing (`TF-04 @ 00:14:30`), il corpo della funzione `dataset` (`TF-04 @ 00:37:29`–`00:42:29`). Il traceback dell'autograph (`TF-04 @ 01:00:12`–`01:00:41`) resta tagliato a destra nei frame, ma la causa è stata identificata con certezza ed è documentata nella sezione 18.
---
## Materiale ufficiale usato
<table header-row="true">
<tr>
<td>File</td>
<td>Ruolo</td>
</tr>
<tr>
<td>`12-06-2025/notebooks/12-06-2025.ipynb`</td>
<td>**Fonte del codice** delle sezioni 1-13. 40 celle, con gli output dell'esecuzione in aula</td>
</tr>
<tr>
<td>`12-06-2025/notebooks/12-06-2025-autograph.ipynb`</td>
<td>**Fonte del codice** delle sezioni 14-18. 47 celle</td>
</tr>
<tr>
<td>`TF-03.mp4`, `TF-04.mp4`</td>
<td>Fonte della **sequenza**: ordine di costruzione, errori corretti dal vivo, sessione di debug della sezione 18</td>
</tr>
</table>
Elenco completo delle divergenze fra notebook e schermo: **`day-02-divergenze.md`**. Verifica per esecuzione: **`VERIFICA-day-02.md`**.
## Notebook della lezione
I file originali del docente, sul tuo Mac in `Downloads/TensorFlow-MDA/Materiale Sito/estratti/`:
- `12-06-2025/12-06-2025/notebooks/12-06-2025-autograph.ipynb`
