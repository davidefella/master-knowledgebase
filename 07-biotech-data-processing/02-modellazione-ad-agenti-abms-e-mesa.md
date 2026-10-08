# 02 - Modellazione ad agenti (ABMS) e MESA

> Fonte Notion: https://app.notion.com/p/3e912abc808d81f08925c149605476c7 — ultima modifica 2026-09-28T17:51:18.961Z

**Registrazione:** `BT-02` (portale, edizione 2025), durata 01:32:15. Giornata: **Day 3** (slide "Agent based modeling, Biocentis, Matteo Rucco - Day 3").
**Materiale:** slide `ABMS.pdf` (solo sul canale Teams 2026, cartella "III lezione"); notebook a schermo `Money_ABMS.ipynb` e `Zombie_ABMS.ipynb`; sul canale Teams `Biotech_LEZIONE3.ipynb` e `Zombie_ABMS_lezione_3_Biotech.ipynb`.
> **Segmento duplicato nel video.** Da `BT-02 @ 00:20:05` a circa `00:25:05` la registrazione ripete l'inizio di `BT-01` (da "quando parlo di sistemi complessi" fino all'annuncio di Eulero e `odeint`), con la slide "Mathematics in Biology, Day 2" a schermo a `00:24:58`. È un errore di montaggio del file del portale: quel tratto non appartiene a questa lezione ed è escluso dal capitolo.
> **Nota sul codice.** Il notebook della lezione, `Money_ABMS.ipynb`, **non è tra i materiali**: il codice della sezione 10 è trascritto dai fotogrammi (`BT-02 @ 01:17:56`-`01:26:57`) e verificato per esecuzione con `mesa==0.9.0`. Il notebook di Teams `Biotech_LEZIONE3.ipynb` è la versione 2026 dello stesso esempio ma con regole diverse (sezione 11). Lo zombie ABM di Teams coincide con quello a schermo.
> **Teams 2026.** Nella lezione 3 (20/05/2026) gli agenti iniziano a `Teams 3 @ 0:53:55`, ma la trascrizione automatica di Stream si interrompe a `0:57:51` su una registrazione di 2:43:33: della parte 2026 sugli agenti si hanno solo i primi quattro minuti (sezione 1) e i notebook.
## Indice
1. Cos'è la modellazione basata su agenti
2. Sistemi complessi e limiti della simulazione numerica
3. Obiettivi della modellazione
4. Agenti: scuole, tipi, caratteristiche
5. Il modello ad agenti: stato, regole, ambiente, interazione
6. Comportamento, tempo, simulazione
7. Ciclo di sviluppo di una simulazione
8. Quando usare gli agenti: vantaggi, svantaggi, applicazioni
9. MESA
10. Colab: preda-predatore con energia (`Money_ABMS.ipynb`)
11. La versione 2026: `Biotech_LEZIONE3.ipynb`
12. Colab: invasione zombie ad agenti
13. Esercizi e collegamento con il test finale
14. Glossario, punti incerti, materiale usato
---
## 1. Cos'è la modellazione basata su agenti
`BT-02 @ 00:00:10`
La modellazione basata su agenti (ABM, *Agent Based Modeling*) è un approccio sviluppato negli ultimi vent'anni circa e ancora in evoluzione, nato dall'informatica: più cresce la capacità di calcolo, più diventano simulabili sistemi complessi. È **complementare** alle equazioni differenziali del capitolo 01: le ODE descrivono solo l'evoluzione nel tempo di una quantità, senza componente spaziale; gli agenti aggiungono lo **spazio** (`BT-02 @ 00:01:27`). Esistono anche tentativi di riconciliare i due mondi, in modo che uno informi l'altro.
Un ABM simula comportamenti e interazioni di molte **entità autonome**, gli agenti, che operano in un ambiente definito. È efficace per i fenomeni **emergenti**: il comportamento collettivo non è la ricombinazione lineare dei comportamenti dei singoli e sarebbe difficile da descrivere in modo analitico (`BT-02 @ 00:01:58`). Ogni agente decide in base a regole predefinite o ad algoritmi; le regole possono essere sostituite o arricchite da algoritmi di machine learning. Gli agenti percepiscono l'ambiente, interagiscono con altri agenti e si adattano agli input (`BT-02 @ 00:04:09`).
Alla domanda del docente su un esempio di sistema complesso, uno studente risponde "il corpo": ogni organo o cellula, a seconda della scala, ha regole e comportamenti propri, non puramente sequenziali; un organo è sempre attivo e cambia comportamento in base agli input, e non produce sempre lo stesso output. Esempio: l'occhio del capitolo 01, che vede meglio o peggio a seconda delle condizioni, in modo soggettivo (`BT-02 @ 00:05:18`).
Rispetto alle ODE e agli approcci statistici aggregati, l'ABM dà una rappresentazione più dettagliata sia del singolo agente sia del sistema, e permette di includere variazioni individuali, adattamento e apprendimento. Un agente è un'entità virtuale autonoma, capace di interagire e decidere: può rappresentare organi, persone, animali, organizzazioni, molecole (`BT-02 @ 00:07:28`).
**Edizione 2026** (`Teams 3 @ 0:53:55`): stessa introduzione. Il docente precisa che l'ABM "non va confuso con il concetto di agente di intelligenza artificiale di cui sentiamo parlare in questo periodo", e che gli agenti possono interagire sia dentro la stessa classe sia tra classi diverse, e anche con l'ambiente.
## 2. Sistemi complessi e limiti della simulazione numerica
`BT-02 @ 00:08:35`
"Non c'è sistema in biologia che non sia un sistema complesso." Slide "Complex systems": un sistema complesso
- è altamente strutturato, con variazioni;
- ha un'evoluzione molto sensibile alle condizioni iniziali e alle piccole perturbazioni;
- ha molte componenti indipendenti che interagiscono, e più percorsi possibili di evoluzione;
- è difficile da capire e verificare per progetto, per funzione o per entrambi;
- ha interazioni multiple tra molte componenti diverse;
- evolve costantemente nel tempo.
Il docente aggiunge che il sistema è in costante ascolto dell'ambiente e reagisce adattandosi; queste caratteristiche lo rendono difficile da prevedere con modelli lineari o deterministici.
Slide "Numeric simulation limits" (`BT-02 @ 00:09:49`):
- i modelli a equazioni hanno molti parametri;
- in biologia, sociologia, economia servono teorie diverse;
- è difficile la transizione micro/macro e rappresentare livelli diversi;
- non si rappresentano i comportamenti, solo il loro risultato complessivo (numero di individui, quantità di cibo);
- non si rende conto dell'emergere di strutture spaziali e temporali (banchi di pesci, stormi, colonne di formiche).
Esempio del docente: con le ODE si studia la crescita di una popolazione di molecole, ma è difficile modellare l'introduzione **casuale** di una nuova quantità; al più si programma un ritardo ($`t + \Delta t`$), che non è un'astrazione del caso (`BT-02 @ 00:10:25`).
**Aneddoto** (`BT-02 @ 00:11:57`): secondo il docente il primo a formalizzare il moto delle formiche fu Richard Feynman, poi premio Nobel. Osservò che una formica va da A a B, dove c'è il cibo, prima in modo casuale, poi con traiettorie sempre più rettilinee ripercorrendo il tragitto, grazie ai **feromoni** rilasciati lungo il percorso. I matematici dell'epoca riconobbero che il fenomeno era formalizzabile con equazioni alle derivate parziali, ma non in modo semplice, e suggerirono di usare **regole** che rappresentassero le spezzate percorse dalle formiche.
> **Nota aggiunta:** nel racconto di Feynman (*Surely You're Joking, Mr. Feynman!*) il raddrizzamento della pista non è opera di una singola formica che affina il proprio percorso, ma dell'effetto collettivo di molte formiche che seguono la traccia di feromone lasciata dalle precedenti, "mediandola". Nel racconto non compare la formalizzazione con le PDE: quella parte va attribuita al docente.
## 3. Obiettivi della modellazione
`BT-02 @ 00:13:32`
Slide "Modeling objectives (1/2)":
- **capire** un sistema: in dettaglio (quantitativo), qualitativamente (relazioni tra le variabili di interesse), per affinare l'intuizione;
- **prevedere o ricostruire a posteriori** (*forecast or backcast*): comportamenti dei partecipanti, stati del sistema a livello micro, meso o macro;
- **supportare interventi**: consigliare i partecipanti sulle strategie, consigliare i responsabili (per esempio i *policy maker*) sulla gestione.
Il ciclo descritto dal docente (`BT-02 @ 00:14:41`): davanti a un sistema biologico nuovo lo si osserva, se ne deducono regole di comportamento (anche in funzione di ambiente e stimoli), le si codifica in un framework ad agenti e si esegue, verificando se l'esperimento digitale cattura le osservazioni del sistema vero. Gli esperimenti digitali costano meno e sono più **ripetibili** di quelli biologici, e possono suggerire nuovi esperimenti di laboratorio. Una volta validato il modello, si può perturbarne l'input e anticipare il comportamento del sistema vero. Gli stati si possono decomporre su tre scale, **micro, meso, macro**, la cui dimensione (micrometri, millimetri, chilometri) dipende dal sistema (`BT-02 @ 00:16:53`).
Slide "Modeling objectives (2/2)":
- creare una realtà (i modelli): la teoria di Black-Scholes sul prezzo delle opzioni;
- abilitare il **coordinamento tra stakeholder** (modelli come artefatti di coordinamento): modelli previsionali negli hedge fund, strategia aziendale, politiche pubbliche su larga scala (modelli macroeconomici nazionali, cambiamento climatico, malattie trasmissibili).
Il docente richiama il SIR del capitolo 01 come esempio di modello utile a informare il policy maker, e conclude: i modelli "non solo descrivono una realtà, ma contribuiscono anche a crearla e a coordinare azioni" (`BT-02 @ 00:18:27`).
## 4. Agenti: scuole, tipi, caratteristiche
`BT-02 @ 00:18:27`
Slide "Agent Schools":
<table header-row="true">
<tr>
<td>Scuola</td>
<td>Uso degli agenti</td>
</tr>
<tr>
<td>Artificial intelligence</td>
<td>agenti come entità autonome che risolvono problemi</td>
</tr>
<tr>
<td>Multi-agent systems</td>
<td>controllo distribuito di sistemi</td>
</tr>
<tr>
<td>Agent-based modeling (and simulation)</td>
<td>simulazione di fenomeni del mondo reale</td>
</tr>
</table>
**Agenti e intelligenza artificiale** (`BT-02 @ 00:25:08`): riprendendo la scuola di Turing, un'intelligenza artificiale imita il comportamento umano in alcune situazioni: percepisce l'ambiente, lo interiorizza in una rappresentazione interna, agisce e monitora l'effetto delle proprie azioni. Un agente a regole è un'IA "iper specializzata, quindi poco intelligente, molto artificiale": dato un input, si comporta sempre allo stesso modo. Lo si può rendere più autonomo con il **reinforcement learning**, apprendimento basato su premi: l'agente agisce, riceve un feedback positivo o negativo dall'ambiente e dopo molte interazioni capisce se sta agendo bene. Gli agenti a rinforzo sono uno dei modi per costruire agenti, e uno dei tentativi verso l'intelligenza artificiale generale, da cui "siamo ancora lontani".
**Slide "Agent types"** (`BT-02 @ 00:27:55`): un diagramma decisionale che parte da "Agent" e porta al tipo di agente:
- *Does it move?* sì → **Mobile Agent**;
- *Does it collect, filter & classify information?* sì → **Info-gathering Agent**;
- *Require Assistant User?* sì → **Interface Agent** (serve comunicazione tra utente e agente, o tra agenti);
- *Does it run without continuous user input?* sì → **Autonomous Agent** (esempio del docente: l'auto a guida completamente autonoma);
- *Can it change its behavior based on past experiences?* sì → **Adaptive Agent** (ha memoria, come gli agenti a rinforzo); no → *Does it have a set solution path?* sì → **Reactive Agent**; no → *Does it care about the utility value?* sì → **Utility Agent** (ottimizza una funzione obiettivo), no → **Goal-based Agent** (raggiunge un obiettivo senza ottimizzare).
Riquadro della slide: "Agents can possess more than one property". Il docente: quando all'esame chiederà di scegliere il tipo di agente adatto a un fenomeno, bisogna partire da questa mappa, tenendo presente che un agente può essere trasversale a più tipi (`BT-02 @ 00:31:28`).
Slide "Agent Features" (`BT-02 @ 00:32:01`):
<table header-row="true">
<tr>
<td>Caratteristica</td>
<td>Significato</td>
</tr>
<tr>
<td>Encapsulated</td>
<td>identificabile, con confini e interfacce ben definiti</td>
</tr>
<tr>
<td>Situated in a particular environment</td>
<td>riceve input da sensori e agisce tramite attuatori</td>
</tr>
<tr>
<td>Capable of flexible action</td>
<td>risponde ai cambiamenti e agisce in anticipo</td>
</tr>
<tr>
<td>Autonomous</td>
<td>controlla stato interno e comportamento, reagisce all'ambiente e cambia comportamento in modo proattivo</td>
</tr>
<tr>
<td>Designed to meet objectives</td>
<td>cerca di raggiungere uno scopo, risolvere un problema, raggiungere obiettivi</td>
</tr>
</table>
## 5. Il modello ad agenti: stato, regole, ambiente, interazione
`BT-02 @ 00:32:33`
Slide "Agent Model (1/2)": un agente è una "cosa persistente" con uno **stato**, che interagisce con altri agenti modificando a vicenda gli stati. Le componenti di un ABM sono una collezione di agenti con i loro stati, le **regole** che governano le interazioni, l'**ambiente** in cui vivono. L'interazione tra agenti è il punto centrale della simulazione.
Slide "Agent Model (2/2)" (`BT-02 @ 00:33:39`): schema di un agente dentro l'ambiente, con due blocchi **State** e **Rules** collegati da frecce nei due sensi; ingressi *Inputs from other Agents* e *Inputs from the Environment*, uscite *Actions on the Environment*, *Actions on other Agents* e *Actions on Self*. Il docente lo legge come un **automa**: dallo stato si scelgono le regole da applicare, e l'applicazione porta l'agente in un altro stato, lo lascia nello stato corrente o lo riporta a uno precedente. L'evoluzione è quindi in generale **ciclica**, non sequenziale; dipende da cosa si modella: l'invecchiamento (giovane, adulto, anziano) non torna indietro, un organismo affamato, sazio, di nuovo affamato sì (`BT-02 @ 00:34:53`).
**Ambiente** (`BT-02 @ 00:36:03`): fisico, sociale o virtuale; insieme alle interazioni è il contesto della simulazione, e la sua scelta è cruciale per risultati realistici. Slide "Environment", cinque rappresentazioni:
- (a) **"Soup" model** (aspaziale): il docente lo collega alle teorie in cui gli elettroni vagano liberi nella materia senza interagire con il nucleo, poi raffinate;
- (b) **Cellular Automata (von Neumann)**: spazio discreto a tasselli, qui celle quadrate di una griglia, ma la tassellazione dipende dall'ambiente (su una sfera, come un pallone da calcio, servono altri poligoni). Utile perché i vicini si trovano subito con i punti cardinali e le diagonali;
- (c) **Euclidean Space (2-D)**, generalizzabile a $`n`$ dimensioni: quello in cui misuriamo le distanze, con la distanza euclidea $`d = \sqrt{\sum_i (x_i - y_i)^2}`$;
- (d) **GIS** (*Geographic Information System*): quando servono informazioni geografiche come altitudine, piovosità, umidità, temperatura (per esempio flussi migratori di insetti), che lo spazio euclideo "appiattisce";
- (e) **Network topology**: un grafo che dice chi è connesso con chi, con informazioni aggiuntive su archi e vertici; molto usato in biologia per le interazioni tra molecole o geni.
Nel corso si usa soprattutto la griglia di von Neumann, bidimensionale e quindi euclidea (`BT-02 @ 00:40:54`).
**Interazione** (`BT-02 @ 00:41:34`), slide "Agent interaction". Sulla griglia si sceglie quali vicini interrogare:
- **Moore**: tutte le 8 celle attorno all'agente;
- **von Neumann**: le 4 celle a nord, sud, est, ovest;
- **von Neumann ruotato**: le 4 diagonali, cioè la differenza tra Moore e von Neumann.
Sui grafi non si conta il numero di vicini ma il **grado** di vicinanza: vicini di primo grado (raggiungibili direttamente), di secondo (il vicino del vicino), e così via fino al quarto nella figura (`BT-02 @ 00:42:47`).
## 6. Comportamento, tempo, simulazione
`BT-02 @ 00:43:39`
Slide "Behavior ingredients":
<table header-row="true">
<tr>
<td>Tecnica</td>
<td>Contenuto</td>
</tr>
<tr>
<td>Rule Based</td>
<td>strutture if-then-else annidate</td>
</tr>
<tr>
<td>Multi criteria decision making</td>
<td>opzioni e pesi</td>
</tr>
<tr>
<td>Inference engines</td>
<td>sistemi esperti, fatti (stati) ed euristiche di decisione</td>
</tr>
<tr>
<td>Machine learning</td>
<td>reti neurali, deep learning, statistica bayesiana, pattern recognition</td>
</tr>
<tr>
<td>Evolutionary computing</td>
<td>soluzione ottima in grandi spazi di soluzioni (algoritmi genetici)</td>
</tr>
</table>
A voce il docente cita anche la **logica fuzzy**. Gli **algoritmi genetici** sono euristiche per trovare la soluzione ottima di un problema, ispirate a selezione e ricombinazione, che migliorano il comportamento di un agente per iterazioni successive; in letteratura si usano per problemi di ottimizzazione con agenti, per esempio il metabolismo ottimale per assorbire un alimento (`BT-02 @ 00:44:54`). Sono l'argomento del capitolo 06.
**Tempo** (`BT-02 @ 00:45:26`), slide "Time":
- le simulazioni avvengono in tempo **discreto**;
- il tempo avanza a **tick**;
- tra due tick tutto si considera simultaneo, per simulare il parallelismo del mondo reale;
- poiché i computer elaborano in serie, **l'ordine** con cui si attivano gli agenti è molto importante.
Slide "Simulation" (`BT-02 @ 00:46:40`): i modelli ad agenti sostituiscono un altro sistema; usano per lo più tempo virtuale; gli agenti vivono in un ambiente simulato, spazio sociale (una rete) o spazio virtuale 2D/3D; tempo e ambiente sono controllati dal modellista. Il significato di un tick (giorno, mese, anno) e di un ambiente (stanza, casa, quartiere, organo) è una **scelta modellistica**.
**Orientati al comportamento o agli obiettivi** (`BT-02 @ 00:47:54`), slide "Behaviors vs goal oriented":
- **behavior-oriented**: il modellista descrive stato e dinamica degli agenti con formalismi come grafi di attività, regole crisp o fuzzy, vincoli; definisce le reazioni a percezioni e cambi di stato; si integra bene con reinforcement learning e concetti evolutivi; gli obiettivi sono impliciti. "Very intuitive mapping with simple biological systems (e.g., insects)": secondo il docente adatto a sistemi biologici semplici e anche complessi;
- **goal-oriented**: il modellista identifica gli obiettivi, l'agente ne sceglie uno e agisce di conseguenza; le reazioni non sono predefinite ma dipendono dall'obiettivo. Più dettagliato ma più soggetto a errori e molto più complesso (slide: "see Belief-Desire-Intention agent models").
La scelta dipende fortemente dal contesto applicativo. Nella mappa dei tipi di agente è il bivio tra goal-based e utility agent (`BT-02 @ 00:48:30`).
## 7. Ciclo di sviluppo di una simulazione
`BT-02 @ 00:51:27`
Slide "Development & Use": due colonne di passi, ciascuno collegato al precedente da frecce nei due sensi, perché ogni passo valida o informa il precedente.
1. **Prototyping**: formalizzazione con carta e penna di cosa deve fare l'agente.
2. **Architectural Design**: chi sono gli agenti e come interagiscono, ad alto livello.
3. **Agent and Agent Rule Design**: caratteristiche e variabili degli agenti. Esempio: per un viaggiatore contano origine e destinazione, non il colore dei capelli, che diventa rilevante solo in una simulazione sociale in cui influenza il comportamento (`BT-02 @ 00:52:41`).
4. **Agent Environment Design**.
5. **Implementation**: scrivere il codice, nel corso con **MESA**.
6. **Verification and Validation**: replicare scenari noti, già osservati nella realtà, e quantificare la differenza tra simulazione e osservazioni; le discrepanze rimandano ai passi precedenti (regole di comportamento, di interazione, ambiente).
Poi, a destra: **Experimental Design**, **Data Collection and Entry**, **Model Execution**, **Results Analysis**, **Results Presentation**. Per il design degli esperimenti il docente suggerisce SALib (capitolo 01), usato anche per campionare i punti, cioè le condizioni iniziali attorno a cui eccitare il simulatore (`BT-02 @ 00:54:54`). Se in futuro arrivano osservazioni nuove che non corrispondono, si torna indietro nel ciclo.
"Il diavolo è nei dettagli": una simulazione ad agenti ha senso solo se si conoscono bene i comportamenti degli agenti e le regole di interazione tra loro e con l'ambiente (`BT-02 @ 00:56:13`).
## 8. Quando usare gli agenti: vantaggi, svantaggi, applicazioni
`BT-02 @ 00:56:49`
Slide "Advantages":
<table header-row="true">
<tr>
<td>Vantaggio</td>
<td>Dettaglio</td>
</tr>
<tr>
<td>Capacità di modellazione in discipline importanti</td>
<td>scienze sociali, biologia, sviluppo software</td>
</tr>
<tr>
<td>Simula sistemi difficili con approcci tradizionali</td>
<td>fenomeni emergenti, modelli a struttura variabile</td>
</tr>
<tr>
<td>Più dettaglio nei modelli</td>
<td>più realismo e micro-validità</td>
</tr>
<tr>
<td>Modo intuitivo di modellare</td>
<td>facilita la comunicazione con altri campi</td>
</tr>
</table>
Slide "Applicability" (`BT-02 @ 00:57:26`), gli agenti servono quando:
- decisioni e comportamenti sono **ben definibili**. È il presupposto: se non si possono definire regole chiare è inutile usarli. Anche un comportamento appreso con il machine learning richiede un campione significativo di osservazioni, altrimenti si catturano solo alcuni comportamenti;
- gli agenti devono **adattarsi** e cambiare comportamento;
- le relazioni tra agenti sono **dinamiche**, si formano, cambiano, decadono. Sulla griglia l'agente può essere isolato a un istante, circondato all'istante dopo, e da agenti diversi ancora dopo; da qui emergono gruppi e alleanze (`BT-02 @ 00:59:03`);
- gli agenti formano organizzazioni, e adattamento e apprendimento contano a livello di organizzazione;
- comportamenti e interazioni hanno una **componente spaziale**, o comunque un supporto di interazione come un grafo, che non deve essere per forza fisico: una rete sociale (Facebook, LinkedIn) collega persone non co-localizzate (`BT-02 @ 01:00:41`);
- il passato non predice il futuro, perché crescita e cambiamento sono dinamici. Se l'andamento è prevedibile da pochi punti, bastano equazioni lineari o interpolazione (`BT-02 @ 01:02:24`);
- la **scalabilità** a livelli arbitrari è importante;
- il cambiamento strutturale deve essere un risultato **endogeno** del modello, non un input.
**Scalabilità** (`BT-02 @ 01:03:27`): capacità di calcolo sufficiente a simulare un numero crescente di agenti. Fino a meno di un decennio fa era un grosso limite, superato con le GPU. Per decine di migliaia di agenti con comportamenti complessi il docente indica **FLAME GPU**, potente ma complicato; a fini didattici basta **MESA**.
**Agenti contro ODE** (`BT-02 @ 01:05:40`), slide "Agent vs Macro (ODE)":
<table header-row="true">
<tr>
<td></td>
<td>ABMS</td>
<td>Macro (ODE)</td>
</tr>
<tr>
<td>**Pro**</td>
<td>tratta direttamente sistemi multi-agente, ogni agente reale è un agente simulato; facilita la validazione strutturale; tratta con eleganza strutture variabili; modella adattamento ed evoluzione; modella facilmente spazio e popolazioni eterogenei; offre più livelli di osservazione</td>
<td>framework matematico consolidato e ben compreso; facile da documentare; pochi parametri, comportamento input-output globale</td>
</tr>
<tr>
<td>**Contro**</td>
<td>sviluppo di modelli complessi costoso; difficile determinare il modello minimo; manca un formalismo consolidato, difficile da documentare; problema di calibrazione (trovare i parametri migliori per un modello strutturalmente valido); problema di sensibilità (piccole modifiche, grandi effetti)</td>
<td>assume spazio e popolazione omogenei; nessuna rappresentazione dell'individuo e della sua località (niente comportamento condizionale, adattivo, interazioni flessibili); osserva solo il sistema nel suo insieme</td>
</tr>
</table>
Il docente sottolinea: il modello ODE simula quantità, non individui; gli agenti rendono il modello più intuitivo, flessibile e spiegabile, e permettono di osservarlo a scala micro, meso e macro. I modelli ODE sono meno sensibili ai parametri, più robusti e danno una visione più stabile del sistema (`BT-02 @ 01:09:00`). Sulla mancanza di formalismo: di recente è stato proposto il protocollo **ODD** per descrivere i modelli ad agenti, da studiare perché utile per simulatori complessi (`BT-02 @ 01:08:25`).
> **Correzione:** il docente attribuisce ODD a "un tale Green". Il protocollo ODD (*Overview, Design concepts, Details*) è di **Volker Grimm** e colleghi (2006, aggiornato nel 2010 e nel 2020).
**Applicazioni** (`BT-02 @ 01:09:39`), slide "Applications": nati per i sistemi sociali, gli agenti si sono estesi a molti campi. La tabella elenca: Business and Organization (manifattura, supply chain, mercati di consumo, assicurazioni), Economics (mercati finanziari artificiali, reti commerciali), Infrastructure (mercati dell'energia elettrica, trasporti, infrastruttura dell'idrogeno), Crowds (movimento pedonale, modelli di evacuazione), Society and Culture (civiltà antiche, disobbedienza civile, determinanti sociali del terrorismo, reti organizzative), Military (comando e controllo, force on force), Biology (dinamica di popolazione, reti ecologiche, comportamento di gruppi animali, comportamento cellulare e processi sub-cellulari), Entertainment (film e giochi). Il docente aggiunge lo sviluppo software: un sistema operativo simulato con agenti per tastiera, mouse, allocazione della memoria.
**Esempio: dengue** (`BT-02 @ 01:10:44`), difficilissima da simulare con le ODE. Nel racconto del docente: una zanzara vettore punge un essere umano; la prima trasmissione in genere non fa scaturire la malattia, ma se un'altra zanzara infetta punge la stessa persona la malattia si sviluppa. Inoltre una zanzara sana che punge una persona infetta ne preleva la carica virale e può poi pungere una persona sana. Gli agenti permettono di simulare lo spostamento sia degli umani sia delle zanzare, su distanze e scale diverse.
> **Nota aggiunta:** la descrizione del docente semplifica la dengue. Il fatto documentato è che una **seconda infezione con un sierotipo diverso** (i sierotipi sono quattro) aumenta il rischio di dengue grave; la prima infezione può già dare malattia sintomatica. Resta valido il punto modellistico: la dinamica dipende dalla storia di esposizione del singolo individuo e dal movimento di ospiti e vettori, cose naturali negli agenti e scomode nelle ODE.
## 9. MESA
`BT-02 @ 01:13:12`
Slide "Software: MESA": uno schema a classi, che richiama la **programmazione orientata agli oggetti** (OOP), in apparenza adatta agli agenti e, dati i vincoli hardware, per anni probabilmente l'approccio migliore. Pilastri: le **classi** sono le specifiche degli agenti (classe essere umano, classe zanzara); gli **oggetti** sono istanze che danno valore agli attributi (sesso, geografia, nome); i **metodi** sono i comportamenti. L'OOP richiede una gerarchia di classi attenta, fattibile per simulazioni *one shot* di sistemi statici; pensare invece in termini di **sistemi di attori** rende le simulazioni più riproducibili, su larga scala, distribuite e asincrone (`BT-02 @ 01:15:00`). MESA è un compromesso: internamente è a classi, ma l'utente pensa direttamente agli agenti. È il framework più popolare per gli ABM, open source, in Python, eseguibile in Colab.
**Versione** (`BT-02 @ 01:16:42`): il codice del corso è scritto per **MESA 0.9**; versioni più recenti richiederebbero di aggiornare alcuni metodi. Si installa con `!pip install mesa==0.9.0`.
> **Nota aggiunta:** da MESA 3.0 `mesa.time.RandomActivation` e lo `schedule` non esistono più (sostituiti da `model.agents.shuffle_do("step")`), gli agenti non ricevono più `unique_id` nel costruttore e `Model.__init__` va chiamato esplicitamente. Il codice di questo capitolo quindi gira solo con la versione fissata (verificato con `mesa==0.9.0`, NumPy 2.4, pandas 3.0).
## 10. Colab: preda-predatore con energia (`Money_ABMS.ipynb`)
`BT-02 @ 01:16:42`
Il sistema preda-predatore già visto con Lotka-Volterra, ora ad agenti su una griglia (`BT-02 @ 01:17:19`).
**Import** (preceduti da `!pip install mesa==0.9.0`):
```python
from mesa import Agent, Model
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from mesa.time import RandomActivation
import matplotlib.pyplot as plt
import pandas as pd
```
**La preda** (`BT-02 @ 01:17:52`). `__init__` riceve un identificativo univoco e il modello, e legge l'energia iniziale dal modello. A ogni tick (`step`) la preda si muove e perde 1 di energia; se l'energia arriva a zero muore ed è rimossa da griglia e scheduler, altrimenti può riprodursi.
```python
class Prey(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.energy = model.prey_energy

    def step(self):
        self.move()
        self.energy -= 1
        if self.energy <= 0:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
        else:
            self.reproduce()

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        if possible_steps:
            new_position = self.random.choice(possible_steps)
            if new_position is not None:
                self.model.grid.move_agent(self, new_position)

    def reproduce(self):
        if self.random.random() < self.model.prey_reproduce:
            new_prey = Prey(self.model.next_id(), self.model)
            self.model.grid.place_agent(new_prey, self.pos)
            self.model.schedule.add(new_prey)
```
Il movimento interroga i vicini sulla griglia con la regola di **Moore** (`moore=True`) e sceglie a caso una delle celle; il nuovo agente riceve l'id successivo (`next_id()`), è posto nella cella della madre e aggiunto allo **scheduler**, il meccanismo interno di MESA che sa quali agenti esistono, dove sono e in che stato (`BT-02 @ 01:20:40`).
> **Correzione:** il docente descrive `possible_steps` come "la lista delle celle libere" (`BT-02 @ 01:20:09`). `get_neighborhood` restituisce **tutte** le celle del vicinato, occupate o no: su una `MultiGrid` più agenti possono stare nella stessa cella, ed è proprio così che il predatore trova le prede da mangiare.
> **Correzione:** la riproduzione, secondo il docente, avviene "se l'energia è maggiore di un numero random" (`BT-02 @ 01:20:40`). Nel codice l'energia serve solo come condizione di sopravvivenza; la riproduzione è un evento con probabilità fissa `prey_reproduce` per tick (`self.random.random() < self.model.prey_reproduce`), indipendente dall'energia residua.
**Il predatore** (`BT-02 @ 01:21:17`): stessa struttura, con energia propria; oltre a muoversi, morire e riprodursi può **mangiare**. Il metodo `move` è identico.
```python
class Predator(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.energy = model.predator_energy

    def step(self):
        self.move()
        self.energy -= 1
        if self.energy <= 0:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
        else:
            self.eat()
            self.reproduce()

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        if possible_steps:
            new_position = self.random.choice(possible_steps)
            if new_position is not None:
                self.model.grid.move_agent(self, new_position)

    def eat(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        preys = [obj for obj in cellmates if isinstance(obj, Prey)]
        if len(preys) > 0:
            prey = self.random.choice(preys)
            self.model.grid.remove_agent(prey)
            self.model.schedule.remove(prey)
            self.energy += self.model.predator_gain_from_food

    def reproduce(self):
        if self.random.random() < self.model.predator_reproduce:
            new_predator = Predator(self.model.next_id(), self.model)
            self.model.grid.place_agent(new_predator, self.pos)
            self.model.schedule.add(new_predator)
```
> La riga iniziale `class Predator(Agent):` e la chiamata a `super().__init__` non sono inquadrate nei fotogrammi (il primo inizia da `self.energy = model.predator_energy`); sono ricostruite per simmetria con `Prey`.
Per mangiare, il predatore controlla se nella **sua cella** c'è almeno una preda; se sì ne sceglie una a caso, la rimuove dalla griglia e dallo scheduler (che "si dimentica" di lei) e guadagna `predator_gain_from_food` di energia (`BT-02 @ 01:21:51`).
**Il modello** (`BT-02 @ 01:23:07`): l'"orchestratore", sottoclasse di `Model`. Riceve le caratteristiche dell'ambiente (griglia `MultiGrid` **toroidale**, `torus=True`, cioè chi esce da un bordo rientra dal bordo opposto) e i parametri; posiziona a caso prede e predatori iniziali; definisce il **DataCollector**, che a ogni tick conta prede e predatori.
```python
class PredatorPrey(Model):
    def __init__(self, width, height, initial_prey, initial_predators, prey_energy, predator_energy,
                 predator_gain_from_food, prey_reproduce, predator_reproduce):
        super().__init__()
        self.grid = MultiGrid(width, height, torus=True)
        self.schedule = RandomActivation(self)
        self.prey_energy = prey_energy
        self.predator_energy = predator_energy
        self.predator_gain_from_food = predator_gain_from_food
        self.prey_reproduce = prey_reproduce
        self.predator_reproduce = predator_reproduce

        # Initialize Prey agents
        for _ in range(initial_prey):
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            prey = Prey(self.next_id(), self)
            self.grid.place_agent(prey, (x, y))
            self.schedule.add(prey)

        # Initialize Predator agents
        for _ in range(initial_predators):
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            predator = Predator(self.next_id(), self)
            self.grid.place_agent(predator, (x, y))
            self.schedule.add(predator)

        # DataCollector to track Prey and Predator populations
        self.datacollector = DataCollector(
            {
                "Prey": lambda m: sum(isinstance(agent, Prey) for agent in m.schedule.agents),
                "Predators": lambda m: sum(isinstance(agent, Predator) for agent in m.schedule.agents)
            }
        )

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
```
> La firma di `__init__` è tagliata sul bordo destro dello schermo dopo `prey_reproduce, preda[illeggibile]`; l'ultimo argomento è `predator_reproduce`, come si ricava dal corpo e dalla chiamata.
`step` del modello: a ogni tick si contano prede e predatori e si dice allo scheduler di far eseguire `step` a ogni agente. `RandomActivation` li attiva in **ordine casuale** a ogni tick, coerentemente con la slide sul tempo (l'ordine conta).
**Esecuzione e grafico** (`BT-02 @ 01:25:04`):
```python
# Set up the model parameters
model = PredatorPrey(
    width=20, height=20, initial_prey=50, initial_predators=20,
    prey_energy=10, predator_energy=15, predator_gain_from_food=20,
    prey_reproduce=0.04, predator_reproduce=0.02
)

# Run the model for 200 steps
for i in range(200):
    model.step()

# Collect the data
data = model.datacollector.get_model_vars_dataframe()

# Plot the predator and prey populations over time
data.plot(title="Predator-Prey Population Dynamics", xlabel="Step", ylabel="Population")
plt.show()
```
Il grafico a schermo (`BT-02 @ 01:25:57`): prede da 50 con qualche oscillazione, crollo verticale attorno al tick 10, estinzione prima del tick 25; predatori da 20 a circa 24, poi in calo a gradini fino all'estinzione attorno al tick 80. Il commento del docente: all'inizio le prede sono molte più dei predatori, dopo meno di 25 tick sono sterminate \[?\]; non essendo implementato il cannibalismo, anche i predatori si estinguono; i piccoli picchi dei predatori sono dovuti alla riproduzione, che però senza cibo non basta a sostenere la popolazione (`BT-02 @ 01:25:44`).
Verificato per esecuzione (50 seed, parametri del video): le prede si estinguono in **tutti** i run, fra il tick 18 e il 37 (mediana 24), i predatori in tutti i run (mediana tick 87). Il crollo al tick 10 compare in ogni run: nel seed 0 le prede passano da 63 al tick 9 a 24 al tick 10.
> **Correzione:** il crollo delle prede non è dovuto principalmente alla predazione. Nel codice l'energia delle prede cala di 1 a ogni tick e **non viene mai reintegrata** (le prede non mangiano): con `prey_energy=10` ogni preda vive esattamente 10 tick, e al tick 10 muoiono di fame tutte le 50 prede iniziali. Ogni preda ha 9 occasioni di riprodursi con probabilità 0.04, quindi in media $`9 \cdot 0.04 = 0.36`$ figli: meno di uno, la popolazione si estingue comunque. Verificato: **senza predatori** (`initial_predators=0`) le prede si estinguono in tutti i 50 run (mediana tick 27); con i predatori ne vengono mangiate in media 25 per run, circa un terzo del totale. Per avere un ecosistema che oscilla come Lotka-Volterra alle prede serve una fonte di energia (per esempio erba che ricresce sulle celle) o una riproduzione non legata all'energia.
**Esercizio suggerito** (`BT-02 @ 01:26:44`): modificare i parametri, anche con cicli `for` annidati, per valutarne l'influenza. Ipotesi del docente: a parità di condizioni iniziali, uno spazio più piccolo fa predare le prede più in fretta.
## 11. La versione 2026: `Biotech_LEZIONE3.ipynb`
Notebook del canale Teams, stesso esempio con regole diverse e commenti in italiano. Nessuna spiegazione a voce disponibile (trascrizione di `Teams 3` interrotta, vedi intestazione).
Le prede non hanno più energia: si riproducono in modo **deterministico** ogni `step_reprod_prey` tick e muoiono solo se mangiate. I predatori muoiono se non mangiano per `step_death_pred` tick (il contatore si azzera a ogni pasto) e si riproducono in base alle prede mangiate (`eat_repr`).
```python
class Prey(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.step_counter = 0  # Inizializza il contatore degli step a 0
        self.step_reprod_prey = model.step_reprod_prey  # Ogni quanti passi la preda si riproduce

    def step(self):
        self.step_counter += 1  # Incrementa il contatore ogni volta che viene chiamato step()
        self.reproduce()         # Controlla se è il momento di riprodursi
        self.move()              # Muove l'agente

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        if possible_steps:
            new_position = self.random.choice(possible_steps)
            if new_position is not None:
                self.model.grid.move_agent(self, new_position)

    def reproduce(self):
        if self.step_counter % self.step_reprod_prey == 0:
            new_prey = Prey(self.model.next_id(), self.model)
            self.model.grid.place_agent(new_prey, self.pos)
            self.model.schedule.add(new_prey)


class Predator(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.step_counter = 0  # Inizializza il contatore degli step a 0
        self.prey_eaten = 0     # Inizializza il contatore delle prede mangiate
        self.step_death_pred = model.step_death_pred  # Passi senza cibo prima della morte
        self.eat_repr = model.eat_repr  # Ogni quante prede mangiate il predatore si riproduce

    def step(self):
        self.step_counter += 1
        self.move()
        if self.step_counter % self.model.step_death_pred == 0:  # non ha mangiato entro il limite: muore
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
        else:
            self.eat()
            self.reproduce()

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        if possible_steps:
            new_position = self.random.choice(possible_steps)
            if new_position is not None:
                self.model.grid.move_agent(self, new_position)

    def eat(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        preys = [obj for obj in cellmates if isinstance(obj, Prey)]
        if len(preys) > 0:
            prey = self.random.choice(preys)
            self.model.grid.remove_agent(prey)
            self.model.schedule.remove(prey)
            self.prey_eaten += 1   # Incrementa il contatore delle prede mangiate
            self.step_counter = 0  # Resetta il contatore degli step dopo aver mangiato

    def reproduce(self):
        if self.prey_eaten != 0 and self.prey_eaten % self.model.eat_repr == 0:
            new_predator = Predator(self.model.next_id(), self.model)
            self.model.grid.place_agent(new_predator, self.pos)
            self.model.schedule.add(new_predator)
```
(Commenti con `print` di debug rimossi.) Il modello `PredatorPrey` ha la stessa struttura della sezione 10, con l'inizializzazione degli agenti spostata in un metodo `_initialize_agents` e la firma `PredatorPrey(width, height, initial_prey, initial_predators, prey_reproduce, step_reprod_prey, step_death_pred, eat_repr)`. Parametri del notebook: griglia 100×100, 10 prede, 30 predatori, `prey_reproduce=0.008`, `step_reprod_prey=2`, `step_death_pred=20`, `eat_repr=1`. La simulazione è di 10 tick e stampa a ogni tick l'intero DataFrame accumulato.
Verificato per esecuzione: prede 10, 10, 20, 20, 40, 40, 80, 80, 160, 160 nei primi 10 tick (come l'output salvato nel notebook), predatori fermi a 30. Proseguendo: prede 320 al tick 10, 1275 al 15, 9882 al 20; predatori 34 al tick 15, 120 al 19, 340 al 21.
> **Nota aggiunta:** tre osservazioni sul codice 2026, verificate per esecuzione. (1) `prey_reproduce` è salvato nel modello ma **non è mai usato**: la riproduzione delle prede dipende solo da `step_reprod_prey`, quindi le prede raddoppiano ogni 2 tick in modo deterministico (crescita esponenziale, $`2^{t/2}`$), limitata solo dalla predazione. Su una griglia 100×100 con 30 predatori la predazione è rara all'inizio e le prede esplodono (quasi 10 000 al tick 20, con costo di calcolo crescente). (2) Con `eat_repr=1` la condizione `prey_eaten % eat_repr == 0` è sempre vera dopo il primo pasto: da quel momento il predatore si riproduce a **ogni** tick, anche senza mangiare. Lo stesso vale in generale: il test è sul totale cumulato, non sul pasto appena fatto. Se l'intento è "un figlio ogni `eat_repr` prede", la riproduzione va innescata dentro `eat`, subito dopo l'incremento di `prey_eaten`. (3) `update()` importa `matplotlib.animation` e chiama `plt.pause`, ma non disegna nessun grafico: stampa solo il DataFrame.
## 12. Colab: invasione zombie ad agenti
`BT-02 @ 01:27:56`
Chiusura della lezione: lo stesso esperimento del capitolo 01, il SIR in versione zombie, simulato ad agenti. Si reinstalla MESA perché è un notebook diverso, quindi una sessione Colab diversa (`BT-02 @ 01:28:58`). Il docente descrive il codice solo a grandi linee e lo lascia come esercizio, "potrebbe essere un esercizio utile per il test finale" (`BT-02 @ 01:30:45`). Il notebook a schermo è `Zombie_ABMS.ipynb`; su Teams c'è `Zombie_ABMS_lezione_3_Biotech.ipynb`, con lo stesso codice nelle parti inquadrate.
**Distanza euclidea**, funzione ausiliaria:
```python
import math
import random

def get_distance(pos1, pos2):
    """
    finds distance between two points given as coordinate tuple (x, y)
    """
    x1, y1 = pos1
    x2, y2 = pos2
    dx = x1 - x2
    dy = y1 - y2
    return math.sqrt(dx**2 + dy**2)
```
**Modello**: un solo zombie iniziale e `human_number` umani, su una `MultiGrid` **non toroidale** (`False`), al massimo un agente per cella all'inizio; lo zombie va nella posizione indicata o in una casuale se `zombie_pos == ('?', '?')`. A ogni tick lo scheduler attiva gli agenti, poi si incrementa l'età da zombie o da umano di ciascuno.
```python
class ZombieModel(Model):
    """ The model with some number of agents - either Human or Zombie """
    def __init__(self, human_number, grid_size, zombie_pos, startup_pos):
        self.humans = human_number
        self.total_agents = human_number + 1
        self.grid_size = grid_size
        self.startup_pos = startup_pos

        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(grid_size, grid_size, False)

        ## only one zombie to start
        agent_creation_list = ['zombie'] + ['human']*human_number

        # create list of all possible x, y coordinates as tuples - so each coordinate can only have one agent
        all_coords = []
        for x in range(grid_size):
            for y in range(grid_size):
                all_coords += [(x, y)]

        # create the agents
        for n in range(self.total_agents):
            agent = SubjectAgent(n, agent_creation_list[n], self)
            self.schedule.add(agent)
            if agent.state == 'zombie':
                if zombie_pos == ('?', '?'):
                    agent_coords = random.choice(all_coords)
                else:
                    agent_coords = zombie_pos
                all_coords.remove(agent_coords)
            elif self.startup_pos == []:
                agent_coords = random.choice(all_coords)
                all_coords.remove(agent_coords)
            else:
                agent_coords = self.startup_pos[n]
            agent.start_pos = agent_coords
            self.grid.place_agent(agent, agent_coords)

    def step(self):
        self.schedule.step()
        for x in self.schedule.agents:
            if x.state == 'zombie':
                x.zombie_age += 1
            elif x.state == 'human':
                x.human_age += 1
```
**Agente**: una sola classe, `SubjectAgent`, con uno **stato** `'human'` o `'zombie'`: la transizione umano → zombie è un cambio di stato, come nell'automa della sezione 5 (`BT-02 @ 01:29:34`). A ogni tick l'agente individua il bersaglio più vicino di tipo opposto (in tutta la griglia: `radius = grid_size`) e si muove di una cella verso una cella vuota del vicinato di Moore o resta fermo. L'umano **fugge**: sceglie la cella più lontana dal suo zombie più vicino. Lo zombie **insegue**: se il bersaglio è adiacente lo converte, altrimenti va nella cella più vicina al bersaglio.
```python
class SubjectAgent(Agent):
    """ An Agent which can be a Human or Zombie """

    def __init__(self, unique_id, state, model):
        super().__init__(unique_id, model)
        self.state = state # human or zombie
        self.orig_state = state # human or zombie
        self.zombie_age = 1 if state == 'zombie' else 0
        self.human_age = 0
        self.speed = 1 # radius of movement: hardcoded at one for now

    # iterator
    def step(self):
        self.locate_target()
        self.move()

    def locate_target(self):
        ## find the closest agent of opposite type
        possible_targets = [agent for agent in self.model.grid.get_neighbors(self.pos, moore=True, include_center=False, radius = self.model.grid_size)
                            if agent.state != self.state]
        # shuffle because 'get_neighbors' tends to order the list from bottom-left to top-right
        random.shuffle(possible_targets)
        if len(possible_targets) == 0:
            self.target = []
        else:
            target_distance = [(get_distance(self.pos, agent.pos), agent) for agent in possible_targets]
            target_distance.sort(key=lambda tup: tup[0])
            self.target = target_distance[0][1]

    def move(self):
        # get agent's movement options
        movement_options = [coord for coord in self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False, radius = self.speed)
                            if self.model.grid.is_cell_empty(coord)] + [self.pos]
        random.shuffle(movement_options)

        if self.target == []:
            # if there are no agents remaining of the opposite type
            self.model.grid.move_agent(self, random.choice(movement_options))

        elif self.state == 'human':
            dist_from_target = [(get_distance(self.target.pos, coord), coord) for coord in movement_options]
            dist_from_target.sort(key=lambda tup: tup[0], reverse=True)
            new_coords = dist_from_target[0][1]
            self.model.grid.move_agent(self, new_coords)

        elif self.state == 'zombie' and self.zombie_age >= 1:
            # see if the zombie is adjacent to it's target human
            adj_target = [human for human in self.model.grid.get_neighbors(self.pos, moore=True, include_center=False, radius = 1) if human.unique_id == self.target.unique_id]
            if len(adj_target) > 0:
                self.target.state = 'zombie'
            else:
                dist_from_target = [(get_distance(self.target.pos, coord), coord) for coord in movement_options]
                dist_from_target.sort(key=lambda tup: tup[0], reverse=False)
                new_coords = dist_from_target[0][1]
                self.model.grid.move_agent(self, new_coords)
```
(Commenti lunghi del notebook accorciati.) Il mescolamento con `random.shuffle` serve a non favorire sempre la cella o il bersaglio in basso a sinistra, perché `get_neighbors` e `get_neighborhood` restituiscono le celle in quell'ordine.
**Esperimento**: `seed_total = 3` simulazioni, 9 umani, griglia 10×10, zombie in (0, 0), al massimo 50 tick o fino all'ultimo umano. Per ogni run si salvano un PNG per tick e una GIF (`imageio`), il tick finale (`t_results`), l'età media degli umani e l'età di ciascun umano per posizione di partenza. Poi tre grafici: istogramma della durata massima della vita umana, istogramma dell'età media, **heatmap** dell'età media per posizione di partenza (`plt.pcolor` con `cmap='hot'`). A schermo (`BT-02 @ 01:30:22`) l'istogramma ha barre attorno a 17, 18 e 25 tick e la heatmap valori fino a circa 35.
Il docente: tra gli output ci sono le distribuzioni dell'età massima degli umani che sopravvivono su tre simulazioni, "ma potremmo anche rappresentare la posizione degli zombie e del numero di infetti e quindi del numero dei guariti alla fine della simulazione" (`BT-02 @ 01:30:13`).
Verificato per esecuzione: con 3 run (seed fisso) l'ultimo umano è convertito ai tick 25, 25, 37; su 100 run fra 13 e 46 (mediana 32), mai al limite di 50. I valori a schermo cambiano a ogni esecuzione perché `random` non ha seme fisso.
> **Correzione:** nel modello ad agenti non esistono guariti né altri compartimenti oltre umano e zombie: la conversione è **irreversibile** e deterministica (basta essere adiacenti allo zombie che ti ha scelto come bersaglio). Anche i parametri citati nell'esercizio finale, "tasso di contagio, velocità degli zombie, capacità di resistenza degli esseri umani" (`BT-02 @ 01:31:20`), non sono nel codice: `speed` è fissato a 1 ("hardcoded at one for now") e non c'è probabilità di contagio né resistenza. Per fare l'esercizio vanno aggiunti, per esempio una probabilità di conversione al contatto e velocità diverse per umani e zombie (con la logica per non entrare in celle occupate, come avverte il commento del notebook).
> **Nota aggiunta:** tre fragilità della cella dei grafici, verificate. (1) `bins=max(t_results)-min(t_results)` vale 0 se tutti i run finiscono allo stesso tick, e `plt.hist` va in errore; con 3 run è possibile. (2) `plt.yticks(list(range(80, 10)), "")`: `range(80, 10)` è vuoto, quindi l'asse y resta senza tacche; probabilmente si intendeva `range(0, 80, 10)`. (3) La condizione per salvare le immagini, `seed%(seed_total/10) == 0`, con `seed_total = 3` vale solo per il seed 0 (resto in virgola mobile di 0.3): le GIF si producono per un run solo.
## 13. Esercizi e collegamento con il test finale
`BT-02 @ 01:30:45`
Slide "Exercises: study the model": "Try adjusting the parameters under various settings. How sensitive is the stability of the model to the particular parameters? Can you find any parameters that generate a stable ecosystem?"
A voce (`BT-02 @ 01:31:20`): sperimentare con l'invasione zombie (tasso di contagio, velocità, resistenza degli umani) o con il preda-predatore (numero di prede e predatori, dimensione dello spazio), e soprattutto **riflettere** sul significato di ogni cambiamento di parametro, anticipando cosa accadrebbe spostandolo in un intervallo di valori, invece di limitarsi a eseguire codice scritto da altri.
<table header-row="true">
<tr>
<td>Test finale 2026</td>
<td>Dove nel capitolo</td>
</tr>
<tr>
<td>Definizione di ABMS (max 3000 caratteri)</td>
<td>sezioni 1, 4, 5</td>
</tr>
<tr>
<td>Caratteristiche di un ABMS</td>
<td>sezioni 4 (Agent Features), 5, 6</td>
</tr>
<tr>
<td>Quando ODE e quando ABMS</td>
<td>sezione 8 (Applicability, Agent vs Macro)</td>
</tr>
<tr>
<td>Pratica (1): Mesa preda-predatore su griglia toroidale, animazione, grafici, rapporto</td>
<td>sezioni 10 e 11</td>
</tr>
</table>
> **Nota aggiunta:** per la pratica (1) il punto di partenza naturale è il codice della sezione 10 (griglia toroidale, DataCollector, grafico). Le due osservazioni verificate nelle sezioni 10 e 11 sono rilevanti per il rapporto: con le regole del 2025 le prede si estinguono comunque perché non si nutrono; con quelle del 2026 le prede crescono in modo esponenziale e i predatori si riproducono a ogni tick dopo il primo pasto. Un ecosistema stabile, come chiede la slide degli esercizi, richiede di correggere una delle due dinamiche.
## 14. Glossario, punti incerti, materiale usato
### Glossario
- **ABM / ABMS:** Agent Based Modeling (and Simulation), modellazione e simulazione basate su agenti.
- **Agente:** entità autonoma con uno stato, regole di comportamento e un ambiente, che interagisce con altri agenti.
- **Comportamento emergente:** comportamento del sistema che non si deduce dai comportamenti dei singoli.
- **Tick:** unità di tempo discreto della simulazione; tra due tick le azioni si considerano simultanee.
- **Vicinato di Moore / von Neumann:** 8 celle attorno all'agente / 4 celle ortogonali; von Neumann ruotato: le 4 diagonali.
- **Griglia toroidale:** griglia in cui i bordi opposti sono collegati.
- **Scheduler:** componente di MESA che tiene traccia degli agenti e ne attiva lo `step` (`RandomActivation`: ordine casuale a ogni tick).
- **DataCollector:** componente di MESA che registra variabili del modello a ogni tick.
- **ODD:** Overview, Design concepts, Details, protocollo standard per descrivere modelli ad agenti (Grimm et al.).
- **Reinforcement learning:** apprendimento basato su ricompense ottenute dall'ambiente.
### Punti incerti
- `[?]` "i predatori sono stati in\[?\]... le prede" (`BT-02 @ 01:25:44`): frase troncata; il senso probabile è che i predatori hanno sterminato le prede.
- `[illeggibile]` ultimo argomento della firma di `PredatorPrey.__init__`, tagliato sul bordo dello schermo; ricostruito come `predator_reproduce`.
- Nomi trascritti male e corretti nel testo: "mur" → Moore; "fornoi man", "von neumann" → von Neumann; "messa", "mesa" → MESA; "flame di più", "frame gpu" → FLAME GPU; "green" → Grimm; "ferro ormoni" → feromoni; "lot cavol terra" → Lotka-Volterra; "logica FATSY" → logica fuzzy; "rimu vei gente" → `remove_agent`; "metodo it" → `eat`.
### Materiale usato
- `Materiale/Teams/III lezione/ABMS.pdf` (testo e figure; le slide a immagine lette dai fotogrammi)
- Fotogrammi `BT-02` delle slide (`00:31:35`, `00:35:38`, `00:41:03`, `00:43:17`, `00:55:45`, `01:12:27`) e del codice (`01:17:56`-`01:30:22`)
- `Materiale/Teams/colab/Biotech_LEZIONE3.ipynb`, `Materiale/Teams/colab/Zombie_ABMS_lezione_3_Biotech.ipynb`
- `Materiale/Teams/Test_Finale_BDP_26.pdf`
- Registrazione `Teams 3` (20/05/2026), trascrizione Stream da `0:53:55` a `0:57:51`
- Verifica: `verifica_bt02.py` (`mesa==0.9.0`)
