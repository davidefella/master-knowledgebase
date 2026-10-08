# 12 - Generazione di testo con LSTM
> Fonte Notion: https://app.notion.com/p/3d612abc808d8124876ac3359c9f72e6 — ultima modifica 2026-09-09T23:31:36.062Z

> Giornata 4 del corso · video `TF-07` e `TF-08`
---
## 15. `5.CharGen-LSTM`: generazione di testo carattere per carattere — `TF-08 @ 00:37:00`
Ultimo notebook della giornata, su Colab con runtime **GPU**.
`già nel materiale` — l'intestazione: «This notebook demonstrates how to use LSTM networks in TensorFlow to generate text at the character level. We use the text from *Alice in Wonderland*.»
**Il compito, enunciato.** `TF-08 @ 00:37:00`: «questo è su GitHub un libro che parla di *Alice's Adventures in Wonderland*. Quello che vogliamo fare è: **data una sequenza di caratteri, generare i prossimi caratteri**. Allora questo è più o meno un modello che non ha un contesto della frase o delle parole, ma proprio dipende da quella sequenza di lettere che abbiamo prima».
`scritta in aula` — celle `[4]`, `[5]`, `[6]`:
```python
# dataset
dataURL = "https://raw.githubusercontent.com/spartrekus/ebooks/master/ebook_en_alice_wonderland_pg28885.txt"

def download_data(urls):
  texts = []
  for url in urls:
    file_path = tf.keras.utils.get_file(url.split('/')[-1], url)
    text = open(file_path, 'r').read().replace('﻿', '').replace('\n', ' ')
    text = re.sub(r'\s+', ' ', text)
    texts.extend(text)
  return texts
```
```python
texts = download_data([dataURL])
```
```python
texts[:5]
```
La funzione prende una **lista** di URL, e il docente lo motiva (`TF-08 @ 00:39:00`): «potrebbe essere che troviamo anche un altro libro, così abbiamo una funzione più o meno dinamica». È lo stesso spunto dell'assegnazione finale.
Le pulizie, dettate mentre le scrive (`TF-08 @ 00:39:30`–`00:41:30`): `get_file` restituisce **un percorso, non il testo** («questo mi dà un path, non è un text… dobbiamo leggerlo»); `﻿` è il BOM, «una carattera speciale… che non possiamo usare con ASCII»; il newline diventa uno spazio, «e lo mettiamo solo in spazio»; infine `re.sub(r'\s+', ' ')` collassa gli spazi multipli.
**`texts.extend(text)`**** invece di ****`append`****.** `extend` su una stringa la scompone nei suoi caratteri, ed è proprio quello che serve: il risultato è una lista di lettere, non una lista di libri.
`scritta in aula` — celle `[8]`, `[9]`, `[10]`:
```python
vocab = sorted(set(texts))
char2index = {c:i for i,c in enumerate(vocab)}
index2char = {i:c for c, i in char2index.items()}
```
```python
index2char
```
```python
text_input = np.array([char2index[c] for c in texts])
data = tf.data.Dataset.from_tensor_slices(text_input)
```
**La differenza con il sentiment analysis**, che il docente rende esplicita (`TF-08 @ 00:43:00`): «per quel sentiment analysis abbiamo creato il vocabolario rispetto alle **parole**… ma invece per questa *char generation* il vocabolario è rappresentato come un **carattere**, una lettera».
E il meccanismo del `set` (`TF-08 @ 00:44:30`): «quando noi prendiamo un array e lo trasformiamo in un `set`, diventa un *unique value set*, che tutti i valori sono unici. Ecco perché abbiamo creato un vocabolario rispetto a quei valori unici». Il `sorted` rende l'ordine riproducibile. Il vocabolario finale ha **86 caratteri**.
> **Punto risolto dal materiale ufficiale.** Queste celle non sono mai inquadrate complete: erano **\[illeggibile\]**, e la versione precedente di questo manuale ricostruiva `index_to_char = np.array(vocab)`. La forma vera è un **dizionario invertito**.
`scritta in aula` — cella `[12]`:
```python
seq_length = 100
sequences = data.batch(seq_length + 1, drop_remainder=True)
def split_input_label(seq):
  return seq[:-1], seq[1:]
sequences = sequences.map(split_input_label)
```
**L'idea del compito**, spiegata con il proprio nome (`TF-08 @ 00:48:30`):
> «Noi abbiamo un input *sequences*, l'output dovrebbe essere anche un'altra *sequences*. Ad esempio, se trasformiamo questo come input e label del mio modello, allora sarebbe **"sono Lu"** e l'output sequence sarà **"ono Lui"**. Quello che vogliamo, perché noi vogliamo fare la predizione dei **prossimi caratteri**.»
Il meccanismo è tutto in `batch(101)` più `seq[:-1], seq[1:]`: si prendono 101 caratteri e se ne fanno due sequenze da 100, sfasate di uno. `drop_remainder=True` scarta la coda incompleta, perché il modello richiede lunghezza fissa.
`scritta in aula` — celle `[14]`, `[15]`:
```python
def create_model(vocab_size, rnn_units, batch_size):
  inputs = tf.keras.Input(shape=(None, ), batch_size=batch_size)
  embedding = tf.keras.layers.Embedding(vocab_size, 256)(inputs)
  lstm = tf.keras.layers.LSTM(rnn_units, return_sequences=True, stateful=True)(embedding)
  dense = tf.keras.layers.Dense(vocab_size)(lstm)
  return tf.keras.Model(inputs=inputs, outputs=dense)
```
```python
model = create_model(len(vocab), 1024, 64)
model.summary()
```
```javascript
│ input_layer (InputLayer)        │ (64, None)             │             0 │
│ embedding (Embedding)           │ (64, None, 256)        │        22,016 │
│ lstm (LSTM)                     │ (64, None, 1024)       │     5,246,976 │
│ dense (Dense)                   │ (64, None, 86)         │        88,150 │
 Total params: 5,357,142 (20.44 MB)
```
**Quattro dettagli che fanno funzionare la generazione**, e sono il motivo per cui il modello è costruito da una funzione parametrica:
- `shape=(None,)` — la lunghezza della sequenza è libera;
- `return_sequences=True` — l'LSTM restituisce un'uscita **per ogni passo**, non solo per l'ultimo: serve perché l'etichetta è una sequenza intera;
- `stateful=True` — lo stato interno **sopravvive** fra una chiamata e la successiva, che è ciò che permette di generare un carattere alla volta;
- `batch_size` è **fissato nel grafo** proprio a causa di `stateful=True`, ed è la ragione per cui alla sezione 16 serve un secondo modello.
L'uscita è `Dense(86)` senza attivazione: **logit**, uno per carattere del vocabolario.
`scritta in aula` — celle `[17]`, `[18]`, `[19]`, `[21]`:
```python
model.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)
```
```python
checkpoints = tf.keras.callbacks.ModelCheckpoint(
    filepath='./training_checkpoints/model_{epoch:02d}.weights.h5',
    save_weights_only=True
)
```
```python
dataset = sequences.shuffle(10000).batch(64, drop_remainder=True).prefetch(tf.data.AUTOTUNE)
```
```python
model.fit(
    dataset.repeat(),
    epochs=100,
    steps_per_epoch=len(texts) // 101 // 64,
    callbacks=[checkpoints]
)
```
```javascript
Epoch 100/100
25/25 ━━━━━━━━━━━━━━━━━━━━ 2s 83ms/step - accuracy: 0.9706 - loss: 0.1430
```
`from_logits=True` perché l'ultimo `Dense` non ha attivazione — la regola della giornata 3. `save_weights_only=True` **e non** il modello intero, perché il modello va poi ricostruito con un `batch_size` diverso: salvare tutto non servirebbe.
`dataset.repeat()` con `steps_per_epoch` esplicito è l'uso del `repeat` che la giornata 3 aveva introdotto: il dataset scorre all'infinito e Keras decide dove finisce un'epoca. Il conto `len(texts) // 101 // 64` dà **25** passi.
<callout icon="➕">
	**Un'accuratezza del 97% su questo compito non significa quasi nulla.** Il modello predice il carattere successivo avendo visto i 100 precedenti **del testo vero**; in generazione, invece, deve costruire sul proprio output. È la differenza fra copiare con il testo davanti e scrivere a memoria, e si vede nel risultato della sezione 16. Questa osservazione è mia.
</callout>
---
## 16. Il modello di inferenza e la generazione — `TF-08 @ 01:12:00`
**Perché serve un secondo modello.** Il modello addestrato ha `batch_size=64` fissato nel grafo; per generare serve un modello a **batch 1**.
`scritta in aula` — cella `[22]`:
```python
inference_model = create_model(len(vocab), 1024, batch_size=1)
inference_model.load_weights('./training_checkpoints/model_99.weights.h5')
inference_model.build(tf.TensorShape([1, None]))
```
Il tooltip della firma, visibile a schermo: `(vocab_size: Any, rnn_units: Any, batch_size: Any) -> Any`. È il punto in cui la scelta di scrivere `create_model` come funzione parametrica paga davvero.
`scritta in aula` — cella `[23]`:
```python
def generate_chars(model, start_string, num_generate_char=100):
  input_eval = [char2index[c] for c in start_string]
  input_eval = tf.expand_dims(input_eval, 0)

  text_generated = []
  for _ in range(num_generate_char):
    predictions = model(input_eval)
    predictions = tf.squeeze(predictions, 0)
    predicted_id = tf.random.categorical(predictions[-1:], num_samples=1)[-1, 0].numpy()
    text_generated.append(index2char[predicted_id])
    input_eval = tf.expand_dims([predicted_id], 0)
  return start_string + ''.join(text_generated)
```
`TF-08 @ 01:12:00`: «dobbiamo prendere proprio questo `random_categorical` prediction, e poi, siccome non abbiamo più quella struttura, allora dobbiamo fare l'`expand_dims` per avere la stessa dimensione che avevamo prima. E poi, quando abbiamo finito la generazione, facciamo il `join` di tutto il testo generato».
Tre cose che il ciclo fa e vale la pena isolare:
1. `predictions[-1:]` — si guarda **solo l'ultimo** passo temporale; gli altri servivano solo a caricare lo stato;
2. `tf.random.categorical` invece di `argmax` — il campionamento è **stocastico**: il carattere si estrae dalla distribuzione, non si prende il massimo. Con `argmax` il testo cadrebbe subito in un ciclo ripetitivo;
3. `input_eval = tf.expand_dims([predicted_id], 0)` — al giro successivo si passa **solo il carattere appena generato**, non tutta la sequenza. Funziona perché l'LSTM è `stateful` e ricorda il resto.
`scritta in aula` — cella `[24]`, il risultato:
```python
input_text_to_generate = "Alice opened the door"

generate_chars(inference_model, input_text_to_generate)
```
```javascript
'Alice opened the door and found that it led into a small passage, not remark lyself up
 very carefully: "No remember hand '
```
Il commento del docente (`TF-08 @ 01:13:00`) è misurato: «mi sa che più o meno il nostro modello ha fatto…».
**Ed è un risultato onesto da leggere.** La prima metà — *«and found that it led into a small passage»* — è una frase corretta e coerente col libro. La seconda si sfalda: *«not remark lyself up very carefully»* ha la forma dell'inglese ma non il significato. Un modello a caratteri impara ortografia, spaziatura e punteggiatura; il senso oltre le poche decine di caratteri gli sfugge, perché non ha nessun contesto — che è esattamente quello che il docente aveva annunciato a `TF-08 @ 00:37:00`.
> **Punto risolto dal materiale ufficiale.** Nei frame il testo generato è **\[illeggibile\]** e la versione precedente di questo manuale ne riportava solo frammenti dal parlato. Il notebook conserva l'output per intero.
---
## 17. L'assegnazione finale — `TF-08 @ 01:14:00`
La giornata si chiude con un'assegnazione articolata, dettata a voce:
> «L'idea è quella che vorrei che facciate voi: **aggiungere più dataset** qua. Potete cercare su **Kaggle**, qualcosa del genere, un libro — e potete usare anche un libro **in italiano** per i vostri progetti.»
È il motivo per cui `download_data` prende una lista di URL.
E l'elenco dei miglioramenti richiesti (`TF-08 @ 01:14:30`–`01:16:00`):
1. **Cambiare l'architettura del modello.**
2. **Aggiungere un \*early stopping***: «perché ovviamente, non lo so, che siamo arrivati qua, forse possiamo cambiare un po' il learning rate… perché mi sa che più o meno abbiamo un overfitting*\*».
3. **Creare un dataset di validazione**: «quando avete più dati, più testo qua, usate anche creare un dataset per la validazione». Il notebook, infatti, addestra su tutto senza validazione: non c'è nessun `val_loss` in cento epoche.
4. **Aggiungere altre callback.**
5. **Fare il plot della ****`history`** dell'addestramento.
6. **Fare una ****`evaluate`** invece del solo testo di input: «se volete, potete creare un *data test* in cui fate un po' un confronto fra i veri dati e quello che è generato».
I punti 2 e 3 sono la risposta a due problemi che questa giornata ha mostrato senza risolverli: l'overfitting della sezione 9 e l'assenza di validazione della sezione 15.
Chiude offrendo assistenza: «domani, comunque, se avete domande di questo, potete mandare un'email o chiedermi adesso».
E l'esercizio della sezione 14, che resta scritto nel notebook come commento: «scarica il *model weight* e fai una *predict* dal test di CIFAR».
---
## Glossario dei termini introdotti
<table fit-page-width="true" header-row="true">
<tr>
<td>Termine</td>
<td>Definizione data nella lezione</td>
</tr>
<tr>
<td>**Dropout in inferenza**</td>
<td>Attivo solo durante l'addestramento: «viene cancellato quando facciamo l'inference». `TF-07 @ 00:02:30`</td>
</tr>
<tr>
<td>**`Conv2DTranspose`**</td>
<td>L'inverso della convoluzione: fa *upscaling*. È il layer del **decoder** di un autoencoder. `TF-07 @ 00:05:00`</td>
</tr>
<tr>
<td>**Encoder / decoder**</td>
<td>«L'encoder fa il downscaling e il decoder fa l'upscaling.» `TF-07 @ 00:06:30`</td>
</tr>
<tr>
<td>**`Bidirectional`**</td>
<td>Legge la sequenza nei due versi e concatena: raddoppia la dimensione d'uscita. `TF-07 @ 00:07:00`</td>
</tr>
<tr>
<td>**`Sequential().add(...)`**</td>
<td>Modo alternativo di costruire un modello, invece della lista di layer. `TF-07 @ 00:20:00`</td>
</tr>
<tr>
<td>**Attivazione come parametro**</td>
<td>`Dense(n, activation="softmax")` invece di un layer `Activation` separato. `TF-07 @ 00:21:00`</td>
</tr>
<tr>
<td>**`to_categorical`**</td>
<td>Trasforma etichette intere in one-hot; da lì `categorical_crossentropy` invece della sparse. `TF-07 @ 00:21:00`</td>
</tr>
<tr>
<td>**`validation_split`**** vs ****`validation_data`**</td>
<td>Il primo funziona su array e tensori; con un `tf.data.Dataset` **non si può usare** e lo split va fatto a mano. `TF-07 @ 00:24:00`, `01:11:00`</td>
</tr>
<tr>
<td>**API funzionale**</td>
<td>Ogni layer è una funzione applicata al tensore precedente; `tf.keras.Model(inputs, outputs)` chiude il grafo. `TF-07 @ 00:38:30`</td>
</tr>
<tr>
<td>**Average pooling**</td>
<td>Il pooling usato da LeNet-5, invece del max pooling. `TF-07 @ 00:40:00`</td>
</tr>
<tr>
<td>**Convoluzione \*pointwise**\*</td>
<td>`Conv2D(120, 1)`: kernel 1×1, combina i canali senza guardare i vicini spaziali. `TF-07 @ 00:41:30`</td>
</tr>
<tr>
<td>**`he_uniform`**</td>
<td>Inizializzazione pensata per la ReLU. `TF-07 @ 01:05:00`</td>
</tr>
<tr>
<td>**Aumento dei dati**</td>
<td>Luminosità, specchiatura e contrasto casuali, per moltiplicare gli esempi. `TF-07 @ 01:00:00`</td>
</tr>
<tr>
<td>**Warm-up**</td>
<td>Un primo addestramento breve prima di quello vero, per portare i nuovi strati in un regime ragionevole. `TF-07 @ 01:10:00`</td>
</tr>
<tr>
<td>**Callback**</td>
<td>«Un'azione che viene lanciata per ogni epoca.» `TF-07 @ 01:12:00`</td>
</tr>
<tr>
<td>**`ModelCheckpoint`**</td>
<td>Salva **tutto il modello**, non solo i pesi; il nome del file può contenere epoca e metriche di validazione. `TF-07 @ 01:13:00`</td>
</tr>
<tr>
<td>**`save_best_only=True`**</td>
<td>Salva solo quando la metrica sorvegliata migliora. `TF-07 @ 01:13:30`</td>
</tr>
<tr>
<td>**`prefetch`**** include il batch**</td>
<td>«La `prefetch` è già *on batch*, non ho più bisogno di mettere il `batch` qua.» `TF-07 @ 01:11:00`</td>
</tr>
<tr>
<td>**`LearningRateScheduler`**</td>
<td>Cambia il passo a scalini durante l'addestramento. Con un primo scalino troppo alto **distrugge** il modello: sezione 10</td>
</tr>
<tr>
<td>**Confidenza della predizione**</td>
<td>L'`argmax` sceglie comunque un massimo, anche se vale 0.1: la classe predetta va letta insieme alla sua probabilità. `TF-08 @ 00:01:30`</td>
</tr>
<tr>
<td>**Transfer learning**</td>
<td>Riusare una rete preaddestrata (InceptionV3) come base e aggiungere strati nuovi in cima. `TF-08 @ 00:22:30`</td>
</tr>
<tr>
<td>**`include_top=False`**</td>
<td>Scarta la testa di classificazione della rete preaddestrata e lascia l'estrattore di caratteristiche. `TF-08 @ 00:20:00`</td>
</tr>
<tr>
<td>**`preprocess_input`**</td>
<td>Ogni rete preaddestrata ha la sua normalizzazione: per InceptionV3 non è `/255`. `TF-08 @ 00:18:00`</td>
</tr>
<tr>
<td>**Congelare i layer**</td>
<td>`layer.trainable = False` sulla base: da 24.591.274 a 2.788.490 parametri addestrabili. `TF-08 @ 00:24:30`</td>
</tr>
<tr>
<td>**Learning rate per il fine-tuning**</td>
<td>`Adam(1e-5)`, cento volte meno del default, per non rovinare i pesi preaddestrati. `TF-08 @ 00:31:30`</td>
</tr>
<tr>
<td>**`stateful=True`**</td>
<td>L'LSTM conserva lo stato fra chiamate; obbliga a fissare il `batch_size` nel grafo. `TF-08 @ 00:50:00`</td>
</tr>
<tr>
<td>**`return_sequences=True`**</td>
<td>Un'uscita per ogni passo temporale, non solo per l'ultimo. `TF-08 @ 00:50:30`</td>
</tr>
<tr>
<td>**Modello di inferenza a batch 1**</td>
<td>Per generare testo serve un modello ricostruito con `batch_size=1` e i pesi ricaricati. `TF-08 @ 01:12:00`</td>
</tr>
<tr>
<td>**Campionamento stocastico**</td>
<td>`tf.random.categorical` invece di `argmax`: il carattere successivo si estrae dalla distribuzione. `TF-08 @ 01:12:30`</td>
</tr>
<tr>
<td>**Next-character prediction**</td>
<td>L'etichetta è l'input spostato di un carattere: «"sono Lu" → "ono Lui"». `TF-08 @ 00:48:30`</td>
</tr>
</table>
---
## Punti a bassa confidenza
**75 segmenti segnalati** su 944 (TF-07: 42 su 502, TF-08: 33 su 442), più **18 segmenti di boilerplate rimossi**. Elenco completo con i motivi in **`day-04-bassa-confidenza.md`**.
### Testo a schermo non leggibile `[illeggibile]`
Il materiale ufficiale ha **risolto otto dei nove** punti che la versione precedente di questo manuale segnalava, incluso l'unico `[?]` su un valore numerico — il «266», che in realtà è la sequenza 1024 → 512 → 256 → 128. Resta:
<table fit-page-width="true" header-row="true">
<tr>
<td>Dove</td>
<td>Punto</td>
<td>Perché resta aperto</td>
</tr>
<tr>
<td>`TF-07 @ 01:20:00`–`01:27:00`</td>
<td>Il pannello di **TensorBoard** aperto dal docente non è mai inquadrato in modo leggibile</td>
<td>I log (`./logs/cifar/`, `./logs/cifar2/`) non fanno parte del materiale distribuito: esistevano solo sulla macchina del docente</td>
</tr>
</table>
**Risolti dal notebook ufficiale:** le celle di preprocessing (`TF-07 @ 00:18:54`), l'avviso di Keras su `dense.py` (`TF-07 @ 00:24:17`), le valutazioni dei modelli uno e due (`TF-07 @ 00:35:26`), la fine di `lenet_5_model` (`TF-07 @ 00:42:34`), l'architettura CNN su CIFAR (`TF-07 @ 01:03:40`), la testa densa del transfer learning (`TF-08 @ 00:22:00`), il secondo tempo del fine-tuning (`TF-08 @ 00:26:00`), le celle del vocabolario (`TF-08 @ 00:45:32`), la funzione di generazione (`TF-08 @ 01:11:57`).
---
## Materiale ufficiale usato
<table fit-page-width="true" header-row="true">
<tr>
<td>File</td>
<td>Ruolo</td>
</tr>
<tr>
<td>`17-06-2025/KERAS-NN-should-be-reviewed.ipynb`</td>
<td>**Fonte** della sezione 2 (materiale della giornata 3, ripreso qui)</td>
</tr>
<tr>
<td>`19-06-2025/1.MNIST-MODEL-SELECTION.ipynb`</td>
<td>**Fonte** delle sezioni 3-7</td>
</tr>
<tr>
<td>`19-06-2025/2.callbacks-n-debug.ipynb`</td>
<td>**Fonte** delle sezioni 8-10</td>
</tr>
<tr>
<td>`19-06-2025/3.callbacks-n-pred.ipynb`</td>
<td>**Fonte** della sezione 11</td>
</tr>
<tr>
<td>`19-06-2025/4_CIFAR_FINETUNE_colab.ipynb`</td>
<td>**Fonte** delle sezioni 12-14</td>
</tr>
<tr>
<td>`19-06-2025/5_CharGen_LSTM_colab.ipynb`</td>
<td>**Fonte** delle sezioni 15-16</td>
</tr>
<tr>
<td>`19-06-2025/initial/estratto/*.ipynb`</td>
<td>Le versioni scheletro, per distinguere ciò che è stato scritto in aula</td>
</tr>
<tr>
<td>`TF-07.mp4`, `TF-08.mp4`</td>
<td>Fonte della **sequenza** e di ciò che non è nei notebook: le due interruzioni manuali, il pannello TensorBoard, l'assegnazione finale, il ragionamento su LeNet-5</td>
</tr>
</table>
Elenco completo delle divergenze: **`day-04-divergenze.md`**.
Verifica per esecuzione: **`VERIFICA-day-04.md`**.
## Notebook della lezione
I file originali del docente, sul tuo Mac in `Downloads/TensorFlow-MDA/Materiale Sito/estratti/`:
- `19-06-2025/19-06-2025/5_CharGen_LSTM_colab.ipynb`
