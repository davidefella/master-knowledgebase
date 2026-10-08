# 01 - Data science e scalabilità

> Fonte Notion: https://app.notion.com/p/3dd12abc808d8170be0bf5b20b07ac90 — ultima modifica 2026-09-17T09:19:53.522Z

Fonti: slide `MDA0` e `MDA1Definitions`, lezioni `LSD-01` (intera) e `LSD-02` (00:00 → 00:22).
## 1. Il corso
Il docente lavora all'IAC-CNR (Istituto per le Applicazioni del Calcolo), dove si occupa delle attività di intelligenza artificiale, ed è docente a Roma Tre di un corso di linguaggi di programmazione e di uno di calcolo parallelo e distribuito. Questo modulo, dice, tocca in piccolo gli argomenti di entrambi (`LSD-01 @ 00:01:23`). Ha partecipato al progetto europeo TAILOR sull'AI affidabile e la sua ricerca riguarda calcolo distribuito, cloud, analisi di dati per individuare anomalie e sicurezza (intrusion detection, sicurezza della virtualizzazione e delle GPU).
**Filo conduttore** dichiarato (`MDA0`, slide 8): calcolo distribuito, intelligenza artificiale, sicurezza. A lezione lo riassume come "calcolo distribuito, intelligenza artificiale e retrogusto di sicurezza", applicati all'analisi dei dati con linguaggi eterogenei (`LSD-01 @ 00:20:04`).
**Programma dichiarato** (`MDA0`, slide 4): introduzione alla data science, fondamenti dei linguaggi di programmazione, selezione e valutazione dei modelli, storage e calcolo su cloud e distribuiti, multithreading, algoritmi paralleli e distribuiti; strumenti pratici (version control, shell e scripting, IDE); installazione e programmazione in linguaggi eterogenei (Rust, Java) e in scenari HPC (cloud, microservizi).
> **Nota aggiunta:** il programma delle slide è più ampio del materiale effettivamente distribuito. Selezione dei modelli, cloud storage e la parte pratica su version control e shell non hanno slide dedicate.
**Obiettivi** (slide 6): incuriosirsi alla data science, conoscere scenari e strumenti, capire l'impatto dei linguaggi di programmazione, poter scegliere in modo più consapevole.
**La posizione del docente su Python** (`LSD-01 @ 00:13:42`–`00:17:23`). Si dichiara "biased" verso Rust e critico verso Python. Ne riconosce il successo, anche in AI, e lo considera ottimo per scopi didattici e per provare rapidamente librerie attraverso le loro API, ma non "la soluzione one size fits all": ha dei limiti, che il corso mostrerà. Lo scopo è capire evoluzione e involuzione dei linguaggi per scegliere in modo informato quando si deve dare una soluzione implementativa a un problema di elaborazione dei dati.
## 2. Cos'è la data science
**Definizione** (slide 2): lo studio dei dati per estrarne informazioni significative per il business. È un approccio multidisciplinare che combina matematica, statistica, intelligenza artificiale e ingegneria informatica per analizzare grandi quantità di dati, e risponde a quattro domande: *cosa è successo, perché è successo, cosa succederà, cosa si può fare con i risultati*.
Il docente aggiunge un punto che dà senso al titolo del corso (`LSD-01 @ 00:21:46`): passare dalla teoria alla pratica significa fare i conti con calcolatori che hanno capacità finite, e quindi sfruttarle al meglio per processare i dati.
La sequenza delle domande descrive un percorso: si parte dal collegare un dato grezzo a un evento reale, si passa a capirne le cause e la sequenzialità, poi a prevedere cosa accadrà sulla base dello storico, e infine a usare queste previsioni per intervenire. È il passaggio "da una parte puramente osservativa a una parte più reattiva" (`LSD-01 @ 00:22:25`–`00:24:47`).
### Perché è importante
Slide 3: le organizzazioni sono sommerse di dati raccolti automaticamente da dispositivi e sistemi online (e-commerce, medicina, finanza), in forma di testo, audio, video e immagini.
Gli esempi del docente (`LSD-01 @ 00:26:09`–`00:31:34`):
- lo **smartphone** come sensore principale, sempre in ascolto: audio, posizione, video
- la **profilazione** degli utenti da parte delle grandi piattaforme, per vendere i dati alle aziende e "venderci dei bisogni"
- i **sistemi di pagamento** e i **dati medici**, con grandi potenzialità e grandi preoccupazioni
- **VirusTotal** come esempio dei rischi della circolazione dei dati: il file caricato viene analizzato da molti antivirus, ma se contiene dati sensibili questi diventano accessibili a una platea mondiale
**Chi consuma più dati dal web?** (`LSD-01 @ 00:32:12`–`00:38:36`). Dopo aver scartato social e motori di ricerca, la risposta del docente sono i modelli di intelligenza artificiale generativa, che per l'addestramento devono "masticare" la maggior quantità possibile di testi e immagini. Serve una capacità di analisi molto scalabile. Il training avviene però in modo black box, su fonti non verificate in cui "si dice tutto e il contrario di tutto": una delle cause delle allucinazioni. Filtrare le fonti riduce le allucinazioni ma limita i dati di training.
### Storia e futuro
Slide 4: il termine compare negli anni '60 come sinonimo di statistica; alla fine degli anni '90 viene formalizzato come disciplina autonoma con tre aspetti: **progettazione** dei dati, **raccolta**, **analisi**.
Il docente sposta l'accento (`LSD-01 @ 00:40:15`): oggi raccogliere dati è facile, il problema vero è analizzarli "in tempi umani". Le tecniche di machine learning rendono l'elaborazione più veloce, ma non necessariamente più affidabile o trasparente, e c'è ancora spazio per il lavoro umano, se non altro per controllare queste tecnologie.
Slide 5: AI e ML hanno reso l'elaborazione più efficiente; la domanda dell'industria ha creato un ecosistema di corsi e posizioni; la multidisciplinarità richiesta fa prevedere una forte crescita.
## 3. I quattro livelli di analisi
<table header-row="true">
<tr>
<td>Analisi</td>
<td>Domanda</td>
<td>Tecniche (slide)</td>
<td>Esempio delle slide</td>
</tr>
<tr>
<td>**Descrittiva**</td>
<td>cosa è successo / sta succedendo</td>
<td>visualizzazioni: torte, barre, linee, tabelle, narrazioni generate</td>
<td>biglietti prenotati al giorno: picchi, cali, mesi migliori</td>
</tr>
<tr>
<td>**Diagnostica**</td>
<td>perché è successo</td>
<td>drill-down, data discovery, data mining, correlazioni</td>
<td>il picco di un mese si spiega con un evento sportivo mensile in una città</td>
</tr>
<tr>
<td>**Predittiva**</td>
<td>cosa succederà</td>
<td>machine learning, forecasting, pattern matching, modelli predittivi</td>
<td>previsione dei picchi di maggio per certe destinazioni, pubblicità mirata da febbraio</td>
</tr>
<tr>
<td>**Prescrittiva**</td>
<td>cosa conviene fare</td>
<td>graph analysis, simulazione, complex event processing, reti neurali, recommendation engine</td>
<td>stimare le prenotazioni per diversi livelli di spesa su diversi canali di marketing</td>
</tr>
</table>
### Descrittiva
Il cuore è la **visualizzazione**, che semplifica il riconoscimento di fenomeni da parte di un umano, ma può alimentare anche strumenti automatici. Esempio del docente: un sistema di prenotazione (di una biblioteca) in cui le visualizzazioni mostrano i momenti di massimo e minimo e la distribuzione spaziale e temporale degli eventi (`LSD-01 @ 00:43:43`–`00:46:33`).
### Diagnostica
Fa un passo oltre la visualizzazione: dà una **motivazione** a quello che è successo (un'alterazione dovuta a un attacco, un guasto, un'infezione). L'analogia del docente: la macchina che produce una TAC fa analisi descrittiva, chi la interpreta fa diagnostica (`LSD-01 @ 00:47:04`). Il **drill-down** scende da un numero aggregato di eventi ai sottoinsiemi di dati in cui si sono verificati; le diverse trasformazioni dei dati fanno emergere aspetti diversi del loro andamento. L'obiettivo è legare con un rapporto di causa-effetto un'anomalia a un altro evento.
### Predittiva
Se conosco i rapporti di causa-effetto tra grandezze, posso prevedere l'andamento futuro dallo storico. Nelle slide: i computer vengono addestrati a "fare reverse engineering" delle connessioni causali nei dati. Il docente nota che oggi questo campo è dominato ("abusato") dal machine learning (`LSD-01 @ 00:51:56`).
Esempio del docente: i pattern di prenotazione negli **anni giubilari**, con picchi in mesi prevedibili (`LSD-01 @ 00:53:34`). Lo storico è indispensabile. Il vantaggio è non essere colti di sorpresa dalle conseguenze di un evento: un approccio **proattivo**.
### Prescrittiva
È "il passo successivo": non solo prevede, ma **indica la reazione migliore** e ne valuta le conseguenze, permettendo analisi *what-if* e la scelta, anche automatica, della risposta ottimale (`LSD-01 @ 00:55:09`). Il livello massimo è un sistema capace di *self-healing*.
Esempio del docente dalla sicurezza di rete: sulla base dello storico e dei pattern di eventi, il sistema decide di chiudere l'accesso a un servizio, filtrare i pacchetti provenienti da un'area geografica o reindirizzare i flussi su un'altra sottorete (`LSD-01 @ 00:56:12`).
**I rischi** secondo il docente:
- **risposta indotta** (`LSD-01 @ 00:58:29`): se un attaccante sa che un certo volume di pacchetti fa bloccare automaticamente degli indirizzi IP, può sfruttare quel comportamento appreso per colpire terzi. La difesa automatica diventa essa stessa un vettore di attacco.
- **medicina** (`LSD-01 @ 01:00:10`): sostituire il medico di base con un'AI che prescrive cure è preoccupante, perché i modelli sono poco trasparenti e possono essere indotti in errore.
- **prezzi dinamici** (`LSD-01 @ 01:01:44`): nell'esempio dei voli, l'analisi prescrittiva serve ad alzare i prezzi nei momenti di massima domanda. Un data scientist che lavora per il consumatore potrebbe usare lo stesso approccio al contrario, per prenotare minimizzando i costi.
### Predittiva e prescrittiva a confronto
<table header-row="true">
<tr>
<td></td>
<td>Predittiva</td>
<td>Prescrittiva</td>
</tr>
<tr>
<td>Output</td>
<td>una previsione (cosa succederà, con quale probabilità)</td>
<td>una decisione o raccomandazione (cosa fare)</td>
</tr>
<tr>
<td>Relazione</td>
<td>presuppone la diagnostica (rapporti causa-effetto)</td>
<td>presuppone la predittiva e ci aggiunge la valutazione delle alternative</td>
</tr>
<tr>
<td>Tecniche</td>
<td>ML, forecasting, pattern matching</td>
<td>simulazione, graph analysis, complex event processing, recommendation engine, reti neurali</td>
</tr>
<tr>
<td>Atteggiamento</td>
<td>proattivo: non farsi sorprendere</td>
<td>reattivo o automatico: intervenire, fino al self-healing</td>
</tr>
<tr>
<td>Utile per</td>
<td>pianificare (campagne, capacità, domanda)</td>
<td>ottimizzare decisioni con molte alternative: marketing, pricing, difesa di rete, raccomandazioni</td>
</tr>
</table>
## 4. Cosa serve al data scientist
Slide 11: una prospettiva **olistica** su teoria, tecnologia e strumenti, e il **lateral thinking**. Il docente insiste sul secondo punto: oltre al ragionamento "verticale" standard, esplorare strade non convenzionali, un concetto che fa risalire agli anni '60 (`LSD-01 @ 01:04:53`). Lo riprende alla fine della lezione come chiave per la scalabilità: invece di comprare un computer più veloce, ripensare l'approccio (`LSD-01 @ 01:18:03`).
> **Nota aggiunta:** l'espressione *lateral thinking* è di Edward de Bono (1967): risolvere un problema cambiando il modo di impostarlo, invece di approfondire la strada logica già intrapresa.
## 5. Scalabilità
**Definizione** (slide 12): la proprietà di un sistema di gestire una quantità di lavoro crescente **aggiungendo risorse**. Si applica a computer, reti, algoritmi, protocolli, programmi e applicazioni.
Il docente precisa che aggiungere risorse **non basta di per sé**: "non è che mettendo più benzina in una macchina ci potete fare entrare 10 persone invece di 5" (`LSD-01 @ 01:07:43`).
La scalabilità riguarda spesso **più grandezze insieme**. Un motore di ricerca deve scalare sia sul numero di utenti contemporanei sia sul numero di pagine indicizzate per unità di tempo (slide 12; `LSD-01 @ 01:08:54`).
**Webscale** (slide 12): un approccio architetturale che porta nei data center aziendali le capacità delle grandi aziende di cloud computing, cioè la capacità di servire l'intero web come fanno Google, Amazon e Microsoft.
### Scale-up e scale-out
<table header-row="true">
<tr>
<td></td>
<td>Scale-up (verticale)</td>
<td>Scale-out (orizzontale)</td>
</tr>
<tr>
<td>Cosa si fa</td>
<td>si potenziano le unità esistenti: CPU più veloce, più memoria, disco più grande (anche su una VM)</td>
<td>si aggiungono unità: 10 server invece di 1, 100 indirizzi IP invece di 1</td>
</tr>
<tr>
<td>Limite</td>
<td>fisico: la CPU più potente che esiste in quel momento</td>
<td>coordinamento: le unità competono per le risorse condivise</td>
</tr>
<tr>
<td>Impatto sul software</td>
<td>nessuna o poche modifiche</td>
<td>servono linguaggio, algoritmi e applicazioni adatti a distribuire il carico</td>
</tr>
<tr>
<td>Pro (slide)</td>
<td>non aggiunge infrastruttura né attività di hosting</td>
<td>preferibile ad esempio in reti geograficamente distribuite, dove la distanza rende difficile lo scale-up</td>
</tr>
<tr>
<td>Costi</td>
<td>sostituzione dell'hardware</td>
<td>consumi e costi crescono di solito linearmente con il numero di unità</td>
</tr>
</table>
**L'analogia del bar** (`LSD-01 @ 01:15:21`). Scale-up significa sostituire un barista lento con uno velocissimo, ma c'è un limite ai caffè che una persona può fare in un'unità di tempo. Scale-out significa avere tre baristi, ma tre baristi nello stesso bar competono per le stesse risorse, e la cosa "va identificata, va progettata".
**Il punto chiave per il corso** (`LSD-01 @ 01:16:24`–`01:18:03`). Per fare scale-out servono il linguaggio opportuno, l'approccio tecnico-scientifico opportuno, algoritmi che permettano la scalabilità orizzontale, applicazioni integrabili che distribuiscano il carico su più istanze. Lo scale-up invece non chiede di cambiare nulla: un'analisi lenta in Python gira più veloce su un computer più potente, ma solo fino allo speedup della nuova macchina. Per una scalabilità vera bisogna ripensare l'approccio.
**Quale conviene per la data science.** Il docente è netto: lo scale-out è "molto più utile" a scala web e in generale preferibile, perché lo scale-up ha il limite fisico della singola macchina (`LSD-01 @ 01:12:46`). Le slide sono più sfumate (slide 14): lo scale-up "è spesso desiderabile" perché non aggiunge infrastruttura, e lo scale-out è preferibile in alcuni scenari.
> **Nota aggiunta:** la competizione tra i baristi ha una formulazione quantitativa nella **legge di Amdahl**: se una frazione *s* del lavoro non è parallelizzabile, lo speedup con *N* unità è al massimo 1 / (*s* + (1 − *s*)/*N*), e non supera mai 1/*s*. Con il 5% di lavoro sequenziale, anche infinite unità non vanno oltre 20×. È il motivo per cui lo scale-out richiede di riprogettare il software e non solo di comprare macchine; il tema torna nel capitolo su scalabilità e data race.
## 6. Scalabilità di programmi e linguaggi
Slide 15–19 di `MDA1Definitions`, commentate in `LSD-02 @ 00:00:46`–`00:22:09`. Le slide riprendono un testo di Mike Vanier (Caltech), *Scalable computer programming languages*, che è anche la base del capitolo 03.
**Programmi e algoritmi** (slide 15): un programma o un algoritmo è scalabile se funziona non solo su piccoli lavori ma è altrettanto efficace, o quasi, quando il lavoro diventa molto più grande.
**Scalabilità e complessità computazionale** (slide 16): l'esempio banale di scarsa scalabilità è un algoritmo inefficiente usato in un prototipo. Funziona sui dataset piccoli e "si pianta" su quelli grandi, perché il tempo di calcolo esplode.
Il docente precisa che la scalabilità di molti algoritmi **non è lineare** rispetto alle risorse, e porta l'esempio che userà per tutto il corso (`LSD-02 @ 00:01:34`–`00:06:13`): un prototipo in **Python** che funziona benissimo su pochi dati e non scala quando i dati crescono. Non vuol dire che Python sia inutile, ma che va "complementato" con altri approcci:
- Python rende al meglio come **linguaggio di scripting**, non come linguaggio di elaborazione diretta. Nato per quello, "fa un lavoro egregio"; il problema è quando se ne abusa.
- Quando si usa con estensioni e librerie (uno studente cita Polars e PySpark), scala perché "sotto al tappeto" lavorano altri linguaggi. È un bene che molti framework offrano API Python, ma la complessità si sposta altrove, su Spark o su TensorFlow, e il codice Python si riduce.
- Sui dataset "toy" dei corsi di Python tutto funziona; per operare in modo scalabile bisogna spesso cambiare linguaggio, sistema o algoritmo.
> **Nota aggiunta:** è il legame tra complessità e scalabilità. Con n = 10³ un algoritmo O(n²) e uno O(n log n) sono entrambi istantanei; con n = 10⁸ il primo richiede circa 10¹⁶ operazioni e il secondo circa 3·10⁹. La complessità asintotica dice come cresce il costo al crescere dei dati, cioè se aggiungere dati è sostenibile; la scalabilità in senso stretto dice se aggiungere risorse compensa quella crescita. Un algoritmo con complessità sfavorevole non diventa scalabile aggiungendo macchine.
**Scalabilità architetturale** (slide 17): un programma che non si riesce a estendere per nuovi requisiti è **fragile** (*brittle*), il contrario di scalabile. Siccome i programmi di successo crescono, uno non scalabile finisce per richiedere una riscrittura completa. La causa tipica è una **scarsa astrazione di progetto** (*design abstraction*): troppe decisioni fondamentali cablate nel codice in troppi punti, impossibili da cambiare senza introdurre bug.
Il docente lo declina così (`LSD-02 @ 00:06:50`–`00:09:21`): un'implementazione con **poca capacità di astrazione** non funziona in ambienti eterogenei, per esempio perché ha costanti o scelte cablate che la legano a un particolare ambiente e le impediscono di girare come codice distribuito. Per strutture dati che devono scalare spesso non basta ritoccare: bisogna riscrivere l'algoritmo. Linguaggi come **Java** e soprattutto **Scala** sono più "aware" della rete e risolvono i problemi di calcolo distribuito in modo più scalabile.
> **Nota aggiunta:** esempi di design abstraction che aiutano la scalabilità: un repository o DAO che isola l'accesso ai dati, così passare da un file CSV a un database tocca un solo modulo; un'interfaccia di storage che permette di sostituire il disco locale con un object storage; in data science, una pipeline scikit-learn in cui preprocessing e modello sono componenti sostituibili. Il caso opposto è il percorso di un file o il nome di una colonna ripetuti in cinquanta punti del codice.
**Riferimento** (slide 18): *Structure and Interpretation of Computer Programs* di Abelson e Sussman, testo classico sulla buona progettazione dei programmi.
**Linguaggi scalabili** (slide 18–19): la nozione di scalabilità vale per i linguaggi quanto per programmi e algoritmi. Informalmente, un linguaggio scalabile è un linguaggio in cui si possono scrivere, ed estendere, programmi molto grandi "senza soffrire troppo": **la difficoltà di gestire la complessità cresce circa linearmente con la dimensione del programma**. In un linguaggio non scalabile cresce molto più che linearmente.
Per essere scalabile un algoritmo deve esserlo in sé, ma deve anche permetterlo il linguaggio in cui lo si implementa. Non esiste un linguaggio adatto a tutto, solo vantaggi e svantaggi (`LSD-02 @ 00:10:23`).
### Perché non si riscrive tutto in un linguaggio scalabile
La domanda ovvia è: allora perché non scrivere tutto in Scala o in un linguaggio funzionale? La risposta del docente è economica, non tecnica (`LSD-02 @ 00:11:30`–`00:22:09`):
- **Non si lavora da soli.** Tutto ciò che si sviluppa si appoggia su componenti esistenti: si aggiunge il proprio delta, si combinano funzionalità, si specializza un'implementazione. Reinventare la ruota è inutile.
- **Il legacy è un investimento.** I sistemi operativi Unix-like, base del cloud e dell'HPC (e anche Windows e macOS seguono ormai la filosofia Unix), sono scritti per lo più in C, con codice che risale agli anni '80–'90. Le librerie di calcolo numerico e in virgola mobile sono in Fortran e C. Sono testate e corrette da decenni: riscriverle introdurrebbe nuovi bug e partirebbe svantaggiato.
- **Non esistono strumenti automatici affidabili** per riscriverle. L'AI generativa non dà garanzie che il codice sia affidabile o privo di bug, e meno che mai sui problemi più complessi.
- Quindi "vince il vecchio, anche se il nuovo è meglio", per costi di manutenzione, creazione e sviluppo. La sostituzione avviene solo progressivamente.
Consiglio pratico del docente: saper lavorare su sistemi **Unix-like**, in particolare Linux, perché sono la base del cloud e dei sistemi HPC (`LSD-02 @ 00:14:38`).
## Collegamento con il Questionario 1
Le pagine di `MDA1Definitions` corrispondono alle "slide" citate nel capitolo. "fine" indica la fine della registrazione.
<table header-row="true">
<tr>
<td>Domanda</td>
<td>Slide</td>
<td>Video</td>
<td>Qui</td>
</tr>
<tr>
<td>1. predittiva vs prescrittiva</td>
<td>`MDA1Definitions` p8–p10</td>
<td>`LSD-01 @ 00:23:46`–`00:25:26`, `00:51:22`–`00:56:12`, `01:01:44`–`01:04:53`</td>
<td>§3, tabella di confronto</td>
</tr>
<tr>
<td>2. a cosa serve la prescrittiva</td>
<td>`MDA1Definitions` p9–p10</td>
<td>`LSD-01 @ 00:55:41`–`01:04:53`</td>
<td>§3, Prescrittiva</td>
</tr>
<tr>
<td>3. definizione di scalabilità e dove è stata utile</td>
<td>`MDA1Definitions` p12, p15; `MDA5` p10–p14</td>
<td>`LSD-01 @ 00:34:33`–`00:36:13`, `01:06:34`–`01:10:37`; `LSD-02 @ 00:00:46`–`00:01:34`; `LSD-05 @ 01:09:06`–`01:12:58`, `01:46:23`–`01:48:09`; `LSD-07 @ 00:33:06`–`00:35:30`; `Teams Extra-1 @ 0:07:41`, `0:13:51`–`0:28:05`</td>
<td>§5; §2 (modelli generativi, webscale); capitolo 05 §5</td>
</tr>
<tr>
<td>4. esempi di scale-out e scale-up</td>
<td>`MDA1Definitions` p13–p14; `MDA5` p21–p22</td>
<td>`LSD-01 @ 01:10:37`–`01:12:46`, `01:14:01`–`01:16:24`, `01:17:33`–fine; `LSD-05 @ 01:33:53`–`01:37:34`, `01:47:35`–`01:48:09`; `LSD-07 @ 00:13:20`–`00:15:22`; `Teams Extra-2 @ 0:16:02`–`0:27:11`</td>
<td>§5, tabella e analogia del bar; capitolo 05 §4</td>
</tr>
<tr>
<td>5. quale è meglio per la data science</td>
<td>`MDA1Definitions` p14</td>
<td>`LSD-01 @ 01:12:15`–`01:14:01`, `01:16:24`–fine; `LSD-02 @ 00:00:09`–`00:00:46`; `LSD-05 @ 01:34:29`–`01:36:45`, `01:44:11`–`01:46:23`; `LSD-07 @ 00:13:57`–`00:15:22`, `00:18:42`–`00:21:29`; `Teams 5 @ 0:52:39`–`0:53:46`; `Teams Extra-2 @ 0:46:03`–`0:48:01`</td>
<td>§5, ultimo paragrafo; capitolo 05 §4 (nota)</td>
</tr>
<tr>
<td>6. complessità e scalabilità</td>
<td>`MDA1Definitions` p15–p16 (p19 parla di complessità di gestione, non computazionale)</td>
<td>`LSD-02 @ 00:01:34`–`00:03:33`; `LSD-05 @ 01:20:41`–`01:21:47`; `LSD-07 @ 00:31:35`–`00:33:06`; `Teams Extra-1 @ 0:33:28`–`0:34:30`</td>
<td>§6 (nota); capitolo 05 §3 e §5</td>
</tr>
<tr>
<td>7. design abstraction</td>
<td>`MDA1Definitions` p17–p18; `MDA3` p55–p62</td>
<td>`LSD-02 @ 00:06:50`–`00:10:56`, `00:44:54`–`00:46:07`; `LSD-03 @ 00:18:57`–`00:22:25`; `LSD-04 @ 01:42:35`–`01:55:20`; `LSD-05 @ 00:04:02`–`00:06:48`</td>
<td>§6 (nota con esempi); capitolo 03 §6</td>
</tr>
<tr>
<td>8. fattori distintivi di un linguaggio</td>
<td>nessuna slide dedicata; `MDA2_PLHistory` p2–p7; `MDA3` (intero)</td>
<td>`LSD-02 @ 00:10:23`–`00:13:15`, `00:26:17`–`00:33:13`; `LSD-03 @ 00:32:12`–`00:42:32`, `00:45:57`–`00:47:36`; `Teams Extra-2 @ 0:29:39`–`0:32:17`</td>
<td>capitolo 02 (paradigmi, tipi, memoria, compilazione o interpretazione) e capitolo 03</td>
</tr>
<tr>
<td>9. linguaggio scalabile vs non scalabile</td>
<td>`MDA1Definitions` p18–p19; `MDA3` p9, p20; `MDA16` p8–p16</td>
<td>`LSD-02 @ 00:01:34`–`00:06:50`, `00:09:21`–`00:22:09`, `01:26:36`–fine; `LSD-03 @ 00:46:30`–`00:47:36`; `LSD-04 @ 00:04:39`–`00:06:53`, `00:42:06`–`00:42:38`; `LSD-05 @ 00:40:27`–`00:43:54`, `01:37:34`–`01:39:38`, `01:55:34`–`01:57:46`; `LSD-07 @ 00:19:12`–`00:21:29`; `Teams 2 @ 1:21:04`; `Teams Extra-2 @ 1:47:56`</td>
<td>§6 (Python, Java e Scala); capitolo 02 (C); capitoli 03 e 04</td>
</tr>
<tr>
<td>10. ingredienti per affrontare problemi di data science</td>
<td>`MDA1Definitions` p2, p4, p11</td>
<td>`LSD-01 @ 00:20:35`–`00:22:25`, `00:24:47`–`00:25:26`, `00:38:36`–`00:40:51`, `01:04:21`–`01:06:34`</td>
<td>§4; §2</td>
</tr>
</table>
## Punti incerti della trascrizione
- `00:01:23` — la sigla del corso di linguaggi di programmazione che il docente tiene a Roma Tre non è comprensibile
- `00:02:16` — "corsi di L'Università di Sardegna" è quasi certamente un errore di trascrizione per i corsi di laurea di Roma Tre `[?]`
- `01:11:41` — "C++ più potente" è un errore di trascrizione per "CPU più potente", coerente con il contesto
