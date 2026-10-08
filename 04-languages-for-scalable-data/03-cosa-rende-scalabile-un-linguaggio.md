# 03 - Cosa rende scalabile un linguaggio

> Fonte Notion: https://app.notion.com/p/3dd12abc808d8146b95cd0d69175668f — ultima modifica 2026-09-16T23:03:03.873Z

Fonti: slide `MDA3ScalableFeatures` (76 pagine), lezioni `LSD-03` (01:15 → fine), `LSD-04` (intera), `LSD-05` (00:00 → 00:26); edizione 2026: `Teams 3` (21/04/2026).
Le slide riprendono, spesso alla lettera, il saggio di **Mike Vanier** (Caltech) *Scalable computer programming languages*, già citato nel capitolo 01: ogni caratteristica di un linguaggio riceve un giudizio, da "very good" a "very bad", in base a quanto aiuta a scrivere ed estendere programmi grandi. Nel portale le slide sono commentate in `LSD-03` (fine), in tutta `LSD-04` e nei primi 26 minuti di `LSD-05` (p58–p76). Nell'edizione 2026 il docente le riprende in `Teams 3` (21/04/2026), con alcune aggiunte segnate come **Edizione 2026**.
<table header-row="true">
<tr>
<td>Caratteristica</td>
<td>Giudizio (slide)</td>
<td>Pagine</td>
<td>Lezione</td>
</tr>
<tr>
<td>Garbage collection</td>
<td>very good</td>
<td>p2–p11</td>
<td>`LSD-03 @ 01:15:42`; `LSD-04 @ 00:00:10`–`00:24:26`</td>
</tr>
<tr>
<td>Accesso diretto alla memoria e aritmetica dei puntatori</td>
<td>very bad</td>
<td>p12–p21</td>
<td>`LSD-04 @ 00:24:26`–`00:54:26`</td>
</tr>
<tr>
<td>Type checking statico</td>
<td>mostly very good</td>
<td>p22–p25</td>
<td>`LSD-04 @ 00:54:26`–`01:04:29`</td>
</tr>
<tr>
<td>Dichiarazioni di tipo e type inference</td>
<td>—</td>
<td>p26–p27</td>
<td>`LSD-04 @ 01:04:29`–`01:13:53`</td>
</tr>
<tr>
<td>Type casting non controllato</td>
<td>bad</td>
<td>p28–p30</td>
<td>`LSD-04 @ 01:13:53`–`01:18:46`</td>
</tr>
<tr>
<td>Tipizzazione statica e dinamica</td>
<td>—</td>
<td>p31–p38</td>
<td>`LSD-04 @ 01:18:46`–`01:25:46`</td>
</tr>
<tr>
<td>Gestione delle eccezioni</td>
<td>good</td>
<td>p39–p41</td>
<td>`LSD-04 @ 01:25:46`–`01:30:48`</td>
</tr>
<tr>
<td>Controllo degli errori a runtime</td>
<td>not so good (ma necessario)</td>
<td>p42–p47</td>
<td>`LSD-04 @ 01:30:48`–`01:38:27`</td>
</tr>
<tr>
<td>Assertion e Design by Contract</td>
<td>very good</td>
<td>p48–p54</td>
<td>`LSD-04 @ 01:38:27`–`01:42:35`</td>
</tr>
<tr>
<td>Astrazioni e sistemi di moduli</td>
<td>very good</td>
<td>p55–p57</td>
<td>`LSD-04 @ 01:42:35`–`01:55:20`</td>
</tr>
<tr>
<td>Programmazione a oggetti</td>
<td>good</td>
<td>p58–p62</td>
<td>`LSD-04 @ 01:55:20`–`02:00:39`; `LSD-05 @ 00:00:11`–`00:10:28`</td>
</tr>
<tr>
<td>Programmazione funzionale</td>
<td>good</td>
<td>p63–p67</td>
<td>`LSD-05 @ 00:10:28`–`00:20:29`</td>
</tr>
<tr>
<td>Macro strutturali</td>
<td>mostly good</td>
<td>p68–p70</td>
<td>`LSD-05 @ 00:20:29` (solo richiamo)</td>
</tr>
<tr>
<td>Componenti</td>
<td>—</td>
<td>p71–p73</td>
<td>`LSD-05 @ 00:20:29`–`00:21:58`</td>
</tr>
<tr>
<td>Sintassi e leggibilità</td>
<td>—</td>
<td>p74–p76</td>
<td>`LSD-05 @ 00:21:58`–`00:25:57`</td>
</tr>
</table>
## 1. Stack e heap
Premessa del docente (`LSD-04 @ 00:01:16`): un processo ha due aree di memoria. Lo **stack** è gestito automaticamente dal programma; lo **heap** a mano, con `malloc` e `free`. Lo mostra in C: un array di tre elementi dichiarato normalmente sta sullo stack, lo stesso vettore allocato con `malloc` sta nello heap. Con il puntatore allo heap si può fare `pt++` e finire fuori dall'area prevista.
> **Nota aggiunta:** in C l'aritmetica dei puntatori vale anche sugli array nello stack (il nome dell'array decade a puntatore) e anche lì si può uscire dai limiti. La differenza vera tra stack e heap è il **tempo di vita**: lo stack si libera da solo al ritorno dalla funzione, lo heap resta allocato finché qualcuno non lo libera. È per questo che il problema della memoria riguarda soprattutto lo heap.
Per questo C e C++ "dovrebbero" servire solo per codice non troppo grande, ma sono "abusati" in progetti molto complessi, dove mostrano tutti i limiti. Anche per i sistemi operativi si sperimentano linguaggi più scalabili, ma la barriera è il costo già sostenuto per sviluppare e correggere il codice esistente: si cambia linguaggio solo se il vantaggio è "veramente notevole" (`LSD-04 @ 00:04:39`–`00:06:53`).
## 2. Garbage collection: very good
### Cos'è e perché aiuta
**Slide p2–p3.** Il GC è il meccanismo con cui il runtime del linguaggio recupera automaticamente la memoria non più usata. È "un'enorme vittoria" per il programmatore e aumenta drasticamente la scalabilità. Di solito è ovvio **quando allocare**; è molto difficile sapere **quando è sicuro liberare**, soprattutto quando i riferimenti vengono passati in giro, restituiti da funzioni, salvati in più strutture dati poi cancellate (o no).
**Docente** (`LSD-03 @ 01:15:42`–`01:18:50`). Il GC evita i **memory leak**, cioè la riduzione progressiva della memoria libera, e quindi aiuta proprio i programmi che devono girare a lungo su tanti dati.
**Dangling pointer** (`LSD-03 @ 01:18:50`). Un puntatore a memoria già liberata. L'analogia è chi cambia numero di telefono: chi ha ancora il vecchio numero, se non trova nessuno, "fa un segmentation fault"; se il numero è stato riassegnato, trova un'altra persona e magari le rivela cose private. Più codice e dati crescono, più i riferimenti incrociati diventano ingestibili, a meno che il linguaggio non impedisca di fare caos (`LSD-03 @ 01:21:11`).
### Senza GC
**Slide p4–p5.** I linguaggi senza GC scoraggiano implicitamente l'uso di strutture dati che non siano le più semplici, perché con strutture complesse la gestione della memoria diventa presto intrattabile. In pratica il programmatore finisce per scriversi un proprio GC (spesso un reference counter), di solito peggiore di quello che avrebbe con un linguaggio che lo ha integrato.
**Docente.** "Dovrebbero scoraggiarlo, ma non lo fanno": prima che il GC si imponesse con Java c'erano solo C e C++, quindi non c'era alternativa (`LSD-04 @ 00:08:21`). Senza GC il problema è di scalabilità del codice e soprattutto dei **dati**: con molti dati è difficile tenere traccia della memoria e l'applicazione, nel tempo, la esaurisce (`LSD-04 @ 00:09:34`). Un GC "fatto in casa" in C è possibile ma macchinoso e rischioso, mentre quello di Java esiste e viene migliorato da oltre trent'anni (`LSD-03 @ 01:23:08`–`01:26:32`).
**Demo dal vivo** (`LSD-04 @ 00:14:22`–`00:17:04`). Un programma C di fatto di una riga, una `malloc` in un ciclo: l'occupazione di memoria sale, si esauriscono RAM e swap, il sistema rallenta e alla fine il processo viene ucciso. Se fosse stata un'analisi di dati, si sarebbero persi risultati parziali e tempo di calcolo. "Una gestione esplicita della memoria non scala." Sullo stack lo stesso si ottiene solo con una ricorsione fatta apposta; nello heap senza GC è "facilissimo".
### Vantaggi
**Slide p6.** Il GC evita tre classi di errori:
- **dangling pointer**: memoria liberata mentre esistono ancora puntatori ad essa, poi dereferenziati quando magari è già stata riassegnata;
- **double free**: liberare una regione già liberata, e forse già riallocata;
- **memory leak**: memoria di oggetti non più raggiungibili che non viene mai liberata, fino all'esaurimento.
**Slide p9.** Il GC è "la singola caratteristica più importante" per rendere scalabile un linguaggio: chi passa da un linguaggio senza GC (C++) a uno di potere espressivo simile con GC (Java) si dice più contento perché può concentrarsi sugli algoritmi. Il docente lo conferma (`LSD-04 @ 00:22:48`) e aggiunge: Java non è perfetto ed è verboso rispetto a Python, ma "se volete stare tranquilli" su safety e in parte security è un'ottima scelta.
Safety e security "vanno spesso a braccetto" (`LSD-04 @ 00:06:53`): se non si sa chi accede a certe aree di memoria e quando, la safety si perde, e ne soffre anche la security, perché non si può impedire che un dato sensibile (una chiave, un dato personale) venga letto.
### Costi
**Slide p7–p8, p10–p11.**
- **Tempo e spazio.** I GC ben progettati, soprattutto quelli **generazionali**, possono essere molto efficienti, più del reference counting ingenuo, ma usano più memoria: stime dell'ordine del **50% in più**. Un programma con memory leak, però, usa più memoria di tutti.
- Uno studio del 2005 conclude che al GC serve **cinque volte la memoria** per andare veloce quanto una gestione esplicita idealizzata. Le interazioni con la gerarchia di memoria possono rendere l'overhead intollerabile in modi difficili da prevedere. Apple ha citato l'impatto sulle prestazioni per non adottare il GC su iOS.
- **Pause imprevedibili.** Il momento in cui la memoria viene raccolta non è prevedibile e produce stalli sparsi, inaccettabili in sistemi real-time, transazionali o interattivi. GC incrementali, concorrenti e real-time mitigano il problema con diversi compromessi.
**Docente.** Il GC "occupa spazio, è un altro thread", consuma CPU e memoria, ma è "un investimento adeguato" se implementato bene; in JDK 24 viene ancora migliorato, e il docente consiglia **Phoronix** per seguire queste novità (`LSD-04 @ 00:17:34`–`00:20:34`).
L'**analogia della stanza** (`LSD-03 @ 01:27:08`–`01:35:02`; `LSD-04 @ 00:21:42`): il GC è qualcuno a cui date le chiavi della camera e che butta via gli oggetti di cui nessuno si ricorda più. Due svantaggi: non sapete quando passa, quindi nel frattempo la stanza è mediamente più piena (più memoria occupata) e, se si riempie, dovete aspettare che arrivi; e quando entra non vi avvisa, vi interrompe mentre state facendo altro (le pause).
**Perché in Java non si accede per sbaglio a un oggetto liberato** (`LSD-03 @ 01:31:05`). Con l'aritmetica dei puntatori, in C++ si scorre uno scaffale di libri facendo +1 +1 +1 e si finisce dove il libro non c'è più. In Java non esiste il concetto di "il libro accanto": ci sono solo riferimenti a oggetti singoli, quindi non si può raggiungere lo spazio vuoto.
<callout icon="⚠️">
	**Correzione.** Il docente descrive il GC di Java come un contatore di riferimenti associato a ogni oggetto, che libera l'oggetto quando arriva a zero (`LSD-03 @ 01:24:56`; `LSD-04 @ 00:20:34`). Non è così, e la slide p7 lo dice implicitamente contrapponendo i GC generazionali al "naive reference counting". I GC della JVM (e di .NET) sono **tracing**: partono dalle radici (variabili sullo stack, campi statici) e marcano tutto ciò che è **raggiungibile**; il resto è garbage. Sono generazionali perché la maggior parte degli oggetti muore giovane. Il reference counting è usato invece da CPython (con un collector aggiuntivo per i cicli) e da Swift, e ha un limite classico: due oggetti che si riferiscono a vicenda non arrivano mai a zero. L'analogia del numero di telefono descrive bene l'idea di raggiungibilità.
</callout>
### GC e sistema operativo
**Slide p13–p14.** La programmazione a basso livello con i puntatori rende molto difficile un GC preciso. Esiste un GC **conservativo** per C e C++ (Boehm-Demers): richiede di riscrivere le `malloc`, è meglio di niente, ma non garantisce che tutta la memoria sia gestita correttamente. Nella pratica lo si vede usato quasi solo in codice che implementa un linguaggio con GC.
**Docente** (`LSD-04 @ 00:26:14`–`00:40:24`). Il GC retrofittato riduce i leak ma "non dà nessuna garanzia di correttezza" e non ha avuto successo. Aggiunge una digressione che non è nelle slide:
- il **kernel** (Linux, dove stanno i device driver) parla direttamente con CPU, memoria e dispositivi, gira con privilegi massimi e non usa `malloc`; secondo il docente non può usare un GC, salvo approcci a microkernel;
- le **applicazioni utente** vivono in un mondo astratto, si appoggiano alla libreria standard C (glibc su Linux) anche se scritte in Python, Java o Scala, e lì il GC esiste. "Sono quelle che interessano a noi", perché nella data science non si scrivono sistemi operativi;
- anche il kernel però deve essere scalabile, per far condividere le risorse alle applicazioni in modo efficiente.
> **Nota aggiunta:** esistono sistemi operativi di ricerca con GC (Singularity di Microsoft Research in C#, Biscuit in Go), anche se i kernel diffusi non lo usano. Linux alloca con allocatori propri (`kmalloc`, `vmalloc`). Su macOS la libreria C non è glibc ma libSystem, di derivazione BSD.
**Memory leak anche con il GC** (`LSD-04 @ 00:42:38`–`00:45:42`). Si hanno leak anche in Python e sulla JVM se si tengono riferimenti a dati che non servono più. Per Python il docente cita **memory_profiler** (`mprof`), **tracemalloc** (traccia allocazioni e deallocazioni) e **objgraph** (grafo delle dipendenze tra oggetti).
## 3. Puntatori e aritmetica dei puntatori: very bad
**Slide p12, p15–p16.** C e C++ permettono di interagire direttamente con gli indirizzi di memoria e di incrementare o decrementare i puntatori. Il costo per la scalabilità va oltre il rendere difficile il GC: i puntatori, e soprattutto l'aritmetica, **distruggono qualsiasi garanzia di safety**. Se si può aggiungere 1.000.000 a un puntatore e dereferenziare una regione di memoria qualsiasi, "all hell can break loose". Se va bene, un core dump; se va male, memoria corrotta e **errori silenti** che si manifestano lontano dall'origine. I tempi di debugging esplodono, la produttività crolla, e le occasioni per questi errori crescono con la dimensione del programma: una barriera significativa alla scalabilità.
**Docente.**
- I puntatori sono necessari nei **device driver** ("devo poter spaccare il bit", accedere ai registri) e utili nelle micro-ottimizzazioni: "passare un puntatore a un oggetto è la cosa più leggera che posso fare" invece di copiare una struttura (`LSD-04 @ 00:25:01`–`00:25:38`).
- Il danno peggiore non sono i crash ma gli **errori silenti**: risultati sbagliati senza accorgersene, e quando lo si scopre il debugging è "la cosa più costosa". Meglio spendere più tempo all'inizio con un linguaggio scalabile, come Java o Rust, "in cui viviamo un po' più nella bambagia" (`LSD-04 @ 00:40:24`–`00:42:38`).
- Nel capitolo 02 c'è la distinzione tra segmentation fault ed errore silente (`LSD-03 @ 00:03:15`).
### Micro-ottimizzazioni contro macro-ottimizzazioni
**Slide p17.** L'argomento classico a favore dei puntatori è la velocità, ed è spesso vero: Vanier ha visto l'aritmetica dei puntatori, usata con giudizio, rendere un programma cinque volte più veloce. Ma spesso vale il contrario: molte ottimizzazioni che il compilatore farebbe da solo diventano difficili o impossibili nel codice che usa i puntatori. **"I linguaggi che permettono le micro-ottimizzazioni spesso rendono impossibili le macro-ottimizzazioni."**
**Docente** (`LSD-04 @ 00:46:16`): passando riferimenti si guadagna qualcosa, ma il compilatore "non conosce la semantica del vostro programma" e non può più ottimizzare.
> **Nota aggiunta:** il meccanismo tecnico è il **pointer aliasing**. Se una funzione riceve due puntatori `a` e `b`, il compilatore non può escludere che puntino alla stessa memoria: scrivere in `*a` potrebbe cambiare `*b`. Deve quindi rileggere i valori dalla memoria a ogni passo e rinunciare a vettorizzare i cicli (SIMD), a propagare costanti, a riordinare o parallelizzare le operazioni. Il C99 ha introdotto la parola chiave `restrict` proprio per promettere al compilatore che non c'è aliasing. Fortran, che non ha aliasing tra argomenti, è storicamente più veloce del C nel calcolo numerico anche per questo, e Rust ottiene lo stesso effetto dalle regole di borrowing. In un grande sistema il guadagno locale di una micro-ottimizzazione è spesso molto inferiore a ciò che si perde nelle ottimizzazioni globali, e in più si paga in safety e manutenibilità.
### Meyer, i componenti a basso livello e Cyclone
**Slide p18–p21.**
- Bertrand Meyer, autore di Eiffel: "puoi avere l'aritmetica dei puntatori o programmi corretti, ma non entrambi". L'accesso diretto alla memoria è **"la singola barriera più grande" alla scalabilità di un linguaggio**.
- I puntatori restano cruciali per la programmazione vicina all'hardware, ma **i programmi grandi scritti a basso livello non sono scalabili**. Il modo giusto di usare il C è scrivere piccoli componenti di basso livello dentro applicazioni scritte soprattutto in linguaggi di alto livello. Lo stesso vale per il C++: classi di basso livello che incapsulano i puntatori, anche se il compilatore non può imporre questo incapsulamento.
- **Cyclone**: variante "safe" del C con tre tipi di puntatori, aritmetica sempre controllata, costo a runtime da trascurabile a sostanziale. Non correggeva gli altri problemi del C. Gli sviluppatori di Rust lo citano come fonte di idee.
**Docente** (`LSD-04 @ 00:46:47`–`00:54:26`). Eiffel è un linguaggio a oggetti con safety altissima (GC, tipi statici, un retrogusto funzionale). Puntatori e cast restano utili a bassissimo livello, per esempio per aggirare bug hardware con patch software. Per programmi complessi e modulari "il C++ non va bene", e il C# semplifica ma non risolve. Il modello "piccoli componenti in C sotto un linguaggio di alto livello" è esattamente quello di Python con le sue librerie: Python "astrae molto, asciuga la sintassi" e rende il codice manutenibile, mentre il lavoro pesante lo fa il C. In Cyclone il controllo avviene a runtime e "non è a costo zero".
## 4. Tipi
### Type checking statico: mostly very good
**Slide p22–p25.** In un linguaggio staticamente tipato ogni dato ha un tipo che non cambia e le variabili non accettano valori di altri tipi. Vantaggi:
- **molti errori a compile time**: il compilatore cattura quelli banali e il programmatore si concentra sulle parti interessanti, con più produttività;
- se il sistema di tipi si estende ai **moduli**, anche l'uso dei moduli importati è verificato: si esclude un'ampia classe di errori nel codice scritto da altri e lo si **riusa con fiducia**;
- **codice più veloce**: se il compilatore sa che `a` e `b` sono interi piccoli, inserisce direttamente l'addizione tra interi; se sa solo che sono oggetti che potrebbero essere interi, float o stringhe, la decisione va rimandata a runtime, e il controllo a runtime costa.
**Docente** (`LSD-04 @ 00:54:26`–`01:04:29`). "Lo static typing è una garanzia ma non è perfetto." Con i tipi statici la compilazione non va a buon fine finché gli errori di tipo non sono corretti, quindi l'eseguibile è "molto più safe". Nei linguaggi modulari come Java, Scala e Kotlin ci si può fidare dei moduli importati, "cosa che in Python non avviene". Secondo il docente "l'optimum" architetturale è Java, compilato in bytecode e poi eseguito da una macchina virtuale, che unisce controllo statico e controllo a runtime; lo preferisce per questo anche a Rust, che produce codice nativo.
> **Nota aggiunta:** la JVM moderna non si limita a interpretare: compila in codice nativo just-in-time le parti eseguite spesso. La safety di Java viene dal sistema di tipi, dal *bytecode verifier* e dai controlli a runtime, non dall'interpretazione in sé. Rust ottiene memory safety a compile time e inserisce anch'esso controlli a runtime (per esempio sui limiti degli array), senza bisogno di una VM; può anche essere compilato in WebAssembly, che è un bytecode eseguito in una VM.
### Dichiarazioni esplicite e type inference
**Slide p26–p27.** Molti programmatori non amano i tipi statici perché le dichiarazioni sono verbose e "sporcano" l'algoritmo. L'esempio è Java: `Foo foo = new Foo();`, tre volte "foo" per dire una cosa sola. L'alternativa è la **type inference**: il linguaggio ricava il tipo di quasi tutte le variabili dal contesto. L'esempio è OCaml, con codice conciso come in Scheme o Python ma con tutti i benefici della tipizzazione statica.
**Docente** (`LSD-04 @ 01:05:00`–`01:13:53`). La verbosità è "sicuramente fin troppa", ma "alla fine la verbosità a volte è meglio della indeterminatezza del dato". Su Python: non si dichiara il tipo e questo "toglie tanta sicurezza". Esistono compilatori come Cython e PyPy che rendono il codice più veloce, ma secondo il docente con meno controlli e senza scalare, perché "Python non nasce per essere compilato". Anche CPython ha migliorato le prestazioni grazie a compilazione just-in-time.
> **Nota aggiunta:** il docente dice che in Python il tipo "viene inferito a runtime". È una confusione di termini: Python è **dinamicamente tipato** (i tipi stanno sugli oggetti e si verificano durante l'esecuzione), mentre la **type inference** è una tecnica statica, a compile time, ed è proprio ciò che le slide contrappongono alla tipizzazione dinamica. Su Cython e PyPy: PyPy è un interprete alternativo con compilatore JIT, conserva la semantica e i controlli di Python e non produce eseguibili; Cython traduce codice Python annotato in C e produce soprattutto moduli di estensione.
> **Nota aggiunta — perché l'inferenza aiuta la scalabilità:** separa due cose che la dichiarazione esplicita lega insieme, cioè la *verifica* dei tipi (che resta completa e a compile time) e la loro *scrittura* (che diventa facoltativa). Si ottiene la concisione dei linguaggi dinamici senza rinunciare a trovare gli errori prima dell'esecuzione, al controllo dei moduli e alla velocità. Oggi è presente anche in linguaggi mainstream: `var` in Java 10, `auto` in C++, Kotlin, Scala, Rust, TypeScript. I suoi limiti sono discussi nel capitolo 02.
### Type casting non controllato: bad
**Slide p28–p30.** Il cast è una via di fuga con cui si dice al compilatore "ho detto che era di tipo X, da ora fingi che sia di tipo Y, me ne prendo la responsabilità". In C è necessario perché il sistema di tipi è debolissimo; in C++ molto meno ed è considerato cattivo stile. In Java i cast esistono (quasi sempre da superclasse a sottoclasse) ma, se falliscono, lanciano un'eccezione; in C non falliscono mai, e se si converte al tipo sbagliato può succedere di tutto. I linguaggi che richiedono molti cast non controllati sono meno scalabili. In Java molti cast servivano a supplire all'assenza di tipi parametrici: anche i cast controllati possono indicare una debolezza.
**Docente** (`LSD-04 @ 01:13:53`–`01:18:46`). In C "il sistema di tipi è praticamente non esistente": un puntatore a `char` si tratta come puntatore a `int` con disinvoltura. **Analogia dell'autobus:** uno studente sale sull'autobus trattato come persona (upcasting); quando scende lo si ritratta da studente (downcasting). Se in realtà era un turista, in Java il cast fallisce con un'eccezione e ci si accorge dell'errore; in C il cast riesce sempre e produce errori silenti o segmentation fault. La probabilità di errore cresce con le righe di codice, quindi il casting libero "non scala".
> **Nota aggiunta:** i "tipi parametrici" citati dalla slide sono i *generics*, introdotti in Java 5 (2004): prima, estraendo un elemento da una `List` si otteneva un `Object` da convertire a mano. Il testo di Vanier è anteriore a quella versione.
### Tipizzazione statica e dinamica
**Slide p31–p38.** È "una delle grandi guerre sante" tra ricercatori e utenti. Nei sistemi dinamici hanno un tipo gli oggetti, non le variabili: una variabile è un legame a un oggetto e può riferirsi a un intero, poi a una stringa, poi a una lista. Conseguenze:
- le operazioni che richiedono certi tipi devono **controllarli a runtime**: penalità di prestazioni significative e **perdita di safety**, perché l'errore di tipo emerge solo durante l'esecuzione;
- d'altra parte la tipizzazione dinamica è **"incredibilmente espressiva"**, più di qualsiasi sistema statico; molta di quella flessibilità si recupera con un sistema statico abbastanza potente (di nuovo OCaml);
- l'argomento della minore verbosità è "debole", perché l'inferenza lo risolve;
- Lisp, Scheme, Python, Ruby e Smalltalk sono piacevoli da usare, ma **la mancanza di controlli statici danneggia sostanzialmente la loro scalabilità**;
- nei grandi progetti in questi linguaggi si scrivono molti **unit test** per catturare errori di tipo oltre che di logica (la comunità Smalltalk e l'extreme programming di Kent Beck);
- una via di mezzo è il **soft typing**: controlla staticamente tutto ciò che può e rimanda a runtime il resto (Dylan, Common Lisp, PLT Scheme).
**Docente** (`LSD-04 @ 01:18:46`–`01:25:46`). Sommando `a` e `b`, Python deve prima scoprire di che tipo sono e poi scegliere l'operazione; in Java la scelta avviene a compile time. "Se quello che vogliamo è facilità di scrittura, Python è sicuramente adatto. Se vogliamo safety e affidabilità, la scelta migliore sono linguaggi fortemente tipati con static typing, come Java o Scala." E il consiglio più netto del corso: **"non scrivete tanto codice in Python perché non è lì per quello"**. I test aiutano, ma estenderli costa e "non dà la garanzia formale" dell'assenza di errori di tipo, perché dipende dai casi che si è pensato di coprire.
> **Nota aggiunta — la risposta alla domanda "perché i linguaggi dinamici scalano male":** in un programma piccolo lo sviluppatore tiene a mente i tipi; in un programma grande e scritto da molti non può più. Senza controlli statici ogni modifica a un'interfaccia può rompere codice lontano senza che nulla lo segnali prima dell'esecuzione; gli strumenti non possono fare refactoring affidabili né navigare il codice con certezza; la documentazione dei tipi è affidata a commenti che invecchiano; i test devono coprire anche ciò che un compilatore verificherebbe gratis. È per questo che l'ecosistema Python ha introdotto i *type hints* (PEP 484) e verificatori statici come mypy e Pyright, e JavaScript ha prodotto TypeScript: sono soft typing in pratica.
## 5. Eccezioni, controlli a runtime, assertion
### Gestione delle eccezioni: good
**Slide p39–p41.** Alcune operazioni possono fallire (leggere una riga oltre la fine del file). In C l'unica soluzione è restituire un codice d'errore e controllarlo a ogni chiamata; poiché una funzione C restituisce un solo valore, il risultato vero va passato tramite un parametro scrivibile, cioè con puntatori: disordinato e soggetto a bug. Con le eccezioni, l'errore viene lanciato e risale lo stack delle chiamate fino al gestore adatto; quasi tutti i linguaggi nuovi le hanno. Le eccezioni funzionano molto meglio con il GC: in C++, che ha eccezioni ma non GC, evitare i leak è complicato (Scott Meyers, *Effective C++*).
**Docente** (`LSD-04 @ 01:25:46`–`01:30:48`). Le eccezioni rendono il codice pulito, robusto e "future proof": un'anomalia viene catturata e, anche senza sapere esattamente cosa sia successo, si può uscire in modo *graceful* senza perdere tutto il lavoro. Lo stack trace mostra "dove è successo cosa e perché". Il principio di fondo è **KISS** (*keep it simple*), come il rasoio di Occam: i codici d'errore del C complicano il valore di ritorno, e un meccanismo più complicato ha più probabilità di contenere errori.
### Controllo degli errori a runtime: not so good, ma necessario
**Slide p42–p47.** I linguaggi dinamici fanno tutti i controlli a runtime, per lo più sui tipi degli argomenti: costoso e più soggetto a errori del controllo a compile time. Ma **anche nei linguaggi statici** ci sono situazioni che nessun sistema di tipi ragionevole (decidibile ed efficiente) può prevedere, e servono controlli a runtime:
- **violazione dei limiti di un array**: accedere al 100° elemento di un array di 10. I linguaggi scalabili la intercettano sempre e lanciano un'eccezione, idealmente con stack trace. Il controllo ha un costo, quindi è bene che il compilatore permetta di disattivarlo quando la velocità conta più della safety. In C non viene mai intercettata e produce core dump e memoria corrotta;
- **errori aritmetici**: la divisione intera per zero lancia un'eccezione nei linguaggi scalabili, così come spesso l'overflow intero; gli errori in virgola mobile (1.0/0.0 = infinito, 0.0/0.0 = NaN) di norma no, nemmeno in Java o OCaml, "per ragioni non chiare".
Principio generale: **rendere il linguaggio safe per default e dare al programmatore la possibilità di scambiare safety con velocità**, idealmente senza riscrivere il codice.
**Docente** (`LSD-04 @ 01:30:48`–`01:38:27`). In Java l'accesso fuori dai limiti produce `ArrayIndexOutOfBoundsException`, evitando segmentation fault ed errori silenti: "non è gratis ma è utilissimo". Disattivare il controllo è "fortemente sconsigliato". Sul floating point avanza un'ipotesi: quando questi linguaggi sono stati progettati le prestazioni in virgola mobile erano così critiche che non si volevano introdurre ritardi. L'uso pratico dell'opzione di disattivazione è misurare quanto pesa un controllo sulle prestazioni, e decidere "se il gioco vale la candela".
> **Nota aggiunta:** il comportamento del floating point è una scelta deliberata dello standard **IEEE 754**: le operazioni eccezionali producono valori speciali (±∞, NaN) e alzano un flag, invece di interrompere il calcolo, così che un'elaborazione numerica lunga possa proseguire e il problema venga gestito alla fine. Esempi di controlli disattivabili: `get_unchecked` in Rust, `-Ounchecked` in Swift, `pragma Suppress` in Ada. In Java non c'è un'opzione, ma il compilatore JIT elimina i controlli sui limiti che dimostra ridondanti.
### Assertion e Design by Contract: very good
**Slide p48–p54.** Quasi tutti i linguaggi, anche il C, hanno `assert`: la dichiarazione che in un certo punto del programma una relazione deve essere vera, per esempio `assert(i == 100);`. È un controllo di sanità integrato. Di solito le assert si attivano in sviluppo e si disattivano a programma finito per velocità. Eiffel ha un sistema molto più elaborato, il **Design by Contract**, integrato nel sistema a oggetti. Usato bene è "un'enorme vittoria": i bug si manifestano molto vicino a dove sono nati, il debugging diventa molto più facile e il linguaggio più scalabile.
- **Assertion**: espressione booleana che deve essere vera in un punto preciso; se falsa a runtime segnala un bug e spesso termina il programma per evitare danni.
- **Contratto**: accordo formale tra un *client* (chi chiama) e un *supplier* (la funzione chiamata), fatto di obblighi e garanzie reciproche:
	- **precondizioni**: requisiti che il chiamante deve soddisfare ("il numero deve essere positivo");
	- **postcondizioni**: garanzie della funzione al termine ("il risultato è la radice quadrata dell'input");
	- **invarianti**: condizioni sempre vere per un oggetto, in particolare prima e dopo ogni metodo pubblico.
- Supporto nativo: **C++26** (`pre`, `post`, `contract_assert`), **Eiffel** (il pioniere), **D** (blocchi `in`, `out`, `invariant`), **Vala** (`requires`, `ensures`).
**Docente** (`LSD-04 @ 01:38:27`–`01:42:35`). Le assertion "evitano di buttare tempo nel testing": sono controlli di sanità che fermano i problemi prima che diventino irrimediabili. Diversamente dalla slide, il docente suggerisce che "spesso è utile tenerle anche dopo". Per la data science scalabile l'obiettivo è un'esecuzione **crash free** e con risultati corretti, non falsati da accessi sbagliati. Eiffel è poco diffuso e difficile, ma molto safe.
> **Nota aggiunta:** in Java le `assert` sono disattivate per default e si attivano con `-ea`; in Python `python -O` le rimuove. Perché riducono il debugging nei grandi sistemi: un errore di logica si scopre di solito dove produce un effetto visibile, spesso lontano e molto dopo il punto in cui è nato. Un contratto violato ferma il programma nel punto esatto e dice anche **di chi è la colpa**: una precondizione violata è un bug del chiamante, una postcondizione violata è un bug della funzione. In un sistema con molti moduli e molti autori è questa attribuzione a far risparmiare tempo. I contratti sono anche documentazione eseguibile delle interfacce.
## 6. Astrazioni
### Supporto per le astrazioni e sistemi di moduli: very good
**Slide p55–p57.** Più un linguaggio aiuta a costruire astrazioni, meglio è: si dice di più con meno codice, e meno codice significa meno bug e sviluppo più rapido. "Un linguaggio senza un buon sistema di moduli è inutile per sviluppare programmi grandi": i moduli permettono di sviluppare e testare parti del programma in isolamento e combinarle dopo, e realizzano librerie riusabili di strutture dati e funzioni. Scritto e corretto una volta, un modulo si importa ovunque, senza reinventare la ruota.
**Docente** (`LSD-04 @ 01:42:35`–`01:55:20`).
- Più un linguaggio permette algoritmi di alto livello validi per tipi di dato diversi, più quegli algoritmi scalano. I moduli esistono in Python, Java e Rust, "in parte in C", che però non protegge i dati dalle funzioni.
- Le strutture dati sono protette perché accessibili solo tramite le funzioni del modulo: "questa è in due parole la traduzione dei benefici di un object oriented fatto bene". Anche le strutture dati di Python sono implementate in modo modulare.
- Il riuso concreto: ci si affida a chi ha implementato **NumPy**, **pandas**, i **wrapper per MPI**, invece di rifarli.
- **Il rovescio: il dependency hell.** Chiede agli studenti qual è il problema della modularità. Un modulo può smettere di essere mantenuto; si può restare legati a una versione vecchia perché le API sono cambiate, e quella versione può essere vulnerabile e dipendere a sua volta da versioni vecchie di altri moduli. In Python il caso emblematico è il passaggio da Python 2 a Python 3. Succede anche in Rust, con crate che funzionano solo con il compilatore sperimentale e magari non girano sul supercalcolatore, che ha versioni vecchie di compilatori, interpreti e librerie.
- **Come se ne esce:** i **virtual environment** congelano la configurazione ma non proteggono dalle vulnerabilità; i **container** congelano la configurazione e permettono di isolare e in parte proteggere anche componenti vulnerabili. "Ovviamente tutto questo fino a un certo punto."
### Programmazione a oggetti: good
**Slide p58–p62.** L'OOP non è la cura di tutti i mali, ma certe applicazioni ne traggono grande beneficio. Il programma si decompone in oggetti con metodi; solo i metodi di un oggetto accedono al suo stato interno, quindi se lo stato cambia in modo inatteso la colpa è di uno di quei metodi (**incapsulamento**, *data hiding*). Con l'**ereditarietà** si creano nuove classi come varianti di quelle esistenti; la chiamata dei metodi è **polimorfica**, cioè il metodo da eseguire si sceglie a runtime. Le simulazioni si prestano all'OOP, i compilatori no: è bene che un linguaggio supporti l'OOP senza imporlo. È vero solo in parte che i programmi a oggetti sono più facili da estendere: se ogni nuovo metodo richiede una sottoclasse, il programma diventa presto macchinoso.
**Docente** (`LSD-04 @ 01:55:20`–`02:00:39`). L'OOP è "sicuramente un passo avanti" perché protegge i dati: incapsulamento forte. Aggiunge un punto che non è nelle slide: i metodi di un oggetto devono essere protetti anche dall'**accesso concorrente**, cioè essere **thread safe**, altrimenti due thread possono lasciare lo stato inconsistente anche se ogni metodo è corretto. "L'encapsulation deve essere garantita anche dal fatto che questi metodi sono thread safe." Mostra i package di Java come risultato di anni di lavoro su metodi thread safe e lock.
Lo riprende all'inizio della lezione successiva (`LSD-05 @ 00:00:43`–`00:10:28`):
- l'incapsulamento aiuta la scalabilità in due sensi: del **codice**, perché lo rende modulare, e dei **dati**, perché riduce la "contaminazione", cioè la manipolazione di un dato da parte di codice non adatto a quel dato;
- **polimorfismo**: tipi collegati da un albero di ereditarietà, con il metodo scelto a runtime (in Java è la JVM a fare il *dynamic dispatch*);
- l'OOP è "una tecnica di astrazione utile, se non abusata", e l'abuso tipico è un albero di ereditarietà troppo profondo. Due modi di estendere il codice: **ereditarietà** (bicicletta → mountain bike) e **aggregazione** (una bicicletta composta da due ruote, un telaio, un manubrio, un cambio). L'aggregazione permette tipi complessi che mantengono la consistenza del dato anche con più thread;
- slogan del docente: "scalabilità fa rima con multithreading, fa rima con avere un dato in formato consistent, fa rima con non gestire l'aritmetica dei puntatori". L'eccezione sono OpenMP e MPI, derivati dal C, che gestiscono i puntatori ma raggiungono prestazioni altissime.
> **Nota aggiunta:** il principio "preferisci la composizione all'ereditarietà" è uno dei cardini di *Design Patterns* (Gamma et al., 1994). Anche le slide Java vs Rust (`Java_vs_Rust` p12) notano che i linguaggi moderni favoriscono composizione e trait rispetto a gerarchie profonde, e Rust non ha ereditarietà classica.
> **Nota aggiunta:** a lezione il docente sembra dire che la maggior parte dei metodi di Java è thread safe. Non è così: le collezioni moderne di `java.util` (`ArrayList`, `HashMap`, `StringBuilder`) non lo sono, per non pagare il costo della sincronizzazione quando non serve. Sono thread safe le classi legacy (`Vector`, `Hashtable`, `StringBuffer`), i wrapper `Collections.synchronized*` e soprattutto il package `java.util.concurrent` (`ConcurrentHashMap`, code bloccanti, `AtomicInteger`). Il tema torna nei capitoli 05 e 06.
Per ereditarietà e polimorfismo si veda anche il capitolo 02 (Simula, `LSD-03 @ 00:17:19`, `00:44:54`).
### Programmazione funzionale: good
**Slide p63–p67.** È in un certo senso duale dell'OOP: invece di decomporre il programma in oggetti, lo decompone in **funzioni**. Richiede che le funzioni siano **di prima classe** (passate come argomenti, restituite, create al volo) e che la ricorsione sia efficiente (**ottimizzazione della ricorsione in coda**), così da poter fare a meno dei cicli. I programmi funzionali evitano il più possibile i dati mutabili e usano molte funzioni piccole. Vantaggi:
- molti algoritmi si esprimono in modo più conciso ed elegante;
- **niente dati mutabili elimina un'ampia classe di bug**;
- i programmi sono molto più facili da **verificare**;
- le funzioni di ordine superiore fattorizzano gli idiomi comuni, e adattare un programma a compiti simili diventa facile.
Pochi linguaggi lo supportano davvero (Lisp, Scheme, OCaml, Standard ML, Haskell): il programmatore medio lo trova difficile e ha fama, in gran parte immeritata, di essere inefficiente.
**Docente** (`LSD-05 @ 00:10:28`–`00:20:29`; vedi anche capitolo 02, `LSD-03 @ 00:23:05`).
- Il linguaggio funzionale e a oggetti "per eccellenza" è **Scala**; subito dietro Python e Java, che hanno seguito il trend funzionale.
- Le funzioni come dati permettono di posticipare il calcolo (**lazy**) e in alcuni casi di risparmiarlo.
- Il punto chiave per la scalabilità: **non si manipola lo stato**. Non c'è una cella di memoria che più thread possono modificare; molto avviene a livello simbolico.
- Ricorsione invece dei cicli, per un codice più asciutto e in alcuni casi più parallelizzabile; i compilatori comunque parallelizzano "discretamente bene" i cicli `for`, come si vedrà con OpenMP.
- Eliminare i dati mutabili (`a = 34`, `a++`) elimina i bachi di **consistency**, cioè i valori transitori e non corretti.
- Contro: "un minimo di scoglio". Opinione del docente: "forse il linguaggio più facile in cui programmare è Java"; per chi non ha esperienza e per compiti specifici, Python.
- Nessun linguaggio pratico è funzionale puro: per fare I/O "deve sporcarsi le mani". Il funzionale puro meglio riuscito è **Haskell**, "pulitissimo" ("io non sarei in grado di programmare in Haskell, e quelli che ci riescono sono ben pagati").
- La fama di inefficienza dipende dall'implementazione: Haskell e Scala sono tutt'altro che lenti.
> **Nota aggiunta:** il docente dice che la valutazione lazy "c'è anche in Python". Python ha valutazione **eager**; offre costrutti lazy (generatori, iteratori, `range`), ma non la valutazione lazy come semantica del linguaggio, che è tipica di Haskell.
> **Nota aggiunta — OOP e FP nello sviluppo su larga scala:** l'OOP organizza il codice attorno ai **dati e al loro stato**: è forte quando il dominio è fatto di entità con identità e ciclo di vita (simulazioni, interfacce grafiche, sistemi gestionali), rende facile aggiungere nuovi tipi che rispettano un'interfaccia, e l'incapsulamento limita chi può cambiare cosa. Il suo punto debole è lo stato mutabile condiviso, che rende difficile ragionare sul codice e pericolosa la concorrenza. La FP organizza il codice attorno alle **trasformazioni**: rende facile aggiungere nuove operazioni su tipi esistenti, le funzioni pure si testano e si compongono in isolamento, e l'immutabilità rende il codice naturalmente parallelizzabile, perché non c'è nulla da proteggere. È il motivo per cui il modello di Spark e MapReduce è funzionale (`map`, `filter`, `reduce` su collezioni immutabili). I linguaggi moderni più usati per sistemi scalabili (Scala, Kotlin, Rust, Java dalle lambda in poi) combinano i due paradigmi: oggetti o moduli per strutturare il sistema, stile funzionale e immutabilità per elaborare i dati.
### Macro strutturali: mostly good
**Slide p68–p70.** Si intendono le macro **strutturali** come in Lisp, non quelle a sostituzione testuale del C. Permettono di incapsulare idiomi ripetuti che non si possono esprimere con funzioni di ordine superiore, per esempio definire nuovi costrutti di controllo (in Lisp si possono creare i propri `if`, `for`, `while`). Problemi: debugging più difficile, codice meno comprensibile perché le macro sembrano funzioni ma si comportano in modo diverso, e scriverne di buone non è banale. Usate bene, alzano molto il livello di astrazione (riferimento: Paul Graham, *On Lisp*). A lezione le macro sono solo richiamate (`LSD-05 @ 00:20:29`); nel 2026 il docente precisa che non se ne parlerà perché non si parlerà di Lisp (`Teams 3 @ 2:43:05`).
### Componenti
**Slide p71–p73.** Un componente è un'unità di funzionalità componibile con altre parti del programma, simile a una libreria ma più autonoma. Architetture: JavaBeans (un solo linguaggio), CORBA e Microsoft COM (più linguaggi). Il vantaggio è che possono essere indipendenti dal linguaggio e dalla posizione; un linguaggio che supporta un'architettura a componenti permette di riusare componenti scritti da altri, anche in altri linguaggi. Di solito è una questione di librerie, ma alcuni linguaggi (C#) sono progettati apposta.
**Docente** (`LSD-05 @ 00:21:27`): in teoria i componenti permettono di mischiare linguaggi diversi, e l'esempio principale è **CORBA**, che però si è rivelato difficile da gestire. "È molto più pulito avere tutto il codice scritto in un unico linguaggio."
### Sintassi e leggibilità
**Slide p74–p76.** È l'aspetto meno interessante dei linguaggi, e paradossalmente l'unico che molti programmatori imparano, ma conta per la scalabilità. Non importa che sia "familiare" (cioè simile al C) ma che sia **coerente**: sintassi barocche con decine di eccezioni, come C++ e soprattutto Perl, rendono i programmi difficili da capire e mantenere perché nessuno ricorda tutti i casi speciali. All'estremo opposto, sintassi minimaliste come quella di Lisp sono difficili da digerire per molti. **Python** è un buon esempio di sintassi amichevole sia per i principianti sia per gli esperti.
**Docente** (`LSD-05 @ 00:21:58`–`00:25:57`; `Teams 3 @ 2:44:42`). Sulla leggibilità "vince Python", che esprime un algoritmo in poche righe; il rovescio è che non permette di manipolare i dati a basso livello e "rende qualcosa" in prestazioni. Python, Java e Rust hanno una sintassi vicina a quella del C, mentre Perl "è completamente incomprensibile"; l'indentazione di Python non è immediata per chi viene da linguaggi a graffe. Nel 2026 aggiunge: "anche se per altri motivi Python non è scalabile, la sua sintassi lo rende da questo punto di vista scalabile", e lo sarebbe di più con la compilazione e maggiori controlli a compile time, che stanno arrivando.
## 7. Edizione 2026: aggiunte in `Teams 3`
Nella lezione del 21/04/2026 il docente ripercorre queste slide "dando informazioni trasversali rispetto alle vecchie registrazioni" (`Teams 3 @ 0:25:03`). Le aggiunte rilevanti:
**Linguaggi, formati e scalabilità dei dati** (`Teams 3 @ 0:15:00`–`0:40:52`). Distingue i linguaggi in generale (regole lessicali, sintattiche, semantiche e pragmatiche per comunicare) dai linguaggi di programmazione. XML, HTML, JSON, DOCX e PDF sono linguaggi di **struttura**, non eseguibili, anche se dentro possono contenere codice eseguibile come le macro (per questo si può prendere un virus da un DOCX). Si può dire che un formato è scalabile?
- **Pro:** una struttura gerarchica ad albero permette di analizzare in parallelo i sottoalberi indipendenti (`0:28:30`).
- **Contro:** i formati testuali occupano più spazio di quelli **binari**, che a parità di byte contengono più informazione (l'esempio del bit field) (`0:30:12`).
- **Serializzazione e deserializzazione** sono parti integranti dell'elaborazione (da file piatto a struttura navigabile in memoria e ritorno) ma sono attività **poco scalabili**: per un grafo molto grande servono file system distribuiti e ridondati che permettano di leggere più parti dello stesso file in parallelo (`0:35:18`–`0:39:10`). "Va bene giocare sul piccolo", ma molti strumenti che funzionano sui dati toy non reggono i dati grandi.
> **Nota aggiunta:** è il motivo per cui nel mondo big data si usano formati binari e **colonnari** come Parquet e ORC (con Arrow per la rappresentazione in memoria): comprimono meglio, permettono di leggere solo le colonne necessarie e sono divisi in blocchi leggibili in parallelo, mentre CSV e JSON vanno letti e interpretati per intero, riga per riga.
**GC e sistemi operativi** (`Teams 3 @ 1:25:01`–`1:33:12`). Rispondendo a una domanda sul modulo `gc` di Python, il docente spiega che in alcuni casi il GC è dannoso: un kernel usa poca memoria ben controllata e deve rispondere in tempo reale senza rallentamenti, ed è quello che ha fatto Apple rinunciando al GC. L'analogia è quella dei cassonetti: se sono pieni bisogna aspettare che passi chi li svuota.
**Rust e il ****`null`** (`Teams 3 @ 2:18:51`–`2:21:20`). Il C ha "un elefante nella cristalleria", il `null`. In Rust una funzione non può restituire `null`: restituisce sempre una "scatola", un `Result`, che contiene il valore oppure un errore. Non esistono null pointer in giro, il che "provoca molti meno errori a runtime". In Java invece il null pointer esiste ed è "uno dei problemi di Java"; Kotlin e Scala controllano i null a compile time.
> **Nota aggiunta:** Rust usa due tipi: `Option<T>` (`Some(valore)` oppure `None`) per un valore che può mancare, e `Result<T, E>` (`Ok(valore)` oppure `Err(errore)`) per un'operazione che può fallire. Il compilatore obbliga a gestire entrambi i casi. Tony Hoare, che introdusse il riferimento nullo in ALGOL W nel 1965, lo ha definito il suo "errore da un miliardo di dollari". In Java esiste `Optional` dalla versione 8, ma non impedisce l'uso di `null`.
**Elixir** (`Teams 3 @ 2:11:25`). Citato come linguaggio "nato per essere scalabile", di cui il docente intendeva parlare; nel seguito dell'edizione 2026 è sostituito da Julia (capitolo 07).
## Collegamento con il Questionario 3
<table header-row="true">
<tr>
<td>Domanda</td>
<td>Slide</td>
<td>Video</td>
<td>Qui</td>
</tr>
<tr>
<td>1. GC e scalabilità: vantaggi, costi in tempo e spazio</td>
<td>`MDA3` p2–p11</td>
<td>`LSD-03 @ 01:15:42`–`01:18:08`, `01:26:32`–`01:35:02`; `LSD-04 @ 00:06:53`–`00:24:26`; `Teams 3 @ 0:40:52`–`0:46:00`, `1:10:00`–`1:33:12`</td>
<td>§2</td>
</tr>
<tr>
<td>2. gestione manuale e strutture dati semplici</td>
<td>`MDA3` p3–p6, p14</td>
<td>`LSD-03 @ 01:18:08`–`01:26:32`; `LSD-04 @ 00:08:21`–`00:17:34`, `00:26:14`–`00:28:34`</td>
<td>§2 Senza GC</td>
</tr>
<tr>
<td>3. aritmetica dei puntatori come barriera</td>
<td>`MDA3` p12–p21</td>
<td>`LSD-03 @ 00:01:25`–`00:13:21`, `01:18:50`–`01:21:11`; `LSD-04 @ 00:24:26`–`00:26:14`, `00:39:12`–`00:54:26`; `Teams 3 @ 1:35:00`–`1:49:27`</td>
<td>§3</td>
</tr>
<tr>
<td>4. micro contro macro-ottimizzazioni</td>
<td>`MDA3` p13, p17</td>
<td>`LSD-04 @ 00:25:38`–`00:26:14`, `00:46:16`–`00:46:47`; `Teams 3 @ 1:43:49`–`1:45:17`</td>
<td>§3 (con nota sul pointer aliasing)</td>
</tr>
<tr>
<td>5. type checking statico: produttività e riuso</td>
<td>`MDA3` p22–p25</td>
<td>`LSD-04 @ 00:54:26`–`01:04:29`</td>
<td>§4</td>
</tr>
<tr>
<td>6. type inference e dichiarazioni esplicite</td>
<td>`MDA3` p26–p27, p33–p34</td>
<td>`LSD-04 @ 01:05:00`–`01:06:36`, `01:11:32`–`01:12:45`, `01:22:22`–`01:22:54`</td>
<td>§4 (con nota)</td>
</tr>
<tr>
<td>7. statica e dinamica; perché i dinamici scalano male</td>
<td>`MDA3` p25, p31–p38</td>
<td>`LSD-04 @ 01:18:46`–`01:25:46`; `LSD-05 @ 01:48:09`–`01:50:35`; `Teams 3 @ 1:50:00`–`2:11:25`</td>
<td>§4 (con nota)</td>
</tr>
<tr>
<td>8. controlli a runtime: array e aritmetica</td>
<td>`MDA3` p42–p47</td>
<td>`LSD-04 @ 01:30:48`–`01:38:27`; `Teams 3 @ 2:25:07`–`2:30:00`</td>
<td>§5</td>
</tr>
<tr>
<td>9. assertion e Design by Contract</td>
<td>`MDA3` p48–p54</td>
<td>`LSD-04 @ 01:38:27`–`01:42:35`; `Teams 3 @ 2:30:00`–`2:31:25`</td>
<td>§5 (con nota)</td>
</tr>
<tr>
<td>10. astrazioni, OOP e FP</td>
<td>`MDA3` p55–p67</td>
<td>`LSD-04 @ 01:42:35`–`02:00:39`; `LSD-05 @ 00:00:11`–`00:20:29`; `Teams 3 @ 2:36:56`–`2:43:05`</td>
<td>§6 (confronto OOP/FP nella nota)</td>
</tr>
</table>
## Punti incerti della trascrizione
- `LSD-04 @ 00:46:16` — il docente dice "micro ottimizzazioni" dove la slide p17 dice macro-ottimizzazioni: probabile lapsus
- `LSD-04 @ 00:51:26` — GNOME Shell e Mono citati come "scritti interamente in C++": GNOME Shell è in C e JavaScript, Mono in C e C#
- `LSD-04 @ 01:21:51` — "Java o Caml": la slide p33 cita solo OCaml, possibile errore di trascrizione
- `LSD-04 @ 01:47:22` — una libreria trascritta come "Neo, [network.io](http://network.io)", forse NetworkX `[?]`
