# 06 - Indicizzazione, broadcasting e layer a mano
> Fonte Notion: https://app.notion.com/p/3d612abc808d81a5b11ce8d3e931d8c1 — ultima modifica 2026-09-09T23:31:20.205Z

> Giornata 2 del corso · video `TF-03` e `TF-04`
---
## 1. Nuovo ambiente di lavoro — `TF-03 @ 00:01:00`
Il docente riepiloga la giornata precedente: «nell'ultima lezione abbiamo visto la parte del tipo di tensore, poi come definire le costanti predefinite, i tensori casuali, poi come applicare alcune funzioni — `squeeze`, `expand_dims` — e poi le nozioni di variabili e costanti, come si fa ad aggiornarli. E alla fine siamo arrivati a quest'operazione di cui parliamo, `gather` e `scatter`».
Crea una cartella nuova, `12-06-2025`, e riparte da zero:
```bash
python3 -m virtualenv venv
source venv/bin/activate
pip install jupyter tensorflow-cpu matplotlib
```
Ripete la ragione dell'ambiente virtuale: «sempre, quando lavoriamo, meglio creare un ambiente virtuale per questo particolare progetto, perché potrebbe essere che avremo bisogno di altre cose e non vogliamo installare nel Python principale».
Precisa anche che **si può seguire su Google Colab**: «potete anche seguirmi usando Google Colab. Ma io lo faccio sempre così, anche per abituarvi a usare il locale, nel caso dobbiate fare dei test prima».
Crea `notebooks/12-06-2025.ipynb`, seleziona il kernel del virtualenv e riporta le celle della giornata precedente per continuare. Cella `[0]`:
```python
import tensorflow as tf
import numpy as np
```
---
## 2. L'esercizio della giornata 1, risolto — `TF-03 @ 00:05:00`
È l'assegnazione lasciata a fine giornata 1: prendere i voti dello **studente numero 5** per ogni modulo e ogni materia, aggiungere 2 punti, senza superare 30.
Il tensore dei voti viene ricreato con la stessa forma. Cella `[1]`:
```python
## tensor dim (8,10,5) 8-modulo, 10-studenti, 5 matiere

scores = tf.random.uniform(
    (8, 10, 5),
    minval=0,
    maxval=31,
    dtype=tf.int32
)
scores
```
**Costruzione degli indici.** Il docente li genera con una doppia comprensione Python — e sottolinea che è Python normale, non TensorFlow: «questa è una semplice Python». Lo studente numero 5 è all'indice **4**. Cella `[2]`:
```python
# definire l index del 5th 
sidx = [[mo, 4, ma] for mo in range(8) for ma in range(5)]
```
Un indice per ogni combinazione modulo × materia: 8 × 5 = **40** terne. Cella `[3]` verifica la prima:
```python
sidx[0]
```
```javascript
[0, 4, 0]
```
**I valori da aggiungere.** Cella `[4]` — ed è una **lista Python**, non un tensore:
```python
update_score_5 = [2]*len(sidx)
```
**L'aggiornamento.** Cella `[5]`, `TF-03 @ 00:10:00`:
```python
scores_update_per_5 = tf.tensor_scatter_nd_add(
    scores,
    sidx,
    update_score_5
)
```
Il docente verifica a mano sul tensore stampato (cella `[6]`): «dobbiamo cercare lo studente… abbiamo 22, 11 \[prima\]… e diventa 24, 13. E potete vedere che abbiamo fatto l'aggiornamento». Gli output salvati confermano: la riga 4 del primo modulo passa da `[22, 11, 5, 5, 22]` a `[24, 13, 7, 7, 24]`.
**Il problema, e la correzione.** `TF-03 @ 00:12:00`: «c'è un problema, perché se lo score era 28, quando aggiungiamo il 2 diventa 30. Vedete qua c'è un voto 32: questo non va bene per noi». Il 32 è visibile nell'output salvato dell'ultimo modulo: `[18, 21, 20, 30, 32]`. La soluzione è `tf.minimum`. Cella `[7]`:
```python
scores_update_per_5_cut = tf.minimum(
    scores_update_per_5, 30
)
scores_update_per_5_cut
```
Nell'output della stessa cella quel `32` è diventato `30`.
Il docente legge il tooltip a schermo: «Returns the min of x and y (i.e. x \< y ? x : y) element-wise. Both inputs are number-type tensors (except complex). `minimum` expects that both tensors have the same `dtype`.» E spiega il broadcasting: «lui mi ritorna la stessa shape di `scores_update_per_5` e mi fa una specie di broadcast, che fa il confronto del minimo per tutti i valori».
> **Nota.** Nel frame `TF-03 @ 00:13:12` gli argomenti di `tf.minimum` sono coperti dal tooltip della firma: **\[illeggibile\]** a schermo. Il blocco qui sopra viene dal notebook ufficiale, quindi il punto è risolto.
**A cosa serve davvero.** `TF-03 @ 00:14:00`: «questo è l'esempio, ma possiamo considerare che a un certo punto vogliamo fare qualcosa che… se abbiamo un'immagine e per un'area ci interessa più precisione sui pixel di quell'area. Possiamo fare la stessa cosa quando facciamo l'aggiornamento del gradiente, durante l'addestramento».
---
## 3. `tensor_scatter_nd_update` — `TF-03 @ 00:15:00`
Variante: invece di **sommare**, **sostituire**. L'esempio: il secondo studente del primo modulo deve avere 30 in ogni materia. Celle `[8]`, `[9]`, `[10]`:
```python
# 2dn studenti, per 1 modulo per ogni matiere deve 30
sindex = [
    [0, 1, ma] for ma in range(5)
]
```
```python
updates_2 = tf.constant([30, 30, 30, 30, 30], dtype=tf.int32)
```
```python
scores_per_2 = tf.tensor_scatter_nd_update(
    scores,
    sindex,
    updates_2
)
scores_per_2
```
Nell'output la seconda riga del primo modulo è `[30, 30, 30, 30, 30]`, e il resto del tensore è quello originale — la prova che `update` **sostituisce** e non somma.
Il docente precisa che la famiglia è più ampia: «ricordate che ci sono anche altre funzioni, non solo `update`; potete fare anche altre operazioni».
> **Divergenza minore.** A schermo il docente scrive gli aggiornamenti come `[30] * 5`; nel notebook salvato la lista è scritta per esteso, `[30, 30, 30, 30, 30]`. Stesso risultato. Vedi `day-02-divergenze.md` §1.
---
## 4. `tf.where`: selezionare per condizione — `TF-03 @ 00:19:00`
La motivazione: «c'è un altro operatore che si chiama `where`, ed è più o meno per selezionare — ma invece di dare l'indice, perché forse non lo sappiamo, vogliamo sapere l'indice **data una condizione**».
**Forma a un argomento** — restituisce gli indici. Cella `[11]`:
```python
# tf.where

consta = tf.constant(
    [[1, -1, 1],
     [2, -2, 2],
     [3, -3, 3]
     ]
)

tf.where(consta < 0)
```
```javascript
<tf.Tensor: shape=(3, 2), dtype=int64, numpy=
array([[0, 1],
       [1, 1],
       [2, 1]])>
```
**Forma a tre argomenti** — condizione, valore se vero, valore se falso. Cella `[12]`:
```python
b = tf.where(
    consta < 0,
    tf.fill(
        consta.shape,
        0
    ),
    consta
)
b
```
```javascript
<tf.Tensor: shape=(3, 3), dtype=int32, numpy=
array([[1, 0, 1],
       [2, 0, 2],
       [3, 0, 3]], dtype=int32)>
```
**Un errore di tipo, e la lezione che ne trae.** `TF-03 @ 00:22:30`: il primo tentativo fallisce perché `tf.fill` produce interi mentre il tensore è di un altro tipo. Il docente: «ricordiamo anche che quando definiamo una costante e non definiamo il tipo, lui di default prende il tipo da Python, e da Python ogni numero così è un integer. Io ho dimenticato di mettere il float».
E riassume la firma: «il primo argomento è la condizione, e poi l'operazione è applicata a cosa».
> **Solo nel video.** Il tentativo fallito non lascia traccia nel notebook salvato: la cella `[12]` contiene già la versione che funziona. L'errore è visibile solo a `TF-03 @ 00:22:58`, dove il messaggio dell'`InvalidArgumentError` è tagliato dal bordo destro della finestra — **\[illeggibile\]**.
---
## 5. `concat` e `stack` — `TF-03 @ 00:24:00`
Il docente parte dal confronto con Python: «avete già visto che su Python, per fare una concatenazione, basta fare un'addizione. Su TensorFlow usiamo `tf.concat`».
Cella `[13]`:
```python
# concat
tensor1 = tf.constant([[1,2,3], [3,4,5]])
tensor2 = tf.constant([[1,2,3], [3,4,5]])

tensor3 = tf.concat(
    [tensor1, tensor2],
    axis=0
)
tensor3
```
```javascript
<tf.Tensor: shape=(4, 3), dtype=int32, numpy=
array([[1, 2, 3],
       [3, 4, 5],
       [1, 2, 3],
       [3, 4, 5]], dtype=int32)>
```
Il vincolo: «dobbiamo avere la stessa dimensione per fare una concatenazione… per assicurarvi un comportamento corretto del codice dovete capire che avremo la stessa dimensione, se no avremo un tensore che è difficile \[da interpretare\]».
**`stack`**** è diverso.** `TF-03 @ 00:26:30`: «`concat` attacca solo dalla parte dell'asse lungo cui vogliamo concatenare; per lo `stack`, invece, per attaccare i due tensori questi devono avere proprio **lo stesso shape**. Anche se definiamo che vogliamo farlo rispetto a un asse, i tensori devono avere lo stesso shape».
Cella `[14]`:
```python
stacked = tf.stack(
    [tensor1,
     tensor2],
     axis=0
)
stacked
```
```javascript
<tf.Tensor: shape=(2, 2, 3), dtype=int32, numpy=
array([[[1, 2, 3],
        [3, 4, 5]],

       [[1, 2, 3],
        [3, 4, 5]]], dtype=int32)>
```
Due tensori `(2, 3)` concatenati su `axis=0` danno `(4, 3)`; impilati danno `(2, 2, 3)`. È la differenza in una riga: `concat` **allunga** un asse esistente, `stack` **ne aggiunge uno nuovo**.
Il tooltip letto a schermo: «Stacks a list of rank-`R` tensors into one rank-`(R+1)` tensor.»
**Perché conta.** `TF-03 @ 00:28:30`: «quello che facciamo è definire direttamente una lista degli input, e questo diventa direttamente, quando lo trasformiamo in un tensore, la prima dimensione, che diventa la dimensione del **batch**. Possiamo fare lo `stack` per creare un input: vi crea direttamente dall'asse 0 il batch».
---
## 6. `split` — `TF-03 @ 00:29:00`
L'operazione inversa: «supponiamo che abbiamo un tensore installato oppure concatenato, possiamo usare `tf.split` per dividerlo… in segmenti di sotto-tensori».
Celle `[15]`, `[16]`, `[17]`:
```python
# tf.split
tensor = tf.range(10)
splited = tf.split(
    tensor,
    num_or_size_splits=5
)
```
```python
tensor
```
```javascript
<tf.Tensor: shape=(10,), dtype=int32, numpy=array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int32)>
```
```python
splited
```
```javascript
[<tf.Tensor: shape=(2,), dtype=int32, numpy=array([0, 1], dtype=int32)>,
 <tf.Tensor: shape=(2,), dtype=int32, numpy=array([2, 3], dtype=int32)>,
 <tf.Tensor: shape=(2,), dtype=int32, numpy=array([4, 5], dtype=int32)>,
 <tf.Tensor: shape=(2,), dtype=int32, numpy=array([6, 7], dtype=int32)>,
 <tf.Tensor: shape=(2,), dtype=int32, numpy=array([8, 9], dtype=int32)>]
```
Dieci elementi divisi in cinque parti: cinque tensori da due. Il risultato è una **lista Python di tensori**, non un tensore.
---
## 7. `reduce_sum` e `map_fn` — `TF-03 @ 00:30:30`
Il ponte con NumPy: «ricordate che, come su NumPy abbiamo il mapping e il reduce, su TensorFlow abbiamo già quel tipo di funzioni».
Celle `[18]`, `[19]`, `[20]`:
```python
# map reduce

tensor = tf.constant([[1, 1], [2, 2]])
sum_all = tf.reduce_sum(
    tensor
)
sum_all
```
```javascript
<tf.Tensor: shape=(), dtype=int32, numpy=6>
```
```python
sum_all_1 = tf.reduce_sum(
    tensor,
    axis=1
)
sum_all_1
```
```javascript
<tf.Tensor: shape=(2,), dtype=int32, numpy=array([2, 4], dtype=int32)>
```
```python
sum_all_kd = tf.reduce_sum(
    tensor,
    keepdims=True
)
sum_all_kd
```
```javascript
<tf.Tensor: shape=(1, 1), dtype=int32, numpy=array([[6]], dtype=int32)>
```
Senza asse somma tutto e restituisce uno **scalare** (rango 0); con `axis=1` somma per riga; con `keepdims=True` il rango è conservato e il risultato è `(1, 1)` invece di `()`.
**`map_fn`** applica una funzione elemento per elemento. Cella `[21]`, `TF-03 @ 00:36:12`:
```python
def square(x):
    return x*x

tensor = tf.constant([1, 2, 3, 4])
squared_tensor = tf.map_fn(
    square,
    tensor
)
squared_tensor
```
```javascript
<tf.Tensor: shape=(4,), dtype=int32, numpy=array([ 1,  4,  9, 16], dtype=int32)>
```
E subito sotto, l'equivalente Python messo a confronto. Cella `[22]`:
```python
l = [1, 2, 3, 4]
lq = list(map(lambda x: x*x, l))
lq
```
```javascript
[1, 4, 9, 16]
```
Cella `[23]` resta un solo commento, l'esercizio che il docente lascia aperto:
```python
# exo: combination of map reduce and map fn
```
---
## 8. Broadcasting — `TF-03 @ 00:40:12`
Prima il caso più semplice, tensore più scalare. Cella `[24]`:
```python
# broadcast

a = tf.constant(
    [1, 2, 3]
)
b = tf.constant(1)

ss = a + b
ss
```
```javascript
<tf.Tensor: shape=(3,), dtype=int32, numpy=array([2, 3, 4], dtype=int32)>
```
Poi il broadcasting implicito fra un vettore e una matrice. Cella `[25]`:
```python
vector = tf.constant([1,0, 1])
matrix = tf.constant([[1, 2, 3], [4, 5, 6]])
sm = vector + matrix
sm
```
```javascript
<tf.Tensor: shape=(2, 3), dtype=int32, numpy=
array([[2, 2, 4],
       [5, 5, 7]], dtype=int32)>
```
Il vettore `(3,)` viene esteso alle due righe della matrice `(2, 3)` senza che nessuno lo chieda: è la regola che rende scrivibile `XW + b` senza replicare il bias.
**La forma esplicita** è `tf.broadcast_to`. Cella `[27]`:
```python
a = tf.constant(
    [[1], [2], [3]]
)
tf.broadcast_to(
    a, [3, 6]
)
```
```javascript
<tf.Tensor: shape=(3, 6), dtype=int32, numpy=
array([[1, 1, 1, 1, 1, 1],
       [2, 2, 2, 2, 2, 2],
       [3, 3, 3, 3, 3, 3]], dtype=int32)>
```
> **Nota sull'ordine.** Nel notebook la cella `[27]` viene **dopo** la cella `[26]`, che è l'esercizio del dense layer della sezione 9 (i contatori di esecuzione lo confermano: 39 per il dense layer, 41 per `broadcast_to`). Qui è riportata insieme alle altre due per unità di argomento; nel video l'ordine è quello del notebook.
---
## 9. Simulazione di un dense layer — `TF-03 @ 00:44:12`
L'esercizio che il docente si era lasciato: costruire a mano ciò che fa un layer denso. Cella `[26]`:
```python
input = tf.random.normal([64, 10])
weights = tf.random.normal([10, 5])
bias = tf.random.normal([5])

outputs = tf.matmul(input, weights) + bias
outputs.shape
```
```javascript
TensorShape([64, 5])
```
64 esempi con 10 feature entrano, 5 uscite escono: è esattamente la formula `Y = XW + b` che il docente aveva enunciato nella giornata 1. Il `bias` di shape `(5,)` si somma a una matrice `(64, 5)` per broadcasting — la regola della sezione 8, applicata.
---
## 10. Funzioni di attivazione — `TF-03 @ 00:51:12`
Cella `[28]`:
```python
# tensorflow
# activation
x = tf.constant([-1.0, 0.0, 1.0, 2.0])

tf.print("relu: ", tf.nn.relu(x))
tf.print("Sigmoid: ", tf.nn.sigmoid(x))
tf.print("Tanh: ", tf.nn.tanh(x))
```
```javascript
relu:  [0 0 1 2]
Sigmoid:  [0.268941432 0.5 0.731058598 0.880797088]
Tanh:  [-0.761594176 0 0.761594176 0.964027584]
```
Poi le stesse funzioni **riscritte a mano con NumPy** e disegnate, per vedere la forma delle curve. Cella `[29]`, `TF-03 @ 00:55:34`:
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([-1.0, 0.0, 1.0, 2])

relu_y = np.maximum(0, x)
sigmoid_y = 1 / ( 1 + np.exp(-x))
tanh_y = np.tanh(x)

x_points = np.linspace(-5.0, 5.0, 400)
relu_y_p = np.maximum(0, x_points)
sigmoid_y_p = 1 / ( 1 + np.exp(-x_points))
tanh_y_p = np.tanh(x_points)

plt.figure(figsize=(8,6))

# plt.plot(x, relu_y, label='relu')
# plt.plot(x, sigmoid_y, label='sigmoid')
# plt.plot(x, tanh_y, label='tanh')

plt.plot(x_points, relu_y_p, label='relu')
plt.plot(x_points, sigmoid_y_p, label='sigmoid')
plt.plot(x_points, tanh_y_p, label='tanh')
```
> **Le tre righe commentate sono il registro della lezione.** Il docente disegna **prima** i quattro punti di `x`, ottiene tre spezzate illeggibili, e a `TF-03 @ 00:56:34` rifà il grafico su `x_points = np.linspace(-5.0, 5.0, 400)` per avere curve lisce. Invece di cancellare le prime tre `plt.plot` le **commenta**, ed è per questo che nel notebook salvato ci sono entrambe le versioni nella stessa cella. La ReLU resta piatta a zero e poi sale lineare; sigmoide e tangente iperbolica hanno la classica forma a S, con la tanh centrata in zero e la sigmoide fra 0 e 1.
---
## 11. Pooling, e l'errore che il docente si porta dietro — `TF-03 @ 01:02:50`
Il tensore di partenza, cella `[30]`:
```python
# pooling
input_tensor = tf.constant([[[[1.0], [2.0], [3.0], [4.0],
                              [5.0], [6.0], [7.0], [8.0],
                              [9.0], [10.0], [11.0], [12.0],
                              [13.0], [14.0], [15.0], [16.0]
                              ]]])
input_tensor.shape
```
```javascript
TensorShape([1, 1, 16, 1])
```
Un solo esempio, altezza 1, larghezza 16, un canale: una riga di sedici numeri, scelta apposta perché il massimo di ogni finestra si veda a occhio.
Cella `[32]`, nella versione finale:
```python
input_tensor = tf.constant([[[[1.0], [2.0], [3.0], [4.0],
                              [5.0], [6.0], [7.0], [8.0],
                              [9.0], [10.0], [11.0], [12.0],
                              [13.0], [14.0], [15.0], [16.0]
                              ]]])
max_pool = tf.nn.max_pool2d(
    input_tensor,
    ksize=[1, 1, 2, 1],
    strides=[1, 1, 1, 1],
    padding='VALID'
)
tf.print("max: ", max_pool)
```
```javascript
max:  [[[[2]
   [3]
   [4]
   ...
   [14]
   [15]
   [16]]]]
```
Finestra larga 2 che scorre di 1: quindici massimi, da 2 a 16.
### L'errore, e come si legge nel notebook salvato
Il tentativo non riesce al primo colpo, e stavolta **il notebook salvato ne conserva la traccia**. La cella `[33]` è:
```python
max_pool.shape
```
```javascript
TensorShape([1, 0, 8, 1])
```
Quell'output **non corrisponde alla cella ****`[32]`**** che sta sopra**: con `ksize=[1, 1, 2, 1]` e `strides=[1, 1, 1, 1]` la forma sarebbe `[1, 1, 15, 1]`. È un output **rimasto indietro** — i contatori di esecuzione lo dicono: la cella `[32]` è stata eseguita per ultima (contatore 80), la `[33]` molto prima (contatore 59).
Da `[1, 0, 8, 1]` si risale ai parametri che l'hanno prodotto: `ksize=[1, 2, 2, 1]` con `strides=[1, 2, 2, 1]`. Su un input alto **1**, una finestra alta **2** non ci sta: `(1 − 2) / 2 + 1 = 0`. La seconda dimensione va a zero e il tensore risultante è **vuoto**.
**Ed è esattamente quello che il docente racconta**, molto più tardi, a `TF-03 @ 01:30:30`, quando ci ritorna sopra dall'altro notebook: «mi dispiace, infatti il problema era la dimensione, lo shape dell'input, che infatti era sbagliato… perché se io lo faccio 2-2, questo infatti mi dà un **empty**». E a `01:32:00`: «per farlo funzionare ho dovuto solo modificare il size — il \[k\]size è infatti 2, allora lo applico da qua, per ogni 2 — e poi lo stride, che rimette lo step, posso definire anche 1 se vogliamo, così li fa prima 2, poi 3, lo fa così».
<callout icon="➕">
	**Nota aggiunta:** la deduzione aritmetica su `[1, 0, 8, 1]` è mia; il docente non enuncia i numeri. Il conto è però verificabile in una riga, e coincide con quello che lui descrive a parole («2-2 mi dà un empty»). Il calcolo è confermato per esecuzione in `VERIFICA-day-02.md`.
</callout>
---
## 12. `softmax`, `argmax`, `one_hot` — `TF-03 @ 01:06:34`
Cella `[34]`:
```python
# softmax
logits = tf.constant([1.0, 3.0, 4.0])

softmax_probs = tf.nn.softmax(logits)

tf.print(softmax_probs)
```
```javascript
[0.0351190232 0.25949645 0.705384493]
```
Tre punteggi grezzi diventano tre probabilità che sommano a 1. Cella `[35]` prende la classe vincente:
```python
predict = tf.argmax(logits)
tf.print(predict)
```
```javascript
2
```
Cella `[36]`, `TF-03 @ 01:11:00` — la codifica one-hot delle etichette:
```python
labels = tf.constant([0,1,2])
one_hot = tf.one_hot(labels, depth=3)
tf.print(one_hot)
```
```javascript
[[1 0 0]
 [0 1 0]
 [0 0 1]]
```
Il docente sul `depth`: «questa è la lunghezza, perché ovviamente questo lo facciamo per i multiclassi e dobbiamo dare la lunghezza, il numero di classe». E sul risultato: «è più o meno una trasformazione binaria».
Il tooltip letto a schermo: «Returns a one-hot tensor. See also `tf.fill`, `tf.eye`. The locations represented by indices in `indices` take value `on_value`, while all other locations take value `off_value`.»
---
## 13. `dropout` e `batch_normalization` — `TF-03 @ 01:12:00`
Il docente premette che sono le versioni «grezze» di due strati che in Keras si scrivono in una riga: «tanto questa cosa che noi vediamo viene solo quando usiamo TensorFlow, ma poi abbiamo anche l'alternativa di questo, la stessa cosa su Keras».
**Dropout** — «facciamo un freezing di alcuni valori random dentro il tensore». Cella `[37]`:
```python
# droput
x = tf.constant(
    [[1.0, 2.0, 3.0, 4.0]]
)
dropout = tf.nn.dropout(
    x, rate=0.5
)
tf.print(dropout)
```
```javascript
[[0 0 6 0]]
```
Su quattro valori con `rate=0.5`, tre vanno a zero e uno passa. E non passa uguale: il `3.0` diventa `6`. È il **riscalamento** che `tf.nn.dropout` applica ai sopravvissuti, dividendo per `1 − rate`, così che la somma attesa resti la stessa. Il docente si limita a constatare la parte visibile: «lui infatti diventa 0, alcuni di questi valori».
Sul seed, `TF-03 @ 01:14:00`: «visto che non ho il seed, allora lui può fare sempre a 50% di questo tensore» — cioè a ogni esecuzione la maschera cambia.
**Batch normalization** — la motivazione è storica, `TF-03 @ 01:14:30`: «quando era nata la convolutional neural network era molto grande e poi pesante, ma noi vogliamo usare su un device più piccolo, e poi c'era ad esempio il **MobileNet**… un'architettura che usa il convolutional network, ma usa in particolare quello che si chiama batch normalization». E la definizione: «non solo che dobbiamo fare la normalizzazione dei dati, dell'input, prima che facciamo l'addestramento, ma lui fa **per ogni batch**. E questo dà anche il vantaggio di velocizzare un po'».
Cella `[38]`:
```python
# bathcnormalization
z = tf.constant([[1.0, 2.0], [3.0, 4.0]])
normalized = tf.nn.batch_normalization(
    z,
    mean=tf.reduce_mean(z),
    variance=tf.math.reduce_variance(x),
    offset=None,
    scale=None,
    variance_epsilon=1e-5
)
tf.print(normalized)
```
```javascript
[[-1.34163547 -0.447211862]
 [0.447211742 1.34163547]]
```
La costruzione è faticosa e il docente la fa a tentativi, leggendo la firma: «mi sa che avrei bisogno di alcuni argomenti… offset, scale, che infatti non mi serve… e poi variance epsilon, cosa è questo? "Small float… divide by zero"… questo è un piccolo valore che noi, quando abbiamo un valore minimo, possiamo considerare come questo, così lui non fa \[una divisione per zero\]».
E spiega la forma scelta: «io l'ho fatta a due dimensioni perché qua abbiamo solo un singolo batch… questa è la dimensione del batch e questo è l'input. Abbiamo due batch qua».
> **Un refuso nel notebook ufficiale**
>
> La `variance` è calcolata su **`x`**, non su `z`: `tf.math.reduce_variance(x)`. `x` è il tensore della cella precedente, `[[1.0, 2.0, 3.0, 4.0]]` — quello del dropout. La normalizzazione usa quindi la media di `z` e la varianza di un **altro** tensore.
>
> Il conto torna: media di `z` = 2.5, varianza di `x` = 1.25, e `(1 − 2.5) / √1.25 = −1.3416`, che è il primo valore dell'output. Con la varianza di `z` (che vale 1.25 anch'essa, per coincidenza dei due campioni) il risultato sarebbe identico — **il refuso non si vede**, ma c'è, ed è per caso che non produce danni. Vedi `day-02-divergenze.md` §2.
**`clip_by_value`**, `TF-03 @ 01:19:30`, viene solo nominata: «forse non avevo bisogno, una `clip_by_value`. Questo è più o meno un'altra operazione che usiamo su TensorFlow». Non compare in nessuna cella del notebook.
## Notebook della lezione
I file originali del docente, sul tuo Mac in `Downloads/TensorFlow-MDA/Materiale Sito/estratti/`:
- `12-06-2025/12-06-2025/notebooks/12-06-2025.ipynb`
