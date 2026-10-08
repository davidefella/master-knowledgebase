# 14 - Serie temporali con LSTM
> Fonte Notion: https://app.notion.com/p/3d612abc808d81d882ddf2e0ce932091 — ultima modifica 2026-09-09T23:31:40.439Z

> Giornata 5 del corso · video `TF-09` e `TF-10`
---
## 7. `BTC-EUR-FORECAST`: la serie temporale — `TF-09 @ 00:47:00`
«Adesso apriamo questo **Bitcoin Euro Forecasting**. Una delle cose che vediamo è usare una *forecast* di una **time series**.»
`già nel materiale` — l'intestazione dichiara che il notebook usa dati storici del Bitcoin da giugno 2024 a giugno 2025 per costruire e valutare diversi modelli di previsione basati su LSTM.
**Un avvertimento che il docente dà subito.** `TF-09 @ 00:47:30`:
> «Quello che vediamo sono basi, come facciamo per creare un modello per fare un forecast. Ma ovviamente **non potete usare questo** se volete fare trading o qualcosa: dovete studiare un po' e migliorare un po' il modello.»
`già nel materiale` — cella `[3]`:
```python
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
```
`scritta in aula` — celle `[5]`, `[6]`:
```python
btc_df = pd.read_csv("./BTC_EUR-Kraken-Historical-Data.csv")
btc_df.head(2)
```
```python
btc_df['Date'] = pd.to_datetime(btc_df['Date'])
btc_df = btc_df.sort_values('Date')
btc_df['Price'] = btc_df['Price'].str.replace(",", "").astype(np.float32)
btc_df.head(2)
```
**I dati.** `TF-09 @ 00:48:00`: «questi dati, io non ricordo dove — forse questo **Kraken**, il sito da cui ho preso questi dati. Più o meno abbiamo il *date*, *price*, il prezzo all'*open*, l'*high price*, *low*, il *volume* e il *change*».
Tre passaggi obbligati che si vedono in due righe: le date vanno **convertite** e **ordinate** (il CSV di Kraken è in ordine inverso), e il prezzo arriva come **stringa** con il separatore delle migliaia — `"62,406.9"` — che va tolto prima di convertire in numero.
`scritta in aula` — cella `[7]`:
```python
# normalization

btc_price = btc_df['Price'].values.reshape(-1, 1)
scaler = MinMaxScaler()
btc_price_scaled = scaler.fit_transform(btc_price)
print(btc_price[:2], btc_price_scaled[:2])
```
```javascript
[[62406.9]
 [62452.2]] [[0.25646764]
 [0.25731832]]
```
Il `MinMaxScaler` porta i prezzi in `[0, 1]`. Serve perché una rete con attivazione `tanh` non può lavorare su numeri dell'ordine di 60.000. Lo `scaler` va **conservato**: alla fine servirà per riportare le predizioni in euro.
`scritta in aula` — cella `[8]`, la costruzione degli esempi:
```python
# inputs
X, Y = [], []
for i in range(1, len(btc_price_scaled)):
    X.append(btc_price_scaled[i -1:i])
    Y.append(btc_price_scaled[i])
X, Y = np.array(X), np.array(Y)
```
> **Qui è definito tutto il problema, in quattro righe.** L'input di ogni esempio è **un solo giorno** — il prezzo di ieri — e l'etichetta è il prezzo di oggi. Non una finestra di 30 giorni, non le altre colonne del CSV: un numero solo.
>
> È l'**ipotesi markoviana** che il docente dichiarerà esplicitamente nella sezione 8, e spiega perché l'`input_shape` del modello sarà `(1, 1)`.
`scritta in aula` — celle `[9]`, `[10]`:
```python
# test data
split_index = len(X) - 30
X_train, Y_train = X[:split_index], Y[:split_index]
X_test, Y_test = X[split_index:], Y[split_index:]

train_dataset = tf.data.Dataset.from_tensor_slices((X_train, Y_train)).repeat().batch(6).prefetch(
    tf.data.AUTOTUNE
)
test_dataset = tf.data.Dataset.from_tensor_slices((X_test, Y_test)).batch(1).prefetch(tf.data.AUTOTUNE)
```
```python
plt.figure(figsize=(12, 6))
plt.plot(btc_df['Date'][:split_index], btc_price[:split_index], color='blue')
plt.show()
```
Lo split è **temporale, non casuale**: gli ultimi 30 giorni sono il test. Su una serie storica è l'unico modo corretto — mescolare significherebbe addestrare sul futuro.
Il `.repeat()` senza argomenti rende il dataset infinito, e sarà `steps_per_epoch` a decidere dove finisce un'epoca: la stessa costruzione della giornata 4.
**Il grafico.** `TF-09 @ 01:05:00`–`01:06:00`: «potete vedere il grafico… questo è il prezzo del Bitcoin dal 2024 fino alla data, fino a maggio».
> **Punto risolto dal materiale ufficiale.** Le celle del `MinMaxScaler` e dello split temporale erano **\[illeggibile\]**.
---
## 8. I tre modelli LSTM, e la previsione ricorsiva — `TF-09 @ 01:06:00` → `TF-10 @ 00:00:00`
> Questa sezione **attraversa il taglio fra i due file**.
**Il modello di base.** `scritta in aula` — cella `[12]`, `TF-09 @ 01:06:30`–`01:07:30`:
```python
def create_model(units=10):
    model = tf.keras.models.Sequential([
        tf.keras.layers.LSTM(units, activation='tanh', input_shape=(1,1)),
        tf.keras.layers.Dense(1)
    ])
    return model
```
Il docente costruisce e commenta: «creiamo un modello che era il `Sequential`… `keras.layers.LSTM`, allora quanti *units* mettiamo? Non lo so, diciamo **10** — no, facciamo così, `units`, così possiamo prendere cose un po' dinamiche». Sull'attivazione: «l'activation lo cambiamo, usiamo la **tangente iperbolica**». Sull'input: **`(1, 1)`**, «perché la lunghezza del \[passo\] è 1».
E il motivo di quella forma, dato più avanti (`TF-09 @ 01:22:30`): «perché noi abbiamo solo il **prezzo** e poi il **tempo giornaliero**, perciò abbiamo uno per uno».
**Più modelli a confronto.** `TF-09 @ 01:08:00`: «quello che voglio è che creiamo **più di un modello** e facciamo confronti».
`scritta in aula` — celle `[13]`, `[14]`:
```python
def create_deep_model(units=32):
    model = tf.keras.models.Sequential([
        tf.keras.layers.LSTM(units, activation='tanh', input_shape=(1,1), return_sequences=True),
        tf.keras.layers.LSTM(int(units/2), activation='tanh'),
        tf.keras.layers.Dense(1)
    ])
    return model
```
```python
def create_very_deep_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.LSTM(64, activation='tanh', input_shape=(1,1), return_sequences=True),
        tf.keras.layers.LSTM(32, activation='tanh', return_sequences=True),
        tf.keras.layers.LSTM(16, activation='tanh'),
        tf.keras.layers.Dense(1)
    ])
    return model
```
Il punto tecnico: **`return_sequences=True`** su ogni LSTM tranne l'ultimo. «Facciamo anche che questo `return_sequences` lo mettiamo su» — è necessario per impilare strati ricorrenti: ciascuno deve restituire l'intera sequenza al successivo, e solo l'ultimo restituisce il singolo stato finale che va al `Dense`.
> **Punto risolto dal materiale ufficiale.** Il numero di unità del secondo LSTM era pronunciato «int» a `TF-09 @ 01:09:00`, in un segmento a bassa confidenza marcato `[?]`. Era letteralmente `int` — `int(units/2)`, cioè **16**. Le celle non erano mai inquadrate complete: erano **\[illeggibile\]**.
`scritta in aula` — cella `[16]`, le callback e la funzione di addestramento:
```python
def get_callbacks(name):
    return [
        tf.keras.callbacks.ModelCheckpoint(f"./checkpoints/{name}/model.keras", save_best_only=True),
        tf.keras.callbacks.TensorBoard(f"./logs/{name}/"),
        tf.keras.callbacks.EarlyStopping(
            patience=10,
            restore_best_weights=True
        )
    ]

def train_model(model, name, steps_per_epoch=50, epochs=100):
    model.compile(
        optimizer='adam',
        loss='mse',
        metrics=['mse']
    )
    history = model.fit(
        train_dataset,
        epochs=epochs,
        steps_per_epoch=steps_per_epoch,
        callbacks=get_callbacks(name)
    )
    return model, history
```
È il riassunto della giornata 4 in una funzione: checkpoint del modello migliore, TensorBoard, ed `EarlyStopping` con `restore_best_weights` — proprio quello che il docente aveva chiesto come esercizio a fine giornata 4.
<callout icon="➕">
	**Le due callback non fanno niente, e il notebook lo dice**
	`train_model` non passa **nessun ****`validation_data`**. `EarlyStopping` e `ModelCheckpoint(save_best_only=True)` sorvegliano di default `val_loss`, che non esiste. Gli output salvati contengono i due avvisi, uno per ciascuna:
	```javascript
keras/src/callbacks/model_checkpoint.py:302: UserWarning: Can save best model only
with val_loss available, skipping.
keras/src/callbacks/early_stopping.py:153: UserWarning: Early stopping conditioned on
metric `val_loss` which is not available.
	```
	Le due conseguenze non sono uguali:
	- **`EarlyStopping`**** non ferma niente.** Senza metrica non ha nulla da sorvegliare, e tutti e tre gli addestramenti arrivano a 100 epoche. Il `restore_best_weights` non ripristina nulla.
	- **`ModelCheckpoint`**** salva, ma non il migliore.** Quando la metrica manca, Keras avvisa e **ricade su ****`save_best_only=False`**: salva a ogni epoca. Il percorso è un nome fisso, `model.keras`, quindi il file viene sovrascritto cento volte e resta il modello **dell'ultima epoca**.
	Il docente non legge gli avvisi. Basterebbe `validation_data=test_dataset`, oppure `monitor='loss'` in entrambe le callback. Questa osservazione è mia, ed è verificata per esecuzione e sul sorgente di Keras.
</callout>
`scritta in aula` — celle `[18]`, `[19]`, `[20]`, i tre addestramenti:
```python
lstm_base, _ = train_model(
    create_model(),
    name="base_model"
)
```
```python
deep_lstm_model, _ = train_model(
    create_deep_model(),
    name="deep_lstm"
)
```
```python
very_deep_lstm_model, _ = train_model(
    create_very_deep_model(),
    name="very_deep_lstm"
)
```
**I risultati, tutti e tre alla centesima epoca:**
<table header-row="true">
<tr>
<td>Modello</td>
<td>Architettura</td>
<td>Loss finale (MSE)</td>
</tr>
<tr>
<td>`lstm_base`</td>
<td>LSTM(10)</td>
<td>**0.0016**</td>
</tr>
<tr>
<td>`deep_lstm_model`</td>
<td>LSTM(32) → LSTM(16)</td>
<td>0.0028</td>
</tr>
<tr>
<td>`very_deep_lstm_model`</td>
<td>LSTM(64) → LSTM(32) → LSTM(16)</td>
<td>0.0035</td>
</tr>
</table>
> **Il modello più semplice vince, e il più profondo perde.** È lo stesso esperimento di selezione della giornata 4 e dà il risultato opposto: là aggiungere strati aiutava, qui peggiora di un fattore due.
>
> Il motivo è nella sezione 7: l'input è **un solo numero**. Non c'è nessuna struttura temporale da estrarre, quindi la capacità in più non ha niente da imparare e serve solo a rendere l'ottimizzazione più difficile. Il docente non trae la conclusione — la tabella non viene mai messa insieme a lezione — ma i tre numeri sono nel notebook distribuito.
**La previsione ricorsiva a 30 giorni.** `scritta in aula` — cella `[22]`, `TF-10 @ 00:00:00`:
```python
def forecast_future(model, last_input, steps=30):
    input_seq = last_input.reshape(1, 1, 1)
    preds = []
    for _ in range(steps):
        pred = model.predict(input_seq, verbose=0)
        preds.append(pred[0])
        input_seq = np.array(pred).reshape(1, 1, 1)
    return np.array
```
Il docente spiega ogni riga: «qua andiamo a fare un forecast dei **30 giorni**, ma potete anche fare una singola giornata se volete… non facciamo il `verbose`, così non vediamo questa cosa quando facciamo il predict… il prezzo, adesso basta fare un `append` di questa predizione — facciamo `0` perché è un batch. E poi l'*input sequence*, dobbiamo aggiornare l'input sequence adesso… ma siccome questo diventa solo un singolo elemento, allora dobbiamo fare anche un **reshape**».
**L'assunzione, dichiarata.** `TF-10 @ 00:01:00`:
> «Perché noi diciamo che questo è più o meno come **markoviano**, che dipende solo dal giorno precedente.»
È un'ipotesi forte e il docente la enuncia: la previsione del giorno *n+1* usa solo la previsione del giorno *n*, non la storia completa. Gli errori si accumulano.
> **`return np.array`**** — la funzione non restituisce le previsioni**
>
> L'ultima riga è `return np.array`, non `return np.array(preds)`. La funzione restituisce **il costruttore di NumPy**, non i trenta prezzi che ha appena calcolato.
>
> È un refuso vero, presente nel notebook distribuito, e passa inosservato per una ragione precisa: **`forecast_future`**** non viene mai chiamata**. Il confronto della cella `[23]` usa `model.predict(X_test)` diretto, che non è affatto una previsione ricorsiva — è una predizione a un passo con i **prezzi veri** in ingresso, uno per volta.
>
> Quindi la previsione ricorsiva a 30 giorni, che è il tema dichiarato di questa sezione e il motivo per cui il docente parla di ipotesi markoviana, **non viene mai eseguita**: esiste solo come funzione scritta e mai invocata. Vedi `day-05-divergenze.md` §3.
`scritta in aula` — celle `[23]`, `[24]`, `[25]`, il confronto finale:
```python
pred_lstm = lstm_base.predict(X_test, verbose=0)
pred_deep = deep_lstm_model.predict(X_test, verbose=0)
pred_very_deep = very_deep_lstm_model.predict(X_test, verbose=0)
```
```python
real_price = scaler.inverse_transform(Y_test)
pred_lstm_unscaled = scaler.inverse_transform(pred_lstm)
pred_deep_unscaled = scaler.inverse_transform(pred_deep)
pred_very_deep_unscalled = scaler.inverse_transform(pred_very_deep)
```
```python
days = list(range(len(real_price)))

plt.figure(figsize=(14, 7))
plt.plot(days, real_price, label="real price", linewidth=2)
plt.plot(days, pred_lstm_unscaled, label="LSTM Base", linewidth=2)
plt.plot(days, pred_deep_unscaled, label="DEEP", linewidth=2)
plt.plot(days, pred_very_deep, label="VERY DEEP", linewidth=2)

plt.xlabel("Days")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()
```
`inverse_transform` riporta le predizioni da `[0, 1]` a euro: è il motivo per cui lo `scaler` andava conservato.
> **L'ultima ****`plt.plot`**** usa ****`pred_very_deep`****, non ****`pred_very_deep_unscalled`****.** La curva «VERY DEEP» viene disegnata con i valori **normalizzati**, cioè numeri fra 0 e 1, su un grafico il cui asse va da circa 55.000 a 100.000 euro. Nel grafico appare come una **riga piatta a zero** in fondo.
>
> Il docente lo intuisce senza identificarlo (`TF-10 @ 00:02:00`): «sicuramente questo… avrà una data molto strana». E poi lascia perdere (`00:03:00`): «questo è il *deep LSTM model*, la predizione, però forse possiamo lasciare per voi, se volete prendere questo».
>
> È l'ultimo dei quattro refusi di questo notebook, ed è quello con l'effetto più visibile: il modello che il grafico fa sembrare inutile è semplicemente disegnato sulla scala sbagliata.
## Notebook della lezione
I file originali del docente, sul tuo Mac in `Downloads/TensorFlow-MDA/Materiale Sito/estratti/`:
- `20-06-2025/20-06-2025/BTC-EUR-FORECAST-completed.ipynb`
