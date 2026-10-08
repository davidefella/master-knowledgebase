# 04 - API low-level dei tensori
> Fonte Notion: https://app.notion.com/p/3d612abc808d819c9060c64e2da9bcef — ultima modifica 2026-09-09T13:08:10.100Z

> Giornata 1, sezioni 22–33 · video `TF-01` e `TF-02`
**Allegati:** `giornata-01-tensori-ricostruito.ipynb` (notebook ricostruito ed eseguito: 38 celle su 38 girano, i 4 errori attesi corrispondono), `VERIFICA-day-01.md`, `api-explorations.ipynb` (versione ufficiale distribuita, con altre variabili)
---
## 22. Ricostruzione dell'ambiente e apertura sui tensori — `TF-01 @ 01:26:00` → `TF-02 @ 00:03:00`
> Questa sezione **attraversa il taglio fra i due file**: comincia in TF-01 e prosegue senza soluzione di continuità in TF-02.
Il docente propone agli studenti di seguire in parallelo: chi non ha ancora installato Python e VS Code può usare Google Colab, creando un nuovo notebook dal Drive (*New notebook in Drive*), che finisce in una cartella chiamata `Colab Notebooks`.
Lui rifà invece il percorso locale da zero, cancellando la cartella precedente. Precisa che userà **solo la CPU**: la sua macchina ha poca memoria video e si scalda.
**La sequenza completa, aggiunta agli appunti** (`TF-01 @ 01:28:30`–`01:31:00`):
```bash
python3 -m pip install virtualenv
python3 -m virtualenv <nome>
```
Per l'attivazione ci sono due strade:
- **la più semplice**, usare le estensioni di VS Code — vanno installate le estensioni **Python** e **Jupyter**;
- **su Linux**, `source <nome>/bin/activate`.
Poi si installano `jupyter`, `tensorflow` (variante **CPU**) e `matplotlib`.
**Il notebook della seconda parte** (`TF-01 @ 01:31:30`). Il docente crea `notebooks/10-06-2025.ipynb`, seleziona il kernel del virtualenv e mostra come inserire una **cella markdown** per i commenti — la intitola *days 1: variables*.
```python
import tensorflow as tf
import numpy as np
```
Spiega perché serve **NumPy**: è una libreria che lavora su liste ottimizzate; qui serve per le operazioni sui tensori, e TensorFlow la usa per alcune funzioni. Non va installata a parte: **viene installata automaticamente insieme a TensorFlow**.
Output (2.8 s):
```javascript
[...] 17:49:52.474321: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use availa[illeggibile] the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
```
Cella `[2]`:
```python
tf.config.get_visible_devices()
```
```javascript
[PhysicalDevice(name='/physical_device:CPU:0', device_type='CPU')]
```
**L'apertura del tema** (`TF-01 @ 01:34:30`). Il docente introduce le **variabili** con un'analogia: è come imparare una lingua nuova, si comincia dalle variabili e dai tipi di dato, che qui sono i **tensori**.
Cella `[3]` — la cella markdown di sezione:
```python
# variables, data types (tensor)
```
Cella `[4]`:
```python
row, col = 3, 3
```
**Qui cade il taglio fra TF-01 e TF-02.** La spiegazione riprende immediatamente in TF-02, sulla stessa cella.
---
## 23. Creare un tensore: shape e dtype — `TF-02 @ 00:00:00`
Per definire un tensore servono due cose: la **shape**, cioè la dimensione, e il **tipo**.
Sulla shape il docente insiste su una regola di lettura: **l'ultima dimensione è quella più interna**, la prima da sinistra è quella più esterna. È l'ordine che torna ogni volta che si manipolano le forme.
Sul tipo: per difetto TensorFlow usa **float a 32 bit**, ma esistono dispositivi a 16 o a 64 bit. La scelta dipende dalla precisione che serve. Il docente descrive il caso tipico: durante l'addestramento su GPU si lavora in genere a 32 bit; quando il modello va poi **deployato**, per esempio su un telefono, si può scendere di precisione per velocizzare l'inferenza `[?]`.
```python
# zeros
zeros = tf.zeros(
    shape=[row, col],
    dtype=tf.float32
)
zeros
```
```javascript
<tf.Tensor: shape=(3, 3), dtype=float32, numpy=
array([[0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.]], dtype=float32)>
```
---
## 24. Tensori precompilati: zeros, ones, constant, fill, zeros_like — `TF-02 @ 00:03:00`
Se invece degli zeri serve una matrice di uni si usa `tf.ones`, e senza specificare il tipo si ottiene di nuovo `float32` per difetto:
```python
# ones
ones = tf.ones([row, col])
ones
```
```javascript
<tf.Tensor: shape=(3, 3), dtype=float32, numpy=
array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]], dtype=float32)>
```
**`tf.constant`** è diverso: qui i valori si danno esplicitamente, e la forma discende da essi. Il docente nota che senza `dtype` il tensore eredita il tipo dei letterali Python — cioè `int32` — e che si può forzare a virgola mobile:
```python
constant = tf.constant([
    [2, 2, 2],
    [2, 2, 2],
    [2, 2, 2]
], dtype=tf.float32)
constant
```
```javascript
<tf.Tensor: shape=(3, 3), dtype=float32, numpy=
array([[2., 2., 2.],
       [2., 2., 2.],
       [2., 2., 2.]], dtype=float32)>
```
Cella `[11]` e `[12]` — i due attributi che si consultano sempre:
```python
constant.shape
```
```javascript
TensorShape([3, 3])
```
```python
constant.dtype
```
```javascript
tf.float32
```
**`tf.fill`** riempie una forma data con un valore dato. L'ordine degli argomenti è l'inverso di `tf.constant`: prima la forma, poi il valore.
Cella `[14]`:
```python
filled = tf.fill(
    [row, col],
    2.0
)
filled
```
```javascript
<tf.Tensor: shape=(3, 3), dtype=float32, numpy=
array([[2., 2., 2.],
       [2., 2., 2.],
       [2., 2., 2.]], dtype=float32)>
```
**`tf.zeros_like`** risolve un problema pratico: creare un tensore di zeri **con la stessa forma** di uno esistente. Senza di esso bisognerebbe estrarre la forma e ripassarla, e la forma è un `TensorShape`, non una lista.
Cella `[15]`:
```python
zeros_like = tf.zeros_like(constant)
zeros_like
```
```javascript
<tf.Tensor: shape=(3, 3), dtype=float32, numpy=
array([[0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.]], dtype=float32)>
```
Per convertire una forma in lista Python serve `list()`:
Cella `[18]`:
```python
list(constant.shape)
```
```javascript
[3, 3]
```
> **Un avvertimento che il docente anticipa qui e riprenderà più avanti** (`TF-02 @ 00:07:30`): `list()` è una funzione Python, e **non si dovrebbero mescolare Python e TensorFlow**. Il motivo è duplice: le prestazioni del codice, e la difficoltà di fare debug quando il comportamento diventa imprevedibile. La spiegazione completa arriva nella sezione 32.
---
## 25. linspace e range — `TF-02 @ 00:08:30`
Due modi per generare una successione.
**`tf.linspace`** vuole inizio, fine e **numero di segmenti**; gli estremi sono inclusi.
```python
# linear space
linear_space = tf.linspace(
    start=0.0,
    stop=1.0,
    num=10
)
linear_space
```
```javascript
<tf.Tensor: shape=(10,), dtype=float32, numpy=
array([0.        , 0.11111111, 0.22222222, 0.33333334, 0.44444445,
       0.5555556 , 0.6666667 , 0.7777778 , 0.8888889 , 1.        ],
      dtype=float32)>
```
**`tf.range`** vuole invece inizio, limite e **passo**:
Cella `[20]`:
```python
range_tns = tf.range(
    start=0,
    limit=1,
    delta=0.1111
)
range_tns
```
```javascript
<tf.Tensor: shape=(10,), dtype=float32, numpy=
array([0.        , 0.1111    , 0.2222    , 0.3333    , 0.4444    ,
       0.55550003, 0.6666    , 0.7777    , 0.8888    , 0.99990004],
      dtype=float32)>
```
---
## 26. Tensori casuali e a cosa servono — `TF-02 @ 00:11:00`
Il docente collega subito la funzione al suo uso reale: **l'inizializzazione dei pesi** di una rete richiede tensori riempiti con valori casuali.
**`tf.random.normal`** vuole, oltre alla forma, i parametri della distribuzione: media e deviazione standard.
Cella `[22]`:
```python
# random normals
random_normal_tns = tf.random.normal(
    shape=[row, col],
    mean=0.0,
    stddev=1.0
)
random_normal_tns
```
```javascript
<tf.Tensor: shape=(3, 3), dtype=float32, numpy=
array([[ 1.7849394 ,  1.5338212 , -1.4150164 ],
       [-1.3422459 ,  0.66299826,  0.16964512],
       [-0.25516132,  2.2990425 ,  0.7391626 ]], dtype=float32)>
```
**`tf.random.uniform`** pesca invece da un intervallo, con probabilità uniforme:
Cella `[23]`:
```python
# random uniform in a set
random_uniform = tf.random.uniform(
    shape=[row, col],
    minval=0,
    maxval=10
)
random_uniform
```
```javascript
<tf.Tensor: shape=(3, 3), dtype=float32, numpy=
array([[9.500458  , 0.55546165, 4.533882  ],
       [7.9240966 , 5.6271515 , 8.06467   ],
       [7.006363  , 7.6108847 , 0.0582087 ]], dtype=float32)>
```
Il docente indica un secondo impiego dell'uniforme, oltre all'inizializzazione: il **dropout**. Nel layer di dropout si vogliono spegnere alcuni neuroni della rete; si fissa una percentuale — per esempio il 50% — e a ogni epoca si estrae uniformemente quali spegnere.
---
## 27. Perché servono le trasformazioni di forma: il batch — `TF-02 @ 00:16:00`
Prima di mostrare le funzioni, il docente spiega **perché** servono, e il motivo è sempre lo stesso: **la dimensione del batch**.
Durante l'addestramento i dati entrano nella rete a blocchi: se il batch è di 10 immagini, l'output di ogni passo porta con sé quella dimensione. Ma **in inferenza** si predice una cosa sola: quella dimensione diventa 1, ed è di troppo — va tolta con `squeeze`. Simmetricamente, un singolo input va **espanso** per assomigliare a un batch di uno prima di entrare nella rete: è `expand_dims`.
Il collegamento che il docente stabilisce è dunque:
- **`squeeze`**** → sull'output**, per togliere la dimensione di batch superflua;
- **`expand_dims`**** → sull'input**, per aggiungerla.
`tf.reshape` è invece la trasformazione generale: dato un tensore e una nuova forma, riorganizza le dimensioni. Serve quando il dataset fornisce un tensore a una dimensione ma l'architettura del modello ne vuole due.
---
## 28. reshape, squeeze, expand_dims — `TF-02 @ 00:21:00`
```python
a = tf.range(row * col - 1)
a.shape
```
```javascript
TensorShape([12])
```
**L'errore, e a cosa serve.** Il docente prova prima una forma incompatibile — 12 elementi in una matrice 3×3, che ne vuole 9:
```python
b = tf.reshape(
    a,
    (row, col)
)
b
```
```javascript
InvalidArgumentError: {{function_node __wrapped__Reshape_device_/job:localhost/replica:0/task:0/device:CPU:0}} Input to [illeggibile]
```
«Mi dà un errore perché lui non può fare un reshape del 12 per 9» (`TF-02 @ 00:22:30`). Corretta la forma in `(3, 4)`, la cella funziona.
**squeeze.** Si costruisce un tensore con due dimensioni unitarie:
```python
sx = tf.random.normal([1, 10, 1, 30])
sx.shape
```
```javascript
TensorShape([1, 10, 1, 30])
```
```python
sx_squeezed = tf.squeeze(sx)
sx_squeezed.shape
```
```javascript
TensorShape([10, 30])
```
Il punto che il docente sottolinea: **`tf.squeeze`**** toglie *tutte* le dimensioni unitarie**, non una sola.
**expand_dims.** Si torna indietro, un asse alla volta, scegliendo dove inserire la dimensione:
```python
sx_expanded = tf.expand_dims(
    sx_squeezed,
    axis=1
)
sx_expanded.shape
```
```javascript
TensorShape([10, 1, 30])
```
```python
sx_original = tf.expand_dims(
    sx_expanded,
    axis=0
)
sx_original.shape
```
```javascript
TensorShape([1, 10, 1, 30])
```
`axis=0` mette la nuova dimensione all'inizio, `axis=1` subito dopo la prima.
**La verifica.** Il docente controlla che il giro sia davvero reversibile, e ne approfitta per introdurre `.numpy()` come ponte verso il mondo NumPy:
Cella `[36]`:
```python
sx.numpy() == sx_original.numpy()
```
Output: un array di `True` di forma `(1, 10, 1, 30)`.
«Questo è solo per mostrarvi che infatti abbiamo lo stesso tensore, abbiamo solo cambiato le dimensioni e poi siamo tornati» (`TF-02 @ 00:29:30`).
---
## 29. transpose e tile — `TF-02 @ 00:30:00`
**transpose.** Su una matrice la trasposta è univoca; su un tensore con più di due dimensioni bisogna dire **quale permutazione** si vuole, con `perm`.
```python
tb = tf.random.normal(
    [100, 64, 51]
)
tb.shape
```
```javascript
TensorShape([100, 64, 51])
```
```python
tb_transposed = tf.transpose(
    tb,
    perm=[1, 2, 0]
)
tb_transposed.shape
```
```javascript
TensorShape([64, 51, 100])
```
**tile.** Il docente la spiega con un'analogia grafica: una *tile* è una piastrella, nel senso di Photoshop — un motivo i cui bordi combaciano, così che ripetendolo si ottenga un'immagine grande senza che si vedano le giunzioni. Serve, dice, quando si vuole una texture arbitrariamente estesa senza memorizzare l'immagine intera.
```python
# tiles (extra)
tile = tf.constant([[1, 2], [3, 4]])
tile
```
```javascript
<tf.Tensor: shape=(2, 2), dtype=int32, numpy=
array([[1, 2],
       [3, 4]], dtype=int32)>
```
```python
tiled = tf.tile(
    tile,
    [2, 2]
)
tiled.numpy()
```
```javascript
array([[1, 2, 1, 2],
       [3, 4, 3, 4],
       [1, 2, 1, 2],
       [3, 4, 3, 4]], dtype=int32)
```
Il secondo argomento dice **quante volte ripetere lungo ciascuna dimensione**.
---
## 30. Costanti e variabili: mutabilità e derivazione automatica — `TF-02 @ 00:36:30`
Nuova sezione markdown creata in diretta:
```markdown
# variables

mutability, should be initialized, tracked during training
```
Il docente motiva la distinzione a partire dal training loop: in un addestramento l'**input** — per esempio un'immagine — non cambia mai, mentre i **pesi** sono i parametri che vengono aggiornati. I primi sono costanti, i secondi variabili.
Le tre proprietà della `tf.Variable`, nell'ordine in cui le enuncia:
1. **mutabilità con memoria fissa**: il valore si aggiorna, ma la posizione in memoria resta la stessa;
2. **deve essere inizializzata**;
3. **è tracciata durante l'addestramento**.
Il terzo punto è quello che conta di più, e il docente lo lega alla **derivazione automatica**: quando si dichiara una `tf.Variable`, TensorFlow **sa già** che rispetto a quel valore andrà calcolata la derivata, senza doverlo dire esplicitamente. Su una costante, invece, la derivazione viene ignorata.
Aggiunge il collegamento con il salvataggio: «quando parliamo di un checkpoint di un modello, noi infatti lo salviamo in variabili», e lo stesso vale per il caricamento nel fine-tuning (`TF-02 @ 00:40:30`).
**La dimostrazione dell'immutabilità.** Cella `[45]` e `[46]`:
```python
ca = tf.constant(2)
```
```python
ca.assign(4)
```
```javascript
AttributeError                            Traceback (most recent call last)
Cell In[46], line 1
----> 1 ca.assign(4)
[...]
AttributeError: 'tensorflow.python.framework.ops.EagerTensor' object has no attribute 'assign'
```
Il messaggio completo suggerisce anche `tf.experimental.numpy.experimental_enable_numpy_behavior()`, che qui non c'entra.
**La variabile, invece, si aggiorna:**
```python
cv = tf.Variable(2)
cv.numpy()
```
```javascript
np.int32(2)
```
```python
cv.assign(4)
cv.numpy()
```
```javascript
np.int32(4)
```
**Il confronto degli ****`id()`****.** Il docente mostra che riassegnare una costante non la modifica: **crea un oggetto nuovo**. È il motivo per cui riassegnare una `tf.constant` è una cattiva pratica — «noi abbiamo già l'assign per le variabili e dobbiamo usare quello» (`TF-02 @ 00:44:00`).
Cella `[56]`:
```python
id(ca)
```
```javascript
134904439875968
```
---
## 31. Operazioni fra tensori: matmul contro multiply — `TF-02 @ 00:44:30`
Nuova sezione markdown `# operations`.
Cella `[57]` — il **prodotto matriciale**:
```python
# operations

a = tf.constant([[1,2], [3,4]])
b = tf.constant([[5,6], [7, 8]])
c = tf.matmul(a, b)
c.numpy()
```
```javascript
array([[19, 22],
       [43, 50]], dtype=int32)
```
Cella `[58]` — il **prodotto elemento per elemento**:
```python
ec = tf.multiply(a,b)
ec
```
```javascript
<tf.Tensor: shape=(2, 2), dtype=int32, numpy=
array([[ 5, 12],
       [21, 32]], dtype=int32)>
```
La differenza, nelle parole del docente: `tf.matmul` è il prodotto righe per colonne; `tf.multiply` è la moltiplicazione **element-wise**, che serve per esempio quando si implementa un kernel che scorre sull'immagine (`TF-02 @ 00:46:00`).
**La regola sulle dimensioni, e l'errore che la mostra.** Perché `matmul` funzioni, il numero di righe della seconda matrice deve essere uguale al numero di colonne della prima. Il docente costruisce apposta un caso incompatibile:
Cella `[60]`:
> **Cella non leggibile.** La cella che definisce `mm` non compare in nessun frame utilizzabile: a `TF-02 @ 00:49:00` il docente la sta ancora scrivendo (`mm = tf.constant()`, vuota) e a `TF-02 @ 00:49:49` la vista è già scrollata sul traceback. Dall'errore si deduce solo che **`mm`**** non è quadrata**, perché `matmul(mm, mm)` fallisce con *Matrix size-incompatible*. Il valore esatto richiede di riguardare il video in quei 49 secondi.
```python
mm = tf.constant(...)   # [illeggibile]
```
```python
mmprod = tf.matmul(
    mm, mm
)
```
```javascript
InvalidArgumentError: {{function_node __wrapped__MatMul_device_/job:localhost/replica:0/task:0/device:CPU:0}} Matrix siz[illeggibile]
```
E lo risolve con quanto appena imparato sulle forme:
```python
mm = tf.transpose(mm)
```
```javascript
array([[19, 32],
       [22, 77]], dtype=int32)
```
Nota che su una matrice **quadrata** `tf.transpose` non ha bisogno di `perm`: scambia semplicemente le due dimensioni. E che con `tf.multiply` il problema non si pone, perché non c'è prodotto righe-colonne.
---
## 32. tf.math, i tipi, e perché non mescolare NumPy e TensorFlow — `TF-02 @ 00:51:30`
Nuova sezione markdown `## tf.math`. Il docente elenca ciò che il modulo contiene: logaritmo, esponenziale, massimo, funzioni trigonometriche, valore assoluto, divisione.
**L'errore di tipo.** Cella `[64]`:
```python
sq = tf.math.sqrt(a)
sq
```
```javascript
InvalidArgumentError                      Traceback (most recent call last)
Cell In[64], line 1
----> 1 sq = tf.math.sqrt(a)
      2 sq
[...]
InvalidArgumentError: Value for attr 'T' of int32 is not in the list of allowed values: bfloat16, half, float, double, c[illeggibile]
 ; NodeDef: {{node Sqrt}}; Op<name=Sqrt; signature=x:T -> y:T; attr=T:type,allowed=[DT_BFLOAT16, DT_HALF, DT_FLOA[illeggibile]
```
La radice quadrata non accetta `int32`. La correzione è dichiarare il tipo.
Cella `[65]` e `[66]`:
```python
## tf.math

a = tf.constant([1,2,3], dtype=tf.float32)
# b = tf.constant([4,5,6])
```
```python
sq = tf.math.sqrt(a)
sq
```
```javascript
<tf.Tensor: shape=(3,), dtype=float32, numpy=array([1.       , 1.4142135, 1.7320508], dtype=float32)>
```
**Il perché di tutto questo** (`TF-02 @ 00:53:30`). Qui il docente dà la ragione di fondo, ed è il passaggio concettualmente più importante della seconda parte:
> «Quando definiamo una funzione di TensorFlow, noi la chiamiamo un **grafo**. E questo grafo deve usare le funzioni di TensorFlow.»
Si potrebbe calcolare la radice quadrata di un tensore con NumPy. Ma usare NumPy **dentro un grafo TensorFlow** produce comportamenti difficili da spiegare, e soprattutto rende il debug quasi impossibile. È la stessa avvertenza fatta a proposito di `list()` nella sezione 24, ora motivata.
---
## 33. gather e scatter: selezionare e aggiornare — `TF-02 @ 00:54:30`
Le ultime due operazioni della giornata rispondono a due esigenze speculari: **estrarre** un sottoinsieme di un tensore dati gli indici (`gather`), e **aggiornare** posizioni precise (`scatter`).
**Perché non un ciclo ****`for`****.** Il docente lo spiega col modello di esecuzione degli acceleratori. Su una GPU ci sono migliaia di thread; se una matrice ha la stessa dimensione dell'insieme di thread, ogni elemento può essere assegnato a un thread diverso. L'esecuzione **non è più sequenziale ma parallela**: si dichiara una condizione — per esempio «aggiorna a 5 solo il thread in posizione 0,1» — e tutti i thread la valutano insieme. Per questo `gather` e `scatter` esistono come primitive ottimizzate, e vanno usate al posto di un ciclo Python (`TF-02 @ 00:57:30`–`00:58:30`).
**L'esempio: i voti.** Un tensore a **tre dimensioni** — 8 moduli × 10 studenti × 5 materie. Il docente costruisce l'esempio a voce: i moduli sono per esempio *data science*, *data analysis*, *crittografia*; per ciascuno ci sono 10 studenti e 5 materie (per data science: TensorFlow, Neural Network, MATLAB).
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
Il docente commenta che `minval=0` «non è reale» come voto, ma serve per l'esempio; il massimo è 31 perché l'estremo superiore è escluso.
**La domanda.** Estrarre i voti relativi al **primo e al terzo modulo**.
Cella `[68]`:
```python
# scores per gli studenti first and third modules
modules_index_g = [0, 2]
g_scores = tf.gather(
    scores,
    indices=modules_index_g,
    axis=1
)
```
> **Nota sull'****`axis`****.** Nel parlato il docente esita fra `axis=0` e `axis=1` (`TF-02 @ 01:04:00`–`01:06:00`) e conclude per `axis=1`, dicendo: «l'idea è che io vorrei estrarre il valore del terzo rispetto alla seconda dimensione. Allora \[...\] nell'axis 1». Il codice riportato è quello effettivamente scritto a schermo. Va osservato che con la shape `(8, 10, 5)` l'asse dei **moduli** è lo 0 e quello degli **studenti** è l'1: l'esitazione non viene sciolta nel video, e la registrazione si interrompe prima di una verifica dell'output.
La lezione si chiude con l'assegnazione dell'esercizio per la volta successiva.
---
---
## File allegati
Il notebook ricostruito dai fotogrammi del video (il file originale del docente, `10-06-2025.ipynb`, non è mai stato distribuito) e il referto della verifica per esecuzione. Il notebook è caricato con estensione `.json` perché Notion non accetta `.ipynb`: dopo il download rinominalo in `.ipynb`.
<file src="notion-file-block://576ed622-c025-47a3-ae59-2475a520e369/b1241a55-8abd-432f-9aeb-bb6c4891ff95?space_id=98012abc-808d-816f-9733-00030a2b4817&name=giornata-01-tensori-ricostruito.json"></file>
<file src="notion-file-block://1093ce5a-e31d-441d-8d77-683adc8de786/f886c16d-d70b-438d-8a56-a6f654654c70?space_id=98012abc-808d-816f-9733-00030a2b4817&name=VERIFICA-day-01.md"></file>
