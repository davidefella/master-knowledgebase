# 02 - Storia dei linguaggi di programmazione

> Fonte Notion: https://app.notion.com/p/3dd12abc808d8199b7c3f15a79faf0df — ultima modifica 2026-09-17T09:19:55.175Z

Fonti: slide `MDA2_PLHistory`, lezioni `LSD-02` (00:22 → fine) e `LSD-03` (00:00 → 01:15).
> **Nota aggiunta:** il testo delle slide segue da vicino il capitolo storico del manuale di Gabbrielli e Martini, *Programming Languages: Principles and Paradigms* (Springer), utile se si vuole approfondire.
Il filo del capitolo, nelle parole del docente: nella storia dei linguaggi "non si è buttato via niente", e spesso non ha vinto il linguaggio migliore ma quello che in un certo momento incontrava i gusti e i requisiti della maggior parte degli utenti (`LSD-02 @ 00:22:09`).
## 1. Cosa ha guidato lo sviluppo dei linguaggi
Le slide elencano cinque fattori.
<table header-row="true">
<tr>
<td>Fattore</td>
<td>Slide</td>
<td>Esempi del docente</td>
</tr>
<tr>
<td>**Hardware**</td>
<td>tipo e prestazioni dei dispositivi disponibili hanno influenzato i linguaggi</td>
<td>macchine lente e costose → l'unico requisito era sfruttare al massimo le poche risorse</td>
</tr>
<tr>
<td>**Applicazioni**</td>
<td>dal solo calcolo numerico a campi che richiedono informazione non numerica; nuovi campi chiedono linguaggi con proprietà specifiche (AI e manipolazione simbolica, videogiochi)</td>
<td>applicazioni di rete, calcolo parallelo (OpenMP e MPI come evoluzione di C e Fortran), AI, grafica 3D</td>
</tr>
<tr>
<td>**Nuove metodologie**</td>
<td>in particolare la *programming in the large*: esempio principale la programmazione a oggetti</td>
<td>l'OOP nasce per modularizzare e trasformare il codice già scritto in black box</td>
</tr>
<tr>
<td>**Implementazione**</td>
<td>implementare un costrutto permette di capirne la validità e l'uso pratico</td>
<td>le prime JVM: approccio utile ma lento e affamato di memoria, e Java è rimasto fuori da alcuni ambienti</td>
</tr>
<tr>
<td>**Teoria**</td>
<td>gli studi teorici selezionano strutture e strumenti: eliminazione del `goto`, sistemi di tipi raffinati</td>
<td>lambda calcolo → linguaggi funzionali; programmazione logica → SQL</td>
</tr>
</table>
Due osservazioni del docente (`LSD-02 @ 00:24:10`–`00:24:55`):
- a volte l'idea di un linguaggio o di un modello di calcolo **ha preceduto l'hardware** capace di eseguirlo, e non ha avuto successo finché quell'hardware non è arrivato;
- il successo di un linguaggio dipende da **quali requisiti contano in quel momento storico**.
### Dall'efficienza alla sicurezza
È lo spostamento più importante (`LSD-02 @ 00:25:34`–`00:32:36`):
- **Ieri:** calcolatori semplici, lenti e costosi. Il requisito era sfruttare al massimo risorse limitate, a scapito della facilità di programmazione. Anche il FORTRAN metteva le prestazioni al primo posto e fu progettato pensando a una macchina precisa, l'IBM 704 (slide).
- **Oggi:** un linguaggio moderno deve essere il più astratto possibile, semplice da programmare senza pensare ai dettagli dell'hardware (i cui limiti però restano), e soprattutto deve garantire **sicurezza**.
"Sicurezza" in inglese ha due significati distinti, con una piccola sovrapposizione:
<table header-row="true">
<tr>
<td></td>
<td>Safety</td>
<td>Security</td>
</tr>
<tr>
<td>Idea</td>
<td>"non si fa male nessuno": il programma funziona come previsto</td>
<td>il sistema resiste a usi illeciti e ad attacchi</td>
</tr>
<tr>
<td>Per un linguaggio o un algoritmo</td>
<td>non va in crash, non causa anomalie né interruzioni del servizio</td>
<td>confidenzialità (le informazioni arrivano solo a chi deve riceverle), resistenza ai cyberattacchi, nessun uso per fini diversi da quelli previsti</td>
</tr>
<tr>
<td>Esempio del docente</td>
<td>un programma che non corrompe la memoria</td>
<td>un'app di messaggistica in cui nessun terzo può leggere i messaggi; il caso dei funzionari americani che hanno usato Signal per informazioni riservate è un problema di security</td>
</tr>
</table>
Fino agli anni '90 e 2000, dice il docente, safety e security non erano tra i requisiti; oggi sono richieste con forza.
### Le applicazioni guidano i linguaggi
"È vero che poi tutto si può fare in C, ma non tutto si può fare bene in C" (`LSD-02 @ 00:35:02`). Un'applicazione di rete chiede un linguaggio che semplifichi la rete; un'analisi di dati veloce chiede multithreading, parallelismo e distribuzione; un word processor si accontenta di una gestione della memoria semplice e locale. Le applicazioni di successo guidano sia la nascita di nuovi linguaggi sia l'evoluzione di quelli vecchi.
**Il caso Julia** (`LSD-02 @ 00:36:39`): linguaggio per il calcolo parallelo con caratteristiche innovative, che però fatica a imporsi per il peso del codice legacy scritto in altri linguaggi. Usare più linguaggi insieme aumenta la complessità e richiede competenze su tutti.
Il punto del corso, detto con una provocazione: si potrebbe usare solo Python e ignorare prestazioni e scalabilità. Ma i sistemi a cui Python si appoggia tramite API hanno al loro interno altri linguaggi e altri meccanismi: si possono usare come black box, oppure capire come funzionano per ottenere prestazioni migliori o capire perché non sono adeguate (`LSD-02 @ 00:37:43`).
Altri esempi del docente di domini che hanno richiesto strumenti specifici: l'intelligenza artificiale ("l'elefante nella cristalleria"), la grafica 3D e i videogiochi, con VTK e ParaView per la visualizzazione scientifica e OpenGL e Vulkan (`LSD-02 @ 00:38:53`–`00:41:29`).
> **Nota aggiunta:** VTK è una libreria, ParaView un'applicazione costruita su VTK, OpenGL e Vulkan sono API grafiche: non sono linguaggi di programmazione in senso stretto, anche se il docente li cita come tali. Il punto resta valido: un nuovo dominio produce strumenti dedicati.
### La teoria: paradigmi e `goto`
Il lambda calcolo ha influenzato i linguaggi funzionali, prima confinati all'accademia (ML) e poi usati in ambito scientifico e commerciale. Lo studio dei linguaggi a oggetti, la programmazione strutturata e quella logico-dichiarativa (da cui SQL) hanno fatto lo stesso (`LSD-02 @ 00:42:13`–`00:47:19`).
Sul paradigma a oggetti il docente distingue: **Java** è un linguaggio a oggetti ben definito; **C++** è stato costruito incrementalmente sul C, con forti limiti nella bontà dell'implementazione a oggetti, e alcune scelte iniziali oggi si pagano in scarsa manutenibilità. In C e C++ il cittadino di prima classe è la funzione, non il dato: si può applicare qualsiasi funzione a una struttura dati "nuda". In Python invece l'allocazione delle strutture dati è trasparente e non si rischiano quei danni.
**Il ****`goto`** (slide; `LSD-02 @ 00:50:46`–`01:01:04`). Con la programmazione strutturata non serve più saltare a una riga del codice: si chiama una funzione, riutilizzabile. Il salto incondizionato è scomparso da molti linguaggi, ma esiste ancora a livello di CPU come istruzione `jump`. Quello che non può scomparire è il **salto condizionato** (tipo `jnz`, *jump if not zero*): ogni `if` di qualsiasi linguaggio, Python compreso, diventa un salto condizionato eseguito dalla CPU. È ciò che rende pratico implementare qualsiasi algoritmo, cioè la Turing-completezza. Le eccezioni sono una cerchia ristrettissima, come i *One Instruction Set Computer*. Un cambio di paradigma vero, secondo il docente, arriverebbe solo col calcolo quantistico, utile per alcuni problemi ma non per tutti.
> **Nota aggiunta:** la lettera di Edsger Dijkstra *Go To Statement Considered Harmful* è del 1968 (Communications of the ACM); il docente colloca la polemica negli anni '80, quando in effetti il dibattito era ancora vivo. Sulla Turing-completezza: in senso stretto basta una forma di scelta condizionata unita a memoria illimitata; il salto condizionato è il modo in cui le CPU la realizzano.
## 2. Il paradigma decide come scala il codice
Il docente ordina i quattro paradigmi principali per scalabilità (`LSD-03 @ 00:26:59`, `00:46:30`, `00:57:59`):
<table header-row="true">
<tr>
<td>Paradigma</td>
<td>Esempi</td>
<td>Scalabilità secondo il docente</td>
<td>Analogia del cocktail</td>
</tr>
<tr>
<td>**Imperativo**</td>
<td>FORTRAN, C</td>
<td>la meno scalabile</td>
<td>il cocktail lo fate voi, da zero</td>
</tr>
<tr>
<td>**A oggetti**</td>
<td>Simula, Java</td>
<td>scala bene sul **codice**</td>
<td>lo fate voi, ma con gli ingredienti già pronti</td>
</tr>
<tr>
<td>**Funzionale**</td>
<td>LISP, ML</td>
<td>la migliore sui **dati**; difficile da programmare</td>
<td>non lo toccate: date istruzioni a una macchina che lo prepara</td>
</tr>
<tr>
<td>**Logico-dichiarativo**</td>
<td>PROLOG, SQL</td>
<td>la più promettente: delega di più alla macchina</td>
<td>chiedete al barista; il risultato dipende da quanto è bravo</td>
</tr>
</table>
## 3. I linguaggi storici
<table header-row="true">
<tr>
<td>Linguaggio</td>
<td>Anno</td>
<td>Autori</td>
<td>Contributo principale</td>
</tr>
<tr>
<td>FORTRAN</td>
<td>1957</td>
<td>gruppo di John Backus (IBM)</td>
<td>primo vero linguaggio imperativo ad alto livello; espressioni aritmetiche simboliche</td>
</tr>
<tr>
<td>LISP</td>
<td>fine anni '50</td>
<td>—</td>
<td>programmazione di ordine superiore, heap e garbage collector</td>
</tr>
<tr>
<td>ALGOL</td>
<td>fine anni '50</td>
<td>—</td>
<td>blocchi `begin`/`end`, stack dei record di attivazione, scope statico</td>
</tr>
<tr>
<td>Simula</td>
<td>dal 1962 (Simula67)</td>
<td>Nygaard e Dahl</td>
<td>classi, oggetti, sottotipi, dynamic dispatch, coroutine</td>
</tr>
<tr>
<td>C</td>
<td>1972</td>
<td>Ritchie e Thompson (AT&T Bell Labs)</td>
<td>programmazione di sistema portabile, accesso diretto a memoria e dispositivi</td>
</tr>
<tr>
<td>ML</td>
<td>metà anni '70</td>
<td>gruppo di Robin Milner (Edimburgo)</td>
<td>type safety dimostrabile, type inference, polimorfismo parametrico</td>
</tr>
<tr>
<td>PROLOG</td>
<td>1972</td>
<td>Colmerauer e Roussel; teoria di Kowalski</td>
<td>primo linguaggio di programmazione logica</td>
</tr>
<tr>
<td>Java</td>
<td>1990–1995</td>
<td>Green team di James Gosling (Sun)</td>
<td>OOP senza aritmetica dei puntatori, bytecode e JVM, rete e thread nativi</td>
</tr>
</table>
> **Nota aggiunta:** le slide non datano LISP e ALGOL. LISP è di John McCarthy (1958, MIT); ALGOL 58 e ALGOL 60 sono il frutto di un comitato internazionale. Java è stato rilasciato pubblicamente nel 1995; Python è del 1991.
### FORTRAN
**Slide.** Considerato il primo vero linguaggio imperativo ad alto livello, sviluppato dal gruppo di John Backus nel 1957 per applicazioni numerico-scientifiche. In un'epoca in cui si programmava solo in assembly e la preoccupazione principale era l'efficienza, non poteva ignorare le prestazioni del codice compilato: fu progettato considerando le caratteristiche dell'IBM 704. Eppure già la prima versione era un linguaggio ad alto livello in senso moderno, con molti costrutti indipendenti dalla macchina, e fu il primo a permettere l'uso diretto di **espressioni aritmetiche simboliche**.
**Docente** (`LSD-02 @ 01:02:44`–`01:06:29`). *FORmula TRANslation*. Prima c'erano codice macchina e schede perforate: il FORTRAN era leggibile e manutenibile. È un linguaggio "verticale", rimasto nel suo campo, ed esiste ancora oggi perché è diventato legacy: c'è chi continua a scriverci codice, e molto codice scritto per versioni vecchie deve continuare a funzionare. La longevità si deve proprio al suo livello di astrazione: permetteva di scrivere espressioni, non solo di "zappettare" numeri nel codice.
### LISP
**Slide.** Linguaggio funzionale: un programma è una sequenza di espressioni da valutare, alcune delle quali sono definizioni di funzioni. Tipicamente interpretato, in un ambiente interattivo. Contributi:
- **programmazione di ordine superiore**: funzioni che accettano funzioni come parametri o le restituiscono come risultato;
- **gestione dinamica della memoria** con heap e **garbage collector**.
Altre caratteristiche, come lo **scope dinamico** implementato con le A-list, sono rimaste confinate al LISP.
**Docente** (`LSD-02 @ 01:06:29`–`01:10:29`). L'heap è la memoria allocata a tempo di esecuzione per grandi moli di dati: quella della `malloc` in C e della `new` in Java. Il garbage collector è il componente che a runtime ripulisce la memoria non più usata per riallocarla, ed evita i problemi della `free` esplicita, che C e C++ non hanno. Java, che ne ha fatto un punto di forza, lo eredita dal LISP. Lo scope dinamico, invece, semplifica solo l'implementazione del linguaggio e rende la visibilità delle variabili non locali più difficile da capire per un umano: il LISP è "assolutamente difficile da comprendere".
### ALGOL
**Slide.** Nato come reazione al FORTRAN. Introduce lo **stack dei record di attivazione**, usa blocchi di istruzioni delimitati da `begin` ed `end` (primo linguaggio con questa sintassi, poi ripresa dal Pascal) e per anni è stato lo standard de facto per descrivere gli algoritmi.
**Docente** (`LSD-02 @ 01:10:29`–`01:12:06`). I record di attivazione tengono traccia dello stato dell'ambiente (i valori delle variabili) quando una funzione chiama un'altra funzione, anche se stessa: sono ciò che rende gestibile la **ricorsione** e permette di realizzare lo **scope statico**, più difficile da implementare dello scope dinamico del LISP ma molto più leggibile. ALGOL e Pascal non hanno avuto successo industriale ma sono stati preziosi nella didattica.
> **Nota aggiunta:** le innovazioni di ALGOL in risposta al FORTRAN, in sintesi: struttura a blocchi annidati con variabili locali, scope statico (lessicale), ricorsione, sintassi definita formalmente con la notazione BNF (Backus-Naur Form, introdotta proprio per ALGOL 60), passaggio dei parametri per valore e per nome. È il capostipite della famiglia a cui appartengono Pascal, C e Simula.
### C
**Slide.** Progettato da Dennis Ritchie e Ken Thompson ai Bell Labs di AT&T come linguaggio di programmazione di sistema per Unix, diventa presto general purpose. Il nome viene dal linguaggio B, a sua volta versione ridotta del BCPL. Rispetto alla famiglia ALGOL offre più accesso alle funzionalità di basso livello: si può accedere direttamente ai caratteri di un terminale, gestire esplicitamente la memoria e i dispositivi mappati in memoria. Si afferma per la sintassi compatta e la possibilità di tradurre i programmi in codice macchina efficiente.
Struttura a blocchi semplificata: **niente funzioni annidate**, il che semplifica la gestione degli ambienti e il passaggio di funzioni come parametri. La presenza esplicita di **puntatori** manipolabili, equivalenti agli array, permette operazioni potentissime ma causa errori insidiosi. Insieme alla **mancanza di un sistema di tipi forte**, è il punto critico del linguaggio quando serve più affidabilità che efficienza.
**Docente** (`LSD-02 @ 01:12:06`–`01:27:10`, `LSD-03 @ 00:00:10`–`00:13:21`).
*Il punto di forza è anche il problema.* Nel C tutto si basa sui puntatori, cioè sull'accesso diretto agli indirizzi di codice e dati. Per un device driver o per le parti del sistema operativo che parlano con l'hardware (GPU, schede di rete, dischi, audio mappati in memoria) è perfetto: legge e scrive nel modo più diretto possibile, con prestazioni ottime, ed è molto meglio dell'assembly. Il C permette di fare tutto quello che si fa in assembly, a un livello di astrazione più alto, ma senza limitare nulla, e quindi senza proteggere da nulla. È "come fare il fornaio e prendere il pane dal forno a mani nude". L'unico strumento è il debugger.
*Scalabilità.* Il C è così semplice che lascia tutti i problemi di scalabilità allo sviluppatore. Appena un algoritmo lavora su problemi non banali, i dati non stanno nello stack e bisogna gestire puntatori all'heap, esponendosi a enormi problemi di safety e security.
*Tipi deboli.* Senza un sistema di tipi forte si può passare un intero, rileggerlo come floating point e poi come stringa: al massimo si ottiene un warning.
*Comportamenti non definiti.* Il C è stato creato da sviluppatori e non definito in modo formale: alcuni comportamenti non sono specificati dal linguaggio, quindi codice che negli anni '90 funzionava può comportarsi in modo imprevedibile con un compilatore nuovo.
*Dove non usarlo.* Il docente non scriverebbe mai in C il controllo di una centrale nucleare o di un'auto a guida autonoma: non ha garanzie di safety né di security, e tutto ciò che si fa in quella direzione è "un aggiustamento a posteriori".
*Crash ed errori silenti* (`LSD-03 @ 00:03:15`–`00:11:07`). Leggere o scrivere nella cella di memoria sbagliata, tipicamente con l'aritmetica dei puntatori, ha due esiti possibili:
1. il sistema operativo se ne accorge e uccide il processo: **segmentation fault**, crash;
2. l'accesso avviene in un'area che il sistema non protegge, e il programma continua con dati sbagliati: **errore silente**.
Il secondo è molto peggio: un navigatore che manda nel posto sbagliato, un messaggio consegnato alla persona sbagliata, il calcolo di un ponte sbagliato senza che nessuno se ne accorga. Salvare checkpoint dei risultati parziali protegge dai crash (il docente racconta di aver perso un mese di calcolo su GPU per un crash), ma non dagli errori silenti. Paradossalmente, più memoria libera c'è, meno probabile è il segmentation fault e più probabile l'errore silente.
*Oggi.* Linux è scritto integralmente in C e alcune parti vengono riscritte in **Rust**, un linguaggio "non completamente diverso dal C" che corregge la gestione "ballerina" della memoria con regole rigide sull'heap.
> **Nota aggiunta:** il supporto a Rust è entrato ufficialmente nel kernel Linux con la versione 6.1 (dicembre 2022), inizialmente per driver.
**Punti di forza e debolezze del C, in sintesi:**
<table header-row="true">
<tr>
<td>Punti di forza</td>
<td>Debolezze</td>
</tr>
<tr>
<td>accesso diretto a memoria e dispositivi: ideale per kernel e driver</td>
<td>aritmetica dei puntatori: accessi fuori dai limiti, dangling pointer, corruzione della memoria</td>
</tr>
<tr>
<td>codice macchina efficiente, prestazioni prevedibili</td>
<td>gestione manuale dell'heap (`malloc`/`free`): memory leak, double free</td>
</tr>
<tr>
<td>sintassi compatta, linguaggio piccolo e portabile</td>
<td>sistema di tipi debole: conversioni implicite e cast senza controlli</td>
</tr>
<tr>
<td>puntatori a funzione: funzioni come parametri in modo semplice</td>
<td>comportamenti non definiti, dipendenti dal compilatore</td>
</tr>
<tr>
<td>enorme base di codice e librerie testate da decenni</td>
<td>errori silenti: il fallimento peggiore per sistemi critici e grandi quantità di dati</td>
</tr>
</table>
### Simula
**Slide.** Discendente di ALGOL 60, "caso da manuale di una tecnologia troppo avanzata per il suo tempo". Sviluppato dal 1962 al Norwegian Computing Centre da Kristen Nygaard e Ole-Johan Dahl, come estensione di ALGOL per la **simulazione a eventi discreti** (situazioni di carico e code, per misurare tempi medi di attesa, lunghezza delle code). Simula67 introduce per la prima volta **classe, oggetto, sottotipo e dynamic method dispatch**, più chiamata per riferimento, puntatori e **coroutine** (vicine al concetto moderno di thread). È il primo linguaggio a oggetti e ha influenzato Smalltalk e C++, anche se la metafora biologica dell'"oggetto" arriverà con Smalltalk e Alan Kay.
Una classe in Simula è una procedura che, terminando, lascia il proprio record di attivazione sullo stack e restituisce un puntatore a esso: quel record, con le variabili locali (le variabili d'istanza) e i puntatori alle funzioni locali (i metodi), è un oggetto.
**Docente** (`LSD-03 @ 00:13:21`–`00:22:25`). Il nome dice tutto: nel mondo reale l'evoluzione nel tempo nasce dall'interazione tra oggetti, e un programma a oggetti in esecuzione è un insieme di oggetti che interagiscono. Perfetto per le simulazioni, e ogni esecuzione può dare risultati diversi.
*A cosa serve l'ereditarietà?* Una classe `Persona`, una sottoclasse `Studente`, una sotto-sottoclasse `StudenteUniversitario`. Chi eredita riceve la struttura del dato e i metodi che vi accedono, senza reinventarli: è uno dei principi della scalabilità. Il risparmio non è di memoria (un oggetto spesso occupa più di una struttura dati equivalente, e ogni oggetto ha il proprio stato) ma di **codice**: se ne scrive meno e ci si appoggia su codice già testato, con una certa garanzia di safety. Inoltre i linguaggi a oggetti moderni possono fare a meno dell'aritmetica dei puntatori esplicita.
*Polimorfismo* (`LSD-03 @ 00:44:54`). Studenti, docenti e personale sono tutti persone: sull'autobus vengono trattati allo stesso modo, in aula ognuno ha il suo ruolo. Gli stessi metodi si applicano a tipi diversi, che si comportano diversamente a seconda del contesto.
### ML
**Slide.** Nato come *Meta Language* per un sistema semi-automatico di dimostrazione di proprietà dei programmi, sviluppato dal gruppo di Robin Milner a Edimburgo dalla metà degli anni '70. Diventa presto un linguaggio vero, adatto alla manipolazione simbolica. Come in LISP, un programma è un insieme di definizioni di funzioni; alla parte puramente funzionale si aggiungono costrutti imperativi, in particolare l'assegnamento limitato alle *reference cell*.
Il contributo più importante riguarda i **tipi**:
- **type safety** con una definizione rigorosa, che esclude in modo dimostrabile errori a runtime non segnalati dovuti a violazioni di tipo;
- sistema di tipi **statico**: il type checker determina il tipo di ogni espressione e non c'è modo di cambiarlo. Se un'espressione è intera, ogni sua valutazione che termina produce un intero;
- **type inference**: il programmatore può omettere i tipi e il sistema li deduce dall'uso. Meccanismi simili erano stati studiati nel lambda calcolo, ma ML è il primo linguaggio a includerla;
- **polimorfismo parametrico**: variabili di tipo istanziate in modo coerente con tipi concreti.
**Docente** (`LSD-03 @ 00:23:05`–`00:31:02`, `00:42:32`–`00:44:23`).
*Funzionale puro.* Non ha stato: niente assegnamento, la variabile non è una scatola in cui mettere un valore. Il programma è un meccanismo di valutazione e riscrittura di espressioni, e non modifica la memoria. Ma un programma che non ha effetti sul mondo sarebbe inutile, per questo in ML e negli altri linguaggi funzionali sono stati "retrofittati" costrutti imperativi. Oggi quasi tutti i linguaggi, Python e Java compresi, hanno una parte funzionale.
*Perché scala sui dati.* Non modificare le celle di memoria, o modificarle il meno possibile, rende il programma più safe. Non significa che il risultato sia corretto (gli errori semantici restano), ma sparisce l'errore silente dovuto all'accesso alla cella sbagliata. Un sistema di tipi funzionale statico è "forse il massimo" per la safety: "una volta che nasce gatto non lo posso trattare come cane", mentre in C una stringa può essere letta come float o come intero senza avvisi.
*E Python?* Ha parti funzionali ma non è funzionale puro: sotto ci sono l'approccio a oggetti e quello imperativo, e i suoi tipi di dato non sono adatti a grandi dimensioni. La soluzione è invocare librerie scritte in altri linguaggi.
#### Excursus: compilatore e interprete
Il docente lo mostra dal vivo (`LSD-03 @ 00:32:12`–`00:42:32`):
- **Interprete** (Python): un prompt interattivo valuta ed esegue subito ogni riga. Come un interprete umano che traduce frase per frase.
- **Compilatore** (C con `gcc prova.c -o prova.exe`): traduce l'intero sorgente in un eseguibile (un ELF a 64 bit, dinamicamente linkato, che richiede librerie del sistema operativo). Come un traduttore che consegna l'intero libro tradotto. Con `gcc -S` si vede il passaggio intermedio in assembly.
La compilazione è un passo in più, fatto in più fasi e con ottimizzazioni, quindi produce codice più veloce. L'interprete è più lento, ma secondo il docente "è un controllo in più": valuta ciò che esegue e può "addolcire la pillola", dando maggiore safety.
> **Nota aggiunta:** la distinzione riguarda le implementazioni, non i linguaggi: esistono compilatori per linguaggi di solito interpretati e viceversa, e molte implementazioni moderne sono ibride (Java compila in bytecode poi interpretato e compilato just-in-time; CPython compila in bytecode prima di interpretarlo). La safety dipende soprattutto dai controlli che il linguaggio impone, statici o a runtime, più che dal fatto di essere interpretato.
### PROLOG
**Slide.** Definito teoricamente da Kowalski negli anni '70, è il primo linguaggio di programmazione logica ed è ancora disponibile. Le idee risalgono a Gödel e Herbrand; le basi teoriche solide sono di Robinson negli anni '60, con l'algoritmo di **unificazione** e la **risoluzione**, un meccanismo di deduzione per dimostrare teoremi in logica del primo ordine. La risoluzione però non fornisce un risultato osservabile come una computazione: serve la **SLD-risoluzione** di Kowalski (1974), che dimostra una formula calcolando esplicitamente i valori delle variabili che la rendono vera, e quei valori sono il risultato. Il linguaggio fu sviluppato da Alain Colmerauer e Philippe Roussel, che lavoravano a un formalismo per il linguaggio naturale basato sulla dimostrazione automatica: prima implementazione nel 1972, standard ISO negli anni '90.
**Docente** (`LSD-03 @ 00:46:30`–`00:57:29`). Nella programmazione logica si dice solo **da dove si parte e dove si vuole arrivare**, cioè regole e obiettivo, e il calcolatore sceglie come arrivarci. Non è come un LLM: ChatGPT "scimmiotta" quello che ha letto e lo applica alla cieca, mentre un sistema logico fa passi deduttivi deterministici e riproducibili. Molto più lento, ma molto più affidabile e degno di fiducia.
*SQL come esempio di dichiaratività.* In una `SELECT` non si spiega al sistema come trovare i dati, si descrive cosa si vuole: "trovami gli studenti con i capelli rossi nati tra tale anno e tale anno". È l'RDBMS a decidere come cercare, e più diventa furbo meglio lo fa, senza cambiare il codice di chi scrive la query. Prima dei database relazionali bisognava scrivere a mano il codice che scorreva tutte le tabelle.
> **Nota aggiunta:** domini in cui la programmazione logica mantiene un vantaggio oggi: motori di regole e sistemi esperti (verifica di conformità, configurazione di prodotti); **Datalog** per l'analisi statica del codice (CodeQL usa un linguaggio derivato da Datalog) e per interrogazioni ricorsive su grafi; *constraint logic programming* per scheduling e pianificazione; ragionamento su ontologie e knowledge graph. In IBM Watson, Prolog è stato usato per il pattern matching sugli alberi sintattici del linguaggio naturale. Il vantaggio è lo stesso indicato dal docente: risultati deduttivi, spiegabili e riproducibili.
### Java
**Slide.** Sviluppato dal *Green team* guidato da James Gosling alla Sun, a partire dal 1990, come linguaggio basato su una nuova implementazione di C++ per piccoli dispositivi in rete collegati a un televisore. La prima versione del 1992 fu ignorata. Nel 1993 arriva **Mosaic**, il primo browser, e il team capisce il potenziale del linguaggio per il web: con la banda ridotta dei computer domestici e i server sovraccarichi, si potevano inviare piccoli programmi, le **applet**, da eseguire sul client, riducendo il carico del server. Requisiti:
- **portabilità**: l'architettura della macchina remota non è nota, quindi su ogni client deve esistere un'implementazione del linguaggio, difficile se il linguaggio è grande o complicato;
- **sicurezza**: eseguire codice ricevuto dalla rete richiede garanzie precise. Oltre al dynamic method dispatch, Java permette il **caricamento dinamico delle classi**: se durante l'esecuzione serve una classe assente, magari remota, viene caricata nella JVM, e il programma può partire anche se alcuni componenti mancano.
**Docente** (`LSD-03 @ 00:57:59`–`01:15:42`). Java è "il più grande risultato" della programmazione a oggetti. Tre vantaggi principali:
1. **OOP fatto bene, senza puntatori** e senza aritmetica dei puntatori: molto più safe del "mezzo passo falso" del C++;
2. **rete nativa**, nato insieme al web, con supporto al calcolo distribuito;
3. **multithreading nativo**: più flussi di esecuzione contemporanei, ideale anche per simulare oggetti che si muovono in modo concorrente.
*Le applet e la scalabilità.* Spostare parte del calcolo sul client alleggerisce il server e, distribuendo il codice su tutti i browser collegati, diventa calcolo distribuito molto scalabile. Esempio del docente: un governo che distribuisce un attacco a forza bruta su un cifrario a milioni di set-top box e televisori. Le applet sono sparite per motivi di sicurezza ed efficienza e oggi il codice lato client è JavaScript, che però è "molto meno safe", con una gestione dei tipi "scandalosa". L'evoluzione del calcolo distribuito nei browser è **WebAssembly** (WASM).
*Portabilità.* Smartphone, smart card, set-top box e televisori hanno processori diversi, con assembly diversi e ordinamenti dei byte diversi (little endian e big endian). Java compila in un linguaggio intermedio, il **bytecode**, poi interpretato dalla **Java Virtual Machine**: è insieme compilato e interpretato, "il meglio dei due mondi". L'idea è così buona che Scala e Kotlin girano sulla JVM. La JVM riduce anche la superficie di attacco e impone controlli di sicurezza, anche se ha avuto le sue vulnerabilità.
*Caricamento dinamico delle classi.* Permette di aggiungere funzionalità senza interrompere l'esecuzione, ma è una potenziale fonte di vulnerabilità: più il codice tocca dati grandi e distribuiti, più serve controllare chi esegue cosa e chi accede a quale dato.
*Implementazioni e memoria* (`LSD-02 @ 00:48:08`–`00:50:14`). Le prime implementazioni erano lente rispetto a C e C++ e, con la RAM limitata degli anni '90, un heap gestito automaticamente "fuori controllo" ha tenuto Java fuori da alcuni ambienti. Secondo il docente Java avrebbe meritato più spazio, mentre è Python ad essersi "allargato troppo" rispetto alle sue capacità.
> **Nota aggiunta:** come il web ha plasmato il design dei linguaggi negli anni '90, oltre a Java: codice mobile e sandbox (il verificatore del bytecode controlla il codice prima di eseguirlo), indipendenza dalla piattaforma tramite macchine virtuali, gestione automatica della memoria come requisito per codice non fidato, librerie di rete e concorrenza nella libreria standard, e l'esplosione dei linguaggi di scripting per il web (JavaScript nel browser, PHP e Perl lato server), che hanno privilegiato rapidità di sviluppo e tipizzazione dinamica rispetto alla safety.
## Collegamento con il Questionario 2
"fine" indica la fine della registrazione.
<table header-row="true">
<tr>
<td>Domanda</td>
<td>Slide</td>
<td>Video</td>
<td>Qui</td>
</tr>
<tr>
<td>1. fattori dello sviluppo: hardware, applicazioni, teoria</td>
<td>`MDA2_PLHistory` p2–p7</td>
<td>`LSD-02 @ 00:24:10`–`00:26:17`, `00:33:13`–`01:02:44`</td>
<td>§1</td>
</tr>
<tr>
<td>2. efficienza prima della safety, e oggi</td>
<td>`MDA2_PLHistory` p9–p10, p16; `MDA3` p45, p47</td>
<td>`LSD-02 @ 00:24:55`–`00:33:13`, `01:25:33`–fine; `LSD-03 @ 00:00:10`–`00:03:15`; `Teams Extra-2 @ 0:29:39`–`0:32:17`</td>
<td>§1, Dall'efficienza alla sicurezza; §3 C</td>
</tr>
<tr>
<td>3. FORTRAN primo linguaggio ad alto livello</td>
<td>`MDA2_PLHistory` p9–p10</td>
<td>`LSD-02 @ 01:02:44`–`01:07:00`; `Teams 2 @ 1:09:56` (esperti di Fortran e COBOL ancora richiesti)</td>
<td>§3 FORTRAN</td>
</tr>
<tr>
<td>4. LISP: ordine superiore e memoria</td>
<td>`MDA2_PLHistory` p11–p12; `MDA3` p2–p11</td>
<td>`LSD-02 @ 01:06:29`–`01:11:00`; `LSD-04 @ 00:08:21`–`00:08:52`</td>
<td>§3 LISP</td>
</tr>
<tr>
<td>5. ALGOL come reazione al FORTRAN</td>
<td>`MDA2_PLHistory` p13</td>
<td>`LSD-02 @ 01:10:29`–`01:12:47`; `LSD-03 @ 00:14:33`–`00:15:07`</td>
<td>§3 ALGOL (con nota)</td>
</tr>
<tr>
<td>6. obiettivi del C e diffusione</td>
<td>`MDA2_PLHistory` p14–p16</td>
<td>`LSD-02 @ 00:16:12`–`00:17:21`, `01:12:06`–`01:13:52`, `01:19:29`–`01:23:50`; `LSD-03 @ 00:00:10`–`00:01:25`</td>
<td>§3 C</td>
</tr>
<tr>
<td>7. punti di forza e debolezze del C</td>
<td>`MDA2_PLHistory` p16; `MDA3` p12–p20, p28–p30, p40, p45</td>
<td>`LSD-02 @ 01:13:21`–`01:19:29`, `01:23:19`–fine; `LSD-03 @ 00:01:25`–`00:13:21`, `00:29:05`–`00:31:02`; `LSD-04 @ 00:03:30`–`00:04:39`, `00:24:26`–`00:25:38`, `01:14:23`–`01:14:56`, `01:27:40`–`01:28:12`; `Teams 2 @ 1:21:04`, `1:36:37`</td>
<td>§3 C, tabella</td>
</tr>
<tr>
<td>8. limiti della type inference</td>
<td>`MDA2_PLHistory` p20–p22; `MDA3` p26–p27, p33–p34</td>
<td>`LSD-03 @ 00:22:25`–`00:32:12`, `00:42:32`–`00:44:54`; `LSD-04 @ 01:11:32`–`01:12:45`, `01:22:22`–`01:22:54` (l'inferenza sì, i suoi limiti no)</td>
<td>§3 ML e nota qui sotto</td>
</tr>
<tr>
<td>9. dove la programmazione logica è ancora vantaggiosa</td>
<td>`MDA2_PLHistory` p23–p25</td>
<td>`LSD-02 @ 00:47:19`–`00:48:08`; `LSD-03 @ 00:45:57`–`00:58:34`</td>
<td>§3 PROLOG (con nota)</td>
</tr>
<tr>
<td>10. il web e il design di Java</td>
<td>`MDA2_PLHistory` p26–p30; `MDA16` p14–p15</td>
<td>`LSD-03 @ 00:57:59`–`01:15:42`; `LSD-02 @ 00:48:08`–`00:50:46`; `LSD-05 @ 01:50:35`–`01:55:34`; `Teams 2 @ 1:48:36` (JavaScript)</td>
<td>§3 Java (con nota); capitolo 04 §5</td>
</tr>
<tr>
<td>11. Simula primo linguaggio a oggetti</td>
<td>`MDA2_PLHistory` p17–p19</td>
<td>`LSD-03 @ 00:13:21`–`00:23:05`; `LSD-02 @ 00:42:53`–`00:46:48`</td>
<td>§3 Simula</td>
</tr>
<tr>
<td>12. idee storiche nei linguaggi moderni</td>
<td>`MDA2_PLHistory` p12, p17–p18, p21–p22, p28–p30; `MDA3` p21</td>
<td>`LSD-02 @ 00:18:37`–`00:22:09`, `00:35:34`–`00:37:12`, `01:04:53`–`01:06:29`; `LSD-03 @ 00:12:11`–`00:13:21`, `00:26:59`–`00:29:05`, `00:43:14`–`00:44:54`, `00:56:55`–`00:58:34`, `01:08:25`–`01:12:07`; `LSD-05 @ 01:52:16`–`01:52:55`; `Teams 2 @ 1:18:47` (Firefox da C++ a Rust)</td>
<td>nota qui sotto; §2</td>
</tr>
</table>
> **Nota aggiunta — limiti della type inference** (domanda 8, non trattata a lezione): i messaggi di errore possono comparire lontano dal punto in cui l'errore è stato commesso, perché il tipo sbagliato si propaga prima di generare un conflitto; il codice diventa meno leggibile quando i tipi non sono scritti (per questo in Haskell, OCaml, Scala o Rust si annotano comunque le funzioni pubbliche); un refactoring può cambiare silenziosamente un tipo inferito e l'interfaccia di un modulo; per sistemi di tipi più espressivi l'inferenza completa diventa indecidibile e servono annotazioni; ML stesso ha dovuto introdurre la *value restriction* per conciliare inferenza, polimorfismo e riferimenti mutabili; l'inferenza può scegliere un tipo più generale o più specifico di quello inteso.
> **Nota aggiunta — idee storiche nei linguaggi moderni** (domanda 12): garbage collector (LISP → Java, Python, Scala, Julia); funzioni di ordine superiore (LISP → `map`/`filter`/`reduce`, il modello di Spark e MapReduce); type safety statica e inferenza (ML → Scala, Kotlin, Rust, TypeScript); classi ed ereditarietà (Simula → Java, Python); coroutine (Simula → `async`/`await`, goroutine); dichiaratività (programmazione logica → SQL, Spark SQL, i dataframe "lazy" di Polars); bytecode e macchina virtuale (Java → Scala e Kotlin sulla JVM, e gran parte dell'ecosistema Big Data, da Hadoop a Spark, sulla JVM); il bisogno di memory safety senza rinunciare alle prestazioni del C → Rust.
## Punti incerti della trascrizione
- `LSD-02 @ 01:03:47` — "John Bacus" è John Backus; `01:12:47` — "Dennis Ricci" è Dennis Ritchie, "laboratori di TNT" sono i Bell Labs di AT&T
- `LSD-02 @ 00:13:15` — il docente dice prima che i sistemi operativi sono scritti in C++, poi si corregge in C
- `LSD-03 @ 00:36:01` — "executable linux format": il formato è ELF, *Executable and Linkable Format*
