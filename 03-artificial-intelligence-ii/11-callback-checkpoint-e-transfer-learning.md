# 11 - Callback, checkpoint e transfer learning
> Fonte Notion: https://app.notion.com/p/3d612abc808d8164ba41d91537cd27d1 — ultima modifica 2026-09-09T23:31:33.977Z

> Giornata 4 del corso · video `TF-07` e `TF-08`
---
## 8. `2.callbacks-n-debug`: CNN su CIFAR — `TF-07 @ 01:03:40`
Secondo notebook, «**CNN Classification & Training Debugging with Callbacks**», con nove sezioni numerate `già nel materiale`.
`scritta in aula` — cella `[4]`:
```python
d_train = tf.keras.utils.image_dataset_from_directory(
    "./data/cifar/train/",
    seed=42,
    image_size=(32, 32),
    batch_size=None
)

d_test = tf.keras.utils.image_dataset_from_directory(
    "./data/cifar/test/",
    seed=42,
    image_size=(32, 32),
    batch_size=None
)
```
```javascript
Found 50000 files belonging to 10 classes.
Found 10000 files belonging to 10 classes.
```
È l'API moderna che sostituisce l'`ImageDataGenerator` della giornata 3. `batch_size=None` restituisce esempi singoli: il batch verrà fatto dopo, nella pipeline.
`scritta in aula` — cella `[5]`:
```python
## create classname file for predict later
class_names = d_train.class_names
with open("cifarlabel.txt", "w") as f:
    for cl in class_names:
        f.write(f"{cl}\n")
```
I nomi delle classi vengono dalle sottocartelle e sono salvati su file: serviranno nel notebook `3.`, che gira in un processo diverso e non ha modo di ricavarli.
`scritta in aula` — cella `[7]`, l'aumento dei dati:
```python
def random_transformation(im, label):
    image = im / 255.
    image = tf.image.random_brightness(image, max_delta=0.1)
    image = tf.image.random_flip_left_right(image)
    image = tf.image.random_contrast(image, lower=.5, upper=.8)
    return image, label

def show_image(im, label):
    plt.figure()
    plt.imshow(im)
    plt.title(class_names[label.numpy()])
    plt.axis('off')

for im, label in d_train.take(2):
    im_normalized = im / 255.
    show_image(im_normalized, label)
    im_random, label_rand = random_transformation(im, label)
    show_image(im_random, label_rand)
```
Tre trasformazioni casuali — luminosità, specchiatura orizzontale, contrasto — applicate insieme alla normalizzazione. Il ciclo finale mostra **la stessa immagine due volte**, prima e dopo, che è il modo di verificare a occhio che l'aumento non abbia distrutto il soggetto.
> La specchiatura orizzontale è sicura su CIFAR (un cane specchiato resta un cane) ma non lo sarebbe su MNIST, dove una cifra specchiata cambia significato. Il docente non lo commenta.
`scritta in aula` — cella `[8]`, lasciata come promemoria:
```python
# debug data (improvement)
```
`scritta in aula` — cella `[10]`, l'architettura:
```python
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(
        input_shape=[32, 32, 3],
        filters=6,
        kernel_size=5,
        activation="relu",
        kernel_initializer="he_uniform"
    ),
    tf.keras.layers.MaxPool2D(
        (2, 2),
        strides=2
    ),
    tf.keras.layers.Conv2D(
        filters=16,
        kernel_size=5,
        activation="relu",
        kernel_initializer="he_uniform"
    ),
    tf.keras.layers.MaxPool2D(
        (2, 2),
        strides=2
    ),
    tf.keras.layers.Conv2D(
        filters=128,
        kernel_size=1,
        activation="relu",
        kernel_initializer="he_uniform"
    ),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation="relu"),
    tf.keras.layers.Dense(256, activation="relu"),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(len(class_names), activation="softmax"),
])

model.summary()
```
```javascript
│ dense (Dense)                   │ (None, 512)            │     1,638,912 │
│ dense_1 (Dense)                 │ (None, 256)            │       131,328 │
│ dense_2 (Dense)                 │ (None, 128)            │        32,896 │
│ dense_3 (Dense)                 │ (None, 10)             │         1,290 │
 Total params: 1,809,474 (6.90 MB)
```
**È LeNet-5 con tre modifiche**: ReLU al posto della tangente iperbolica, max pooling al posto dell'average, e una testa densa molto più grande (512 → 256 → 128 → 10). Da 257 mila a **1,8 milioni** di parametri, di cui il 90% nel primo `Dense`.
`kernel_initializer="he_uniform"` è l'inizializzazione pensata per la ReLU — la stessa cosa di cui il docente aveva parlato nella giornata 3 lasciandola come esercizio.
`scritta in aula` — celle `[12]`, `[14]`, `[15]`:
```python
model.compile(
    optimizer="adam",
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics=["accuracy"]
)
```
```python
d_train_transformed = d_train.shuffle(1000).batch(32).map(random_transformation)
d_test_transformed = d_test.batch(32).map(random_transformation)
```
```python
# cache data
d_train_transformed = d_train_transformed.cache().prefetch(tf.data.AUTOTUNE)
d_test_transformed = d_test_transformed.cache().prefetch(tf.data.AUTOTUNE)
```
Qui la loss è **sparse**, non categorical: `image_dataset_from_directory` dà etichette intere, non one-hot. È la distinzione della giornata 3, applicata.
E la pipeline `shuffle → batch → map → cache → prefetch` è la cella `# explained next time` che la giornata 3 aveva rinviato.
<callout icon="➕">
	**Nota aggiunta:** `map` dopo `batch` applica `random_transformation` all'intero batch, quindi tutte le 32 immagini di un batch ricevono **la stessa** luminosità e lo stesso contrasto. Con `map` prima di `batch` ogni immagine avrebbe la sua.
	Più importante: `random_transformation` è applicata **anche al test set**. Il modello viene quindi valutato su immagini deformate a caso, il che contribuisce a tenere bassa la `val_accuracy`. Il docente non commenta né l'una né l'altra cosa.
</callout>
---
## 9. Warm-up, checkpoint e TensorBoard — `TF-07 @ 01:10:00`
**Il warm-up.** `TF-07 @ 01:10:00`: «ricordate che quando facciamo un addestramento facciamo prima un piccolo **warm-up** e poi facciamo — come vediamo anche come si fa un *fine-tuning* — ma l'idea è che adesso facciamo un piccolo warm-up del modello e poi facciamo il vero addestramento».
E il vincolo pratico: «ovviamente io non sto usando la GPU, e vedete che questo modello è più grande e non posso usare la GPU qua. Allora forse qua faccio solo una piccola epoca. Due, forse».
`scritta in aula` — cella `[17]`:
```python
model.fit(
    d_train_transformed,
    epochs=2,
    validation_data=d_test_transformed
)
```
```javascript
Epoch 1/2
1563/1563 ━━━━━━━━━━━━━━━━━━━━ 50s 31ms/step - accuracy: 0.3191 - loss: 1.8533 - val_accuracy: 0.4940 - val_loss: 1.4132
Epoch 2/2
1563/1563 ━━━━━━━━━━━━━━━━━━━━ 54s 35ms/step - accuracy: 0.4997 - loss: 1.4002 - val_accuracy: 0.5405 - val_loss: 1.3054
```
**Due avvertimenti che ritornano.** `TF-07 @ 01:11:00`:
1. «Ricordate che la `prefetch` è già *on batch*. Allora non ho più bisogno di mettere il `batch` qua.»
2. «Non posso usare il `validation_split` qua, perché se no mi dà un errore: ho un dato che ha già fatto il `prefetch` e non posso più fare uno split di questo dataset. Allora devo dare come `validation_data` il *test transformed*.»
È esattamente la situazione anticipata nella sezione 4.
**Le callback.** `TF-07 @ 01:12:00`: «una funzione si chiama **callback**, nel senso che noi possiamo creare un'azione che viene lanciata **per ogni epoca**». E i due usi: «l'uso del **TensorBoard** per vedere l'addestramento *online*, e poi anche il **checkpoint** per salvare i pesi per ogni epoca — ma dipende dalla posizione che gli diamo».
`scritta in aula` — celle `[19]`, `[20]`:
```python
callbacks = [
    tf.keras.callbacks.ModelCheckpoint(
        filepath="./checkpoints/cifar/model.{epoch:02d}-{val_loss:.3f}.keras",
        save_best_only=True
    ),
    tf.keras.callbacks.TensorBoard(
        log_dir="./logs/cifar/"
    )
]
```
```python
model.fit(
    d_train_transformed,
    epochs=5,
    validation_data=d_test_transformed,
    callbacks=callbacks
)
```
```javascript
Epoch 2/5  accuracy: 0.6177 - loss: 1.0923 - val_accuracy: 0.5430 - val_loss: 1.3782
Epoch 3/5  accuracy: 0.6643 - loss: 0.9540 - val_accuracy: 0.5119 - val_loss: 1.5438
Epoch 4/5  accuracy: 0.6986 - loss: 0.8553 - val_accuracy: 0.5074 - val_loss: 1.5968
Epoch 5/5  accuracy: 0.7331 - loss: 0.7599 - val_accuracy: 0.4977 - val_loss: 1.7859
```
**Il nome del file, spiegato.** `TF-07 @ 01:13:30`: «basta che gli do il path dove lo salvo… visto che questo callback ha accesso ad alcune variabili — ad esempio l'**indice dell'epoca** — allora io posso mettere questa epoca qua. E posso dire anche che usa **due decimali**. E poi, se ho messo `validation_data`, allora avrò anche accesso a `val_loss` e `val_accuracy`, se nel `compile` ho usato anche `accuracy`».
Una precisazione: «questo per salvare — è proprio **non solo il peso**, ma è proprio tutto il modello».
> **Questi quattro numeri sono un manuale di overfitting.** L'accuratezza di addestramento sale da 0.50 a 0.73; quella di validazione **scende** da 0.5405 a 0.4977, e la `val_loss` sale da 1.31 a 1.79. Con `save_best_only=True` il checkpoint viene scritto **una volta sola**, alla prima epoca: è l'unica in cui la validazione migliora.<br><br>È esattamente il caso per cui esiste l'`EarlyStopping`, che il docente nominerà solo nell'assegnazione finale.
---
## 10. Il learning rate scheduler che uccide il modello — `TF-07 @ 01:20:00`
È la sezione più istruttiva della giornata, e il docente non se ne accorge.
`scritta in aula` — cella `[22]`:
```python
def lr_scheduler(epoch):
    if epoch < 5:
        return 0.1
    elif epoch < 8:
        return 0.01
    else:
        return 0.001
    
callbacks = [
    tf.keras.callbacks.ModelCheckpoint(
        filepath="./checkpoints/cifar2/model.{epoch:02d}-{val_loss:.3f}.keras",
        save_best_only=True
    ),
    tf.keras.callbacks.TensorBoard(
        log_dir="./logs/cifar2/"
    ),
    tf.keras.callbacks.LearningRateScheduler(
        schedule=lr_scheduler
    )
]
```
L'idea è ragionevole e standard: partire con un passo grande e ridurlo a scalini.
`scritta in aula` — cella `[23]`:
```python
model.fit(
    d_train_transformed,
    epochs=10,
    validation_data=d_test_transformed,
    callbacks=callbacks
)
```
```javascript
Epoch 7/10  accuracy: 0.1003 - loss: 2.3041 - val_accuracy: 0.1000 - val_loss: 2.3049 - learning_rate: 0.0100
Epoch 8/10  accuracy: 0.1004 - loss: 2.3041 - val_accuracy: 0.1000 - val_loss: 2.3049 - learning_rate: 0.0100
Epoch 9/10  accuracy: 0.1002 - loss: 2.3036 - val_accuracy: 0.1000 - val_loss: 2.3027 - learning_rate: 0.0010
Epoch 10/10 accuracy: 0.1003 - loss: 2.3028 - val_accuracy: 0.1000 - val_loss: 2.3027 - learning_rate: 0.0010
```
<callout icon="➕">
	### Il modello è morto, e i numeri lo dicono
	**Accuratezza 0.10 su dieci classi è il caso.** Il modello tira a indovinare.
	E la loss lo conferma: **2.3026 è ****`ln(10)`**, cioè esattamente la cross-entropy di una distribuzione uniforme su dieci classi. Il modello non ha imparato niente — anzi, ha **disimparato** quello che sapeva: alla sezione 9 era arrivato al 73% in addestramento.
	**La causa è il primo scalino.** `learning_rate = 0.1` con Adam è cento volte il valore di default (0.001). I pesi vengono spinti fuori scala nelle prime iterazioni, le ReLU si spengono, i gradienti diventano zero, e **abbassare il learning rate dopo non serve più a niente**: le epoche 9 e 10, con `lr = 0.001`, restano inchiodate.
	Il docente non commenta questi numeri e passa al notebook successivo.
	Questa lettura è mia — il docente non la fa — ma è verificabile: `ln(10) = 2.302585`, e il valore stampato è `2.3027`.
</callout>
**E la conseguenza si propaga.** I checkpoint salvati in `checkpoints/cifar2/` sono quelli di questo modello: `model.01-2.317.keras`, `model.06-2.305.keras`, `model.09-2.303.keras`, `model.10-2.303.keras`. Le `val_loss` nei nomi — 2.317, 2.305, 2.303, 2.303 — sono tutte a ridosso di `ln(10)`.
È **il modello di questi checkpoint** che il notebook successivo caricherà per fare inferenza.
---
## 11. `3.callbacks-n-pred`: predire su una nuova immagine — `TF-07 @ 01:28:00` → `TF-08 @ 00:00:00`
> Questa sezione **attraversa il taglio fra i due file**.
TF-07 si chiude sulla funzione di preprocessing (`TF-07 @ 01:28:00`): «una normalizzazione. E poi, quello che usiamo sempre, il **batch**, perché dobbiamo fare un `expand_dims` di questa *image array*… **axis 0**, perché il modello aspetta un input come batch».
`scritta in aula` — cella `[2]`:
```python
def load_and_preprocess(image_path):
    img = tf.keras.preprocessing.image.load_img(
        image_path,
        target_size=(32, 32)
    )
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = img_array / 255.
    img_batch = np.expand_dims(img_array, axis=0)
    return img_batch, img
```
La funzione restituisce **due cose**: il batch da dare al modello e l'immagine originale da disegnare.
TF-08 riprende immediatamente sulla funzione che la usa.
`scritta in aula` — cella `[4]`:
```python
def predict(model, image_path, class_names=None):
    img_batch, img = load_and_preprocess(image_path)
    predictions = model.predict(img_batch)
    predcted_classes = np.argmax(predictions, axis=1)[0]
    confidence = np.max(predictions)
    plt.imshow(img)
    label = F"{class_names[predcted_classes]}" if class_names else f"{predcted_classes}"
    plt.title(f"{label}, {confidence}")
```
(`predcted_classes` è un refuso del docente, presente nel codice eseguito.)
**Perché ****`argmax`**** e perché ****`[0]`****.** `TF-08 @ 00:01:00`: «dobbiamo fare un `argmax` perché dobbiamo vedere l'**indice del massimo** di questa prediction. L'axis dobbiamo metterlo **1** perché anche questa è un batch. Allora questo `np.argmax` ritorna nello stesso shape, allora togliamo quello fuori: prendiamo quello dentro, questo lo metto zero qua».
**La confidenza.** `TF-08 @ 00:01:30`: «possiamo anche vedere la confidenza in percentuale, perché ovviamente noi possiamo avere che il softmax mi dà al massimo 0.1 — ma siccome lui deve prendere l'argmax, allora **non è tanta confidenza**».
> Ed è precisamente quello che succede qui, anche se il docente lo dice come ipotesi generale e non come diagnosi: il modello caricato è quello morto della sezione 10, che produce dieci probabilità quasi identiche, tutte intorno a 0.1.
`scritta in aula` — celle `[6]`, `[7]`, `[9]`:
```python
model = tf.keras.models.load_model(
    "./checkpoints/cifar2/model.10-2.303.keras"
)
```
```python
# Optional class names
class_names = []
with open("cifarlabel.txt", "r") as f:
    class_names = [line.strip() for line in f]
class_names
```
```javascript
['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
```
```python
predict(
    model,
    "./data/cifar/test/airplane/0001.png",
    class_names
)
```
> **Il checkpoint caricato è quello del modello morto**<br><br>`model.10-2.303.keras` è **l'ultimo checkpoint della sezione 10**: `val_loss = 2.303`, cioè `ln(10)`, cioè un classificatore che tira a indovinare.<br><br>La dimostrazione di inferenza è quindi tecnicamente corretta — carica un modello, lo applica a un'immagine, disegna il risultato con la sua confidenza — ma il numero che esce **non ha significato**: qualunque immagine dà una classe a caso con confidenza intorno a 0.1.<br><br>Il docente non lo rileva. È il motivo per cui questa sezione va letta come *come si fa l'inferenza*, non come *quanto è bravo il modello*. Vedi `day-04-divergenze.md` §3.
I nomi delle classi vengono dal file salvato nella sezione 8: due notebook diversi, due processi diversi, e il file di testo è il ponte.
---
## 12. `4.CIFAR-FINETUNE`: transfer learning su Colab — `TF-08 @ 00:12:00`
Il docente passa a **Google Colab**: `colab.research.google.com/drive/1-mz2OCFgRT-EiuqqJaaI70owdIdPoyyT`.
`già nel materiale` — l'intestazione: «This notebook demonstrates transfer learning and fine-tuning using **InceptionV3** pretrained on **ImageNet** to classify images from the **CIFAR-10** dataset.»
`già nel materiale` — cella `[2]`, il montaggio di Drive:
```python
from google.colab import drive
drive.mount('/content/drive')
```
`TF-08 @ 00:12:00`: «se io faccio `ls content drive my drive`, qui mi mostra tutti i file nel mio Google Drive. Comunque per questo progetto io non userò Google Drive, ma per voi, se volete salvare il checkpoint dentro il vostro Google Drive, va bene».
`scritta in aula` — celle `[7]`, `[8]`, `[10]`, `[11]`:
```python
(X_train, Y_train), (X_test, Y_test)  = tf.keras.datasets.cifar10.load_data()
```
```python
# Labels
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']
```
```python
data_train = tf.data.Dataset.from_tensor_slices((X_train, Y_train))
data_test = tf.data.Dataset.from_tensor_slices((X_test, Y_test))
```
```python
def plot_im(im, label):
  plt.imshow(im)
  plt.title(class_names[label.numpy()[0]])
  plt.axis('off')

for im, label in data_train.take(2):
  plot_im(im, label)
```
Il `[0]` in `label.numpy()[0]` è il dettaglio che il docente incontra dal vivo (`TF-08 @ 00:16:00`): «qua devo prendere, perché questo mi dà una **lista** con la dimensione» — le etichette di `cifar10.load_data()` hanno shape `(n, 1)`, non `(n,)`.
`scritta in aula` — celle `[13]`, `[14]`, il preprocessing:
```python
def transoform_image(im, label):
  im = tf.cast(im, tf.float32)
  im = tf.image.resize(im, (75, 75))
  im = tf.keras.applications.inception_v3.preprocess_input(im)
  return im, label
```
```python
# cache data, shuffling prefetch
data_train = data_train.shuffle(10_000).batch(50).map(transoform_image).cache().prefetch(tf.data.AUTOTUNE)
data_test = data_test.batch(50).map(transoform_image).cache().prefetch(tf.data.AUTOTUNE)
```
(`transoform_image` è un refuso del docente.) Due adattamenti obbligati: CIFAR è 32×32, InceptionV3 vuole almeno 75×75; e la normalizzazione **non** è `/255` ma quella specifica della rete, `preprocess_input`, che porta i valori in `[-1, 1]`. Usare la normalizzazione sbagliata con una rete preaddestrata è un errore silenzioso e comune.
`scritta in aula` — cella `[16]`:
```python
inception_model = tf.keras.applications.InceptionV3(include_top=False, input_shape=(75, 75, 3), weights='imagenet')
inception_model.summary()
```
`include_top=False` scarta la testa di classificazione a 1000 classi di ImageNet e lascia solo l'estrattore di caratteristiche.
---
## 13. Congelare i layer: il warm-up — `TF-08 @ 00:23:30`
`scritta in aula` — cella `[17]`, la testa nuova:
```python
x = inception_model.output
x = tf.keras.layers.GlobalAveragePooling2D()(x)
x = tf.keras.layers.Dense(1024, activation='relu')(x)
x = tf.keras.layers.Dropout(0.5)(x)
x = tf.keras.layers.Dense(512, activation='relu')(x)
x = tf.keras.layers.Dropout(0.5)(x)
x = tf.keras.layers.Dense(256, activation='relu')(x)
x = tf.keras.layers.Dropout(0.5)(x)
x = tf.keras.layers.Dense(128, activation='relu')(x)
x = tf.keras.layers.Dropout(0.5)(x)
output = tf.keras.layers.Dense(10, activation='softmax')(x)

model = tf.keras.Model(inputs=inception_model.input, outputs=output)
```
Quattro strati densi decrescenti — 1024, 512, 256, 128 — con un `Dropout(0.5)` dopo ciascuno, e l'uscita a 10 classi. L'API funzionale della sezione 6, qui applicata a un modello che esiste già: `inception_model.output` è il punto di innesto.
> **Punto risolto dal materiale ufficiale.** Questa cella non è mai inquadrata: era **\[illeggibile\]**, e la versione precedente di questo manuale riportava `Dense(266)` ricostruito dal parlato e marcato `[?]`. I valori veri sono **1024, 512, 256, 128**.
`scritta in aula` — cella `[19]`:
```python
model.summary()
```
```javascript
Total params: 24,591,274 (93.81 MB)
Trainable params: 24,556,842 (93.68 MB)
Non-trainable params: 34,432 (134.50 KB)
```
Sul conteggio (`TF-08 @ 00:23:00`): «posso fare anche un `model.summary()` per vedere quanti adesso. Sì sì, tanto era **22**, adesso **24 milioni**».
**Perché congelare.** `TF-08 @ 00:23:30`:
> «Quello che facciamo al solito è che, visto che questi layer che abbiamo aggiunto qua **non hanno ancora visto nessun dataset** e sono inizializzati con gli initializer di default di Keras — allora quello che possiamo fare è, prima, per l'*initial training*, **congelare i layer di Inception originale**.»
L'idea: se si addestrasse tutto insieme, i gradienti provenienti dai nuovi strati casuali rovinerebbero i pesi già buoni della base.
`scritta in aula` — celle `[22]`, `[23]`:
```python
for inception_layer in inception_model.layers:
  inception_layer.trainable = False
```
```python
model.summary()
```
```javascript
Total params: 24,591,274 (93.81 MB)
Trainable params: 2,788,490 (10.64 MB)
Non-trainable params: 21,802,784 (83.17 MB)
```
**Come si fa, e perché funziona.** `TF-08 @ 00:24:00`: «quando abbiamo definito così, `model.output`, questa è una **referenza**, allora noi possiamo modificare… e viene modificato automaticamente dentro il modello». Cioè: `inception_model` e `model` condividono gli stessi oggetti-layer, quindi cambiare `trainable` sull'uno si riflette sull'altro.
Il risultato (`TF-08 @ 00:25:00`): «vediamo che i parametri *trainable* erano adesso solo **2 milioni**, e ricordate che prima erano 24 milioni». Esattamente **2.788.490**: la sola testa nuova.
`scritta in aula` — celle `[25]`, `[26]`:
```python
model.compile(
    optimizer=tf.keras.optimizers.Adam(),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```
```python
model.fit(
    data_train,
    epochs=50,
    validation_data=data_test
)
```
```javascript
Epoch 5/50  accuracy: 0.6171 - loss: 1.1631 - val_accuracy: 0.6348 - val_loss: 1.0895
Epoch 6/50  accuracy: 0.6273 - loss: 1.1241 - val_accuracy: 0.6461 - val_loss: 1.0693
Epoch 7/50  accuracy: 0.6413 - loss: 1.0977 - val_accuracy: 0.6496 - val_loss: 1.0586
Epoch 8/50   708/1000 ━━━━━━━━━━━ 4s 16ms/step - accuracy: 0.6484 - loss: 1.0676
---------------------------------------------------------------------------
KeyboardInterrupt
```
**L'addestramento viene interrotto a mano**, all'ottava epoca su cinquanta. Il `KeyboardInterrupt` è salvato nel notebook distribuito, e il docente lo commenta (`TF-08 @ 00:31:00`): «no, era *interrupted*. Va bene, va bene».
Fino a lì il transfer learning funziona: **64.96%** di validazione in sette epoche, su un modello la cui base non è stata toccata — e con la validazione **sopra** l'addestramento, segno che il dropout sta lavorando e che non c'è overfitting.
---
## 14. Sfreezare e rifinire — `TF-08 @ 00:28:00`
`scritta in aula` — cella `[28]`:
```python
for inception_layer in inception_model.layers[:-75]:
  inception_layer.trainable = True
```
Il docente lo detta così (`TF-08 @ 00:28:00`): «possiamo **unfreeze** alcuni dei layer. Ad esempio, se io faccio `inception layer` così, questo mi dà direttamente tutti; ma potrebbe essere che faccio una prova, faccio solo il non-freezing dei **primi 50 layer**. O potete usare, facciamo **75**, così».
<callout icon="➕">
	### Il codice non fa quello che la voce dice
	InceptionV3 ha **311 layer**. `inception_model.layers[:-75]` significa «tutti tranne gli ultimi 75», cioè i **primi 236**.
	Il docente dice «faccio il non-freezing dei primi 75»; il codice ne sblocca **236** e lascia congelati proprio gli ultimi 75.
	E la pratica corrente del fine-tuning è l'opposto ancora: si sbloccano gli **ultimi** layer, quelli che codificano le caratteristiche specifiche del dominio, tenendo congelati i primi, che riconoscono bordi e texture valide ovunque. La forma convenzionale sarebbe `layers[-75:]`.
	Questa osservazione è mia; il docente non la fa, e il notebook distribuito contiene la versione con `[:-75]`. Vedi `day-04-divergenze.md` §5.
</callout>
`scritta in aula` — celle `[30]`, `[32]`, `[33]`:
```python
callbacks = [
    tf.keras.callbacks.ModelCheckpoint(
        filepath="./checkppoints/{epoch:02d}-{val_loss:.3f}.keras",
        save_best_only=True
    )
]
```
```python
model.compile(
    optimizer=tf.keras.optimizers.Adam(1e-5),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```
```python
model.fit(
    data_train,
    epochs=10,
    validation_data=data_test,
    callbacks=callbacks
)
```
```javascript
Epoch 1/10  131s 63ms/step - accuracy: 0.3370 - loss: 1.9390 - val_accuracy: 0.5458 - val_loss: 1.3354
Epoch 2/10   609/1000 ━━━━━━━━━━━ 19s 50ms/step - accuracy: 0.5336 - loss: 1.3692
---------------------------------------------------------------------------
KeyboardInterrupt
```
(`checkppoints` è un refuso del docente.)
**Il learning rate scende a ****`1e-5`**, cento volte meno del default. È la mossa giusta e il docente la fa senza spiegarla: quando si sbloccano layer preaddestrati, un passo normale li rovinerebbe. È l'esatto opposto dell'errore della sezione 10.
Sui tempi (`TF-08 @ 00:32:30`): «adesso abbiamo più valori, di parametri *trainable*, allora questo è più lento di quello di prima» — 63 ms per step contro 21.
Anche questo secondo addestramento viene **interrotto a mano**, alla seconda epoca. E l'accuratezza è ripartita da 0.337 contro lo 0.648 di dove si era fermato il warm-up: il modello sta ricostruendo, e servirebbero molte più epoche di quelle disponibili in aula per superare il risultato precedente.
`già nel materiale` — l'ultima cella, l'esercizio:
```python
# download the model weight and predict dal test di cifar data
```
`TF-08 @ 00:33:30`: «un esercizio che vi chiedo: scarica il *model weight* e fai una *predict* dal test di CIFAR».
## Notebook della lezione
I file originali del docente, sul tuo Mac in `Downloads/TensorFlow-MDA/Materiale Sito/estratti/`:
- `19-06-2025/19-06-2025/2.callbacks-n-debug.ipynb`
- `19-06-2025/19-06-2025/3.callbacks-n-pred.ipynb`
- `19-06-2025/19-06-2025/4_CIFAR_FINETUNE_colab.ipynb`
