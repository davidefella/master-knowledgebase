# Divergenze

> Fonte Notion: https://app.notion.com/p/3e912abc808d81a4b584f0b4648ed332 — ultima modifica 2026-09-28T18:31:49.546Z

Differenze fra video, slide e notebook, errori del docente, e parti ricostruite. Una sezione per capitolo.
## Mappatura lezioni e materiale
<table header-row="true">
<tr>
<td>Registrazione</td>
<td>Giornata</td>
<td>Slide</td>
<td>Notebook (da confermare capitolo per capitolo)</td>
</tr>
<tr>
<td>nessuna</td>
<td>Day 1</td>
<td>`Day1_v25.pdf` (2025), `Biotech Data Processing Course Introduction.pdf` (2026, contenuto diverso)</td>
<td>nessuno</td>
</tr>
<tr>
<td>BT-01</td>
<td>Day 2</td>
<td>`Math_in_biology.pdf`</td>
<td>`Lotka_Volterra` (a schermo `Lotka-Volterra`), `Zombie_invasion`. I notebook `01`-`04` Eulero/odeint ed `Epidemiology` non compaiono nel video: probabilmente edizione 2026</td>
</tr>
<tr>
<td>BT-02</td>
<td>Day 3</td>
<td>`ABMS.pdf` (solo Teams, maggio 2026)</td>
<td>`Zombie_ABMS_lezione_3_Biotech`, `Biotech_LEZIONE3`</td>
</tr>
<tr>
<td>BT-03</td>
<td>Day 4</td>
<td>`TDA.pdf`</td>
<td>`Jerne`, `MESA_KURAMOTO*`, `MESA_VICSEK_persistent_entropy_final`, `mapper_quickstart`</td>
</tr>
<tr>
<td>BT-04</td>
<td>Day 5</td>
<td>nessuna</td>
<td>`SIR_ABMS`, `SIR_Network`</td>
</tr>
<tr>
<td>BT-05</td>
<td>Day 6</td>
<td>nessuna</td>
<td>notebook del genoma a schermo, non nel materiale</td>
</tr>
<tr>
<td>BT-06</td>
<td>Day 7</td>
<td>nessuna</td>
<td>`tsp_genetic_algorithm_with_...` a schermo, non nel materiale</td>
</tr>
<tr>
<td>nessuna</td>
<td>Day 8</td>
<td>nessuna</td>
<td>traccia del test</td>
</tr>
</table>
### Registrazioni Teams 2026
<table header-row="true">
<tr>
<td>Registrazione</td>
<td>Data</td>
<td>Contenuto</td>
<td>Capitolo</td>
</tr>
<tr>
<td>`Teams 1`</td>
<td>18/05/2026</td>
<td>introduzione, ODE, quattro casi di studio, esame</td>
<td>00</td>
</tr>
<tr>
<td>`Teams 2`</td>
<td>19/05/2026</td>
<td>notebook `01`-`04`, Mathematics in Biology</td>
<td>01</td>
</tr>
<tr>
<td>`Teams 3`</td>
<td>20/05/2026</td>
<td>Colab LV, SIR, zombie, SALib (fino a 0:31); agenti da 0:53:55. Trascrizione Stream interrotta a 0:57:51 su 2:43:33</td>
<td>01 (13.6), 02</td>
</tr>
<tr>
<td>`Teams 4`</td>
<td>21/05/2026</td>
<td>sistemi complessi, TDA, Kuramoto ad agenti</td>
<td>03</td>
</tr>
<tr>
<td>`Teams 5`</td>
<td>22/05/2026</td>
<td>seminario di un ospite: simulatore ad agenti per sistemi ecologici (annunciato a `Teams 4 @ 2:12:33`)</td>
<td>02 (contesto)</td>
</tr>
<tr>
<td>`Teams 6`</td>
<td>25/05/2026</td>
<td>epidemiologia, esame</td>
<td>04, Assessment</td>
</tr>
</table>
## Capitolo 00
- Nessuna registrazione 2025 (Day 1). Capitolo costruito da `Teams 1` (riassunto) e dalle slide 2025 e 2026, che hanno contenuti diversi.
- Programma 2025 (slide `Day1_v25`) diverso dall'ordine delle lezioni registrate.
- Correzioni: spettrometria di massa descritta come analisi nell'infrarosso (`Teams 1 @ 0:14:47`); metodi multistep "adattativi" e impliciti "per minimi e massimi locali" (`Teams 1 @ 0:56:38`), contro la slide che dice "problemi stiff".
## Capitolo 01
### Mappatura
- Registrazione `BT-01` = Day 2 "Mathematics in Biology" (titolo della slide). Slide: `Math_in_biology.pdf` (portale e Teams, file identici, creati il 20/11/2025).
- Notebook a schermo: `Lotka-Volterra.ipynb` (Colab, link `drive/1N_vx-iIR5705...`) e `Zombie_invasion.ipynb` ("Data ultima modifica: 8 novembre"). Nel materiale Teams: `Lotka_Volterra.ipynb` e `Zombie_invasion.ipynb`.
### Notebook `Lotka_Volterra.ipynb`: il file di Teams è una versione successiva
Caso (a): stesso file, versione diversa. Le funzioni (`euler`, `first`, `derivative`, `Euler`) e il codice di plotting coincidono; i valori dei parametri no. I valori del file di Teams non riproducono nessuno dei grafici mostrati a lezione, e un commento rimasto invariato ("conterrà 1000 campionamenti" con `Nt = 10000`) indica una modifica successiva. **Nel manuale: funzioni dal notebook, parametri dal video.** Scelta confermata.
<table header-row="true">
<tr>
<td>Cella</td>
<td>Video (`BT-01`)</td>
<td>Notebook Teams</td>
</tr>
<tr>
<td>Configurazione di `first`</td>
<td>`dt = 0.1`, `n = 100`; `alpha = 0.1`, `y0 = 1` dedotti dal grafico (cella non inquadrata per intero) @ 01:03:48</td>
<td>`dt = 0.8`, `alpha = 160`, `y0 = 20` (la `print(y)` salvata arriva a 3.3e43)</td>
</tr>
<tr>
<td>Confronto di `alpha`</td>
<td>`alpha = 0.1`, `y0 = 1`, curve `y`, `y2`, `y3` @ 01:03:49</td>
<td>`alpha = 0.00000000010`, `y0 = 0.1`, `dt = 0.01`, curva aggiuntiva `y6` con `alpha + 0.9`</td>
</tr>
<tr>
<td>Impostazioni LV</td>
<td>`alpha = 1.`, `x0 = 4.`, `y0 = 2.` @ 01:11:19</td>
<td>`alpha = 2`, `x0 = 10.`, `y0 = 10.`</td>
</tr>
<tr>
<td>`odeint` LV</td>
<td>`Nt = 1000` @ 01:11:28</td>
<td>`Nt = 10000` (commento invariato: "conterrà 1000 campionamenti")</td>
</tr>
<tr>
<td>Effetto di beta</td>
<td>`np.arange(0.9, 1.4, 0.1)` @ 01:13:11</td>
<td>`np.arange(0.9, 1.9, 0.1)`</td>
</tr>
<tr>
<td>Ritratto di fase</td>
<td>`np.linspace(1.0, 6.0, 21)` @ 01:14:03</td>
<td>`np.linspace(1.0, 1.9, 25)`</td>
</tr>
<tr>
<td>Celle vuote</td>
<td>nessuna a schermo</td>
<td>due celle di codice vuote (indici 1 e 15)</td>
</tr>
</table>
Nome del file: a schermo `Lotka-Volterra.ipynb`, su Teams `Lotka_Volterra.ipynb`.
### Notebook `Zombie_invasion.ipynb`
Coincide con quello a schermo. Differenza di stato: a lezione la cella SALib fallisce con `ModuleNotFoundError: No module named 'SALib'` (@ 01:26:50) perché `!pip install SALib` non era stato eseguito; il file di Teams contiene l'output riuscito (S1 = 0.3168, 0.4438, 0.0122), coerente con la verifica per esecuzione.
### Slide contro video e codice
1. **Slide "Euler method in python" (@ 00:57:24):** codice con `a = 1`, grafico con `a = 0.1`. Verificato: `a = 1` → y(10) ≈ 13 781; `a = 0.1` → y(10) ≈ 2.705 (curva della slide). A voce il docente dice `a = 1`. Riquadro **Correzione** nel manuale, sezione 5.
2. **Slide "Let's code Lotka-Volterra!" (@ 01:10:47):** il grafico "odeint method" (lepri fino a circa 4.8, linci fino a circa 3.7) non corrisponde a `beta = 1` (massimi 4.40 e 4.40) ma a `beta = 1.3` (massimi verificati 4.83 e 3.72): probabilmente prodotto dopo il ciclo su `betas`, che lascia `beta = 1.3` (vedi punto 3). Non riportato nel manuale come correzione, solo descritto senza valori.
3. **Stato globale del notebook:** il ciclo `for beta, i in zip(betas, ...)` lascia `beta = 1.3`; il ciclo del ritratto di fase lascia `X0 = [6.0, 1.0]`. Il ritratto di fase e la soluzione con Eulero a schermo sono calcolati con questi valori, non con quelli delle impostazioni. Verificato: con `beta = 1.3` e partenza (6, 1) Eulero dà massimi lepri 7.11, 8.60 e linci 4.83, 5.73, 6.96, come a schermo (@ 01:15:11); con `beta = 1` i massimi delle linci sarebbero 6.26, 7.42, 8.99. **Nota aggiunta** nel manuale, sezioni 6.3 e 6.4.
### Affermazioni del docente corrette nel manuale
<table header-row="true">
<tr>
<td>Dove</td>
<td>Detto</td>
<td>Correzione</td>
</tr>
<tr>
<td>`BT-01 @ 00:09:54`</td>
<td>le conchiglie seguono la formula aurea</td>
<td>spirale logaritmica sì, rapporto aureo no in generale</td>
</tr>
<tr>
<td>`BT-01 @ 00:11:01`</td>
<td>"premio Nobel per l'intelligenza artificiale" a Hopfield</td>
<td>Nobel per la Fisica 2024 (Hopfield e Hinton)</td>
</tr>
<tr>
<td>`BT-01 @ 00:31:09`</td>
<td>osteoblasti, osteoclasti e osteoni "rispettivamente" erodono, depongono, calcificano</td>
<td>gli osteoclasti riassorbono, gli osteoblasti depongono; l'osteone è un'unità strutturale, non una cellula</td>
</tr>
<tr>
<td>`BT-01 @ 01:15:02`</td>
<td>anche la soluzione con Eulero è "un sistema chiuso"</td>
<td>spirale che si allarga: errore numerico di Eulero esplicito (invariante da 5.51 a 8.84, con `odeint` costante)</td>
</tr>
<tr>
<td>`BT-01 @ 01:23:55`</td>
<td>esposti del SEIR = sani che a contatto con un malato non per forza si ammalano</td>
<td>E = infettati in latenza, non ancora contagiosi</td>
</tr>
<tr>
<td>`BT-01 @ 01:25:09`</td>
<td>nel modello zombie il terzo compartimento "ritorna sano"</td>
<td>R = rimossi (morti e zombie distrutti), ζR li fa risorgere come zombie</td>
</tr>
<tr>
<td>notebook LV</td>
<td>`alpha #mortality rate due to predators`</td>
<td>`alpha` è il tasso di crescita delle prede (lo dice anche il docente a voce)</td>
</tr>
<tr>
<td>notebook LV</td>
<td>`#odeint metodo di derivazione di shipy`</td>
<td>`odeint` integra; la libreria è SciPy</td>
</tr>
</table>
### Verifica per esecuzione
Script `verifica_bt01.py` (numpy 2.4.4, scipy 1.17.1, SALib da PyPI). Nessun blocco di codice del manuale è stato trascritto dai frame senza riscontro nel notebook, tranne:
- esempio `pend` della documentazione SciPy (letto dai frame @ 00:53:26 e @ 00:53:58);
- codice della slide Eulero (letto dal frame @ 00:56:41 e @ 00:57:24), identico nella logica alla funzione del notebook.
- valori dei parametri delle celle del `Lotka-Volterra.ipynb` che differiscono dal file di Teams (letti dai frame, vedi tabella sopra).
Tutti gli esempi numerici citati nel manuale (Eulero su a·y, massimi e picchi del LV, invariante, zombie, indici di Sobol, numero di campioni di Saltelli) sono stati ricalcolati.
### Da riguardare
- Nomi incerti: progetto europeo sul diabete (@ 00:08:44), ricercatori di neuroscienze (@ 00:10:24), autori del 1991 sulla striscia primitiva (@ 00:33:37).
- Slide "Visual System" (@ 00:37:24) e "Embryo Development" (@ 00:34:40): immagini non trascritte, testo dalla slide PDF.
### Integrazioni Teams 2026
- Il `Lotka_Volterra.ipynb` di Teams è la versione 2026: i valori `alpha = 160`, `dt = 0.8`, `y0 = 20` vengono dalla prova in diretta di `Teams 2 @ 1:38:51` (alpha 0.8, 1.6, 160).
- Notebook `01`-`04` (edizione 2026), eseguiti: 01 errore 43.20%, logistica a 1.00e9; 02 errori finali non monotoni (metrica all'ultimo istante, soluzioni a regime 9.05 g/L), errore massimo monotono; 03 `np.trapz` rimosso in NumPy recenti; 04 prodotto 8.012 g/L, volume 1.960 L, ottimo di induzione al bordo della griglia (6 h; 4 h e 2 h danno di più), Eulero viola il bilancio di massa per il clipping con `np.maximum`.
- Markdown dei notebook 02 e 03: `\frac` reso come "rac" (backslash interpretato come escape), formule illeggibili nel rendering.
- Correzioni `Teams 2`: errore di Eulero che crescerebbe con passi fitti (`0:17:52`, `1:29:11`); volume "proporzionale a biomassa e prodotto" (`0:41:01`); ottimo a 6 h letto come inizio del feed (`0:41:30`); parametri c e p del Lotka-Volterra invertiti (`1:42:23`).
- Confermato il nome del progetto Presidium (`Teams 2 @ 1:25:08`).
- `Teams 3 @ 0:00:02`-`0:31:28`: Colab di LV, SIR, zombie ODE e SALib, sezione 13.6. Correzioni: SALib descritto come "metodi bayesiani" (`0:20:38`); variabile più importante definita al contrario (`0:24:50`). $`x_1`$ è la prima per indice totale, non per indice del primo ordine. $`R_0`$ trascritto "B per K" \[?\] (`0:14:51`).
## Capitolo 02
### Video e file del portale
- **Segmento duplicato:** `BT-02 @ 00:20:05`-`00:25:05` ripete l'inizio di `BT-01` (slide "Mathematics in Biology, Day 2" a schermo a `00:24:58`). Errore di montaggio del file del portale, escluso dal capitolo.
- `Money_ABMS.ipynb`, il notebook usato in video, **non è tra i materiali**: codice trascritto dai fotogrammi. Nome e contenuto non coincidono (è un preda-predatore, non un modello di scambio di denaro).
- `Zombie_ABMS.ipynb` a schermo corrisponde a `Zombie_ABMS_lezione_3_Biotech.ipynb` di Teams nelle parti inquadrate.
### Slide
- `ABMS.pdf` è solo sul canale Teams (cartella "III lezione"). Diverse slide sono immagini (Agent types, Agent Model 2/2, Environment, Agent interaction, Development & Use, Applications, MESA): lette dai fotogrammi.
- A voce il docente cita la logica fuzzy tra gli ingredienti del comportamento; la slide non la elenca.
### Codice: 2025 (video) contro 2026 (Teams)
<table header-row="true">
<tr>
<td>Aspetto</td>
<td>`Money_ABMS.ipynb` (video 2025)</td>
<td>`Biotech_LEZIONE3.ipynb` (Teams 2026)</td>
</tr>
<tr>
<td>Preda</td>
<td>energia che cala di 1 per tick, mai reintegrata; riproduzione con probabilità 0.04</td>
<td>nessuna energia; riproduzione deterministica ogni 2 tick; muore solo se mangiata</td>
</tr>
<tr>
<td>Predatore</td>
<td>energia, +20 per preda mangiata; riproduzione con probabilità 0.02</td>
<td>muore dopo 20 tick senza mangiare; si riproduce in base al numero cumulato di prede mangiate</td>
</tr>
<tr>
<td>Griglia</td>
<td>20×20 toroidale</td>
<td>100×100 toroidale</td>
</tr>
<tr>
<td>Iniziali</td>
<td>50 prede, 20 predatori</td>
<td>10 prede, 30 predatori</td>
</tr>
<tr>
<td>Esecuzione</td>
<td>200 tick e grafico</td>
<td>10 tick, stampa del DataFrame, nessun grafico</td>
</tr>
<tr>
<td>Esito verificato</td>
<td>estinzione di entrambe le specie in tutti i run</td>
<td>crescita esponenziale delle prede, poi esplosione dei predatori</td>
</tr>
</table>
### Affermazioni del docente corrette nel manuale
- `possible_steps` descritto come lista delle celle libere: contiene tutte le celle del vicinato (`BT-02 @ 01:20:09`).
- Riproduzione "se l'energia è maggiore di un numero random": probabilità fissa, indipendente dall'energia (`BT-02 @ 01:20:40`).
- Crollo delle prede attribuito alla predazione: le prede muoiono soprattutto di fame, perché non si nutrono; si estinguono anche senza predatori (verificato, `BT-02 @ 01:25:44`).
- ODD attribuito a "un tale Green": Volker Grimm (`BT-02 @ 01:08:25`).
- Zombie ABM: "numero dei guariti" e parametri "tasso di contagio, velocità, resistenza" non esistono nel codice (`BT-02 @ 01:30:13`, `01:31:20`).
### Note aggiunte
- Aneddoto delle formiche di Feynman: il raddrizzamento della pista è un effetto collettivo, non di una singola formica.
- Dengue: il rischio di forma grave è legato alla seconda infezione con un sierotipo diverso.
- MESA 3.x incompatibile con il codice del corso (niente `RandomActivation`, niente `unique_id` nel costruttore).
- `Biotech_LEZIONE3.ipynb`: `prey_reproduce` inutilizzato; con `eat_repr=1` il predatore si riproduce a ogni tick dopo il primo pasto; `update()` non disegna.
- Zombie: `bins=0` possibile nell'istogramma, `range(80, 10)` vuoto, GIF per un solo seed.
### Teams 2026
- `Teams 3`: la parte sugli agenti inizia a `0:53:55`, ma la trascrizione Stream si interrompe a `0:57:51` su 2:43:33. Nei quattro minuti disponibili: stessa introduzione del 2025, con la precisazione che l'ABM non va confuso con gli "agenti" dell'IA di cui si parla oggi.
### Verifica per esecuzione
Script `verifica_bt02.py` (`mesa==0.9.0`, NumPy 2.4, pandas 3.0): 50 run del preda-predatore del video (anche senza predatori), 22 tick del notebook 2026, 100 run dello zombie ABM.
## Capitolo 03
### Notebook
- A schermo `MESA_VICSEK.ipynb` e `mapper_tda_tutorial.ipynb` (KeplerMapper su Iris): **non tra i materiali**. Il primo coincide nel codice con `MESA_VICSEK_persistent_entropy_final.ipynb`; il secondo è trascritto dai fotogrammi (`BT-03 @ 00:58:31`-`00:59:46`), import in parte non inquadrati.
- Parametri cambiati in diretta: `MESA_KURAMOTO` K = 1.0 poi 0.5 (file Teams 0.5); `MESA_KURAMOTO_persistent_entropy_persim` K = 1.5 poi un valore non inquadrato (file Teams 0.5); Vicsek scatola 50×50 in `MESA_VICSEK`, 100×100 nella versione con entropia (file Teams 100×100).
- `Jerne.ipynb` di Teams non contiene il calcolo dell'entropia persistente mostrato nel 2026 (`Teams 4 @ 1:57:30`).
### Affermazioni del docente corrette nel manuale
- Kuramoto: "con K troppo grande il sistema non si sincronizza" (`BT-03 @ 00:27:53`): artefatto del passo di Eulero con Δt = 1; con Δt = 0.05 r → 1 (verificato).
- Vicsek: "forze attrattive e repulsive", "calamite" (slide, `BT-03 @ 00:29:46`, `Teams 4 @ 0:34:52`): il codice fa solo allineamento delle velocità con rumore; r misura l'allineamento, non il raggruppamento.
- Vicsek: `r = norm(avg_velocity) / N` divide due volte per N; valori a schermo fra 0.0005 e 0.0028.
- Mapper 2025: descrizione senza il passo di clustering (`BT-03 @ 00:52:04`); Mapper 2026: filtro "distanza dal centro" (`Teams 4 @ 1:16:20`), nel codice proiezione sugli assi.
- Vietoris-Rips descritto con la regola del complesso di Čech (`BT-03 @ 01:06:36`, `Teams 4 @ 1:34:02`).
- Jerne 2026: "non serve una griglia spaziale" (`Teams 4 @ 1:47:12`): nel codice si interagisce solo nella stessa cella.
### Note aggiunte
- Kuramoto: aggiornamento sequenziale dentro `SimultaneousActivation` (advance vuoto); r di regime 0.87 contro 0.97 con aggiornamento simultaneo.
- Entropia su Kuramoto: `ripser` senza `distance_matrix=True`; fasi non ridotte modulo 2π, con distanza circolare l'entropia H0 resta attorno a 4.17.
- Vicsek: distanze euclidee piatte su griglia toroidale.
- Jerne: affinità massima per idiotipi uguali, antigeni immortali e statici, soppressione dominante, nessun anticorpo supera la concentrazione iniziale.
- Iris: Mapper separa setosa da versicolor + virginica (36 nodi e 92 archi come a schermo).
- β0 conta le componenti connesse; entropia persistente: riferimenti in letteratura, persim scarta le barre infinite.
### Verifica per esecuzione
Script `verifica_bt03.py` (MESA 0.9, ripser 0.6.15, persim 0.3.8, KeplerMapper 2.1) e `verifica_mapper_giotto.py` (giotto-tda 0.6.2, numpy 1.26).
## Capitolo 04
### Materiale
- Nessun PDF delle slide di epidemiologia né sul portale né su Teams: testo e formule dai fotogrammi.
- `SIR_ABMS.ipynb` e `SIR_Network.ipynb` coincidono con quelli a schermo. `Epidemiology.ipynb` (SIR della "Freshman Plague", odeint ed Eulero) non è mostrato né nel 2025 né nel 2026.
- `SIR_Network.ipynb` con `EoN` 2.0 va in errore su `transmission_weight`; funziona con `EoN==1.2`.
### Slide
- Formula del picco: $`I(t)\cdot[\beta S(t) - \gamma]`$ al posto di $`I(t)\cdot[1 + \beta S(t) - \gamma]`$.
- Esercizio in tabella senza condizioni iniziali; con i valori dati ($`\beta N = 0.30`$, $`\gamma = 0.80`$) non c'è picco (verificato).
### Affermazioni del docente corrette nel manuale
- Variolazione come "diffusione del variolo" (`BT-04 @ 00:20:00`, `Teams 6 @ 0:22:54`).
- Ross: scoperta del vettore nel 1911 invece che nel 1897; "popolazione della malaria" invece che delle zanzare (`BT-04 @ 00:21:17`).
- "$`R_0`$ scende sotto 1" con l'immunità: è $`R_t`$ (`BT-04 @ 00:50:27`).
- SIR_ABMS: età "media 30 fra 20 e 40" (è `normalvariate(20, 40)`); celle "libere" e contagio "fra celle vicine" (è la stessa cella); "tutti recuperati" (muore circa un terzo degli infetti); "0,01 per cento" di mortalità (è l'1% per step).
- EoN 2026: "$`R_0`$ = $`I_0/N`$" (è la frazione iniziale di infetti, `Teams 6 @ 0:56:41`).
- "Neumann/von Neumann e Brouwer/Brower": Newman (2003) e Brauer (2008).
### Note aggiunte
- Derivazione di $`\beta = 2\alpha/(N-1)`$; significato di $`k`$, $`\beta`$, $`\mu`$; Google Flu Trends chiuso nel 2015; agenti morti che restano sulla griglia e variabile globale `model` in SIR_ABMS; `tau` di EoN come tasso per arco; dettagli di `Epidemiology.ipynb`.
### Teams 2026
- `Teams 6` (25/05) fino a `0:57:41`: stessi contenuti, con aggiunte su COVID-19, limiti del SIR, trasmissione indiretta, SIR nei sistemi isolati, strumenti e pipeline di analisi, grafi e matrice di adiacenza (sezione 10).
### Verifica per esecuzione
Script `verifica_bt04.py` (MESA 0.9, SciPy) e `verifica_bt04_network.py` (EoN 1.2, numpy 1.26).
## Capitolo 05
### Materiale
- Nessun PDF delle slide di bioinformatica e nessun notebook `Genome.ipynb` fra i materiali: slide, pagine NCBI/BLAST e codice ricostruiti dai fotogrammi.
- `Genome.ipynb` è la traduzione italiana di un tutorial pubblico su pandas e annotazione del genoma (GFF3 Ensembl release 85, GRCh38). Il GFF3 non è scaricabile dall'ambiente di lavoro: codice eseguito su righe sintetiche, numeri dell'output letti a schermo. URL del `wget` tagliato a schermo.
### Slide e documenti a schermo
- Esercizio k-mer: elencati 12 2-mer invece di 14 (mancano `AG` e `GA`).
- Slide UniProt: "quasi 600.000 proteine" riferito a UniProtKB/Swiss-Prot, grafico fermo al 2015.
### Affermazioni del docente corrette nel manuale
- Cas9 "rilasciata" dalla guide RNA: formano un unico complesso (`BT-05 @ 00:25:02`).
- Allineamento globale descritto prima come quello con i gap, poi come quello che richiede il match esatto (`BT-05 @ 00:36:55`, `00:37:26`).
- "Nobel per l'intelligenza artificiale" a "un chimico computazionale di Google", AlphaFold con reinforcement learning: Nobel per la Chimica 2024 a Baker, Hassabis e Jumper; AlphaFold è deep learning supervisionato e parte dalla sequenza di amminoacidi (`BT-05 @ 00:39:42`).
- "UniProt e GenBank raffinamenti di NCBI": GenBank è la primaria di NCBI, RefSeq la secondaria; UniProt è di un altro consorzio (`BT-05 @ 00:46:38`).
- Co-occorrenza di C e G come "indice di qualità": proprietà composizionale (GC, CpG); la qualità si misura con i punteggi Phred (`BT-05 @ 01:01:10`).
- E-value come "probabilità": è il numero atteso di match casuali (`BT-05 @ 01:09:36`).
- "Genoma mappato per circa il 37%": il notebook dice 0,37% incompleto (`BT-05 @ 01:24:55`).
### Note aggiunte
- `__contains__` e operatore `in`; minuscole come soft-masking e codici IUPAC; traduzione deterministica e uso reale degli HMM; classifica BLAST a schermo (secondo *Theropithecus gelada*, gorilla più in basso); scaffold KI/GL; `-` contro `~`; `import matplotlib as plt`; nomi di geni ripetuti come geni distinti; `.ix` nel testo del notebook; `SettingWithCopyWarning` assente con pandas 3.0; 42.470 geni del file contro circa 20.000 codificanti; eredità materna del DNA mitocondriale.
### Punti non verificati
- Limite di 10.000 nucleotidi di BLAST online; frase sulla modifica di Indy per "dimezzare il ciclo di vita".
### Teams 2026
- Nessuna registrazione 2026 copre la bioinformatica; il test finale 2026 non ha domande su questo tema.
### Verifica per esecuzione
Script `verifica_bt05.py` (pandas 3.0): k-mer, frazione non assemblata dalle lunghezze GRCh38 a schermo, pipeline del notebook su GFF3 sintetico.
## Capitolo 06
### Materiale
- Nessun PDF delle slide e nessun notebook `tsp_genetic_algorithm_with_comments.ipynb` fra i materiali: slide e codice dai fotogrammi. Le celle di selezione, crossover e mutazione, a schermo per pochi secondi, sono lette da fotogrammi estratti dal video (`00:58:48`, `00:59:12`, `00:59:24`).
- La lettura della traccia del test annunciata a fine lezione non è nella registrazione.
### Slide
- Due slide consecutive intitolate "Quando usare GA": la seconda è "quando non usarli" (lo segnala il docente).
- "Finonacci" per Fibonacci; "Termine ottmizzazione".
### Codice
- `best_path` preso dalla popolazione nuova con l'indice delle fitness della vecchia: il percorso stampato `[4 8 3 0 7 9 5 1 2 6]` è lungo 5.71, non 4.10 (verificato).
- Nessun elitismo: la miglior distanza oscilla e la soluzione migliore si perde; con un individuo elitario il GA termina sull'ottimo esatto 2.903 (forza bruta sulle 10 città).
- Modulo `random` senza seed: risultati non riproducibili. `mutation_rate` del ciclo non usata.
### Affermazioni del docente corrette nel manuale
- "NP" come "non polinomiali" (`BT-06 @ 00:05:52`).
- Simulated annealing "implementato attraverso il quantum computing" (`BT-06 @ 00:08:19`).
- Roulette "russa o francese" con 37 o 38 caselle: europea 37, americana 38 (`BT-06 @ 00:26:29`).
- Fitness "proporzionale alla lunghezza" con percorsi brevi a fitness più alta: inversamente proporzionale (`BT-06 @ 00:35:12`).
- "Miglior percorso alla generazione 180, dove ci siamo arrestati": il ciclo fa 200 generazioni e il risultato non è il migliore (`BT-06 @ 00:59:28`).
### Note aggiunte
- Elitismo con pochi individui; TPOT (programmazione genetica, fitness in cross-validation); numero di giri del TSP $`(n-1)!/2`$; seed di `random` e correzione minima del `best_path`.
### Punti non verificati
- Articolo 2008-2009 sulla campagna di Obama pianificata con algoritmi genetici "nei 49 stati".
### Teams 2026
- Nessuna registrazione 2026 copre gli algoritmi genetici; il test finale 2026 non ha domande su questo tema.
### Verifica per esecuzione
Script `verifica_bt06.py` (NumPy 2.4): codice del notebook, forza bruta sulle 10 città, cinque esecuzioni con e senza elitismo.
