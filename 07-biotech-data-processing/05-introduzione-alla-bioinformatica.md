# 05 - Introduzione alla bioinformatica

> Fonte Notion: https://app.notion.com/p/3e912abc808d81e3820dd1eeb41c8487 — ultima modifica 2026-09-28T18:32:01.234Z

**Registrazione:** `BT-05` (portale, edizione 2025), durata 01:25:55. Giornata: **Day 6** (slide "Introduzione alla Bioinformatica, Biocentis, Matteo Rucco - Day 6").
**Materiale:** nessun PDF delle slide e nessun notebook di bioinformatica fra i materiali (portale e Teams): testo delle slide, pagine NCBI/BLAST e codice del notebook `Genome.ipynb` sono ricostruiti dai fotogrammi.
**Teams 2026:** nessuna registrazione 2026 copre la bioinformatica (vedi Divergenze).
> **Nota sul codice.** `Genome.ipynb` è la traduzione italiana di un tutorial pubblico sull'annotazione del genoma umano con pandas; il file `Homo_sapiens.GRCh38.85.gff3.gz` (Ensembl release 85) non è scaricabile da questo ambiente. Il codice è stato quindi eseguito su un GFF3 sintetico costruito con righe visibili a schermo (`verifica_bt05.py`, pandas 3.0): i numeri dell'output reale (righe, conteggi, statistiche) sono quelli **letti a schermo**, non ricalcolati. L'esempio k-mer è verificato per esecuzione.
## Indice
1. Che cos'è la bioinformatica
2. Esercizio: ricerca di sottostringhe e k-mer
3. Informatica prima della biologia
4. Genomica: costi, CRISPR-Cas9, big data
5. Il flusso dell'informazione biologica
6. DNA, allineamento, sintesi proteica
7. Banche dati biologiche
8. Ricerca per parola chiave: il gene Indy su NCBI
9. Il formato FASTA
10. Ricerca per similarità: BLAST
11. Colab: annotazione del genoma umano con pandas (`Genome.ipynb`)
12. Collegamento con il test finale
13. Glossario, punti incerti, materiale usato
---
## 1. Che cos'è la bioinformatica
`BT-05 @ 00:00:09`
Disciplina all'interfaccia fra biologia, informatica e matematica, con l'obiettivo di **analizzare, interpretare e visualizzare dati biologici complessi**: sequenze di DNA, RNA e proteine. Scopi: comprendere meglio i meccanismi biologici di una specie, migliorare terapie e diagnostica (`BT-05 @ 00:00:45`).
Non nasce insieme alla biologia: mancavano calcolatori potenti e soprattutto mancavano i dati. Il **Progetto Genoma Umano**, concluso nel suo corpo principale nel **2003** (e ancora in corso come raffinamento), non sarebbe stato possibile senza strumenti bioinformatici per analizzare circa **3 miliardi di nucleotidi** (`BT-05 @ 00:01:16`). Grazie alla bioinformatica si identificano geni associati a malattie, si progettano farmaci, si studia l'evoluzione molecolare. Il data scientist in bioinformatica usa sia strumenti sviluppati con i biologi sia strumenti generalisti (pulizia dei dati, machine learning, visualizzazione) per prevedere mutazioni o trovare relazioni fra geni e fenotipi (`BT-05 @ 00:01:49`).
Programma della lezione: una carrellata sugli aspetti principali, con enfasi sulle **banche dati primarie** e sui loro strumenti di analisi via web, e un esercizio finale in Colab (`BT-05 @ 00:02:25`).
Annuncio (`BT-05 @ 00:02:56`): la settimana successiva, in tre ore, chiusura degli argomenti in sospeso e un **piccolo test finale**: domande e, opzionale, una parte Python; circa un'ora, un'ora e mezza; la consegna può avvenire anche dopo, lavorando offline, con il docente connesso per i dubbi sulla parte Python (`BT-05 @ 00:03:29`). Per il test 2026 vedi **Assessment**.
Slide "Rilevanza della bioinformatica" (`BT-05 @ 00:04:02`):
- le nuove biotecnologie hanno ridotto costi e tempi di acquisizione delle informazioni sulle biomolecole, quindi esistono banche dati con informazioni su milioni di biomolecole;
- la dimensione dei problemi biologici basta a motivare lo sviluppo di algoritmi efficienti;
- i problemi sono accessibili (molti dati pubblici e letteratura) e interessanti;
- le scienze biologiche usano sempre più strumenti computazionali.
Alcuni algoritmi sono concettualmente semplici, ma senza ottimizzazione il tempo di esecuzione cresce con la lunghezza dell'input fino a diventare eccessivo (`BT-05 @ 00:04:36`). Esempio: la ricerca di sottostringhe.
## 2. Esercizio: ricerca di sottostringhe e k-mer
`BT-05 @ 00:05:16`
Una sequenza di DNA è una concatenazione di quattro lettere (A, T, C, G), molto lunga; si vuole trovare una sottosequenza (**query**) in una sequenza (**target**).
**Suddividere il target** con una finestra mobile (*sliding window*), due varianti (`BT-05 @ 00:05:51`):
- finestre **adiacenti** di lunghezza $`n`$: la finestra successiva parte subito dopo la fine della precedente (con $`n = 4`$: nucleotidi 1-4, poi 5-8, ...);
- **k-mer**: finestra di lunghezza $`k`$ che avanza di **1** (`BT-05 @ 00:06:27`); una sequenza di lunghezza $`L`$ produce $`L - k + 1`$ k-mer, molti se il target è lungo (`BT-05 @ 00:07:37`).
**L'esempio** (documento a schermo, `BT-05 @ 00:09:47`): target `ATCGACCCGAGATCG`, query `CGA`, k-mer con $`k = 2`$. Le sottosequenze della query di lunghezza 2 sono `CG` e `GA`; si cerca se almeno una di esse ha un match con i k-mer del target (`BT-05 @ 00:10:51`). Per ora basta trovare una sottostruttura della query, non la query intera; il docente osserva che, per trovare la query esatta, il k-mer dovrebbe essere lungo almeno quanto la query (`BT-05 @ 00:11:36`).
> **Correzione:** a schermo (e a voce, `BT-05 @ 00:10:17`) i 2-mer elencati sono 12: `AT TC CG GA AC CC CC CG GA AT TC CG`. Il target ha 15 nucleotidi, quindi i 2-mer sono $`15 - 2 + 1 = 14`$: mancano `AG` e `GA` in posizione 9 e 10 (da `...CGAGAT...`). Verificato per esecuzione (`verifica_bt05.py`).
**Criterio di esclusione** (`BT-05 @ 00:12:10`), proposto dagli studenti: la lettera `T` non compare nella query, quindi ogni k-mer che contiene `T` non può dare un match di due lettere su due e si scarta senza confrontarlo. Si escludono i 4 k-mer `AT`, `TC`, `AT`, `TC` ("almeno quattro sotto sequenze", `BT-05 @ 00:14:25`). Sui k-mer restanti: `CG` e `GA` sono match perfetti; `AC` no, ma resta candidato.
Verificato per esecuzione: sui 14 k-mer, 4 esclusi; 6 match perfetti (`CG` in posizione 2, 7, 13; `GA` in 3, 8, 10); la query intera `CGA` compare nel target in posizione 2 e 7 (indici da 0).
Domanda di uno studente: per escludere un k-mer non lo si sta già valutando? Il docente (`BT-05 @ 00:14:57`): il confronto completo richiede di controllare la prima lettera, poi la seconda, e così via, per ogni sottosequenza della query; il test di presenza di una lettera esclusa è un solo controllo, e nel caso fortunato scarta subito il k-mer.
In Python (`BT-05 @ 00:16:24`): il metodo speciale `__contains__` restituisce un booleano. A schermo:
```python
k_target.__contains__("T")   # True -> il k-mer va escluso
```
(`k-target` a schermo; qui con il trattino basso per renderlo un identificatore valido.)
> **Nota aggiunta:** `s.__contains__("T")` è ciò che Python invoca con l'operatore `"T" in s`, la forma idiomatica.
Il ragionamento non ha nulla di biologico: è logica e matematica, poi tradotta in algoritmo (`BT-05 @ 00:16:01`). Con sequenze più lunghe servono strumenti più evoluti (`BT-05 @ 00:17:41`):
- **calcolo parallelo**, suggerito da uno studente, per cercare le sottosequenze non in sequenza;
- **divide et impera**, alla base di importanti algoritmi di ordinamento (`BT-05 @ 00:18:11`);
- se i k-mer sono lunghi e la query contiene tutti i nucleotidi, il criterio della lettera assente non basta: si può usare la **frequenza dei nucleotidi** come criterio di inclusione o esclusione (`BT-05 @ 00:19:19`). A schermo la query modificata `CCGATAT` con l'istogramma C: 2, G: 1, A: 2, T: 2 (verificato).
## 3. Informatica prima della biologia
`BT-05 @ 00:20:55`
Consiglio del docente: molti informatici si demotivano temendo di sapere poca biologia. La biologia è vastissima; l'informatico sviluppa metodi e strumenti di cui la biologia ha bisogno. Per essere un buon bioinformatico serve una **solida base di informatica e matematica**; i concetti di biologia si acquisiscono problema per problema. Chi vuole spostarsi verso la bioinformatica consolidi i fondamenti: algoritmi di ordinamento, divide et impera, bubble sort (`BT-05 @ 00:21:30`). Le scienze biologiche non possono più fare a meno di strumenti computazionali (`BT-05 @ 00:22:00`).
## 4. Genomica: costi, CRISPR-Cas9, big data
`BT-05 @ 00:22:36`
- **Costo del sequenziamento:** da svariati miliardi di dollari a circa **1000 dollari per genoma umano**, con volumi di dati enormi. Il genetista, figura prima di nicchia perché il sequenziamento era troppo costoso per enti pubblici e privati, oggi è consultato più spesso; in caso di dubbio su patologie o predisposizioni si suggerisce una mappatura genetica. Dal campione alla mappatura dei geni servono pochi giorni (`BT-05 @ 00:23:08`).
- **CRISPR-Cas9** (`BT-05 @ 00:24:21`): tecnologia di editing genetico trovata nei batteri, nei meccanismi di difesa del loro DNA da aggressioni esterne. Due elementi: la **guide RNA**, lunga 20-23 nucleotidi, che trova la sequenza complementare nel DNA bersaglio; e la proteina **Cas9**, che taglia il DNA nel sito di aggancio (`BT-05 @ 00:25:02`). Poi gli scienziati possono introdurre o rimuovere materiale genetico, per esempio eliminare parte di un gene (degli esoni) per inibire una problematica (`BT-05 @ 00:25:38`).
> **Correzione:** a voce la guida, "una volta agganciata sul DNA target, rilascia una proteina detta Cas9" (`BT-05 @ 00:25:02`). Guide RNA e Cas9 formano un unico complesso (ribonucleoproteina) prima del riconoscimento: la guida porta Cas9 sul bersaglio, non la rilascia.
- **Sfide big data** (`BT-05 @ 00:26:09`): compressione per archiviare sequenze genomiche, clustering per trovare pattern genetici, analisi di reti per le interazioni genetiche. Il data scientist applica alla biologia metodi acquisiti in contesti più fondazionali.
## 5. Il flusso dell'informazione biologica
`BT-05 @ 00:26:42`
La bioinformatica fa da ponte fra biologia e informatica: nei sistemi biologici esistono **flussi di informazione**. Il DNA viene copiato, trascritto in RNA e tradotto in proteine funzionali; la catena si schematizza come **dati di input, elaborazione, dati di output** (`BT-05 @ 00:27:16`), e gli algoritmi bioinformatici la simulano per prevedere comportamenti biologici o trovare bersagli terapeutici.
Slide "Bioinformatica: interazione fra biologia e scienze dell'informazione" (`BT-05 @ 00:29:35`): dati di input (DNA), elaborazione (lettura, copiatura, traduzione), dati di output (proteina). Il DNA contiene le istruzioni, l'RNA le trasporta, le proteine svolgono le funzioni cellulari. Biologia e scienza dell'informazione studiano entrambe flussi di informazione, li manipolano e hanno bisogno di rappresentarli (`BT-05 @ 00:28:27`): schematizzare i processi biologici come processi logici li rende meno oscuri.
Per il data scientist (`BT-05 @ 00:30:06`): la replicazione del DNA si simula con modelli computazionali che prevedono errori di replicazione associati a mutazioni; servono strutture dati come gli **alberi filogenetici** e algoritmi paralleli, per esempio per simulare la trascrizione che avviene in parallelo su più loci.
Slide "L'informazione nei sistemi biologici viventi" (`BT-05 @ 00:30:46`): i viventi sono fatti di moltissime molecole, ognuna funzionalmente unica e costruita secondo criteri ben definiti; se ogni molecola segue un "progetto", deve esistere un luogo che immagazzina i progetti e li rende disponibili quando servono. Analogia: il DNA come **database**, o come un manuale di istruzioni in cui ogni pagina è un gene che codifica una molecola (`BT-05 @ 00:31:20`).
Per archiviare e cercare sequenze servono database ottimizzati: il docente userebbe **Elasticsearch** o **SQL** (relazionale), da cui poi i database non relazionali come quelli **a grafo** (`BT-05 @ 00:31:50`). Il DNA umano ha più di 3 miliardi di caratteri: il problema non è solo immagazzinarli ma cercarli, e un sistema **indicizzato** velocizza la ricerca (`BT-05 @ 00:32:51`). Proiettare il DNA nel digitale vuol dire stratificarlo: quali parti sono geni, e nei geni esoni, introni e altre regioni non codificanti (long non-coding RNA), poi indicizzarle (`BT-05 @ 00:33:26`).
## 6. DNA, allineamento, sintesi proteica
`BT-05 @ 00:34:04`
Slide "Biologia molecolare e informazione":
- depositario dell'informazione: il **DNA**;
- **doppia elica**: ognuna delle due eliche si ricostruisce dall'informazione dell'altra ("banca dati con sistema di backup incorporato");
- ogni elica è una lunga catena di 4 elementi, i **nucleotidi**: adenina (A), timina (T), citosina (C), guanina (G) (`BT-05 @ 00:34:38`).
Il backup naturale del DNA ha ispirato algoritmi di ridondanza in crittografia e archiviazione; il sistema immunitario ha ispirato algoritmi di apprendimento; l'evoluzione ha ispirato le euristiche di ottimizzazione degli **algoritmi genetici**, in cui il DNA di due genitori si ricombina (`BT-05 @ 00:35:08`; vedi capitolo 06).
**Allineamento** (`BT-05 @ 00:35:43`): algoritmi come **Smith-Waterman** e **BLAST** allineano sequenze e ne misurano la somiglianza, strumento fondamentale per gli studi evolutivi. Date due sequenze di lunghezza in genere diversa, si verifica se una è presente nell'altra e dove (`BT-05 @ 00:36:16`). Il docente distingue allineamento locale e globale (`BT-05 @ 00:36:55`).
> **Correzione:** a voce il globale è descritto prima come "quello più utile", che trova sottoporzioni della query nel target introducendo **gap**, poi come "quello con meno probabilità di successo perché si richiede che la query sia esattamente trovata" nel target (`BT-05 @ 00:37:26`). Le definizioni corrette: l'allineamento **globale** (Needleman-Wunsch) allinea le due sequenze per tutta la loro lunghezza; quello **locale** (Smith-Waterman, e in forma euristica BLAST) cerca le sottoregioni più simili. Entrambi ammettono gap e mismatch; nessuno dei due richiede un match esatto.
Maiuscole e minuscole (`BT-05 @ 00:37:56`): secondo il docente, in una sequenza reale la lettera maiuscola indica certezza che il nucleotide sia stato letto correttamente, la minuscola incertezza (pochi campioni, errori di gestione dell'informazione).
> **Nota aggiunta:** nei genomi di riferimento (Ensembl, UCSC) il minuscolo indica di norma regioni ripetitive "mascherate" (*soft-masking*); l'incertezza su una base si codifica con i simboli IUPAC (N per base ignota, R per A o G, ecc.). L'uso del minuscolo per basi di bassa qualità esiste in alcuni strumenti di assemblaggio, ma non è la convenzione generale.
**Sintesi proteica** (slide "Manipolazione dell'informazione - Esempio sintesi proteina", `BT-05 @ 00:38:29`):
- *copia*: un tratto di DNA (gene) viene copiato in una molecola di RNA in grado di portare l'informazione altrove (fuori dal nucleo);
- *traduzione*: l'RNA messaggero (mRNA) viene letto a gruppi di tre lettere; a ogni **tripletta** corrisponde uno di 20 amminoacidi; si sintetizza la catena di amminoacidi, la proteina (`BT-05 @ 00:39:02`).
La bioinformatica permette di simulare questi processi; il docente cita il premio Nobel legato alla predizione della struttura delle proteine e **AlphaFold** (`BT-05 @ 00:39:42`).
> **Correzione:** a voce "premio Nobel per l'intelligenza artificiale attribuito quest'anno a un chimico computazionale che lavorava per Google, nel progetto AlphaFold, che sfrutta il reinforcement learning, per predire la struttura di una proteina a partire da un gene" (`BT-05 @ 00:39:42`). Il premio è il **Nobel per la Chimica 2024**: metà a David Baker (progettazione computazionale di proteine), metà a **Demis Hassabis e John Jumper** (Google DeepMind) per la predizione della struttura delle proteine. AlphaFold 2 è un modello di **deep learning** (reti con meccanismi di attenzione) addestrato in modo supervisionato sulle strutture note, non un sistema di reinforcement learning; e predice la struttura a partire dalla **sequenza di amminoacidi**, non dal gene.
Con strumenti locali, meno potenti, il docente suggerisce di simulare la trascrizione e sintesi con **modelli markoviani** per prevedere le sequenze di amminoacidi (`BT-05 @ 00:40:46`).
> **Nota aggiunta:** dato l'mRNA, la traduzione in amminoacidi è deterministica (codice genetico, una tabella da 64 triplette). I modelli di Markov nascosti (HMM) si usano in bioinformatica per problemi con incertezza, come individuare i geni in una sequenza o classificare famiglie di proteine.
## 7. Banche dati biologiche
`BT-05 @ 00:41:17`
Oltre agli algoritmi servono dimestichezza e consapevolezza nell'uso delle banche dati. Slide "Bioinformatica, sequenze e database": tutte le biosequenze (DNA, geni, mRNA, proteine) sono immagazzinate in banche dati apposite; quella di riferimento per le proteine è **UniProt** (`www.uniprot.org`), "quasi 600.000 proteine", con il grafico "Number of entries in UniProtKB/Swiss-Prot" dal 1985 al 2015 (`BT-05 @ 00:41:50`).
Obiettivi delle banche dati: disseminare dati e informazioni biologiche, creare standard de facto sulle strutture di geni, proteine, DNA, RNA, strutturare l'informazione in modo che un computer la legga e la modifichi (`BT-05 @ 00:42:20`). Una banca dati biologica deve avere almeno uno **strumento di ricerca ed estrazione** dei dati: un file di testo, per esempio, non è una banca dati, serve un editor per estrarne qualcosa (`BT-05 @ 00:43:34`).
Storia: circa 40 anni; la prima nel **1982**, con calcolatori poco potenti e senza internet diffusa, solo reti con limitazioni (`BT-05 @ 00:44:10`). Le prime erano collezioni di file di testo, simili a pagine web statiche, senza strumenti di estrazione. UniProt, pubblicata nel **1986**, aveva all'inizio qualche decina di sequenze; nel 2015 era oltre 500.000 (`BT-05 @ 00:44:43`). Per interrogarle: SQL o Python, per esempio la libreria **Biopython**, che si interfaccia con le banche dati, scarica i dati e ne facilita l'analisi (`BT-05 @ 00:45:18`).
Slide "Banche dati biologiche" (`BT-05 @ 00:46:01`):
- **primarie** ("collettori primari"): raccolgono ogni giorno tutte le informazioni sulle biomolecole prodotte nei laboratori del mondo e le rendono disponibili, senza un vero processo di revisione;
- **secondarie**: poiché l'informazione dei collettori primari è sporca e ridondante, ne esaminano i dati, correggono gli errori, aggiungono informazioni e rendono disponibili i risultati del raffinamento. Consumano i dati delle primarie (`BT-05 @ 00:47:11`).
Slide "Banche dati primarie": **GenBank** (NCBI), **EMBL** (European Molecular Biology Laboratory) e **DDBJ** (DNA Data Bank of Japan), **sincronizzate ogni 24 ore** (`BT-05 @ 00:47:45`). GenBank contiene sequenze di milioni di organismi; durante la pandemia tutte le sequenze del coronavirus sono state condivise rapidamente tramite GenBank. I dati primari richiedono pulizia e parsing avanzati (`BT-05 @ 00:48:15`).
Slide "Banche dati secondarie" (`BT-05 @ 00:48:46`): **RefSeq** (reference sequence, NCBI) costruita su GenBank, EMBL e DDBJ; intervento umano per correggere errori ed eliminare ridondanze; aggiunta di letteratura e integrazione fra banche dati; **UniProt** (Universal Protein Resource). Un'**annotazione** è l'insieme dei dettagli su dove si trova una caratteristica biologica nel genoma e qual è la sua funzione; UniProt aggiunge funzione biologica, interazioni e variazioni clinicamente rilevanti (`BT-05 @ 00:49:16`). I dati secondari sono pronti per l'uso: per esempio le sequenze annotate di UniProt per addestrare reti neurali che prevedono l'effetto delle mutazioni sulla funzione proteica.
> **Correzione:** a voce "NCBI è una banca dati primaria; UniProt e GenBank sono raffinamenti di NCBI", banche dati validate (`BT-05 @ 00:46:38`). La slide stessa (`BT-05 @ 00:47:45`) mette **GenBank** fra le primarie: GenBank è la banca dati primaria di sequenze gestita da NCBI (NCBI è l'ente, non una banca dati). La secondaria di NCBI è **RefSeq**; **UniProt** è del consorzio UniProt (EMBL-EBI, SIB, PIR), non un raffinamento di NCBI.
## 8. Ricerca per parola chiave: il gene Indy su NCBI
`BT-05 @ 00:49:46`
Le banche dati si usano via interfaccia web o API, cercando per parole chiave. Slide "Come usare una banca dati" (`BT-05 @ 00:50:19`): l'effetto delle mutazioni si studia su organismi facili da manipolare in laboratorio; nel moscerino della frutta, *Drosophila melanogaster*, è stato identificato un gene che, se mutato, **raddoppia la durata media della vita**: **INDY** (*I'm Not Dead Yet*). Ogni gene ha un nome, o almeno un'etichetta.
Il docente aggiunge che Indy è attivo nei tessuti ad alta richiesta energetica (intestino, muscoli); la sua ridotta attività abbassa il metabolismo, con un effetto simile alla restrizione calorica (`BT-05 @ 00:54:36`); è stato identificato con approcci genetici classici e, con NCBI e BLAST, se ne sono trovate varianti (`BT-05 @ 00:55:38`). Per un data scientist è un caso di studio: pipeline per le mutazioni, espressione nei tessuti, reti di interazione genetica.
**Google contro NCBI** (slide "Primo tentativo: usiamo Google & NCBI", `BT-05 @ 00:51:29`). Demo:
1. Google "indy": risultati che non c'entrano; serve raffinare con "melanogaster" (`BT-05 @ 00:52:12`).
2. NCBI: già in digitazione suggerisce *Drosophila melanogaster*. La scheda **Gene** ("Indy I'm not dead yet \[Drosophila melanogaster (fruit fly)\]", Gene ID 40049) dà sequenza, informazioni fenomenologiche, bibliografia e la posizione: **cromosoma 3** (`BT-05 @ 00:52:52`).
3. Vista **Nucleotide** (`BT-05 @ 00:54:01`): l'etichetta Indy compare in più organismi (anche *Drosophila suzukii*); filtrando su melanogaster si vedono le **varianti di trascritto** (A, B, C, D, ...), per esempio "transcript variant D, mRNA, 2,581 bp, NM_001169994.2" (`BT-05 @ 00:56:11`). Le differenze fra varianti si potrebbero studiare con i k-mer della sezione 2 (`BT-05 @ 00:57:20`).
4. Record GenBank `AF509505.1` ("Drosophila melanogaster INDY transporter protein (Indy) mRNA, complete cds", 2602 bp, mRNA lineare) (`BT-05 @ 00:58:07`): la prima riga (LOCUS) dà lunghezza e tipo di molecola; il **codice di accesso** (*accession*) è l'identificativo univoco da usare nelle ricerche successive, più sicuro dell'etichetta leggibile (scrivendo "indi" si otterrebbe altro) (`BT-05 @ 00:58:38`). In fondo la sequenza; evidenziata la parte codificante (CDS), cioè la porzione del gene tradotta in proteina (`BT-05 @ 00:59:09`).
## 9. Il formato FASTA
`BT-05 @ 00:59:51`
Le sequenze si esportano in locale, per esempio in **FASTA**, compatibile con la maggior parte degli strumenti. Slide "FASTA" (`BT-05 @ 01:00:29`):
- il formato FASTA (text) mostra solo la sequenza, **senza spazi e senza numeri**, e senza caratteri invisibili (a differenza delle altre visualizzazioni);
- in questo formato la sequenza è input per programmi di analisi (ad esempio la composizione: frequenza di A, C, G, T).
Un file FASTA inizia con una **riga di intestazione** marcata da `>`. Esempio a schermo, la sequenza di Indy scaricata da NCBI:
```plain text
>gi|442633232|ref|NM_079426.4| Drosophila melanogaster I'm not dead yet (Indy), transcript variant A, mRNA
ATTCAGTCGCGCATTTCACCGTTTCGAATCGGACGAACCGGGCGTGCTTGCTCTCCTGCTGCTTTCGAG
...
```
L'intestazione dà codice di accesso, organismo e tipo di molecola (`BT-05 @ 01:01:10`). Un FASTA è input per strumenti di allineamento come BLAST o per analisi statistiche come la frequenza dei nucleotidi.
> **Correzione:** a voce "la frequenza di co-occorrenza delle lettere C e G è un indice di qualità: tanto più alta, tanto maggiore la qualità della sequenza" (`BT-05 @ 01:01:10`). Il **contenuto in GC** (frazione di G e C) e la frequenza dei dinucleotidi **CpG** sono proprietà composizionali della sequenza: variano fra specie e regioni, influenzano la stabilità della doppia elica e servono, per esempio, a individuare le "isole CpG" vicino ai promotori (nel GFF3 della sezione 11 compaiono righe `logic_name=cpg`). Non misurano la qualità del sequenziamento, che si esprime con i punteggi di qualità per base (Phred, nel formato FASTQ).
## 10. Ricerca per similarità: BLAST
`BT-05 @ 01:02:05`
La **ricerca esplorativa** serve quando si ha una sequenza sconosciuta (per esempio estratta in un esperimento con i biologi) e non si può cercare per parola chiave: si vuole sapere se corrisponde a una struttura molecolare nota (`BT-05 @ 01:02:40`). Lo strumento è **BLAST** (*Basic Local Alignment Search Tool*, NCBI; slide "Ricerca tramite similarità di sequenza", `BT-05 @ 01:03:11`): confronta nucleotidi con nucleotidi (blastn), proteine con proteine (blastp) e sequenze nucleotidiche tradotte con proteine e viceversa (blastx, tblastn) (`BT-05 @ 01:03:45`).
Demo (`BT-05 @ 01:04:15`): Nucleotide BLAST, si incolla la sequenza (copiandola dal PowerPoint si inseriscono spazi da togliere, `BT-05 @ 01:04:45`) e si lancia la ricerca di sequenze simili. Risultato (`BT-05 @ 01:05:18`): con ottima probabilità la sequenza appartiene al gene umano della **tioredossina** (TXN).
- **Allineamento** (`BT-05 @ 01:06:10`): query e *subject* (il target) allineati; nessun **gap** (mancherebbe almeno una lettera nel subject) e nessun **mismatch** (mancherebbe la linea che collega le lettere) (`BT-05 @ 01:06:41`). Dal codice di accesso si torna alla scheda NCBI: NCBI è una banca dati vera e propria perché, oltre ai dati, offre strumenti di visualizzazione e analisi (`BT-05 @ 01:07:17`).
- **Grafici e tassonomia** (`BT-05 @ 01:07:54`): score di similarità con le sequenze note e specie in cui si sono trovati risultati. Lo **score** misura la qualità dell'identificazione: il più alto è in *Homo sapiens*, **1218** (`BT-05 @ 01:08:26`); a seguire altri primati (il docente cita il gorilla).
- **Tabella** (`BT-05 @ 01:09:02`), prima riga a schermo: "Homo sapiens thioredoxin (TXN), transcript variant 2, mRNA", Max Score 1218, Total Score 1218, **Query Cover 81%**, E value 0.0, **Per. Ident 100.00%**, lunghezza 677, `NM_001244938.2`. La query è presente per l'81% della sua lunghezza, e in quel tratto è identica al 100%.
> **Nota aggiunta:** nella tabella a schermo il secondo risultato è *Theropithecus gelada* (score 1044) e il gorilla compare più in basso (score 590); tutti i primi risultati sono primati o altri mammiferi.
**E-value** (`BT-05 @ 01:09:36`): per il docente, misura statistica della probabilità che l'allineamento sia casuale; un valore molto basso, vicino a zero, indica forte similarità e una possibile relazione funzionale o evolutiva.
> **Correzione:** l'E-value non è una probabilità ma il **numero atteso** di allineamenti con punteggio almeno uguale che si troverebbero per caso cercando in una banca dati di quelle dimensioni ($`E = K m n e^{-\lambda S}`$, con $`m`$, $`n`$ lunghezze di query e banca dati, $`S`$ lo score). Può superare 1; solo per valori piccoli è approssimativamente uguale alla probabilità di almeno un match casuale ($`P = 1 - e^{-E}`$). La lettura pratica del docente (più basso, meno casuale) resta corretta.
Slide "Riepilogo" (`BT-05 @ 01:10:12`): le banche dati biologiche sono collezioni di informazioni sulle molecole dei viventi, di grandi dimensioni, rese disponibili con strumenti di ricerca specializzati. Due tipi di ricerca:
- **per parola chiave**: estrae una o più sequenze combinando parole chiave, con filtri progressivi; non si può usare senza informazioni sull'obiettivo;
- **per similarità di sequenza**: una sequenza sonda al posto delle parole chiave, per trovare le sequenze più simili in banca dati.
Limiti e sviluppi (`BT-05 @ 01:10:46`): secondo il docente BLAST online non accetta sequenze con più di 10.000 nucleotidi, oltre i quali serve BLAST in locale, scaricabile e installabile gratuitamente. L'output di BLAST si può arricchire con annotazioni funzionali in file **GFF** o **BED**, separati da tabulazione, con nome del gene, posizione e descrizione della funzione (`BT-05 @ 01:11:27`); gli output di BLAST si prestano a dashboard interattive (`BT-05 @ 01:11:57`). In biologia gli strumenti agnostici al dominio (Google) si usano solo dopo aver ottenuto informazioni dettagliate con gli strumenti del settore (BLAST, NCBI, RefSeq) (`BT-05 @ 01:12:32`).
## 11. Colab: annotazione del genoma umano con pandas (`Genome.ipynb`)
`BT-05 @ 01:12:32`
Esercizio di analisi del **file di annotazione** del genoma umano: file separato da tabulazioni con posizione, nome e ruolo delle entità molecolari (`BT-05 @ 01:13:07`). Il notebook, in italiano, apre con due domande: "Quanta parte del genoma è incompleta?" e "Quanto è lungo un gene tipico?".
### 11.1 Caricamento
`BT-05 @ 01:13:45`
Il file GFF3 pesa circa 37 MB contro circa 3 GB di testo del genoma, perché contiene solo le annotazioni; le sequenze stanno in FASTA.
```python
!wget ftp://ftp.ensembl.org/pub/release-85/gff3/homo_sapiens/Homo_sapiens.GRCh38.85.gff3.gz

import pandas as pd
import re
import matplotlib as plt

col_names = ['seqid', 'source', 'type', 'start', 'end', 'score', 'strand', 'phase', 'attributes']
df = pd.read_csv('Homo_sapiens.GRCh38.85.gff3.gz', compression='gzip',
                 sep='\t', comment='#', low_memory=False,
                 header=None, names=col_names)
```
(L'URL completo del `wget` è tagliato a schermo \[illeggibile\]; quello sopra è ricostruito dal nome del file e dalla release, "saved \[38469475\]" byte.) Il file non è un CSV standard (`BT-05 @ 01:14:20`): `compression='gzip'` perché è compresso, `comment='#'` per ignorare le righe di commento, `sep='\t'` perché il separatore è la tabulazione, `names` perché non c'è intestazione (`BT-05 @ 01:14:51`).
> **Nota aggiunta:** `import matplotlib as plt` importa il pacchetto, non `pyplot`: `plt.show()` fallirebbe, infatti nel notebook è commentato (`#plt.show()`). I grafici funzionano lo stesso perché passano da `DataFrame.plot` di pandas. La forma corretta è `import matplotlib.pyplot as plt`.
### 11.2 Esplorazione
`BT-05 @ 01:15:24`
```python
pd.set_option('display.max_colwidth', None)
df.head(10)
df.info()
df.seqid.unique()
df.source.value_counts()
```
- `head(10)`: righe del cromosoma 1, con `strand` (su quale elica si legge, da sinistra a destra o viceversa) e il materiale biologico associato (`BT-05 @ 01:16:01`). Le prime righe sono `chromosome` e `biological_region` (fra cui `logic_name=cpg`, `logic_name=eponine`).
- `info()` a schermo: **2.601.849 righe**, 9 colonne, `start` ed `end` `int64`, le altre `object` (stringhe o valori misti), circa 178.7 MB in memoria (`BT-05 @ 01:16:35`).
- `seqid.unique()`: **194** sequenze distinte, cromosomi 1-22, X, Y, il DNA mitocondriale (MT) e sequenze il cui nome inizia per KI o GL, "non ancora confermate" (`BT-05 @ 01:17:44`).
- `source.value_counts()` a schermo: havana 1.441.093, ensembl_havana 745.065, ensembl 228.212, `.` 182.510, mirbase 4.701, GRCh38 194, insdc 74.
> **Nota aggiunta:** le sequenze KI/GL sono *scaffold* non localizzati o non posizionati: DNA sequenziato che non si sa ancora collocare su un cromosoma (nel file hanno tipo `supercontig`).
Il docente accenna a ricerche su dimensione e dettagli dei geni e a completezza dell'assemblaggio (`BT-05 @ 01:18:22`).
### 11.3 Quanto del genoma è incompleto
`BT-05 @ 01:18:53`
Le informazioni sui cromosomi interi stanno nelle righe con `source == 'GRCh38'`:
```python
gdf = df[df.source == 'GRCh38']
gdf.shape                       # (194, 9)
gdf = gdf.copy()
gdf['length'] = gdf.end - gdf.start + 1
gdf.length.sum()
chrs = [str(_) for _ in range(1, 23)] + ['X', 'Y', 'MT']
gdf[-gdf.seqid.isin(chrs)].length.sum() / gdf.length.sum()
# 0.0037021917421198327
```
Le sequenze non assemblate sono di tipo `supercontig`, le altre `chromosome`. La lunghezza totale è circa 3,1 miliardi di basi e la frazione non assemblata circa **0,37%**. Il `.copy()` evita il `SettingWithCopyWarning` quando si aggiunge la colonna `length`.
Verificato per esecuzione (dalle lunghezze GRCh38 visibili a schermo): la somma dei cromosomi 1-22, X, Y, MT è 3.088.286.401 bp; con la frazione a schermo il totale è circa 3.099.762.315 bp, cioè circa 11,5 milioni di basi su scaffold non assemblati.
> **Nota aggiunta:** `-gdf.seqid.isin(chrs)` nega una Series booleana; la forma idiomatica è `~gdf.seqid.isin(chrs)`.
### 11.4 Tipi di entità e geni
`BT-05 @ 01:19:31`
```python
edf = df[df.source.isin(['ensembl', 'havana', 'ensembl_havana'])]
edf.sample(10)
edf.type.value_counts()
```
A schermo, i tipi più frequenti: exon 1.180.596, CDS 704.604, five_prime_UTR 142.387, three_prime_UTR 133.938, transcript 96.375, **gene 42.470**, processed_transcript 28.228, ... Le strutture più numerose sono gli **esoni**, poi le sequenze codificanti (CDS), i trascritti, i geni, gli pseudogeni (`BT-05 @ 01:19:31`). "Tutto questo senza una profonda conoscenza della biologia" (`BT-05 @ 01:20:11`).
Filtro sui geni ed estrazione di nome, ID e descrizione dalla colonna `attributes` (stringa `chiave=valore;...`) con espressioni regolari (`BT-05 @ 01:20:43`):
```python
ndf = edf[edf.type == 'gene']
ndf = ndf.copy()
ndf.sample(10).attributes.values

RE_GENE_NAME = re.compile(r'Name=(?P<gene_name>.+?);')
def extract_gene_name(attributes_str):
    res = RE_GENE_NAME.search(attributes_str)
    return res.group('gene_name')
ndf['gene_name'] = ndf.attributes.apply(extract_gene_name)

RE_GENE_ID = re.compile(r'gene_id=(?P<gene_id>ENSG.+?);')
def extract_gene_id(attributes_str):
    res = RE_GENE_ID.search(attributes_str)
    return res.group('gene_id')
ndf['gene_id'] = ndf.attributes.apply(extract_gene_id)

RE_DESC = re.compile('description=(?P<desc>.+?);')
def extract_description(attributes_str):
    res = RE_DESC.search(attributes_str)
    if res is None:
        return ''
    else:
        return res.group('desc')
ndf['desc'] = ndf.attributes.apply(extract_description)

ndf.drop('attributes', axis=1, inplace=True)
print(ndf.head())
```
Dal testo del notebook: `+?` è **non avido**, si ferma al primo `;` (con `+` arriverebbe all'ultimo); la regex è compilata una volta con `re.compile` perché si applica a migliaia di stringhe; `apply` applica la funzione a ogni elemento della Series. La regex dell'ID è più specifica: ogni `gene_id` inizia con `ENSG` (ENS = Ensembl, G = gene). Non tutti i geni hanno una descrizione, da qui il ramo `None` (`BT-05 @ 01:21:23`). Verificato per esecuzione su righe sintetiche: con `.+` avido il nome di `DDX11L1` diventerebbe `DDX11L1;biotype=...;description=...`.
A schermo, `head()`: DDX11L1 (ENSG00000223972), WASH7P, OR4G4P, OR4G11P, OR4F5.
**Nomi contro ID** (`BT-05 @ 01:21:59`):
```python
print(ndf.shape)                      # (42470, 11)
print(ndf.gene_id.unique().shape)     # (42470,)
print(ndf.gene_name.unique().shape)   # (42387,)
count_df = ndf.groupby('gene_name').count().iloc[:, 0].sort_values().iloc[::-1]
print(count_df.head(10))
ndf[ndf.gene_name == 'SCARNA20']
```
Ci sono meno nomi che ID: alcuni nomi corrispondono a più ID. Il notebook: un nome può essere condiviso da un massimo di **sette** ID (SCARNA20, presente sui cromosomi 1, 11, 14, 15, 17). Il docente lo spiega come un gene scomposto in più sottostrutture con lo stesso nome e ID diversi (`BT-05 @ 01:22:33`).
> **Nota aggiunta:** nel file ogni `gene_id` è un gene distinto; i nomi ripetuti come SCARNA20 sono copie o paraloghi in posizioni diverse del genoma (qui su cinque cromosomi), non sottostrutture di un unico gene. Le sottostrutture (trascritti, esoni) hanno righe proprie e ID `ENST`, `ENSE`. Il testo del notebook cita `.ix[::-1]`, rimosso da pandas 1.0; il codice usa correttamente `.iloc[::-1]`.
### 11.5 Quanto è lungo un gene
`BT-05 @ 01:23:06`
```python
ndf['length'] = ndf.end - ndf.start + 1
print(ndf.length.describe())
ndf.length.plot(kind='hist', bins=50, logy=True)
ndf[ndf.length > 2e6].sort_values('length').iloc[::-1]
```
A schermo: 42.470 geni, media circa 35.833 basi, mediana 5.170,5, minimo 8, massimo 2.304.997. La media molto più grande della mediana indica una distribuzione **asimmetrica a destra**; l'istogramma (asse y logaritmico) ha quasi tutti i geni nel primo bin. I geni oltre 2 milioni di basi sono CNTNAP2, PTPRD, DMD (distrofina), DLG2 e altri.
### 11.6 Geni per cromosoma
`BT-05 @ 01:23:43`
```python
ndf = ndf[ndf.seqid.isin(chrs)]
chr_gene_counts = ndf.groupby('seqid').count().iloc[:, 0].sort_values().iloc[::-1]
print(chr_gene_counts)

df[(df.type == 'gene') & (df.seqid == 'MT')]

gdf = gdf[gdf.seqid.isin(chrs)]
gdf.drop(['start', 'end', 'score', 'strand', 'phase', 'attributes'], axis=1, inplace=True)
gdf.sort_values('length').iloc[::-1]

cdf = chr_gene_counts.to_frame(name='gene_count').reset_index()
merged = gdf.merge(cdf, on='seqid')
merged[['length', 'gene_count']].corr()
# grafico gene_count contro length, con l'etichetta di ogni cromosoma
```
A schermo: il cromosoma 1 ha più geni, **3902**, poi il 2 con 2806; X ha **1852**, Y **436** (`BT-05 @ 01:23:43`). Nessun gene sul mitocondrio (MT) nel conteggio, "il che non è vero": i geni MT hanno sorgente `insdc` e sono stati esclusi dal filtro su havana/ensembl (`BT-05 @ 01:24:12`); il filtro diretto su `df` li mostra (MT-RNR1, MT-RNR2, MT-ND1, ...). Correlazione di Pearson fra lunghezza del cromosoma e numero di geni: **0,73** (0.728221), positiva ma non per tutti i cromosomi; per alcuni (6, 15, 14, 13) il notebook indica una relazione negativa. Nella versione a schermo `gdf.drop(..., inplace=True)` su un `gdf` filtrato produce un `SettingWithCopyWarning`.
Il docente ricorda che il mitocondrio si usa spesso per analisi filogenetiche, per stabilire la discendenza (`BT-05 @ 01:24:18`).
> **Nota aggiunta:** il DNA mitocondriale si eredita per via materna. Con pandas 3.0 (copy-on-write) il `SettingWithCopyWarning` non compare più: `gdf[...]` è già una copia indipendente (`verifica_bt05.py`).
### 11.7 Conclusioni
`BT-05 @ 01:24:55`
> **Correzione:** a voce "il genoma è stato mappato per circa il suo 37%" (`BT-05 @ 01:24:55`). La conclusione del notebook a schermo è "circa lo **0,37%** del genoma umano è ancora incompleto" (frazione su scaffold non assemblati 0.0037, sezione 11.3): il genoma di riferimento è assemblato per oltre il 99%.
Il file, aggiornato periodicamente, contiene circa **42.000 geni**; un gene può essere scomposto in molte sottostrutture. Un'analisi di questa dimensione non si fa a mano: filtri, query e grafici con pandas sono la base della manipolazione dell'informazione genetica (`BT-05 @ 01:25:28`).
> **Nota aggiunta:** i 42.470 "geni" del file includono pseudogeni e geni di RNA non codificante; i geni codificanti proteine nell'uomo sono circa 20.000.
## 12. Collegamento con il test finale
Il test finale 2026 (vedi **Assessment**) non contiene domande né esercizi di bioinformatica: la teoria riguarda ABMS, ODE ed epidemiologia computazionale, la pratica un modello Mesa preda-predatore o il modello di Gompertz. Il capitolo resta materiale di corso, non d'esame.
## 13. Glossario, punti incerti, materiale usato
### Glossario
- **Nucleotide:** unità del DNA (A, T, C, G; nell'RNA U al posto di T).
- **k-mer:** sottosequenza di lunghezza $`k`$ ottenuta con una finestra che avanza di 1; $`L - k + 1`$ per una sequenza di lunghezza $`L`$.
- **Gene, esone, introne, CDS, UTR:** tratto di DNA che codifica un prodotto; parti del gene mantenute nell'mRNA maturo; parti rimosse; sequenza codificante tradotta in proteina; regioni non tradotte agli estremi.
- **Trascrizione, traduzione:** copia di DNA in RNA; sintesi della proteina dall'mRNA, una tripletta per amminoacido.
- **Allineamento globale e locale:** su tutta la lunghezza delle sequenze (Needleman-Wunsch); sulle sottoregioni più simili (Smith-Waterman, BLAST).
- **Banca dati primaria e secondaria:** raccolta dei dati sperimentali (GenBank, EMBL, DDBJ); raffinamento curato (RefSeq, UniProt).
- **Accession:** codice univoco di un record in banca dati (es. `AF509505.1`).
- **FASTA:** formato testuale con intestazione `>` e sequenza.
- **BLAST:** ricerca per similarità di sequenza; score, query cover, percentuale di identità, E-value.
- **GFF3:** formato tabellare a 9 colonne per le annotazioni genomiche.
- **GRCh38:** versione di riferimento del genoma umano (Genome Reference Consortium, build 38).
### Punti incerti
- Limite di 10.000 nucleotidi per BLAST online (`BT-05 @ 01:10:46`): affermazione del docente non verificata qui \[?\].
- "In passato, dove la melanogaster era un problema di sovrappopolazione, si proponeva la modifica del gene Indy per dimezzarne il ciclo di vita" (`BT-05 @ 00:50:58`): la frase è poco chiara (la mutazione di Indy allunga la vita) \[?\].
- Target dettato a voce (`BT-05 @ 00:09:33`, "a chi ci ha dcg...") illeggibile nell'audio: usato quello scritto a schermo.
- Nomi trascritti male e corretti nel testo: "GinBank/Gimbank" → GenBank; "IMBL" → EMBL; "RefSec/rafstech" → RefSeq; "Unicrot/unibrot" → UniProt; "Spercas9" → Cas9; "straccia redd e query language" → Structured Query Language; "modelli marco piani" → markoviani; "tioredoxina" → tioredossina.
### Materiale usato
- Fotogrammi `BT-05` delle slide (`00:04:10`, `00:09:28`, `00:29:51`, `00:31:41`, `00:38:27`, `00:40:35`, `00:45:12`, `00:47:11`, `00:48:25`, `00:49:44`, `00:50:56`, `00:51:34`, `01:00:35`, `01:03:05`, `01:12:21`), del documento dell'esercizio (`00:10:32`-`00:20:32`), delle pagine NCBI e BLAST (`00:52:12`-`01:10:01`) e del notebook `Genome.ipynb` (`01:13:14`-`01:24:45`)
- Verifica: `verifica_bt05.py` (k-mer, frazione non assemblata, pipeline pandas su GFF3 sintetico; pandas 3.0)
