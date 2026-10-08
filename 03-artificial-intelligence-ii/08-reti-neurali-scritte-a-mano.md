# 08 - Reti neurali scritte a mano
> Fonte Notion: https://app.notion.com/p/3d612abc808d81dbbe81d05bef4b06ea — ultima modifica 2026-09-09T23:31:24.428Z

> Giornata 3 del corso · video `TF-05` e `TF-06`
---
## 1. Il materiale della giornata — `TF-05 @ 00:00:00`
«Nella cartella `materials` ci sono alcuni notebook, e poi c'è questa cartella dei dati dove c'è CIFAR — un'immagine —, Titanic e un CSV.»
La struttura visibile nell'Explorer:
```javascript
17-06-2025/
  materials/
    DATASET.ipynb   KERAS-NN.ipynb   LOSS-OPTIM.ipynb
    LR-TF.ipynb     NN-TF.ipynb      SENTIMENT-KERAS.ipynb
    data/cifar/     data/titanic/
    uploadme/
  venv/
  materials.zip
```
Il docente ricrea l'ambiente come nelle giornate precedenti (`virtualenv`, `source`, `pip install jupyter`, TensorFlow CPU) e ricorda il consiglio a chi segue da Colab: «se seguite da Google Colab, cambiate il runtime e usate CPU» — precisando poi, per la rete neurale, «potete scegliere il runtime GPU» (`TF-05 @ 00:09:30`).
Un dettaglio pratico che ripete: se il virtualenv non compare nell'elenco dei kernel, `F1` → **Python: Select Interpreter** → scegliere `venv/bin/python`.
Nel corso della giornata installerà a mano anche le due dipendenze che mancano (`TF-05 @ 00:55:30`): «basta aprire un nuovo terminale, `source venv/bin/activate`, `pip install pandas`… `pip install scikit-learn`».
---
## 2. `LR-TF`: guardare la regressione, e perché il seed conta — `TF-05 @ 00:04:00`
`LR-TF.ipynb` è **l'unico notebook della giornata distribuito già completo**: la versione in `initial/` e quella finale sono identiche cella per cella. Il docente non lo scrive, lo commenta.
Ed è la **soluzione dell'esercizio assegnato a fine giornata 2**: «vi chiedo se potete fare solo un plot di questo dataset rispetto alla funzione lineare che abbiamo generato» (`TF-04 @ 01:11:00`). Le prime dieci celle sono la regressione della giornata 2 senza una virgola di differenza; le ultime due sono la risposta.
**Cosa è cambiato**, nelle sue parole: «quello che ho aggiunto su questo notebook è l'ultima parte, per vedere la curva della predizione».
**Il seed.** `TF-05 @ 00:04:00`: «ricordate che era molto difficile da addestrare, perché avevamo… i dati non hanno una distribuzione \[tale che\] 100 epoche siano abbastanza per addestrarlo. Allora ho provato a cercare quale sarebbe il **seed migliore**: ho provato con **65**, ma comunque potete provare altri seed per vedere se funziona per voi, perché questo dipende dal random, dai valori che abbiamo generato».
`già nel materiale` — cella `[1]`:
```python
tf.random.set_seed(65)
size = 400
```
> Nella giornata 2 la stessa riga era **commentata** (`# tf.random.set_seed(12)`), ed è la ragione per cui l'addestramento non convergeva a dovere davanti alla classe. Qui il seed è attivo e vale 65. È la chiusura, mai dichiarata a voce, dei dieci minuti di debug irrisolti di `TF-04 @ 01:01:30`–`01:11:00`.
**La visualizzazione.** `già nel materiale` — cella `[11]`, `TF-05 @ 00:07:58`:
```python
plt.figure(figsize=(12,5))
ax1 = plt.subplot(121)
ax1.scatter(X[:,0], Y[:,0], alpha=0.5, label="Data")
ax1.plot(X[:,0], weight[0]*X[:,0] + bias[0], "-r", label="Model")
ax1.set_title("Feature 1 vs Output")
ax1.legend()

ax2 = plt.subplot(122)
ax2.scatter(X[:,1], Y[:,0], alpha=0.5, label="Data")
ax2.plot(X[:,1], weight[1]*X[:,1] + bias[0], "-r", label="Model")
ax2.set_title("Feature 2 vs Output")
ax2.legend()

plt.tight_layout()
plt.show()
```
**Diagramma.** Due pannelli affiancati. A sinistra «Feature 1 vs Output»: nuvola di punti con una retta rossa a **pendenza positiva** (il coefficiente vero è `+1.0`). A destra «Feature 2 vs Output»: retta a **pendenza negativa** (coefficiente `−2.0`).
Il commento del docente è onesto: «vedete che il modello è un po' male, ma dobbiamo avere più o meno qualcosa per generalizzare… nella seconda dimensione mi sa che ci siamo più o meno». E indica cosa si può regolare: «questo tipo di cosa lo facciamo più o meno a scelta del learning rate, oppure anche del numero di batch, e dipende anche dall'inizializzazione del weight: qua ad esempio diciamo `random_normal`, ma potete usare un'altra funzione per inizializzare».
---
## 3. `NN-TF`: il problema dei due anelli — `TF-05 @ 00:09:00`
Nuovo notebook, intitolato «**Binary Classification using TensorFlow**». Il markdown di testa è preesistente; **tutto il codice è scritto in aula**.
**Il dataset, costruito apposta.** `TF-05 @ 00:10:00`: «il problema è una classificazione, ma lo chiamiamo anche **binary classification**, quella vero o falso. L'idea è: creiamo un tipo di dati come un **anello**, e quello interno lo mettiamo i numeri positivi… e quello esterno all'anello i numeri negativi».
`scritta in aula` — cella `[2]`:
```python
# Number of the positive/negative samples
n_positive, n_negative = 2000, 2000

# Generating the positive samples
r_p = 5.0 + tf.random.truncated_normal([n_positive,1], 0.0, 1.0)
theta_p = tf.random.uniform([n_positive,1], 0.0, 2*np.pi)
Xp = tf.concat([r_p * tf.cos(theta_p), r_p * tf.sin(theta_p)], axis=1)
Yp = tf.ones_like(r_p)

# Generating the negative samples
r_n = 8.0 + tf.random.truncated_normal([n_negative,1], 0.0, 1.0)
theta_n = tf.random.uniform([n_negative,1], 0.0, 2*np.pi)
Xn = tf.concat([r_n * tf.cos(theta_n), r_n * tf.sin(theta_n)], axis=1)
Yn = tf.zeros_like(r_n)

# Combine all samples
X = tf.concat([Xp, Xn], axis=0)
Y = tf.concat([Yp, Yn], axis=0)
```
La costruzione, spiegata pezzo per pezzo mentre la scrive:
- stesso numero di campioni positivi e negativi, **2000** ciascuno;
- i positivi su un anello di **raggio 5**, i negativi su uno di **raggio 8**;
- un rumore `truncated_normal` sul raggio, «perché se usiamo solo \[un raggio\] fisso, allora avremo proprio un cerchio» — cioè una circonferenza sottile invece di una corona;
- un angolo `theta` estratto uniformemente **da 0 a 2π**: «questa è infatti una random uniforme da 0 a 2π, allora tutti i cerchi tra la circonferenza»;
- il passaggio da polari a cartesiane con `r·cos(θ)` e `r·sin(θ)`, uniti con `concat` sull'asse 1 — la stessa `tf.concat` della giornata 2, qui usata per affiancare due colonne;
- le etichette con `ones_like` e `zeros_like`, che prendono la forma da `r_p` e `r_n` senza doverla riscrivere;
- infine `concat` sull'asse 0 per impilare i 4000 punti.
**La visualizzazione.** `scritta in aula` — cella `[4]`, `TF-05 @ 00:13:00`:
```python
plt.figure(figsize=(5,5))
plt.scatter(Xp[:,0], Xp[:, 1], c="r", label="Positive")
plt.scatter(Xn[:,0], Xn[:, 1], c="b", label="Negative")
plt.legend()
plt.show()
```
**Diagramma.** Due nuvole di punti concentriche: quelle rosse (positive) formano una corona interna di raggio \~5, quelle blu (negative) una corona esterna di raggio \~8. Il docente osserva: «potete vedere che qua più o meno — non lo so quale è questo raggio — c'è un po' di **intersezione**». Le due classi non sono perfettamente separabili: con deviazione standard 1 su raggi che distano 3, le code si toccano. È voluto.
**L'obiettivo, nelle sue parole** (`TF-05 @ 00:16:00`): «quello che vogliamo fare è generare una funzione che, dati `x` e `y`, i coordinati, deve decidere se questi numeri appartengono al campo dei positivi o al campo dei negativi. Questa è l'idea della binary classification».
> **Punto risolto dal materiale ufficiale.** Questa cella non è mai inquadrata per intero nei frame: era **\[illeggibile\]**, e la versione precedente di questo manuale ricostruiva dal parlato nomi sbagliati (`xp`/`xn` minuscoli) e parametri approssimati.
---
## 4. Il generatore di batch, riscritto — `TF-05 @ 00:16:30`
`scritta in aula` — cella `[6]`. È lo stesso generatore della giornata 2, riscritto da capo con una sola differenza: il parametro si chiama `batch`, non `batch_size`.
```python
def dataset(inputs, labels, batch):
    length = len(inputs)
    indexes = list(range(length))
    np.random.shuffle(indexes)
    for i in range(0, length, batch):
        index = indexes[i: min(i + batch, length)]
        yield tf.gather(inputs, index), tf.gather(labels, index)
```
Il docente ripercorre il `min(...)`: «questo per evitare che noi usciamo da questo, che Python dia un errore, che questo è **out of range**».
---
## 5. Il modello come `tf.Module` — `TF-05 @ 00:19:00`
**Perché ereditare da ****`tf.Module`****.** `TF-05 @ 00:19:30`: «come al solito lo definiamo come una classe, ma a questo punto questa classe è una **subclass di ****`tf.Module`**. Non è più come una classe base, come abbiamo fatto per la linear regression, ma ereditiamo i metodi di questo `tf.Module`».
E la ragione pratica (`TF-05 @ 00:20:30`): «se avete altri layer che non erano definiti su Keras ma volete implementarli, per creare un nuovo layer potete solo implementare una subclass di questo `tf.Module`. Che vedete — se passo il mouse qua — ad esempio il `Dense` era infatti una subclass di questo `tf.Module`».
Il tooltip letto a schermo: «Base neural network module class. A module is a named container for `tf.Variable`s, other `tf.Module`s and functions which apply to user input.»
`scritta in aula` — cella `[8]`, prima parte:
```python
class NNModel(tf.Module):
    def __init__(self, name=None):
        super(NNModel, self).__init__(name)
        self.w1 = tf.Variable(tf.random.truncated_normal([2, 8]), dtype=tf.float32)
        self.b1 = tf.Variable(tf.zeros([1, 8]), dtype=tf.float32)
        self.w2 = tf.Variable(tf.random.truncated_normal([8, 16]), dtype=tf.float32)
        self.b2 = tf.Variable(tf.zeros([1, 16]), dtype=tf.float32)
        self.w3 = tf.Variable(tf.random.truncated_normal([16, 1]), dtype=tf.float32)
        self.b3 = tf.Variable(tf.zeros([1, 1]), dtype=tf.float32)

    @tf.function(input_signature=[tf.TensorSpec(shape=[None,2], dtype=tf.float32)])
    def __call__(self, x):
        x = tf.nn.relu( x @ self.w1 + self.b1)
        x = tf.nn.relu( x @ self.w2 + self.b2)
        y = tf.nn.sigmoid( x @ self.w3 + self.b3)
        return y
```
**L'architettura, e perché queste dimensioni.** 2 → 8 → 16 → 1.
Il docente costruisce le forme ragionando ad alta voce (`TF-05 @ 00:23:00`–`00:25:30`): «qua abbiamo un input 2, allora vuol dire che per fare la moltiplicazione dobbiamo avere la stessa dimensione per fare la moltiplicazione di matrice… e poi questo possiamo sceglierlo quando vogliamo, ma io lo metterò ad esempio a **8**». Poi: «qua avrò 2, ma a questo punto ho 8 elementi, allora devo creare una \[matrice\] con 8 per poter fare la moltiplicazione matriciale… e poi posso aumentare di nuovo qua, **16**». Infine: «l'output, quello che noi vogliamo è nel binario; al solito per la classificazione binaria usiamo una **singola uscita**, e al solito usiamo una **sigmoide** — ricordate quando abbiamo parlato di attivazione: il sigmoide dà una **probabilità**».
**`truncated_normal`**** invece di ****`normal`****.** `TF-05 @ 00:22:30`: «la differenza è che noi facciamo il *truncated* delle normali invece di usare direttamente `random_normal`. Che potete esplorare — ad esempio, come esercizio, cambiare la funzione di inizializzazione».
**Il bias inizializzato a zero**: «questa è infatti solo la somma, allora posso anche inizializzare con 0».
> **Il decoratore sul ****`__call__`**** è arrivato dopo**
>
> `@tf.function(input_signature=[tf.TensorSpec(shape=[None,2], dtype=tf.float32)])` **non c'è** mentre il docente scrive la classe: lo aggiunge fra le due registrazioni, per far girare l'addestramento dopo il crash della sezione 9. Lo dichiara lui stesso a `TF-06 @ 00:01:30`: «ho trasformato solo il `__call__` come un **autografo** — ma secondo me questo dovrebbe essere già automatico, perché noi ereditiamo da `tf.Module`: se fate un override dovrebbe essere già \[convertito\], ma io lo metto così solo per essere sicuro».
>
> L'`input_signature` con `shape=[None, 2]` fissa la firma del grafo: qualunque dimensione di batch, esattamente 2 feature. È così che si **impedisce il retracing** a ogni batch di dimensione diversa — il warning che aveva incontrato nella giornata 2.
---
## 6. La loss scritta a mano: binary cross-entropy — `TF-05 @ 00:28:30`
**Perché non l'errore quadratico.** «Ricordate che quando facciamo i confronti fra due valori, potrebbe essere molto molto piccolo. Noi possiamo usare ad esempio un *mean square*, ma **non ha senso** usare il mean square quando il valore è troppo piccolo. Ed è anche raccomandato, per la binary classification, usare una **binary cross-entropy**.»
**Il problema del logaritmo di zero.** `TF-05 @ 00:29:30`: «noi sappiamo che il `log(0)` **non è definito**. Allora, per non avere quell'errore durante questo calcolo, gli facciamo un piccolo margine… trasformiamo prima la predizione, perché il valore vero va bene — abbiamo 0.0 o 1.0 — ma della predizione non sapremmo mai il valore del sigmoide».
`scritta in aula` — cella `[8]`, secondo metodo:
```python
@tf.function
def loss_func(self, y_true, y_pred):
    eps = 1e-7
    y_pred = tf.clip_by_value(
        y_pred,
        eps,
        1.0 - eps
    )
    bce = - y_true * tf.math.log(y_pred) - (1 - y_true) * tf.math.log(1 - y_pred)
    return tf.reduce_mean(bce)
```
Sul valore di `eps` (`TF-05 @ 00:30:30`): «posso mettere qua ad esempio una epsilon, chiamiamola epsilon, e questo mettiamo… **10 alla meno 7**».
E la formula, dettata: «l'idea è che dobbiamo fare il **meno** del valore vero moltiplicato per il `log` della predizione, meno `1 - y_true` moltiplicato per il `log` di `1 - predizione`». Poi `reduce_mean`.
`tf.clip_by_value` è l'operazione che a `TF-03 @ 01:19:30` aveva solo nominato senza usarla. Qui serve davvero.
---
## 7. La metrica: accuratezza con soglia — `TF-05 @ 00:33:00`
`scritta in aula` — cella `[8]`, terzo metodo:
```python
# acccuracy 
@tf.function
def metric_func(self, y_true, y_pred):
    y_pred = tf.where(y_pred > 0.5, tf.ones_like(y_pred), tf.zeros_like(y_pred))
    return tf.reduce_mean(1 - tf.abs(y_true - y_pred))
```
Il docente riusa `tf.where` della giornata 2 — «ricordate anche questa API `tf.where`» — nella forma a tre argomenti, e spiega la **soglia**: «se l'output mi dà 0.3, allora questo dovrebbe essere negativo; se l'output è 0.6, allora positivo. E la soglia che io uso è **0.5**».
Poi la formula: `1 - |y_true - y_pred|` vale 1 quando coincidono e 0 quando differiscono, quindi la sua media è la frazione di predizioni corrette.
**Un'anticipazione importante** (`TF-05 @ 00:33:30`): «ovviamente qua vediamo più in dettaglio quando facciamo il sentiment analysis, perché qua lo faccio solo 0.5 come soglia — ma questo ovviamente \[conta\] durante l'addestramento». È il filo che riprende nella sezione 17.
---
## 8. Il ciclo di addestramento — `TF-05 @ 00:36:00`
La struttura è quella della giornata 2, con una differenza sostanziale.
`scritta in aula` — cella `[10]`:
```python
@tf.function
def train_step(model, inputs, labels, learning_rate=0.01):
    with tf.GradientTape() as tape:
        predictions = model(inputs)
        loss = model.loss_func(
            labels,
            predictions
        )
    grads = tape.gradient(loss, model.trainable_variables)
    for var, grad in zip(model.trainable_variables, grads):
        var.assign_sub(learning_rate * grad)
    metric = model.metric_func(labels, predictions)
    return loss, metric
```
> **Questo è il guadagno di ****`tf.Module`****, ed è il punto della sezione 5.** Nella giornata 2 il gradiente era chiesto su una lista scritta a mano, `[weight, bias]`, e l'aggiornamento era due righe copiate. Qui `model.trainable_variables` raccoglie da solo tutte e **sei** le variabili — `w1, b1, w2, b2, w3, b3` — perché `tf.Module` tiene traccia di ogni `tf.Variable` assegnata a un attributo. Il ciclo `zip` aggiorna tutto senza sapere quante sono. Aggiungere un layer non richiede di toccare l'addestramento.
`scritta in aula` — cella `[11]`:
```python
@tf.function
def train_loop(model, epochs):
    for epoch in range(1, epochs + 1):
        for inputs, labels in dataset(X, Y, batch=100):
            loss, metric = train_step(model, inputs, labels)
        if epoch % 10 == 0:
            tf.print("Epoch", epoch, " Loss: ", loss, "accuracy: ", metric)
```
> **Il ciclo esterno usa ****`range`****, non ****`tf.range`****.** È l'opposto della giornata 2. Con `range` di Python il ciclo viene **srotolato** in fase di tracing: il grafo contiene 50 copie del corpo. Funziona, ma il tracing costa — ed è una delle spiegazioni plausibili del crash della sezione 9. Il docente non lo commenta.
`scritta in aula` — cella `[13]`:
```python
model = NNModel()
train_loop(model, 50)
```
```javascript
Epoch 10  Loss:  0.569210351 accuracy:  0.66
Epoch 20  Loss:  0.527694881 accuracy:  0.7
Epoch 30  Loss:  0.432875365 accuracy:  0.85
Epoch 40  Loss:  0.398494601 accuracy:  0.88
Epoch 50  Loss:  0.313737661 accuracy:  0.88
```
**Il risultato, e una discrepanza.** A `TF-06 @ 00:01:30` il docente dice: «è andata per 50 epoche, potete vedere, l'accuratezza diventa **94**». Il notebook distribuito ne riporta **88**. Sono due esecuzioni diverse — il notebook non ha seed, e l'accuratezza è misurata **sull'ultimo batch** dell'ultima epoca, non sull'insieme. Vedi `day-03-divergenze.md` §3.
**La visualizzazione del risultato.** `scritta in aula` — cella `[15]`:
```python
plt.figure(figsize=(12, 5))

# Before training
ax1 = plt.subplot(121)
ax1.scatter(Xp[:,0], Xp[:,1], c="r")
ax1.scatter(Xn[:,0], Xn[:,1], c="b")
ax1.set_title("Ground Truth")

# After prediction
Xp_pred = tf.boolean_mask(X, tf.squeeze(model(X) >= 0.5))
Xn_pred = tf.boolean_mask(X, tf.squeeze(model(X) < 0.5))

ax2 = plt.subplot(122)
ax2.scatter(Xp_pred[:,0], Xp_pred[:,1], c="r")
ax2.scatter(Xn_pred[:,0], Xn_pred[:,1], c="b")
ax2.set_title("Model Predictions")

plt.show()
```
`tf.boolean_mask` separa i punti secondo la predizione del modello, con la stessa soglia 0.5 della metrica. Il confronto affiancato mostra dove la rete sbaglia: sulla corona di intersezione fra i due anelli.
---
## 9. Il kernel che muore, e il trasloco su Colab — `TF-05 @ 00:45:01`
Al lancio dell'addestramento il kernel muore:
```javascript
The Kernel crashed while executing code in the current cell or a previous cell.
Please review the code in the cell(s) to identify a possible cause of the failure.
Click here for more info.
View Jupyter log for further details.
```
```javascript
The kernel 'venv (Python 3.10.12)' died. Click here for more info. Vie[illeggibile]
```
Il docente apre un terminale e diagnostica — dopo due refusi, `ndvia-smi` e `ndivia-smi`:
```javascript
$ nvidia-smi
Tue Jun 17 16:51:25 2025
| NVIDIA-SMI 550.163.01   Driver Version: 550.163.01   CUDA Version: 12.4 |
|   0  NVIDIA GeForce RTX 2060   Off | 00000000:01:00.0  On |          N/A |
| N/A   68C    P8    9W /  80W |   4873MiB /  6144MiB |   0%      Default |
Processes:
|    0   N/A  N/A      3986      G   /usr/bin/gnome-shell              1MiB |
|    0   N/A  N/A    582477      C   ...LASS2025/17-06-2025/venv/bin/python  4834MiB |
$ kill -9 582477
```
Il processo Python del kernel teneva **4834 MiB su 6144**: la GPU era satura. Il docente lo termina a mano.
**E poi cambia macchina.** `TF-05 @ 00:46:00`: «questo è il problema, che non vorrei usare GPU… vado direttamente su **Google Colab** al momento, perché mi dava questo errore su VS Code, non so perché».
Da qui in avanti — per tutto il resto di TF-05 e per TF-06 — il docente lavora **su Colab**, caricando i notebook con *File → Upload notebook* e i dati con l'uploader della barra laterale. Le conseguenze pratiche che segnala mentre lavora:
- «dovete ricordare che questo notebook \[i file caricati\] si cancellerà quando cambiamo il **runtime**» (`TF-05 @ 00:49:00`), e infatti gli succede a `00:53:00`;
- il runtime va scelto **prima**: «prima di tutto lo scegliamo il runtime. Allora, io uso il CPU. Save. Faccio una bella *connect*»;
- i file caricati stanno sotto `/content`: «questo è come Linux, allora dovrebbe essere dentro `content`».
**La ripresa dell'addestramento**, `TF-06 @ 00:01:30`: «ho provato a lanciare questo e potete vedere che ho cambiato, perché sicuramente è un problema del mio GPU, del mio computer. Ho trasformato solo il `__call__` come un autografo… e poi è andata per 50 epoche».
<callout icon="➕">
	**Nota aggiunta:** il crash non ha una causa dichiarata nel video. Le due candidate visibili nel codice sono il ciclo esterno su `range` di Python, che srotola 50 copie del grafo in fase di tracing, e il `__call__` non decorato, che forza un retracing a ogni batch. Il docente interviene proprio sul secondo. Questa lettura è mia, ed è marcata.
</callout>
## Notebook della lezione
I file originali del docente, sul tuo Mac in `Downloads/TensorFlow-MDA/Materiale Sito/estratti/`:
- `17-06-2025/17-06-2025/NN-TF-completed.ipynb`
- `17-06-2025/17-06-2025/LR-TF.ipynb`
