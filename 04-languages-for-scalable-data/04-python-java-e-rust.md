# 04 - Python, Java e Rust

> Fonte Notion: https://app.notion.com/p/3dd12abc808d811c85a9d85a28f59ab5 — ultima modifica 2026-09-16T23:27:11.777Z

Fonti: slide `MDA16PythonvsJava` (30 pagine), `MDA19PythonVsRust` (14), `Java_vs_Rust` (21), `RustLearningResources` (156, E. Risa, Rust Roma Meetup); lezioni `LSD-05` (00:25:57 → 00:46:15, 01:37:34 → fine), `LSD-06` (00:00:10 → 00:43:51), `LSD-07` (00:28:23 → 00:29:48, 00:39:29 → 00:42:41); edizione 2026: `Teams 4` (23/04/2026).
Il capitolo confronta a coppie i linguaggi usati nel master (Python, Java) con quello che il docente presenta come alternativa "con maggiori garanzie" (Rust). Il filo conduttore è sempre lo stesso: **non esiste un linguaggio "one size fits all"**, e ogni scelta paga in un'altra dimensione (produttività, prestazioni, safety, scalabilità). Le slide MDA16 sono prese da un articolo di SnapLogic e da un post di Cardinal Peak su Cython e PyPy; MDA19 e Java_vs_Rust sono sintesi comparative.
<table header-row="true">
<tr>
<td>Tema</td>
<td>Slide</td>
<td>Portale</td>
<td>Edizione 2026</td>
</tr>
<tr>
<td>Python: design e ambiti</td>
<td>MDA16 p3–p7</td>
<td>`LSD-05 @ 00:25:57`–`00:38:42`; `LSD-06 @ 00:01:48`–`00:05:18`</td>
<td>`Teams 4 @ 0:17:14`–`0:27:00`</td>
</tr>
<tr>
<td>GIL</td>
<td>MDA16 p8–p13; MDA19 p8–p9, p12</td>
<td>`LSD-05 @ 00:38:42`–`00:46:15`, `01:37:34`–`01:43:38`</td>
<td>`Teams 4 @ 0:27:00`–`0:40:24`</td>
</tr>
<tr>
<td>Java</td>
<td>MDA16 p14–p19</td>
<td>`LSD-05 @ 01:48:09`–`01:57:46`; `LSD-06 @ 00:00:10`–`00:08:45`, `00:27:27`–`00:43:51`</td>
<td>`Teams 4 @ 0:40:24`–`0:50:16`</td>
</tr>
<tr>
<td>Prestazioni e compilazione di Python</td>
<td>MDA16 p20–p30</td>
<td>`LSD-06 @ 00:08:45`–`00:27:27`</td>
<td>`Teams 4 @ 1:29:27`–`1:38:16`</td>
</tr>
<tr>
<td>Rust vs Python</td>
<td>MDA19 p4–p14; RustLearningResources</td>
<td>`LSD-07 @ 00:28:23`–`00:29:48`, `00:39:29`–`00:42:41`</td>
<td>`Teams 4 @ 1:38:16`–`2:00:31`</td>
</tr>
<tr>
<td>Java vs Rust</td>
<td>Java_vs_Rust p1–p21</td>
<td>non commentate</td>
<td>non commentate</td>
</tr>
</table>
## 1. Python: che cos'è e a cosa serve
**Slide p3–p4.** Python è un linguaggio **interpretato**, **dinamicamente tipato**, **general purpose**, con sintassi pensata per la leggibilità. Punti di forza elencati: semplicità e leggibilità, versatilità (web, data analysis, ML, AI, calcolo scientifico, automazione), ecosistema di librerie, comunità. L'esempio è una web app Flask di poche righe.
**Docente** (`LSD-05 @ 00:25:57`–`00:38:42`). La domanda "a cosa serve Python?" ha una risposta sola: **Python è un linguaggio di scripting**. Serve a esprimere in poche righe un algoritmo di alto livello e a invocare funzionalità scritte altrove, come uno script di shell o un `.bat`, ma più potente e leggibile. Dire che "è utile per la data science" non risponde: Python serve a gestire la data science **ad alto livello**, perché le API e le librerie numeriche che usa **non sono scritte in Python**. È esattamente il modello del notebook: ogni cella ha poche righe, non un programma di 200. Quando lo si abusa con codice molto lungo, **non scala** come dimensione del codice: diventa difficile da mantenere.
- **Origine.** Nasce come linguaggio di scripting per il sistema operativo distribuito **Amoeba**: Guido van Rossum non era soddisfatto degli script di shell dell'epoca (`LSD-05 @ 00:30:26`–`00:31:46`).
- **Perché si è affermato.** Leggibilità, curva di apprendimento dolce ("molti scienziati non vogliono perdere tempo"), inerzia, tanto help online, uso diffuso anche tra i sistemisti.
- **Rapid prototyping.** Per test veloci e visualizzazioni il risultato arriva in pochi secondi, ancora meglio con Jupyter/JupyterLab su un server. "Il segreto di Python" è far sviluppare rapidamente anche chi non vuole sporcarsi le mani con il basso livello (`LSD-05 @ 00:36:18`–`00:37:24`).
**Il REPL** (`LSD-06 @ 00:03:32`–`00:05:18`). Il docente mostra il *Read-Evaluate-Print Loop*, usato pervasivamente in Jupyter: esegue una riga alla volta mantenendo lo stato. Esiste anche in Java ma "è un afterthought": i linguaggi si copiano a vicenda quando hanno successo.
**Edizione 2026** (`Teams 4 @ 0:17:14`–`0:27:00`). Stessa definizione, con tre aggiunte:
- il codice Python circola in **formato sorgente**, con la documentazione (docstring) dentro il sorgente: è trasparente, facile da condividere e modificare;
- nello scripting è fondamentale **non dover ricompilare**: si vedono subito gli effetti delle modifiche;
- "non c'è nulla che non potrei fare in Java", ma **il motivo per cui Python vince è la prototipazione**: "provo a fare qualcosa e vedo se funziona". Il principio di fondo è **KISS**.
> **Nota aggiunta:** a `LSD-05 @ 00:34:29` il docente dice che il sistema di pacchetti di Debian/Ubuntu (`apt`) "è tutto scritto in Python". APT è scritto in C++ (`libapt-pkg`); in Python erano scritti altri gestori, come `yum` e le prime versioni di `dnf` in Red Hat/Fedora. Sulla storia: van Rossum lavorava al CWI di Amsterdam sul progetto Amoeba e si ispirò al linguaggio ABC.
## 2. Quando usare Python e quando Java
**Slide p5–p7 e p18–p19.** Python conviene per facilità di apprendimento e leggibilità, per ML e data science (TensorFlow, PyTorch; "86% dei data scientist") e per lo sviluppo rapido. Java conviene per prestazioni (compilazione + JIT), applicazioni enterprise (Spring, Hibernate) e connettività ai database (JDBC). Le percentuali delle slide vengono da blog di settore e vanno prese come indicative.
**Docente** (`LSD-06 @ 00:00:10`–`00:03:01`, `00:05:55`–`00:08:07`).
- Python "va benissimo" per notebook, cose interattive o di breve durata, e per gli **script di sistema** (manutenzione, gestione pacchetti).
- Java è da preferire lato **server**: molti servizi sono stati scritti in Java "e hanno funzionato perfettamente". Il docente critica la "moda" di riscrivere in Python funzionalità server che erano thread-safe in Java.
- "Se c'è un servizio che deve rimanere collegato a un database di continuo, in Python non lo consiglierei mai": Python non è nato per girare a lungo come server con garanzie di stabilità.
- **Python è ottimo per sperimentare in piccolo**, ma quando l'algoritmo va applicato a terabyte di dati "il sistema schiatta": da Python si può *lanciare* l'esecuzione, non *eseguirla* (`LSD-05 @ 01:38:35`–`01:39:38`).
**Aneddoto** (`LSD-05 @ 01:42:31`–`01:43:38`). Il docente ha lanciato da Python un attacco a forza bruta implementato in CUDA; dopo un paio di mesi l'interprete è andato in crash e si sono persi due mesi di lavoro. Morale: qualsiasi esecuzione lunga su un supercalcolatore deve avere **checkpoint** periodici.
## 3. Il Global Interpreter Lock
**Slide p8–p13.** Il **GIL** è un lock di mutua esclusione dell'interprete: **un solo thread nativo per processo** può eseguire le operazioni di base (allocazione di memoria, reference counting) alla volta. Ce l'hanno CPython e Ruby MRI. C'è un GIL per processo, quindi con **più processi** si ottiene parallelismo pieno, ognuno con il proprio interprete.
- **Vantaggi (p11):** programmi single-thread più veloci (nessun lock su ogni struttura dati), integrazione facile di librerie C non thread-safe, implementazione dell'interprete molto più semplice.
- **Svantaggi (p12–p13):** limita il parallelismo ottenibile con i thread di un solo processo; se il codice è quasi tutto interpretato e non fa chiamate bloccanti fuori dall'interprete, su un multiprocessore lo speedup è quasi nullo; i segnali tra thread CPU-bound possono rallentare anche su un solo processore.
**Docente** (`LSD-05 @ 00:38:42`–`00:46:15`).
- "Il GIL è il singolo più grande difetto di Python": anche su un multicore i thread Python lavorano di fatto in sequenza. Oggi si comprano processori con 192 core, e Python ne usa uno.
- Se le analisi "vanno veloci" è perché qualcun altro ha scritto codice parallelo in **C/C++ o OpenMP**, che Python invoca "rimanendo lì fermo ad aspettare". Quindi "**Python non è scalabile**".
- **Perché non lo si toglie:** il codice sequenziale è molto più safe di quello parallelo, e c'è tantissimo codice legacy che, senza GIL, potrebbe smettere di funzionare o, peggio, **dare risultati errati in modo silenzioso**. "Retrofittare la thread safety in Python è quasi impossibile".
- **Confronto con Java:** nati quasi insieme, ma Java è nato con l'esecuzione parallela e "la scalabilità come ingrediente nativo", Python come linguaggio di scripting.
- Alla nascita il GIL è stato "una pensata molto intelligente": semplifica enormemente l'interprete. Diventa un problema quando si vogliono usare i core.
**Il GIL e l'I/O** (`LSD-05 @ 01:40:55`–`01:42:31`; `LSD-06 @ 00:34:16`–`00:43:51`). L'unica forma di parallelismo con il GIL si ha con le **chiamate bloccanti**: un thread fermo su un'operazione di I/O rilascia il GIL e un altro può calcolare. Il docente spiega le chiamate bloccanti con `socket.accept()` in un server Java: il thread chiede al sistema operativo di essere svegliato quando arriva una connessione e intanto è sospeso. **Ogni chiamata di I/O è bloccante**, perché il codice non sa quando il sistema operativo gli restituirà il controllo. Con un solo thread il programma si ferma; con più thread gli altri vanno avanti. Per questo la concorrenza "è il presupposto del parallelismo" ed esiste anche su un single core, grazie al time slicing.
**Edizione 2026** (`Teams 4 @ 0:27:00`–`0:40:24`). Il docente struttura la discussione come domanda "il GIL è un bene o un male?":
- **bene** per la semplicità: il codice sequenziale ha "una sua semplicità innata" e meno problemi di concorrenza;
- **male** per le prestazioni: con CPU multicore e GPU "non c'è mai reale parallelismo" (grafico di p9);
- due strade per parallelizzare: il modulo `threading`, utile soprattutto per l'I/O, e le **proposte di rimozione del GIL**, frenate dalla **retrocompatibilità** ("funziona nel 99% dei casi ma spesso dà risultati non corretti");
- il GIL è "forse il **peccato originale** più grande di Python", ma con una concorrenza nativa alla Java "forse Python non avrebbe avuto tutto questo successo".
<callout icon="⚠️">
	**Correzione.** Due affermazioni ricorrenti vanno ridimensionate. **"Python non ha il multithreading"** (`LSD-06 @ 00:00:41`) e **"Python ha la thread safety perché non ha il multithreading"** (`Teams 4 @ 1:52:13`): CPython ha thread veri del sistema operativo; il GIL impedisce solo che più thread eseguano **bytecode** nello stesso istante. L'interprete può cambiare thread tra un'istruzione bytecode e l'altra (intervallo predefinito 5 ms), quindi un'operazione composta come `x += 1` o un *check-then-act* su un dizionario **non è atomica**: race condition e perdite di aggiornamenti esistono anche con il GIL, e servono `threading.Lock` e simili. Il GIL protegge la coerenza interna dell'interprete (reference counting), non la correttezza del programma. **"Multithreading solo con I/O, dual thread nel caso migliore, e va abilitato"** (`LSD-05 @ 01:41:59`–`01:42:31`): con carichi I/O-bound molti thread avanzano utilmente insieme e non c'è nulla da abilitare; il limite vale per i carichi **CPU-bound** in Python puro.
</callout>
> **Nota aggiunta — lo stato attuale del GIL:** la **PEP 703** ha introdotto una build di CPython **free-threaded**, senza GIL, sperimentale in Python 3.13 (2024). Con la **PEP 779** è diventata ufficialmente supportata in Python 3.14 (ottobre 2025), come build alternativa e non predefinita. I costi sono quelli previsti dal docente: rallentamento single-thread, estensioni C da adeguare, codice che dava per scontato il GIL. Altre implementazioni: Jython e IronPython non hanno GIL, PyPy sì.
## 4. Parallelismo in Python nonostante il GIL
**Slide MDA16 p10; MDA19 p6, p9, p12.** Le strade sono tre, e ciascuna ha un costo:
- **`multiprocessing`**: più processi, ciascuno con il proprio interprete e il proprio GIL. È il meccanismo principale per il parallelismo CPU-bound, ma porta più memoria e comunicazione tra processi (IPC) più complessa (MDA19 p9, p12);
- **`asyncio`**: concorrenza cooperativa su un solo thread, adatta ai carichi I/O-intensivi (MDA19 p9);
- **librerie ed estensioni native**: il calcolo pesante gira in C, C++, Fortran o Rust, che rilasciano il GIL (MDA16 p8).
MDA19 p6–p7 riassume: Python scala bene quando il carico è dominato dall'I/O e la velocità di sviluppo conta più delle prestazioni; per il CPU-bound la scalabilità passa per scelte **architetturali** (processi, servizi esterni), cioè **orizzontali**.
**Docente.**
- **Multithreading vs multiprocessing** (`LSD-06 @ 00:43:51`–`00:48:50`): il multithreading dà a un processo più flussi d'esecuzione, il multiprocessing fa girare più processi in parallelo. Con htop mostra Chromium, fortemente multithread: molti PID che condividono lo stesso spazio di memoria. "Il multithreading è fondamentale per qualsiasi applicazione".
- **Librerie native** (`LSD-05 @ 00:40:27`): il parallelismo che si vede da Python è di codice C/C++/OpenMP invocato da Python.
- **Edizione 2026** (`Teams 4 @ 0:37:57`–`0:40:24`): Python come **wrapper** di librerie in C, C++, Rust, OpenMP. Pro: "ogni linguaggio vive nel proprio ambiente ideale". Contro: il passaggio tra linguaggi crea problemi di gestione della memoria e soprattutto di **debugging** ("farlo capire al Python chiamante è un altro paio di maniche"). È il **problema dei due linguaggi** che Julia vuole risolvere (capitolo 07).
> **Nota aggiunta — schema di scelta:** carico **I/O-bound** (rete, disco, chiamate a servizi, anche le chiamate parallele a un LLM) → `threading` o `asyncio`; carico **CPU-bound in Python puro** → `multiprocessing` o `concurrent.futures.ProcessPoolExecutor`, pagando serializzazione (pickle) e memoria; **calcolo numerico** → NumPy e librerie native, che rilasciano il GIL; **codice proprio critico** → Numba (JIT), Cython con `nogil` e `prange` (che usa OpenMP), estensioni in Rust con PyO3. Nel calcolo distribuito lo stesso ruolo lo hanno Dask, Ray o Spark, dove Python orchestra e il lavoro gira altrove.
## 5. Java
**Slide p14–p19.** Java è **staticamente tipato**, general purpose, orientato agli oggetti, concorrente, con il principio **Write Once, Run Anywhere** (WORA): il sorgente è compilato in **bytecode** eseguito da una **JVM** su qualunque piattaforma. Il compilatore **JIT** traduce in codice nativo le parti eseguite spesso. Punti di forza: OOP per codice modulare e riusabile, controllo della concorrenza (metodi e blocchi `synchronized`), framework enterprise (Spring, Hibernate), backend, Android, **JDBC** per l'accesso ai database.
**Docente** (`LSD-05 @ 01:48:09`–`01:57:46`).
- Java "non è un linguaggio perfetto ma è scalabile". La **tipizzazione statica** è la prima ragione: in Python una variabile "magicamente" cambia tipo durante l'esecuzione, e "mi dà i brividi" pensarlo su un supercalcolatore dove ogni minuto costa. In Java la correttezza almeno sui tipi si verifica a compile time.
- **WORA:** "il codice Java che ho scritto nel 1996 ancora funziona, e funziona il compilato". La JVM, "all'inizio denigrata", dà portabilità, isolamento e longevità del codice; ci girano sopra anche Scala e Kotlin.
- **Concorrenza nativa:** Java "sa che cos'è un thread"; la sincronizzazione mantiene il dato consistente con molti thread, quindi è adatto a server con molti client (applicazioni enterprise, Spring, Hibernate, database relazionali e non).
- **Calcolo distribuito:** Java contiene il concetto di oggetto che vive su un computer remoto.
- **Perché non ha sfondato in HPC:** lì conta spremere core e memoria, e questo si fa meglio con linguaggi "C-like" che permettono di "spaccare il bit", come OpenMP e MPI, anche a costo di safety. Su macchine che costano centinaia di migliaia di euro si vuole **strong scaling**: "più tempo giro e più pago".
**Docente** (`LSD-06 @ 00:05:55`–`00:08:07`, `00:27:27`–`00:33:41`).
- Il sorgente diventa bytecode, "linguaggio intermedio a basso livello, però standard", "un tipo di assembly portabile"; la JVM lo esegue e il JIT traduce direttamente le parti più frequenti.
- JDBC permette di mantenere in modo consistente un database **transazionale**.
- **Demo multithreading:** una classe che implementa `Runnable`; all'avvio del thread (`start`) viene eseguito `run`. Ogni thread stampa il proprio nome e dorme 5 secondi; l'ordine di esecuzione cambia a ogni run e sul monitor si vedono entrambi i core al lavoro. Su un server con centinaia di core questo permette di **scalare su una macchina**, e con più macchine di "moltiplicare i core".
**Edizione 2026: interprete, JVM e sicurezza** (`Teams 4 @ 0:40:24`–`0:50:16`). Il docente sposta l'accento dalla portabilità al **controllo**:
- "JVM fa rima con interprete, con macchina astratta": qualcosa che a runtime sta tra l'algoritmo e la macchina;
- il suo valore è poter **intercettare azioni dannose** prima che vengano eseguite; C, C++ e Rust, compilati in nativo, sono più veloci "ma non hanno guardrail";
- legame con la scalabilità: bisogna **scalare in maniera safe**, e qui la bilancia pende verso Java e Python; se servono le prestazioni migliori, C/C++/Rust. "La risposta è: dipende";
- come interprete Python "non è particolarmente smart", la JVM è più avanzata, ma è un grande pezzo di codice con i suoi bug.
- La **verbosità** è il vero difetto di Java (`Teams 4 @ 1:31:10`).
<callout icon="⚠️">
	**Correzione.** **"La maggior parte delle classi fornite da Oracle sono thread safe"** (`LSD-06 @ 00:07:53`): le collezioni più usate (`ArrayList`, `HashMap`, `StringBuilder`) **non** lo sono; lo sono le legacy `Vector`, `Hashtable`, `StringBuffer` e il package `java.util.concurrent`. Java offre *primitive* per la concorrenza, non classi thread-safe di default, e non impedisce le race: `synchronized` va usato bene dal programmatore (Java_vs_Rust p9: "powerful but error-prone"). **"L'interprete fa controlli di sicurezza, può dirti che non puoi cancellare un file"** (`Teams 4 @ 0:46:03`–`0:48:07`): CPython non ha alcuna sandbox e i permessi sui file li applica il sistema operativo; Java aveva il `SecurityManager`, deprecato in Java 17 e disabilitato in JDK 24. La garanzia reale di Java e Python è la **memory safety** del linguaggio (niente puntatori arbitrari, controllo dei limiti), e anche Rust la offre, a compile time. **Date:** Java 1.0 è del 1996 e nasce con la diffusione del Web, non di Internet; gli oggetti remoti (RMI) arrivano con JDK 1.1 nel 1997; il REPL di Java (JShell) è del 2017, Java 9.
</callout>
## 6. Prestazioni: compilare Python
**Slide p20–p30.** Una tabella (p20) confronta C++, Java e Python su un ordinamento. Poi i tentativi di velocizzare Python:
<table header-row="true">
<tr>
<td>Strumento</td>
<td>Che cosa fa</td>
<td>Limiti (slide)</td>
</tr>
<tr>
<td>**PyPy**</td>
<td>interprete alternativo con **JIT tracing**; nessuna modifica al codice</td>
<td>runtime diverso da CPython, compatibilità limitata con le estensioni C, serve che il programma giri per più di qualche secondo</td>
</tr>
<tr>
<td>**Numba**</td>
<td>JIT su un sottoinsieme di Python basato su LLVM, per codice NumPy</td>
<td>linguaggio supportato limitato, dipendenza pesante (LLVM)</td>
</tr>
<tr>
<td>**Pythran**</td>
<td>compilatore statico Python→C++ per un sottoinsieme numerico</td>
<td>sottoinsieme del linguaggio</td>
</tr>
<tr>
<td>**mypyc**</td>
<td>compilatore Python→C che sfrutta le annotazioni PEP 484</td>
<td>niente ottimizzazioni a basso livello, interpretazione "opinionated" dei tipi, meno introspezione</td>
</tr>
<tr>
<td>**Nuitka**</td>
<td>compilatore statico Python→C, molto fedele al linguaggio, eseguibili autonomi</td>
<td>niente ottimizzazioni e tipi a basso livello</td>
</tr>
<tr>
<td>**Cython**</td>
<td>superset di Python (`.pyx`) con dichiarazioni di tipo C, tradotto in C e compilato; `cimport` di librerie C</td>
<td>le funzioni `cdef` non sono visibili da Python fuori dal modulo</td>
</tr>
</table>
Nel benchmark dell'autore del post (p28–p30) Cython porta un programma da 9 secondi a 0,2. La conclusione: Cython per le parti critiche individuate con il profiling, PyPy come "quick fix" con il rischio di trovarsi un giorno con una libreria incompatibile.
**Docente** (`LSD-06 @ 00:08:45`–`00:27:27`).
- Il benchmark "lascia il tempo che trova ma è indicativo": C++ molto più veloce, Java intermedio, Python ultimo perché interpretato. "Il tempo di compilazione è ben speso", da cui l'idea di compilare anche Python.
- PyPy, Numba, Pythran, mypyc e Nuitka: non sempre velocizzano e riducono la compatibilità, quindi "potrebbero creare risultati inattesi". Fare calcolo numerico scritto in Python è "controintuitivo": meglio usare librerie in C/C++.
- **"Viva Cython"**: il più completo compilatore Python→C, compatibile con il codice esistente; con un po' di C si può anche leggere e ritoccare il C generato. Invito a provarlo sul codice scritto negli altri moduli del master.
- **Il punto chiave:** questi strumenti rendono Python più veloce sui grandi dati, "**ma non è che lo rendono più safe**". E lo speed-up di Cython **non viene dal parallelismo**, "tutt'altro", ma dalla compilazione e dai tipi C. "Se dovete fare qualcosa di veramente scalabile dovete usare altri linguaggi": Java, OpenMP, MPI.
**Edizione 2026** (`Teams 4 @ 1:29:27`–`1:38:16`).
- Avere i sorgenti permette di **ricompilare con le ottimizzazioni per il proprio hardware** (per esempio le istruzioni vettoriali AVX-512): "è come fare scale up". Il tema torna con Julia (capitolo 07).
- Compilare Python ha un costo: si perdono l'interattività e il controllo dell'interprete, e il compilatore deve fare scelte imposte da un linguaggio di alto livello che "non è detto siano adeguate". "Compilare un linguaggio che non è nato per essere compilato non dà sempre i benefici sperati". Consiglio: **linguaggi diversi per compiti diversi**.
<callout icon="⚠️">
	**Correzione.** A `LSD-06 @ 00:09:51` il docente legge 15.000–22.000 ns per Python e dice "un secondo e mezzo": sono **15–22 microsecondi**. PyPy è "fully language compliant" (p21): il limite riguarda le **estensioni C** di CPython, e la slide sulla mancata compatibilità con NumPy si riferisce a PyPy 2.5 (2015); oggi NumPy funziona su PyPy tramite uno strato di compatibilità, con prestazioni variabili. mypyc ha "good support for PEP-484 typing": il contro è l'assenza di tipi e ottimizzazioni *a basso livello*. Nuitka è un compilatore, non un linguaggio. Cython **può** parallelizzare: con `nogil` e `prange` genera cicli OpenMP. A `Teams 4 @ 1:35:03` il docente dice che Python compilato "va in crash" dove l'interprete lancerebbe un'eccezione: PyPy, Nuitka e Cython conservano le eccezioni Python; si perdono controlli solo se li si disattiva esplicitamente (per esempio `boundscheck(False)` in Cython).
</callout>
> **Nota aggiunta — come ragionare sulla domanda 7 del Questionario 4 (applicazione numerica critica):** la scelta dipende da dove sta il tempo di calcolo. Se il lavoro è fatto da operazioni vettoriali su array, **Python con NumPy/SciPy** è già vicino al C, perché il ciclo gira in librerie native. Se c'è un **ciclo proprio**, stretto e numerico, Python puro è la scelta peggiore (tipi dinamici, oggetti *boxed*, GIL); **Numba** o **Cython** con tipi dichiarati danno speed-up di uno o due ordini di grandezza con poche modifiche; **PyPy** aiuta sul codice Python puro ma meno con le estensioni C. **Java** dà prestazioni prevedibili grazie al JIT, **multithreading reale** senza GIL e un ecosistema adatto a servizi che girano a lungo, al costo di verbosità e di un ecosistema numerico meno ricco; il suo JIT richiede un tempo di *warm-up*. Se l'applicazione deve anche **scalare su più core** per il calcolo, Java o Python con codice nativo parallelo battono Python puro; se deve scalare su un cluster, servono MPI, Spark o Dask. In un'argomentazione conviene esplicitare criteri: tempo per unità di calcolo, parallelismo, costo di sviluppo, manutenibilità, rischio di incompatibilità.
## 7. Rust
**Slide MDA19 p4–p14.** Rust è pensato per software che **gira in modo efficiente, scala in sicurezza e resta affidabile nel tempo**:
- **niente garbage collector**: la memoria è gestita a compile time con **ownership e borrowing**, e questo dà **prestazioni prevedibili**, importanti nei sistemi grandi e *time-critical* (p4);
- sfrutta pienamente i multicore per i carichi CPU-bound (p4); ambiti tipici: programmazione di sistema, networking, infrastruttura, tool (p5);
- Rust scala **verticalmente** dentro un singolo processo, Python più spesso **orizzontalmente** o con scelte architetturali (p7);
- la **thread safety è imposta a compile time** dal sistema di ownership e dai tipi, quindi i **data race sono impediti prima dell'esecuzione**; i thread Rust girano davvero in parallelo perché non c'è un lock globale (p10); i trait **`Send`** e **`Sync`** garantiscono che i dati condivisi tra thread siano usati in modo sicuro (p11);
- conclusione (p14): Python per sistemi I/O-bound in rapida evoluzione, Rust per software scalabile, critico per le prestazioni e altamente concorrente.
**Slide RustLearningResources** (Enrico Risa, Rust Roma Meetup). Sponsorizzato da Mozilla Research, 1.0 nel maggio 2015 con compatibilità all'indietro garantita. Multiparadigma (imperativo, funzionale, concorrente), tipizzazione statica con inferenza locale, compilato, **zero-cost abstraction**, move semantics, memory safety garantita, **thread senza data race**, generics basati su trait, pattern matching, runtime minimo, binding efficiente con il C (p6–p8). L'obiettivo è unire il **controllo** di C/C++ alla **safety** di Java e Python (p9–p10).
- **Che cosa vuol dire safety** (p57–p58): i problemi nascono quando una risorsa è contemporaneamente **condivisa** (più riferimenti, *alias*) e **mutabile**: "alias + mutable = 💀", che è "quasi la definizione di data race".
- **Il GC non basta** (p59): si perde controllo, serve un runtime, e comunque non impedisce data race né l'invalidazione degli iteratori.
- **La via di Rust** (p66): spostare il più possibile i controlli a compile time con tre concetti:
	- **ownership** (p68–p77): ogni valore ha un solo proprietario; quando il proprietario esce dallo scope il valore viene rilasciato. Passare un `Vec` a una funzione ne **trasferisce** la proprietà, e usarlo dopo è un errore di compilazione;
	- **borrowing** (p78–p88): si può prestare un valore con **uno o più riferimenti in sola lettura** (`&T`) **oppure esattamente un riferimento mutabile** (`&mut T`), mai le due cose insieme. Modificare un vettore preso in prestito in lettura non compila;
	- **lifetime** (p89–p91): lo scope per cui un riferimento è valido, così nessun riferimento sopravvive al proprietario.
- Il resto del mazzo è sintassi: struct, enum (`Result<T,E>` per gli errori, `Option<T>` al posto di `null`), pattern matching esaustivo, generics monomorfizzati senza costo a runtime, trait con dispatch statico o dinamico (`dyn`).
**Docente** (`LSD-07 @ 00:28:23`–`00:29:48`, `00:39:29`–`00:42:41`).
- Rust "non è a livelli di MPI", ma "se la batte nel piccolo con OpenMP", cioè su un **nodo singolo**. Esempio "molto più asciutto" di un `main` che crea in un ciclo `for` diversi thread che stampano un numero.
- Rust "nato da Mozilla": imperativo, funzionale e concorrente; **static typing**, compilato, uso safe della memoria heap, molto veloce; "il controllo di C/C++ e la sicurezza di Java".
- "L'unica cosa che vi volevo dire di Rust, a parte la sintassi" è l'**ownership**: con `s1 = "hello"` e `s2 = s1`, stampare `s1` non compila. "Rust è un linguaggio difficile ma che dà tante soddisfazioni".
**Edizione 2026** (`Teams 4 @ 1:38:16`–`2:00:31`).
- "Python e Rust vivono in due mondi complementari". Rust è multiparadigma e "meno object oriented": "di object oriented ha soltanto le interfacce" (i trait), "il che forse è positivo".
- Rust è nato per il **software di sistema**. Digressione su **kernel space e user space**: il kernel manipola pochi dati e deve essere stabile; il vero problema di scalabilità è nelle applicazioni, che in HPC girano su migliaia di macchine. I **sistemi operativi distribuiti** (Amoeba) sono falliti: si perdeva il controllo su dove finivano i processi; oggi ogni nodo ha il suo Linux e sopra uno strato come MPI, e la distribuzione la fa consapevolmente l'applicazione.
- **Rust = scalabilità verticale di un singolo processo**, Python "con un po' di fatica" orizzontale. Per la scalabilità "ancora meglio" Scala, Elixir, Erlang.
- **Thread safety**, con l'analogia della videochiamata: il codice thread-safe è quello che impedisce a tutti di attivare il microfono insieme, così i flussi "convivono pacificamente" e non si perde il dato. Rust la garantisce **a compile time** e obbliga lo sviluppatore a "un modello di gestione dei dati condivisi molto più sano": è **avoidance**, si evita che i problemi si verifichino. È più difficile da imparare "ma anche da far compilare"; nemmeno Java dà le stesse garanzie.
- **Uso ibrido:** una libreria in Rust chiamata da Python. Si **prototipa con Python** su dati piccoli e scenari diversi; quando i dati crescono o serve il tempo reale, si passa a Rust che chiama Rust, più **autocontenuto, stabile e omogeneo**.
<callout icon="⚠️">
	**Correzione.** L'esempio `s1`/`s2` (`LSD-07 @ 00:41:35`–`00:42:09`) non compila per la **move semantics**: `let s2 = s1;` sposta la `String` in `s2`, e l'errore è *borrow of moved value: **`s1`*. Il motivo non è una race condition (in un solo thread non ce ne sono), ma garantire un **unico proprietario** che libera la memoria, quindi niente *double free* né puntatori pendenti. Il legame con i data race è la regola "alias XOR mutabile" del borrowing, estesa ai thread da `Send` e `Sync`. Rust "con la facilità di Python" (`LSD-07 @ 00:40:30`) contraddice sia il docente sia Java_vs_Rust p17 ("steeper learning curve"). "C/C++/Rust non hanno guardrail" (`Teams 4 @ 0:46:03`) vale per C e C++, non per Rust: controlli a compile time (borrow checker) e a runtime (limiti degli array, panic invece di comportamento indefinito), salvo i blocchi `unsafe`. Infine, Safe Rust impedisce i **data race** ma non le **race condition logiche** né i **deadlock** (capitolo 06).
</callout>
> **Nota aggiunta — perché Rust dà prestazioni prevedibili (Questionario 4, domanda 9):** (1) **niente GC**, quindi niente pause di raccolta dal momento imprevedibile; la memoria viene liberata in un punto noto a compile time, quando il proprietario esce dallo scope (*deterministic destruction*, RAII); (2) **compilazione ahead-of-time** in codice nativo, quindi niente *warm-up* del JIT né deottimizzazioni a runtime (Java_vs_Rust p6); (3) **zero-cost abstraction**: generics monomorfizzati e iteratori compilati come cicli scritti a mano, dispatch statico per default; (4) **runtime minimo** e controllo del layout in memoria (valori sullo stack, struct senza header di oggetto), quindi uso di cache prevedibile; (5) il borrowing esclude l'*aliasing* mutabile, che permette al compilatore ottimizzazioni che in C richiederebbero `restrict` (capitolo 03). Prevedibile non vuol dire sempre più veloce: vuol dire bassa varianza della latenza, che conta nei sistemi grandi e *time-critical*.
> **Nota aggiunta — perché Rust si presta ad applicazioni altamente concorrenti (Questionario 4, domanda 10):** (1) un thread Rust è un thread del sistema operativo, senza lock globale; (2) il compilatore rifiuta a priori il codice con data race: un dato mutabile può avere un solo riferimento mutabile alla volta, e per condividerlo tra thread bisogna passare da tipi che lo rendono sicuro (`Arc<Mutex<T>>`, `Arc<RwLock<T>>`, tipi atomici); (3) `Send` indica che un valore può essere trasferito a un altro thread, `Sync` che può essere condiviso per riferimento: `Rc` non è `Send`, quindi usarlo tra thread è un errore di compilazione; (4) il `Mutex` di Rust **possiede** il dato, quindi non si può accedere al dato senza aver preso il lock; (5) librerie come **Rayon** (parallelismo dati: `par_iter`) e **Tokio** (asincrono) si appoggiano alle stesse garanzie. È la cosiddetta *fearless concurrency* (Java_vs_Rust p9).
## 8. Java e Rust a confronto
**Slide Java_vs_Rust p1–p21.** Il mazzo non è commentato né nelle lezioni del portale né in `Teams 4`; lo riassumo perché completa il quadro.
<table header-row="true">
<tr>
<td>Aspetto</td>
<td>Java</td>
<td>Rust</td>
</tr>
<tr>
<td>Origine e filosofia (p4)</td>
<td>1995, portabilità, applicazioni di rete, runtime gestito, produttività</td>
<td>affidabilità e sicurezza del software di sistema, prestazioni senza perdere safety, esplicitezza</td>
</tr>
<tr>
<td>Esecuzione (p6, p16)</td>
<td>bytecode + JVM + JIT; ottimo sui processi lunghi, con *warm-up*</td>
<td>nativo ahead-of-time; avvio rapido, latenza deterministica, binari autocontenuti</td>
</tr>
<tr>
<td>Memoria (p7–p8)</td>
<td>GC: semplice, ma overhead e pause; safety a runtime (controllo dei limiti)</td>
<td>ownership, borrowing, lifetime a compile time; nessun overhead a runtime, ma regole da imparare</td>
</tr>
<tr>
<td>Concorrenza (p9)</td>
<td>thread, `synchronized`, lock, `java.util.concurrent`: potente ma soggetto a errori</td>
<td>*fearless concurrency*: errori di concorrenza trovati in compilazione</td>
</tr>
<tr>
<td>Errori (p10)</td>
<td>eccezioni checked e unchecked</td>
<td>`Result` e `Option` espliciti nelle firme</td>
</tr>
<tr>
<td>Tipi e paradigmi (p11–p13)</td>
<td>nominale, classi, ereditarietà, generics; lambda e Stream</td>
<td>tipi algebrici, pattern matching, trait; niente ereditarietà; idiomi funzionali più coerenti</td>
</tr>
<tr>
<td>Ecosistema (p14–p15, p20)</td>
<td>libreria standard vasta, Maven, Spring; interoperabilità con Kotlin, Scala, Groovy sulla JVM</td>
<td>libreria standard piccola, Cargo e [crates.io](http://crates.io); interoperabilità via FFI con C e C++</td>
</tr>
<tr>
<td>Apprendimento e governance (p17–p18)</td>
<td>accessibile; governance aziendale, stabilità</td>
<td>curva ripida, ma messaggi del compilatore molto didattici; governance comunitaria</td>
</tr>
<tr>
<td>Sicurezza (p19)</td>
<td>sandbox, verifica del bytecode, controlli a runtime</td>
<td>elimina a compile time le vulnerabilità di memoria e i data race</td>
</tr>
</table>
Messaggio finale (p19, p21): prevenire le vulnerabilità durante lo sviluppo è più efficace che scoprirle a runtime; la scelta dipende da requisiti, prestazioni ed esperienza del team, e il confronto mostra il compromesso tra astrazione, safety ed efficienza.
## Collegamento con il Questionario 4
<table header-row="true">
<tr>
<td>Domanda</td>
<td>Slide</td>
<td>Video</td>
<td>Qui</td>
</tr>
<tr>
<td>1. design goals di Python, tipizzazione, interpretazione, ecosistema</td>
<td>`MDA16` p3–p7; `MDA19` p3</td>
<td>`LSD-05 @ 00:25:57`–`00:38:42`; `LSD-06 @ 00:01:48`–`00:05:18`; `Teams 4 @ 0:17:14`–`0:20:23`, `0:25:47`–`0:27:00`</td>
<td>§1</td>
</tr>
<tr>
<td>2. quando Python su Java; esempi data science e ML</td>
<td>`MDA16` p5–p7, p18–p19</td>
<td>`LSD-05 @ 00:26:28`–`00:29:56`, `00:36:18`–`00:38:03`, `01:38:35`–`01:39:38`; `LSD-06 @ 00:00:10`–`00:03:32`; `Teams 4 @ 0:20:23`–`0:27:00`</td>
<td>§2</td>
</tr>
<tr>
<td>3. GIL: vantaggi, svantaggi, CPU-bound e I/O-bound</td>
<td>`MDA16` p8–p13; `MDA19` p8, p12</td>
<td>`LSD-05 @ 00:38:42`–`00:46:15`, `01:40:55`–`01:42:31`; `LSD-06 @ 00:34:16`–`00:43:51`; `Teams 4 @ 0:27:00`–`0:37:57`</td>
<td>§3 (con correzione)</td>
</tr>
<tr>
<td>4. parallelismo nonostante il GIL</td>
<td>`MDA16` p8, p10; `MDA19` p6, p9, p12</td>
<td>`LSD-05 @ 00:40:27`–`00:41:05`; `LSD-06 @ 00:43:51`–`00:48:50`; `Teams 4 @ 0:30:09`–`0:31:43`, `0:37:57`–`0:40:24`, `1:56:04`–`1:59:28`</td>
<td>§4 (multiprocessing e asyncio solo nelle slide; schema nella nota)</td>
</tr>
<tr>
<td>5. Java e WORA: JVM e bytecode</td>
<td>`MDA16` p14–p15, p18</td>
<td>`LSD-05 @ 01:50:35`–`01:52:55`; `LSD-06 @ 00:06:32`–`00:07:34`, `00:28:41`–`00:29:47`; `Teams 4 @ 0:40:24`–`0:42:30`, `1:31:10`</td>
<td>§5</td>
</tr>
<tr>
<td>6. Java enterprise: OOP, concorrenza, database</td>
<td>`MDA16` p15–p16, p19</td>
<td>`LSD-05 @ 01:52:55`–`01:57:46`; `LSD-06 @ 00:00:41`–`00:01:48`, `00:05:55`–`00:08:07`, `00:27:27`–`00:33:41`</td>
<td>§5 (con correzione)</td>
</tr>
<tr>
<td>7. app numerica: Java, Python puro o Python ottimizzato</td>
<td>`MDA16` p18, p20–p30</td>
<td>`LSD-06 @ 00:08:45`–`00:27:27`; `LSD-05 @ 01:55:34`–`01:57:46`; `Teams 4 @ 1:29:27`–`1:38:16`</td>
<td>§6 (criteri nella nota)</td>
</tr>
<tr>
<td>8. un'applicazione per Python e una per Rust</td>
<td>`MDA19` p4–p7, p14</td>
<td>`LSD-07 @ 00:28:23`–`00:29:48`, `00:40:00`–`00:41:01`; `Teams 4 @ 1:38:16`–`1:49:58`, `1:56:04`–`1:59:28`</td>
<td>§7</td>
</tr>
<tr>
<td>9. Rust e prestazioni prevedibili</td>
<td>`MDA19` p4, p13; `Java_vs_Rust` p6–p8; `RustLearningResources` p7–p8, p59, p66–p68</td>
<td>`LSD-07 @ 00:40:00`–`00:40:30`; `Teams 4 @ 1:55:02` (solo citato: il perché non è spiegato a voce)</td>
<td>§7 (nota)</td>
</tr>
<tr>
<td>10. Rust e applicazioni altamente concorrenti</td>
<td>`MDA19` p8–p13; `Java_vs_Rust` p9; `RustLearningResources` p8, p57–p58, p66–p88</td>
<td>`LSD-07 @ 00:28:23`–`00:29:48`, `00:41:01`–`00:42:41`; `LSD-06 @ 00:43:19`; `Teams 4 @ 1:49:58`–`1:55:02`</td>
<td>§7 (nota e correzione)</td>
</tr>
</table>
## Punti incerti della trascrizione
- `LSD-05 @ 00:46:15` — frase interrotta "quello che viene fatto adesso è che per esempio invece di…": allude al multiprocessing (slide p10)
- `LSD-06 @ 00:09:17` — il docente non sa dire cosa misuri la colonna "compilazione" del benchmark: numeri da prendere con cautela
- `LSD-06 @ 00:27:27` — "OpenCL", corretto subito in OpenMP
- `LSD-07 @ 00:42:09` — frase finale su Rust mal trascritta
- `Teams 4 @ 0:41:27` — "praticamente tipato": si intende staticamente tipato
