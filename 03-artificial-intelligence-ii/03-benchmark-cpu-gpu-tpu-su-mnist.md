# 03 - Benchmark CPU / GPU / TPU su MNIST
> Fonte Notion: https://app.notion.com/p/3d612abc808d8128838af927d8a19466 — ultima modifica 2026-09-09T13:08:03.686Z

> Giornata 1, sezioni 17–21 · video `TF-01`
**Allegati:** `colab_mnist_cpu_gpu.ipynb`, `colab_mnist_tpu.ipynb` (notebook ufficiali del docente)
---
## 17. La pipeline dei dati con `tf.data` e MNIST `TF-01 @ 00:57:30`
Il docente carica su Colab il notebook `CPUMinst.ipynb`, preso come esempio per **misurare la performance** sui diversi acceleratori; il codice sarà poi ripreso riga per riga in un'altra occasione.
Il dataset è **MNIST** (le cifre scritte a mano), caricato con **TensorFlow Datasets**.
```python
import tensorflow as tf
import tensorflow_datasets as tfds
```
```python
(ds_train, ds_test), ds_info = tfds.load(
    'mnist',
    split=['train', 'test'],
    shuffle_files=True,
    as_supervised=True,
    with_info=True,
)
```
Il docente commenta gli argomenti: si indica il nome del dataset; si chiede lo **split** fra dati di addestramento e di test; `as_supervised=True` restituisce le coppie **input/label** — cioè la `x` e la `y` che servono in un problema supervisionato; `with_info=True` aggiunge le informazioni sul dataset.
Output alla prima esecuzione:
```javascript
WARNING:absl:Variant folder /root/tensorflow_datasets/mnist/3.0.1 has no dataset_info.json
Downloading and preparing dataset Unknown size (download: Unknown size, generated: Unknown size, total: Unknown size) to /root/tensorflow_datasets/mnist/3.0.1...
Dl Completed...: 100% 4/4 [00:01<00:00,  3.19 url/s]
Dl Size...: 100% 10/10 [00:01<00:00,  8.07 MiB/s]
Extraction completed...: 100% 4/4 [00:01<00:00,  3.29 file/s]
Dataset mnist downloaded and prepared to /root/tensorflow_datasets/mnist/3.0.1. Subsequent calls will reuse this data.
```
Il docente fa notare che la prima esecuzione **scarica e mette in cache** il dataset: le volte successive TensorFlow Datasets riuserà la cache.
**La funzione che costruisce il dataset** (dal notebook ufficiale `colab_mnist_cpu_gpu.ipynb`):
```python
def get_dataset(batch_size, is_training=True):
  if is_training:
    dataset, info = tfds.load(name='mnist', split='train', with_info=True,
                            as_supervised=True, try_gcs=True)
  else:
    dataset = tfds.load(name='mnist', split='test',
                        as_supervised=True, try_gcs=True)

  # Normalize the input data.
  def scale(image, label):
    image = tf.cast(image, tf.float32)
    image /= 255.0
    return image, label

  dataset = dataset.map(scale)

  if is_training:
    dataset = dataset.shuffle(10000)
    dataset = dataset.repeat()

  dataset = dataset.batch(batch_size)

  return dataset
```
> **Divergenza.** A schermo il docente scrive la stessa funzione con un ternario e una sola chiamata a `tfds.load` (`split = 'train' if is_training else 'test'`, con `with_info=True` in entrambi i rami). Il comportamento e' equivalente; la forma no. Vedi `day-01-divergenze.md` §2.
**La normalizzazione.** Il docente riprende l'esempio dei prezzi delle case: non si possono dare in pasto a un algoritmo valori che vanno da 20.000 a 4 milioni; bisogna riportarli in un intervallo di scala. Qui però la normalizzazione riguarda **l'input, non le label**: i valori dei pixel sono definiti da **0 a 255**, e si vogliono portare nell'intervallo **0–1**. Per farlo basta dividere per il massimo, cioè 255.
`dataset.map(scale)` applica la funzione a tutto il dataset.
**`shuffle`**** e ****`repeat`****.** In addestramento si mescolano i dati con un buffer di 10.000 e si ripete il dataset. Il docente spiega perché serve `repeat()` con un esempio numerico: se si ha un vettore di lunghezza 10 e un batch di dimensione 4, si ottengono due batch pieni **e un resto di due elementi**. Con la ripetizione, i batch che non hanno la dimensione esatta vengono completati.
**I parametri:**
```python
batch_size = 200
steps_per_epoch = 60000 // batch_size
validation_steps = 10000 // batch_size

train_dataset = get_dataset(batch_size, is_training=True)
test_dataset = get_dataset(batch_size, is_training=False)
```
`steps_per_epoch` è il numero di passi da compiere in ogni epoca: la dimensione del dataset divisa per la dimensione del batch.
---
## 18. Il modello e il ciclo di addestramento `TF-01 @ 01:03:00`
```python
model = tf.keras.models.Sequential([tf.keras.layers.Conv2D(256, 3, activation='relu', input_shape=(28, 28, 1)),
        tf.keras.layers.Conv2D(256, 3, activation='relu'),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10)])

model.compile(
    optimizer=tf.keras.optimizers.Adam(0.001),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=[tf.keras.metrics.SparseCategoricalAccuracy()],
)

model.summary()

history = model.fit(
    train_dataset,
    epochs=1,
    steps_per_epoch=steps_per_epoch,
    validation_data=test_dataset,
    validation_steps=validation_steps,
)
```
> **Divergenza sul numero di epoche.** Il notebook distribuito ha **`epochs=1`**; a schermo (`TF-01 @ 01:03:30` e seguenti) il docente usa **`epochs=5`** e su quel numero costruisce il confronto CPU/GPU. Chi rilancia il notebook ufficiale ottiene un solo passaggio. Vedi `day-01-divergenze.md` §3.
>
> L'ufficiale contiene anche `model.summary()` in coda a questa cella e una cella di diagnostica con tre `print` che a schermo non compaiono (§4).
Il docente ricollega il codice ai cinque passi visti all'inizio: qui c'è la **definizione del modello**, poi la **funzione di perdita** da minimizzare, poi la **metrica** che misura la performance — in questo caso `SparseCategoricalAccuracy` — e infine il **training loop**, con cinque epoche.
Sottolinea di nuovo il punto metodologico: il *test set* passato come `validation_data` è **separato** e non condivide dati con il *training set*; è questo che consente una misura veritiera.
```python
tf.config.get_visible_devices()
```
```javascript
[PhysicalDevice(name='/physical_device:CPU:0', device_type='CPU')]
```
---
## 19. Confronto CPU contro GPU T4 `TF-01 @ 01:04:30`
Questo è il cuore dimostrativo della lezione.
**Prima esecuzione — runtime CPU ****`TF-01 @ 01:07:00`****.** Prima di lanciare si sceglie il runtime da *Change runtime type*. Con `tf.config.get_visible_devices()` il docente conferma di avere la sola CPU. Poi avvia l'addestramento:
```javascript
/usr/local/lib/python3.11/dist-packages/keras/src/layers/convolutional/base_conv.py:107: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, pr[illeggibile]
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/5
  3/300 ━━━━━━━━━━━━━━━━━━━━ 50:42 10s/step - loss: 2.2512 - sparse_categorical_accuracy: 0.1536
```
Il commento del docente: ogni passo richiede **dieci secondi**, e i passi sono 300 — l'epoca stimata è di circa **50 minuti**. Non si può aspettare. Poco dopo `TF-01 @ 01:10:12` interrompe l'esecuzione:
```javascript
Epoch 1/5
  8/300 ━━━━━━━━━━━━━━━━━━━━ 49:40 10s/step - loss: 1.9481 - sparse_categorical_accuracy: 0.3471
KeyboardInterrupt                         Traceback (most recent call last)
<ipython-input-6-8f1c49197dc6> in <cell line: 0>()
```
**Seconda esecuzione — runtime GPU T4 ****`TF-01 @ 01:08:30`****.** Il docente **non cambia una riga di codice**: cambia soltanto il runtime, salva, aspetta la riconnessione e rilancia. Il dataset va riscaricato, perché cambiando runtime si perde la cache. Il risultato `TF-01 @ 01:11:16`:
```javascript
Epoch 1/5
300/300 ━━━━━━━━━━━━━━━━━━━━ 39s 91ms/step - loss: 0.3661 - sparse_categorical_accuracy: 0.8836 - val_loss: 0.0394 - val_sparse_categorical_accuracy: 0.9872
Epoch 2/5
132/300 ━━━━━━━━━━━         13s 81ms/step - loss: 0.0422 - sparse_categorical_accuracy: 0.9877
KeyboardInterrupt                         Traceback (most recent call last)
<ipython-input-7-8f1c49197dc6> in <cell line: 0>()
     12 )
     13
---> 14 history = model.fit(train_dataset,
     15         epochs=5,
     16         steps_per_epoch=steps_per_epoch,
```
**Il confronto, nelle parole del docente:** ogni passo è passato da 10 secondi a circa **80-90 millisecondi**, e l'epoca da 40-50 minuti a **39 secondi**.
Un'avvertenza pratica: con un singolo account si può usare **un solo runtime alla volta**.
---
## 20. La TPU: `TPUStrategy` e il problema della `loss: nan` `TF-01 @ 01:11:30`
Il docente apre un secondo notebook, `TPUMinst.ipynb`. La **TPU** è un ulteriore acceleratore, e per quanto gli risulta al momento **solo Google la mette a disposizione**. Nel runtime scelto compare come **v2-8 TPU**; la versione gratuita basta per la dimostrazione.
**Perché servono versioni specifiche ****`TF-01 @ 01:13:00`****.** Essendo TensorFlow open source gli aggiornamenti sono continui, ma il supporto TPU non è allineato: il docente riferisce di aver provato il giorno prima e che la **2.19 non funziona** con la TPU. In più il runtime TPU di Colab **non ha TensorFlow preinstallato**. Per questo installa una versione precisa:
```python
!pip install tensorflow==2.18.0 -q
!pip install tensorflow-tpu==2.18.0 --find-links=https://storage.googleapis.com/libtpu-tf-releases/index.html -q
!pip install ml_dtypes==0.5.0
```
> **Divergenza.** La terza riga (`ml_dtypes==0.5.0`) e' nel notebook distribuito ma non compare in nessun frame del video: e' proprio la riga che risolve il conflitto di dipendenze di cui il docente parla a `TF-01 @ 01:15:30`. Vedi §5.
Coglie l'occasione per spiegare la sintassi: il **punto esclamativo** davanti a un comando dentro una cella di notebook serve a eseguirlo nel terminale sottostante, non nell'interprete Python. Il secondo comando ha bisogno dell'URL indicato per trovare i *binary* di `libtpu`.
Il runtime risulta: "Connected to Python 3 Google Compute Engine backend (TPU), RAM: 4.23 GB/334.56 GB, Disk: 18.15 GB/225.33 GB".
**Gli import ****`TF-01 @ 01:16:35`****:**
```python
import tensorflow as tf
import tensorflow_datasets as tfds
import os
import numpy as np
import pandas as pd
```
Output:
```javascript
/usr/local/lib/python3.11/dist-packages/jax/__init__.py:31: UserWarning: cloud_tpu_init failed: AttributeError("module 'libtpu' has no attribute 'get_library_path'")
 This a JAX bug; please report an issue at https://github.com/jax-ml/jax/issues
  _warn(f"cloud_tpu_init failed: {exc!r}\n This a JAX bug; please report ")
```
**Connessione alla TPU ****`TF-01 @ 01:16:30`****.** Il docente spiega che la TPU è di fatto un **worker**, un piccolo servizio a cui bisogna prima connettersi; se non è disponibile occorre attendere.
```python
try:
  tpu = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='local')
  print(f'Running on a TPU w/{tpu.num_accelerators()["TPU"]} cores')
except ValueError:
  raise BaseException('ERROR: Not connected to a TPU runtime')

tf.config.experimental_connect_to_cluster(tpu)
tf.tpu.experimental.initialize_tpu_system(tpu)
tpu_strategy = tf.distribute.TPUStrategy(tpu)
```
```javascript
Running on a TPU w/8 cores
```
**Il modello diventa una funzione ****`TF-01 @ 01:17:00`****:**
```python
def create_model():
  return tf.keras.Sequential(
      [tf.keras.layers.Conv2D(256, 3, activation='relu', input_shape=(28, 28, 1)),
       tf.keras.layers.Conv2D(256, 3, activation='relu'),
       tf.keras.layers.Flatten(),
       tf.keras.layers.Dense(256, activation='relu'),
       tf.keras.layers.Dense(128, activation='relu'),
       tf.keras.layers.Dense(10)])
```
La funzione `get_dataset` è **la stessa** usata per CPU e GPU.
**Perché il modello va creato dentro lo scope ****`TF-01 @ 01:17:30`****.** Qui il docente riprende il concetto dall'inizio della lezione: TensorFlow **non è l'interprete Python** — deve costruire il grafo. Bisogna quindi dichiarare che il modello va costruito **dentro la TPU**, ed è per questo che si usa il *context manager* `with tpu_strategy.scope()`:
```python
with tpu_strategy.scope():
  model = create_model()
  model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['sparse_categorical_accuracy'])
model.summary()
```
**`model.summary()`**** ****`TF-01 @ 01:20:55`** (coda della tabella; le prime due righe `conv2d` sono sopra il bordo superiore del frame — \[illeggibile\]):
<table header-row="true">
<tr>
<td>Layer (type)</td>
<td>Output Shape</td>
<td>Param #</td>
</tr>
<tr>
<td>flatten (Flatten)</td>
<td>(None, 147456)</td>
<td>0</td>
</tr>
<tr>
<td>dense (Dense)</td>
<td>(None, 256)</td>
<td>37,748,992</td>
</tr>
<tr>
<td>dense_1 (Dense)</td>
<td>(None, 128)</td>
<td>32,896</td>
</tr>
<tr>
<td>dense_2 (Dense)</td>
<td>(None, 10)</td>
<td>1,290</td>
</tr>
</table>
```javascript
Total params: 38,375,818 (146.39 MB)
Trainable params: 38,375,818 (146.39 MB)
Non-trainable params: 0 (0.00 B)
```
**Il problema ****`TF-01 @ 01:19:00`****–****`TF-01 @ 01:23:30`****.** L'addestramento su TPU produce `nan` in tutte le metriche:
```javascript
Epoch 1/5
300/300 ━━━━━━━━━━━━━━━━━━━━ 20s 44ms/step - loss: nan - sparse_categorical_accuracy: nan - val_loss: nan - val_sparse_categorical_accuracy: nan
Epoch 2/5
300/300 ━━━━━━━━━━━━━━━━━━━━ 9s 29ms/step - loss: nan - sparse_categorical_accuracy: nan - val_loss: nan - val_sparse_categorical_accuracy: nan
Epoch 3/5
144/300 ━━━━━━━━━ 3s 23ms/step - loss: nan - sparse_categorical_accuracy: nan
```
La spiegazione del docente: poiché il modello è definito dentro lo scope della `TPUStrategy`, l'addestramento avviene **sul worker della TPU**; il problema è che quel worker **non riesce a riportare i valori alla CPU**, che è ciò che li mostra a schermo. La loss quindi **non è indefinita**: viene aggiornata, ma non arriva all'interfaccia. Il docente precisa di aver cercato una soluzione e di aver contattato Google senza ottenerne una, e che il problema potrebbe riguardare soltanto la versione gratuita.
**La verifica ideata dal docente.** Per dimostrare che l'addestramento avviene davvero, costruisce un confronto in due tempi:
1. **Prima dell'addestramento.** Crea il modello da zero, con pesi e bias casuali, e lo usa per predire; si aspetta che quasi nessuna predizione corrisponda alla verità.
2. **Dopo cinque epoche.** Rilancia la stessa funzione sul modello addestrato.
```python
predictions = model.predict(test_dataset)
pred_labels = np.argmax(predictions, axis=1)


true_labels = np.concatenate([
    label_batch.numpy() for _, label_batch in test_dataset
], axis=0)

df = pd.DataFrame({
    'label_true': true_labels,
    'label_pred': pred_labels
})

df.head(10)
```
Output con il modello non addestrato `TF-01 @ 01:24:18`:
```javascript
50/50 ━━━━━━━━━━━━━━━━━━━━ 4s 50ms/step
   label_true  label_pred
0           2           3
1           0           3
```
Il docente commenta il primo caso: il valore vero era 2 e la predizione 3. Dopo l'addestramento `TF-01 @ 01:23:00`, invece, **le prime dieci predizioni risultano sostanzialmente corrette**. È la prova che l'addestramento è avvenuto e che il `nan` è un problema di trasmissione del valore dalla TPU all'interfaccia, non di calcolo.
---
## 21. Persistenza dei file su Colab `TF-01 @ 01:24:30`
Il docente chiude la parte su Colab con l'avvertenza operativa. Se si devono usare dati propri, vanno messi **su Google Drive**; esiste una guida per montare il Drive nel notebook. Il motivo è concreto: **cambiando il runtime si perdono i file** salvati nella sessione, e con essi anche i dataset messi in cache. Questo è, dice, il *drawback* di Google Colab.
Un'ultima avvertenza `TF-01 @ 01:25:30`: quando si finisce di lavorare su Colab conviene **disconnettere il runtime**, altrimenti non si riesce ad aprire un'altra sessione — il runtime è legato all'account e resta attivo.
---
---
## File allegati
I due notebook ufficiali del docente. Caricati con estensione `.json` perché Notion non accetta `.ipynb`: dopo il download rinominali in `.ipynb` per aprirli in Jupyter.
<file src="notion-file-block://f288c125-f43a-45a7-ba32-0356fc08937c/0407aac1-e262-4c31-91c6-1a8c4dab4c22?space_id=98012abc-808d-816f-9733-00030a2b4817&name=colab_mnist_cpu_gpu.json"></file>
<file src="notion-file-block://c6a7490d-e987-4bd7-8e56-084634248c92/23f4dbff-be0f-48df-8f59-591adcf5d792?space_id=98012abc-808d-816f-9733-00030a2b4817&name=colab_mnist_tpu.json"></file>
