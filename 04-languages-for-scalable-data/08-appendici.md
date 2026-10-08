# 08 - Appendici

> Fonte Notion: https://app.notion.com/p/3dd12abc808d81618755fe1fb439940a — ultima modifica 2026-09-17T09:21:00.801Z

Glossario, fonti del manuale e differenze tra l'edizione del portale e l'edizione 2026. I punti incerti delle trascrizioni sono in fondo a ogni capitolo.
## A. Glossario
<table header-row="true">
<tr>
<td>Termine</td>
<td>Significato</td>
<td>Capitolo</td>
</tr>
<tr>
<td>**Amdahl, legge di**</td>
<td>con una frazione α non parallelizzabile, lo speedup con p unità è 1 / (α + (1−α)/p) e non supera mai 1/α</td>
<td>05 §5; 06 §5.6</td>
</tr>
<tr>
<td>**asyncio**</td>
<td>concorrenza cooperativa su un solo thread in Python, per carichi I/O-bound</td>
<td>04 §4</td>
</tr>
<tr>
<td>**barriera** (*barrier*)</td>
<td>punto di sincronizzazione in cui tutti i thread devono arrivare prima di proseguire; implicita alla fine di una regione OpenMP</td>
<td>05 §7; 06 §4</td>
</tr>
<tr>
<td>**borrowing**</td>
<td>in Rust, prestito di un valore: più riferimenti in lettura (`&T`) oppure uno solo mutabile (`&mut T`), mai insieme</td>
<td>04 §7</td>
</tr>
<tr>
<td>**bytecode**</td>
<td>codice intermedio portabile eseguito da una macchina virtuale (JVM per Java, Scala, Kotlin)</td>
<td>02; 04 §5</td>
</tr>
<tr>
<td>**chiamata bloccante**</td>
<td>chiamata che sospende il thread finché il sistema operativo non restituisce il controllo, tipicamente l'I/O</td>
<td>04 §3; 05 §2</td>
</tr>
<tr>
<td>**concorrenza**</td>
<td>più attività che avanzano in un ordine non controllato, anche su un solo core (time slicing); presupposto del parallelismo</td>
<td>05 §2</td>
</tr>
<tr>
<td>**copy-on-write**</td>
<td>tecnica per cui dopo una `fork` le pagine di memoria si copiano solo quando vengono modificate</td>
<td>05 §2</td>
</tr>
<tr>
<td>**core**</td>
<td>unità di esecuzione indipendente con il proprio stato; "quello che una volta era una CPU"</td>
<td>05 §1</td>
</tr>
<tr>
<td>**CPU-bound / I/O-bound**</td>
<td>carico limitato dal calcolo / dall'attesa di input e output; decide se i thread Python aiutano</td>
<td>04 §3–§4</td>
</tr>
<tr>
<td>**data race**</td>
<td>due o più contesti concorrenti accedono alla stessa locazione, almeno uno scrive, gli accessi non sono sincronizzati</td>
<td>06 §2</td>
</tr>
<tr>
<td>**deadlock**</td>
<td>attesa circolare in cui nessuno può procedere; richiede le quattro condizioni di Coffman</td>
<td>06 §3</td>
</tr>
<tr>
<td>**Design by Contract**</td>
<td>precondizioni, postcondizioni e invarianti verificate sul codice (Eiffel)</td>
<td>03 §5</td>
</tr>
<tr>
<td>**efficienza** (parallela)</td>
<td>speedup diviso per il numero di unità: E(p) = S(p)/p</td>
<td>05 §5</td>
</tr>
<tr>
<td>**expression problem**</td>
<td>aggiungere a un tipo sia nuovi casi sia nuove operazioni senza toccare il codice esistente</td>
<td>07 §1</td>
</tr>
<tr>
<td>**false sharing**</td>
<td>thread che scrivono dati diversi ma vicini sulla stessa linea di cache e si rallentano a vicenda</td>
<td>06 §4</td>
</tr>
<tr>
<td>**Flynn, tassonomia di**</td>
<td>SISD, SIMD, MISD, MIMD: flussi di istruzioni e di dati</td>
<td>05 §3</td>
</tr>
<tr>
<td>**fork-join**</td>
<td>modello di OpenMP: il master crea un team di thread a ogni regione parallela e lo riassorbe alla fine</td>
<td>05 §7</td>
</tr>
<tr>
<td>**garbage collector**</td>
<td>componente del runtime che libera la memoria non più raggiungibile</td>
<td>03 §2</td>
</tr>
<tr>
<td>**GIL**</td>
<td>*Global Interpreter Lock* di CPython: un solo thread per processo esegue bytecode alla volta</td>
<td>04 §3</td>
</tr>
<tr>
<td>**interleaving**</td>
<td>uno dei possibili ordinamenti delle operazioni di più thread; il loro numero cresce in modo combinatorio</td>
<td>06 §5.3</td>
</tr>
<tr>
<td>**JIT**</td>
<td>compilazione *just-in-time* in codice nativo delle parti eseguite spesso (JVM, PyPy, Numba, Julia)</td>
<td>04 §5–§6; 07 §1</td>
</tr>
<tr>
<td>**JVM**</td>
<td>Java Virtual Machine: esegue il bytecode, con interprete e JIT</td>
<td>04 §5</td>
</tr>
<tr>
<td>**lifetime**</td>
<td>in Rust, l'intervallo in cui un riferimento è valido</td>
<td>04 §7</td>
</tr>
<tr>
<td>**load amplification**</td>
<td>con più carico gli accessi allo stato condiviso e la sensibilità ai tempi crescono, e i race emergono</td>
<td>06 §5.4</td>
</tr>
<tr>
<td>**memoria condivisa / distribuita**</td>
<td>tutte le unità vedono la stessa memoria / ogni nodo ha la sua e si comunica per messaggi</td>
<td>05 §4</td>
</tr>
<tr>
<td>**MPI**</td>
<td>*Message Passing Interface*: standard di libreria per programmi a memoria distribuita</td>
<td>05 §8</td>
</tr>
<tr>
<td>**multiple dispatch**</td>
<td>scelta del metodo in base ai tipi di tutti gli argomenti (Julia)</td>
<td>07 §1</td>
</tr>
<tr>
<td>**multithreading / multiprocessing**</td>
<td>più flussi dentro un processo che condividono la memoria / più processi isolati</td>
<td>05 §2</td>
</tr>
<tr>
<td>**mutex**</td>
<td>lock di mutua esclusione: un solo thread alla volta nella sezione critica</td>
<td>06 §4</td>
</tr>
<tr>
<td>**NUMA**</td>
<td>*Non-Uniform Memory Access*: il costo di accesso alla memoria dipende da quale socket la possiede</td>
<td>05 §1</td>
</tr>
<tr>
<td>**OpenMP**</td>
<td>API di direttive `#pragma`, routine e variabili d'ambiente per il parallelismo a memoria condivisa in C, C++, Fortran</td>
<td>05 §7</td>
</tr>
<tr>
<td>**ownership**</td>
<td>in Rust, ogni valore ha un solo proprietario e viene rilasciato quando questo esce dallo scope</td>
<td>04 §7</td>
</tr>
<tr>
<td>**parallel reduction**</td>
<td>aggregazione ad albero di risultati parziali con un'operazione associativa, in log₂ P passi</td>
<td>06 §4</td>
</tr>
<tr>
<td>**problema dei due linguaggi**</td>
<td>scrivere la parte critica in C/C++ e il resto in Python, pagando la complessità di entrambi</td>
<td>04 §4; 07 §1</td>
</tr>
<tr>
<td>**Pthreads**</td>
<td>API POSIX di basso livello per creare e sincronizzare thread in C</td>
<td>05 §6</td>
</tr>
<tr>
<td>**race condition**</td>
<td>comportamento che dipende dall'ordine o dai tempi di eventi non controllabili</td>
<td>06 §1</td>
</tr>
<tr>
<td>**reduction** (OpenMP)</td>
<td>clausola che crea una copia privata per thread e combina i risultati con un operatore associativo</td>
<td>05 §7; 06 §4</td>
</tr>
<tr>
<td>**safety / security**</td>
<td>il programma non produce errori o crash / il sistema resiste ad accessi e usi malevoli</td>
<td>02 §1; 07 §1</td>
</tr>
<tr>
<td>**scale-up / scale-out**</td>
<td>potenziare la singola macchina (verticale) / aggiungere macchine (orizzontale)</td>
<td>01 §5; 05 §4</td>
</tr>
<tr>
<td>**`Send`**** / ****`Sync`**</td>
<td>trait di Rust: un valore può essere trasferito a un altro thread / condiviso per riferimento tra thread</td>
<td>04 §7</td>
</tr>
<tr>
<td>**sezione critica**</td>
<td>porzione di codice che accede a dati condivisi e va eseguita da un thread alla volta</td>
<td>06 §4</td>
</tr>
<tr>
<td>**SIMD / vettorizzazione**</td>
<td>stessa istruzione su più dati, anche dentro un singolo core (SSE, AVX)</td>
<td>05 §3; 07 §1</td>
</tr>
<tr>
<td>**speedup**</td>
<td>S(p) = T(1) / T(p)</td>
<td>05 §5</td>
</tr>
<tr>
<td>**strong / weak scaling**</td>
<td>stesso problema in meno tempo / problema più grande nello stesso tempo</td>
<td>05 §5</td>
</tr>
<tr>
<td>**thread-safe**</td>
<td>codice che resta corretto quando più thread lo eseguono insieme</td>
<td>04 §7; 06</td>
</tr>
<tr>
<td>**type inference**</td>
<td>il compilatore deduce i tipi statici senza che siano scritti (ML, OCaml, Rust)</td>
<td>02 §3; 03 §4</td>
</tr>
<tr>
<td>**Universal Scalability Law**</td>
<td>modello di Gunther con contesa e costo di coerenza: oltre un certo numero di thread il throughput cala</td>
<td>06 §5.6</td>
</tr>
<tr>
<td>**wall-clock time**</td>
<td>tempo reale trascorso; è quello da usare per misurare lo speedup</td>
<td>05 §5</td>
</tr>
<tr>
<td>**WORA**</td>
<td>*Write Once, Run Anywhere*: stesso bytecode su qualunque piattaforma con una JVM</td>
<td>04 §5</td>
</tr>
</table>
## B. Fonti e lezioni
### Lezioni del portale (edizione passata)
<table header-row="true">
<tr>
<td>Lezione</td>
<td>Durata</td>
<td>Contenuto</td>
<td>Capitoli</td>
</tr>
<tr>
<td>`LSD-01`</td>
<td>1h 19m</td>
<td>presentazione, data science, quattro analisi, scalabilità, scale-up e scale-out</td>
<td>01</td>
</tr>
<tr>
<td>`LSD-02`</td>
<td>1h 28m</td>
<td>scalabilità di programmi e linguaggi, legacy; storia dei linguaggi fino al C</td>
<td>01, 02</td>
</tr>
<tr>
<td>`LSD-03`</td>
<td>1h 36m</td>
<td>C, Simula, ML, compilatore e interprete, PROLOG, Java; inizio di MDA3 (garbage collection)</td>
<td>02, 03</td>
</tr>
<tr>
<td>`LSD-04`</td>
<td>2h 01m</td>
<td>MDA3: garbage collection, puntatori, tipi, eccezioni, assertion, astrazioni</td>
<td>03</td>
</tr>
<tr>
<td>`LSD-05`</td>
<td>1h 58m</td>
<td>fine di MDA3; Python e GIL; multicore, thread e processi, Flynn, memoria condivisa e distribuita; Java</td>
<td>03, 04, 05</td>
</tr>
<tr>
<td>`LSD-06`</td>
<td>1h 23m</td>
<td>Java vs Python, compilare Python, Cython; thread in Java, chiamate bloccanti, multiprocessing; OpenMP, MPI; race condition</td>
<td>04, 05, 06</td>
</tr>
<tr>
<td>`LSD-07`</td>
<td>46m</td>
<td>OpenMP e regola del trapezio, MPI, strong e weak scaling, htop e meld, Rust e ownership, race condition e deadlock</td>
<td>04, 05, 06</td>
</tr>
</table>
### Registrazioni Teams (edizione 2026)
Consultate in pagina, senza scaricarle. Il download delle registrazioni è disabilitato. Le due lezioni del 28 e 30 aprile non erano a calendario e non compaiono come riunioni su Teams: probabilmente una continuazione informale offerta alla classe dopo l'ultima lezione del 24/04. Sono successive alla pubblicazione dei questionari e nel manuale valgono come integrazione.
<table header-row="true">
<tr>
<td>Sigla</td>
<td>Data</td>
<td>Contenuto usato</td>
<td>Capitoli</td>
</tr>
<tr>
<td>`Teams 2`</td>
<td>17/04/2026</td>
<td>modalità dei questionari; storia dei linguaggi (Fortran, C, Rust in Firefox, JavaScript, Scala)</td>
<td>Assessment, 02, 07</td>
</tr>
<tr>
<td>`Teams 3`</td>
<td>21/04/2026</td>
<td>MDA3 con aggiunte: formati e serializzazione, GC e kernel, `Result` in Rust, Elixir</td>
<td>03, 07</td>
</tr>
<tr>
<td>`Teams 4`</td>
<td>23/04/2026</td>
<td>Python e GIL, Java, interpreti e sicurezza, talk di Domas, compilare Python, Rust vs Python, multicore, thread e processi</td>
<td>04, 05, 07</td>
</tr>
<tr>
<td>`Teams 5`</td>
<td>24/04/2026</td>
<td>questionari come esonero; discussione sui progetti; transazioni e dati modificabili; MDA21 e data race</td>
<td>Assessment, 06</td>
</tr>
<tr>
<td>`Teams Extra-1`</td>
<td>28/04/2026 (lezione extra)</td>
<td>speedup, NUMA, Amdahl, strong e weak scaling; progettazione della somma parallela; WSL e VirtualBox</td>
<td>05, 06, 07</td>
</tr>
<tr>
<td>`Teams Extra-2`</td>
<td>30/04/2026 (lezione extra)</td>
<td>memoria condivisa e distribuita; Julia, SIMD, Pluto; htop; Pthreads e OpenMP; assessment proposto</td>
<td>05, 07</td>
</tr>
</table>
Non esaminata: `MDALSD-20260416cut.mkv` (registrazione tagliata del 16/04/2026).
### Slide
<table header-row="true">
<tr>
<td>File</td>
<td>Pagine</td>
<td>Edizione</td>
<td>Capitolo</td>
</tr>
<tr>
<td>`MDA0`, `MDA1Definitions`</td>
<td>8, 19</td>
<td>portale</td>
<td>01</td>
</tr>
<tr>
<td>`MDA2_PLHistory`</td>
<td>30</td>
<td>portale</td>
<td>02</td>
</tr>
<tr>
<td>`MDA3ScalableFeatures`</td>
<td>76</td>
<td>portale</td>
<td>03</td>
</tr>
<tr>
<td>`MDA16PythonvsJava`</td>
<td>30</td>
<td>portale</td>
<td>04</td>
</tr>
<tr>
<td>`MDA19PythonVsRust`, `Java_vs_Rust`, `RustLearningResources`</td>
<td>14, 21, 156</td>
<td>2026</td>
<td>04, 07</td>
</tr>
<tr>
<td>`MDA5Multithreading`, `008_OpenMP`, `ProcessesVsThreads.png`</td>
<td>138, 97, —</td>
<td>portale</td>
<td>05</td>
</tr>
<tr>
<td>`MDA21ScalabilityandDataRaces`, `ChiarissimoDataRaceVsRaceCondition`, `design-of-parallel-programs`</td>
<td>25, 3, 22</td>
<td>2026</td>
<td>06</td>
</tr>
<tr>
<td>`Race-condition-Wikipedia`, `Deadlock-Wikipedia`</td>
<td>8, 5</td>
<td>portale</td>
<td>06</td>
</tr>
<tr>
<td>`julia-slides`, `julia-course-slides`, `SCALA book.docx`</td>
<td>39, 101, —</td>
<td>2026</td>
<td>07</td>
</tr>
<tr>
<td>`us-17-Domas-Breaking-The-x86-ISA`</td>
<td>166</td>
<td>portale</td>
<td>07</td>
</tr>
</table>
## C. Differenze tra le due edizioni
<table header-row="true">
<tr>
<td>Aspetto</td>
<td>Portale (edizione passata)</td>
<td>Edizione 2026</td>
</tr>
<tr>
<td>Verifica</td>
<td>valutazione "integrata" con gli altri corsi e piccolo progetto facoltativo (`LSD-01 @ 00:18:24`); questionari entro settembre (`LSD-07 @ 00:24:19`)</td>
<td>5 questionari in PDF, valgono come esonero in itinere (`Teams 5 @ 0:06:18`); scadenza "non stringente"</td>
</tr>
<tr>
<td>Python, Java, Rust</td>
<td>MDA16 commentata; Rust solo in chiusura (`LSD-07`)</td>
<td>in più MDA19 e Java_vs_Rust; Rust vs Python discusso a lungo (`Teams 4`)</td>
</tr>
<tr>
<td>Interpreti e sicurezza</td>
<td>talk di Domas tra i materiali, non commentato</td>
<td>talk commentato; interprete come "guardrail", supply chain, ricompilare da sorgente (`Teams 4`)</td>
</tr>
<tr>
<td>Data race</td>
<td>race condition con l'esempio del conto corrente e deadlock</td>
<td>MDA21 e slide Chiarissimo; data race come problema di scalabilità (`Teams 5`)</td>
</tr>
<tr>
<td>Parallelismo</td>
<td>MDA5 e OpenMP a voce, formule solo accennate; Pthreads saltati</td>
<td>formule di speedup e Amdahl, somma parallela passo per passo (lezione extra); Pthreads "sconsigliatissimi"</td>
</tr>
<tr>
<td>Linguaggi "alternativi"</td>
<td>Julia e Scala solo citati</td>
<td>Julia presentata in una lezione extra al posto di Elixir; Scala promesso in slide separate</td>
</tr>
<tr>
<td>Aggiunte su MDA3</td>
<td>—</td>
<td>formati e serializzazione, GC e kernel, `Result` in Rust (`Teams 3`)</td>
</tr>
<tr>
<td>Pratica</td>
<td>demo di Java, htop, meld</td>
<td>WSL o VirtualBox con Linux, htop, Pluto; studio comparativo proposto nelle lezioni extra</td>
</tr>
</table>
## D. Come è stato costruito il manuale
- Le 7 lezioni del portale sono state trascritte con Whisper large-v3 (mlx-whisper, lingua italiana) con timestamp; i segmenti a bassa confidenza sono segnalati nei capitoli come punti incerti.
- Il testo delle slide è stato estratto pagina per pagina; le pagine citate sono quelle del PDF.
- Le registrazioni Teams sono state lette in pagina tramite la trascrizione automatica di Stream, e usate solo per le integrazioni.
- Le parti marcate **Nota aggiunta** e i riquadri **Correzione** sono integrazioni: vanno verificate prima di citarle come "dette a lezione".
