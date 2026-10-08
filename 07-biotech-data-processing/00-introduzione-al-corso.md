# 00 - Introduzione al corso

> Fonte Notion: https://app.notion.com/p/3e912abc808d816b8cfed4912902297e — ultima modifica 2026-09-28T17:33:06.619Z

**Fonti:** nessuna registrazione sul portale (Day 1 2025 non pubblicato). Il capitolo si basa su:
- `Teams 1` (18/05/2026, 1:16:08): prima lezione dell'edizione 2026, letta dalla trascrizione Stream e **riassunta**, non ricopiata;
- slide `Day1_v25.pdf` (edizione 2025, 7/11/2025, 11 pagine);
- slide `Biotech Data Processing Course Introduction.pdf` (edizione 2026, "MDA 26", 30 pagine).
> Le slide del 2025 e del 2026 sono diverse: quelle del 2025 presentano docente, programma e casi di studio di Biocentis; quelle del 2026 partono da una revisione della letteratura sul biotech data processing e introducono le ODE con quattro casi di studio. Il docente stesso dice che le slide 2026 sono "complementari" a quelle delle lezioni registrate (`Teams 1 @ 0:08:18`).
## Indice
1. Il docente e l'organizzazione del corso
2. Biotech data e modelli
3. La pipeline del biotech data processing
4. Revisione della letteratura: tendenze e competenze
5. Programma del corso
6. Introduzione alle ODE e ai metodi numerici (edizione 2026)
7. I quattro casi di studio (edizione 2026)
8. Casi di studio Biocentis (edizione 2025)
9. Esame
10. Glossario e materiale usato
---
## 1. Il docente e l'organizzazione del corso
`Teams 1 @ 0:03:30`
**Matteo Rucco** si occupa di analisi dei dati da alcune decine di anni. Nel 2026 ha tre ruoli: responsabile del gruppo di data science di **Biocentis**, startup biotech che sviluppa tecnologie di gene editing (CRISPR-Cas9) per il controllo di popolazioni di insetti nocivi, come alternativa ai pesticidi chimici; responsabile scientifico di Spindox Labs, gruppo R&D della società italiana Spindox; lecturer al dipartimento di matematica dell'Università di Siviglia, dove sviluppa metodi di analisi dei dati basati sulla **topologia**, poi applicati per esempio alla clinica di precisione. Tiene questo corso a Roma Tre da quattro o cinque anni.
Slide 2025: "Biotech data processing, Master Data Analytics, Matteo Rucco – [matteo.rucco@Biocentis.com](mailto:matteo.rucco@Biocentis.com)".
Organizzazione 2026 (`Teams 1 @ 0:06:04`, `0:07:38`):
- il corso è erogato insieme ai due livelli del master, e il docente cerca di calibrarlo per entrambi;
- sei incontri; i video delle lezioni degli anni precedenti sono disponibili sulla piattaforma di e-learning, e negli incontri successivi il docente riprende parte di quel materiale per approfondirlo con la parte pratica;
- a differenza degli anni precedenti, già la prima lezione ha una parte pratica: esercizi soprattutto di programmazione Python, a volte di revisione della letteratura;
- tutte le esercitazioni sono su **Google Colab**, che permette di eseguire Python senza installare un ambiente di sviluppo;
- il docente annuncia un ospite esperto per l'incontro del venerdì (`Teams 1 @ 1:07:17`).
## 2. Biotech data e modelli
`Teams 1 @ 0:07:46`
Slide 2025 "Biotech data – definition & applications": "Any technological application that uses biological systems, living organisms, or derivatives thereof, to make or modify products or processes for specific use." Sotto, l'infografica "Types of biotechnology" con i colori delle biotecnologie: Red (medical and pharmaceutical), White or gray (industrial), Green (agricultural), Gold (bioinformatics and data), Blue (marine and aquatic environments), Yellow (food production), Violet (governance of ethical considerations), Dark (warfare).
Per il docente "biotech" indica l'insieme delle tecnologie, soprattutto digitali, che circondano il mondo biologico e ne generano dati: non solo biologia umana ma anche veterinaria e vegetale, cioè tutto ciò che è vivente e osservabile con sensori fisici o virtuali. Il corso mette l'accento sul **dato**; i concetti di biologia servono solo a interpretarlo.
Perché interessa (`Teams 1 @ 0:09:30`): medicina di precisione, biologia avanzata, farmacogenetica, agricoltura di precisione; l'interesse per nuovi farmaci e per un'agricoltura più robusta, anche contro insetti che il riscaldamento globale porta a latitudini nuove; e, in parallelo, tecnologie come imaging e sequenziamento che generano dati a velocità crescente. Generare dati però non basta: vanno analizzati, compresi, visualizzati e **modellati**.
Il **modello** (`Teams 1 @ 0:11:32`): il docente parte dalla definizione che attribuisce ad Aristotele, un modello è una qualsiasi descrizione qualitativa o quantitativa di un fenomeno. Una descrizione in linguaggio naturale ("oggi ci siamo incontrati per parlare di biotech data processing") è già un modello qualitativo; aggiungere quantità misurabili ("eravamo in nove") lo rende più oggettivo e difficile da confutare. Il tema principale del corso è **costruire modelli** attorno ai dati biotech, con approcci canonici e altri più recenti presi da matematica, informatica e fisica.
Slide 2025 "How Data Science is Impacting Biotechnology": "While data science continues down its own evolutionary path, the science of data doesn't stray from the fundamentals of: Generating a question (or series of questions); Collecting data; Prepping data; Choosing a relevant model; Testing the model; Fine-tuning the model; Launching the model into a larger production environment; Continuously monitoring and optimizing the model."
Slide 2025 "Biotech data processing as part of Science": "Agriculture, medicine, biology, and biotechnology represent fundamental industrial assets where data is crucial, and they all use multiple data analytics methods to extract insights. The program will train on using cutting-edge technologies to analyze several use cases from these disciplines, ranging from tumor detection in medical images, analysis of clinical tabular data, automatic sex identification of mosquitoes, and application of natural language understanding to the analysis of genomics data. Each lesson will introduce a new challenge and hands-on activity to solve it. The program will use Python and Google Colab."
## 3. La pipeline del biotech data processing
`Teams 1 @ 0:13:33`
Slide 2026 (infografica "Biotech Data Processing: dal dato grezzo alla conoscenza biologica"). Il biotech data processing non è un tool né una tecnica, ma una **sequenza di metodi** da calare nel contesto applicativo. L'immagine è costruita sull'analisi di sequenze genomiche, ma i passi valgono in generale:
1. **Acquisizione dei dati**, a scale, risoluzioni e con strumenti diversi: genomica (NGS, microarray), trascrittomica (RNA-seq, conteggi di espressione genica), proteomica (spettrometria di massa), metabolomica (LC-MS, NMR), dati fenotipici e clinici (spesso tabellari), altri dati (immagini: risonanza magnetica, tomografia, microscopia digitale; sensori).
2. **Pre-elaborazione e pulizia**: controllo di qualità, quantificazione dei bias (anche errori strumentali), filtraggio degli outlier, normalizzazione (utile sia per i test statistici sia per il machine learning, che lavorano meglio con distribuzioni note), gestione dei dati mancanti, correzione degli effetti batch.
3. **Analisi esplorativa**: statistiche descrittive (momenti di basso ordine: media, mediana, deviazione standard), PCA per ridurre dati ad alta dimensionalità e far emergere cluster o separazioni negli scatter plot, heatmap di distribuzioni e correlazioni.
4. **Modellazione**: ODE per come una quantità varia nel tempo, modelli ad agenti (ABMS) quando si conoscono le regole di comportamento, **Topological Data Analysis** per studiare il dato da un punto di vista geometrico. Un modello permette di simulare il fenomeno e di cambiare le condizioni iniziali rispetto all'esperimento reale.
5. **Analisi avanzata**: analisi differenziale (volcano plot dei geni sovra e sotto espressi), arricchimento funzionale e pathway analysis, machine learning.
6. **Integrazione e interpretazione**: integrazione multi-omica, reti biologiche, contestualizzazione con la letteratura e le basi di conoscenza per confermare o arricchire le ipotesi.
7. **Decisioni e applicazioni**: biomarcatori, sviluppo di farmaci, medicina personalizzata, ottimizzazione di bioprocessi.
Il docente segnala un refuso nella slide: il passo 5 compare due volte, il secondo è il 6 (`Teams 1 @ 0:20:36`).
Tecnologie e strumenti: database e storage (relazionali e non), linguaggi (Python, R), librerie generiche (pandas, NumPy, scikit-learn) e di dominio (Bioconductor), calcolo ad alte prestazioni (HPC: in Italia il CINECA; oppure cloud come AWS), visualizzazione (Matplotlib, Seaborn, Plotly, Cytoscape). Oltre ai dati vanno gestiti i **metadati**: con quale strumento, quando e perché è stato generato un dato, così da ricostruirne la catena di elaborazione.
Il corso si concentra sul **passo 4, la modellazione** (`Teams 1 @ 0:23:03`); la slide successiva evidenzia proprio quella colonna.
> **Correzione:** a `Teams 1 @ 0:14:47` il docente descrive la spettrometria di massa come "analisi nel campo della luce infrarossa". La spettrometria di massa separa gli ioni in base al rapporto massa/carica; l'analisi nell'infrarosso è la spettroscopia IR (o NIR), una tecnica diversa.
## 4. Revisione della letteratura: tendenze e competenze
`Teams 1 @ 0:23:14`
Per capire quanto le tecniche del corso siano attuali, il docente ha fatto una revisione della letteratura. Slide "Computational Approaches & Best Practices in Biotechnology Data Processing. A Comprehensive Review for Junior and Senior Scientists": fonte Google Scholar, 20 paper, periodo 2010-2025, pubblico junior e senior scientist. La risposta anticipata: le tecniche del corso sono ancora oggetto di ricerca, sia di base sia di maturazione.
Contenuti delle slide, con il commento del docente:
- **The Data Revolution in Biotechnology**: la biologia è diventata una scienza data-intensive (sequenziamento high-throughput, CRISPR, imaging); le scienze omiche cambiano i flussi di lavoro; i junior devono costruire competenze computazionali, i senior guidare progetti data-intensive. Il docente aggiunge l'esempio dei **data stream**: pazienti epilettici monitorati 24 ore su 24, con analisi in tempo reale, accurata e personalizzata (`Teams 1 @ 0:25:33`).
- **Key Computational Tools**: ambienti di dati integrati (gestione del dato con analisi no-code o low-code, così che il biologo interroghi e analizzi senza scrivere codice), PhyloSuite (piattaforma desktop per sequenze molecolari e analisi filogenetica), machine learning e AI (per esempio transformer per predire strutture di proteine e nuovi farmaci; il docente cita la startup Oxford Drug Discovery), ERP con analytics AI.
- **FAIR Data Management**: Findable, Accessible, Interoperable, Reusable. Il docente lo spiega come poter trovare il dato, mantenerlo accessibile nel tempo con la sua storia, portarlo tra piattaforme e sistemi, riusarlo per studi diversi; i lavori citati (Rehnert, Griffin) mostrano più di 20 casi dal 2017.
- **Adoption of Key Data Practices** (stime dalla letteratura 2017-2025): FAIR 72%, integrazione del machine learning 65%, quaderni di laboratorio elettronici 58%, formazione su Jupyter/notebook 49%, protocolli di cyberbiosecurity 41%. Sui quaderni: nei *wet lab* si usano ancora quaderni di carta, in controtendenza rispetto a FAIR. Sulla **cyberbiosecurity** (`Teams 1 @ 0:34:39`): una sequenza genetica digitale che rappresenta un virus, se arriva a strutture che non rispettano l'etica, può diventare pericolosa; i laboratori devono proteggere anche il "gemello digitale" del materiale organico. Il docente cita le ipotesi sull'origine del Covid da laboratorio e dice che l'evidenza più supportata è una ricombinazione avvenuta nel mondo animale e poi passata all'uomo.
- **Training the Next Generation**: per i junior, notebook Jupyter con simulatori di organismi virtuali, corsi a distanza, integrazione graduale dei metodi computazionali, deep learning per microscopia e imaging; per i senior, guidare con l'esempio sugli standard FAIR, fare mentoring su flussi collaborativi, bilanciare esternalizzazione e competenze interne, allinearsi ai requisiti industriali.
- **Across Domains**: genomica e omiche, microscopia e imaging, agricoltura e filiera alimentare.
- **Best Practices**: applicare FAIR fin dall'inizio; adottare piattaforme integrate; usare ML spiegabile per sistemi biologici complessi; investire in formazione; proteggere i dati (cyberbiosecurity, condivisione sicura).
- **Future Directions**: automazione e integrazione dell'AI negli esperimenti di laboratorio; trasformazione digitale (dal quaderno di carta agli strumenti digitali); big data analytics e integrazione con gli ERP; open innovation fra industria e accademia, che "spesso ancora non si parlano".
- **Conclusion**: "The biology-data science convergence is irreversible — mastering data processing skills is essential for transformative scientific impact across genomics, medicine, and beyond."
Riferimenti delle slide: Bhambri et al. 2025; Braet et al. 2024; Chinthamu 2023; Cizauskas et al. 2025; Duncan et al. 2020; Griffin et al. 2017; Lavrynenko et al. 2018; Liebal et al. 2021; Moreddu 2025; Rehnert et al. 2022; Stevens 2011; Zhang et al. 2018 (DOI nelle slide).
## 5. Programma del corso
Slide 2025 "Course contents presentation":
- Day 2: Mathematics in Bio(techno)logy
- Day 3: Agent-based modeling (ABMS)
- Day 4: DIY on Modeling
- Day 5: A comprehensive introduction to your genome
- Day 6: Epidemiology and compartmental model
- Day 8: DIY: combine what we have learned and bonus time for final assessment
"All the lectures are completed with hands-on activities in Google Colab: do you know it?"
> Le lezioni 2025 effettivamente registrate seguono un ordine diverso: Day 4 TDA, Day 5 epidemiologia, Day 6 bioinformatica, Day 7 algoritmi genetici (vedi hub e Divergenze).
Slide 2026 "Course Content Overview":
1. Foundations of Biological Data: tipi e fonti di dati (sequenziamento, imaging, sensori); pre-elaborazione e controllo di qualità.
2. Mathematical and Computational Tools: equazioni differenziali (ODE, PDE); modelli compartimentali (SIR, Lotka-Volterra); modelli ad agenti e di rete.
3. Complex Systems and Data Analysis: Topological Data Analysis.
4. Applications and Case Studies: epidemie e dinamiche di infezione; formazione di pattern e attività neurale; regolazione metabolica e modelli immunitari.
5. Practical Components: Python (Eulero, ODEINT, SALib); strumenti e piattaforme di bioinformatica; simulazione, visualizzazione e analisi dei parametri.
Il docente dice che il corso si concentrerà sulle sezioni 2 e 3, con ogni teoria mostrata su casi di studio concreti, semplificati ma rappresentativi, a volte scrivendo i tool da zero e a volte con librerie di terze parti (`Teams 1 @ 0:43:30`).
Learning Outcomes (slide 2026): comprendere i concetti chiave dei dati biotecnologici e le relative sfide; acquisire competenze pratiche nell'elaborazione e nell'analisi di set di dati biologici; applicare metodi computazionali per risolvere problemi biotecnologici.
## 6. Introduzione alle ODE e ai metodi numerici (edizione 2026)
`Teams 1 @ 0:45:13`
Il docente chiede alla classe cos'è un'equazione differenziale; la risposta di uno studente, che il docente conferma: un'equazione la cui incognita è una funzione, per esempio del tempo, di solito accompagnata da un **dato iniziale** necessario a risolverla. Le ODE servono a studiare la variazione di una quantità nel tempo (per esempio la concentrazione di cellule); in fisica, a studiare i **sistemi dinamici**, cioè sistemi tempo-dipendenti. Il corso non è di matematica: si concentra su come risolverle **numericamente** al computer, non analiticamente.
Slide "Perché le ODE nel biotech?": le ODE descrivono sistemi dinamici: crescita cellulare, farmacocinetica, fermentazioni, produzione proteica. L'infografica ruota attorno alla forma generale
$$
\frac{dy}{dt} = f(y, t, \theta)
$$
(tasso di variazione, variabile biologica, tempo, parametri biologici) con cinque esempi:
- **crescita della popolazione**: $`dN/dt = rN`$ ($`N`$ numero di individui, $`r`$ tasso di crescita); batteri, colture cellulari, popolazioni animali;
- **farmacocinetica**: $`dC/dt = -kC`$ ($`C`$ concentrazione del farmaco nel sangue, $`k`$ costante di eliminazione); il docente sottolinea che rispetto alla crescita cambia solo il segno;
- **cinetica enzimatica** (E + S ⇄ ES → E + P): $`dS/dt = -k_1 ES + k_{-1}C`$, $`dE/dt = -k_1 ES + (k_{-1}+k_2)C`$, $`dP/dt = k_2 C`$; un sistema accoppiato che descrive la velocità delle reazioni biochimiche;
- **epidemiologia (SIR)**: $`dS/dt = -\beta SI`$, $`dI/dt = \beta SI - \gamma I`$, $`dR/dt = \gamma I`$;
- **bioreattore (coltura batch)**: $`dX/dt = \mu X`$, $`dS/dt = -\frac{1}{Y_{X/S}}\mu X`$ ($`X`$ biomassa, $`S`$ substrato, $`\mu`$ velocità specifica di crescita, $`Y_{X/S}`$ resa biomassa/substrato).
Perché sono importanti: comprendono dinamiche complesse, aiutano a interpretare gli esperimenti (al variare di condizioni iniziali e costanti), permettono simulazioni e previsioni, supportano decisioni in ricerca e biotecnologia; "trasformano i meccanismi biologici in modelli matematici che possiamo analizzare e comprendere".
Slide "Metodi Numerici per ODE nel Biotech" `Teams 1 @ 0:54:27`: il percorso è **modello → discretizzazione → algoritmo → soluzione** (approssimata, con analisi dell'errore). Il problema continuo $`dy/dt = f(t,y)`$, $`y(t_0) = y_0`$ diventa un problema discreto valutato in istanti $`t_0, t_1, \dots, t_n`$, a passo regolare o adattivo. Fonti di errore: troncamento (dovuto all'algoritmo), arrotondamento (precisione finita), propagazione dell'errore. Esempi di metodi:
- **Eulero esplicito**, "semplice e intuitivo": $`y_{n+1} = y_n + h\,f(t_n, y_n)`$;
- **Runge-Kutta**, "più accurati", in particolare RK4;
- **metodi a più passi**, che usano più punti precedenti (es. Adams-Bashforth);
- **metodi impliciti**, "maggior stabilità per problemi stiff", per esempio Eulero implicito $`y_{n+1} = y_n + h\,f(t_{n+1}, y_{n+1})`$.
> **Correzione:** a voce (`Teams 1 @ 0:56:38`) il docente attribuisce ai metodi a più passi "step adattativi in base alla pendenza" e dice che i metodi impliciti sono utili "dove ci sono diversi minimi e massimi locali". Un metodo multistep come Adams-Bashforth riusa i valori dei passi precedenti e di base lavora a passo fisso; i metodi impliciti servono per i **problemi stiff** (componenti con scale temporali molto diverse), come dice la slide stessa.
I metodi numerici servono perché le ODE complesse raramente hanno soluzione analitica; rendono possibili "gemelli digitali" del fenomeno in cui variare i parametri costa meno che ripetere l'esperimento in laboratorio, e permettono l'**analisi di sensibilità**: interrogare il modello con parametrizzazioni diverse per trovare gli intervalli in cui i parametri non cambiano molto l'output, e suggerire al biologo dove fare i prossimi esperimenti (`Teams 1 @ 0:58:12`).
Slide "Metodo di Eulero": metodo numerico esplicito; usa la derivata locale per stimare il punto successivo; semplice da implementare; buono per introdurre le ODE. Il docente: "un algoritmo di quattro righe", strumento didattico, dettagli alla lezione successiva.
Slide "Introduzione a odeint": solver avanzato di SciPy; passo adattativo; alta stabilità numerica; usato in simulazioni scientifiche reali. Il docente aggiunge che per ODE molto semplici Eulero è più economico computazionalmente di `odeint` (`Teams 1 @ 1:00:17`).
Slide "Concetti Chiave": le ODE modellano sistemi biologici; Eulero è semplice ma limitato; odeint è più accurato; le simulazioni aiutano il design biotech. Il docente aggiunge che Eulero non è affidabile su sistemi complessi (`Teams 1 @ 1:05:42`). "Conclusioni": dalle basi ai sistemi complessi; approccio progressivo; comprensione numerica e biologica; base per simulazioni avanzate.
## 7. I quattro casi di studio (edizione 2026)
`Teams 1 @ 1:00:46`
Quattro esempi-giocattolo per introdurre le ODE, ciascuno con un notebook Colab (codice e confronto numerico nel capitolo 01, sezione "Casi di studio 2026"):
1. **Crescita batterica**: i batteri si riproducono per scissione binaria (una cellula madre duplica il DNA e si divide in due cellule figlie identiche); modello esponenziale $`dN/dt = rN`$, implementato con Eulero, studio del tasso di crescita al variare di condizione iniziale e $`r`$. Notebook `01_eulero_crescita_batterica.ipynb`, che aggiunge la logistica.
2. **Bioreattore batch** (o "reattore a cotta"): sistema chiuso in cui tutti i componenti (nutrienti, terreno di coltura, microrganismi) sono caricati all'inizio e non si aggiunge né rimuove materiale, salvo gas e correttori di pH; biomassa e substrato, confronto Eulero vs odeint, consumo del nutriente, stabilità numerica. Notebook `02_eulero_vs_odeint_bioreattore_batch.ipynb`.
3. **Farmacocinetica**: la branca della farmacologia che studia "cosa l'organismo fa al farmaco", nelle quattro fasi ADME (assorbimento, distribuzione, metabolismo, eliminazione); eliminazione $`dC/dt = -kC`$, curve dose-risposta. Notebook `03_odeint_farmacodinamica_biotech.ipynb`.
4. **Fed-batch**: coltivazione in cui i nutrienti si aggiungono gradualmente durante il processo, invece che tutti all'inizio (batch) o in continuo (coltura continua); sistema multi-variabile, produzione di proteina ricombinante, bilanci di massa, simulazione industriale. Notebook `04_odeint_fed_batch_proteina_ricombinante.ipynb`.
A fine lezione il docente apre il primo notebook in Colab (`Teams 1 @ 1:12:17`): import di NumPy, Matplotlib e `odeint`, la funzione di Eulero esplicito ("la parte funzionale si risolve in un loop for"), i parametri della crescita esponenziale (cellule per mL iniziali, tasso $`r`$, 8 ore di osservazione a passi di 0.25 ore). Il resto è alla lezione successiva.
## 8. Casi di studio Biocentis (edizione 2025)
Solo slide, nessun commento a voce disponibile.
Slide "BIOCENTIS" e slide con il logo dell'Azienda Ospedaliero Universitaria Ospedali Riuniti di Ancona e l'infografica "Data Science in Healthcare" (Genetics & Genomics, Data Management, Drug Discovery, Virtual Assistance, Predictive Analysis, Image Analysis; evidenziate le ultime due).
Slide "Glioblastoma": "Glioblastoma multiforme (GBM) is a fast-growing and highly invasive brain tumor that tends to occur in adults between the ages of 45 and 70 and accounts for 52 percent of all primary brain tumors. Usually, GBMs are detected by magnetic resonance images (MRI). Among MRI, a fluid-attenuated inversion recovery (FLAIR) sequence produces high-quality digital tumor representation. Need for a personalized diagnosis." A destra, una serie di sezioni assiali di risonanza magnetica.
Slide "Towards personalized medicine":
- "Topological Data Analysis of a simplified 2D tumor Growth Mathematical Model: Identification how tumor growth over time is affected by the initial amount of available chemical nutrient." Grafici: distribuzione radiale delle cellule (proliferative, quiescenti, necrotiche) per alpha = 0.0, 0.5, 1.0, e curve di entropia persistente (PE H0, PE H1) e GE per le tre popolazioni.
- "Topological Data Analysis of Glioblastoma temporal progression on FLAIR: Evaluation of GBM temporal evolution after treatment."
- "Textural and topological data analysis for imaging: Automatic GBM classification on FLAIR." Schema: immagine FLAIR con il tumore segmentato, patch, diagrammi di persistenza H0 e H1, feature topologiche e testurali in tabella.
> Questi casi anticipano la TDA e l'entropia persistente del capitolo 03.
## 9. Esame
`Teams 1 @ 1:09:01`
A una domanda sull'organizzazione (il modulo fa parte di "Intelligenza Artificiale III"), il docente risponde: una traccia con **4-5 domande a risposta aperta** sui concetti teorici delle lezioni più **un esercizio Python**, somministrata l'ultimo giorno di lezione, da analizzare insieme; si può lavorare anche offline, con un intervallo di consegna da definire. Non c'è obbligo di presenza, e chi non può seguire una lezione ha comunque il tempo per lavorarci. Dettagli in **Assessment**.
## 10. Glossario e materiale usato
### Glossario
- **Modello:** descrizione qualitativa o quantitativa di un fenomeno.
- **FAIR:** Findable, Accessible, Interoperable, Reusable, principi di gestione dei dati di ricerca.
- **Metadato:** dato sul dato (strumento, data, scopo della generazione).
- **Wet lab:** laboratorio sperimentale "umido", contrapposto al lavoro computazionale.
- **Cyberbiosecurity:** protezione dei dati biologici digitali (sequenze, progetti di farmaci) dal loro uso improprio.
- **Sistema dinamico:** sistema che evolve nel tempo.
- **Problema stiff:** sistema con componenti che evolvono su scale temporali molto diverse, che richiede metodi impliciti o passi molto piccoli.
- **Batch, fed-batch, coltura continua:** nutrienti caricati tutti all'inizio, aggiunti gradualmente, aggiunti di continuo.
- **ADME:** assorbimento, distribuzione, metabolismo, eliminazione di un farmaco.
### Punti incerti
- Nomi propri dalla trascrizione Stream corretti nel testo: "Bio scientis" → Biocentis, "Spintox Laps" → Spindox Labs, "baycon Doctor" → Bioconductor, "filo suite" → PhyloSuite.
### Materiale usato
- `Materiale/Portale/Day1_v25.pdf`
- `Materiale/Teams/I lezione/Biotech Data Processing Course Introduction.pdf`
- Registrazione `Teams 1` (18/05/2026), trascrizione Stream
