# 13 - Generazione di titoli a parole
> Fonte Notion: https://app.notion.com/p/3d612abc808d81efadc7dca35752bcb8 — ultima modifica 2026-09-09T23:31:38.309Z

> Giornata 5 del corso · video `TF-09` e `TF-10`
---
## 1. Chiusura della generazione a caratteri — `TF-09 @ 00:00:00`
Il docente riprende il notebook della giornata precedente, `5_CharGen_LSTM_colab.ipynb`, per chiudere un punto rimasto confuso: «scusatemi, perché ieri con Google Colab forse avevo un po' di confusione».
**L'obiettivo** (`TF-09 @ 00:01:00`): «dato un input, una sequenza di lettere, noi vogliamo generare tipo **100 lettere** dopo questa».
**Le tre trasformazioni sull'output**, spiegate una per una sul codice della giornata 4:
1. `TF-09 @ 00:01:30`: «quando facciamo la predizione del modello, abbiamo una dimensione **batch** e poi la **lunghezza della sequenza**… non abbiamo softmax ma comunque con *logit*».
2. `TF-09 @ 00:02:00`: «dobbiamo togliere il batch, allora abbiamo fatto lo **squeeze**».
3. `TF-09 @ 00:02:30`: «adesso è una matrice — la lunghezza della sequenza e poi la dimensione del vocabolario con quei logit — noi prendiamo **l'ultimo valore della sequenza**, ecco perché è il **meno 1**».
**Perché non ****`argmax`****.** `TF-09 @ 00:03:00`, ed è il punto concettuale:
> «Quando abbiamo fatto la classificazione noi abbiamo fatto un `argmax` per vedere l'indice… Per questo tipo di progetto, in cui vogliamo fare una predizione della prossima lettera, noi **invece di usare l'argmax usiamo una probabilità**.»
Con `argmax` il modello genererebbe sempre lo stesso testo dato lo stesso inizio; campionando dalla distribuzione (`tf.random.categorical`) il testo varia ed è più naturale.
> **Tenete a mente questo passaggio.** Il notebook di *questa* giornata, `HEADLINE-GEN`, farà l'opposto — userà `argmax` — e la sezione 6 mostra il risultato.
---
## 2. `HEADLINE-GEN`: dai caratteri alle parole — `TF-09 @ 00:14:00`
Nuovo notebook, «**Headline Generator using LSTM**». Il progetto è lo stesso della giornata 4 — generare testo — ma l'unità cambia: non più **caratteri**, ma **parole**.
`già nel materiale` — celle `[2]` e `[3]`:
```python
!unzip ny.zip
```
```python
# import
import tensorflow as tf
import pandas as pd
import numpy as np
import glob
import string
```
**I dati** sono i titoli del New York Times, in nove CSV dentro `ny/`: `ArticlesApril2017.csv`, `ArticlesApril2018.csv`, `ArticlesFeb2017.csv`, `ArticlesFeb2018.csv`, `ArticlesJan2017.csv`, `ArticlesJan2018.csv`, `ArticlesMarch2017.csv`, `ArticlesMarch2018.csv`, `ArticlesMay2017.csv`.
`scritta in aula` — celle `[5]`, `[6]`:
```python
all_articles = []
for fname in glob.glob("./ny/*.csv"):
    article = pd.read_csv(fname)
    all_articles.extend(list(article.headline.values))
```
```python
all_articles[:10]
```
Il dettaglio pratico che il docente segnala (`TF-09 @ 00:14:00`): «questo mi dà una sequenza di *map*, allora per Python dobbiamo trasformarla in una **lista**». Da qui `list(...)` e `extend`, la stessa scelta della giornata 4.
`scritta in aula` — celle `[8]`, `[10]`, la pulizia:
```python
filtered_articles = [title for title in all_articles if title != 'Unknown']
len(filtered_articles) == len(all_articles)
```
```python
def cleaning(text):
    text = "".join(p for p in text if p not in string.punctuation).lower()
    text = text.encode("utf-8").decode("ascii", "ignore")
    return text
corpus = list(map(lambda x: cleaning(x), filtered_articles))
corpus[:10]
```
Tre pulizie in tre righe: si buttano i titoli letteralmente scritti `Unknown`; si toglie la punteggiatura e si porta tutto in minuscolo; e l'ultima riga fa il giro `encode("utf-8")` → `decode("ascii", "ignore")` per **eliminare i caratteri non ASCII** — virgolette tipografiche, trattini lunghi, accenti.
Il confronto `len(filtered_articles) == len(all_articles)` restituisce `False`: qualche titolo `Unknown` c'era.
---
## 3. Il tokenizer, e perché dipende dal dataset — `TF-09 @ 00:14:30`
`scritta in aula` — cella `[12]`:
```python
token_ex = tf.keras.preprocessing.text.Tokenizer()
token_ex.fit_on_texts(corpus)
token_ex.index_word
```
**Che cos'è un token, nelle parole del docente** (`TF-09 @ 00:15:00`): «il tokenizer trasforma le parole alla loro base. Ad esempio *meeting*: la base è *meet*. Quello che fa la tokenizzazione — perché *meeting* fa parte di *meet*, allora il token di questo è *meet*».
«Come facciamo per addestrare un modello, possiamo fare un `fit_on_texts`, prende il corpus… l'indice delle parole. Lui trasforma in token così: questo è il set di token e dà già una mappa, come quello che abbiamo fatto per il carattere — quello del carattere comunque lo abbiamo fatto **a mano**.»
**Il punto che vale la lezione.** `TF-09 @ 00:16:30`:
> «Il token cambia, dipende dal dataset. Ricordate questo perché, ad esempio, se siete abituati a usare ChatGPT, **non potete usare lo stesso token** che sta usando — non lo so — Llama o Anthropic, perché dipende dai dataset che loro stanno usando, e durante l'addestramento crea il token.
>
> Questo è importante, perché quando creiamo un **embedding** dobbiamo prendere il vero token dei dati su cui il modello era addestrato.»
È l'avvertimento operativo più importante della sezione: tokenizer e modello sono inseparabili.
<callout icon="➕">
	**Nota aggiunta:** la descrizione che il docente dà del tokenizer — *meeting* → *meet* — è quella di uno **stemmer** o di un tokenizzatore a sotto-parole. Il `keras.preprocessing.text.Tokenizer` che usa qui non fa niente del genere: divide sugli spazi, toglie la punteggiatura e assegna un indice intero a ogni parola **intera**, ordinata per frequenza. *meeting* e *meet* restano due voci distinte del vocabolario. Il concetto che spiega è giusto e importante; lo strumento in questa cella è più semplice di così. Il docente non fa la distinzione.
</callout>
---
## 4. Le sequenze progressive — `TF-09 @ 00:17:00`
«Adesso creiamo l'*input sequence* come quello che abbiamo fatto per CharGen.»
`scritta in aula` — cella `[14]`:
```python
def create_sequences_of_token(corpus, tokenizer):
    tokenizer.fit_on_texts(corpus)
    total_words = len(tokenizer.word_index) + 1
    inputs_sequences = []
    for headline in corpus:
        token_list = tokenizer.texts_to_sequences([headline])[0]
        for i in range(1, len(token_list)):
            n_g = token_list[:i+1]
            inputs_sequences.append(n_g)
    return inputs_sequences, total_words

tokenizer = tf.keras.preprocessing.text.Tokenizer()
inputs_sequences, total_words = create_sequences_of_token(
    corpus, tokenizer
)
print(total_words)
```
```javascript
11265
```
**Il ****`+1`**** spiegato** (`TF-09 @ 00:18:00`): «il *total words* è il numero di vocaboli… la lunghezza del `tokenizer.word_index`. Ovviamente abbiamo anche qua un indice specializzato, perché se noi andiamo all'inizio di questo vedete che **inizia dall'1**». L'indice 0 è riservato al padding, quindi la dimensione del vocabolario è `len(word_index) + 1` = **11.265**.
**La costruzione delle sequenze.** Per ogni titolo si generano tutti i prefissi di lunghezza crescente: da `[w1, w2]` fino a `[w1, ..., wn]`. Ogni prefisso è un esempio in cui l'ultimo token è l'etichetta e i precedenti sono l'input — la stessa idea del *next-character prediction* della giornata 4, applicata alle parole. Il nome `n_g` sta per *n-gram*.
`scritta in aula` — cella `[17]`:
```python
def create_input_nd_label(inputs_sequences, total_words):
    max_seq_len = max([len(x) for x in inputs_sequences])
    x_sequences = np.array(
        tf.keras.preprocessing.sequence.pad_sequences(
            inputs_sequences,
            maxlen=max_seq_len
        )
    )
    x, y = x_sequences[:, :-1], x_sequences[:, -1]
    label = tf.keras.utils.to_categorical(y, num_classes=total_words)
    return x, label, max_seq_len

predictors, label, max_sequence_len = create_input_nd_label(
    inputs_sequences, total_words
)
print(predictors.shape, max_sequence_len)
```
```javascript
(51770, 23) 24
```
(`nd` in `create_input_nd_label` sta per «and»: è un refuso del docente.)
`pad_sequences` porta tutte le sequenze a 24 token riempiendo di zeri **a sinistra**; poi la separazione è pulita: le prime 23 colonne sono l'input, l'ultima è l'etichetta, che viene resa **one-hot** su 11.265 classi.
> **Punto risolto dal materiale ufficiale.** Queste due celle non sono mai inquadrate complete: erano **\[illeggibile\]** e la versione precedente di questo manuale le dichiarava solo per sommi capi.
---
## 5. Il modello, e i due gigabyte di etichette — `TF-09 @ 00:30:00`
`scritta in aula` — cella `[19]`:
```python
EMB_LENGTH = predictors.shape[-1]

def create_model(total_words):
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Embedding(
        total_words,
        10,
        input_length=EMB_LENGTH
    ))
    model.add(tf.keras.layers.LSTM(100))
    model.add(tf.keras.layers.Dense(total_words, activation='softmax'))
    return model

model = create_model(total_words)
model.summary()
```
```javascript
keras/src/layers/core/embedding.py:97: UserWarning: Argument `input_length` is deprecated.
Just remove it.

Model: "sequential_1"
│ embedding_1 (Embedding)         │ ?                      │   0 (unbuilt) │
│ lstm (LSTM)                     │ ?                      │   0 (unbuilt) │
│ dense (Dense)                   │ ?                      │   0 (unbuilt) │
 Total params: 0 (0.00 B)
```
> **È lo stesso ****`summary()`**** a zero della giornata 3.** `input_length` è ignorato in Keras 3, il modello non conosce la forma dell'input e resta non costruito. Il docente non lo commenta, come non lo aveva commentato allora.
L'architettura è minima: un embedding a **10 dimensioni** per parola — contro le 256 della giornata 3 — un solo LSTM da 100 unità, e un `Dense` a **11.265 uscite** con softmax. È quest'ultimo a costare: 100 × 11.265 + 11.265 ≈ **1,14 milioni** di parametri solo per lo strato finale.
`scritta in aula` — celle `[21]`, `[23]`:
```python
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)
```
```python
history = model.fit(
    predictors,
    label,
    epochs=5,
    validation_split=0.2
)
```
```javascript
2025-06-20 16:39:18: W cpu_allocator_impl.cc:83] Allocation of 1866204960 exceeds 10%
of free system memory.
Epoch 1/5
1295/1295 ━━━━━━━━━━ 66s 51ms/step - accuracy: 0.0484 - loss: 7.3714 - val_accuracy: 0.0494 - val_loss: 7.8861
Epoch 3/5
1295/1295 ━━━━━━━━━━ 66s 51ms/step - accuracy: 0.0578 - loss: 7.1340 - val_accuracy: 0.0621 - val_loss: 7.9486
Epoch 4/5
1295/1295 ━━━━━━━━━━ 69s 53ms/step - accuracy: 0.0679 - loss: 6.8947 - val_accuracy: 0.0630 - val_loss: 8.0412
Epoch 5/5
1295/1295 ━━━━━━━━━━ 70s 54ms/step - accuracy: 0.0705 - loss: 6.6725 - val_accuracy: 0.0634 - val_loss: 8.1345
```
<callout icon="➕">
	**Due cose da leggere in questo output**
	**1,87 GB per le sole etichette.** L'avviso `Allocation of 1866204960 exceeds 10% of free system memory` viene da `to_categorical`: 51.770 esempi × 11.265 classi × 4 byte = **2,3 GB** di matrice one-hot densa, quasi tutta zeri. Il docente lo nota di sfuggita a `TF-09 @ 00:46:30` («adesso ad esempio c'è un problema della memoria») senza collegarlo alla causa.
	La `SparseCategoricalCrossentropy` della giornata 3 avrebbe evitato interamente il problema: tiene le etichette come interi e non le espande mai. Questa osservazione è mia.
	**L'overfitting comincia dalla prima epoca.** La loss di addestramento scende (`7.37 → 6.67`), quella di validazione **sale** (`7.89 → 8.13`), e l'accuratezza di validazione si ferma al **6.3%**. Su 11.265 classi il caso darebbe 0.009%, quindi il modello ha imparato qualcosa — ma sta già memorizzando.
</callout>
---
## 6. Generare un titolo — `TF-09 @ 00:44:00`
`scritta in aula` — cella `[25]`:
```python
def generate_headline(model, text, tokenizer, num_words=10):
    for _ in range(num_words):
        token_list = tokenizer.texts_to_sequences([text])[0]
        token_list = tf.keras.preprocessing.sequence.pad_sequences([token_list], maxlen=max_sequence_len)
        predicted = model.predict(token_list)
        y_pred = np.argmax(predicted, axis=1)
        output_words = ""
        for w, index in tokenizer.word_index.items():
            if index == y_pred:
                output_words = w
                break
        text += " " + output_words
    return text
```
Il docente la prova dal vivo (`TF-09 @ 00:44:00`): «se io faccio `generate_headline`, il model, il text… il headline è questo arancione, forse vediamo *The Republican*… e poi il tokenizer… e possiamo prendere il default da **10 parole**».
**Un errore, e la correzione.** `TF-09 @ 00:45:00`–`00:45:30`: «qual è il problema? Perché il token è lista… perché un array? Ma questo dovrebbe essere… **ah, questo è l'axis 1**, perché… sì. Ok, ci siamo». È l'`axis=1` dell'`argmax`, la stessa cosa della giornata 4.
`scritta in aula` — cella `[26]`, e il risultato completo:
```python
generate_headline(
    model,
    "The Republicans",
    tokenizer
)
```
```javascript
'The Republicans of the new york of the times of the new'
```
> «Allora, questo è ovviamente **molto male**, ma comunque io vorrei che potete generare una headline che ha senso.» (`TF-09 @ 00:45:30`)
**Perché è andata così** (`TF-09 @ 00:46:30`): «qua sto usando la CPU, allora ho usato solo **5 epoche**… adesso ad esempio c'è un problema della memoria, ma su Google Colab con GPU dovrebbe andare bene».
<callout icon="➕">
	**Le epoche non sono l'unica causa**
	Il testo generato non è casuale: è **ciclico**. *of the new york of the times of the new*. E il motivo sta in una riga della funzione, non nel numero di epoche.
	`y_pred = np.argmax(predicted, axis=1)` prende sempre **la parola più probabile**. È esattamente ciò che il docente aveva spiegato di non fare, dodici minuti prima, alla sezione 1: «invece di usare l'argmax usiamo una probabilità». Con l'`argmax` il modello è deterministico, e appena ricade su uno stato già visto — *the* → *new* → *york* → *of* → *the* — non ne esce più.
	Il notebook di ieri campionava con `tf.random.categorical`; questo prende il massimo. Il confronto fra i due output è il modo più diretto per vedere cosa cambia.
	Questa lettura è mia: il docente attribuisce il risultato alle 5 epoche e alla CPU, e non torna sul punto dell'`argmax`.
</callout>
E il suggerimento per chi vuole proseguire: «se avete fatto un *fine-tuning*, dopo questo potete usare… `load_model` from checkpoint. A partire dal checkpoint devi fare un `load`». Resta scritto come esercizio, `scritta in aula` — cella `[27]`:
```python
# exrcise: load model from checkpoints
```
> **Punto risolto dal materiale ufficiale.** La funzione e il titolo generato erano **\[illeggibile\]**: la versione precedente di questo manuale riportava solo il frammento «of the new, of the times, of the new», sentito a voce.
## Notebook della lezione
I file originali del docente, sul tuo Mac in `Downloads/TensorFlow-MDA/Materiale Sito/estratti/`:
- `20-06-2025/20-06-2025/HEADLINE-GEN-completed.ipynb`
