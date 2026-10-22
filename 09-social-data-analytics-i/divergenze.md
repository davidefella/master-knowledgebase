# Divergenze

Correzioni, note aggiunte, confronti fra slide, parlato e notebook, e codice eseguito, capitolo per capitolo. Ogni sezione riproduce il file `out/lezione-0N/lezione-0N-divergenze.md` del Mac.

## Indice
- [01 - Introduzione](#01---introduzione)
- [02 - Attività degli utenti](#02---attività-degli-utenti)
- [03 - Reti sociali](#03---reti-sociali)
- [04 - Natural Language Processing](#04---natural-language-processing)
- [05 - Text similarity e topic modeling](#05---text-similarity-e-topic-modeling)
- [06 - Sentiment analysis](#06---sentiment-analysis)

## 01 - Introduzione

Capitolo: [01-introduzione-social-data-analytics.md](01-introduzione-social-data-analytics.md)

### Fonti e mappatura

| Fonte | Uso |
|---|---|
| SD-01 (portale, preregistrata, 1:14:15) | fonte di verità |
| `0_General_Info_SDA25.pdf`, `1_Introduction_SDA25.pdf` | slide mostrate nel video |
| `0_General_Info_SDA26.pdf`, `1_Introduction_SDA26.pdf` (Teams) | confronto: `1_Introduction` differisce solo per due refusi corretti ("belongs" → "belong", "a format is more convenient" → "a format more convenient"); `0_General_Info` cambia programma, CFU, aggiunge il disclaimer sull'ordine dei video e sostituisce "Exam" con "Assignment" |
| Teams 1 (01/10/2026) | **non usabile**: trascrizione Teams generata in inglese su parlato italiano |
| Teams 4 (06/10/2026) | unica trascrizione 2026 leggibile; usata per programma I livello e assignment |

### Slide contro parlato

| Punto | Slide | Video | Scelta |
|---|---|---|---|
| Ordine degli argomenti | Social media prima di data analytics, coerente con lo schema ad albero | stesso ordine; Mele dice di aver invertito l'ordine rispetto al libro, non alle slide | ordine delle slide |
| Capitoli di Liu | 1-5 (`0_General_Info`) | SD-01 cita 1-2, 3, 4 e il livello di aspetto senza numero; SD-08 @ 01:21:06 "primi quattro capitoli" | riportati entrambi, nota nel capitolo |
| Programma | SDA25: elenco senza numeri di lezione; SDA26: lezioni 1-8 + DL solo II livello | descritto a voce senza numeri | tabella con la numerazione SDA26 |

### Correzioni e note aggiunte

1. **Nomi degli altri docenti** (SD-01 @ 00:12:04): "Maielli", "Maieli", "Enrico" sono trascrizioni non verificate: marcati [?].
2. **Primo autore del libro** (SD-01 @ 00:03:57): "Zabbo" → Gabor Szabo.
3. **API di X e Facebook** (SD-01 @ 00:15:16): la lezione presenta le restrizioni come limiti di quantità "in passato". Nota aggiunta con la situazione 2026 di X (lettura a pagamento dal 2023, pay-per-use dal 2026; fonte secondaria con interesse commerciale) e di Facebook dopo il 2018 (non ricontrollata). Non è una correzione del docente: la lezione è del 2025 e il tema non è centrale.
4. **Twitter 140 caratteri** (SD-01 @ 00:37:28): corretto per il Twitter delle origini; nota aggiunta sul passaggio a 280 nel 2017.
5. **Citazione "Data is like garbage"** attribuita a Mark Twain in slide: attribuzione non documentata, nota aggiunta senza fonte primaria. Non marcata come Correzione perché non verificata.
6. **MapReduce** (SD-01 @ 00:30:47): descrizione semplificata (manca la fase di shuffle). Nota aggiunta con esempio word count, eseguito: `{'social': 2, 'data': 3, 'analytics': 2, 'applied': 1, 'to': 1, 'media': 1}`.
7. **Bilanciamento delle classi** (SD-01 @ 01:10:36): esempio quantificato in nota aggiunta, eseguito: accuracy 0.95, recall negativa 0.0.
8. **CPM/CPC/CPA**: terminologia aggiunta, non usata a lezione.

Nessuna **Correzione** in senso stretto: la lezione è introduttiva e non contiene errori tecnici certi.

### Codice

Nessun codice a lezione. I due blocchi del capitolo sono note aggiunte, verificati per esecuzione (Python 3).

---

## 02 - Attività degli utenti

Capitolo: [02-attivita-degli-utenti.md](02-attivita-degli-utenti.md)

### Fonti e mappatura

| Fonte | Uso |
|---|---|
| SD-02 (portale, preregistrata, 1:05:08) | fonte di verità |
| `2_User_Activity_SDA25.pdf` (41 pagine) | slide mostrate nel video; tutte le pagine renderizzate a 80 dpi e guardate, la 16 anche a 200 dpi per leggere gli assi del grafico delle canzoni |
| `2_User_Activity_SDA26.pdf` (42 pagine, Teams) | confronto testuale con `pdftotext -layout`: vedi sotto |
| Libro [1], capitolo 1 (pp. 1-40) | solo verifica di grafici e numeri; tutto ciò che viene da qui e non dalla lezione è marcato "Nota aggiunta" |
| Teams 2026 | non usate (perimetro del brief) |
| Notebook | nessuno per questa lezione |
| Frame | controllati `frame_00-55-39.jpg` e `frame_01-01-37.jpg` (in corrispondenza dei vuoti di trascrizione): identici alle slide SDA25 |

Mappatura sezioni del capitolo → slide SDA25 → timestamp:

| Sez. | Slide | Inizio |
|---|---|---|
| 1 | 2-3 | 00:01:52 |
| 2 | 4 | 00:05:57 |
| 3 | 5 | 00:09:46 |
| 4 | 6-8 | 00:14:27 |
| 5 | 9-10 | 00:19:23 |
| 6 | 11-12 | 00:22:45 |
| 7 | 13-16 | 00:24:26 |
| 8 | 17-25 | 00:31:13 |
| 9 | 26-30 | 00:42:21 |
| 10 | 31-33 | 00:49:28 |
| 11 | 34-35 | 00:52:20 |
| 12 | 36-40 | 00:56:12 |
| 13 | 41-42 (Sum Up, Homework) | 01:01:58 |

#### SDA25 contro SDA26

| Differenza | Dettaglio | Trattamento |
|---|---|---|
| Pagina nuova *Wikipedia "bots"* (SDA26 p. 11) | tipi di bot (editing / non-editing), Toolforge, Bot Approvals Group, divieto di riscrittura con LLM | riquadro "Slide SDA26, non mostrata nel video" in sez. 4; contiene un refuso, "Administrative and tagging tog" per "bots" |
| Refusi corretti | "not human but bots" → "not humans, they are bots"; "two time different periods" → "two different periods"; punto finale della definizione di CCDF | nessuno |

### Slide contro parlato

| Punto | Slide / libro | Video | Scelta |
|---|---|---|---|
| Edit dei bot in un mese | slide 8 "~1K"; slide 14 tabella 80.003 / 79.357 / 63.136; libro "tens of thousands" | "circa 1000" (00:16:14) | **Correzione** (sez. 4) |
| Relazione lineare della power law | fra ln U(r) e ln r | "fra il numero di utenti e il numero di modifiche" (00:24:26) | **Correzione** (sez. 6) |
| Estremo della somma nella PDF | ∞ | "per i da 1 a 1000" (00:32:14) | **Correzione** (sez. 8) |
| CDF a ρ = 100 | grafico ≈ 0,97; slide 35 "<5% sopra 100"; slide 33 "≈100%" | "99,9%" (00:51:07) | **Correzione** (sez. 10) |
| Ordinamento del ranking | slide "by their increasing activities" ma più attivi all'inizio; libro: rank 1 = più attivo | "attività crescenti", poi "posizione 0, rank 0" (00:24:26-00:25:33) | nota aggiunta: ordine decrescente, rank da 1 |
| Fanning out | slide: "showing most active users (e.g., bots)"; libro: effetto della varianza con pochi utenti per bucket | "gli utenti più attivi come i bot hanno questa caratteristica" (00:21:19) | riportata la lezione, nota aggiunta con la spiegazione del libro |
| Grafico "Normalized functions (from 1 to 3 months)" | asse y "Number of users in period", valori assoluti fino a ~110.000 | descritto come "istogrammi normalizzati" (00:32:50) | nota aggiunta: è la versione non normalizzata (Fig. 1.3 del libro) |
| r̄₂ e modifiche "di meno" | slide 30: "never fewer than the edits of Jan" | "potrebbero averne fatte di meno" (00:47:04) | nota aggiunta |
| Costante del modello | slide R12; libro R21 = 1,75 | "R1-2" | usata R12 come la slide, nota con R21 del libro |
| "Burst activity" | slide: titolo della sezione con la formula di r̄₂(r₁); libro: burst = eccezione al tasso costante, rimando al cap. 4 | come la slide | riportata la lezione, nota aggiunta |
| Finestre di X | "3 weeks (Aug. 1 to 28)"; legenda 8/1-8/28; libro "three-week" ma codice a 28 giorni | "tre settimane dal 1 al 28 agosto" | Punto incerto, non Correzione: 28 giorni sono 4 settimane e le pendenze della slide 40 (≈2 e ≈4) sono coerenti con 4 |
| Asse y del grafico di X | "Number of users in period", valori < 1 | "il numero di utenti" | nota aggiunta: è una PDF normalizzata |
| X "non segue una power law" | slide: relazione non lineare in log-log, PDF non sovrapposte in alto | "la decrescita non la vediamo, è abbastanza piatta" (01:00:15) | riportata la sostanza della slide (curve concave), citata la frase |
| Mesi | gennaio-marzo | "gennaio, febbraio e maggio" (00:39:26) | lapsus corretto in silenzio, segnalato nei Punti incerti |
| Canzoni Rhapsody | asse x spezzato; 25.000 = confine fra canzoni anche su Wal-Mart e solo su Rhapsody; asse y fino a 180.000 | "poche canzoni, circa 25.000, hanno moltissimi download, fino a 180.000" | riportata la lezione con la descrizione del grafico |
| PDF a r = 1 vs CDF a ρ = 1 | ≈ 0,35 vs 0,40 nei due grafici del libro | non discusso | nota aggiunta (incongruenza minore del materiale) |

### Correzioni (`> **Correzione:**`)

1. **SD-02 @ 00:16:14, sez. 4.** Bot "circa 1000" edit al mese: i primi tre ne fanno 63-80 mila (tabella slide 14, libro p. 27).
2. **SD-02 @ 00:24:26, sez. 6.** Linearità fra i logaritmi, non fra U e r.
3. **SD-02 @ 00:32:14, sez. 8.** Somma della PDF fino a ∞, non a 1000 (escluderebbe i bot).
4. **SD-02 @ 00:51:07, sez. 10.** CDF a 100 ≈ 0,95-0,97, non 99,9%.

### Note aggiunte

| Sez. | Contenuto | Fonte |
|---|---|---|
| 2 | motivo per intervalli brevi e continui | libro p. 2 |
| 3 | date acquisizione Twitter (ott. 2022) e rebranding X (lug. 2023) | WebSearch 22/10/2026: Wikipedia *Twitter under Elon Musk*, Daily Illini 24/07/2023 |
| 4 | SAX contro DOM, dimensione del dump, Listing 1.1 | libro pp. 3-5 |
| 5 | rette parallele = rapporto costante; fanning out come effetto di varianza; binning logaritmico | libro pp. 18-19 |
| 6 | scale invariance U(cr) = cᵞU(r) | derivazione propria |
| 6 | fit log-log in Python (OLS testa, OLS tutto, binning log) | codice proprio, eseguito |
| 6 | MLE di Clauset-Shalizi-Newman (2009) e pacchetto `powerlaw` | **non verificato** in sessione, citato come riferimento |
| 6 | γ = −1,87 da U₁, U₂, R21 | libro p. 20, ricalcolato |
| 7 | curva cumulativa del ranking; top 10 = 12%, top 100 = 29%; 0,07% degli utenti | libro p. 26 |
| 7 | secondi fra edit dei bot ricavati; dati senza bot (6% e 18%) | libro pp. 27-28, ricalcolato |
| 7 | regola p/q | libro p. 28 |
| 8 | PMF vs PDF; errore 6-8%; refuso C_ij slide 23; passaggio U₂ = C21·U₁; C31 2,2-2,3 | libro pp. 7-12 |
| 9 | R21 = 1,75; burst nel libro; derivazione della power law con il teorema di Euler | libro pp. 12-17 |
| 9 | simulazione di r̄₂(r₁) | codice proprio, eseguito |
| 11 | integrale della coda, γ < −1, cutoff e finite size effect a 10^2,5 e 10³ | libro pp. 22-25 |
| 11 | verifica numerica di CDF + CCDF = 1 e pendenza γ + 1 | codice proprio, eseguito |
| 12 | binning logaritmico, Listing 1.10 in R; curvatura dei dati di X; limiti imposti dalla piattaforma | libro pp. 35-39 |

### Codice

Nessun codice a lezione e nessun notebook. Tutti i blocchi del capitolo sono **note aggiunte**, estratti da `verifica_sd02.py` (Python 3, NumPy 2.5.3), eseguito per intero con `python3 -I verifica_sd02.py`; output salvato in `verifica_sd02_output.txt`. I cinque blocchi Python del manuale sono stati anche estratti dal Markdown ed eseguiti in sequenza (fit, γ, rapporti, CDF/CCDF, r̄₂): output identici a quelli riportati.

| Blocco (sez.) | Esito |
|---|---|
| Fit power law (6) | media 22,8, mediana 1; OLS testa γ = −1,874; OLS tutti i punti −0,781; binning log −1,849 |
| γ dal libro (6) | C21 = 1,629; γ = −1,872 (libro −1,87) |
| Rapporti (8) | 1,903 e 2,903 (slide ≈1,9 e ≈2,9); 2,0 e 3,0; C21 = 1,629 (slide 1,6) |
| r̄₂(r₁) simulato (9) | R21 stimato 1,903 = 59/31, come atteso con tassi costanti; rapporto utenti attivi 1,192 |
| CDF/CCDF (11) | somma 1,0 per ρ = 1, 10, 100; pendenza CCDF −0,846 (atteso −0,87) |

Esiti da notare:
- Una stima di massima verosimiglianza con approssimazione continua e x_min = 1, provata nella prima versione dello script, dava γ = −1,715 (distorta, perché l'approssimazione continua è cattiva a x_min = 1); è stata tolta dallo script e dal capitolo.
- Una prima versione della simulazione misurava anche C21(r) per r = 5, 10, 20, 40 e otteneva 1,72-1,88, non costante e diverso dal rapporto totale 1,19: il modello giocattolo non riproduce la costanza di C21(r) osservata su Wikipedia. Quella parte è stata tolta per non confondere; la simulazione resta solo come illustrazione della formula di r̄₂(r₁).
- I numeri sintetici sono deterministici (seed 42) ma dipendono dal generatore di NumPy: con versioni diverse possono variare leggermente.

### Esame, progetto, consegne

Nessuna menzione di esame, progetto, assignment, consegne o dataset in SD-02 (ricerca per radici sulla trascrizione). Unico compito: leggere il capitolo 1 del libro [1] (slide *Homework*, SD-02 @ 01:04:47).

---

## 03 - Reti sociali

Capitolo: [03-reti-sociali.md](03-reti-sociali.md)

### Fonti e mappatura

| Fonte | Uso |
|---|---|
| SD-03 (portale, preregistrata, 1:16:12 = 4572,16 s) | fonte di verità |
| `3_Social_Networks_SDA25.pdf` (50 pagine) | slide mostrate nel video; tutte renderizzate, figure controllate a vista |
| `3_Social_Networks_SDA26.pdf` (Teams) | confronto testuale con `pdftotext -layout` e `diff` |
| Libro [1], cap. 2, pp. 41-76 | verifica di definizioni, figure e numeri; Listing 2.5 portato a Python 3 |
| Teams 2026 | fuori perimetro per questo capitolo |
| Notebook | nessuno per questa lezione |

#### Mappatura sezioni → slide → video

| Sez. | Slide (pagine SDA25) | Video |
|---|---|---|
| 1 | 3-5 (1-2 non mostrate) | 00:00:10-00:05:52 |
| 2 | 6-10 | 00:05:52-00:17:34 |
| 3 | 11-14 | 00:17:34-00:21:48 |
| 4 | 15-17 | 00:21:48-00:26:51 |
| 5 | 18-19 | 00:26:51-00:30:57 |
| 6 | 20-23 | 00:30:57-00:37:33 |
| 7 | 24-26 | 00:37:33-00:42:02 |
| 8 | 27-38 | 00:42:02-00:52:25 |
| 9 | 39-42 | 00:52:25-00:57:06 |
| 10 | 43 | 00:57:06-01:01:19 |
| 11 | 44-48 | 01:01:19-01:11:39 |
| 12 | 49-50 | 01:11:39-01:16:12 |

L'indice OCR dei frame mostra un solo ritorno indietro (00:22:44 → 00:23:06, di nuovo *In- and Out-Degree*, poi di nuovo *Node and Edge Properties*); per il resto l'ordine del video segue quello delle slide.

### Controlli sulla registrazione

| Controllo | Esito |
|---|---|
| Durata (ffprobe) | formato 4572,159 s; video 4572,133 s; audio 4572,159 s. Nessuno sfasamento |
| Inizio | 0-10,2 s: schermata "Social Data Analytics, Dott.ssa Ida Mele", audio a -91 dB (silenzio digitale). Primo parlato 10,72 s, a metà discorso ("Vi stavo accennando"), già sulla slide 3. Slide 1-2 mai mostrate |
| Fine | ultima parola trascritta 4568,34 s ("quindi voi prendete sempre come"). Profilo RMS a finestre di 0,25 s: parlato (da -19 a -30 dB) fino a 4571,4 s, con pause brevi a 4569,75 e 4570,0; poi crollo a -76/-85 dB a 4571,5 s e fine file a 4572,16 s. Circa **3 s di parlato non trascritti** e **taglio netto a metà frase**, senza la coda di silenzio di una chiusura naturale |
| Ultimo frame | slide 50, *Homework* (tutte le 50 slide percorse) |
| Ritrascrizione della coda | non riuscita: la VM del Mac e il container non raggiungono Hugging Face (403 dal proxy), quindi niente modello Whisper locale. Il contenuto dei 3 s resta `[?]` |
| Contenuto mancante | nessuna slide saltata. Si perde solo la chiusura della raccomandazione di lettura ("prendete sempre come [riferimento le slide?]") |
| Possibile montaggio | a 01:01:19 la docente dice "un argomento che non abbiamo fatto in tempo la volta scorsa è quello del network modeling", ma SD-02 termina con un riepilogo completo ("siamo riusciti a finire anche un po' prima"). Probabile registrazione composta da sessioni diverse; la sequenza delle slide (43 → 44) è regolare |

### Slide SDA25 contro SDA26

Differenze rilevate dal `diff` del testo:

1. p. 6: SDA25 "Social networks (e.g., Facebook, X, Instagram, LinkedIn)"; SDA26 separa "Social networks (e.g., Facebook, X, Instagram)" e aggiunge "Professional social networks (e.g., LinkedIn, ResearchGate)". Riportata nel capitolo, sez. 2.
2. p. 48: virgoletta di chiusura corretta in "friends of friends become friends".
3. Un carattere di spaziatura nel piè di pagina.

Gli errori elencati sotto (pp. 6, 28, 43, 47) sono presenti **in entrambe** le versioni.

### Slide e libro contro parlato

| Punto | Slide / libro | Video | Scelta nel capitolo |
|---|---|---|---|
| Coda e testa dell'arco (00:19:37) | slide: *x* tail, *y* head (convenzione standard); **libro p. 45: head = origine, tail = destinazione** | "seguendo il libro, X è la coda e Y è la testa" | Correzione sull'attribuzione; definizione della slide |
| Metcalfe (00:30:26) | singolo utente ∝ n-1; rete ∝ n(n-1)/2 | il singolo utente vale n(n-1)/2 | Correzione |
| Clustering, massimo dei link (00:43:15) | slide p. 28: "in the undirected graph ... kᵢ(kᵢ-1)"; libro p. 64: "directed" | "perché è un directed" | Correzione sulla slide; la docente è corretta |
| Rewiring (00:49:43, 00:50:40) | slide e libro: scambio delle destinazioni di due archi | "modifichiamo l'orientamento", "cambio le direzioni"; "l'out degree è rimasto per C e D" | Correzione (lapsus: in-degree per C e D; scambio, non inversione) |
| Densità al grado 1 (00:39:37) | annotazione "100%" sul punto (1, 10⁰) | "il 100% hanno in-degree e out-degree pari a 1" | Nota aggiunta: in una densità il valore è < 1, va letto "quasi tutti" |
| LiveJournal, andamento (00:48:33) | slide e libro: power law "apparente", gobba 200-1000 | "seguono a power law" | riportati entrambi |
| Twitter: curve follower/followee | libro p. 56: quasi sovrapposte | non detto | Nota aggiunta dal libro |
| Assortatività di reti tecnologiche e biologiche | slide: "do not show assortative mixing"; libro: "often disassortative" | "le reti che invece non lo sono" | slide; nota con la precisazione del libro |
| *Friendship paradox* | slide p. 42: "the user's friends are more popular than the user" | non commentato (si parla di media e mediana) | riportato come contenuto di slide, nota aggiunta |
| Milgram (00:59:23-01:00:49) | slide: "6-degrees of separation", 1967 | "alcune lettere non sono arrivate", in media sei passaggi | Nota aggiunta: 64 su 296 arrivate, partenze Omaha e Wichita |
| Facemash (00:03:51) | slide: "started as a website gathering photos of Harvard students (Facemash)" | "aveva addirittura un altro nome, era chiamata FaceMash" | Nota aggiunta, non Correzione |
| Spike a 2000 followee (00:41:20) | slide e libro: limite di Twitter | idem, "per evitare spamming" | Nota aggiunta con il limite 2000 → 5000 del 2015 |
| Riepilogo modelli (01:15:00) | *To Sum Up*: "Adding links (Preferential Attachment) and users (Pólya's urn model)" | idem | Nota aggiunta: l'urna generalizzata include entrambi |
| Nomenclatura "urna di Pólya" | libro: "generalized Pólya's urn model" | "modello dell'urna di Pólya" | Nota aggiunta: è il modello di Simon (1955) |

#### Refusi di slide (non segnalati come Correzione nel capitolo)

- p. 6: "World WarCraft" per *World of Warcraft*.
- p. 43: "the second smallest is much smaller than the giant component" per *second largest*. Nel capitolo è riportata la forma corretta ("una seconda componente molto più piccola"), che coincide con quanto dice la docente.
- p. 47: "The modes has a parameter" per *The model has a parameter*.
- p. 17: "delay the message" per *relay* (libro: "relay").

### Correzioni (`> **Correzione:**` nel capitolo)

1. **Coda e testa** (SD-03 @ 00:19:37): definizione corretta, attribuzione al libro sbagliata. Il libro (p. 45) usa la convenzione inversa e non standard.
2. **Legge di Metcalfe** (SD-03 @ 00:30:26): valore del singolo utente n-1, non n(n-1)/2.
3. **Slide p. 28** (clustering): "undirected" va letto "directed"; la docente lo dice correttamente a voce (SD-03 @ 00:43:15).
4. **Rewiring** (SD-03 @ 00:49:43, 00:50:40): si scambiano le destinazioni, non si inverte il verso; per C e D resta invariato l'in-degree.

### Note aggiunte

1. Apertura della registrazione e contenuto dell'outline non mostrato (sez. 1).
2. Facemash e TheFacebook (verificato: Wikipedia, *History of Facebook*).
3. Dettagli del Listing 2.1: namespace 3, regex dei bot, gennaio 2013, 100k utenti e 136k archi (dal libro).
4. NetworkX e l'ordine `(u, v)` degli archi.
5. Grado nel grafo non diretto (dal libro).
6. Normalizzazione delle proprietà di nodi e archi (lettura da database, richiamata dal libro p. 46).
7. Verifica Dijkstra dell'esempio dei ritardi.
8. Completezza nel caso diretto e costo di memoria O(N) contro O(N²) (dal libro p. 48).
9. Snowball contro campione casuale su grafo sintetico.
10. Parametri di visualizzazione del Listing 2.2 (dal libro).
11. "100%" della densità al grado 1.
12. Limite di follow di Twitter (2000, poi 5000 dal 27/10/2015; verificato su Social Media Today e Search Engine Journal) e sovrapposizione delle curve nel libro.
13. Clustering diretto in NetworkX (Fagiolo) contro formula del libro.
14. Numeri della Figura 2.7 (dal libro).
15. Dataset LiveJournal e cause ipotizzate della gobba (dal libro).
16. Rapporto di clustering dopo il rewiring nel grafo sintetico (25x) contro LiveJournal (~1000x); `nx.directed_edge_swap`.
17. *Friendship paradox* (Feld 1991, non ricontrollato), assortatività su grafo Barabási-Albert.
18. Milgram (verificato: Wikipedia, *Small-world experiment*).
19. Esempio numerico del preferential attachment e riferimento Barabási-Albert 1999 (dal libro; anno e rivista non ricontrollati online).
20. Modello di Simon ed esponente asintotico (verificato: Bornholdt ed Ebel, arXiv cond-mat/0008465).
21. Simulazione dell'urna e tabella delle stime dell'esponente.
22. "Winner takes all" nella simulazione.
23. Connection kernel e reti scale-free (dal libro).
24. Riepilogo: Pólya generalizzata copre nodi e archi.
25. Fine della registrazione.

### Codice

La lezione non ha notebook e a schermo non compare codice. Tutto il codice del capitolo è aggiunto.

| Blocco nel capitolo | Tipo | Esito |
|---|---|---|
| In/out-degree del grafo di slide 14 | Nota aggiunta | eseguito: nodo rosso in 1, out 3 (= slide); somme 17 = 17 = archi |
| Dijkstra sul grafo dei ritardi | Nota aggiunta | eseguito: percorsi 65, 38, 24, tre infiniti; minimo 24 (= slide) |
| Snowball sampling | Nota aggiunta | eseguito: livelli 1/54/185/401; 640 archi contro 25 del campione casuale |
| Clustering di slide 29-32 | Nota aggiunta | eseguito: 5, 4, 20, **0,2** (= slide); `nx.clustering` diretto 0,1786 (definizione diversa); non diretto 0,3 |
| Rewiring | Nota aggiunta (porting del Listing 2.7) | eseguito: gradi identici sulla lista di archi; 18 self-loop e 94 doppi; clustering 0,2120 → 0,0084 (25x) |
| Listing 2.5, urna di Pólya | Dal materiale ufficiale (libro), non mostrato a lezione | eseguito dopo il porting Python 2 → 3: 1981 cestini, 10001 palline, 1086/340/159 cestini con 1/2/3 palline, massimo 1652. Il libro non riporta numeri, mostra solo il grafico |

Eseguiti solo nello script `verifica_sd03.py` (risultati citati nel testo, codice non riportato nel capitolo): completezza (sez. [4]), Metcalfe ([5]), assortatività e friendship paradox su grafo BA ([9]), urna veloce a 4·10⁶ passi con stima MLE dell'esponente, BA con m = 1, urna senza preferential attachment ([10]).

**Esiti da segnalare.**

- Esponente dell'urna: le stime convergono a 1 + 1/(1-p) solo nella coda (xmin alto). Con p = 0,8 la coda è troppo corta (massimo 45) e la stima resta a 5,25 contro 6. Non contraddice slide e libro: la formula è asintotica. Valori probabilistici, variano con il seme.
- `nx.clustering` su grafi diretti **non** riproduce la formula del corso: chi usa NetworkX per l'assignment deve saperlo.
- Il rapporto di clustering dopo il rewiring dipende dalla rete: 25x sul grafo sintetico, ~1000x su LiveJournal secondo slide e libro.

Ambiente: Python 3.13.16, NetworkX 3.7, NumPy 2.5.3, Matplotlib 3.11.2 (container).

### Esame, progetto, consegne

Nessuna indicazione su esame, progetto o dataset in questa lezione. L'unico compito è leggere il capitolo 2 del libro [1] seguendo le slide (SD-03 @ 01:15:30), perché la docente cambia l'ordine di alcune parti e ne salta altre.

---

## 04 - Natural Language Processing

Capitolo: [04-natural-language-processing.md](04-natural-language-processing.md)

### Fonti e mappatura

| Fonte | Uso |
|---|---|
| SD-04 (portale, preregistrata, 1:47:06) | fonte di verità per sezioni 1-13: slide 1-46 e tutorial NLTK fino a WordNet |
| SD-05 (portale, preregistrata, 0:38:55) | fonte di verità per sezioni 14-18: slide 47-64, tutorial NLTK (BoW, TF-IDF), tutorial spaCy |
| `4_NLP_SDA25.pdf` (64 pagine) | slide mostrate nel video; testo con `pdftotext -layout`, figure e codice da render a 80 dpi guardati pagina per pagina |
| `4_NLP_SDA26.pdf` (64 pagine, Teams) | confronto, sotto |
| `NLP_withNLTK_tutorial.ipynb`, `NLP_withSpacy_tutorial.ipynb` (portale 2025) | codice del capitolo; rieseguiti per intero |
| stessi notebook 2026 (Teams) | diff cella per cella, sotto; rieseguiti per intero |
| `Natural_Language_Processing_Text.txt` | identico fra 2025 e 2026 (`cmp`), 679 byte, 4 CR |
| Libro [1] cap. 4, pp. 123-134 | riferimento per Stack Exchange, distribuzione dei termini, Zipf, tf-idf |
| Teams 4 (06/10/2026) | integrata dal coordinatore dopo la stesura: 6 riquadri "Integrazione Teams 2026" (sez. 1, 3, 5, 6, 18 e intestazione); riassunto in `out/teams-2026/integrazioni-capitolo-04.md`. Contenuto quasi identico a SD-04/SD-05 |

Struttura della registrazione: SD-04 alterna slide e notebook in due blocchi (00:53-01:02 preprocessing; 01:26-01:47 stemming, lemmatizzazione, PoS, chunking, NER, WordNet). I frame mostrano "Last Checkpoint: 2 hours ago" nel primo blocco e "3 days ago" nel secondo: la lezione è stata registrata in più sessioni. SD-05 riprende dal bag-of-words, con il notebook NLTK a 00:24-00:27 e quello spaCy a 00:30-00:38.

### Slide 2025 contro 2026

Differenze trovate con `pdftotext` e con confronto pixel a pixel delle 64 pagine renderizzate (le altre pagine differiscono solo per il logo del dipartimento nelle pagine titolo):

| Pagina | 2025 | 2026 |
|---|---|---|
| 2 Outline | BoW e TF-IDF sotto "Analyzing text" | voce separata "Representation of documents"; "detecting noun chunks (chunking)" |
| 5 Motivation | "understand how humans understand and interpret NL text" | "**simulate** how humans understand..." |
| 36 PoS Tagging: Example | cella `In [28]` con il ciclo `for words in tokenized_words` | cella `[33]` senza ciclo, con `print(tokenized_words)` |
| 50 BoW: Example (aggregazione) | *was* = 1 (errato) | *was* = **2** |
| 51 BoW: Example (modello finale) | "We get the final model" | "We get the final model: document-term matrix", con frecce "documents" e "terms/words" sulla figura |
| 63 To Sum Up | 4 voci | riformulato: NLP come riduzione del "gap", esempi di UGC, "analysis with WordNet", voce "Document representations" |

### Slide contro parlato

| Punto | Slide | Video | Scelta nel capitolo |
|---|---|---|---|
| Quarto componente | "Disclosure Integration" | idem (SD-04 @ 00:27:14) | Correzione: *Discourse* Integration |
| Statistical NLP | "Models are trained on large amounts of data" | "training completamente unsupervised" (SD-04 @ 00:19:26, 00:21:10) | Correzione |
| Stemming e *to be* | slide Stemming vs Lemmatization: "am, are, is → be" come obiettivo comune | lo stemming collassa *was, were, am, are* su *to be* (SD-04 @ 01:03:22) | Correzione: è la lemmatizzazione |
| Chunk dell'esempio | albero con 2 NP | tre chunk, il terzo "*is walking on*" (SD-04 @ 01:16:20) | output del codice; segnalato fra i punti incerti |
| Antonimo *sharp* | solo lista | interpretato come "elegante" (SD-04 @ 01:25:07) | Correzione: senso musicale |
| BoW aggregato, *by* | 2 | "prima e seconda frase" (SD-05 @ 00:03:17), poi "prima e terza" (00:04:21) | prima e terza; nota nella Correzione |
| Rapporto dell'IDF | "never less than 1" | "sempre minore o uguale a 1" (SD-05 @ 00:23:08) | Correzione, a favore della slide |
| IDF di un termine in tutti i documenti | log(1) = 0 | "parole che hanno logaritmo pari a 1" (SD-05 @ 00:17:57) | lapsus, segnalato |
| Figura distribuzione dei termini | assi: numero di occorrenze / numero di termini | spiegata in termini di rango (SD-05 @ 00:12:46) | nota aggiunta che distingue le due viste |
| NER: frase usata | slide con *United States near Yosemite Park* | il notebook ha attiva quella con *Switzerland near WHO*; a schermo Mele inverte il commento (SD-04 @ 01:38:59, `frame_01-39-32`) | riportati entrambi gli output |

### Notebook contro schermo

- **SD-04 @ 01:39:32**: la cella NER `[54]` a schermo ha attiva la frase *United States... Yosemite Park* e commentata quella della Svizzera; nel notebook distribuito è il contrario. Output a schermo: PERSON, PERSON, GPE (*United States*), FACILITY (*Yosemite Park*), identico alla riesecuzione e al notebook 2026.
- **SD-05 @ 00:25:59-00:26:59**: la cella TF-IDF a schermo coincide con il notebook (frasi a tre, `norm=None`, frase a due commentata). A voce Mele dice di poterla eseguire anche sull'esempio delle slide; i frame mostrano solo la versione a tre frasi.
- **Slide 21** (tokenizzazione con `RegexpTokenizer`) e **slide 24** (`stop_words[:20]`): codice presente solo nelle slide. Il primo è stato rieseguito, output identico alla slide. Il secondo nella slide dà `['i', 'me', 'my', ...]`, ordine delle vecchie versioni di NLTK; notebook 2025, 2026 e NLTK 3.10.4 danno la lista alfabetica di 198 parole.
- **Slide 32** (`lemma.lemmatize(w)` senza `pos`): non è nel notebook nella stessa forma; rieseguita, output identico (*study, leaf, decrease, play*).

### Notebook 2025 contro 2026 (diff cella per cella)

#### `NLP_withNLTK_tutorial.ipynb` (2025: 84 celle; 2026: 85)

| Cella 2025 → 2026 | Differenza |
|---|---|
| [2] | output `Python 3.12.2` → `Python 3.10.20` |
| [6] | nel 2025 la cella `wget` è commentata ma conserva l'output di un'esecuzione precedente (31/10/2025, file salvato come `...txt.2`); nel 2026 senza output |
| [10] | output di `nltk.download("popular")`: differenze solo di stato dei pacchetti |
| [19] | 2026 stampa anche il testo originale; il secondo `print` dice per errore "original text:" davanti al testo pulito |
| (nessuna) → [20] | **nuova cella 2026**: `lower()` su `"Apple is a Company"` |
| [20] → [21] | aggiunto il commento `#reduce all words to lowercase` |
| [28]/[29] | la cella markdown "After preprocessing we have a cleaned text" è spostata dopo l'intestazione WordCloud |
| [31] → [32] | `clean_text + " "+clean_word` → `clean_text+" "+clean_word` (solo spazi) |
| [49], [51], [52], [56], [58], [60] → [50], [52], [53], [57], [59], [61] | **tolto il ciclo superfluo** `for words in tokenized_words:` attorno a `nltk.pos_tag`; in [50] aggiunto `print(tokenized_words)`. Output identici |
| [53]/[54] | celle markdown riordinate ("Here, study is correctly tagged as a verb" e intestazione Chunking) |
| [58] → [59] | output 2026 contiene due righe di log macOS (`IMKClient subclass`) prodotte da `draw()` |
| [60] → [61] | **`binary=True` → `binary=False`** nella cella "Named Entity Recognition plus PoS tagging"; il commento dice ancora "print if it is a named-entity". Output con i tipi (PERSON, GPE, FACILITY) invece di NE: l'esempio `binary=True` della lezione non è più nel notebook 2026 |
| [82] → [83] | frase 3: `"full.Travelling"` → `"full. Travelling"` (spazio dopo il punto); output identico, perché il tokenizer di scikit-learn spezza comunque sul punto |
| altre | solo numeri di esecuzione |

#### `NLP_withSpacy_tutorial.ipynb` (2025: 17 celle; 2026: 16)

| Cella | Differenza |
|---|---|
| [1] | `Python 3.12.2` → `Python 3.10.20` |
| [3] | 2025 `!python3 -m pip install --user spacy` attivo; 2026 commentato |
| [5]-[7] 2025 | **2026 toglie le celle delle stopword di spaCy e di `string.punctuation`**; `nlp = spacy.load(...)` e `text = ...` spostati in una sola cella |
| [9] → [7] | ordine di `doc = nlp(text)` e dei `print` invertito; "Input text:" → "Input:" |
| [10] → [8] | tolto il `"\n"` finale nel `print` (output più compatto) |
| [15] → [13] | **output: 2 entità invece di 3**, *WHO* non è più riconosciuto come ORG |
| [15], [16] | tolto il commento sugli indici di inizio e fine |

### Correzioni e note aggiunte

**Correzioni** (`> **Correzione:**` nel capitolo):

1. **Statistical NLP non è solo unsupervised** (SD-04 @ 00:19:26): molti modelli (il tagger di `nltk.pos_tag`, i modelli spaCy) sono addestrati su corpora annotati.
2. **Discourse, non Disclosure Integration** (slide 2025 e 2026, SD-04 @ 00:27:14).
3. **Lo stemming non riduce *was/were/am/are* a *be*** (SD-04 @ 01:03:22): Porter dà `am, is, are, wa, were`; serve il lemmatizer con `pos="v"`. Verificato.
4. **PRP$ nel Penn Treebank** (slide PoS, SD-04 @ 01:11:41): è il tag di *my, your, his, their*; *mine, yours, theirs* sono PRP. Basato sulle linee guida del Penn Treebank (Santorini 1990), non ricontrollate sulla fonte primaria in questa sessione; verificato per esecuzione che *my* è taggato PRP$.
5. **Antonimo *sharp*** (SD-04 @ 01:25:07): viene da `natural.a.05`, nota musicale (bequadro contro diesis), non dalla moda. Verificato su WordNet 3.0.
6. **BoW aggregato, *was* = 2** (slide 2025 p. 50; corretta nella 2026) e lapsus su *by* (SD-05 @ 00:03:17).
7. **Rapporto dell'IDF ≥ 1** (SD-05 @ 00:23:08): detto "minore o uguale a 1".
8. **TF-IDF di *second* = 0,1155, non 0,13** (slide p. 59; SD-05 @ 00:18:28); *first* = 0,1386 è troncato a 0,13 nella slide. Più il lapsus "logaritmo pari a 1" (SD-05 @ 00:17:57).

**Note aggiunte** principali: comportamento reale dei tagger sull'esempio *can* (NLTK sbaglia, spaCy no); versioni delle librerie e opt-in proxy di `nltk.download`; 679 byte contro 675 caratteri; ciclo superfluo attorno a `pos_tag`; errore di tagging di *English*; `draw()` e Tkinter; spaCy che separa *Mr.* e *Smith* (NLTK) / tagga il parco come GPE; WordCloud con stopword e plurali propri; riassegnazione di `stopwords`; token_pattern e lowercase di `CountVectorizer`; sparsità 26/45; assi della figura di Zipf ed esponente -1,45 del libro; base del logaritmo; formula di `TfidfVectorizer` (tf grezzo, smoothing, +1, L2) con tabella delle configurazioni e codice per riprodurre la slide; formula di Wu-Palmer; *WHO* stopword per spaCy; *WHO* non più riconosciuto da `en_core_web_sm` 3.8.0; stopword spaCy (326) contro NLTK (198); Snowball per l'italiano; Meta come utente di spaCy non verificato.

### Codice eseguito ed esiti

Ambiente: container Linux, Python 3.13.16, NLTK 3.10.4 (dati: `popular`, `punkt_tab`, `averaged_perceptron_tagger_eng`, `maxent_ne_chunker_tab`), spaCy 3.8.16 + `en_core_web_sm` 3.8.0, scikit-learn 1.9.1, wordcloud 1.9.6, matplotlib 3.11.2. Esecuzione con `nbclient` (`allow_errors=True`), `NLTK_ALLOW_PROXIED_URLOPEN=1`.

| Notebook | Esito | Celle in errore |
|---|---|---|
| NLTK 2025 | tutti gli output testuali **identici** al notebook (escluse versione di Python e log dei download) | [56], [58], [60]: `ModuleNotFoundError: No module named 'tkinter'` su `.draw()`, dopo aver stampato l'output. Errore d'ambiente (container senza GUI), non del notebook |
| NLTK 2026 | identici | [57], [59], [61]: stesso errore Tkinter |
| spaCy 2025 | identici tranne la NER [15]: **2 entità invece di 3** (*WHO* non riconosciuto). Ordine di stampa delle stopword diverso (è un `set`) | nessuna; la cella `pip install --user` gira e installa |
| spaCy 2026 | identici, incluse le 2 entità | nessuna |

Nessuna cella fallisce senza ragione d'ambiente. Da segnalare per chi riesegue sul proprio computer: `draw()` apre una finestra Tk che va chiusa, e su sistemi senza display fallisce; `nltk.download` dietro un proxy richiede l'opt-in con NLTK ≥ 3.10; con NLTK 3.9+ i dati `punkt_tab`, `averaged_perceptron_tagger_eng` e `maxent_ne_chunker_tab` sostituiscono quelli vecchi, ma `download("popular")` li include.

`verifica_sd04.py` (output in `verifica_sd04-output.txt`), tutte le sezioni eseguite con successo:

1. tokenizzazione della slide *Let's tokenize!*: righe "spazi" e "regole" confermate;
2. PoS di *Can you help me with the can?*: NLTK `MD`/`MD` (secondo *can* sbagliato), spaCy `MD`/`NN`;
3. BoW: matrice a mano = `CountVectorizer` (True); aggregato *was* = 2, *by* = 2; 26 zeri su 45 celle;
4. TF-IDF a mano con la formula della slide: *first* 0,1386, *second* 0,1155, tutti gli altri 0;
5. stesso esempio con `TfidfVectorizer` in tre configurazioni (default, `norm=None`, `norm=None, smooth_idf=False`) e riproduzione esatta della slide via `idf_ - 1`;
6. tre frasi con `norm=None`: 1,69314718 = ln(4/2)+1, 1,28768207 = ln(4/3)+1, 1 = ln(4/4)+1, *flight* = 2 × 1,693 = 3,386; con L2 la riga 1 diventa `[0.4107 0.4107 0.3124 ...]`;
7. 679 byte, 675 caratteri, 4 CR;
8. stemming di *am/is/are/was/were* (Porter `wa`) contro lemmatizzazione (`be`);
9. tokenizzazione della slide con `word_tokenize` e `RegexpTokenizer`; lista stopword NLTK di 198 parole in ordine alfabetico;
10. antonimi di *natural* con il synset di provenienza; Wu-Palmer *ship/boat* 0,909 con LCS `vessel.n.02`.

Verifiche puntuali fuori script: Porter, Snowball e Lancaster su *consult...*, *changing...*, *university/universe* (tutti *consult*, *chang*, *univers*); `lemmatize` senza `pos` su *studies, leaves, decreases, plays*; stopword spaCy (326, contengono *made, three, full, call, who*); `WordCloud().generate(text)` sul testo grezzo (pesi massimi *pig*, *little*).

### Tentativi non riusciti

- **Ritrascrizione dei due buchi** (SD-05 @ 00:15:13, SD-04 @ 01:19:48): estratti i tratti audio, ma il download del modello `faster-whisper` da Hugging Face è bloccato dal proxy (403). Recuperati poi sul Mac con mlx-whisper (`scripts/ritrascrivi_tratti.py`) e integrati.
- **Teams 4**: integrata a posteriori, timestamp a blocchi di 10 minuti marcati "circa".

---

## 05 - Text similarity e topic modeling

Capitolo: [05-text-similarity-e-topic-modeling.md](05-text-similarity-e-topic-modeling.md)

### Fonti e mappatura

| Fonte | Uso |
|---|---|
| SD-06 (portale, preregistrata), da 00:00:10 a 00:49:53 | fonte di verità. Da 00:50:01 ("Supervised Approaches") la lezione passa alla sentiment analysis supervisionata: capitolo 06, non trattata qui |
| `5_TextSimilarity_SDA25.pdf` (39 pagine) | slide del video, testo con `pdftotext -layout`, tutte le pagine renderizzate e guardate |
| `5_TextSimilarity_SDA26.pdf` (Teams) | testo identico (`diff` vuoto). Differenze grafiche solo nelle quattro slide di titolo (pp. 1, 10, 16, 20): rimosso il logo DMF. Su p. 25 una differenza di 8 pixel, artefatto di rendering |
| Libro [1], cap. 4, pp. 129-153 | riferimento per clustering su Stack Exchange, popolarità dei topic, interessi degli utenti, topic extraction, LDA |
| Notebook I livello | nessuno su questi temi |
| `Tutorials/topic_modeling_Gensim_BERTopic/` (Teams, II livello) | solo citato in una nota (sez. 9), per la traccia #SDA3 |
| Teams 2026 | nessuna integrazione per questo capitolo |

Mappatura sezioni del capitolo → slide (numerazione PDF) → tempo nel video:

| Sezione | Slide | SD-06 |
|---|---|---|
| 1 Clustering e text similarity | 1-3 | 00:00:10-00:02:46 |
| 2 Clustering gerarchico | 4 | 00:02:46-00:05:36 |
| 3 Document clustering e cosine | 5-7 | 00:06:09-00:10:28 |
| 4 Step e problemi | 8 | 00:10:28-00:13:25 |
| 5 Dendrogramma | 9 | 00:13:25-00:15:30 |
| 6 Stack Exchange, valutazione | 10-12 | 00:15:30-00:20:05 |
| 7 Popolarità, interessi | 13-15 | 00:20:05-00:23:37 |
| 8 Topic extraction, string matching | 16-19 | 00:23:37-00:30:06 |
| 9 Statistical topic modeling | 20-22 | 00:30:06-00:36:12 |
| 10 LDA input/output, modello grafico | 23-25 | 00:36:12-00:39:40 |
| 11 Processo generativo, inferenza | 26-32 | 00:39:40-00:43:34 |
| 12 Tool, clustering con LDA | 33-37 | 00:43:34-00:46:37 |
| 13 Riepilogo e compiti | 38-39 | 00:46:37-00:49:53 |

### Slide contro parlato

| Punto | Slide | Video | Scelta |
|---|---|---|---|
| Cut height e dimensione dei cluster (p. 14) | "We go higher in the dendrogram (e.g., cut height with 0.5) and clusters are bigger"; "steeper for larger clusters" | stesso contenuto, 0,7 e 0,9 "più in profondità" | **Correzione** (vedi sotto) |
| Tabella User Interests (p. 15) | "The most popular tag is used by around 50% of the users" | "il tag più frequente è stato usato dal 52,1% degli utenti" | **Correzione** (vedi sotto) |
| Esempio Wikipedia (p. 26) | 50% / 30% / 20% | "50% politica, 30% geografia, 3% religione" | 20% con [?] |
| Topic 2 con K = 3 (p. 24) | "county" | "country" | riportata la slide, segnalato nei punti incerti |
| Lunghezza dei documenti (p. 25) | "assumption all documents have same length" | aggiunge che i documenti corti si riempiono di "parole vuote" | **Correzione** sul riempimento |
| BERTopic (p. 22) | embedding BERT + class-based TF-IDF | migliore "rispetto alla semplice definizione di TF-IDF" | nota aggiunta: anche BERTopic usa una TF-IDF |
| Inferenza (p. 31) | Gibbs sampling | "GIF sampling" (Gibbs) | riportato; nota aggiunta: i tool della slide usano inferenza variazionale |
| Video contro PDF 2025 | "It is called 'cosine similarity'"; "Computing Similarity" con "for dimensionality reduction" | il video (frame 00:10:18, 00:13:27) mostra "It's called 'cosine'" e "stemming, lemmatization" senza "for dimensionality reduction" | differenze di forma, testo del PDF |

### Slide contro libro

| Punto | Slide | Libro | Nota |
|---|---|---|---|
| Esempio string matching | "The right player could have scored that goal" | "The right winger..." | nota aggiunta nel capitolo |
| "same as taking the dot product u · v" | frase isolata | riferita al numeratore della formula | nota aggiunta: vero solo per vettori normalizzati |
| "distance metric" | cosine similarity come "distance metric" | stessa frase | nota aggiunta: è una similarità; 1 - cos non è una metrica (controesempio eseguito) |
| Distanza | d = 1 - S | il codice R usa d = -S per non perdere la sparsità, poi somma 1 alle altezze | nota aggiunta |
| Grafico modello LDA | β dentro un plate K (LDA "smoothed") | Figura 4.15: β fuori dai plate | nota aggiunta sul processo generativo standard |

### Correzioni

1. **Cut height** (SD-06 @ 00:21:26-00:22:30, slide p. 14). Lezione e slide dicono che tagliando a 0,5 si ottengono cluster più grandi e che la distribuzione è più ripida per i cluster più grandi. È il contrario: l'asse del dendrogramma è una distanza, quindi 0,5 è un taglio **basso**, con molti cluster piccoli, e 0,9 un taglio alto, con pochi cluster grandi. Fonti: libro cap. 4 ("As we go higher in the dendrogram (let the clustering proceed further), we start to see the distributions shift toward larger cluster sizes", con esponente "shallower"); il grafico della slide stessa (serie 0,5 fino a circa 10 post per ramo, serie 0,9 oltre 100); verifica per esecuzione (sezione 6 dello script: 446 cluster con dimensione media 3,4 a 0,5, 25 cluster con media 60 a 0,9).
2. **User interests, 52,1%** (SD-06 @ 00:22:30, slide p. 15). Non è la quota di utenti che usa il tag più popolare: è la frequenza relativa media, nei post di un utente, del suo tag più usato (rank per utente). Fonte: didascalia della Table 4.1 del libro, Listing 4.6. Verifica con una reimplementazione Python della Listing 4.6 su dati inventati.
3. **Documenti riempiti con "parole vuote"** (SD-06 @ 00:38:37-00:39:07). In LDA ogni documento ha la sua lunghezza N_d; la lunghezza uguale è solo una semplificazione della figura, e né scikit-learn né Gensim fanno padding: lavorano su conteggi bag of words.

### Note aggiunte

- Precisazioni sulla cosine similarity: intervallo [-1, 1] in generale, 1 per vettori proporzionali, prodotto scalare uguale solo per vettori normalizzati, 1 - cos non metrica.
- Dettagli del libro non detti a lezione: 54 termini per post e 116.000 di vocabolario, trucco d = -S, taglio a 0,9 per scegliere i sottoalberi A/B/C, esponente -1,4 della distribuzione dei tag, tag più usati, "right winger".
- Formulazione di Firth (1957): non verificata su fonte primaria.
- BERTopic usa una TF-IDF class-based.
- Processo generativo di LDA in notazione standard (Dirichlet su θ e β, categoriali su z e w).
- Inferenza approssimata: MCMC (Gibbs) o variazionale. Verificato il 22/10/2026 sulla documentazione: `sklearn.decomposition.LatentDirichletAllocation` usa "online variational Bayes" (default `learning_method='batch'`, priori di default 1/n_components); `gensim.models.LdaModel` implementa l'online LDA di Hoffman et al. (2010). Il libro usa il Gibbs sampler del pacchetto R `lda`.
- Tutorial II livello `topic_modeling_Gensim_BERTopic` citato per la traccia #SDA3.

### Codice eseguito

Nessun codice a lezione e nessun notebook ufficiale. Tutti gli 8 blocchi Python del capitolo sono note aggiunte; li ho estratti dal Markdown ed eseguiti così come sono scritti. Il blocco della sez. 7 sui tagli (variabile `Zs`) è un estratto: gira per intero nello script. Lo script `verifica_sd05.py` contiene tutto; l'output completo è in `verifica_sd05_output.txt`. Ambiente: Python 3, numpy 2.5.3, scipy 1.18.1, scikit-learn 1.9.1. Gensim non è installato nel container e non è stato usato.

| # | Verifica | Esito |
|---|---|---|
| 1 | cosine similarity, tre forme della formula | 0.8895 in tutti e tre i casi; prodotto scalare grezzo 12; d = 0.1105 |
| 2 | esempio string matching della slide | similarità 0.0 |
| 3 | "Good morning!" su 1M dimensioni | 2 componenti non nulle, frazione 2e-06 |
| 4 | disuguaglianza triangolare con 1 - cos | d(a,c) = 1.0 > d(a,b) + d(b,c) = 0.5858: violata |
| 5 | clustering gerarchico, average/single/complete | 7 merge per 8 documenti; ordine delle fusioni coerente con l'esempio sportivo della lezione; sklearn `AgglomerativeClustering` concorde |
| 6 | tagli del dendrogramma su dati sintetici | 0,5: 446 cluster (media 3,4); 0,7: 60 (25,0); 0,9: 25 (60,0). Conferma la correzione 1 |
| 7 | Listing 4.6 in Python | {1: 0.756, 2: 0.178, 3: 0.067} |
| 8 | LDA sklearn, 2 seed, hard e soft | stessi tre topic, numerazione permutata; il doc 10 cambia da θ = [0.87, ...] (seed 0) a mix [0.38, 0.57, ...] (seed 1). Risultato probabilistico: dipende da seed e versione |

Nessun output da confrontare con slide o notebook: gli esempi delle slide (dendrogramma Stack Exchange, grafici power law, tabella 52,1%, topic K = 3) vengono da dati non forniti e non sono riproducibili. Le verifiche riproducono i meccanismi, non i numeri.

---

## 06 - Sentiment analysis

Capitolo: [06-sentiment-analysis.md](06-sentiment-analysis.md)

### Fonti e mappatura

| Fonte | Uso |
|---|---|
| SD-07 (portale, intera, 1:14:14) | fonte di verità, sez. 1-10 (slide 1-35) |
| SD-06 da 00:49:53 alla fine (1:03:48) | fonte di verità, sez. 11 (slide 36-41). La nota della docente dice "dal minuto 50": la frase di passaggio è a 00:49:53, la slide-titolo "Supervised Approaches" compare nel frame 00:50:01 |
| SD-08 (intera, 1:21:15) | fonte di verità, sez. 12-18 (slide 42-62) e tutorial dal vivo (00:13:43-01:03:56) |
| `important_note_about_videos.txt` | ordine di lettura SD-07 → SD-06 (parte finale) → SD-08 |
| `6_Sentiment_Analysis_SDA25.pdf` (62 pp.) | struttura, testo delle slide, figure guardate a 80 dpi (schema ML/NLP/AI, tabella del lessico, tabella 3.2, formule PMI/SO, Bayes, confusion matrix, esempio micro/macro, ROC) |
| `6_Sentiment_Analysis_SDA26.pdf` (62 pp.) | confronto: vedi sotto |
| `Sentiment_mining_Twitter.ipynb`, `Read_Clothing_Reviews.ipynb` (portale 2025) | codice e output del capitolo |
| versioni Teams 2026 + `Sentiment_mining_Twitter-sample.ipynb` + `Twitter_train_clean.tsv` | diff, sez. 15.10 |
| Liu, *Sentiment Analysis and Opinion Mining* | par. 2.1.1 (quintupla), 3.2 (Turney, tabella 3.2, eq. 3), 3.3, 3.5, 4.4 (sarcasmo) |
| `0_General_Info_SDA26.pdf`, pagina *Assignment: Proposals* | solo nota di collegamento alle tre proposte dette a voce |
| Registrazioni Teams 2026 | non usate (perimetro) |

### SDA25 contro SDA26

Testo identico salvo:

| Pagina | SDA25 | SDA26 |
|---|---|---|
| 8 | "negation handling, and word-sense disambiguation" | "negation handling, and Word-Sense Disambiguation (WSD), NER" |
| 45-47 | confusion matrix senza titoli | etichette "confusion matrix" e "'positive' class" sopra la figura |
| 47 | "(macro) avgerage can be misleading, it is better to use a the micro-avgerage" | "average" e "micro-average" corretti; resta "use a the micro-average" |
| 1, 6, 11, 18, 27, 36, 42, 52 (pagine-titolo) | loghi Data Analytics, Roma Tre, DMF | senza logo DMF |

Confronto pixel per pagina (ImageMagick, fuzz 5%): nessun'altra differenza.

### Slide nel video contro PDF

Le slide registrate (2025) differiscono in qualche dettaglio dal PDF SDA25 distribuito:

| Punto | Video | PDF |
|---|---|---|
| SD-07 @ 00:48:34, slide 19 | "Classifying text based on the sentiment: Subjectivity Analysis / Polarity Detection" | "Sentiment classification is based on two steps: Subjectivity Classification / Orientation (Polarity) Detection" |
| SD-07 @ 00:55:48, slide 23 | "Also sentences may express..." | "Also, the sentences may express..." |

Contenuto equivalente; il capitolo segue il PDF.

### Slide contro parlato

| Punto | Slide | Parlato | Scelta |
|---|---|---|---|
| Soglia rating → label | slide 37: tre schemi espliciti | "almeno tre stelline" positive (SD-07 @ 00:09:25); "più di 3 su 5" (SD-07 @ 00:21:55); poi gli schemi della slide (SD-06 @ 00:51:44) | tabella della slide, incoerenze in "Punti incerti" |
| Rating delle review di abbigliamento | | negativi "0 o 1 o 2" (SD-08 @ 01:04:31) | Correzione: il rating va da 1 a 5 (verificato sul file) |
| P(D\|h) | "posterior probability of D given h" | idem (SD-08 @ 00:00:39, 00:03:02) | Correzione: è la likelihood |
| AUC | "aggregate measure of performance across all possible classifiers" | "più è grande l'AUC migliore il classificatore" | Correzione: across all classification thresholds |
| Recall | TP / (TP + FN) | trascritto "true positive diviso i false negative" (SD-08 @ 00:05:48) | segue la slide; probabile errore di trascrizione |
| Percentuale negativi | | "circa il 43%" (SD-08 @ 00:45:59) | 43,54%: nota |
| Accuracy tutorial | notebook 0.7679 | "0,76" (SD-08 @ 00:41:52) | entrambi riportati |
| Confronto con l'autore | tabella: 0.7601 | "0 76 01 ... 0 76 e 79" (SD-08 @ 00:44:51) | interpretato 0,7601 contro 0,7679; nota sulle cause |

### Notebook contro schermo

| Punto | Schermo | Notebook | Scelta |
|---|---|---|---|
| Cella negativi SIA1 (SD-08 @ 00:50:05) | output di una sessione precedente: `NameError: name 'total_data' is not defined` (Cell In[1]); la docente: "devo ricalcolare, vabbè dopo lo faccio" | output corretto, 2758 tweet | riportato il notebook, errore annotato nel capitolo |
| Tutto il resto | coincide con il notebook distribuito (frame 00:24:28, 00:38:16, 00:39:36, 00:42:04, 00:42:59, 00:45:24, 00:50:10, 00:56:34, 00:57:40, 01:03:55, 01:04:32) | | |

### Correzioni (`> **Correzione:**` nel capitolo)

1. **P(D|h) chiamata "posterior"** (slide 44; SD-08 @ 00:00:39, @ 00:03:02): nella terminologia standard è la likelihood; P(D) è l'evidence.
2. **AUC "across all possible classifiers"** (slide 50): è aggregata su tutte le soglie di classificazione dello stesso classificatore (la prima riga della stessa slide lo dice correttamente).
3. **Rating "0 o 1 o 2"** (SD-08 @ 01:04:31): nel `Clothing_review.csv` il rating va da 1 a 5 (842, 1.565, 2.871, 5.077, 13.131 righe). La regola del notebook è corretta.

### Note aggiunte (`> **Nota aggiunta:**` nel capitolo)

| Sezione | Contenuto | Verifica |
|---|---|---|
| 4 | quintupla come schema relazionale; quadrupla (g, s, h, t) di Liu e aspetto GENERAL | Liu par. 2.1.1 |
| 10.4 | VADER e TextBlob sulle frasi delle slide (film, auto sarcastica, domanda Nokia, materasso) | eseguito, `verifica_sd06.py` sez. 9 |
| 10.5 | estrazione Turney passo 1 con il POS tagger di NLTK | eseguito, sez. 2 |
| 10.5 | SO con soli conteggi (eq. 3 di Liu), esempio con hit inventati, accuratezze 84%/66% | eseguito, sez. 3; Liu par. 3.2 |
| 11.5 | range di polarity/subjectivity di TextBlob, VADER | documentazione |
| 12 | regola di decisione del Multinomial NB con smoothing di Laplace, esempio a mano contro sklearn | eseguito, sez. 4 |
| 13.3 | macro F1 di sklearn = media degli F1 (diversa dalla formula della slide in generale); micro = accuracy in multiclasse; weighted avg | eseguito, sez. 5 |
| 13.4 | ROC richiede score; AUC come probabilità di ordinamento corretto | eseguito, sez. 7 |
| 15.1 | `tweet`/`sentiment` contengono nomi di colonna | lettura del codice |
| 15.2 | **due bug del preprocessing**: le negazioni contratte spariscono (la regex delle lettere singole cancella la *t* di *n't* prima delle contrazioni); `:D` e `XD` non riconosciuti perché `lower()` precede `emoji()` | eseguito, sez. 8 |
| 15.3 | `lemmatize(w, pos='v')` tratta tutto come verbo | lettura del codice |
| 15.4 | `toarray()` denso da ~339 GiB: MemoryError su Linux | eseguito (errore riprodotto) |
| 15.5 | shuffle di default, `stratify` | documentazione scikit-learn |
| 15.6 | ordine degli argomenti in `accuracy_score` | lettura del codice |
| 15.7 | 0,7601 contro 0,7679; determinismo di NB; "Leaderboard Highest: 0.79249" del notebook 2026 | eseguito |
| 15.8 | soglie raccomandate di VADER (±0,05) | README vaderSentiment |
| 15.8 | "must think about positive" etichettato negativo da TextBlob: subjectivity 0,545, polarity 0,227 ≤ 0,5 | eseguito, sez. 9 |
| 15.9 | *amp* = residuo di `&amp;` (2.769 tweet lo contengono); *na* da *gonna*/*wanna* (`word_tokenize` → gon, na) | eseguito |
| 15.9 | log-log a gruppi di quattro ranghi; LDA su TF-IDF | lettura del codice |
| 16 | statistiche del dataset delle review, sbilanciamento, `Recommended IND`, fonte Kaggle/OpenML | eseguito; OpenML d/43673 |
| 16 | proposte #SDA1-#SDA3 della slide 2026 | `0_General_Info_SDA26.pdf` |
| 17.3, 17.5 | VADER/TextBlob sulla condizionale; risultati di González-Ibáñez et al. (57%) | eseguito; Liu par. 4.4 |

### Codice eseguito

Ambiente del container: Python 3.13.16, pandas 3.0.5, scikit-learn 1.9.1, NLTK 3.10.4, numpy 2.5.3, TextBlob 0.20.1, wordcloud 1.9.6. Dati NLTK scaricati: wordnet, omw-1.4, vader_lexicon, punkt, punkt_tab, averaged_perceptron_tagger_eng.

| Notebook | Esito |
|---|---|
| `Sentiment_mining_Twitter.ipynb` (2025) | eseguito per intero. Unica modifica: le due celle `print(...toarray())` sostituite con `print(shape, nnz)` perché la versione originale fallisce con `MemoryError: Unable to allocate 339. GiB for an array with shape (99989, 455577)` (riprodotto). **Tutti gli output numerici identici al notebook distribuito**, LDA compreso; differenze solo nel `dtype` stampato (`str` con pandas 3) |
| `Sentiment_mining_Twitter.ipynb` (2026) | eseguito per intero (stesse due stampe `toarray()` sostituite): output identici al notebook distribuito salvo kernel, percorsi `nltk_data`, `dtype` e larghezza delle tabelle pandas; `Twitter_train_clean.tsv` rigenerato identico a quello distribuito |
| `Sentiment_mining_Twitter-sample.ipynb` (2026) | celle eseguite come script (sotto nbclient il kernel moriva, causa d'ambiente non indagata): 75.856 feature, confusion matrix [[615, 256], [278, 851]], accuracy 0,733, F1 0,70/0,76, AUC 0,8013, coincidenti con il file |
| `Read_Clothing_Reviews.ipynb` (2025 e 2026) | eseguiti, output identico (22.628 righe) |
| `verifica_sd06.py` | output in `verifica_sd06_output.txt` |

Esiti di `verifica_sd06.py` sugli esempi delle slide:

| Esempio | Slide/lezione | Ottenuto |
|---|---|---|
| lessico, somma | +5,5 | +5,5 |
| lessico con negation detection | positivo | +1,5 |
| lessico con negazione e terrible = -5 | negativo (-2 + -5 + 5) | -2 |
| Turney passo 1 su "This piano produces beautiful sounds" | "beautiful sounds", pattern 1 | idem |
| macro precision 4 classi | 0,4 | 0,4 (a mano e sklearn) |
| micro precision 4 classi | 0,123 | 0,1226 (a mano e sklearn) |
| metriche dalla confusion matrix del tutorial | report 0.73/0.79, macro 0.76, weighted 0.77, accuracy 0.77 | 0,7342/0,7941, 0,7641, 0,7679, 0,7679 |
| NB a mano contro sklearn | (nota aggiunta) | 0,7262/0,2738 identici |

### Esiti anomali

1. **MemoryError** sulle stampe dense (sopra): il notebook non è eseguibile così com'è su Linux con overcommit di default.
2. **Bug del preprocessing** (negazioni contratte perse, `:D`/`XD` non riconosciuti): non cambiano i risultati riportati, che sono quelli del notebook, ma contraddicono quanto la lezione dice sull'importanza di negazioni ed emoticon.
3. **Soglie di VADER e TextBlob** asimmetriche: spiegano i conteggi sbilanciati (30.707 "negativi" di TextBlob).
4. Il confronto "0,76 contro 0,79" del brief non regge: a voce sono 0,7601 (autore) e 0,7679 (docente e mia esecuzione). Lo 0,79 è probabilmente il "Leaderboard Highest: 0.79249" del notebook 2026, non citato a voce.

---
