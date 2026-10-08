# 06 - Scalabilità e data race

> Fonte Notion: https://app.notion.com/p/3dd12abc808d8102a0e5ef76889de4f8 — ultima modifica 2026-09-17T09:21:35.601Z

Fonti: slide `MDA21ScalabilityandDataRaces` (25 pagine), `ChiarissimoDataRaceVsRaceCondition` (3), `Race-condition-Wikipedia` (8), `Deadlock-Wikipedia` (5), `design-of-parallel-programs` (22; Moreno Marzolla, Università di Bologna); lezioni `LSD-06` (01:11:03 → fine), `LSD-07` (00:05:42 → 00:06:12, 00:21:29 → 00:27:14, 00:42:41 → fine); edizione 2026: `Teams 5` (24/04/2026, 0:56:16 → 1:05:52 e 1:27:19 → fine), `Teams Extra-1` (28/04/2026, 0:39:00 → 2:12:40).
Il capitolo chiude il modulo di I livello e contiene il nucleo del Questionario 5. La tesi del docente, e delle slide MDA21, è che **i data race non sono semplici bug ma il sintomo di un limite di scalabilità**: aggiungere thread aumenta gli interleaving, quindi la probabilità di errore; la sincronizzazione che corregge l'errore serializza, quindi limita lo speedup. MDA21 non è commentata nelle lezioni del portale: è materiale nuovo dell'edizione 2026, presentato in `Teams 5`. Nel portale il tema è trattato attraverso la race condition (`LSD-06`, `LSD-07`).
## 1. Race condition
**Slide Race-condition-Wikipedia p1–p2.** Una **race condition** (*race hazard*) è la condizione di un sistema elettronico o software in cui il comportamento dipende dalla **sequenza o dal tempo di eventi non controllabili**, con risultati inattesi o inconsistenti; diventa un bug quando uno dei comportamenti possibili è indesiderato. Il termine è del 1954 (tesi di Huffman sui circuiti). Nei circuiti logici nasce da ritardi di propagazione diversi; nel software, quando più percorsi di codice eseguono insieme e l'esito dipende da quale arriva prima. Tra gli esempi celebri, la macchina per radioterapia Therac-25 (p6).
**Docente** (`LSD-06 @ 01:11:03`–`01:20:25`). Esempio del **conto corrente**: saldo 100, il thread T1 accredita +2, il thread T2 addebita −1.
<table header-row="true">
<tr>
<td>Scenario</td>
<td>Sequenza</td>
<td>Saldo finale</td>
</tr>
<tr>
<td>corretto</td>
<td>T1 legge 100, scrive 102; poi T2 legge 102, scrive 101</td>
<td>**101**</td>
</tr>
<tr>
<td>aggiornamento perso (1)</td>
<td>T1 e T2 leggono 100; T1 scrive 102; T2 scrive 99</td>
<td>**99**: sparisce il bonifico</td>
</tr>
<tr>
<td>aggiornamento perso (2)</td>
<td>T1 e T2 leggono 100; T2 scrive 99; T1 scrive 102</td>
<td>**102**: sparisce il prelievo</td>
</tr>
</table>
A seconda dello scheduling, che non controlliamo, il risultato è corretto o sbagliato. "Soprattutto il problema è **modificare**". La race condition "è il rischio principale quando utilizzo il multithreading o il calcolo distribuito per aumentare la scalabilità".
**Docente** (`LSD-07 @ 00:42:41`–`00:44:31`).
- **Analogia della consegna:** i progetti di Tizio e Caio sono indipendenti, l'ordine non conta; ma se hanno **lo stesso nome file** e finiscono nella stessa cartella, chi arriva dopo sovrascrive l'altro. "Questo è esattamente una race condition": il risultato dipende da chi ha iniziato prima o dopo.
- **Analogia aritmetica:** "4 + 4 deve sempre fare 8"; con una race condition "4 + 4 a volte non fa 8".
**Edizione 2026** (`Teams 5 @ 1:38:30`–`1:39:34`). Una race condition è una situazione con più flussi di esecuzione in cui non so quale arriva prima a leggere o scrivere una variabile. Questo introduce **non determinismo**, che di per sé non è un male: le stampe di un programma multithread escono in ordine diverso a ogni esecuzione. Il problema nasce quando il non determinismo tocca la **correttezza** del risultato.
<callout icon="⚠️">
	**Correzione.** "In Java, con un minimo di sforzo, la race condition si risolve" (`LSD-06 @ 01:19:52`–`01:20:57`): Java offre la sincronizzazione ma non impedisce le race a priori; va usata correttamente, e anche con tutte le classi thread-safe si possono avere race condition logiche (per esempio un *check-then-act* su due chiamate separate). È Rust a garantire l'assenza di data race a compile time. "OpenMP è molto più veloce di Java" (`01:20:25`) è una generalizzazione senza dati.
</callout>
## 2. Data race
**Slide MDA21 p3.** Si ha un **data race** quando:
1. **due o più contesti di esecuzione concorrenti** accedono alla **stessa locazione di memoria**;
2. **almeno uno degli accessi è una scrittura**;
3. **gli accessi non sono ordinati da un meccanismo di sincronizzazione**.
**Slide Chiarissimo p1–p3** (una risposta su Stack Overflow). La distinzione tra data race e race condition:
- il **data race** riguarda accessi *conflittuali* e **non sincronizzati** alla stessa locazione, a livello di semplici load e store in memoria. L'ordine di quegli accessi non si può ragionare: con pipeline fuori ordine, speculazione, cache multilivello e multicore può succedere di tutto, per esempio che due scritture concorrenti lascino metà parola di ciascuna. Per questo i linguaggi di basso livello definiscono il data race come **comportamento indefinito**;
- la **race condition** è un comportamento **indeterminato ma ben definito**: gli accessi sono sincronizzati, quindi il loro ordine si può ragionare, ma l'esito dipende comunque da quale ordine si verifica;
- per questo Java e C++ definiscono un proprio **modello di memoria**. Un linguaggio che rendesse ordinato ogni accesso alla memoria non avrebbe data race, ma potrebbe avere race condition;
- conclusione: si può considerare il data race un caso speciale di race condition, e la frontiera tra i due dipende da dove si mette il confine tra comportamento indefinito e comportamento definito ma indeterminato (oggi, l'interfaccia tra linguaggio e processore).
La pagina Wikipedia (p3–p4) aggiunge che non tutti considerano i data race un sottoinsieme delle race condition, e riporta la definizione del linguaggio Java: due accessi alla stessa variabile sono **conflittuali** se almeno uno è una scrittura, e un programma ha un data race se contiene due accessi conflittuali non ordinati da una relazione *happens-before*.
**Edizione 2026** (`Teams 5 @ 1:28:20`, `1:39:34`–`1:42:45`).
- Il data race accade quando due o più thread accedono alla stessa locazione, uno scrive, e l'accesso non è protetto; la probabilità cresce con il numero di thread.
- **Esempio della slide Chiarissimo:** due thread leggono, incrementano e scrivono una variabile globale. Sequenza corretta: 0 → 1 → 2. Sequenza sbagliata: entrambi leggono 0, entrambi calcolano 1, entrambi scrivono 1. Il risultato "semanticamente" dovrebbe essere 2: è un data race, "**il peggio che una race condition può dare**", perché produce risultati sbagliati.
- Con sincronizzazione o dentro una transazione i due thread vengono **isolati ed eseguiti in serie**, "al costo di perdere un po' di performance".
- Si può avere **non determinismo senza data race**: se tutti gli accessi alla memoria usano **operazioni atomiche**, l'ordine resta non deterministico ma si "è sempre nell'ambito della correttezza". "Ben vengano le operazioni atomiche".
**Lezione extra del 28/04, lo stesso errore nel codice** (`Teams Extra-1 @ 1:00:03`–`1:08:37`). Nella somma parallela di un array (§4), `sum += v[i]` sembra un'istruzione sola ma sono quattro passi: leggi `v[i]`, leggi `sum`, somma, scrivi `sum`. Nessuno garantisce che thread diversi li eseguano senza interruzioni. Con tre thread che leggono `sum = 0` e scrivono 1, 2 e 3, invece di 6 si ottiene 1, 2 o 3, a seconda di chi scrive per ultimo. È un **silent error**, "il peggiore errore che può succedere": corrompe il dato senza segnalare nulla.
> **Nota aggiunta — perché ciascuna delle tre condizioni è essenziale (Questionario 5, domanda 1):** basta togliere una condizione per eliminare il data race, ed è proprio così che funzionano le soluzioni. **(1) Più contesti concorrenti sulla stessa locazione:** se un solo thread accede al dato (dati **privati** per thread, *thread-local*, partizionamento, `private` in OpenMP, processi separati in MPI) non c'è nessuno con cui entrare in conflitto. **(2) Almeno una scrittura:** se tutti leggono, qualunque interleaving produce lo stesso risultato; i dati **immutabili** o in sola lettura scalano senza sincronizzazione, come osserva il docente per un dataset statico (`Teams 5 @ 1:02:43`–`1:04:52`). **(3) Nessun ordinamento imposto:** se un lock, un'operazione atomica, una barriera o una transazione ordina gli accessi, gli stati intermedi di un'operazione non sono visibili agli altri thread. Le tre condizioni corrispondono a tre strategie di progetto: **non condividere**, **non mutare**, **sincronizzare**; le prime due non costano scalabilità, la terza sì (§5). La regola di Rust "alias + mutabile = 💀" (capitolo 04) è la stessa definizione vista dal lato del linguaggio: il compilatore rifiuta la combinazione di (1) e (2) senza (3).
> **Nota aggiunta — data race e race condition sono indipendenti:** esistono data race *benigni* che non cambiano il risultato (per esempio due thread che scrivono lo stesso valore in un flag), ma in C e C++ restano comportamento indefinito; ed esistono race condition senza data race, come un saldo letto con un lock e aggiornato con un altro lock: ogni accesso è sincronizzato, ma tra lettura e scrittura un altro thread può intervenire. Per questo "usare classi thread-safe" non basta: bisogna rendere atomica l'intera operazione logica.
## 3. Deadlock
**Slide Deadlock-Wikipedia p1–p3.** Un **deadlock** è una situazione in cui nessun membro di un gruppo può procedere perché ciascuno aspetta un'azione di un altro, tipicamente il rilascio di un lock. Esempio classico: P1 ha la risorsa R2 e aspetta R1, P2 ha R1 e aspetta R2. Si verifica solo se valgono insieme le quattro **condizioni di Coffman** (1971):
1. **mutua esclusione**: almeno una risorsa è usabile da un solo processo alla volta;
2. **hold and wait**: un processo tiene almeno una risorsa e ne chiede altre;
3. **nessuna prelazione**: una risorsa si rilascia solo volontariamente;
4. **attesa circolare**: P1 aspetta P2, P2 aspetta P3, …, PN aspetta P1.
Le strategie: ignorarlo (se si dimostra che non accade), **rilevarlo** e risolverlo, **prevenirlo** rompendo una delle condizioni (soprattutto l'attesa circolare, imponendo un ordine gerarchico ai lock), **evitarlo** con algoritmi come quello del banchiere.
**Docente** (`LSD-07 @ 00:05:42`–`00:06:12`, `00:44:31`–`00:45:40`). I due problemi principali dei linguaggi multithread sono la race condition e il deadlock. La differenza: con una race condition "4 + 4 a volte non fa 8"; con un deadlock chiedo 4 + 4 e **la risposta non arriva mai**, perché il nodo 1 aspetta il nodo 2, che aspetta il 3, che aspetta il 4, che aspetta l'1: "una perenne **attesa circolare**". Analogia: in un progetto di coppia Tizio aspetta un'implementazione da Caio mentre Caio aspetta un'altra cosa da Tizio.
> **Nota aggiunta:** la race condition è un problema di **safety** (succede qualcosa di sbagliato), il deadlock di **liveness** (non succede niente). I due sono in tensione: più lock si aggiungono per evitare race, più aumenta il rischio di deadlock. Parenti stretti del deadlock: il **livelock** (i thread non sono bloccati ma continuano a cedersi il passo senza progredire) e la **starvation** (un thread non ottiene mai la risorsa). La prevenzione pratica più comune è acquisire i lock sempre nello **stesso ordine**. Safe Rust impedisce i data race ma **non** i deadlock. In MPI si ha deadlock quando due processi fanno una `MPI_Send` sincrona uno verso l'altro senza che nessuno riceva.
## 4. Progettare un programma parallelo: la somma di un array
**Slide design-of-parallel-programs p4–p16**, commentate passo per passo nella lezione extra del 28/04 (`Teams Extra-1 @ 0:39:00`–`2:12:40`). Nessuna domanda riguarda questo esempio in sé, ma è un'ottima illustrazione per le domande 1, 7, 8 e 9 del Questionario 5. Si parte dall'algoritmo sequenziale `for (i=0; i<n; i++) sum += v[i];` e lo si parallelizza su memoria condivisa. Le variabili che iniziano con `my_` sono private per processore, le altre condivise.
<table header-row="true">
<tr>
<td>Versione</td>
<td>Idea</td>
<td>Esito</td>
<td>Video</td>
</tr>
<tr>
<td>1 (p6)</td>
<td>blocchi di `n/P` elementi; ogni processore fa `sum += v[my_i]` sulla variabile condivisa</td>
<td>**sbagliata**: data race su `sum`</td>
<td>`Teams Extra-1 @ 0:42:04`–`1:08:37`</td>
</tr>
<tr>
<td>2 (p7–p8)</td>
<td>mutex intorno a ogni `sum += v[my_i]`</td>
<td>**ancora sbagliata**: con n = 17 e P = 3 la divisione intera dà blocchi da 5 e due elementi non vengono sommati</td>
<td>`1:08:37`–`1:13:47`</td>
</tr>
<tr>
<td>3 (p9)</td>
<td>partizione `my_start = (n*my_id)/P`, `my_end = (n*(my_id+1))/P`; mutex a ogni elemento</td>
<td>**corretta ma inefficiente**: blocchi da 5, 6, 6, ma troppa contesa sul mutex</td>
<td>`1:13:47`–`1:24:28`</td>
</tr>
<tr>
<td>4 (p10)</td>
<td>somma parziale in una variabile **locale** `my_sum`; mutex una sola volta alla fine</td>
<td>corretta, molta meno contesa</td>
<td>`1:37:42`–`1:40:54`</td>
</tr>
<tr>
<td>5 (p11–p12)</td>
<td>niente mutex: ogni processore scrive in `psum[my_id]`; il processore 0 somma tutte le `psum`</td>
<td>**sbagliata in modo sottile**: il master può sommare prima che gli altri abbiano finito</td>
<td>`1:40:54`–`1:53:20`</td>
</tr>
<tr>
<td>6 (p13)</td>
<td>come la 5, ma con una `barrier()` prima della somma globale</td>
<td>**corretta**</td>
<td>`1:54:20`–`1:57:40`</td>
</tr>
</table>
**Le analogie del docente** (`Teams Extra-1`).
- **Il traghetto** (`1:10:45`–`1:12:47`): molte persone possono salire da tante scalette, ma c'è **una sola cassa** o **una sola passerella**. Quel punto seriale è il mutex: la riga protetta è "la parte più cicciotta" del codice, e serializzarla "ammazza tutte le performance".
- **La biglietteria** (`1:17:40`–`1:24:28`): chi è alla cassa chiede il prezzo, cerca i contanti, aspetta il resto. È la α di Amdahl. La soluzione non è togliere la cassa ma **ridurre il tempo che ognuno ci passa**: solo carta, "bip", biglietto via email. "Principio fondamentale" della parallelizzabilità: il Δt nella parte seriale deve essere il più piccolo possibile.
- **Gli scout** (`1:47:32`–`1:53:20`): ognuno raccoglie foglie nel proprio sacco (versione 5); il capo scout, se è più veloce, carica sul camion i sacchi quando gli altri non li hanno ancora riempiti.
- **Il rifugio in montagna** (`1:55:26`): ai checkpoint ci si aspetta tutti, e chi arriva prima attende. La barriera è "una misura di safety" che costa tempo ma senza la quale "non ha senso andare avanti".
**Memoria distribuita** (slide p14–p15; `Teams Extra-1 @ 1:57:40`–`2:07:20`). Il master distribuisce i pezzi dell'array, ogni processo somma **sequenzialmente** i propri dati e manda il risultato al processo 0, che fa `for i = 1..P-1: receive from i`. Vantaggio: **non esistono variabili condivise**, quindi non ci sono data race. Svantaggio: il master è "**tartassato**" da P−1 messaggi che arrivano quasi insieme e li riceve in un ordine fisso, anche se i processi finiscono in ordine non deterministico. È "un errore di progettazione" che "impone una sequenzialità laddove non c'è": come un negozio con un solo commesso e cento clienti.
**Parallel reduction** (slide p16; `Teams Extra-1 @ 2:07:20`–`2:12:40`). I risultati si aggregano ad **albero**: al primo passo ogni processo pari somma il proprio risultato con quello del vicino, al secondo si combinano risultati a distanza 2, poi 4. Si fanno comunque P−1 somme, ma il processo 0 riceve circa **log₂ P** messaggi e fa circa log₂ P somme. Funziona solo per operazioni **associative** e "rende scalabile qualcosa che di solito non lo è". Il docente riprende lo schema nella lezione successiva (`Teams Extra-2 @ 0:17:00`).
**Task e data parallelism** (slide p17–p20, non commentate a lezione). Con il **data parallelism** si distribuiscono i dati e ogni processore esegue lo stesso compito su dati diversi; con il **task parallelism** si distribuiscono compiti, eventualmente diversi. Esempio: una tabella di temperature orarie (365 righe, 24 colonne) di cui calcolare minimo, massimo e media giornalieri: dividere le righe tra i processori è data parallel, assegnare a ciascun processore un calcolo diverso (minimo, massimo, media) è task parallel. Conclusione (p22): le architetture parallele richiedono paradigmi di programmazione paralleli, e scrivere programmi paralleli è più difficile che scriverne di sequenziali.
<callout icon="⚠️">
	**Correzione.** **"Aumentare la granularità del mutex"** (slide p10; `Teams Extra-1 @ 1:38:44`): nella versione 4 non si usano lock più fini (più lock su dati più piccoli), si **riduce il numero di acquisizioni**, cioè si accumula in locale e si entra nella sezione critica una volta sola; il lock diventa anzi *più grossolano* in termini di lavoro per acquisizione. **Versione 5 e false sharing:** `psum[]` è un array contiguo aggiornato a ogni iterazione; celle vicine stanno sulla stessa *cache line*, e ogni scrittura invalida la cache degli altri core. Meglio accumulare in una variabile locale e scrivere `psum[my_id]` una volta sola. **Ricezione in ordine fisso:** il tempo totale del master cambia poco (deve comunque aspettare il processo più lento) e per messaggi piccoli MPI bufferizza; il problema diventa serio con messaggi grandi, quando i mittenti restano bloccati, e con molti processi. Rimedi: `MPI_ANY_SOURCE`, ricezioni non bloccanti (`MPI_Irecv` + `MPI_Waitall`) o direttamente la collettiva `MPI_Reduce`, che usa schemi ad albero. **"Da complessità P a log₂ P"** (`Teams Extra-1 @ 2:10:38`): scendono a log₂ P il numero di passi e il carico del processo 0; il lavoro totale resta P−1 somme e P−1 messaggi. **"Monitor"** (`1:17:09`): la versione usa un mutex; un monitor è un mutex con variabili di condizione incapsulate, come `synchronized` in Java. **"Succede lo stesso in Julia, in Elixir"** (`1:45:45`): vale per Julia con thread a memoria condivisa; Elixir ed Erlang non condividono memoria tra processi, quindi non hanno data race (possono avere race condition sull'ordine dei messaggi).
</callout>
> **Nota aggiunta — le stesse versioni in OpenMP:** la versione 1 è `#pragma omp parallel for` con `sum` condivisa; le versioni 2–3 aggiungono `#pragma omp critical` dentro il ciclo; la versione 4 è `my_sum` privata e `critical` (o `atomic`) una volta per thread; le versioni 5–6 sono `psum[omp_get_thread_num()]` con la barriera implicita a fine regione. La soluzione idiomatica è **`#pragma omp parallel for reduction(+:sum)`**, che fa esattamente la versione 4 senza lock: una copia privata inizializzata a 0 per thread e una combinazione finale. La partizione bilanciata la fa `schedule(static)`. Lo stesso percorso è nelle slide `008_OpenMP` p35–p44 con la regola del trapezio (capitolo 05, §7).
## 5. Perché i data race sono un problema di scalabilità
**Slide MDA21 p4–p25**, presentate in `Teams 5 @ 1:28:20`–`1:36:53`. È l'ultimo set di slide del modulo e "fa parte delle domande dell'ultimo" questionario (`1:42:45`). Lo seguo nell'ordine delle slide.
### 5.1 La scalabilità è prestazioni più correttezza
**Slide p4.** Qui scalabilità significa soprattutto **scalabilità delle prestazioni**: aumentare il throughput o ridurre la latenza aggiungendo core, thread o nodi. Ma la scalabilità **non è solo una proprietà prestazionale**: è una **proprietà congiunta di prestazioni e correttezza**, e i data race stanno esattamente all'intersezione.
**Docente.** "Quant'è bello il multithreading", perché sfrutta tutti i core, "ma quanto è pericoloso, delicato" (`Teams 5 @ 0:56:16`). Il problema vero è il **dato modificabile**: su dati in sola lettura "la scalabilità ce n'è tanta", si possono fare tantissime cose in parallelo; con un conto in banca, un carrello, i dati di un paziente, quando più thread o processi accedono allo stesso dato servono **guardrail**: transazioni (tutto o niente, altrimenti rollback) e sincronizzazione (`Teams 5 @ 0:57:17`, `1:02:43`–`1:05:52`). Lo stesso concetto in `Teams 4 @ 0:47:04`: bisogna "scalare in maniera safe".
### 5.2 La concorrenza come meccanismo di scalabilità
**Slide p5–p6.** I sistemi moderni scalano con la concorrenza perché la frequenza di clock si è fermata a metà anni 2000, i miglioramenti arrivano soprattutto dal parallelismo multicore, e i carichi orientati al throughput beneficiano dell'esecuzione sovrapposta. Quindi **più core → più concorrenza → più interazione tra thread**, e ogni tentativo di scalare verticalmente con la concorrenza **aumenta il numero di interleaving** possibili. Le ragioni architetturali e storiche sono nel capitolo 05, §1.
**Docente** (`Teams 5 @ 1:29:31`). "L'aumento del numero dei core ha prodotto un aumento della concorrenza \[…\] quindi c'è maggiore interazione tra i thread", e questo dà un aumento di scalabilità "però limitato dall'interazione tra i vari thread".
### 5.3 Interleaving ed esplosione dello spazio degli stati
**Slide p7–p9.** Il numero di interleaving cresce in modo **combinatorio** con il numero di thread. I data race non sono bug accidentali: sono **proprietà emergenti** del fatto di scalare l'esecuzione. Con più concorrenza gli ordini di esecuzione crescono in modo esponenziale, ragionare o testare in modo esaustivo diventa impossibile, e **gli interleaving rari diventano statisticamente inevitabili**. Un sistema che sembra corretto con 2 thread può fallire sistematicamente con 64, non perché il codice sia cambiato ma perché lo spazio degli stati è cresciuto: **più scalabilità → più interleaving → più probabilità di race**.
**Docente** (`Teams 5 @ 1:29:31`–`1:30:33`, `1:47:11`). "Il numero delle possibili alternanze di accesso tra le attività dei thread cresce con il numero dei thread"; il data race "non è un baco ma un grande problema dovuto alla scalabilità": "un sistema che sembra corretto con un solo thread può avere problemi consistenti con 64". "Più siamo e più è la probabilità che il problema si verifichi". Nel portale lo stesso fenomeno si vede negli output delle esecuzioni ripetute (MDA5 p55, p98, p138; `LSD-06 @ 01:18:12`–`01:19:22`; `LSD-07 @ 00:21:29`–`00:22:41`).
> **Nota aggiunta — quanto crescono gli interleaving (domanda 4):** se n thread eseguono ciascuno k passi atomici, gli interleaving possibili sono (nk)! / (k!)\^n, i modi di mescolare n sequenze mantenendo l'ordine interno di ciascuna. Con 2 thread da 3 passi sono 20; con 4 thread da 3 passi 369.600; con 8 thread da 3 passi circa 3,7 × 10¹⁷. Nessun test può coprirli, ed è per questo che servono garanzie per costruzione (§5.7) o strumenti di rilevamento.
> **Nota aggiunta — perché corretto con 2 thread e rotto con 64 (domanda 5):** tre effetti si sommano. **(1) Probabilità:** se una singola operazione ha una probabilità minuscola p di cadere in una finestra di interferenza, su N operazioni la probabilità di almeno un errore è 1 − (1 − p)\^N; con p = 10⁻⁹ e 10⁹ operazioni è già circa 63%. Con 64 thread le operazioni concorrenti e le coppie di thread che possono interferire (circa n²/2: 1 con 2 thread, 2.016 con 64) crescono enormemente. **(2) Vero parallelismo:** con 2 thread su molti core le finestre di sovrapposizione sono rare, e su un core le interruzioni avvengono solo ai cambi di contesto; con 64 thread su 64 core le sovrapposizioni sono continue. **(3) Cambia la macchina:** più socket, NUMA, cache e scheduler diversi cambiano i tempi (§5.4). Un test che passa con 2 thread quindi non prova nulla.
### 5.4 Effetti di amplificazione del carico
**Slide p10–p11.** Scalare spesso significa **più richieste**, **accessi più frequenti allo stato condiviso** e **sezioni critiche più brevi eseguite più spesso**. Questo amplifica la sensibilità ai tempi: ritardi di coerenza delle cache, riordinamenti della memoria, decisioni dello scheduler. Per questo le race condition compaiono spesso **solo sotto carichi scalabili** e non nei test su piccola scala: empiricamente sono **guasti dipendenti dal carico**.
**Docente** (`Teams 5 @ 1:30:33`–`1:31:45`). Il data race "produce anche problemi sulla coerenza della memoria cache" quando ci sono tante modifiche di dati, con conseguenze "sulla gestione dell'ordinamento dei dati in memoria e sulle decisioni dello scheduler, \[…\] quindi potrebbe portare anche anomalie nelle performance". Un'illustrazione concreta di amplificazione del carico è il master "tartassato" di messaggi della somma distribuita (`Teams Extra-1 @ 2:01:58`–`2:07:23`).
> **Nota aggiunta — load amplification (domanda 6):** in un servizio poco carico due richieste che toccano lo stesso stato si sovrappongono raramente; aumentando il carico di 100 volte, le sovrapposizioni crescono più che linearmente, perché dipendono dalle *coppie* di richieste attive nello stesso intervallo. Inoltre il carico cambia i tempi: con code più lunghe e più cambi di contesto un thread viene sospeso proprio a metà della sequenza leggi-modifica-scrivi, la finestra di vulnerabilità si allunga, e i ritardi di propagazione tra le cache dei core fanno vedere a thread diversi versioni diverse dello stesso dato. È il motivo per cui questi errori emergono in produzione, nei *load test* o nei *chaos test*, e per cui gli strumenti di rilevamento (ThreadSanitizer per C, C++ e Go, il flag `-race` di Go, Helgrind di Valgrind) si usano insieme a test di stress.
### 5.5 La tensione tra sincronizzazione e scalabilità
**Slide p12–p14.** Per evitare i data race si introduce **sincronizzazione**: lock, mutex, operazioni atomiche, barriere, monitor. Ma la sincronizzazione costa: la **serializzazione** riduce il parallelismo, la **contesa** aumenta la latenza, l'**invalidazione delle cache** penalizza il throughput. Ne nasce una **tensione fondamentale**: togliere sincronizzazione migliora la scalabilità ma rischia data race; aggiungerla previene i data race ma limita la scalabilità. **Non è un problema di implementazione ma un limite teorico imposto dallo stato mutabile condiviso.**
**Docente** (`Teams 5 @ 1:31:45`–`1:33:46`). Serve un modo per "serializzare, per non parallelizzare gli accessi a determinate aree di codice": lock, mutex, istruzioni atomiche, sezioni critiche, barriere, disponibili in molti linguaggi (in Python non nativamente ma tramite librerie). Ma "il fatto che un solo thread alla volta possa accedere e modificare o leggere una variabile riduce il parallelismo". Bisogna **minimizzare i data race mantenendo il dato consistente, limitando il meno possibile il parallelismo**.
**Nei casi concreti.** Il traghetto e la biglietteria (§4); il GIL come caso limite di una sola regione sincronizzata per tutto l'interprete, che dà semplicità e correttezza al prezzo del parallelismo, e la sua rimozione, che darebbe parallelismo al prezzo di errori silenziosi nel codice esistente (`Teams 4 @ 0:28:53`–`0:37:57`; `LSD-05 @ 00:41:05`–`00:43:54`; capitolo 04, §3). La versione 5 della somma: togliendo anche la barriera il codice è più veloce ma sbagliato.
> **Nota aggiunta — i due lati della tensione (domande 7 e 8):** togliere un lock elimina attese e contesa, ma rende visibili a tutti gli stati intermedi: si torna ad aggiornamenti persi, invarianti violate, strutture dati corrotte, spesso senza alcun segnale. Aggiungere lock garantisce l'ordine ma crea code: per Amdahl la sezione serializzata limita lo speedup, la contesa aggiunge latenza che cresce con il numero di thread, e il continuo passaggio del lock tra core fa rimbalzare le linee di cache (*cache line bouncing*); con più lock aumenta anche il rischio di deadlock. Le vie d'uscita non eliminano la tensione, la aggirano riducendo lo stato mutabile condiviso: dati privati e riduzione finale (versione 4, `reduction`), dati immutabili, partizionamento dei dati per proprietario, strutture concorrenti a grana fine o *lock-free* basate su operazioni atomiche (compare-and-swap), copy-on-write, RCU, message passing.
### 5.6 Amdahl e le regioni serializzate
**Slide p15–p16.** Per la legge di Amdahl lo speedup è limitato dalla parte seriale. I data race obbligano a proteggere le sezioni critiche, serializzare gli accessi, introdurre lock globali o contesi. **Anche regioni sincronizzate piccole** limitano lo speedup massimo e **diventano dominanti su larga scala**. Quindi i data race limitano la scalabilità **anche quando sono corretti**, perché la correzione aumenta la serializzazione.
**Docente** (`Teams 5 @ 1:32:46`–`1:33:46`). La sincronizzazione ha "implicazioni di performance e di mancato parallelismo che si riversano sulla legge di Amdahl" (trascritto "legge di Han"), che serve a capire "qual è il limite di scalabilità di un'implementazione", un limite che "ne impedisce la parallelizzazione estrema". La formula e l'esempio del 10% seriale sono in `Teams Extra-1 @ 0:20:30`–`0:25:30` (capitolo 05, §5); la biglietteria è la stessa idea in forma di storia.
> **Nota aggiunta — perché una regione piccola diventa dominante (domanda 9):** con Amdahl, se la regione sincronizzata è l'1% del tempo, lo speedup massimo è 100; con 16 core si ottiene circa 13,9, con 64 circa 39, con 1.024 circa 91: la stessa regione che su pochi core era irrilevante mangia la maggior parte del guadagno. E Amdahl è ottimista, perché considera la parte seriale di durata fissa. Con molti thread un lock si **contende**: la regione dura l'1% del lavoro di un thread, ma se 64 thread la vogliono spesso, ognuno passa tempo in coda, e il tempo di attesa cresce con i thread. La **Universal Scalability Law** di Gunther modella i due effetti: C(N) = N / (1 + σ(N−1) + κN(N−1)), con σ la contesa (Amdahl) e κ il costo di **coerenza** tra coppie di thread (le "coherence traffic" di MDA21 p18). Con κ \> 0 il throughput raggiunge un massimo e poi **scende**: aggiungere thread peggiora. È quello che il docente osserva a voce con il trapezio ("a un certo punto il tempo non diminuisce più", `LSD-07 @ 00:12:07`).
### 5.7 Modelli di memoria e architettura
**Slide p17–p20.** Le architetture moderne usano modelli di memoria deboli, protocolli di coerenza delle cache ed esecuzione speculativa. Scalando, i ritardi di visibilità della memoria aumentano, il traffico di coerenza domina il tempo di esecuzione e le viste inconsistenti diventano più frequenti. I data race sfruttano proprio questi effetti: su larga scala il comportamento della memoria non è più intuitivo e il codice non sincronizzato mostra un non determinismo che **peggiora con il numero di core**. I data race violano le ipotesi su cui si reggono i sistemi di memoria scalabili.
Per questo i sistemi scalabili tendono a **minimizzare lo stato mutabile condiviso**, **partizionare la proprietà dei dati**, spostare il coordinamento verso il **message passing** o i **dati immutabili**. "Non è una preferenza stilistica": **lo stato mutabile condiviso introduce un tetto alla scalabilità, e i data race sono il sintomo di averlo raggiunto**. I sistemi senza race scalano meglio perché riducono sincronizzazione globale, traffico di coerenza e dipendenze tra thread.
### 5.8 Un problema di scalabilità, non solo un bug
**Slide p21–p22.** Dal punto di vista scientifico un data race indica **sincronizzazione insufficiente rispetto al livello di concorrenza**; aumentare le risorse rivela bug di correttezza latenti; **un sistema che funziona solo su piccola scala non è scalabile per definizione**. Un data race è la prova che l'argomento di correttezza del programma non scala con il modello di esecuzione.
### 5.9 Conseguenze per il progetto dei linguaggi
**Slide p23–p25.** Per questo molti linguaggi e paradigmi moderni **rilevano i race** staticamente o dinamicamente, **restringono l'aliasing e la mutazione condivisa**, trattano **l'assenza di race come proprietà di correttezza**. Scambiano flessibilità con una **scalabilità garantita della correttezza**. Riassunto: la scalabilità aumenta concorrenza e interleaving; più interleaving rendono i data race più probabili; prevenirli richiede sincronizzazione; la sincronizzazione limita le prestazioni parallele. **Un sistema non può scalare efficacemente se il suo modello di correttezza non scala con il suo modello di concorrenza.**
**Docente** (`Teams 5 @ 1:34:49`–`1:36:53`). "Uno dei modi più carini è utilizzare dei sistemi **race free**" invece di controllare a runtime. I data race e le race condition sono anche un **problema di sicurezza**, perché aprono vulnerabilità sfruttabili. "Parola finale": un sistema non può scalare in maniera efficace se il suo sistema di correttezza, di consistenza dei dati, non scala con la concorrenza; "i data race non sono semplicemente bug, ma indicano problemi di scalabilità".
> **Nota aggiunta — come i linguaggi moderni limitano lo stato mutabile condiviso (domanda 10):**
> - **Rust**: ownership e borrowing ("alias XOR mutabile") e i trait `Send` e `Sync` rendono i data race un **errore di compilazione**; lo stato condiviso passa da tipi espliciti come `Arc<Mutex<T>>`, e il `Mutex` possiede il dato (capitolo 04, §7).
> - **Erlang ed Elixir** (BEAM): **modello ad attori**, processi leggeri senza memoria condivisa, dati immutabili, comunicazione solo per messaggi; niente data race sulla memoria, e un processo che fallisce viene riavviato da un supervisore.
> - **Go**: goroutine e **channel** nello stile CSP ("non comunicare condividendo memoria; condividi memoria comunicando"), ma senza garanzie a compile time: c'è un rilevatore dinamico (`go test -race`).
> - **Linguaggi funzionali** (Haskell, Clojure, Scala con collezioni immutabili): **immutabilità per default**; dove serve stato mutabile, **Software Transactional Memory** (Haskell `STM`, Clojure `ref`), cioè transazioni in memoria come quelle del database che cita il docente.
> - **Java e C#**: non impediscono i race, ma definiscono un modello di memoria (*happens-before*) e offrono tipi immutabili (`record`), strutture concorrenti e, in Java, i *virtual thread*.
> - **Swift**: dalla versione 6 i data race tra *actor* e tipi `Sendable` sono verificati dal compilatore.
> - Nei **framework** vale lo stesso principio: Spark trasforma dati immutabili (RDD e DataFrame), MPI non ha memoria condivisa, e la *parallel reduction* combina solo risultati privati.
> Il prezzo, come dice la slide p23, è la flessibilità: più regole, curva di apprendimento più ripida, a volte copie di dati. Il guadagno è che la correttezza non va riverificata ogni volta che si aggiungono core.
## Collegamento con il Questionario 5
<table header-row="true">
<tr>
<td>Domanda</td>
<td>Slide</td>
<td>Video</td>
<td>Qui</td>
</tr>
<tr>
<td>1. data race e le tre condizioni necessarie</td>
<td>`MDA21` p3; `Chiarissimo` p1–p2; `Race-condition-Wikipedia` p2–p4; `design-of-parallel-programs` p6</td>
<td>`Teams 5 @ 1:28:20`–`1:29:31`, `1:38:30`–`1:42:45`; `Teams Extra-1 @ 1:00:03`–`1:08:37`; `LSD-06 @ 01:11:03`–`01:20:25`; `LSD-07 @ 00:42:41`–`00:44:31`</td>
<td>§1, §2 (perché ciascuna condizione è essenziale: nota)</td>
</tr>
<tr>
<td>2. scalabilità come proprietà congiunta di prestazioni e correttezza</td>
<td>`MDA21` p4, p21–p22, p25</td>
<td>`Teams 5 @ 0:56:16`–`0:57:17`, `1:02:43`–`1:05:52`, `1:35:50`–`1:36:53`; `Teams 4 @ 0:47:04`; `Teams Extra-1 @ 1:09:39`–`1:10:45`, `1:17:09`, `1:56:35`</td>
<td>§5.1, §5.8</td>
</tr>
<tr>
<td>3. perché la concorrenza è il meccanismo principale di scaling</td>
<td>`MDA21` p5–p6; `MDA5` p2–p14</td>
<td>`Teams 5 @ 1:29:31`; `Teams 4 @ 2:15:25`–`2:24:46`; `Teams Extra-1 @ 0:10:05`–`0:11:05`; `LSD-05 @ 00:46:15`–`00:55:22`</td>
<td>§5.2; capitolo 05 §1</td>
</tr>
<tr>
<td>4. più thread, più interleaving; data race come proprietà emergente</td>
<td>`MDA21` p6–p8; `MDA5` p55, p98, p138</td>
<td>`Teams 5 @ 1:29:31`–`1:30:33`; `Teams Extra-1 @ 1:07:34`–`1:08:37`; `LSD-06 @ 01:18:12`–`01:19:22`; `LSD-07 @ 00:21:29`–`00:22:41`</td>
<td>§5.3 (conteggio nella nota)</td>
</tr>
<tr>
<td>5. corretto con 2 thread, sbagliato con 64</td>
<td>`MDA21` p9</td>
<td>`Teams 5 @ 1:30:33`, `1:47:11`; `Teams 4 @ 0:33:40`–`0:34:41`</td>
<td>§5.3 (nota)</td>
</tr>
<tr>
<td>6. effetti di amplificazione del carico</td>
<td>`MDA21` p10–p11</td>
<td>`Teams 5 @ 1:30:33`–`1:31:45`; `Teams Extra-1 @ 2:01:58`–`2:07:23`</td>
<td>§5.4 (nota)</td>
</tr>
<tr>
<td>7. tensione fondamentale tra sincronizzazione e scalabilità</td>
<td>`MDA21` p12–p14</td>
<td>`Teams 5 @ 1:31:45`–`1:33:46`; `Teams Extra-1 @ 1:08:37`–`1:12:47`, `1:38:44`, `1:54:20`–`1:57:37`; `Teams Extra-2 @ 1:39:12`</td>
<td>§4, §5.5</td>
</tr>
<tr>
<td>8. togliere sincronizzazione migliora la scalabilità ma rischia la correttezza, e viceversa</td>
<td>`MDA21` p14</td>
<td>`Teams 5 @ 1:41:44`–`1:42:45`; `Teams Extra-1 @ 1:39:52`–`1:57:37`; `Teams 4 @ 0:31:43`–`0:34:41`; `LSD-05 @ 00:41:05`–`00:43:54`</td>
<td>§4, §5.5 (nota)</td>
</tr>
<tr>
<td>9. perché anche piccole regioni sincronizzate limitano la scalabilità</td>
<td>`MDA21` p15–p16</td>
<td>`Teams 5 @ 1:32:46`–`1:33:46`; `Teams Extra-1 @ 0:20:30`–`0:25:30`, `1:17:40`–`1:24:28`; `LSD-07 @ 00:12:07`–`00:12:46`</td>
<td>§5.6 (numeri e USL nella nota)</td>
</tr>
<tr>
<td>10. perché i linguaggi moderni limitano lo stato mutabile condiviso</td>
<td>`MDA21` p19–p20, p23; `MDA19` p10–p11; `RustLearningResources` p57–p58, p66–p88</td>
<td>`Teams 5 @ 1:34:49`–`1:35:50`; `Teams 4 @ 1:49:58`–`1:55:02`; `LSD-07 @ 00:41:01`–`00:42:41`; `Teams Extra-1 @ 1:58:40`</td>
<td>§5.7, §5.9 (nota)</td>
</tr>
</table>
## Punti incerti della trascrizione
- `LSD-06 @ 01:13:55`–`01:16:56` — la trascrizione a tratti dice "diminuito di 2": i valori 102 e 99 implicano +2 e −1
- `Teams 5 @ 1:32:46` — "legge di Han": è la legge di Amdahl
- `Teams 5 @ 1:40:43` — "thread 1 e thread 2" trascritti come "3 1 e 3 2"
- `Teams Extra-1` — i numeri delle versioni della somma non sono pronunciati; la corrispondenza con le slide è ricostruita dal contenuto
- `Teams Extra-1 @ 1:04:09` — "errato nella maggior parte dei casi": dipende da scheduling, numero di thread e lunghezza del ciclo; il punto è che l'esito non è deterministico
