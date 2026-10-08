# 05 - Appendici
> Fonte Notion: https://app.notion.com/p/3d612abc808d81ba9d37c29ba5a73104 — ultima modifica 2026-09-09T12:50:09.680Z

> Giornata 1 · esercizi lasciati aperti, glossario, punti a bassa confidenza, materiale ufficiale usato.
---
## Esercizi lasciati aperti
**Assegnato a voce a fine giornata** (`TF-02 @ 01:06:30`–`01:08:30`), in due parti:
1. Selezionare i voti dello **studente numero 5** per **tutti i moduli**.
2. Sugli stessi voti, **aggiungere 2** a ciascuna materia, tenendo conto che **un voto non può superare 30**.
**Presenti come commenti nel notebook ufficiale ****`api-explorations.ipynb`**, senza soluzione:
- cella 28: creare un tensore `float32` di shape `(2, 4)` riempito solo di 7, **senza usare ****`tf.fill`**;
- cella 46: `# ex: range(24), reshape 2, 3,4 => transpose 4,3,2` e `# es di scatter_nd`.
> Nessuno di questi viene risolto nelle due registrazioni della giornata 1.
## Glossario dei termini introdotti
<table header-row="true">
<tr>
<td>Termine</td>
<td>Definizione data nella lezione</td>
</tr>
<tr>
<td>**Tensore**</td>
<td>Un vettore a cui si aggiunge la dimensione dei canali; è il tipo di dato fondamentale di TensorFlow ed è ciò che ogni nodo del grafo produce in uscita. `TF-01 @ 00:03:00`</td>
</tr>
<tr>
<td>**Framework (vs libreria)**</td>
<td>TensorFlow non esegue il codice Python riga per riga: lo trasforma in un grafo da compilare. Python è solo l'interfaccia verso un core scritto in C++. `TF-01 @ 00:02:00`</td>
</tr>
<tr>
<td>**Dataflow graph**</td>
<td>Grafo diretto in cui i nodi sono operazioni e gli archi il flusso dei dati fra un'operazione e l'altra. `TF-01 @ 00:04:00`</td>
</tr>
<tr>
<td>**Loss function**</td>
<td>Funzione che misura la performance del modello durante l'addestramento; l'obiettivo è diminuirla. `TF-01 @ 00:06:00`</td>
</tr>
<tr>
<td>**Backpropagation**</td>
<td>Il meccanismo con cui si propaga l'errore per aggiornare i parametri; si appoggia alla discesa del gradiente stocastica. `TF-01 @ 00:06:30`</td>
</tr>
<tr>
<td>**Ottimizzatore**</td>
<td>Ciò che decide come compiere il passo verso il minimo della loss. Nei problemi di ML trovare il minimo globale è difficile; si cerca un minimo che generalizzi. `TF-01 @ 00:07:00`</td>
</tr>
<tr>
<td>**Epoca**</td>
<td>Un passaggio completo sul dataset di addestramento; il training loop ne definisce il numero. `TF-01 @ 00:08:00`</td>
</tr>
<tr>
<td>**Batch**</td>
<td>Il sottoinsieme di dati su cui si applica la backpropagation a ogni passo. `TF-01 @ 00:08:30`</td>
</tr>
<tr>
<td>**Early stopping**</td>
<td>Definire una variabile da sorvegliare e fermare il training loop quando raggiunge un certo valore. `TF-01 @ 00:09:00`</td>
</tr>
<tr>
<td>**Training set / test set**</td>
<td>I dati vanno separati; i dati di test non devono partecipare all'addestramento, altrimenti la misura finale non è veritiera. `TF-01 @ 00:09:00`, `TF-01 @ 01:04:00`</td>
</tr>
<tr>
<td>**Normalizzazione**</td>
<td>Riportare i dati nello stesso intervallo. Per le immagini: i pixel vanno da 0 a 255, si dividono per 255 per portarli in 0–1. `TF-01 @ 00:11:00`, `TF-01 @ 01:00:30`</td>
</tr>
<tr>
<td>**Clustering**</td>
<td>Algoritmo usato per categorizzare e classificare i dati assegnando una categoria. `TF-01 @ 00:11:30`</td>
</tr>
<tr>
<td>**Embedding**</td>
<td>Rappresentazione necessaria per la ricerca semantica su testo (applicazioni tipo RAG). `TF-01 @ 00:12:30`</td>
</tr>
<tr>
<td>**Reward**</td>
<td>L'output da cui l'agente impara nell'apprendimento per rinforzo; l'obiettivo è massimizzarla. `TF-01 @ 00:15:00`</td>
</tr>
<tr>
<td>**CNN (rete convoluzionale)**</td>
<td>Il tipo di rete con cui è stato affrontato il problema della computer vision. `TF-01 @ 00:15:00`</td>
</tr>
<tr>
<td>**cuDNN**</td>
<td>Libreria CUDA scritta in C++ che implementa le reti neurali a basso livello. `TF-01 @ 00:31:00`</td>
</tr>
<tr>
<td>**Pluggable device**</td>
<td>Architettura che aggiunge il supporto a nuovi dispositivi come pacchetti plug-in separati, senza modificare il codice di TensorFlow (comunicazione via C API). `TF-01 @ 00:30:00`</td>
</tr>
<tr>
<td>**Container (Docker)**</td>
<td>Ambiente separato come una macchina virtuale, ma progettato per un **singolo processo**; serve a dichiarare una volta tutti i requisiti e ottenere un ambiente omogeneo. `TF-01 @ 00:32:30`</td>
</tr>
<tr>
<td>**NVIDIA Container Toolkit**</td>
<td>Il componente che permette al container di vedere la scheda grafica: Docker da solo vede solo la virtualizzazione della CPU. `TF-01 @ 00:38:30`</td>
</tr>
<tr>
<td>**TPU**</td>
<td>Acceleratore hardware messo a disposizione da Google; si presenta come un *worker* a cui bisogna connettersi. `TF-01 @ 01:12:00`, `TF-01 @ 01:16:30`</td>
</tr>
<tr>
<td>**TPUStrategy / scope**</td>
<td>Context manager dentro cui il modello va costruito e compilato, perché il grafo venga creato sulla TPU. `TF-01 @ 01:17:30`</td>
</tr>
<tr>
<td>**`!`**** nelle celle di notebook**</td>
<td>Prefisso che esegue il comando nel terminale sottostante invece che nell'interprete Python. `TF-01 @ 01:14:00`</td>
</tr>
<tr>
<td>**shape / dtype**</td>
<td>Le due proprieta' che definiscono un tensore. Regola di lettura: l'ultima dimensione e' la piu' interna, la prima da sinistra la piu' esterna. `TF-02 @ 00:02:30`</td>
</tr>
<tr>
<td>**`tf.fill`**** vs ****`tf.constant`**</td>
<td>In `constant` si danno i valori e la forma ne discende; in `fill` si da' prima la forma e poi il valore. `TF-02 @ 00:05:30`</td>
</tr>
<tr>
<td>**`tf.zeros_like`**</td>
<td>Crea un tensore di zeri con la stessa forma di uno esistente, senza dover estrarre e riconvertire la shape. `TF-02 @ 00:07:00`</td>
</tr>
<tr>
<td>**`tf.squeeze`**</td>
<td>Toglie **tutte** le dimensioni unitarie. Si usa sull'**output**, per eliminare la dimensione di batch superflua in inferenza. `TF-02 @ 00:18:30`</td>
</tr>
<tr>
<td>**`tf.expand_dims`**</td>
<td>Aggiunge una dimensione nella posizione indicata da `axis`. Si usa sull'**input**, per far sembrare un singolo esempio un batch di uno. `TF-02 @ 00:20:00`</td>
</tr>
<tr>
<td>**`perm`**** in ****`tf.transpose`**</td>
<td>Su un tensore a piu' di due dimensioni la trasposizione non e' univoca: `perm` dichiara la permutazione voluta. Su una matrice quadrata si puo' omettere. `TF-02 @ 00:31:00`</td>
</tr>
<tr>
<td>**tile**</td>
<td>Piastrella: un motivo i cui bordi combaciano, ripetibile senza giunzioni visibili. `tf.tile` ripete il tensore lungo ciascuna dimensione. `TF-02 @ 00:33:30`</td>
</tr>
<tr>
<td>**`tf.Variable`**</td>
<td>Mutabile con memoria fissa, va inizializzata, ed e' **tracciata durante l'addestramento**: TensorFlow sa che rispetto a essa va calcolata la derivata. E' cio' che si salva in un checkpoint. `TF-02 @ 00:37:30`</td>
</tr>
<tr>
<td>**`tf.matmul`**** vs ****`tf.multiply`**</td>
<td>Prodotto righe-per-colonne contro prodotto elemento per elemento. `TF-02 @ 00:46:00`</td>
</tr>
<tr>
<td>**Grafo e funzioni TensorFlow**</td>
<td>Una funzione TensorFlow definisce un grafo, e il grafo deve usare funzioni TensorFlow: mescolarvi NumPy o funzioni Python produce comportamenti imprevedibili e rende impossibile il debug. `TF-02 @ 00:53:30`</td>
</tr>
<tr>
<td>**`tf.gather`**** / ****`tf.scatter`**</td>
<td>Selezionare e aggiornare per indici. Sostituiscono il ciclo `for` perche' sugli acceleratori l'esecuzione e' parallela sui thread, non sequenziale. `TF-02 @ 00:57:30`</td>
</tr>
</table>
---
## Punti a bassa confidenza
Segnalati automaticamente dai criteri combinati (`avg_logprob < -0.6`, `no_speech_prob > 0.5`, sequenze anomale, parola di contenuto sotto 0.15 di probabilita' esclusi glossario e parole funzione). L'elenco completo, con i motivi, e' in `day-01-bassa-confidenza.md`.
**TF-01 — 23 segmenti segnalati.**
**TF-02 — 16 segmenti segnalati.**
### Testo a schermo non leggibile `[illeggibile]`
<table header-row="true">
<tr>
<td>Dove</td>
<td>Punto</td>
</tr>
<tr>
<td>`TF-01 @ 00:16:55`</td>
<td>Negli appunti, il blocco per l'installazione **con supporto GPU** resta sotto il bordo inferiore in tutti i frame.</td>
</tr>
<tr>
<td>`TF-01 @ 00:30:41`, `00:36:27`</td>
<td>Nella pagina *GPU device plugins*, la riga `[PhysicalDevice(...)` e' tagliata a destra.</td>
</tr>
<tr>
<td>`TF-01 @ 00:44:02`, `00:51:22`</td>
<td>I log CUDA nelle celle sono troncati dalla larghezza della finestra.</td>
</tr>
<tr>
<td>`TF-01 @ 01:07:00`, `01:10:12`, `01:11:16`, `01:19:11`</td>
<td>Il `UserWarning` di Keras su `input_shape` e' sempre troncato.</td>
</tr>
<tr>
<td>`TF-01 @ 01:20:55`</td>
<td>Nella tabella di `model.summary()` le prime due righe (i due `conv2d`) sono sopra il bordo superiore.</td>
</tr>
<tr>
<td>`TF-01 @ 00:26:00`</td>
<td>Nell'output di `nvidia-smi` la sezione "Processes:" prosegue sotto il bordo.</td>
</tr>
<tr>
<td>`TF-02 @ 00:22:58`</td>
<td>Il messaggio dell'`InvalidArgumentError` sul reshape e' tagliato a destra.</td>
</tr>
<tr>
<td>`TF-02 @ 00:50:07`</td>
<td>Il messaggio "Matrix size-incompatible" del `matmul` e' tagliato a destra.</td>
</tr>
<tr>
<td>`TF-02 @ 00:52:45`</td>
<td>L'elenco dei dtype ammessi da `Sqrt` e' tagliato a destra su entrambe le righe.</td>
</tr>
</table>
### Non trascritto per riservatezza
A `TF-01 @ 00:56:00` una schermata del browser mostra la barra di ricerca con suggerimenti personali e l'indirizzo email privato del docente. Il frame resta in `out/TF-01/frames/` ma il contenuto non e' riportato.
---
## Materiale ufficiale usato
<table header-row="true">
<tr>
<td>File</td>
<td>Usato per</td>
</tr>
<tr>
<td>`APPUNTI.pdf`</td>
<td>Perimetro e ordine degli argomenti della giornata</td>
</tr>
<tr>
<td>`tensorflow day-1/day-01-appunti.pdf`</td>
<td>E' il PDF mostrato a schermo come `appunti.pdf` (sezioni 6, 8)</td>
</tr>
<tr>
<td>`tensorflow day-1/docker/docker-compose.yml`</td>
<td>Blocco YAML della sezione 13 (versione ufficiale)</td>
</tr>
<tr>
<td>`tensorflow day-1/docker/README.md`</td>
<td>Prerequisiti e verifica GPU (sezione 12)</td>
</tr>
<tr>
<td>`tensorflow day-1/notebooks/colab_mnist_cpu_gpu.ipynb`</td>
<td>Blocchi di codice delle sezioni 17-19</td>
</tr>
<tr>
<td>`tensorflow day-1/notebooks/colab_mnist_tpu.ipynb`</td>
<td>Blocchi di codice della sezione 20</td>
</tr>
<tr>
<td>`tensorflow day-1/notebooks/api-explorations.ipynb`</td>
<td>**Non** usato come fonte dei blocchi: e' un file diverso da quello mostrato. Fonte degli esercizi aperti. Vedi `day-01-divergenze.md` §1</td>
</tr>
</table>
Elenco completo delle divergenze fra materiale e schermo: **`day-01-divergenze.md`**.
