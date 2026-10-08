# Artificial Intelligence - II
> Fonte Notion: https://app.notion.com/p/3d612abc808d8153aef4eb676bc28e01 — ultima modifica 2026-09-11T09:16:04.236Z

Modulo del Master Data Analytics. Il corso è **TensorFlow**, docente Louis Nantenaina Andrianaivo.
Si articola in **7 giornate**. Le registrazioni pubblicate sul portale coprono le prime 5, divise in 10 file video (`TF-01` … `TF-10`): ogni giornata è una registrazione tagliata a metà. Le giornate 6 e 7 hanno il materiale ma non la registrazione.
## Come sono fatte queste pagine
Ogni capitolo nasce dalla trascrizione dell'audio unita alla lettura dei fotogrammi del video, con il codice preso dai notebook ufficiali dove esistono. I riferimenti tipo `TF-02 @ 00:44:30` indicano il file video e il minuto, per tornare al punto originale.
Convenzioni:
- `[?]` — parola non chiara nell'audio
- `[illeggibile]` — testo non leggibile a schermo
- Le note marcate **Nota aggiunta** sono integrazioni non trattate a lezione
## Giornata 1 — Introduzione, ambiente, acceleratori, API dei tensori
Video `TF-01` e `TF-02`.
<table header-row="true">
<tr>
<td>Capitolo</td>
<td>Sezioni</td>
<td>Contenuto</td>
</tr>
<tr>
<td>[01 - Cos'è TensorFlow](01-cos-e-tensorflow.md)</td>
<td>1–5</td>
<td>framework contro libreria, tensori e grafo di dataflow, i cinque passi, campi di applicazione</td>
</tr>
<tr>
<td>[02 - Ambiente e installazione](02-ambiente-e-installazione.md)</td>
<td>6–16</td>
<td>virtualenv e VS Code, verifica GPU, Jupyter, Docker e nvidia-ctk, Colab e Kaggle</td>
</tr>
<tr>
<td>[03 - Benchmark CPU / GPU / TPU su MNIST](03-benchmark-cpu-gpu-tpu-su-mnist.md)</td>
<td>17–21</td>
<td>`tf.data`, il modello, i tempi a confronto, `TPUStrategy` e la `loss: nan`</td>
</tr>
<tr>
<td>[04 - API low-level dei tensori](04-api-low-level-dei-tensori.md)</td>
<td>22–33</td>
<td>creazione e forma, reshape e transpose, costanti e variabili, operazioni, gather e scatter</td>
</tr>
<tr>
<td>[05 - Appendici](05-appendici.md)</td>
<td>—</td>
<td>esercizi aperti, glossario (33 voci), punti a bassa confidenza</td>
</tr>
</table>
## Stato
<table header-row="true">
<tr>
<td>Giornata</td>
<td>Video</td>
<td>Materiale</td>
<td>Manuale</td>
</tr>
<tr>
<td>1</td>
<td>TF-01, TF-02</td>
<td>sì</td>
<td>fatto</td>
</tr>
<tr>
<td>2</td>
<td>TF-03, TF-04</td>
<td>sì</td>
<td>fatto</td>
</tr>
<tr>
<td>3</td>
<td>TF-05, TF-06</td>
<td>sì</td>
<td>fatto</td>
</tr>
<tr>
<td>4</td>
<td>TF-07, TF-08</td>
<td>sì</td>
<td>fatto</td>
</tr>
<tr>
<td>5</td>
<td>TF-09, TF-10</td>
<td>sì</td>
<td>fatto</td>
</tr>
<tr>
<td>6</td>
<td>—</td>
<td>sì (init + finale)</td>
<td>da fare</td>
</tr>
<tr>
<td>7</td>
<td>—</td>
<td>sì (init + finale)</td>
<td>da fare</td>
</tr>
</table>

- [TensorFlow](tensorflow.md)
- [01 - Cos'è TensorFlow](01-cos-e-tensorflow.md)
- [02 - Ambiente e installazione](02-ambiente-e-installazione.md)
- [03 - Benchmark CPU / GPU / TPU su MNIST](03-benchmark-cpu-gpu-tpu-su-mnist.md)
- [04 - API low-level dei tensori](04-api-low-level-dei-tensori.md)
- [05 - Appendici](05-appendici.md)
- [08 - Reti neurali scritte a mano](08-reti-neurali-scritte-a-mano.md)
- [06 - Indicizzazione, broadcasting e layer a mano](06-indicizzazione-broadcasting-e-layer-a-mano.md)
- [13 - Generazione di titoli a parole](13-generazione-di-titoli-a-parole.md)
- [09 - Da tf.data a Keras, e le metriche](09-da-tf-data-a-keras-e-le-metriche.md)
- [14 - Serie temporali con LSTM](14-serie-temporali-con-lstm.md)
- [07 - Grafo, autograph e derivazione automatica](07-grafo-autograph-e-derivazione-automatica.md)
- [10 - Selezione del modello e LeNet-5](10-selezione-del-modello-e-lenet-5.md)
- [15 - Autoencoder e dati tabellari](15-autoencoder-e-dati-tabellari.md)
- [11 - Callback, checkpoint e transfer learning](11-callback-checkpoint-e-transfer-learning.md)
- [12 - Generazione di testo con LSTM](12-generazione-di-testo-con-lstm.md)

---
## Giornata 2 — indicizzazione, broadcasting, grafo · `TF-03` `TF-04`
<table header-row="true">
<tr>
<td>Capitolo</td>
<td>Contenuto</td>
</tr>
<tr>
<td>[06 - Indicizzazione, broadcasting e layer a mano](06-indicizzazione-broadcasting-e-layer-a-mano.md)</td>
<td>selezione per condizione, broadcasting, simulazione di un dense layer, funzioni di attivazione, pooling</td>
</tr>
<tr>
<td>[07 - Grafo, autograph e derivazione automatica](07-grafo-autograph-e-derivazione-automatica.md)</td>
<td>che cos'è il grafo e quanto fa guadagnare, le tre regole dell'autograph, `GradientTape`, regressione lineare a mano</td>
</tr>
</table>
## Giornata 3 — dalle reti a mano a Keras · `TF-05` `TF-06`
<table header-row="true">
<tr>
<td>Capitolo</td>
<td>Contenuto</td>
</tr>
<tr>
<td>[08 - Reti neurali scritte a mano](08-reti-neurali-scritte-a-mano.md)</td>
<td>il problema dei due anelli, generatore di batch, modello come `tf.Module`, binary cross-entropy a mano, ciclo di addestramento</td>
</tr>
<tr>
<td>[09 - Da tf.data a Keras, e le metriche](09-da-tf-data-a-keras-e-le-metriche.md)</td>
<td>l'API `tf.data`, perché passare a Keras, MNIST, recensioni IMDB, perché l'accuratezza non basta, curve e soglia</td>
</tr>
</table>
## Giornata 4 — selezione del modello, CNN, transfer learning · `TF-07` `TF-08`
<table header-row="true">
<tr>
<td>Capitolo</td>
<td>Contenuto</td>
</tr>
<tr>
<td>[10 - Selezione del modello e LeNet-5](10-selezione-del-modello-e-lenet-5.md)</td>
<td>catalogo dei layer Keras, MNIST con modelli a confronto, dropout, LeNet-5, il verdetto</td>
</tr>
<tr>
<td>[11 - Callback, checkpoint e transfer learning](11-callback-checkpoint-e-transfer-learning.md)</td>
<td>CNN su CIFAR, warm-up e TensorBoard, il learning rate scheduler che uccide il modello, congelare e sfreezare i layer</td>
</tr>
<tr>
<td>[12 - Generazione di testo con LSTM](12-generazione-di-testo-con-lstm.md)</td>
<td>generazione carattere per carattere, modello di inferenza, l'assegnazione finale</td>
</tr>
</table>
## Giornata 5 — testo, serie storiche, autoencoder, dati tabellari · `TF-09` `TF-10`
<table header-row="true">
<tr>
<td>Capitolo</td>
<td>Contenuto</td>
</tr>
<tr>
<td>[13 - Generazione di titoli a parole](13-generazione-di-titoli-a-parole.md)</td>
<td>dai caratteri alle parole, il tokenizer, sequenze progressive, generare un titolo</td>
</tr>
<tr>
<td>[14 - Serie temporali con LSTM](14-serie-temporali-con-lstm.md)</td>
<td>il forecast su BTC-EUR, tre modelli LSTM a confronto, la previsione ricorsiva</td>
</tr>
<tr>
<td>[15 - Autoencoder e dati tabellari](15-autoencoder-e-dati-tabellari.md)</td>
<td>super-risoluzione, l'autoencoder, guardare i risultati, il caso Titanic</td>
</tr>
</table>
<callout icon="⚠️">
	**Tre errori passati inosservati a lezione**, documentati e verificati rieseguendo il codice. Nel capitolo 11 il learning rate scheduler azzera l'addestramento, e il suo checkpoint viene poi ricaricato dal notebook successivo. Nel capitolo 13 `argmax` è la causa del testo ciclico. Nel capitolo 14 le callback del forecast sono inerti e `ModelCheckpoint` salva l'ultima epoca invece della migliore. Se studi da quei notebook, leggi prima le note.
</callout>
