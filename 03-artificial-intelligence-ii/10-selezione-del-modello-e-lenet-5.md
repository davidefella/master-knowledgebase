# 10 - Selezione del modello e LeNet-5
> Fonte Notion: https://app.notion.com/p/3d612abc808d81af88aadcda56440228 — ultima modifica 2026-09-09T23:31:29.438Z

> Giornata 4 del corso · video `TF-07` e `TF-08`
---
## 1. Ripresa: i notebook corretti della giornata 3 — `TF-07 @ 00:00:30`
Il docente apre annunciando due file nuovi: «il notebook che ho aggiunto si chiama **NN-TensorFlow-Completed**». E poco dopo: «ho lasciato questo notebook anche nel materiale, che è già completato, ma comunque **non l'abbiamo guardato**».
Sono le versioni **corrette** dei notebook della giornata 3: `NN-TF-completed.ipynb` e `KERAS-NN-should-be-reviewed.ipynb`.
Il motivo del ritorno indietro (`TF-07 @ 00:01:00`): «il mio \[GPU\] che non è andata bene, allora torno un attimo con la lezione dell'altro ieri».
---
## 2. `KERAS-NN`: il catalogo dei layer — `TF-07 @ 00:01:30`
> **È materiale della giornata 3**, distribuito in `17-06-2025/materials.zip` e mai aperto in quella lezione. Il docente lo recupera qui: «c'è Keras, material, Keras… vi do un passo veloce veloce, per mostrare un po' alcuni dei layer che sono popolari e più usati su Keras».<br><br>La rassegna dura sette minuti, fino a `TF-07 @ 00:08:00`. Il codice viene da `17-06-2025/KERAS-NN-should-be-reviewed.ipynb`; **18 delle sue 21 celle di codice sono state compilate dal docente fuori dall'aula**, prima di distribuirlo.
Il notebook mostra ogni layer applicandolo a un tensore d'esempio e stampandone la forma d'uscita. Il valore didattico sta tutto lì: **come cambia la forma**.
`già nel materiale` — l'intestazione: «This notebook demonstrates various popular TensorFlow Keras layers, showing how each works with example inputs and outputs, including shape transformations.»
### Layer densi e di forma
`scritta in aula` — su un batch `x` di shape `(2, 8)`:
```python
# data example
x = tf.random.normal((2, 8))  # Example batch with 8 features
x.shape
```
```python
# Dense Layer
dense = tf.keras.layers.Dense(4)
y_dense = dense(x)
print("Dense Input Shape:", x.shape)
print("Dense Output Shape:", y_dense.shape)
```
«Quello che vediamo sempre è la *fully connected*, quel dense layer: potete vedere come si usa.»
```python
# Activation
activation = tf.keras.layers.Activation('relu')
y_act = activation(y_dense)
print("Activation Output Shape:", y_act.shape)
```
«Ricordate che noi possiamo anche usarla direttamente come **parametro** del dense layer alla fine, oppure definiamo proprio un'altra layer nel nostro modello.»
```python
# Dropout (in training mode to see effect)
dropout = tf.keras.layers.Dropout(0.5)
y_dropout = dropout(y_act, training=True)
print("Dropout Output Shape:", y_dropout.shape)
```
> **L'informazione operativa più importante della rassegna**, e il docente la dà senza soffermarcisi (`TF-07 @ 00:02:30`): «il dropout è per congelare un po' alcuni dei neuroni, e questo valore è la **probabilità** dei neuroni che possono essere congelati. Durante l'addestramento ovviamente, perché **questo viene cancellato quando facciamo l'inference**».<br><br>Da qui il `training=True` esplicito: chiamato fuori da un `fit`, al layer va detto in quale modalità sta.
```python
# BatchNormalization
bn = tf.keras.layers.BatchNormalization()
y_bn = bn(y_dense, training=True)
print("BatchNormalization Output Shape:", y_bn.shape)
```
«Per l'immagine facciamo una normalizzazione del batch.» Stessa avvertenza del dropout: in addestramento usa le statistiche del batch, in inferenza quelle accumulate.
```python
# Flatten
x2 = tf.random.normal((2, 4, 4))
flatten = tf.keras.layers.Flatten()
y_flat = flatten(x2)          # (2, 4, 4) -> (2, 16)
```
```python
# Reshape
reshape = tf.keras.layers.Reshape((2, 8))
y_reshape = reshape(y_flat)   # (2, 16) -> (2, 2, 8)
```
Sul `Flatten`: «al solito quando abbiamo un tensore di più di una dimensione e vogliamo applicare un dense layer». Sul `Reshape`: «si può usare anche per fare un reshape durante l'addestramento».
```python
# Concatenate
concat = tf.keras.layers.Concatenate()
y_concat = concat([x, x])     # due (2, 8) -> (2, 16)
```
```python
# Elementwise Add
add = tf.keras.layers.Add()
y_add = add([x, x])           # due (2, 8) -> (2, 8)
```
**L'esempio del ****`Concatenate`**** è il più concreto della rassegna** (`TF-07 @ 00:04:00`): «se abbiamo due input diversi — un modello che prende testo e l'altro immagine, ma alla fine vogliamo concatenare: ad esempio un'immagine e la sua *caption*, ma vogliamo usare tutto quello come input».
`Concatenate` **affianca**, `Add` **somma**: sono i due modi di unire due rami, e i mattoni delle architetture non sequenziali.
### Layer convolutivi
`scritta in aula` — su un batch di immagini `(2, 28, 28, 3)`:
```python
x_img = tf.random.normal((2, 28, 28, 3))  # Batch of images
```
```python
# conv2d
conv2d = tf.keras.layers.Conv2D(16, (3, 3), padding='same')
y_conv2d = conv2d(x_img)      # (2, 28, 28, 16) — padding 'same' conserva la dimensione
```
```python
# MaxPooling2D
pool = tf.keras.layers.MaxPooling2D((2, 2))
y_pool = pool(y_conv2d)       # (2, 14, 14, 16) — dimezza
```
```python
# Conv2DTranspose
conv2dt = tf.keras.layers.Conv2DTranspose(16, (3, 3), strides=2, padding='same')
y_conv2dt = conv2dt(y_pool)   # (2, 28, 28, 16) — raddoppia
```
`TF-07 @ 00:04:30`: «c'è la convolutional, questo ad esempio l'ho preso come due dimensioni ma potete anche il singolo dimensione. Il max pooling che viene applicato… più o meno quello che facciamo è, dopo la convolutional, applichiamo un pooling: può essere un average pooling, max pooling, global pooling».
**E poi la digressione più densa dei sette minuti** (`TF-07 @ 00:05:00`–`00:06:30`), sull'ultimo dei tre:
> «Poi c'è la **convolutional transpose**. Questo più o meno è l'inverso del convolutional… questo lo facciamo per il **decoder**. Non so se avete già sentito, in un altro corso di Neural Network, un tipo di layer si chiama **autoencoder**… Un esempio facile: per trasformare un'immagine in un QR code, che è più piccola, una piccola rappresentazione di un'immagine grande. Allora, quello che facciamo è usare un **encoder**, e poi a partire da quell'encoder vogliamo **ricostruire** l'immagine… usiamo il conv transpose per ricostruire l'immagine a partire da quel QR code. Questo si chiama **decoder**. L'encoder fa il *downscaling* e il decoder fa l'*upscaling*.»
È l'annuncio dell'ultimo progetto del corso: la super-risoluzione della giornata 5.
### Layer ricorrenti
`scritta in aula` — su una sequenza `(2, 10, 8)`: batch, tempo, feature.
```python
x_seq = tf.random.normal((2, 10, 8))  # Sequence data: batch, time, features
```
```python
# SimpleRNN
rnn = tf.keras.layers.SimpleRNN(4)
print("SimpleRNN Output Shape:", rnn(x_seq).shape)      # (2, 4)
```
```python
# LSTM
lstm = tf.keras.layers.LSTM(4)
print("LSTM Output Shape:", lstm(x_seq).shape)          # (2, 4)
```
```python
# GRU
gru = tf.keras.layers.GRU(4)
print("GRU Output Shape:", gru(x_seq).shape)            # (2, 4)
```
```python
# Bidirectional
bi_lstm = tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(4))
print("Bidirectional LSTM Output Shape:", bi_lstm(x_seq).shape)   # (2, 8)
```
`TF-07 @ 00:06:30`: «c'è Simple RNN, che è ovviamente per le *sequences*; c'è l'LSTM, che sicuramente avete già sentito; il GRU è una variante di LSTM; e poi c'è anche il **bidirectional**. Sono tutti layer che prendono input come sequenza — che oggi vediamo alcuni esempi… c'è questo 5 \[`5.CharGen-LSTM`\] che vediamo».
Tutti e tre collassano i **10 passi temporali** in un solo vettore da 4: è il comportamento di default (`return_sequences=False`). Il `Bidirectional` raddoppia l'uscita a 8, perché legge la sequenza nei due versi e concatena.
### Embedding e attenzione
`scritta in aula`:
```python
# Embedding
x_indices = tf.constant([[1, 2, 3], [4, 5, 6]])
embedding = tf.keras.layers.Embedding(input_dim=10, output_dim=4)
y_emb = embedding(x_indices)     # (2, 3) -> (2, 3, 4)
```
```python
# Additive Attention
query = tf.random.normal((2, 4, 8))
value = tf.random.normal((2, 6, 8))
attention = tf.keras.layers.AdditiveAttention()
y_attention = attention([query, value])    # (2, 4, 8)
```
`TF-07 @ 00:07:30`: «noi abbiamo già visto l'embedding, ad esempio per quella binary classification; poi anche l'**attention**, e quello è usato con il **GPT** ad esempio».
L'`AdditiveAttention` prende una *query* di 4 posizioni e un *value* di 6, e restituisce 4 posizioni: ogni posizione della query diventa una media pesata dei value. È l'unico affaccio del corso sul meccanismo che sta sotto i transformer.
E la chiusura della rassegna (`TF-07 @ 00:08:00`): «ci sono questi che ho messo su questo notebook, ma comunque ci sono **più layer** già implementati nelle API di Keras. Allora dipende dai vostri progetti, potete scegliere il layer appropriato».
---
## 3. `1.MNIST-MODEL-SELECTION`: configurazione e dati — `TF-07 @ 00:13:54`
Notebook intitolato «**Model Selection on MNIST: A Practical Guide**».
`già nel materiale` — l'intestazione, che dichiara il piano: «We'll start with a simple softmax regression, then try to incrementally improve the model using deeper neural networks and convolutional layers.»
**A che serve**, `TF-07 @ 00:09:30`: «questa è una delle strategie che io vi consiglio di usare quando avete un progetto e non siete ancora sicuri di scegliere il modello… per provare più modelli e creare un dataset che sia compatibile con alcuni modelli che noi possiamo usare».
`scritta in aula` — celle `[2]`, `[3]`, `[4]`:
```python
# config
EPOCHS = 100
BATCH_SIZE = 128
NB_CLASSES = 10
VALIDATION_SPLIT = 0.2
```
```python
# load dataset
(X_train, Y_train), (X_test, Y_test) = tf.keras.datasets.mnist.load_data()
```
```python
X_train.shape
X_test.shape
```
Tutti i parametri in testa, una volta sola: è la premessa perché il confronto fra i quattro modelli sia leale.
`scritta in aula` — celle `[5]`, `[6]`:
```python
# preprocess
X_train = X_train.reshape(60000, 28*28).astype('float32') / 255.0
X_test = X_test.reshape(10000, 28*28).astype('float32') / 255.0
```
```python
# preprocess label
Y_train = tf.keras.utils.to_categorical(Y_train, NB_CLASSES)
Y_test = tf.keras.utils.to_categorical(Y_test, NB_CLASSES)
Y_train[0]
```
Le immagini vengono **appiattite** a 784 valori e normalizzate; le etichette diventano **one-hot** con `to_categorical`. Il docente lo richiama a `TF-07 @ 00:21:00`: «visto che ho trasformato in one-hot encoded», ed è la ragione per cui in tutto il notebook si usa `categorical_crossentropy` e non la versione sparse.
> **Punto risolto dal materiale ufficiale.** Le due celle non sono mai inquadrate complete: erano **\[illeggibile\]**, e la versione precedente di questo manuale poteva solo dedurre il one-hot dal parlato.
`scritta in aula` — cella `[7]`:
```python
# show some images
indices = np.random.choice(np.arange(len(X_train)), 3, replace=False)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for i, ax in zip(indices, axes):
    im = X_train[i]
    imreshaped = im.reshape(28, 28)
    ax.imshow(imreshaped, cmap='gray')
    label = np.argmax(Y_train[i])
    ax.set_title(label)

plt.show()
```
**Diagramma** (`TF-07 @ 00:24:17`): tre cifre MNIST in scala di grigi con assi numerati 0-25. Da notare le due conseguenze del preprocessing: le immagini vanno **rimesse in forma 28×28** per essere disegnate, e il titolo si ottiene con `argmax` perché l'etichetta è ormai un vettore one-hot.
---
## 4. Il primo modello: un solo strato — `TF-07 @ 00:20:00`
`scritta in aula` — cella `[8]`:
```python
# first model
model_one = tf.keras.models.Sequential()
model_one.add(tf.keras.layers.Dense(NB_CLASSES, input_shape=(28*28,), activation="softmax"))

model_one.compile(
    optimizer=tf.keras.optimizers.SGD(), loss="categorical_crossentropy", metrics=["accuracy"] 
)
model_one.summary()
```
```javascript
Model: "sequential"
┌─────────────────────────────────┬────────────────────────┬───────────────┐
│ dense (Dense)                   │ (None, 10)             │         7,850 │
└─────────────────────────────────┴────────────────────────┴───────────────┘
 Total params: 7,850 (30.66 KB)
```
**Due scelte, entrambe motivate.** `TF-07 @ 00:20:00`: «posso fare anche così, invece di mettere direttamente nel `Sequential` — ricordate, così dovete capire **altri modi** per definire un modello». Cioè: `Sequential()` vuoto e poi `.add(...)`, invece della lista.
`TF-07 @ 00:21:00`: «invece di definire un'altra layer che si chiama `Activation`, io posso mettere direttamente un'attivazione. Visto che ho trasformato in one-hot encoded, allora non ho più bisogno di lasciare questo e fare una loss con *logit*, ma posso usare direttamente una **softmax** e lui la calcola già».
**Perché il ****`summary()`**** funziona subito.** `TF-07 @ 00:23:00`: «questa definizione, perché abbiamo messo l'`input_shape`, allora quando abbiamo fatto il `compile` possiamo vedere il summary e può trovare la stima del numero di parametri». Con un solo strato: «abbiamo solo **7000** parametri» — esattamente 784 × 10 + 10 = **7.850**.
> È il contrappunto al `summary()` a zero della giornata 3: lì `input_length` veniva ignorato e il modello restava non costruito; qui `input_shape` è dichiarato e i parametri si contano subito. Keras avvisa comunque che la forma andrebbe data con un layer `Input`:
```javascript
keras/src/layers/core/dense.py:93: UserWarning: Do not pass an `input_shape`/
`input_dim` argument to a layer...
```
`scritta in aula` — celle `[9]`, `[10]`:
```python
# train first model
model_one.fit(
    X_train, Y_train, batch_size=BATCH_SIZE, epochs=EPOCHS, validation_split=VALIDATION_SPLIT
)
```
```javascript
Epoch 100/100
375/375 ━━━━━━━━━━━━━━━━━━━━ 1s 4ms/step - accuracy: 0.9179 - loss: 0.2960 - val_accuracy: 0.9202 - val_loss: 0.2882
```
```python
model_one.evaluate(X_test, Y_test)
```
```javascript
313/313 ━━━━━━━━━━━━━━━━━━━━ 0s 1ms/step - accuracy: 0.9090 - loss: 0.3292
[0.28848475217819214, 0.9204999804496765]
```
Cento epoche per arrivare al **92.05%**, ed è in piano da un pezzo: la loss di addestramento e quella di validazione sono praticamente uguali (0.296 contro 0.288). Nessun overfitting — il modello è **troppo semplice** per andare oltre.
**`validation_split`**** contro ****`validation_data`****.** `TF-07 @ 00:24:00`. Il docente ne approfitta per un avvertimento operativo:
> «Se noi abbiamo un array così, perché abbiamo un tensore, possiamo fare la `validation_split`. Oppure possiamo mettere `X_test` e `Y_test` come `validation_data`. **Ma ricordate**: se abbiamo usato l'API di TensorFlow che crea il dataset — `tf.data.Dataset` — **non possiamo usare ****`validation_split`**, perché quel dataset è già nella cache. Allora non possiamo più dirgli di fare uno split, ma dobbiamo creare lo split da noi, manualmente.»
Il punto torna concreto nella sezione 9, dove lo split manuale diventa necessario.
---
## 5. Più profondo, e con dropout — `TF-07 @ 00:30:00`
`scritta in aula` — celle `[11]`, `[12]`, `[13]`:
```python
# depper model
model_two = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, input_shape=(28*28,), activation="relu"),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(NB_CLASSES, activation="softmax")
])

model_two.compile(
    optimizer=tf.keras.optimizers.SGD(), loss="categorical_crossentropy", metrics=["accuracy"] 
)
model_two.summary()
```
```python
# train deeper model
model_two.fit(
    X_train, Y_train,
    batch_size=BATCH_SIZE,
    epochs=EPOCHS,
    validation_split=VALIDATION_SPLIT
)
```
```python
model_two.evaluate(X_test, Y_test)
```
```javascript
[0.08618811517953873, 0.9735000133514404]
```
(`depper` è un refuso del docente.) Due strati nascosti, stesso ottimizzatore, stesse cento epoche: da **92.05% a 97.35%**. La loss scende da 0.288 a 0.086.
`scritta in aula` — celle `[14]`, `[15]`, `[16]`:
```python
# deeper with dropout
model_three = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, input_shape=(28*28,), activation="relu"),
    tf.keras.layers.Dropout(.3),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dropout(.3),
    tf.keras.layers.Dense(NB_CLASSES, activation="softmax")
])

model_three.compile(
    optimizer=tf.keras.optimizers.SGD(), loss="categorical_crossentropy", metrics=["accuracy"] 
)
model_three.summary()
```
```python
model_three.evaluate(X_test, Y_test)
```
```javascript
313/313 ━━━━━━━━━━━━━━━━━━━━ 0s 1ms/step - accuracy: 0.9642 - loss: 0.1147
[0.09435245394706726, 0.9704999923706055]
```
**Il dropout peggiora leggermente il risultato: 97.05% contro 97.35%.**
<callout icon="➕">
	**Nota aggiunta:** non è un fallimento del dropout, è la conferma della diagnosi. Il dropout è una **regolarizzazione**, serve contro l'overfitting; qui l'overfitting non c'è (addestramento e validazione stanno insieme in tutti e tre i modelli), quindi l'unico effetto è togliere capacità. Il docente non lo dice; il confronto lo mostra.
</callout>
---
## 6. LeNet-5 — `TF-07 @ 00:38:30`
«Ci sono tante versioni, ma usiamo quella di **LeNet-5**.»
`scritta in aula` — cella `[17]`:
```python
# convolutional lenet5
def lenet_5_model():
    inputs = tf.keras.Input(shape=(32, 32, 1))
    x = tf.keras.layers.Conv2D(6, (5, 5), activation="tanh")(inputs)
    x = tf.keras.layers.AveragePooling2D((2, 2), strides=2)(x)
    x = tf.keras.layers.Conv2D(16, (5 ,5), activation="tanh")(x)
    x = tf.keras.layers.AveragePooling2D((2, 2), strides=2)(x)
    x = tf.keras.layers.Conv2D(120, 1, activation="tanh")(x)
    x = tf.keras.layers.Flatten()(x)
    x = tf.keras.layers.Dense(84, activation="tanh")(x)
    outputs = tf.keras.layers.Dense(
        NB_CLASSES,
        activation="softmax"
    )(x)
    model = tf.keras.Model(
        inputs=inputs,
        outputs=outputs
    )
    return model
```
> **È il primo modello del corso scritto con l'API funzionale**, non con `Sequential`: ogni layer è una funzione applicata al tensore precedente, e alla fine `tf.keras.Model` chiude il grafo fra `inputs` e `outputs`. È la stessa forma che servirà per il transfer learning della sezione 13, dove il modello ha una base preesistente.
Il docente costruisce l'architettura strato per strato, spiegando ogni scelta:
- **L'input.** `TF-07 @ 00:39:00`: «lo shape originale era **32×32**, con 3 canali anche; ma noi teniamo il 32×32 ma con un **singolo canale**».
- **Prima convoluzione:** «6 filtri di dimensione di kernel 5×5, e l'attivazione era la **tangente iperbolica**» — è l'attivazione dell'articolo originale di LeCun del 1998, scritto prima che la ReLU diventasse standard.
- **Primo pooling:** «dopo una convoluzione usiamo sempre un pooling; per LeNet usiamo l'**average pooling**, 2×2 e *strides* 2».
- **Seconda convoluzione e pooling:** stessa struttura, 16 filtri.
- **Il layer *pointwise*.** `TF-07 @ 00:41:30`: «dopo questo abbiamo usato quello **pointwise**, che è un kernel di dimensione **1**». E una nota di sintassi: «se noi definiamo due dimensioni allora non avremo bisogno di mettere lo shape così, ma possiamo mettere solo `5` qua» — cioè `Conv2D(120, 1)` invece di `Conv2D(120, (1,1))`.
- **Flatten e dense:** «abbiamo 120 elementi, perché sono i filtri, allora possiamo usare la `Flatten`… e poi un dense layer, l'attivazione è sempre tangente iperbolica».
- **Output:** «una layer dense con le dimensioni del numero di classi e l'attivazione **softmax**».
`scritta in aula` — celle `[18]`, `[19]`:
```python
# compile model
model_lenet = lenet_5_model()
model_lenet.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=["accuracy"]
)
```
```python
model_lenet.summary()
```
```javascript
Model: "functional_3"
│ flatten (Flatten)               │ (None, 3000)           │             0 │
│ dense_7 (Dense)                 │ (None, 84)             │       252,084 │
│ dense_8 (Dense)                 │ (None, 10)             │           850 │
 Total params: 257,546 (1006.04 KB)
```
La compilazione (`TF-07 @ 00:43:30`): «possiamo usare la stessa… no, usiamo **Adam** ad esempio, la loss è sempre quella **categorical cross-entropy**, e poi le metriche». È l'unico dei quattro modelli a non usare SGD.
**Il ****`Flatten`**** produce 3000 valori**, e da lì i 252.084 parametri del `Dense(84)`: sono il 98% dell'intera rete. La parte convolutiva costa pochissimo — è il punto di tutta l'architettura.
`scritta in aula` — celle `[20]`, `[21]`:
```python
# reshapre and pad dataset
X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)

X_train = np.pad(X_train, ((0, 0), (2, 2), (2, 2), (0, 0)))
X_test = np.pad(X_test, ((0, 0), (2, 2), (2, 2), (0, 0)))

X_train.shape
```
```python
# train model
model_lenet.fit(
    X_train,
    Y_train,
    batch_size=BATCH_SIZE,
    epochs=5,
    validation_split=VALIDATION_SPLIT
)
```
```javascript
Epoch 5/5
375/375 ━━━━━━━━━━━━━━━━━━━━ 9s 25ms/step - accuracy: 0.9828 - loss: 0.0587 - val_accuracy: 0.9793 - val_loss: 0.0694
```
(`reshapre` è un refuso del docente.) Due passaggi obbligati e facili da dimenticare: le immagini erano state **appiattite** a 784 nella sezione 3 e vanno rimesse in `(28, 28, 1)`; e vanno **imbottite** da 28×28 a 32×32, perché LeNet-5 nasce così. Il `np.pad` aggiunge due pixel di zeri per lato solo sulle due dimensioni spaziali.
**Cinque epoche invece di cento**, e `val_accuracy` **0.9793**.
---
## 7. Il verdetto del confronto — `TF-07 @ 00:42:34`
Tutti e quattro i modelli, sullo stesso dataset e con lo stesso `VALIDATION_SPLIT`:
<table fit-page-width="true" header-row="true">
<tr>
<td>Modello</td>
<td>Struttura</td>
<td>Epoche</td>
<td>Parametri</td>
<td>Accuratezza su test</td>
</tr>
<tr>
<td>`model_one`</td>
<td>`Dense(10, softmax)`</td>
<td>100</td>
<td>7.850</td>
<td>**92.05%**</td>
</tr>
<tr>
<td>`model_two`</td>
<td>`128 → 64 → 10`</td>
<td>100</td>
<td>\~109.000</td>
<td>**97.35%**</td>
</tr>
<tr>
<td>`model_three`</td>
<td>come sopra + `Dropout(.3)` ×2</td>
<td>100</td>
<td>\~109.000</td>
<td>**97.05%**</td>
</tr>
<tr>
<td>`model_lenet`</td>
<td>LeNet-5 convolutiva</td>
<td>**5**</td>
<td>257.546</td>
<td>**97.93%** (validazione)</td>
</tr>
</table>
**Quello che il confronto dice davvero:** LeNet-5 batte tutti in **cinque** epoche invece di cento. Non è più profonda in senso banale — è **convolutiva**, cioè sfrutta il fatto che i pixel vicini sono correlati, informazione che i modelli densi hanno buttato via nel momento in cui `reshape(60000, 784)` ha appiattito l'immagine.
Il commento del docente a `TF-07 @ 00:38:00` è più cauto: «come potete vedere è **96.04**. Se qua vediamo la valutazione di quello prima… quello sì è più o meno… no, quello sì è sottoproporzionato ed è meglio, perché vedete anche il loss non era… convergono, ma non lo so, c'è una direzione che dà un po' di problema — forse possiamo modificare il *learning rate*».
> **Il «96.04» non corrisponde a nessuno dei numeri salvati.** Il valore più vicino è lo `0.9642` che compare nella barra di avanzamento di `model_three.evaluate` — cioè la media parziale sui batch, non il risultato finale (`0.9705`). Vedi `day-04-divergenze.md` §2.
`scritta in aula` — cella `[22]`, l'ultima, che resta un commento:
```python
# model_lenet.evaluate()
```
La valutazione di LeNet-5 sul test set **non viene mai eseguita**: l'unico numero disponibile è quello di validazione.
## Notebook della lezione
I file originali del docente, sul tuo Mac in `Downloads/TensorFlow-MDA/Materiale Sito/estratti/`:
- `19-06-2025/19-06-2025/1.MNIST-MODEL-SELECTION.ipynb`
