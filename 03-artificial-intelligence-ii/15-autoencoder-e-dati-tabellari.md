# 15 - Autoencoder e dati tabellari
> Fonte Notion: https://app.notion.com/p/3d612abc808d812395dfd45494413e27 — ultima modifica 2026-09-09T23:31:42.693Z

> Giornata 5 del corso · video `TF-09` e `TF-10`
---
## 9. `SUPER_RES`: super-risoluzione — `TF-10 @ 00:16:00`
Terzo notebook, su **Google Colab**: `colab.research.google.com/drive/1TxmgoGF-0B9_HD3gNVN8nydza-HRzpaB`.
È il progetto annunciato nella giornata 4, quando il docente aveva presentato `Conv2DTranspose`: «l'encoder fa il downscaling e il decoder fa l'upscaling».
`già nel materiale` — l'intestazione dichiara che il notebook implementa una pipeline di super-risoluzione basata su un autoencoder convoluzionale in TensorFlow/Keras, con i dati attesi in `datasets/train/high_res/`, `datasets/train/low_res/`, `datasets/val/high_res/` e `datasets/val/low_res/`, e l'obiettivo di ricostruire immagini ad alta risoluzione a partire dalle corrispondenti a bassa risoluzione.
`già nel materiale` — celle `[1]`, `[2]`:
```python
# upload data and unzip
!unzip sample_data/archive.zip
```
```python
# import library
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
from pathlib import Path
```
`scritta in aula` — cella `[3]`:
```python
# Configuration
DATASET_PATH = Path("dataset")
TRAIN_DIR = DATASET_PATH / "train"
VAL_DIR = DATASET_PATH / "val"
BATCH_SIZE = 16
IMAGE_SIZE = (256, 256)
```
Il docente segnala una comodità di `pathlib` (`TF-10 @ 00:16:30`): «la bella cosa di questo `pathlib` è che posso fare solo questo come una **divisione** fra due cose, ma comunque questa è una **concatenazione del percorso**».
`scritta in aula` — celle `[4]`, `[5]`:
```python
# Utility: Load and preprocess image (drop alpha channel, normalize to [0, 1])
def load_image(path):
  image = Image.open(path).convert("RGB").resize(IMAGE_SIZE)
  return np.array(image, dtype=np.float32) / 255.0
```
```python
# Load dataset: return list of (low_res, high_res) image path pairs
def load_image_pairs(base_path):
  lowdir = base_path / "low_res"
  highdir = base_path / "high_res"
  low_images = sorted(lowdir.glob("*.png"))
  high_images = sorted(highdir.glob("*.png"))
  return list(zip(low_images, high_images))
```
Le tre operazioni di `load_image`, spiegate (`TF-10 @ 00:18:00`–`00:18:30`): «usiamo **PIL** per leggerlo. Poi facciamo una conversione a **RGB**, perché potrebbe essere che questo ha un altro canale, si chiama **alpha**. E poi una **resize**, per confermare che abbiamo tutti lo stesso size. Poi ritorniamo un array NumPy di queste immagini, diviso… questa è la **normalizzazione** che al solito facciamo per l'immagine, così abbiamo uno nel range di 0-1».
In `load_image_pairs` il lavoro lo fa il doppio `sorted`: due elenchi ordinati per nome si allineano, e lo `zip` appaia ogni immagine a bassa risoluzione con la sua corrispondente ad alta. **La corrispondenza è affidata interamente ai nomi dei file.**
`scritta in aula` — celle `[6]`, `[7]`, `[8]`:
```python
# Custom tf.data.Dataset loader
def get_dataset(pairs, augment=False):
  def load_pair(low_path, high_path):
    low = tf.numpy_function(load_image, [low_path], tf.float32)
    high = tf.numpy_function(load_image, [high_path], tf.float32)
    low.set_shape([*IMAGE_SIZE, 3])
    high.set_shape([*IMAGE_SIZE, 3])
    return low, high

  low_paths, high_paths = zip(*pairs)
  low_ds = tf.data.Dataset.from_tensor_slices([str(p) for p in low_paths])
  high_ds = tf.data.Dataset.from_tensor_slices([str(p) for p in high_paths])
  ds = tf.data.Dataset.zip((low_ds, high_ds))
  ds = ds.map(load_pair, num_parallel_calls=tf.data.AUTOTUNE)
  if augment:
    ds = ds.map(lambda x, y: (tf.image.random_flip_left_right(x), tf.image.random_flip_left_right(y)))
  ds = ds.batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)
  return ds
```
```python
# Load training and validation datasets
train_pairs = load_image_pairs(TRAIN_DIR)
val_pairs = load_image_pairs(VAL_DIR)

train_ds = get_dataset(train_pairs, augment=True)
val_ds = get_dataset(val_pairs)
```
```python
for x, y in train_ds.take(1):
  print(x.shape, y.shape)
```
```javascript
(16, 256, 256, 3) (16, 256, 256, 3)
```
<callout icon="➕">
	**`tf.numpy_function`**** è il pezzo interessante di questa cella.** PIL è una libreria Python: dentro un grafo TensorFlow non ci si può usare — è la **regola 1 dell'autograph** della giornata 2. `tf.numpy_function` è la scappatoia ufficiale: avvolge una funzione Python in un'operazione del grafo, a costo di eseguirla fuori dal grafo e senza parallelismo interno.
	Il prezzo è visibile nelle due righe successive: la funzione avvolta **non dichiara la forma del risultato**, quindi il resto della pipeline non saprebbe che shape aspettarsi. Da qui i due `set_shape` espliciti.
	C'è però un problema nell'aumento dei dati: le due `random_flip_left_right` sono chiamate **separatamente** su `x` e `y`, quindi decidono in modo indipendente se specchiare. Metà delle volte l'immagine a bassa risoluzione viene specchiata e la sua etichetta no — il modello riceve una coppia incoerente. La forma corretta sarebbe generare un solo numero casuale e applicarlo a entrambe. Questa osservazione è mia.
</callout>
---
## 10. L'autoencoder — `TF-10 @ 00:41:04`
`scritta in aula` — cella `[9]`:
```python
# Define the Autoencoder architecture
def create_autoencoder():
  inputs = tf.keras.layers.Input(shape=(*IMAGE_SIZE, 3))
  # encoder
  x = tf.keras.layers.Conv2D(
      16,
      (3, 3),
      strides=(2, 2),
      padding="same",
      activation="relu"
  )(inputs)
  x = tf.keras.layers.Conv2D(
      32,
      (3, 3),
      strides=(2, 2),
      padding="same",
      activation="relu"
  )(x)
  x = tf.keras.layers.BatchNormalization()(x)
  x = tf.keras.layers.Conv2D(
      64,
      (3, 3),
      strides=(2, 2),
      padding="same",
      activation="relu"
  )(x)

  # decoder

  x = tf.keras.layers.Conv2DTranspose(
      32,
      (3, 3),
      strides=(2, 2),
      padding="same",
      activation="relu"
  )(x)
  x = tf.keras.layers.Conv2DTranspose(
      16,
      (3, 3),
      strides=(2, 2),
      padding="same",
      activation="relu"
  )(x)
  x = tf.keras.layers.BatchNormalization()(x)
  output = tf.keras.layers.Conv2DTranspose(
      3,
      (3, 3),
      strides=(2, 2),
      padding="same",
      activation="sigmoid"
  )(x)

  return tf.keras.Model(inputs, output)
```
**La struttura è simmetrica**, ed è il punto:
<table header-row="true">
<tr>
<td></td>
<td>Encoder</td>
<td></td>
<td>Decoder</td>
<td></td>
</tr>
<tr>
<td>input</td>
<td>256×256×3</td>
<td></td>
<td>32×32×64</td>
<td></td>
</tr>
<tr>
<td>Conv2D 16</td>
<td>128×128×16</td>
<td></td>
<td>Conv2DTranspose 32 → 64×64×32</td>
<td></td>
</tr>
<tr>
<td>Conv2D 32</td>
<td>64×64×32</td>
<td></td>
<td>Conv2DTranspose 16 → 128×128×16</td>
<td></td>
</tr>
<tr>
<td>Conv2D 64</td>
<td>**32×32×64**</td>
<td></td>
<td>Conv2DTranspose 3 → **256×256×3**</td>
<td></td>
</tr>
</table>
`strides=(2, 2)` dimezza a ogni convoluzione e raddoppia a ogni convoluzione trasposta. Il collo di bottiglia è `32×32×64`: l'immagine passa da 196.608 numeri a 65.536, un fattore 3 di compressione. È il «QR code» dell'esempio della giornata 4.
L'uscita ha **tre canali** (RGB) e attivazione `sigmoid`, perché i pixel sono normalizzati in `[0, 1]`.
`scritta in aula` — cella `[10]`:
```python
# Initialize and compile model
model = create_autoencoder()
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
    loss=tf.keras.losses.MeanSquaredError()
)
model.summary()
```
```javascript
Model: "functional_1"
│ conv2d_transpose_3 (Conv2DTranspose) │ (None, 64, 64, 32)   │        18,464 │
│ conv2d_transpose_4 (Conv2DTranspose) │ (None, 128, 128, 16) │         4,624 │
│ batch_normalization_3                │ (None, 128, 128, 16) │            64 │
│ conv2d_transpose_5 (Conv2DTranspose) │ (None, 256, 256, 3)  │           435 │
 Total params: 47,299 (184.76 KB)
 Trainable params: 47,203 (184.39 KB)
 Non-trainable params: 96 (384.00 B)
```
**Quarantasettemila parametri in tutto.** È il modello più piccolo delle cinque giornate — meno del `Dense(84)` di LeNet-5 da solo — e lavora su immagini 256×256. È la proprietà delle reti completamente convolutive: il costo dipende dai **kernel**, non dalla dimensione dell'immagine.
La loss è l'**errore quadratico medio** fra l'immagine ricostruita e quella ad alta risoluzione vera: non c'è nessuna etichetta esterna, il bersaglio è un'altra immagine. Il learning rate è `0.0001`, dieci volte meno del default di Adam.
`scritta in aula` — cella `[11]`:
```python
# Train model
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=10
)
```
```javascript
Epoch 7/10   43/43 ━━━━━━━━━━ 6s 138ms/step - loss: 0.0407 - val_loss: 0.0449
Epoch 8/10   43/43 ━━━━━━━━━━ 5s 120ms/step - loss: 0.0420 - val_loss: 0.0373
Epoch 9/10   43/43 ━━━━━━━━━━ 10s 125ms/step - loss: 0.0381 - val_loss: 0.0303
Epoch 10/10  43/43 ━━━━━━━━━━ 11s 156ms/step - loss: 0.0383 - val_loss: 0.0250
```
<callout icon="➕">
	**È l'unico modello delle quattro giornate che non va in overfitting**, e si vede da un dettaglio: la `val_loss` è **più bassa** della loss di addestramento, e continua a scendere quando quella di addestramento si è già assestata.
	Le due ragioni sono entrambe nel codice: 47 mila parametri sono pochissimi per memorizzare 688 immagini, e l'addestramento vede l'aumento dei dati mentre la validazione no (`augment=True` solo per `train_ds`). A dieci epoche il modello sta ancora migliorando: è l'unico caso del corso in cui **fermarsi presto è uno spreco**, non una salvezza.
	Questa lettura è mia; il docente non commenta i numeri.
</callout>
> **Punto risolto dal materiale ufficiale.** La tabella del `summary()` proseguiva sotto il bordo inferiore ed era **\[illeggibile\]**. La versione precedente di questo manuale aveva ricostruito l'encoder deducendolo dai due soli conteggi leggibili — 448 e 4.640 — e la ricostruzione risulta **corretta**: `3·3·3·16+16 = 448`, `3·3·16·32+32 = 4.640`.
---
## 11. Guardare i risultati — `TF-10 @ 00:52:00`
`scritta in aula` — celle `[12]`, `[13]`:
```python
# Visualization function: show low-res, super-res, and high-res images
def show_images(model, num_images=3):
  for lowers_batch, highers_batch in val_ds.take(1):
    preds = model.predict(lowers_batch)
    fig, axis = plt.subplots(num_images, 3, figsize=(12, 5*num_images))
    for i in range(num_images):
      axis[i, 0].imshow(lowers_batch[i])
      axis[i, 0].set_title("Low-res")
      axis[i, 1].imshow(preds[i])
      axis[i, 1].set_title("Prediction")
      axis[i, 2].imshow(highers_batch[i])
      axis[i, 2].set_title("OG High-res")
      for ax in axis[i]:
        ax.axis("off")
    plt.show()
```
```python
# Plot predictions on validation data
show_images(model)
```
Il docente lo costruisce a voce (`TF-10 @ 00:53:00`–`00:56:00`): «una `subplot` di… il *lower resolution*, *super resolution*… e prendiamo solo **tre**… la dimensione dell'immagine potrebbe essere **5 per il numero di immagini**… questo è il *low resolution*, e poi questa è la **predizione**, e poi questa invece è l'**originale**… e per l'`axis`, non mostriamo… non facciamo mostrare quella *grid*».
**Diagramma.** Tre righe per tre colonne: bassa risoluzione, ricostruzione, originale. Il titolo «OG High-res» compare 93 volte negli indici OCR, quindi la figura resta a schermo a lungo.
> **Una precisazione sul confronto.** La colonna «Low-res» non mostra immagini più piccole: `load_image` le ha già portate tutte a 256×256 con `resize`. Quello che si vede a sinistra è l'immagine a bassa risoluzione **ingrandita**, quindi sfocata. È il confronto giusto — sfocata contro ricostruita contro nitida — ma il nome della colonna può trarre in inganno.
`scritta in aula` — cella `[14]`:
```python
# Save model weights
model.save_weights("sresolution.weights.h5")
```
> **Punto risolto dal materiale ufficiale.** Questa cella non era mai inquadrata completa e la versione precedente di questo manuale ne dava una forma **dichiaratamente indicativa**, ricostruita dal parlato. Adesso è verbatim.
---
## 12. `TITANIC-HELLOWORLD`: dati tabellari — `TF-10 @ 01:20:00`
Ultimo notebook della giornata e del corso registrato. È l'unico caso di studio su **dati tabellari** dei cinque giorni.
`già nel materiale` — l'intestazione, che elenca il piano in sei punti: caricare ed esplorare, analizzare il bilanciamento delle classi, preprocessare, visualizzare le correlazioni, addestrare, valutare. E una tabella con la descrizione di ogni colonna, che dichiara già quali non verranno usate: `Name` («not used in model»), `Ticket` («not used»).
`scritta in aula` — celle `[1]`, `[3]`:
```python
# import
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```
```python
data_train = pd.read_csv("../titanic/train.csv")
data_test = pd.read_csv("../titanic/test.csv")
data_train.head(2)
```
Sono gli stessi CSV del Titanic usati nella giornata 3 per `tf.data`, qui letti con pandas — il percorso `../titanic/` punta fuori dalla cartella del notebook.
`scritta in aula` — celle `[6]`, `[8]`, le due esplorazioni:
```python
ax = data_train['Survived'].value_counts().plot(kind='bar', figsize=(10, 4))
ax.set_ylabel('counts')
ax.set_xlabel('survived')
plt.show()
```
```python
ax = data_train['Age'].plot(kind='hist', bins=20, color='red', figsize=(8, 5))
ax.set_ylabel('Frequency')
ax.set_xlabel('Age')
plt.show()
```
Il markdown che le precede spiega perché si guardano proprio queste due: il conteggio dei sopravvissuti «helps assess class balance (important for choosing metrics and loss functions)» — cioè decide se l'accuratezza basti o servano precision e recall, il tema della giornata 3; e l'istogramma delle età «helps us understand missing data».
**Il preprocessing.** `scritta in aula` — cella `[10]`:
```python
def preprocess(df):
    returnDf = pd.DataFrame()
    dfPClass = pd.get_dummies(df['Pclass'], prefix='Pclass')
    dfSex = pd.get_dummies(df['Sex'])
    returnDf = pd.concat([returnDf, dfPClass, dfSex], axis=1)

    returnDf['Age'] = df['Age'].fillna(0)
    returnDf['Age_is_null'] = pd.isna(df['Age']).astype('int32')
    returnDf['SibSp'] = df['SibSp']
    returnDf['Parch'] = df['Parch']
    returnDf['Fare'] = df['Fare']
    returnDf['Cabin_null'] = pd.isna(df['Cabin']).astype('int32')
    dfEmbarked = pd.get_dummies(df['Embarked'], dummy_na=True, prefix='Embarked')
    returnDf = pd.concat([returnDf, dfEmbarked], axis=1)
    return returnDf
```
`TF-10 @ 01:20:00`: «facciamo anche che *null* lo mettiamo anche, creiamo anche **un'altra colonna** per quello. E poi il *prefix* lo mettiamo…»
> **Il trattamento dei valori mancanti è la parte da leggere con attenzione**, e la funzione lo fa in tre modi diversi:
>
> - **`Age`**: riempita con 0 **più** una colonna `Age_is_null` che segnala dove è stato fatto. La rete può così distinguere «neonato» da «età sconosciuta» — riempire e basta le confonderebbe.
> - **`Cabin`**: il valore non viene usato affatto, solo la sua **presenza** (`Cabin_null`). Su questo dataset avere una cabina registrata è correlato alla classe e alla sopravvivenza: l'informazione utile è che il dato esista.
> - **`Embarked`**: `dummy_na=True` dà ai mancanti una **colonna propria** fra le dummy.
>
> Tre strategie per tre situazioni diverse, in una funzione di dodici righe.
`scritta in aula` — cella `[12]`:
```python
x_train = preprocess(data_train)
x_train.head()
```
Il risultato, commentato a schermo: «potete vedere ad esempio questo… vedete, *female*, e alcune cose, l'*embarked* e tutti».
**La correlazione, saltata.** `TF-10 @ 01:21:30`: «al momento vogliamo vedere un po' di *correlation analysis*, ma **lo togliamo perché non abbiamo abbastanza tempo**».
> Il markdown della sezione «Correlation Analysis» c'è nel notebook, e promette una *heatmap*; la cella sotto contiene solo la chiamata a `preprocess`. **La heatmap non esiste in nessuna versione del notebook**, né iniziale né finale. Non è stata tagliata dal video: non è mai stata scritta.
**Il modello.** `scritta in aula` — celle `[14]`, `[16]`:
```python
def create_model():
    inputs = tf.keras.layers.Input(shape=(x_train.shape[1],))
    x = tf.keras.layers.Dense(32, activation="relu")(inputs)
    outputs = tf.keras.layers.Dense(1, activation="sigmoid")(x)
    return tf.keras.Model(
        inputs=inputs,
        outputs=outputs
    )
```
```python
model = create_model()
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
```
Un passaggio che il docente corregge dal vivo (`TF-10 @ 01:23:00`): «devo creare… `create_model`, perché questo non va bene… **devo definire prima l'input** e in funzione di quello, non posso definire direttamente così». È la differenza fra l'API `Sequential` e quella **funzionale**: con la funzionale ogni layer si applica al tensore precedente, quindi l'input deve esistere prima.
Sulla forma dell'input: «dovrebbe essere `x_train.shape`, il **secondo** \[elemento\] è la dimensione» — cioè il numero di colonne dopo il dummy encoding.
**Un solo strato nascosto da 32 unità.** È il modello più piccolo del corso dopo l'autoencoder, ed è appropriato: poche centinaia di righe di dati non ne reggono di più.
`scritta in aula` — celle `[18]`, `[19]`:
```python
x_train = x_train.astype(np.float32)
history = model.fit(
    x_train.values,
    data_train['Survived'].values,
    batch_size=32,
    epochs=40,
    validation_split=0.2
)
```
```javascript
Epoch 39/40  23/23 ━━━━━━━━━━ 0s 4ms/step - accuracy: 0.7975 - loss: 0.4637 - val_accuracy: 0.8268 - val_loss: 0.4100
Epoch 40/40  23/23 ━━━━━━━━━━ 0s 4ms/step - accuracy: 0.7899 - loss: 0.4579 - val_accuracy: 0.8212 - val_loss: 0.3915
```
```python
def plot_metric(history, metric):
    train_metrics = history.history[metric]
    val_metrics = history.history['val_' + metric]
    epochs = range(1, len(train_metrics) + 1)
    plt.plot(epochs, train_metrics, 'bo--', label=f'Train {metric}')
    plt.plot(epochs, val_metrics, 'ro-', label=f'Validation {metric}')
    plt.xlabel('Epochs')
    plt.ylabel(metric)
    plt.title(f'Training and Validation {metric}')
    plt.legend()
    plt.show()

plot_metric(history, 'loss')
```
L'`astype(np.float32)` non è un dettaglio: `get_dummies` produce colonne **booleane**, e Keras non le accetta.
**82.12% in validazione**, e per una volta la validazione sta **sopra** l'addestramento (0.8212 contro 0.7899) con una loss più bassa (0.39 contro 0.46) — nessun overfitting in quaranta epoche.
**Il test.** `scritta in aula` — celle `[21]`, `[22]`, `[23]`, `[24]`:
```python
x_test = preprocess(data_test)
```
```python
# Align columns
x_test = x_test.reindex(columns=x_train.columns, fill_value=0)
```
```python
x_test = x_test.fillna(0).astype(np.float32)
```
```python
y_pred_probs = model.predict(x_test).flatten()
submission_df = pd.read_csv("../titanic/gender_submission.csv")
y_test = submission_df['Survived'].values
```
> **La cella ****`# Align columns`**** risolve un problema che si presenta sempre e non si vede mai.** `get_dummies` crea le colonne a partire dai **valori presenti nei dati**. Se nel test manca un porto d'imbarco, o compare una classe che nel train non c'era, le due tabelle hanno colonne diverse — e il modello, che si aspetta un numero fisso di ingressi in un ordine fisso, fallisce o peggio produce numeri senza senso.
>
> `reindex(columns=x_train.columns, fill_value=0)` forza il test ad avere **esattamente** le colonne del train, nello stesso ordine, riempiendo di zeri quelle assenti e scartando quelle in più. È una riga, ed è la differenza fra un modello che funziona in produzione e uno che funziona solo sul proprio notebook.
**L'ultima cella, mai eseguita.** `già nel materiale` — cella `[25]`, senza contatore di esecuzione:
```python
from sklearn.metrics import precision_recall_curve, auc

precisions, recalls, thresholds = precision_recall_curve(y_test, y_pred_probs)
pr_auc = auc(recalls, precisions)

plt.figure(figsize=(10, 6))
plt.plot(thresholds, precisions[:-1], "b--", label="Precision")
plt.plot(thresholds, recalls[:-1], "g-", label="Recall")
plt.xlabel("Threshold")
plt.ylabel("Score")
plt.title(f"Precision and Recall vs Threshold (PR AUC = {pr_auc:.2f})")
plt.legend()
plt.grid(True)
```
È la curva precision-recall della giornata 3, scritta con lo strumento diretto di scikit-learn invece che con il ciclo su cento soglie. **Non viene mai eseguita**: il contatore è vuoto e non c'è output.
Il docente ammette il limite di tempo (`TF-10 @ 01:24:30`): «tanto forse non abbiamo tempo, ma potete anche continuare». La registrazione si interrompe su un errore — «*Invalid object*, quale?» — il cui messaggio non è mai inquadrato: **\[illeggibile\]**.
<callout icon="➕">
	**Il corso registrato finisce qui**, su una cella non eseguita e un errore non letto. La valutazione del modello Titanic — l'ultimo dei sei punti che l'intestazione del notebook prometteva — non esiste in nessuna fonte.
	Vale la pena notare, per chi volesse completare l'esercizio, che `y_test` viene da `gender_submission.csv`: è il file di esempio di Kaggle, che predice la sopravvivenza **in base al solo sesso**. Non sono le etichette vere del test set — quelle Kaggle non le distribuisce. La curva precision-recall che ne uscirebbe misura quanto il modello somiglia a quella regola, non quanto è accurato. Questa osservazione è mia.
</callout>
---
## Esercizi lasciati aperti
**Dalla giornata 4, ripreso qui** (`TF-09 @ 00:46:00`): riprendere la generazione di titoli, fare fine-tuning e ricaricare da checkpoint con `load_model`. Resta scritto nel notebook: `# exrcise: load model from checkpoints`.
**A voce, in questa giornata:**
- `TF-09 @ 00:45:30` — «io vorrei che potete generare una headline che **ha senso**»: il modello a 5 epoche produce `of the new york of the times of the new`;
- `TF-09 @ 00:47:30` — migliorare il modello di forecast prima di prenderlo sul serio: «non potete usare questo se volete fare trading»;
- `TF-10 @ 00:03:00` — completare il confronto fra i tre modelli LSTM: «forse possiamo lasciare per voi, se volete prendere questo»;
- `TF-10 @ 01:24:30` — completare il Titanic: «forse non abbiamo tempo, ma potete anche continuare».
**E quattro esercizi che il materiale lascia senza dirlo**, perché il codice c'è ma non gira: la previsione ricorsiva a 30 giorni (`forecast_future`, mai chiamata e con un `return` sbagliato), la heatmap delle correlazioni del Titanic (promessa dal markdown, mai scritta), la curva precision-recall del Titanic (scritta, mai eseguita), e il confronto fra i tre LSTM in forma di tabella (i numeri ci sono, il confronto no).
---
## Glossario dei termini introdotti
<table header-row="true">
<tr>
<td>Termine</td>
<td>Definizione data nella lezione</td>
</tr>
<tr>
<td>**Campionamento invece di ****`argmax`**</td>
<td>Nella generazione di testo si estrae dalla distribuzione invece di prendere il massimo, altrimenti l'output è deterministico e ciclico. `TF-09 @ 00:03:00`</td>
</tr>
<tr>
<td>**`squeeze`**** e ****`[-1]`**** nella generazione**</td>
<td>Togliere la dimensione di batch e prendere **l'ultimo** passo della sequenza: è lì che sta la predizione del token successivo. `TF-09 @ 00:02:00`–`00:02:30`</td>
</tr>
<tr>
<td>**Tokenizer**</td>
<td>«Trasforma le parole alla loro base»: *meeting* → *meet*. `TF-09 @ 00:15:00`</td>
</tr>
<tr>
<td>**Il tokenizer è legato al modello**</td>
<td>«Non potete usare lo stesso token che sta usando Llama o Anthropic»: token ed embedding devono venire dallo stesso addestramento. `TF-09 @ 00:16:30`</td>
</tr>
<tr>
<td>**`len(word_index) + 1`**</td>
<td>L'indice 0 è riservato al padding, quindi il vocabolario ha una posizione in più. Qui: **11.265**. `TF-09 @ 00:18:00`</td>
</tr>
<tr>
<td>**Sequenze progressive (n-grammi)**</td>
<td>Per ogni titolo si generano tutti i prefissi: l'ultimo token è l'etichetta. Da 15.000 titoli escono 51.770 esempi. `TF-09 @ 00:17:30`</td>
</tr>
<tr>
<td>**Costo del one-hot**</td>
<td>51.770 × 11.265 float = 2,3 GB di etichette quasi tutte zero. La `SparseCategoricalCrossentropy` lo evita. `TF-09 @ 00:46:30`</td>
</tr>
<tr>
<td>**`MinMaxScaler`**</td>
<td>Normalizzazione dei prezzi in `[0, 1]` prima di darli alla rete; lo `scaler` va conservato per `inverse_transform`. `TF-09 @ 00:54:00`</td>
</tr>
<tr>
<td>**Split temporale**</td>
<td>Su una serie storica il test set sono gli **ultimi** giorni, non un campione casuale. `TF-09 @ 01:02:00`</td>
</tr>
<tr>
<td>**`input_shape=(1, 1)`**</td>
<td>Un passo temporale, una feature: «abbiamo solo il prezzo e poi il tempo giornaliero». `TF-09 @ 01:07:00`, `01:22:30`</td>
</tr>
<tr>
<td>**`return_sequences=True`**</td>
<td>Necessario su ogni LSTM tranne l'ultimo, per impilarli: ciascuno deve passare al successivo l'intera sequenza. `TF-09 @ 01:08:30`</td>
</tr>
<tr>
<td>**`EarlyStopping`**** con ****`restore_best_weights`**</td>
<td>Ferma l'addestramento e **ripristina** i pesi migliori; richiede però una metrica di validazione per funzionare. `TF-09 @ 01:12:00`</td>
</tr>
<tr>
<td>**Previsione ricorsiva**</td>
<td>La predizione del giorno *n* diventa l'input del giorno *n+1*. `TF-10 @ 00:00:30`</td>
</tr>
<tr>
<td>**Ipotesi markoviana**</td>
<td>«Dipende solo dal giorno precedente»: assunzione dichiarata, che fa accumulare gli errori. `TF-10 @ 00:01:00`</td>
</tr>
<tr>
<td>**`pathlib`**** con ****`/`**</td>
<td>L'operatore divisione concatena i percorsi. `TF-10 @ 00:16:30`</td>
</tr>
<tr>
<td>**Canale alpha**</td>
<td>Va rimosso con `.convert("RGB")`: alcune immagini hanno 4 canali invece di 3. `TF-10 @ 00:18:00`</td>
</tr>
<tr>
<td>**`tf.numpy_function`**</td>
<td>Avvolge una funzione Python (qui PIL) in un'operazione del grafo; obbliga a dichiarare la forma a mano con `set_shape`. `TF-10 @ 00:30:00`</td>
</tr>
<tr>
<td>**Autoencoder per super-risoluzione**</td>
<td>Convoluzioni con `strides=2` che riducono, `Conv2DTranspose` che ricostruiscono; loss = MSE fra ricostruita e originale. 47.299 parametri in tutto. `TF-10 @ 00:41:04`</td>
</tr>
<tr>
<td>**Dummy encoding con ****`dummy_na`**</td>
<td>Le categoriche diventano colonne binarie, e i valori mancanti ottengono **una colonna propria**. `TF-10 @ 01:20:00`</td>
</tr>
<tr>
<td>**Colonna-sentinella per i mancanti**</td>
<td>`Age` riempita con 0 **più** `Age_is_null`: la rete distingue «zero» da «non so». `TF-10 @ 01:20:30`</td>
</tr>
<tr>
<td>**`reindex`**** fra train e test**</td>
<td>Le dummy dipendono dai valori presenti: le colonne del test vanno allineate a quelle del train, riempiendo di zeri. `TF-10 @ 01:25:00`</td>
</tr>
<tr>
<td>**API funzionale e ordine**</td>
<td>«Devo definire prima l'input, e in funzione di quello»: con l'API funzionale il tensore d'ingresso deve esistere prima dei layer. `TF-10 @ 01:23:00`</td>
</tr>
</table>
---
## Punti a bassa confidenza
**95 segmenti segnalati** su 994 (TF-09: 34 su 501, TF-10: 61 su 493), più **20 segmenti di boilerplate rimossi**. **È la giornata con più punti incerti delle quattro**, e la ragione è visibile nella trascrizione: nella seconda metà il docente lavora in fretta, dichiara più volte di essere a corto di tempo e detta il codice a mezza voce mentre digita. Elenco completo con i motivi in **`day-05-bassa-confidenza.md`**.
> **La conseguenza sulla fedeltà è cambiata.** La versione precedente di questo manuale conteneva, nelle sezioni finali, blocchi di codice **ricostruiti dal parlato** e dichiarati indicativi. Con i notebook ufficiali non ce ne sono più: **tutto il codice di questo manuale è verbatim.** L'audio incerto resta, ma non tocca più il codice.
### Testo a schermo non leggibile `[illeggibile]`
Il materiale ufficiale ha **risolto nove dei dieci** punti che la versione precedente segnalava — è il recupero più consistente delle quattro giornate. Resta:
<table header-row="true">
<tr>
<td>Dove</td>
<td>Punto</td>
<td>Perché resta aperto</td>
</tr>
<tr>
<td>`TF-10 @ 01:26:00`</td>
<td>L'errore su cui si chiude la registrazione — «*Invalid object*, quale?» — non è mai inquadrato</td>
<td>Il notebook distribuito contiene la versione corretta e non conserva nessun errore</td>
</tr>
</table>
**Risolti dal notebook ufficiale:** `pad_sequences` e `predictors`/`labels` (`TF-09 @ 00:27:35`), `generate_headline` (`TF-09 @ 00:42:35`), `MinMaxScaler` e split temporale (`TF-09 @ 00:54:37`, `01:02:50`), le unità del secondo LSTM — che era `int(units/2)`, cioè 16 — (`TF-09 @ 01:09:00`), il secondo e il terzo modello LSTM (`TF-09 @ 01:13:37`, `01:18:37`), il `summary()` dell'autoencoder (`TF-10 @ 00:45:53`), la figura a tre colonne (`TF-10 @ 00:55:45`), il preprocessing del Titanic (`TF-10 @ 01:18:50`), le celle `compile` e `fit` del Titanic (`TF-10 @ 01:23:40`).
**Sulla «Correlation Analysis» saltata** (`TF-10 @ 01:21:30`): non era un `[illeggibile]` ma un'assenza vera. Il notebook ha il titolo markdown e non ha la cella: la heatmap non è mai stata scritta.
---
## Materiale ufficiale usato
<table header-row="true">
<tr>
<td>File</td>
<td>Ruolo</td>
</tr>
<tr>
<td>`20-06-2025/HEADLINE-GEN-completed.ipynb`</td>
<td>**Fonte** delle sezioni 2-6</td>
</tr>
<tr>
<td>`20-06-2025/BTC-EUR-FORECAST-completed.ipynb`</td>
<td>**Fonte** delle sezioni 7-8</td>
</tr>
<tr>
<td>`20-06-2025/SUPER_RES_colab.ipynb`</td>
<td>**Fonte** delle sezioni 9-11</td>
</tr>
<tr>
<td>`20-06-2025/TITANIC-HELLOWORLD-completed.ipynb`</td>
<td>**Fonte** della sezione 12</td>
</tr>
<tr>
<td>`20-06-2025/initial/estratto/materials/`</td>
<td>Le versioni scheletro, più i dati: `BTC_EUR-Kraken-Historical-Data.csv`, `ny.zip`, `archive.zip`, `HEADLINE-GEN.md`</td>
</tr>
<tr>
<td>`19-06-2025/5_CharGen_LSTM_colab.ipynb`</td>
<td>Fonte della sezione 1 (notebook della giornata 4, ripreso qui)</td>
</tr>
<tr>
<td>`TF-09.mp4`, `TF-10.mp4`</td>
<td>Fonte della **sequenza** e di tutto ciò che non è nei notebook: le correzioni dal vivo, la sezione saltata per mancanza di tempo, l'errore finale, gli esercizi a voce</td>
</tr>
</table>
Elenco completo delle divergenze: **`day-05-divergenze.md`**.
Verifica per esecuzione: **`VERIFICA-day-05.md`**.
## Notebook della lezione
I file originali del docente, sul tuo Mac in `Downloads/TensorFlow-MDA/Materiale Sito/estratti/`:
- `20-06-2025/20-06-2025/SUPER_RES_colab.ipynb`
- `20-06-2025/20-06-2025/TITANIC-HELLOWORLD-completed.ipynb`
