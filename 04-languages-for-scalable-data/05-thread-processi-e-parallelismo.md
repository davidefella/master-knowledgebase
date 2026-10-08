# 05 - Thread, processi e parallelismo

> Fonte Notion: https://app.notion.com/p/3dd12abc808d81c7b8f3ca30244b9f34 — ultima modifica 2026-09-17T09:21:33.378Z

Fonti: slide `MDA5Multithreading` (138 pagine con animazioni, 27 schermate; slide di Elia Onofri, Roma Tre), `008_OpenMP` (97 pagine; Moreno Marzolla, Università di Bologna, dal cap. 5 del Pacheco), immagine `ProcessesVsThreads.png`; lezioni `LSD-05` (00:46:15 → 01:48:09), `LSD-06` (00:43:51 → fine), `LSD-07` (00:00:09 → 00:39:29); edizione 2026: `Teams 4` (2:11:18 → fine), `Teams Extra-1` (28/04/2026, 0:09:30 → 0:39:00), `Teams Extra-2` (30/04/2026, 0:13:39 → 0:27:11, 1:28:18 → fine).
Il capitolo spiega perché oggi le prestazioni passano per il parallelismo, quali sono i modelli (thread e processi, memoria condivisa e distribuita), come si misura la scalabilità e come si programma in pratica con **Pthreads**, **OpenMP** e **MPI**. I problemi di correttezza che nascono dal parallelismo (race condition, data race, deadlock) e la progettazione di un algoritmo parallelo sono nel capitolo 06. `Teams Extra-1` e `Teams Extra-2` sono due **lezioni extra** del 28 e 30 aprile 2026, non a calendario: probabilmente una continuazione informale offerta alla classe dopo l'ultima lezione del 24/04. I questionari erano già stati pubblicati, quindi le uso solo come integrazione ed esempio.
> **Nota sulla numerazione delle slide:** `MDA5` è un PDF esportato con le animazioni, quindi la stessa schermata occupa più pagine. Cito la pagina in cui la schermata è completa: p9 (architetture), p14 (vincoli fisici), p18 (thread e processi), p24 (domande), p33 (tabella multithreading/multiprocessing), p43 (Pthreads), p51 e p55 (esempio Pthreads), p62 (considerazioni), p72 (OpenMP), p82 (concetti OpenMP), p92 e p98 (esempio OpenMP), p108 (MPI), p115 (concetti MPI), p116–p124 (topologie e collettive), p134 e p138 (esempio MPI).
## 1. Perché il parallelismo è inevitabile
**Slide MDA5 p2–p14.** "C'era una volta" l'architettura di **Von Neumann**: una sola unità di elaborazione, un'istruzione alla volta, memoria **piatta** (ogni accesso ha lo stesso costo). Oggi ci sono più unità di elaborazione, più istruzioni eseguite su più dati allo stesso tempo, istruzioni complesse spezzate in istruzioni semplici messe in **pipeline**, e una **forte gerarchia di memoria** con costi di accesso diversi (p9). Il grafico delle prestazioni single-thread mostra un **plateau** mentre il numero di transistor continua a crescere (p10). Non si possono fare transistor più piccoli (limiti fisici del silicio), non si può aumentare la frequenza (dissipazione del calore), non si possono aggiungere transistor (vincoli di comunicazione): quindi **più unità di elaborazione** (p11–p14).
**Docente** (`LSD-05 @ 00:46:15`–`00:55:22`).
- La frequenza si è fermata sui 3–4 GHz ma i transistor aumentano perché aumentano i **core**: un processore moderno equivale a "4, 8 processori di una volta". Questo ha tenuto in vita la legge di Moore, ma non le prestazioni single-thread. L'unico modo di ottenere prestazioni adeguate è il **parallelismo**, nelle due forme di **multithreading** e **multiprocessing**.
- **Che cos'è un core** (p15–p16): quello che una volta era una CPU, con unità di controllo, program counter, unità aritmetico-logica e cache. Ogni core ha cache **L1 e L2** proprie e condivide la **L3**; i core condividono controller di memoria e I/O.
- **NUMA** (*Non-Uniform Memory Access*): con 4 core il controller di memoria non è un collo di bottiglia, con 192 sì. Si mettono più controller, ognuno "vicino" a una parte della RAM; accedere alla memoria "lontana" costa più latenza.
**Edizione 2026** (`Teams 4 @ 2:11:18`–`2:24:46`; `Teams Extra-1 @ 0:09:30`–`0:20:30`).
- Il multithreading è "il vero elefante nella cristalleria" della scalabilità. Dal 2005 circa l'unico modo di fare scale up è stato aumentare i core; gli algoritmi pensati per l'esecuzione sequenziale vanno **ripensati** per il multicore. "Un core oggi è ciò che 20 anni fa era una CPU".
- Analogia: dieci persone che scrivono la stessa lettera non la finiscono in un decimo del tempo.
- **NUMA in concreto** (`Teams Extra-1 @ 0:16:04`–`0:20:07`): su una macchina a due socket ogni socket ha accesso privilegiato a una parte della RAM; un vettore da 20 GB è "spalmato" su più nodi di memoria, e un core che lavora sulla parte dell'altro socket paga più latenza.
<callout icon="⚠️">
	**Correzione.** **"La memoria piatta è vera ancora oggi nella maggior parte delle architetture"** (`LSD-05 @ 00:47:32`): contraddice la slide p9. La gerarchia cache L1/L2/L3–RAM–disco rende i costi di accesso non uniformi su qualunque PC; la NUMA vera e propria riguarda soprattutto i server con più socket. **Pipeline** (`LSD-05 @ 00:48:06`): fetch, decode, execute e store non sono eseguite contemporaneamente per la stessa istruzione; si sovrappongono le fasi di istruzioni *diverse*, come in una catena di montaggio. **Legge di Moore:** riguarda il numero di transistor, non le prestazioni. **Date:** il plateau della frequenza (fine del *Dennard scaling*) è di metà anni 2000. **NUMA "per certi versi uno scale-out"** (`Teams Extra-1 @ 0:19:14`): una macchina NUMA è **scale-up**, un solo nodo con un solo spazio di indirizzi; lo scale-out aggiunge nodi con memorie separate. Il transito verso la memoria dell'altro socket avviene in hardware (interconnessione QPI/UPI o HyperTransport), senza intervento dei core remoti. **Conteggio dei core** (`Teams Extra-2 @ 0:52:05`): 2 socket × 10 core × 2 thread hardware fanno 20 core fisici e **40 CPU logiche**, non 80; i thread SMT (hyper-threading) condividono le risorse del core e rendono di solito lo 0–30% in più, non il doppio.
</callout>
## 2. Thread e processi
**Slide MDA5 p17–p18.** Tra thread e processo "**uno contiene l'altro**"; si differenziano per **creazione** (*spawning*), **condivisione dei dati** e **comunicazione**.
**Slide MDA5 p33** (tabella completa):
<table header-row="true">
<tr>
<td>Multithreading</td>
<td>Multiprocessing</td>
</tr>
<tr>
<td>serve ad aumentare la potenza di calcolo</td>
<td>serve ad aumentare la potenza di calcolo</td>
</tr>
<tr>
<td>permette a un processo di eseguire più segmenti di codice</td>
<td>permette a più unità di elaborazione di girare in parallelo</td>
</tr>
<tr>
<td>i thread sono creati da un solo processo; la creazione è **economica**</td>
<td>i processi sono creati con chiamate di sistema; la creazione è **costosa**</td>
</tr>
<tr>
<td>nuovi thread creati in modo simmetrico o asimmetrico</td>
<td>classificati in simmetrici e asimmetrici</td>
</tr>
<tr>
<td>condividono lo spazio di memoria</td>
<td>spazi di memoria e indirizzi indipendenti</td>
</tr>
<tr>
<td>comunicano tramite la memoria condivisa (la slide dice "activation registries")</td>
<td>comunicano tramite canali: pipe, memoria condivisa, socket</td>
</tr>
<tr>
<td>possono "sconfinare" negli altri thread</td>
<td>operano in modo indipendente</td>
</tr>
</table>
**Docente** (`LSD-05 @ 00:55:22`–`01:08:32`).
- I processi sono **isolati** dal sistema operativo insieme alla CPU: Word non accede ai dati di Chrome, e un accesso alla memoria altrui fa terminare il processo. I thread di un processo invece **condividono trasparentemente la memoria**. È "più preoccupante": un thread può scrivere i dati su cui lavora un altro, quindi nascono **problemi di consistenza**.
- Allora perché usare il multithreading? **Analogia dei dipendenti:** dieci dipendenti con dieci progetti diversi sono multiprocessing, ognuno ha il pieno controllo del suo; se voglio che *un* progetto finisca prima lo do a un gruppo, ed è lì che serve il multithreading. Più veloce, ma in gruppo c'è chi sovrascrive il file dell'altro: "è più veloce il multithreading ma è più facile che ci siano problemi".
- **Analogia biologica:** la `fork` crea un processo come la mitosi crea due cellule indipendenti; nel multithreading è come se nella stessa cellula "si splittassero soltanto i nuclei". I thread eseguono lo stesso codice ma ognuno ha un **identificativo** (0, 1, 2, …) con cui sa su quale **fetta dei dati** lavorare: "crea n thread e dividi la torta in n fette" va scritto esplicitamente.
- "Un core è collegato a un **flusso di esecuzione**, non a un processo": 4 core possono eseguire 4 processi single-thread o 1 processo con 4 thread.
**Docente** (`LSD-06 @ 00:43:51`–`01:00:48`).
- Con **htop** mostra che una macchina dual core esegue decine di processi grazie al time slicing, e che le righe di Chromium sono thread (PID diversi, stessa memoria).
- **Analogia dell'appartamento:** un processo è un appartamento, i thread sono le persone che ci vivono con le chiavi di casa. È più facile aggiungere un inquilino che un appartamento al palazzo. Tra appartamenti ci si parla "al telefono" (un canale esterno, lento); tra inquilini con un post-it sulla lavagna di casa (veloce). Ma i coinquilini "hanno accesso anche al frigorifero dove c'è il cibo degli altri": ogni thread ha una "stanza propria" (le variabili locali) con una porta senza chiave.
- "Scalable data science fa più rima con multithreading che con multiprocessing", salvo i sistemi a memoria distribuita.
**Edizione 2026** (`Teams 4 @ 2:24:46`–`2:39:45`). Stessa distinzione, con lo schema classico di `ProcessesVsThreads.png`: i thread di un processo condividono **codice, dati e file aperti**, ma ciascuno ha **registri e stack propri**. Analogia della casa condivisa: se un coinquilino sposta la cravatta o finisce il pane, gli altri non li trovano. E una distinzione importante: "**il multithreading è una cosa software, il multicore è una cosa hardware**". Con 4 core si possono eseguire 4 processi isolati oppure 4 thread che lavorano sugli stessi dati: il secondo modo "velocizza tantissimo" alcuni algoritmi, se il codice è thread-safe.
<callout icon="⚠️">
	**Correzione.** La slide p33 dice che i thread condividono "the same static memory space (**stack**)": ogni thread ha il **proprio stack**; condividono heap, dati globali e codice. È quello che dice il docente con la "stanza propria" delle variabili locali. **Fork e copia della memoria** (`LSD-06 @ 00:55:10`–`00:55:44`): su Linux `fork()` usa il **copy-on-write**, quindi le pagine si copiano fisicamente solo quando vengono modificate; creare un processo resta più costoso che creare un thread, ma non per una copia integrale immediata. I valori RES di htop includono anche memoria condivisa. **"Il sistema operativo uccide i thread che hanno fatto l'intrusione"** (`LSD-06 @ 00:56:22`): con la memoria virtuale un processo di norma non riesce nemmeno a indirizzare la memoria altrui; un accesso non valido genera un segnale (SIGSEGV) che termina l'intero processo. **Comunicazione tra processi "sempre lenta"**: la slide cita anche la memoria condivisa tra processi, che non è lenta. **Chrome** (`LSD-05 @ 00:57:15`) è soprattutto *multi-processo* (un processo per renderer, GPU, rete, audio), con molti thread in ciascun processo. **Multiprocessing e multitasking** (`LSD-06 @ 00:44:30`): eseguire più programmi su pochi core con il time slicing è multitasking; il multiprocessing è l'uso di più unità di elaborazione o processi in parallelo.
</callout>
**Concorrenza e chiamate bloccanti** (slide p23–p24; `LSD-06 @ 00:33:41`–`00:43:51`). La **concorrenza** è l'esecuzione di più attività in un ordine che non si controlla, che fanno evolvere lo stato del sistema: esiste anche su un single core grazie al *time slicing*, ed è "il presupposto principale del parallelismo". Una **chiamata bloccante** sospende il thread finché il sistema operativo non restituisce il controllo (tipicamente l'I/O, come `socket.accept()`). La spiegazione completa è nel capitolo 04, §3.
## 3. Tassonomia di Flynn
**Slide MDA5 p19–p20.** Flynn classifica le architetture per numero di flussi di istruzioni e di dati.
<table header-row="true">
<tr>
<td>Classe</td>
<td>Significato</td>
<td>Esempio (docente)</td>
</tr>
<tr>
<td>**SISD**</td>
<td>single instruction, single data</td>
<td>CPU single core, esecuzione seriale</td>
</tr>
<tr>
<td>**SIMD**</td>
<td>single instruction, multiple data</td>
<td>GPU: molti core semplici che eseguono, a gruppi, la stessa istruzione su dati diversi</td>
</tr>
<tr>
<td>**MIMD**</td>
<td>multiple instruction, multiple data</td>
<td>CPU multicore: ogni core esegue istruzioni diverse su dati diversi</td>
</tr>
<tr>
<td>**MISD**</td>
<td>multiple instruction, single data</td>
<td>"praticamente inutilizzata"</td>
</tr>
</table>
**Docente** (`LSD-05 @ 01:15:58`–`01:22:37`). Per il MISD propone un attacco a forza bruta su un cifrario (stesso registro, operazioni diverse) e subito lo smonta: un'architettura con mille core dà uno speedup ×1000, ma la forza bruta ha complessità **super-polinomiale**, quindi "non la scalfisco minimamente". È un buon esempio del rapporto tra **complessità computazionale e scalabilità**: il parallelismo abbassa le costanti, non cambia la classe di complessità. Il passaggio da **multi-core** a **many-core** (GPU con migliaia di core più semplici) è uno dei motivi del successo delle GPU (`LSD-05 @ 01:14:52`–`01:15:58`).
**Lezione extra: SIMD dentro un core** (`Teams Extra-2 @ 0:49:08`–`1:05:59`). Ogni core ha istruzioni **vettoriali** (SSE, AVX, AVX-512) che operano su vettori invece che su scalari, **senza bisogno di multithreading**. Per usarle bisogna **compilare per la CPU su cui si gira**, perché le librerie distribuite in binario usano il minimo comune denominatore. È uno dei vantaggi di Julia, che compila per la CPU disponibile (capitolo 07).
<callout icon="⚠️">
	**Correzione.** Il SIMD non è solo delle GPU: comprende le estensioni vettoriali dentro un singolo core; le GPU sono più precisamente SIMD/SPMD (NVIDIA parla di SIMT). Per il MISD in letteratura si citano i sistemi ridondanti *fault-tolerant*, come i computer di volo dello Space Shuttle, e il suo esempio della forza bruta è più naturalmente SIMD (stessa operazione, chiavi diverse). **AVX-512 non vuol dire 512 operazioni in parallelo** (`Teams Extra-2 @ 0:55:50`): 512 è la larghezza in bit del registro, che contiene 8 double o 16 float; lo speed-up teorico è il numero di elementi, e in pratica meno. Nell'assembly `vaddsd` è un'addizione **scalare** (`sd` = *scalar double*), la vettoriale è `vaddpd`; la `v` indica la codifica VEX. OpenMP e MPI sono modelli **SPMD** (*single program, multiple data*), non strettamente classificabili in Flynn (`008_OpenMP` p8).
</callout>
## 4. Memoria condivisa e memoria distribuita
**Slide MDA5 p21–p22.** Nei sistemi a **memoria condivisa** più CPU o core accedono alla stessa memoria; nei sistemi a **memoria distribuita** ogni CPU ha una memoria locale inaccessibile alle altre e si comunica in rete.
**Docente** (`LSD-05 @ 01:22:37`–`01:37:34`).
- **Memoria condivisa** = un PC multicore o un server con più socket e terabyte di RAM: "fa rima" con **multithreading**, perché tutti vedono la stessa memoria.
- **Memoria distribuita** = calcolatori collegati in rete: fa rima con **multiprocessing**. Più calcolatori con una rete ad alte prestazioni (tanta banda, poca latenza) formano un **cluster**.
- **Perché complicarsi la vita?** Perché esistono problemi che "sul mostro non fittano": quando anche la macchina più potente acquistabile non basta, non si può più fare **scale up** (verticale) e si deve fare **scale out** (orizzontale). "Non ho scelta".
- **Analogia della festa:** gli amici sono troppi per una sala, quindi si affittano quattro sale da ballo collegate da video wall. "Non c'era una sala adeguata per tutti: questo si chiama problema di scalabilità".
- **Guasti** (`LSD-05 @ 01:43:38`–`01:47:04`): se si rompe una macchina a memoria condivisa si ferma tutto e si spera nei checkpoint; in un sistema distribuito "si sa che le cose si rompono" (su 100 nodi qualche disco si guasta in pochi mesi) e il **coordinatore** riassegna a un altro nodo la parte del nodo guasto. L'architettura distribuita è più scalabile e più robusta ai guasti.
**Lezione extra** (`Teams Extra-2 @ 0:13:39`–`0:27:11`). I due approcci sono "profondamente diversi anche se sembrano simili": in memoria condivisa non si copiano dati tra le unità di calcolo; in memoria distribuita i dati vanno spezzati e spediti, e c'è "l'**elefante nella stanza**, la rete". Linguaggi e strumenti: OpenMP, Pthreads, Rust e Julia per la memoria condivisa; MPI e Julia distribuito per il cluster.
<callout icon="⚠️">
	**Correzione.** "In un'architettura a memoria distribuita il multithreading non lo posso fare" (`LSD-05 @ 01:29:01`): nella pratica HPC si usa il modello **ibrido**, MPI tra i nodi e OpenMP o thread dentro ogni nodo (il docente lo precisa a `01:36:08`). "4 socket da 256 core" (`LSD-05 @ 01:23:10`): gli AMD EPYC supportano al massimo 2 socket; configurazioni a 4 o 8 socket esistono con Intel Xeon, con meno core per socket.
</callout>
> **Nota aggiunta — scale-up o scale-out per la data science (Questionario 1, domanda 5):** la regola pratica è **scale-up finché regge**. Su un nodo solo non c'è rete, i dati stanno in RAM, il modello di programmazione è più semplice (thread, librerie vettorizzate, una GPU) e molti dataset reali ci stanno comodamente. Lo scale-out diventa necessario quando i dati o il modello non entrano in un nodo, quando serve tolleranza ai guasti o throughput oltre il limite di una macchina; il prezzo è la comunicazione (Amdahl si aggrava) e la complessità (partizionamento, coordinamento). Framework come Spark e Dask, e MPI nell'HPC, nascondono parte di questa complessità. Il docente, in più lezioni, argomenta la stessa gerarchia: prima si sfrutta bene la singola macchina, poi si distribuisce "quando non ce la fate più" (`Teams 5 @ 0:52:39`).
## 5. Misurare la scalabilità
**Quattro tipi di scalabilità** (`LSD-05 @ 01:46:23`–`01:48:09`), "i quattro concetti da tenere a mente":
- **strong scalability**: risolvere lo **stesso problema in meno tempo**;
- **weak scalability**: risolvere **nello stesso tempo problemi più grandi**;
- **scalabilità verticale** (scale up): sostituire l'hardware con uno più potente;
- **scalabilità orizzontale** (scale out): invece di 10 PC ne metto 100.
**L'esempio delle previsioni del tempo** torna in tre lezioni (`LSD-05 @ 01:09:06`–`01:12:24`; `LSD-07 @ 00:33:06`–`00:35:30`; `Teams Extra-1 @ 0:29:06`–`0:30:14`). Se il calcolo delle previsioni di domani dura 48 ore su un core è inutile; con 4 core 12 ore, con 8 core 6 ore: è **strong scaling**. Se invece voglio previsioni migliori usando i dati di tutta Europa invece che della sola Italia, nello stesso tempo utile, è **weak scaling**. Nella lezione extra del 28/04 l'esempio di strong scaling è l'attacco a forza bruta a un cifrario ("da vent'anni a 20 minuti"), quello di weak scaling la meteo che deve essere pronta per il telegiornale della sera.
**Lezione extra: le formule** (`Teams Extra-1 @ 0:13:51`–`0:39:00`).
- **Speedup:** S(p) = T(1) / T(p). In pratica S(p) \< p; a volte si osserva uno speedup **superlineare** (S(p) \> p), dovuto a effetti di cache o a una suddivisione dei dati che sfrutta meglio la gerarchia di memoria. "Il livello di scalabilità è dato dal massimo speedup che riusciamo a ottenere".
- **Legge di Amdahl:** se una frazione α del programma non è parallelizzabile, T(p) = α·T(1) + (1−α)·T(1)/p, e per p → ∞ lo speedup tende a **1/α**. Con il 10% seriale e 20 secondi di esecuzione non si scende sotto i **2 secondi**, qualunque sia il numero di core. Una parte seriale c'è sempre, per l'I/O e per la **consistenza dei dati**.
- **Strong scaling efficiency:** E(p) = S(p)/p = T(1) / (p·T(p)), misurata per diversi p; il grafico "è un riflesso della legge di Amdahl".
- **Weak scaling efficiency:** E(p) = T(1)/T(p), con il lavoro **per processore** costante. Attenzione alla complessità: per un prodotto di matrici O(n³), raddoppiando i processori non si può raddoppiare n; bisogna scegliere n_p = c·∛p perché il lavoro per processore resti costante. È un collegamento diretto tra **complessità computazionale e scalabilità** (Questionario 1, domanda 6).
- **Misurare il tempo giusto:** lo speedup si misura con il **wall-clock time** ("con un orologio esterno"), non con il tempo CPU: con 24 core pieni il tempo CPU è circa 24 volte quello reale. In C quindi non `clock()`.
**Docente, la pratica** (`LSD-07 @ 00:11:34`–`00:12:46`, `00:29:48`–`00:33:06`). Con la regola del trapezio in OpenMP: 1 thread 0,01 s, 2 thread 0,008 s, 4 thread ancora meno, poi il tempo **non scende più**: "la mia scalabilità forte è limitata" e "ci sono delle leggi" per stimarlo. Dove intervenire? **Nei cicli**, dove il calcolo passa la maggior parte del tempo, tipicamente un ciclo per dimensione del dato: "parallelo fa rima con prestazioni, che fa rima con scalabilità".
<callout icon="⚠️">
	**Correzione.** Nel trapezio lo speedup da 1 a 2 thread è solo 0,01/0,008 = **1,25**, efficienza 62%: con tempi dell'ordine dei millisecondi pesano la creazione e la gestione dei thread, oltre ad Amdahl. **T(1)** (`Teams Extra-1 @ 0:14:11`): lo speedup *relativo* usa il programma parallelo eseguito con un thread, quello *assoluto* il miglior programma seriale; di solito il primo è più lento, quindi lo speedup relativo sovrastima. **"200 volte più veloce"** con 100 processori (`Teams Extra-1 @ 1:47:32`): lo speedup ideale è 100. **`clock()`** non misura "la corrente utilizzata": restituisce il tempo CPU del processo, sommato su tutti i thread; per il wall-clock si usano `clock_gettime(CLOCK_MONOTONIC)`, `omp_get_wtime()` o `MPI_Wtime()`. "Strong e weak si ottengono col multithreading nel 99% dei casi" (`LSD-05 @ 01:12:58`): il weak scaling è anzi il regime tipico dei cluster MPI.
</callout>
> **Nota aggiunta — Amdahl e Gustafson:** Amdahl vale a **problema fisso** (strong scaling) ed è pessimista: con α = 5% lo speedup massimo è 20, anche con mille core. La **legge di Gustafson** (1988) guarda al weak scaling: se con p processori si risolve un problema p volte più grande e la parte seriale resta costante in tempo assoluto, lo speedup *scalato* è S(p) = p − α·(p − 1), quasi lineare. Le due leggi non si contraddicono: rispondono a domande diverse, ed è per questo che i supercalcolatori si usano soprattutto per risolvere problemi più grandi, non gli stessi problemi più in fretta. Nella pratica si aggiunge l'overhead di comunicazione e sincronizzazione, che cresce con p e può far *peggiorare* il tempo oltre un certo numero di thread (capitolo 06).
## 6. Pthreads
**Slide MDA5 p34–p62.** Le **POSIX Threads** (standard IEEE POSIX 1003.1c, 1995) sono l'API di basso livello per i thread: `pthread.h`, flag di compilazione `-lpthread`, circa 100 procedure con prefisso `pthread_` in quattro categorie: gestione dei thread, lock (**mutex**), monitoraggio (variabili di condizione), sincronizzazione. Permettono di personalizzare tutto al prezzo di una sintassi complessa (p43). L'esempio `pthreads-hello.c` crea 5 thread con `pthread_create`, ognuno stampa il proprio numero (p51). Quattro esecuzioni danno quattro ordini diversi (p55). Considerazioni (p62): i thread sono **creati in sequenza** dal master ma **non eseguiti in sequenza**; alcuni possono terminare prima che altri vengano creati; non si sa dove girano (a turno su un core o in parallelo su più core); **accedono alle stesse aree di memoria**.
**Docente.** Nel portale i Pthreads sono saltati: meccanismo "a bassissimo livello", mostrato solo per far capire perché i thread "non vengono mai gestiti direttamente da codice C" (`LSD-06 @ 01:00:48`–`01:02:32`; `LSD-07 @ 00:00:42`–`00:01:22`). Nella lezione extra del 30/04 il giudizio è ancora più netto: "**sconsigliatissimo**", la probabilità di introdurre deadlock e race condition "è altissima" e si rischia di andare più lenti; "non utilizzate mai pthreads in C nudo per qualcosa di più di questa demo". Pthreads contro OpenMP è come "andare a piedi e andare in macchina" (`Teams Extra-2 @ 1:32:46`–`1:38:02`).
> **Nota aggiunta:** nell'esempio della slide il `main` termina con `pthread_exit(NULL)`, che aspetta la fine degli altri thread; con un semplice `return` il processo terminerebbe uccidendo i thread ancora attivi. Il modo esplicito è `pthread_join`. Anche l'**output** dei thread su stdout può mescolarsi: le quattro esecuzioni della slide mostrano solo una parte dei possibili interleaving.
## 7. OpenMP
**Slide MDA5 p63–p98.** **OpenMP** (*Open Multi-Processing*) è un insieme di **direttive di compilazione, routine di libreria e variabili d'ambiente** per C, C++ e Fortran. Serve a parallelizzare in fretta con modifiche minime, flag `-fopenmp`, direttive `#pragma`, stesso codice per la versione seriale e parallela; offre meno personalizzazione dei Pthreads, **gira in modo efficiente solo su piattaforme a memoria condivisa** e **manca una gestione affidabile degli errori** (p72). Concetti (p82):
- creazione dei thread: `#pragma omp parallel`;
- *work-sharing*: `omp for`, `omp single`, `omp master`, `omp section`;
- clausole di condivisione: `shared`, `private`, `reduction`;
- sincronizzazione: `critical`, `atomic`, `ordered`, `barrier`, `nowait`;
- scheduling dei cicli: `static`, `dynamic`, `guided`.
L'esempio `openMP-hello.c` (p92): `#pragma omp parallel private(tid) reduction(+:sum)`, ogni thread legge il proprio `tid` con `omp_get_thread_num()`, il thread 0 stampa `omp_get_num_threads()`, e `sum += tid` viene sommato correttamente grazie alla `reduction` (con 4 thread dà sempre 6). Il numero di thread si fissa con `export OMP_NUM_THREADS=` (p98).
**Slide 008_OpenMP (Marzolla).** Più approfondite, e utili come riferimento:
- **modello fork-join** (p9): si parte con un solo thread (master); a ogni regione parallela il master crea un team di thread, alla fine c'è una **barriera implicita** e si torna al solo master;
- numero di thread (p11–p16): dipende dall'implementazione; si controlla con `OMP_NUM_THREADS`, la clausola `num_threads()` o `omp_set_num_threads()`; `omp_get_wtime()` per misurare il tempo (p19);
- **scope delle variabili** (p21–p30): `shared` è il default; `private` crea copie non inizializzate; `firstprivate` le inizializza con il valore di prima; `default(none)` obbliga a dichiarare tutto;
- **regola del trapezio** (p31–p44): problema *embarrassingly parallel*. Prima versione con `partial_result[t]` per thread sommati dal master; seconda con variabile locale e `#pragma omp atomic` sull'aggiornamento globale; terza con `reduction(+:result)`; infine `#pragma omp parallel for reduction(+:result)`;
- **reduction** (p38–p42): operatore binario **associativo**; una copia privata per thread inizializzata con l'elemento neutro, combinata alla fine;
- **dipendenze tra iterazioni** (p46–p48): `parallel for` è scorretto se un'iterazione dipende da un'altra (esempio del calcolo di π con `factor` alternato, corretto rendendo `factor` privato e calcolato da `k`); test rapido: se il ciclo eseguito al contrario resta corretto, *forse* è parallelizzabile;
- **scheduling** (p49–p54): `static` per lavoro prevedibile, `dynamic` o `guided` per lavoro irregolare (Mandelbrot); la dimensione ottimale del chunk si misura; `collapse` per cicli annidati (p55–p62);
- **sincronizzazione** (p73–p75): `barrier`, `master`, `single`;
- **task** (p77–p90): per strutture non a ciclo, come liste concatenate o Fibonacci ricorsivo; attenzione allo scope (una variabile `shared` può cambiare prima che il task parta).
**Docente** (`LSD-06 @ 01:02:32`–`01:11:03`, `01:20:25`–`01:22:38`).
- OpenMP è "forse il più usato" per scrivere codice parallelo partendo dal seriale: si aggiunge `-fopenmp` e si ottiene codice multithread con thread gestiti automaticamente. "L'opzione più rapida e performante nei sistemi a memoria condivisa".
- `#pragma omp parallel` apre un blocco in cui sono attivi i thread; `#pragma omp for` è "il costrutto più importante" e dà grandi speedup "a meno che non ci sia un legame tra i risultati di un'iterazione e la successiva". OpenMP gestisce creazione, distruzione e raccolta dei risultati.
- Ma **"OpenMP non vi risolve i problemi di race condition"**: la correttezza della parallelizzazione è lasciata al programmatore. "Probabilmente molte delle library che usate sono scritte in OpenMP".
**Docente** (`LSD-07 @ 00:00:09`–`00:13:20`, `00:27:14`–`00:28:23`). "C più OpenMP" è la scelta più adeguata per avere in modo semplice una certa scalabilità, "fino a un certo punto": non controlla gli errori di parallelizzazione e non garantisce che il codice sia più veloce del seriale. Poi la regola del trapezio con `OMP_NUM_THREADS`. In OpenMP basta "una riga" dove in MPI ne servono diverse.
**Lezione extra** (`Teams Extra-2 @ 1:38:02`–`1:48:50`). Si parallelizza codice esistente con poco sforzo; "parallelizzare un ciclo for è triviale". L'esempio con `reduction(+:sum)` sui thread ID mostra che "sono bastati due pragma". Compilazione `gcc -fopenmp`. "Resta basato su C, quindi non particolarmente safe" e non si può usare in un notebook. "I due che preferisco e che sono più scalabili, di quelli visti, sono **Julia e OpenMP**".
<callout icon="⚠️">
	**Correzione.** **OpenMP e MPI non sono linguaggi** "derivati dal C" (`LSD-06 @ 01:02:32`, `01:05:28`; `LSD-07 @ 00:13:20`): OpenMP è un'API di direttive, routine e variabili d'ambiente; MPI è lo standard di una libreria di scambio messaggi con implementazioni come OpenMPI e MPICH. "OpenMP è il meglio per sistemi a memoria distribuita" (`LSD-06 @ 01:06:04`) è un lapsus: p72 dice il contrario. **`omp single`**** e ****`omp master`**** non sono sincronizzazione** (`LSD-06 @ 01:10:25`): sono costrutti di *work-sharing*; per proteggere dati condivisi servono `critical`, `atomic` o `reduction`. **`omp parallel`**** non crea "tutti i thread possibili"**: il default dipende dall'implementazione (di solito i core logici) e si controlla. **Trapezio con solo ****`omp parallel`** (`LSD-07 @ 00:09:12`): così ogni thread rifarebbe l'intero calcolo e l'accumulo su `result` sarebbe una race; servono la divisione degli intervalli e `atomic` o `reduction`, come nelle slide p35–p38. `OMP_NUM_THREADS` è una **variabile d'ambiente**, non una direttiva. **"OpenMP gestisce automaticamente le SIMD; ****`gcc -fopenmp`**** produce un eseguibile già ottimizzato per la vostra macchina"** (`Teams Extra-2 @ 1:41:33`, `1:45:51`): `-fopenmp` abilita solo i pragma; la vettorizzazione la fa il compilatore con `-O2`/`-O3`, e per usare le istruzioni della propria CPU serve `-march=native`; OpenMP 4.0 offre `#pragma omp simd` per chiederla esplicitamente. Un comando ragionevole: `gcc -O3 -march=native -fopenmp prog.c -o prog`.
</callout>
## 8. MPI
**Slide MDA5 p99–p138.** **MPI** (*Message Passing Interface*) è un'API standard con più implementazioni (OpenMPI, MPICH); la comunicazione tra processi avviene di solito su socket TCP (o reti HPC). Si compila con `mpicc` (un wrapper di gcc) e si lancia con `mpirun -np 8 ./programma`: `mpirun` avvia i processi sui nodi della rete, ognuno è un programma che esegue per conto suo, e si può indicare quale host esegue cosa (p108). Concetti (p115):
- inizializzazione e chiusura: `MPI_Init`, `MPI_Finalize`;
- **comunicatori**, che raggruppano i processi per identificativo (*rank*) secondo una **topologia**: cartesiana, a grafo (`MPI_Cart`, `MPI_Graph`);
- **punto a punto**: `MPI_Send`, `MPI_Recv`, bloccanti e non bloccanti;
- **collettive**: `MPI_Bcast`, `MPI_Alltoall`, `MPI_Reduce`… (p120–p124, anche per l'I/O);
- **comunicazione one-sided**: `MPI_Put`, `MPI_Get`, `MPI_Accumulate`;
- tipi derivati: `MPI_INT`, `MPI_CHAR`, `MPI_DOUBLE`.
L'esempio `MPI-hello.c` (p134): il rank 0 manda "Hello i!" a ogni altro processo e poi riceve da ciascuno "task complete"; gli altri ricevono, stampano e rispondono. Quattro esecuzioni con `mpirun -np 4` mostrano ordini di stampa diversi (p138).
**Docente** (`LSD-06 @ 01:05:28`–`01:06:04`; `LSD-07 @ 00:13:20`–`00:28:23`).
- Tra calcolatori collegati in rete non si può condividere memoria: bisogna **inviare e ricevere messaggi**, "perché è quello che viaggia sulla rete". Serve quando il problema non scala su una macchina.
- La rete introduce ritardi: bisogna "studiare molto il problema" per **minimizzare gli scambi di dati tra nodi**.
- **Topologie** e **analogia del progetto di gruppo**: se ognuno può telefonare a chiunque la rete è totalmente connessa (distanza 1); se tutti parlano solo con il capo progetto è una stella; se si passa il messaggio in cerchio è un anello, con tempi alti "se non si fa attenzione".
- **Spettro della scalabilità** secondo il docente: a un estremo Python, all'altro MPI, in mezzo Java, OpenMP e Rust. MPI è "molto, molto, molto più complesso" ma dà **la massima scalabilità**; spesso lo si usa senza saperlo, lanciando da un notebook librerie scritte con MPI.
- **Non determinismo** e **analogia del questionario**: l'ordine dei risultati cambia a ogni esecuzione. Se i compiti sono indipendenti non importa, come gli studenti che consegnano il questionario in giorni diversi: conta che l'ultimo arrivi entro la scadenza. Il problema vero del calcolo altamente scalabile sono le **dipendenze**, quando per andare avanti bisogna aspettare qualcun altro, come in un progetto di coppia.
- In OpenMP basta un pragma; in MPI servono tre righe di inizializzazione, una `send` per distribuire il lavoro e una `receive` per raccogliere i risultati.
**Lezione extra.** In `Teams Extra-1 @ 1:57:40`–`2:12:40` la somma di un array in memoria distribuita mostra il collo di bottiglia del master e la *parallel reduction* (capitolo 06, §4).
<callout icon="⚠️">
	**Correzione.** "In MPI e in OpenMP c'è sempre un nodo master, il nodo zero, che distribuisce e raccoglie" (`LSD-07 @ 00:18:11`): in MPI il rank 0 fa da coordinatore per convenzione negli esempi, ma il modello non lo impone, e le collettive e la comunicazione one-sided sono simmetriche; in OpenMP il master thread non distribuisce il lavoro, lo fanno i costrutti di work-sharing. "MPI scala su milioni di nodi" (`LSD-07 @ 00:20:52`): i supercalcolatori più grandi hanno decine di migliaia di nodi, cioè milioni di *core* e di processi MPI. Lo **spettro** Python–MPI è un'immagine didattica: MPI (memoria distribuita) e OpenMP, Rust o Java (memoria condivisa) risolvono problemi diversi e si combinano.
</callout>
## 9. Osservare quello che succede: htop e dintorni
Il docente insiste su un'abitudine: quando si esegue codice, anche un notebook Python, **controllare quante risorse si usano davvero**, per capire se si può fare meglio (`LSD-07 @ 00:36:43`–`00:39:29`). **htop** mostra il carico per core, la memoria, lo swap, la CPU e la memoria per processo e per thread. Nella lezione extra del 30/04 racconta di aver scritto codice multithread con prestazioni "scandalosamente basse" e di aver scoperto con htop che **girava su un thread solo** (`Teams Extra-2 @ 1:28:18`–`1:32:46`). Alternative: **glances**, che mostra anche l'I/O. Altri strumenti e l'ambiente di lavoro sono nel capitolo 07.
<callout icon="⚠️">
	**Correzione.** Nella barra CPU di htop (modalità predefinita) il **verde** è tempo utente a priorità normale e il **rosso** tempo **kernel** (system), non "attesa dell'I/O" (`LSD-07 @ 00:38:19`; anche `LSD-06 @ 00:30:52`). L'I/O wait si vede solo attivando la modalità dettagliata dei contatori CPU, con un altro colore.
</callout>
## Collegamento con i questionari
Le domande del Questionario 5 sono nel capitolo 06. Qui i collegamenti per le domande che questo capitolo tratta in modo sostanziale.
<table header-row="true">
<tr>
<td>Domanda</td>
<td>Slide</td>
<td>Video</td>
<td>Qui</td>
</tr>
<tr>
<td>Q1.3 definire la scalabilità (anche capitolo 01)</td>
<td>`MDA5` p10–p14</td>
<td>`LSD-05 @ 01:09:06`–`01:15:58`, `01:46:23`–`01:48:09`; `LSD-07 @ 00:33:06`–`00:35:30`; `Teams Extra-1 @ 0:07:41`, `0:13:51`–`0:28:05`</td>
<td>§5</td>
</tr>
<tr>
<td>Q1.4 esempi di scale-out e scale-up (anche capitolo 01)</td>
<td>`MDA5` p21–p22, p72, p108</td>
<td>`LSD-05 @ 01:22:37`–`01:37:34`; `LSD-06 @ 00:32:36`–`00:33:41`; `LSD-07 @ 00:13:20`–`00:15:22`; `Teams Extra-1 @ 1:57:37`–`1:58:40`; `Teams Extra-2 @ 0:16:02`–`0:27:11`</td>
<td>§4</td>
</tr>
<tr>
<td>Q1.5 scale-out o scale-up per la data science</td>
<td>`MDA5` p21–p22, p108</td>
<td>`LSD-05 @ 01:33:53`–`01:37:34`, `01:43:38`–`01:47:04`; `LSD-06 @ 00:50:02`–`00:50:33`; `LSD-07 @ 00:13:57`–`00:15:22`, `00:18:42`–`00:21:29`; `Teams 5 @ 0:52:39`–`0:53:46`; `Teams Extra-2 @ 0:46:03`–`0:48:01`</td>
<td>§4 (nota)</td>
</tr>
<tr>
<td>Q1.6 complessità computazionale e scalabilità (anche capitolo 01)</td>
<td>nessuna specifica</td>
<td>`LSD-05 @ 01:20:41`–`01:21:47`; `LSD-07 @ 00:31:35`–`00:33:06`; `Teams Extra-1 @ 0:33:28`–`0:34:30`</td>
<td>§3, §5</td>
</tr>
<tr>
<td>Q5.3 perché la concorrenza è diventata il meccanismo principale di scaling (anche capitolo 06)</td>
<td>`MDA5` p2–p14; `MDA21` p5</td>
<td>`LSD-05 @ 00:46:15`–`00:55:22`; `LSD-06 @ 00:32:36`–`00:35:55`; `Teams 4 @ 2:15:25`–`2:24:46`, `2:35:18`–`2:37:29`; `Teams Extra-1 @ 0:10:05`–`0:11:05`; `Teams 5 @ 1:29:31`</td>
<td>§1</td>
</tr>
</table>
## Punti incerti della trascrizione
- `LSD-05 @ 00:51:20` — "dal 2020 in poi, diciamo anche dal 2000": il plateau è di metà anni 2000
- `LSD-05 @ 01:20:41` — il docente si corregge tra MISD e SIMD nell'esempio della forza bruta
- `LSD-06 @ 00:57:34` — "activation registries" è il testo della slide p33, di significato poco chiaro
- `LSD-07 @ 00:22:41` — intervento dello studente mal trascritto
- `LSD-07 @ 00:26:12` — "OpenMPI" detto al posto di "OpenMP e MPI"
- `LSD-07 @ 00:32:36` — "su una matrice un ciclo": per una matrice servono due cicli annidati, uno per dimensione
- `Teams Extra-1 @ 0:36:00` — trascritto "work lock time": è *wall-clock time*
