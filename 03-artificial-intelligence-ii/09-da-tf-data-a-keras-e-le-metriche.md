# 09 - Da tf.data a Keras, e le metriche
> Fonte Notion: https://app.notion.com/p/3d612abc808d8182ad7bcc372552c4f5 — ultima modifica 2026-09-09T23:31:28.174Z

> Giornata 3 del corso · video `TF-05` e `TF-06`
---
## 10. `DATASET`: l'API `tf.data` — `TF-05 @ 00:48:30` → `TF-06 @ 00:01:00`
> Questa sezione **attraversa il taglio fra i due file**.
`TF-05 @ 00:48:30`: «prima di andare all'API di Keras, prima esploriamo un po' un altro API di TensorFlow, si chiama **dataset**».
Il notebook è uno scheletro con dieci sezioni numerate e le celle vuote: il docente le riempie una per una. `già nel materiale` — la cella degli import e il markdown di testa:
```python
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn import datasets
from matplotlib import pyplot as plt
```
E la motivazione, letta dal markdown (`TF-05 @ 00:54:00`): «quello che vogliamo mostrare è l'uso del `tf.data`, che è molto efficiente, è scalabile per l'input di un modello machine learning, e poi è molto flessibile per ogni tipo di dati: DataFrame, CSV, generator e testo».
### 1. Da array NumPy — `TF-05 @ 00:56:30`
`scritta in aula` — cella `[4]`:
```python
iris = datasets.load_iris()
ds_numpy = tf.data.Dataset.from_tensor_slices(
    (iris["data"], iris["target"])
)
for feat, label in ds_numpy.take(5):
    print(feat.numpy(), label.numpy())
```
«Definiamo un array che prendiamo da scikit-learn, un dataset dei fiori… per creare una dataset possiamo dire `from_tensor_slices`, che questo ovviamente dà un array.» E il metodo per ispezionare: «abbiamo un metodo più o meno dedicato per questo nuovo API `tf.data`: se vogliamo prendere un sample possiamo usare il `take`».
### 2. Da DataFrame pandas — `TF-05 @ 00:59:30`
`scritta in aula` — cella `[6]`:
```python
df_iris = pd.DataFrame(
    iris["data"], columns=iris["feature_names"]
)
ds_df = tf.data.Dataset.from_tensor_slices(
    (df_iris.to_dict("list"), iris["target"])
)
for feat, label in ds_df.take(5):
    print(feat['sepal length (cm)'], label.numpy())
```
Il passaggio chiave è `to_dict("list")`: un DataFrame non entra direttamente in `from_tensor_slices`, va prima convertito in un dizionario colonna → lista. Ogni elemento del dataset diventa allora un **dizionario di tensori scalari**, uno per feature.
Il docente ci arriva per tentativi (`TF-05 @ 01:00:30`): «posso creare una `pd`, `iris`… *list* — no, devo fare un `to_dict`, per vedere così, `list`». E poi, guardando l'output completo: «vedete adesso che è difficile \[da leggere\]» — da cui la stampa della sola `sepal length (cm)`: «per vedere solo il valore di questo, posso fare così».
### 3. Da generatore Python — `TF-05 @ 01:02:30`
`scritta in aula` — celle `[8]`, `[9]`, `[10]`:
```python
image_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255).flow_from_directory(
    "./data/cifar/test/",
    target_size=(32, 32),
    batch_size=20,
    class_mode='binary'
)
class_dict = image_generator.class_indices
```
```python
inverted_class = {v:k for k,v in class_dict.items()}

def generator():
    for feat, label in image_generator:
        yield feat, label

ds_generator = tf.data.Dataset.from_generator(
    generator,
    output_types=(tf.float32, tf.float32)
)
```
```python
plt.figure(figsize=(6,6))
for i, (img, label) in enumerate(ds_generator.unbatch().take(9)):
    ax = plt.subplot(3, 3, i +1)
    ax.imshow(img.numpy())
    ax.set_title(f"label: {inverted_class[label.numpy()]}")
    ax.axis('off')
plt.show()
```
È il caso che richiede la cartella `data/cifar/` caricata su Colab. `flow_from_directory` deduce le classi dai nomi delle sottocartelle e le mette in `class_indices`; il dizionario **invertito** serve a rimettere il nome sul grafico. `rescale=1./255` porta i pixel in `[0, 1]`, e `unbatch()` scioglie i batch da 20 per poterne prendere 9 singole.
**Diagramma.** Una griglia 3×3 di immagini CIFAR a bassa risoluzione, ciascuna con il nome della classe come titolo.
### 4. Da file CSV — `TF-06 @ 00:03:42`
`scritta in aula` — cella `[12]`:
```python
csv_ds = tf.data.experimental.make_csv_dataset(
    ["./data/titanic/train.csv"], batch_size=3, label_name="Survived", na_value="", num_epochs=2, ignore_errors=True
)
for batch in csv_ds.take(2):
    print(batch)
```
`label_name` separa da solo la colonna bersaglio dalle feature; `na_value=""` dice cosa considerare mancante. L'avviso di deprecazione a schermo:
```javascript
tf.data.Dataset.ignore_errors' instead.
```
### 5. Da file di testo
`scritta in aula` — cella `[14]`:
```python
text_ds = tf.data.TextLineDataset(
    ["./data/titanic/train.csv", "./data/titanic/test.csv"]
).skip(1)

for line in text_ds.take(5):
    print(line.numpy().decode())
```
Lo stesso CSV letto come **testo grezzo**, riga per riga, con `.skip(1)` per l'intestazione. Due file in una lista diventano un flusso solo.
### 6-7. Trasformazioni e combinazioni
`scritta in aula` — celle `[16]`, `[18]`, `[19]`, `[21]`, `[22]`:
```python
text_data = tf.data.Dataset.from_tensor_slices(
    ["hello worlds", "hello tensorflow"]
)
map_ds = text_data.map(lambda x: tf.strings.split(x))
for w in map_ds.take(2):
    print(w.numpy())
```
```python
d1 = tf.data.Dataset.range(3)
d2 = tf.data.Dataset.range(3, 10)
zip_ds = tf.data.Dataset.zip((d1, d2))
concat_ds = tf.data.Dataset.concatenate(d1, d2)
```
`map` applica una funzione a ogni elemento senza materializzare nulla; `zip` appaia due dataset elemento per elemento (e si ferma al più corto: 3 elementi, non 7); `concatenate` li mette in fila.
### 9. Batching, unbatching, finestre — `TF-05 @ 01:26:33`
`scritta in aula` — celle `[26]`, `[27]`:
```python
batched = tf.data.Dataset.range(10).batch(2)
windowed = tf.data.Dataset.range(10).window(2, shift=1).flat_map(lambda x: x.batch(2))
```
```python
for i in windowed.take(5):
    print(i)
```
`batch(2)` fa cinque gruppi disgiunti; `window(2, shift=1)` fa nove **finestre sovrapposte** che scorrono di uno. È la stessa distinzione fra `ksize` e `strides` del pooling, applicata a una sequenza — e sarà lo strumento con cui la giornata 5 costruisce le finestre temporali per la previsione.
### 10. Shuffling
`scritta in aula` — cella `[29]`:
```python
shuffled = tf.data.Dataset.range(10).shuffle(buffer_size=5)
```
`buffer_size` è la dimensione della finestra da cui si pesca: non rimescola tutto, tiene 5 elementi in memoria e ne estrae uno per volta.
### Prefetch, cache, e la pipeline completa
**Qui cade il taglio.** TF-06 riprende su `prefetch` e `cache`.
`TF-06 @ 00:00:00`–`00:01:00`: «e poi anche il `prefetch` e il `cache`, tutti e due… questo è un esempio in cui facciamo la combinazione del `map`, poi il `batch`, il `prefetch` e poi il `repeat`».
Sul `prefetch` (`TF-05 @ 01:28:00`): «`tf.data` non solo ti trasforma questa cosa per andare in una pipeline di machine learning, ma dà anche un'**ottimizzazione**: se abbiamo qualche memoria libera lui può mettercelo già, allora la GPU può leggere molto veloce».
`già nel materiale` — cella `[35]`, l'unica del notebook che il docente **non compila e non esegue**, e che porta scritto il rinvio:
```python
# explained next time
def preprocess(x, y):
    x = tf.cast(x, tf.float32) / 255.0
    return x, y

(x_train, y_train), _ = tf.keras.datasets.mnist.load_data()
x_train = x_train[..., tf.newaxis] # add new axis/dimension (here we need channel so it create dim 1)

ds = tf.data.Dataset.from_tensor_slices((x_train, y_train))
ds = ds.map(preprocess)
ds = ds.shuffle(1000).batch(32).prefetch(tf.data.AUTOTUNE)
```
È la pipeline completa — normalizzazione, mescolamento, batch, prefetch — e il commento `# explained next time` è del docente. Viene ripresa nella **giornata 4**.
Sul `cache` lo lascia come esercizio: «questo cache vi lascio come exercise, così potete vedere; tanto lo vediamo quando passiamo \[a Keras\]». Le celle `[24]`, `[31]`, `[33]` restano infatti con il solo commento `# exercise`.
### Il resto del notebook
`scritta in aula` — celle `[37]`, `[39]`, `[41]`. Tre esempi brevi, aggiunti in coda:
```python
# da compilare
repeat_ds = tf.data.Dataset.range(3).repeat(2)
for x in repeat_ds:
    print(x.numpy())
```
```python
features = tf.data.Dataset.range(10)
labels = tf.data.Dataset.range(10, 20)

zipped = tf.data.Dataset.zip((features, labels))
for x, y in zipped:
    print(f"Feature: {x.numpy()}, Label: {y.numpy()}")
```
```python
sample = tf.constant("5.1,3.5,1.4,0.2,Iris-setosa")
record_defaults = [0.0, 0.0, 0.0, 0.0, ""]

fields = tf.io.decode_csv(sample, record_defaults)
fields  # parsed tensor fields
```
Sul `repeat` (`TF-06 @ 00:00:30`): «al solito quello che vogliamo è, ad esempio, se abbiamo un'epoca in cui non abbiamo abbastanza dati — abbiamo definito che il numero di batch diventa una singola epoca e non abbiamo abbastanza dati — dobbiamo **ripetere** i dati».
`decode_csv` mostra il livello più basso: `record_defaults` dichiara insieme il **tipo** e il valore di riempimento di ogni colonna.
---
## 11. Perché passare a Keras — `TF-06 @ 00:02:30`
È il passaggio concettuale della giornata, e il docente lo motiva esplicitamente:
> «Quello che abbiamo visto fino adesso sono tutte API di TensorFlow. Ma perché abbiamo guardato questo? Perché a volte anche dentro l'API di Keras ci sono tanti modelli, tanti layer già implementati — ma a volte dipende dal progetto, dovete implementare la **vostra** architettura, perché dipende dall'architettura della vostra rete neurale. Ecco perché abbiamo guardato un po' come usare TensorFlow: di base avremo bisogno di avere una piccola base di TensorFlow prima di entrare nell'API di Keras.»
E il primo esempio concreto: «per definire il nostro modello abbiamo definito la loss; ma su Keras esiste già una funzione di loss che noi possiamo usare. E ovviamente c'è anche l'**optimizer**».
---
## 12. `LOSS-OPTIM`: le loss di Keras — `TF-06 @ 00:03:30`
Il notebook si intitola «Losses and Optimizers in TensorFlow (keras API)». Le tabelle markdown — l'elenco delle loss e quello degli optimizer — sono `già nel materiale`; il docente le legge e le commenta.
`già nel materiale` — la tabella di riferimento:
<table header-row="true">
<tr>
<td>Loss</td>
<td>Uso</td>
<td>Codice</td>
</tr>
<tr>
<td>Mean Squared Error</td>
<td>Regressione</td>
<td>`tf.keras.losses.MeanSquaredError()`</td>
</tr>
<tr>
<td>Mean Absolute Error</td>
<td>Regressione, robusta agli outlier</td>
<td>`tf.keras.losses.MeanAbsoluteError()`</td>
</tr>
<tr>
<td>Binary Crossentropy</td>
<td>Classificazione binaria</td>
<td>`tf.keras.losses.BinaryCrossentropy()`</td>
</tr>
<tr>
<td>Categorical Crossentropy</td>
<td>Multiclasse, etichette **one-hot**</td>
<td>`tf.keras.losses.CategoricalCrossentropy()`</td>
</tr>
<tr>
<td>Sparse Categorical Crossentropy</td>
<td>Multiclasse, etichette **intere**</td>
<td>`tf.keras.losses.SparseCategoricalCrossentropy()`</td>
</tr>
</table>
Sulla binary cross-entropy: «quella che abbiamo implementato esplicitamente con la formula — ma comunque Keras lo fa, c'è già un'API».
**La differenza fra le due categoriali**, spiegata con un esempio: «quando abbiamo una classificazione in molte classi ma trasformiamo l'output come **one-hot encoded**… abbiamo tre classi, allora invece di mettere 0 mettiamo un array di tre elementi. La classe è l'**indice dell'1**: quindi 0 → `1,0,0`; 1 → `0,1,0`; 2 → `0,0,1`. E per questo usiamo la `CategoricalCrossentropy`. Invece, se noi abbiamo già l'indice — 0, 1, 2, 3, come quello di CIFAR — possiamo usare la **sparse** categorical cross-entropy.»
`scritta in aula` — celle `[5]`, `[6]`, `[7]`, `[8]`, con i valori calcolati sul posto:
```python
y_true_reg = [[1.], [2.], [3.]]
y_pred_reg = [[1.5], [2.5], [3.3]]
# MSE
mse = tf.keras.losses.MeanSquaredError()
print("MSE: ", mse(y_true_reg, y_pred_reg).numpy())
```
```javascript
MSE:  0.19666666
```
```python
# MAE
mae = tf.keras.losses.MeanAbsoluteError()
print("MAE: ", mae(y_true_reg, y_pred_reg).numpy())
```
```javascript
MAE:  0.4333333
```
```python
# BinaryCrossEntropy
y_true_bin = [[1.], [0.]]
y_pred_bin = [[.8], [.2]]
bce = tf.keras.losses.BinaryCrossentropy()
print("BCE: ", bce(y_true_bin, y_pred_bin).numpy())
```
```javascript
BCE:  0.22314353
```
Gli errori sono `0.5`, `0.5`, `0.3`: la MAE ne fa la media (`0.433`), la MSE la media dei quadrati (`0.197`). Sono due modi diversi di pesare un errore grande rispetto a molti piccoli, ed è la ragione per cui la MAE è «robusta agli outlier».
```python
# Categorical Crossentropy
y_true_cat = [[0., 1.], [1.0, 0]]
y_pred_cat = [[.05, .95], [.9, .1]]
catce = tf.keras.losses.CategoricalCrossentropy()
print("CCE: ", bce(y_true_cat, y_pred_cat).numpy())
```
```javascript
CCE:  0.078326926
```
> **Refuso nel notebook ufficiale.** L'ultima cella costruisce `catce` e poi chiama **`bce`**. Il valore `0.078` stampato sotto l'etichetta «CCE» è una **binary** cross-entropy, non una categorical. Con `catce` il risultato sarebbe `0.0783` anch'esso — le due coincidono su due classi complementari — quindi anche qui il refuso non dà sintomi. Vedi `day-03-divergenze.md` §4.
---
## 13. MNIST con `Sequential` — `TF-06 @ 00:16:00`
Il primo modello Keras della giornata, nelle ultime celle di `LOSS-OPTIM`.
`scritta in aula` — celle `[12]`, `[13]`:
```python
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
```
```python
x_train = x_train / 255.
x_test = x_test / 255.


model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(10)
])
```
Il docente costruisce il modello ragionando sulle forme: «faccio un `Flatten`, perché avrò un'immagine bianco e nero, quadrata, allora io vorrei un array *flatten*. Questo prende l'input… di default MNIST ha **28×28 pixel** ed è un singolo canale, perché è un'immagine bianco-nero». Poi «quello che si chiama una *single fully connected layer*, allora faccio questo **128**, e l'attivazione, posso scegliere ReLU». Infine «l'output sarebbe `Dense(10)`, perché il numero delle label è 10 — numeri da 0 a 9».
Keras avvisa che `input_shape` dentro un layer è deprecato:
```javascript
keras/src/layers/reshaping/flatten.py:37: UserWarning: Do not pass an `input_shape`/
`input_dim` argument to a layer. When using Sequential models, prefer using an
`Input(shape)` object as the first layer in the model instead.
```
`scritta in aula` — cella `[14]`:
```python
model.compile(
    optimizer=tf.keras.optimizers.Adam(),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)
```
Sul `compile`: «prima di fare il test devo **compilare** il modello». Sulla scelta della loss: «ricordate, noi abbiamo 10 \[classi\]… multiclasse, label **intere**, non one-hot encoded, allora posso usare la sparse categorical cross-entropy».
**`from_logits=True`**, spiegato (`TF-06 @ 00:19:00`): «cosa vuol dire *logit*? Logit è proprio che abbiamo un output così, ma noi infatti quello di cui abbiamo bisogno è un numero di **probabilità**». L'ultimo `Dense(10)` non ha attivazione: produce logit, non probabilità, e la loss se ne occupa internamente.
`scritta in aula` — cella `[15]`, l'addestramento:
```python
model.fit(
    x_train,
    y_train,
    epochs=5,
    validation_data=(x_test, y_test)
)
```
```javascript
Epoch 1/5
1875/1875 ━━━━━━━━━━ 7s 3ms/step - accuracy: 0.8747 - loss: 0.4423 - val_accuracy: 0.9586 - val_loss: 0.1388
Epoch 2/5
1875/1875 ━━━━━━━━━━ 5s 3ms/step - accuracy: 0.9643 - loss: 0.1231 - val_accuracy: 0.9681 - val_loss: 0.0977
Epoch 3/5
1875/1875 ━━━━━━━━━━ 5s 3ms/step - accuracy: 0.9772 - loss: 0.0790 - val_accuracy: 0.9749 - val_loss: 0.0789
Epoch 4/5
1875/1875 ━━━━━━━━━━ 5s 3ms/step - accuracy: 0.9833 - loss: 0.0554 - val_accuracy: 0.9782 - val_loss: 0.0718
Epoch 5/5
1875/1875 ━━━━━━━━━━ 5s 3ms/step - accuracy: 0.9872 - loss: 0.0421 - val_accuracy: 0.9777 - val_loss: 0.0712
```
**97.8% di accuratezza in validazione, in trentadue secondi e undici righe di codice.** Il confronto con la giornata 2 — dove ottenere una retta richiedeva un'ora di lavoro e un debug irrisolto — è tutta la motivazione della sezione 11.
Vale la pena leggere l'ultima riga: fra l'epoca 4 e la 5 l'accuratezza di addestramento sale (`0.9833 → 0.9872`) ma quella di validazione **scende** (`0.9782 → 0.9777`). È il primo affacciarsi dell'overfitting, che nella sezione 16 diventerà il tema.
<callout icon="➕">
	**Nota rilevante, non commentata a lezione.** Qui la GPU **funziona**: nell'output compaiono `XLA service ... for platform CUDA`, `StreamExecutor device (0): NVIDIA GeForce RTX 2060, Compute Capability 7.5` e `Loaded cuDNN version 90600`. Nella giornata 1 lo stesso hardware non veniva visto da TensorFlow (vedi `day-01-manuale.md` §15). Fra le due lezioni l'ambiente è stato sistemato; **nei video non si vede quando né come**. Da notare che questa esecuzione avviene sulla macchina del docente, non su Colab: il percorso `/home/louis/Documents/TEACHING/INCLASS2025/17-06-2025/venv/` nel warning lo conferma.
</callout>
`già nel materiale` — l'ultima cella markdown propone come esercizio di cambiare l'optimizer e di osservare la velocità di convergenza e l'accuratezza.
---
## 14. `SENTIMENT-KERAS`: recensioni IMDB — `TF-06 @ 00:33:00`
Terzo notebook, intitolato «**IMDB Sentiment Classification (Binary)**». Il docente lo introduce come possibile traccia d'esame (`TF-06 @ 00:33:00`): «vorrei finire questo sentiment analysis perché potrebbe essere anche importante se volete scegliere questo come un progetto».
`scritta in aula` — cella `[2]`, la configurazione:
```python
# configuration
NUM_WORDS = 10000
MAX_LEN = 200
```
`scritta in aula` — cella `[3]`, `TF-06 @ 00:38:01`:
```python
# load data nad preprocess
def load_data():
    (X_train, Y_train), (X_test, Y_test) = tf.keras.datasets.imdb.load_data(num_words=NUM_WORDS)
    X_train = tf.keras.preprocessing.sequence.pad_sequences(
        X_train,
        maxlen=MAX_LEN
    )
    X_test = tf.keras.preprocessing.sequence.pad_sequences(
        X_test,
        maxlen=MAX_LEN
    )
    return (X_train, Y_train), (X_test, Y_test)

(X_train, y_train), (X_test, y_test) = load_data()
print(X_train.shape, X_test.shape)
```
```javascript
(25000, 200) (25000, 200)
```
(`nad` è un refuso del docente per «and».) Due parametri governano tutto: si tengono le **10.000 parole più frequenti** e si porta ogni recensione a **esattamente 200 token** — tagliando le lunghe e riempiendo di zeri le corte. Ne esce una matrice rettangolare, che è ciò che serve per fare batch.
`scritta in aula` — cella `[4]`:
```python
# explore data
print("First review : ", X_train[0])
print("Label: ", y_train[0])
```
«Vedete che sono un indice di parole, e questo ad esempio è positivo.»
**I token e gli indici riservati.** `TF-06 @ 00:34:00`–`00:36:00`. Il docente collega al mondo dei modelli linguistici: «dobbiamo definire quel **token** — non so se avete sentito queste parole, \[se\] usate ChatGPT».
`scritta in aula` — cella `[5]`:
```python
word_index = tf.keras.datasets.imdb.get_word_index()

index_word = {
    index + 3:word for word, index in word_index.items() 
}
index_word[0] = "<PAD>"
index_word[1] = "<START>"
index_word[2] = "<UNK>"
index_word[3] = "<UNUSED>"


decoded_review = " ".join([index_word.get(i, '?') for i in X_train[0]])
pprint(decoded_review)
```
E spiega perché il `+3`: «gli indici particolari sono lo **0 per il padding**, l'**1 per l'inizio** di una nuova sequenza, e c'è anche un'altra per il **carattere speciale** che non era definito nel vocabolario. E poi un altro indice riservato… allora, qua, per creare l'indice devo iniziare da 3, perché avrò bisogno di **4 spazi** per quei caratteri speciali».
I quattro nomi sono scritti esplicitamente nel notebook: `<PAD>`, `<START>`, `<UNK>`, `<UNUSED>`. Lo scarto di 3 sposta ogni parola reale per fare posto.
> **Punto risolto dal materiale ufficiale.** Questa cella non è mai inquadrata per intero: era **\[illeggibile\]** e la versione precedente di questo manuale ne aveva ricostruito solo le prime due righe, senza i quattro token.
**Il modello.** `scritta in aula` — cella `[6]`, `TF-06 @ 00:39:00`:
```python
# Build and Compile Model
def build_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Embedding(
            NUM_WORDS, 256, input_length=MAX_LEN
        ),
        tf.keras.layers.GlobalMaxPool1D(),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid'),
    ])
    return model

model = build_model()

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='binary_crossentropy',
    metrics=[
        tf.keras.metrics.AUC(name='auc'),
        tf.keras.metrics.Precision(name='precision'),
        tf.keras.metrics.Recall(name='recall')
    ]
)

model.summary()
```
**L'embedding**, `TF-06 @ 00:33:30`: «questo tipo di modello, come facciamo per trasformare questa sequenza? Noi usiamo quello, il layer si chiama **embedding**… l'embedding è una trasformazione di questa sequenza in un vettore. Il numero di parole è la lunghezza del dizionario, e poi l'`input_length` sarebbe il `MAX_LEN`, la dimensione della sequenza». Ogni indice di parola diventa un vettore di **256** numeri: da `(batch, 200)` a `(batch, 200, 256)`.
**Il pooling globale**: «dopo un embedding possiamo definire ad esempio una **global max pooling** a una dimensione». Collassa i 200 token in un solo vettore da 256, tenendo per ogni dimensione il valore massimo lungo la sequenza — cioè il segnale più forte trovato nella recensione, ovunque si trovi.
Poi la testa densa `256 → 128 → 1` con sigmoide, come nella rete della sezione 5.
**Un ****`summary()`**** che non dice niente**, `TF-06 @ 00:41:00`: «forse non so perché, perché lì devi darmi anche i numeri di *trainable*, ma tanto potete vedere che noi abbiamo un embedding, e poi globalmax, dense, dense1, dense2».
```javascript
Model: "sequential"
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ Layer (type)                    ┃ Output Shape           ┃       Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ embedding (Embedding)           │ ?                      │   0 (unbuilt) │
│ global_max_pooling1d            │ ?                      │             0 │
│ dense (Dense)                   │ ?                      │   0 (unbuilt) │
│ dense_1 (Dense)                 │ ?                      │   0 (unbuilt) │
│ dense_2 (Dense)                 │ ?                      │   0 (unbuilt) │
└─────────────────────────────────┴────────────────────────┴───────────────┘
 Total params: 0 (0.00 B)
```
<callout icon="➕">
	**La causa è nell'avviso della cella sopra**, che il docente non collega: `Argument 'input_length' is deprecated. Just remove it.` In Keras 3 `input_length` viene ignorato, quindi il modello non conosce la forma dell'input e resta **non costruito** finché non riceve dati. Da qui tutti gli zeri e i `?`. Con un `tf.keras.Input(shape=(MAX_LEN,))` in testa il `summary()` mostrerebbe i 2.560.000 parametri dell'embedding. Questa lettura è mia, ed è marcata.
</callout>
---
## 15. Perché l'accuratezza non basta — `TF-06 @ 00:44:30`
È il passaggio metodologicamente più importante della giornata.
**La loss, in forma breve.** `TF-06 @ 00:44:00`: «ricordate anche che noi abbiamo definito la loss `tf.keras.losses.BinaryCrossentropy`… ma possiamo anche definirla così, `binary` **come stringa**, e Keras lo vede già e usa quella loss». Nel notebook infatti: `loss='binary_crossentropy'`.
**Il problema dell'accuratezza.** `TF-06 @ 00:44:30`: «ricordate che l'accuracy **non era appropriata** per una classificazione binaria — io l'ho fatto solo per vedere che possiamo calcolare anche una metrica».
E l'esempio clinico che usa per spiegarlo (`TF-06 @ 00:45:30`): «se mi dice che io faccio un'analisi e mi dà che potrebbe essere che sono malato ma con **probabilità 0.1**… oppure non malato ma con **probabilità 0.6**. L'accuracy mi dà solo un singolo valore per questo, ma io vorrei avere un valore **rispetto all'esito**».
La conclusione: «l'accuracy per una classificazione binaria non può essere sempre valida per vedere la performance di un progetto di tipo binary classification».
**Le tre metriche.** `scritta in aula`, dentro il `compile` della sezione 14:
```python
metrics=[
    tf.keras.metrics.AUC(name='auc'),
    tf.keras.metrics.Precision(name='precision'),
    tf.keras.metrics.Recall(name='recall')
]
```
Sull'AUC: «c'è una metrica che si chiama AUC: questa è una curva che rappresenta più o meno la differenza fra precision e recall rispetto alla soglia».
`già nel materiale` — le definizioni, in una lunga cella markdown che il docente legge:
<table header-row="true">
<tr>
<td>Termine</td>
<td>Significato</td>
</tr>
<tr>
<td>TP</td>
<td>predetto 1, davvero 1</td>
</tr>
<tr>
<td>TN</td>
<td>predetto 0, davvero 0</td>
</tr>
<tr>
<td>FP</td>
<td>predetto 1, davvero 0</td>
</tr>
<tr>
<td>FN</td>
<td>predetto 0, davvero 1</td>
</tr>
</table>
**Precision** = `TP / (TP + FP)` — di tutti quelli che ho dichiarato positivi, quanti lo erano davvero. Alta precision = pochi falsi allarmi.
**Recall** = `TP / (TP + FN)` — di tutti i positivi veri, quanti ne ho trovati. Alta recall = pochi mancati.
E il compromesso, sempre dal materiale: soglia **alta** → precision alta, recall bassa; soglia **bassa** → il contrario.
**Quando preferire l'una o l'altra.** `TF-06 @ 01:00:00`, sull'esempio dello spam: «spam detection, che in questo caso avremo bisogno solo del **precision**, che sia vicino a 1 — perché noi non possiamo avere un **falso positivo**. Ma il falso negativo va bene per noi quando facciamo una spam detection». Cioè: è accettabile che qualche spam passi, non è accettabile che una mail vera finisca nello spam.
La tabella del materiale estende l'idea: diagnosi medica → **recall**; spam → **precision**; frode → recall; classificazione di documenti legali → precision.
---
## 16. Le curve di addestramento, e l'overfitting — `TF-06 @ 00:50:02`
`scritta in aula` — cella `[7]`:
```python
# train the model
history = model.fit(
    X_train, y_train,
    epochs=5,
    batch_size=64,
    validation_data=(X_test, y_test),
    verbose=2
)
```
```javascript
Epoch 1/5
391/391 - 8s - 20ms/step - auc: 0.8936 - loss: 0.4065 - precision: 0.8077 - recall: 0.7781
              - val_auc: 0.9487 - val_loss: 0.3066 - val_precision: 0.9082 - val_recall: 0.8128
Epoch 2/5
391/391 - 2s - 6ms/step - auc: 0.9739 - loss: 0.2056 - precision: 0.9172 - recall: 0.9222
              - val_auc: 0.9458 - val_loss: 0.3113 - val_precision: 0.8953 - val_recall: 0.8341
Epoch 3/5
391/391 - 2s - 6ms/step - auc: 0.9926 - loss: 0.1028 - precision: 0.9666 - recall: 0.9640
              - val_auc: 0.9352 - val_loss: 0.4027 - val_precision: 0.8872 - val_recall: 0.8154
Epoch 4/5
391/391 - 2s - 6ms/step - auc: 0.9985 - loss: 0.0365 - precision: 0.9908 - recall: 0.9897
              - val_auc: 0.9245 - val_loss: 0.5228 - val_precision: 0.8732 - val_recall: 0.8319
Epoch 5/5
391/391 - 2s - 6ms/step - auc: 0.9997 - loss: 0.0091 - precision: 0.9986 - recall: 0.9980
              - val_auc: 0.9107 - val_loss: 0.6986 - val_precision: 0.8909 - val_recall: 0.7966
```
**È l'overfitting scritto in cifre, e vale la pena leggerlo riga per riga.** La loss di addestramento crolla da `0.41` a `0.009`; quella di **validazione** parte da `0.31`, tocca il minimo alla prima epoca e poi **risale** fino a `0.70`. L'AUC di validazione segue la stessa parabola: `0.949 → 0.911`. Il modello impara a memoria le 25.000 recensioni di addestramento.
**Il momento migliore era l'epoca 1.** Tutto quello che viene dopo peggiora il comportamento su dati nuovi. È esattamente il problema che la giornata 4 risolve con l'`EarlyStopping`.
`scritta in aula` — cella `[8]`, `TF-06 @ 01:10:42`:
```python
# trainign curve
plt.figure(figsize=(14, 5))

plt.subplot(1,3,1)
plt.plot(history.history['precision'], label="Precision")
plt.plot(history.history['val_precision'], label="Validation precision")
plt.title("precision vs epochs")
plt.xlabel("Epochs")
plt.ylabel("Precision")
plt.legend()

plt.subplot(1,3,2)
plt.plot(history.history['recall'], label="recall")
plt.plot(history.history['val_recall'], label="Validation recall")
plt.title("recall vs epochs")
plt.xlabel("Epochs")
plt.ylabel("recall")
plt.legend()

plt.subplot(1,3,3)
plt.plot(history.history['auc'], label="auc")
plt.plot(history.history['val_auc'], label="Validation auc")
plt.title("auc vs epochs")
plt.xlabel("Epochs")
plt.ylabel("auc")
plt.legend()
```
(`trainign` è un refuso del docente.)
**Diagramma.** Tre pannelli affiancati — «precision vs epochs», «recall vs epochs», «auc vs epochs». In tutti e tre la curva di **addestramento** sale verso 1.0 mentre quella di **validazione** resta piatta o scende. È il quadro classico dell'overfitting, e i numeri sopra ne sono la tabella.
---
## 17. La curva precision-recall e la scelta della soglia — `TF-06 @ 01:00:00`
Il docente riprende il filo lasciato aperto nella sezione 7 e lo chiude.
> «Quello che noi dobbiamo fare, dopo l'addestramento, è il **plot della curva precision-recall**, così l'utente finale può scegliere da sé la soglia che vuole. Questa è più o meno una curva che rappresenta la precision e la recall rispetto alla soglia.»
E la scelta dello strumento (`TF-06 @ 01:01:00`): «usiamo scikit-learn, che abbiamo installato prima, e lì c'è anche una funzione che fa quelle metriche e mi dà questa curva — perché mi sa che su Keras non c'è».
`scritta in aula` — cella `[10]`:
```python
# plot thresholds
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score, recall_score

def evaluate_thresholds(model, X, y_true, num_thresholds=100):
    # 1
    y_prods = model.predict(X).flatten()
    thresholds = np.linspace(0, 1, num=num_thresholds)
    precisions = []
    recalls = []

    # 2.
    for t in thresholds:
        y_pred = (y_prods >= t).astype(int)
        precisions.append(precision_score(y_true, y_pred))
        recalls.append(recall_score(y_true, y_pred))

    # 3 plot
    plt.figure(figsize=(14, 5))
    plt.subplot(1, 2, 1)
    plt.plot(thresholds, precisions, label="Precision")
    plt.plot(thresholds, recalls, label="recall")
    plt.title("Precision and reacall vs Threshold")
    plt.xlabel("Threshold")
    plt.ylabel("Score")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(precisions, recalls, marker='.')
    plt.title("Precision vs Recall")
    plt.xlabel("Precision")
    plt.ylabel("Recall")
    
    plt.show()
```
I tre commenti numerati (`# 1`, `# 2.`, `# 3 plot`) sono la struttura che il docente enuncia mentre scrive: predire una volta sola, poi ricalcolare le metriche per **cento soglie** diverse riusando le stesse probabilità, poi disegnare.
Sul `flatten()` (`TF-06 @ 01:02:30`): «lo facciamo un `flatten` per avere una lista più o meno». Sul perché NumPy e non TensorFlow: «il threshold è quello che abbiamo visto anche \[con\] `linspace`, ma qua usiamo **NumPy perché non è un grafo**» — siamo fuori dall'addestramento, in fase di analisi, e la regola 1 dell'autograph non si applica.
`scritta in aula` — cella `[11]`:
```python
# evaluate
evaluate_thresholds(model, X_test, y_test)
```
**Diagramma.** Due pannelli. A sinistra precision e recall in funzione della soglia: la precision sale da \~0.5 verso 1, la recall scende da 1 verso 0, e si incrociano. A destra la curva precision-recall vera e propria.
Il commento del docente (`TF-06 @ 01:08:00`) è di nuovo onesto: «il nostro modello ancora non è ben addestrato, allora non abbiamo una bella curva, ma più o meno dobbiamo trovare il **punto comune** se noi vogliamo bilanciare un po' la performance del modello. È quello che avremo bisogno del precision-recall».
E l'indicazione per l'esame: «questo, se prendete un esempio di binary classification, allora nel vostro assignment vorrei vedere qualcosa del genere».
> **Punto risolto dal materiale ufficiale.** Questa funzione non è mai inquadrata per intero: era **\[illeggibile\]**, e la versione precedente di questo manuale supponeva l'uso di `precision_recall_curve`. Lo strumento vero è diverso — `precision_score` e `recall_score` in un ciclo su cento soglie — ed è didatticamente più esplicito.
---
## 18. Decodificare una recensione e predire — `TF-06 @ 01:10:42`
`scritta in aula` — celle `[12]`, `[13]`, `[14]`:
```python
def decod_review(encoded):
    return " ".join([index_word.get(i, '?') for i in encoded])

sample_index = 1
sample_input = X_test[sample_index: sample_index + 1]
sample_label = y_test[sample_index]

pred = model.predict(sample_input)[0][0]
```
```python
pred_label = int(pred >= 0.1)
```
```python
print("review")
pprint(decod_review(X_test[sample_index]))
print(f"label: {pred_label}")
print(f"true label: {y_test[sample_index]}")
```
Il `'?'` come valore di default è il carattere per le parole fuori vocabolario di cui parlava nella sezione 14. Lo `slice` `X_test[i:i+1]` invece di `X_test[i]` serve a mantenere la dimensione di batch che `predict` si aspetta.
L'output, che nei frame era tagliato sotto il bordo inferiore:
```javascript
review
("psychological <UNK> it's very interesting that robert altman directed this "
 'considering the style and structure of his other films still the trademark '
 'altman audio style is evident here and there i think what really makes this '
 "film work is the brilliant performance by sandy dennis it's definitely one "
 'of her darker characters but she plays it so perfectly and convincingly that '
 [...]
 "unfortunately it's very difficult to find in video stores you may have to "
 'buy it off the internet')
label: 1
true label: 1
```
Si vedono all'opera i token della sezione 14: i `<UNK>` sono le parole fuori dalle 10.000 più frequenti, e la recensione comincia a metà frase perché il `pad_sequences` ha tagliato i primi token per stare in 200.
> **La soglia è 0.1, non 0.5**
>
> È la conseguenza pratica di tutta la sezione 17: la soglia non è un dato di fatto, si sceglie guardando le curve precision-recall in funzione di cosa costa di più sbagliare. Nella sezione 7, sulla rete scritta a mano, la soglia era 0.5 e il docente aveva annunciato che ci sarebbe tornato: qui ci torna, e la abbassa a 0.1 — cioè privilegia la **recall**.
>
> Su questo esempio la scelta non cambia l'esito: la recensione è chiaramente positiva e il modello la classifica 1 con qualunque soglia ragionevole. Il punto è il metodo.
---
## Esercizi lasciati aperti
**A voce:**
- `TF-05 @ 00:22:30` — cambiare la funzione di inizializzazione dei pesi: «potete esplorare, ad esempio come esercizio, di cambiare la funzione di inizializzazione» (`truncated_normal` contro `random.normal`);
- `TF-05 @ 00:22:00` — ampliare la rete: «potete anche esplorare da voi… potete aggiungere di più \[layer\] e anche cambiare la dimensione»;
- `TF-05 @ 00:48:00` — **il più impegnativo**: «un altro esercizio che vi chiedo: di trasformare quelle cose che abbiamo fatto qua su Keras, usando l'API di Keras» — cioè riscrivere la rete dei due anelli della sezione 5 con `Sequential`;
- `TF-05 @ 01:28:30` — il `cache` di `tf.data`: «questo cache vi lascio come exercise».
**Nel notebook, come celle lasciate con il solo commento:**
- `DATASET` cella `[24]`: `# exercise`, sotto la sezione «8. Reducing»;
- `DATASET` cella `[31]`: `# exrcies`, sotto «Prefetching»;
- `DATASET` cella `[33]`: `# exercise`, sotto «Caching Dataset»;
- `DATASET` cella `[17]`: `# explore some of the methods`;
- `LOSS-OPTIM`, ultima cella markdown: cambiare optimizer e osservare velocità di convergenza e accuratezza.
**E il rinvio esplicito:** `DATASET` cella `[35]`, la pipeline completa `map`+`shuffle`+`batch`+`prefetch`, porta il commento `# explained next time`.
---
## Glossario dei termini introdotti
<table header-row="true">
<tr>
<td>Termine</td>
<td>Definizione data nella lezione</td>
</tr>
<tr>
<td>**`tf.Module`**</td>
<td>Classe base da cui ereditare per definire un modello o un layer nuovo. `Dense` di Keras è a sua volta una sua sottoclasse. `TF-05 @ 00:20:30`</td>
</tr>
<tr>
<td>**`trainable_variables`**</td>
<td>L'elenco che `tf.Module` costruisce da solo con tutte le `tf.Variable` assegnate ad attributi: rende l'addestramento indipendente dal numero di layer. `TF-05 @ 00:38:00`</td>
</tr>
<tr>
<td>**`truncated_normal`**</td>
<td>Inizializzazione normale con le code tagliate, alternativa a `random.normal`. `TF-05 @ 00:22:30`</td>
</tr>
<tr>
<td>**Sigmoide in uscita**</td>
<td>Per la classificazione binaria si usa una **singola uscita** con sigmoide, perché «il sigmoide dà una probabilità». `TF-05 @ 00:25:00`</td>
</tr>
<tr>
<td>**Binary cross-entropy**</td>
<td>`-y·log(ŷ) - (1-y)·log(1-ŷ)`, mediata. Preferibile all'errore quadratico quando i valori sono piccoli. `TF-05 @ 00:29:00`</td>
</tr>
<tr>
<td>**`clip_by_value`**** per la loss**</td>
<td>`log(0)` non è definito: la predizione va confinata in `[ε, 1-ε]` con `ε = 1e-7`. `TF-05 @ 00:29:30`</td>
</tr>
<tr>
<td>**`input_signature`**</td>
<td>Fissa la firma del grafo di un `@tf.function` (`shape=[None, 2]`: batch libero, 2 feature) e impedisce il retracing. `TF-06 @ 00:01:30`</td>
</tr>
<tr>
<td>**Soglia decisionale**</td>
<td>Il valore sopra il quale la probabilità diventa classe 1. Di partenza 0.5, ma **si sceglie**. `TF-05 @ 00:34:00`, `TF-06 @ 01:00:00`</td>
</tr>
<tr>
<td>**`from_tensor_slices`**</td>
<td>Costruisce un dataset affettando la prima dimensione di array, DataFrame convertiti o tuple. `TF-05 @ 00:57:00`</td>
</tr>
<tr>
<td>**`from_generator`**</td>
<td>Costruisce un dataset da un generatore Python, dichiarando i tipi in uscita. `TF-05 @ 01:03:00`</td>
</tr>
<tr>
<td>**`window`**** vs ****`batch`**</td>
<td>`batch(2)` fa gruppi disgiunti, `window(2, shift=1)` finestre sovrapposte. `TF-05 @ 01:26:33`</td>
</tr>
<tr>
<td>**`prefetch`**</td>
<td>Precarica i dati mentre la GPU calcola: «se abbiamo qualche memoria libera lui può mettercelo già, allora la GPU può leggere molto veloce». `TF-05 @ 01:28:00`</td>
</tr>
<tr>
<td>**`repeat`**</td>
<td>Ripete il dataset quando i dati non bastano a coprire le epoche previste. `TF-06 @ 00:00:30`</td>
</tr>
<tr>
<td>**`from_logits=True`**</td>
<td>L'ultimo `Dense` senza attivazione produce **logit**, non probabilità; la loss se ne occupa. `TF-06 @ 00:19:00`</td>
</tr>
<tr>
<td>**Categorical vs Sparse categorical**</td>
<td>La prima per etichette **one-hot**, la seconda per etichette **intere**. `TF-06 @ 00:05:30`</td>
</tr>
<tr>
<td>**Embedding**</td>
<td>Trasforma indici interi di parole in vettori densi: da `(batch, 200)` a `(batch, 200, 256)`. `TF-06 @ 00:33:30`</td>
</tr>
<tr>
<td>**`GlobalMaxPool1D`**</td>
<td>Collassa la dimensione temporale tenendo il massimo per ogni canale: il segnale più forte, ovunque si trovi nella sequenza. `TF-06 @ 00:34:30`</td>
</tr>
<tr>
<td>**Padding e token speciali**</td>
<td>0 = `<PAD>`, 1 = `<START>`, 2 = `<UNK>`, 3 = `<UNUSED>`. Da qui lo scarto di 3 negli indici. `TF-06 @ 00:35:00`</td>
</tr>
<tr>
<td>**Precision e recall**</td>
<td>Metriche per classe, non globali. La precision conta quando un falso positivo è costoso (spam), la recall quando lo è un falso negativo (diagnosi). `TF-06 @ 00:44:30`, `01:00:00`</td>
</tr>
<tr>
<td>**AUC**</td>
<td>«Una curva che rappresenta la differenza fra precision e recall rispetto alla soglia.» `TF-06 @ 00:46:30`</td>
</tr>
<tr>
<td>**Overfitting, letto dalle curve**</td>
<td>Addestramento che sale e validazione che scende. Qui: loss di addestramento `0.41 → 0.009`, di validazione `0.31 → 0.70`. `TF-06 @ 00:50:02`</td>
</tr>
</table>
---
## Punti a bassa confidenza
**67 segmenti segnalati** su 943 (TF-05: 29 su 527, TF-06: 38 su 416), più **7 segmenti di boilerplate rimossi**. Elenco completo con i motivi in **`day-03-bassa-confidenza.md`**.
### Testo a schermo non leggibile `[illeggibile]`
Il materiale ufficiale ha **risolto nove dei dieci** punti che la versione precedente di questo manuale segnalava. Resta:
<table header-row="true">
<tr>
<td>Dove</td>
<td>Punto</td>
<td>Perché resta aperto</td>
</tr>
<tr>
<td>`TF-05 @ 00:45:01`</td>
<td>Il messaggio «The kernel died» è tagliato a destra</td>
<td>È un messaggio dell'interfaccia, non del notebook: non esiste in nessun file</td>
</tr>
</table>
**Risolti dal notebook ufficiale:** la cella della visualizzazione dei due anelli (`TF-05 @ 00:13:00`), il corpo del generatore `dataset` (`TF-05 @ 00:20:13`), le prime righe di `loss_func` (`TF-05 @ 00:32:33`), gli output di `ds_df.take(5)` (`TF-05 @ 01:02:14`), i log XLA e cuDNN (`TF-06 @ 00:23:24`), la cella `index_word` (`TF-06 @ 00:36:00`), il `compile` con le tre metriche (`TF-06 @ 00:46:30`), la funzione `evaluate_thresholds` (`TF-06 @ 01:03:02`), il testo decodificato della recensione (`TF-06 @ 01:15:20`).
---
## Materiale ufficiale usato
<table header-row="true">
<tr>
<td>File</td>
<td>Ruolo</td>
</tr>
<tr>
<td>`17-06-2025/LR-TF.ipynb`</td>
<td>**Fonte** della sezione 2. Identico alla versione `initial/`: distribuito completo</td>
</tr>
<tr>
<td>`17-06-2025/NN-TF-completed.ipynb`</td>
<td>**Fonte** delle sezioni 3-9</td>
</tr>
<tr>
<td>`17-06-2025/DATASET-completed.ipynb`</td>
<td>**Fonte** della sezione 10</td>
</tr>
<tr>
<td>`17-06-2025/LOSS-OPTIM-completed.ipynb`</td>
<td>**Fonte** delle sezioni 12-13</td>
</tr>
<tr>
<td>`17-06-2025/SENTIMENT-KERAS-completed.ipynb`</td>
<td>**Fonte** delle sezioni 14-18</td>
</tr>
<tr>
<td>`17-06-2025/KERAS-NN-should-be-reviewed.ipynb`</td>
<td>Non usato qui: non viene aperto in questa giornata. Il docente lo riprende a `TF-07 @ 00:01:30` — vedi **giornata 4, sezione 2**</td>
</tr>
<tr>
<td>`17-06-2025/initial/estratto/materials/*.ipynb`</td>
<td>Le versioni scheletro, per distinguere ciò che è stato scritto in aula</td>
</tr>
<tr>
<td>`TF-05.mp4`, `TF-06.mp4`</td>
<td>Fonte della **sequenza** e di tutto ciò che non è nei notebook: il crash della GPU, il trasloco su Colab, il ragionamento sulle forme, gli esercizi a voce</td>
</tr>
</table>
Elenco completo delle divergenze: **`day-03-divergenze.md`**.
Verifica per esecuzione: **`VERIFICA-day-03.md`**.
## Notebook della lezione
I file originali del docente, sul tuo Mac in `Downloads/TensorFlow-MDA/Materiale Sito/estratti/`:
- `17-06-2025/17-06-2025/DATASET-completed.ipynb`
- `17-06-2025/17-06-2025/KERAS-NN-should-be-reviewed.ipynb`
- `17-06-2025/17-06-2025/LOSS-OPTIM-completed.ipynb`
- `17-06-2025/17-06-2025/SENTIMENT-KERAS-completed.ipynb`
