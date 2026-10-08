# 02 - Probabilità condizionata

> Fonte Notion: https://app.notion.com/p/3c612abc808d81feb0acd4e83963bc4f — ultima modifica 2026-08-25T23:02:21.001Z

<table_of_contents color="gray"/>
Cosa succede alla probabilità quando **ricevi un'informazione**. Esempio della lezione: il mese di nascita di uno sconosciuto.
<callout icon="📅" color="blue_bg">
	**L'esempio di riferimento.** Incontri una persona di cui non sai nulla e ti chiedi in che mese è nata. Lo spazio campionario è $`\Omega`$ = i 12 mesi, considerati equiprobabili: $`P(\text{un mese specifico}) = 1/12`$.
</callout>
---
## I due eventi della lezione
<table fit-page-width="true" header-row="true">
<tr>
<td>Evento</td>
<td>Definizione</td>
<td>Quali mesi</td>
<td>Quanti</td>
</tr>
<tr>
<td>$`L`$</td>
<td>Mesi **lunghi**, cioè da 31 giorni</td>
<td>Jan, Mar, May, Jul, Aug, Oct, Dec</td>
<td>**7**</td>
</tr>
<tr>
<td>$`r`$</td>
<td>Mesi il cui nome contiene la lettera **r**</td>
<td>Jan, Feb, Mar, Apr, Sep, Oct, Nov, Dec</td>
<td>**8**</td>
</tr>
</table>
Da cui le probabilità di partenza:
$$
P(L) = \tfrac{7}{12} \qquad P(r) = \tfrac{8}{12}
$$
**L'intersezione** — i mesi che sono *sia* lunghi *sia* con la r — sono quattro: **Jan, Mar, Oct, Dec**.
Si ottengono partendo dai sette lunghi e togliendo quelli senza la r: *May*, *July* e *August*. Restano quattro.
$$
P(L \cap r) = \tfrac{4}{12} = \tfrac{1}{3}
$$
<callout icon="⚠️" color="yellow_bg">
	**\[integrazione\] Attenzione: la "r" vale sui nomi INGLESI.**
	È il punto in cui ci si incastra: contando in italiano l'intersezione fa **3** e non 4, perché *gennaio* non ha la r mentre *January* sì. Rimarrebbero solo marzo, ottobre e dicembre, e tutti i numeri della pagina cambierebbero.
	Sugli appunti del docente i mesi sono scritti in inglese: è quella la lista giusta.
</callout>
### Il conto, in una tabella
Incrociando le due proprietà si leggono in un colpo solo tutti i numeri di questa pagina:
<table fit-page-width="true" header-row="true">
<tr>
<td></td>
<td>con la **r**</td>
<td>senza r</td>
<td>totale</td>
</tr>
<tr>
<td>**lunghi** (31 giorni)</td>
<td>**4**</td>
<td>3</td>
<td>**7** = $`|L|`$</td>
</tr>
<tr>
<td>corti</td>
<td>4</td>
<td>1</td>
<td>5</td>
</tr>
<tr>
<td>totale</td>
<td>**8** = $`|r|`$</td>
<td>4</td>
<td>**12**</td>
</tr>
</table>
La casella in alto a sinistra è $`L \cap r`$: **4**. Le quattro caselle interne sommano a 12, come devono.
> L'unica casella con **1** è *June*: né lungo né con la r. È lo stesso mese che più avanti spiega perché $`P(L \cup r) = 11/12`$.
<details>
<summary>I dodici mesi uno per uno, se vuoi ricontare</summary>
	<table fit-page-width="true" header-row="true">
<tr>
<td>Mese</td>
<td>Giorni</td>
<td>Ha la r</td>
<td>Sta in $`L \cap r`$</td>
</tr>
<tr>
<td>**January**</td>
<td>**31**</td>
<td>**sì**</td>
<td>**✓**</td>
</tr>
<tr>
<td>February</td>
<td>28</td>
<td>sì</td>
<td></td>
</tr>
<tr>
<td>**March**</td>
<td>**31**</td>
<td>**sì**</td>
<td>**✓**</td>
</tr>
<tr>
<td>April</td>
<td>30</td>
<td>sì</td>
<td></td>
</tr>
<tr>
<td>May</td>
<td>31</td>
<td>no</td>
<td></td>
</tr>
<tr>
<td>June</td>
<td>30</td>
<td>no</td>
<td></td>
</tr>
<tr>
<td>July</td>
<td>31</td>
<td>no</td>
<td></td>
</tr>
<tr>
<td>August</td>
<td>31</td>
<td>no</td>
<td></td>
</tr>
<tr>
<td>September</td>
<td>30</td>
<td>sì</td>
<td></td>
</tr>
<tr>
<td>**October**</td>
<td>**31**</td>
<td>**sì**</td>
<td>**✓**</td>
</tr>
<tr>
<td>November</td>
<td>30</td>
<td>sì</td>
<td></td>
</tr>
<tr>
<td>**December**</td>
<td>**31**</td>
<td>**sì**</td>
<td>**✓**</td>
</tr>
	</table>
	Sette righe con 31 giorni, otto con la r, quattro con entrambe.
</details>
---
## Le due domande da non confondere
Sono domande diverse e danno numeri diversi.
<table fit-page-width="true" header-row="true">
<tr>
<td>Domanda</td>
<td>Si scrive</td>
<td>Vale</td>
</tr>
<tr>
<td>"È nato in un mese lungo **e** con la r?"</td>
<td>$`P(L \cap r)`$</td>
<td>$`4/12 \approx 33\%`$</td>
</tr>
<tr>
<td>"**So già** che è nato in un mese lungo: ha la r?"</td>
<td>$`P(r \mid L)`$</td>
<td>$`4/7 \approx 57\%`$</td>
</tr>
</table>
Nella prima non sai nulla e chiedi che si verifichino entrambe le condizioni. Nella seconda una condizione è già data per certa, e chiedi solo dell'altra.
---
## Condizionare = restringere il campo
Questa è tutta l'idea. **"Dato **$`L`$**" significa che qualcuno ti ha già detto qualcosa, e tu butti via tutto il resto.**
Prima non sai niente: i mesi possibili sono 12. Poi ti dicono "è nato in un mese lungo": da quel momento gli altri cinque mesi smettono di esistere. Restano 7 candidati, e fra questi conti quanti hanno la r.
![](notion-file-block://c7abbb23-01be-4ce8-ac27-1f19c6ffd5e1/349b9246-0cbc-4364-be5d-df34716c2a62?space_id=98012abc-808d-816f-9733-00030a2b4817&name=condizionata-mesi.svg)
Quattro sì su sette candidati:
$$
P(r \mid L) = \tfrac{4}{7} \approx 57\%
$$
Non serve altro per capirlo. La formula è solo il modo di ottenere questo conto senza rifare l'elenco a mano:
$$
P(r \mid L) = \frac{P(r \cap L)}{P(L)} = \frac{4/12}{7/12} = \frac{4}{7}
$$
### Perché quella divisione, passo per passo
I due pezzi sopra e sotto la linea sono **due conteggi, misurati entrambi sui 12 mesi**:
<table fit-page-width="true" header-row="true">
<tr>
<td>Pezzo</td>
<td>Cosa conta</td>
<td>Valore</td>
</tr>
<tr>
<td>sopra: $`P(r \cap L)`$</td>
<td>i mesi buoni — lunghi **e** con la r</td>
<td>4 su 12</td>
</tr>
<tr>
<td>sotto: $`P(L)`$</td>
<td>il mondo ristretto — quanti mesi restano in gioco</td>
<td>7 su 12</td>
</tr>
</table>
Dividendoli, i dodicesimi si semplificano:
$$
\frac{4/12}{7/12} \;=\; \frac{4}{12} \times \frac{12}{7} \;=\; \frac{4}{7}
$$
<callout icon="💡" color="blue_bg">
	**È un cambio di unità di misura.** Entrambi i numeri erano espressi in *dodicesimi*; la divisione li riconverte in *settimi*.
	Il numeratore non cambia mai — restano sempre quei quattro mesi. Cambia solo **su quanti li stai rapportando**: prima su 12, dopo su 7.
</callout>
**La prova che funziona:** dentro il mondo ristretto le probabilità devono tornare a sommare a 1.
$$
P(r \mid L) + P(\bar{r} \mid L) = \tfrac{4}{7} + \tfrac{3}{7} = 1 \qquad\text{✓}
$$
Senza dividere avresti $`4/12 + 3/12 = 7/12`$: non fa 1, quindi non è una probabilità valida — è solo un pezzo di quella vecchia.
---
## Come si legge la notazione
La barra si legge "**dato**", e ciò che la segue è l'informazione che possiedi già.
$$
P(\underbrace{r}_{\text{cosa chiedo}} \mid \underbrace{L}_{\text{cosa so}})
$$
- **a destra della barra** → la condizione già verificata: è la `WHERE`, il filtro
- **a sinistra** → ciò che stai contando dentro quel filtro
<callout icon="🚨" color="red_bg">
	**L'ordine non è scambiabile.** Invertire i due termini cambia il denominatore, quindi cambia la risposta:
	- $`P(r \mid L) = 4/7 \approx 57\%`$ — so che è lungo, mi chiedo se ha la r
	- $`P(L \mid r) = 4/8 = 50\%`$ — so che ha la r, mi chiedo se è lungo
	Stesso numeratore (sempre quei 4 mesi), risposte diverse.
</callout>
<details>
<summary>\[integrazione\] Perché questo scambio è l'errore più costoso della statistica</summary>
	Scambiare i due lati della barra sembra un dettaglio formale, ma nelle applicazioni cambia tutto.
	"Il 99% dei malati risulta positivo al test" è $`P(\text{positivo} \mid \text{malato})`$. **Non** significa che il 99% dei positivi sia malato, che sarebbe $`P(\text{malato} \mid \text{positivo})`$.
	Se la malattia è rara, il secondo numero può essere bassissimo — anche sotto il 10% — perché i sani sono così tanti che i loro pochi falsi positivi superano di gran lunga i malati veri. È lo stesso meccanismo dei 12 mesi che diventano 7: cambia il denominatore, cambia la risposta.
	Il passaggio da una all'altra è esattamente ciò che fa il teorema di Bayes, ultimo blocco del corso.
</details>
---
## Verifica sul dado
Lo stesso ragionamento sull'esempio del modulo precedente. $`\Omega = \{1,2,3,4,5,6\}`$, con $`A`$ = "esce pari" e $`B`$ = "esce maggiore di 3".
- Senza informazioni: $`P(A) = 3/6 = 50\%`$
- Sapendo che è uscito un numero maggiore di 3, i candidati si riducono a $`\{4,5,6\}`$, di cui due sono pari: $`P(A \mid B) = 2/3 \approx 67\%`$
L'informazione ha **cambiato** la probabilità: sapere che il numero è alto rende più plausibile che sia pari.
---
## La probabilità dipende sempre da $`\Omega`$
Quando scrivi $`P(r)`$ stai in realtà scrivendo $`P(r \mid \Omega)`$: "la probabilità di r, **dato che siamo nel mondo** $`\Omega`$". La probabilità "assoluta" non esiste: è solo il condizionamento all'intero spazio campionario, così ovvio che si smette di scriverlo.
Cambia $`\Omega`$ e il numero cambia, pur restando lo stesso evento:
<table fit-page-width="true" header-row="true">
<tr>
<td>Se $`\Omega`$ è...</td>
<td>allora la probabilità di r vale</td>
</tr>
<tr>
<td>tutti i 12 mesi</td>
<td>$`8/12 \approx 67\%`$</td>
</tr>
<tr>
<td>i soli mesi lunghi</td>
<td>$`4/7 \approx 57\%`$</td>
</tr>
</table>
<callout icon="🎯" color="blue_bg">
	**Finché non dichiari **$`\Omega`$**, quel numero non significa niente.** Non è un dettaglio di notazione: $`\Omega`$ è il denominatore implicito di ogni probabilità che scrivi. È anche il motivo per cui vale la pena essere precisi su cos'è $`\Omega`$ fin dall'inizio.
</callout>
---
## Anatomia della formula
$$
P(r \mid L) = \frac{P(r \cap L)}{P(L)}
$$
<table fit-page-width="true" header-row="true">
<tr>
<td>Pezzo</td>
<td>Come si chiama</td>
<td>Cosa conta</td>
<td>Sui mesi</td>
</tr>
<tr>
<td>$`P(r \mid L)`$</td>
<td>Probabilità condizionata</td>
<td>Il risultato che cerchi</td>
<td>$`4/7`$</td>
</tr>
<tr>
<td>$`P(r \cap L)`$</td>
<td>Probabilità congiunta</td>
<td>I casi che soddisfano **entrambe** le condizioni</td>
<td>$`4/12`$</td>
</tr>
<tr>
<td>$`P(L)`$</td>
<td>**Fattore di normalizzazione**</td>
<td>Quanto è grande il mondo ristretto</td>
<td>$`7/12`$</td>
</tr>
</table>
> **A cosa serve normalizzare.** Dentro il mondo ristretto le probabilità devono tornare a sommare a 1. Verifica: $`P(r \mid L) = 4/7`$ e $`P(\bar{r} \mid L) = 3/7`$, somma $`= 1`$. Senza dividere per $`P(L)`$ avresti $`4/12`$ e $`3/12`$, che sommano a $`7/12`$: non è più una probabilità valida, è un pezzo di quella vecchia.
---
## Le due regole finali
<callout icon="ℹ️" color="gray">
	**\[integrazione\] Nota di notazione.** Sugli appunti compaiono $`\otimes`$ per l'AND e $`\oplus`$ per l'OR. Nei libri gli stessi due operatori si scrivono $`\cap`$ e $`\cup`$.
</callout>
### Regola del prodotto
$$
P(A \cap B) = P(A \mid B) \cdot P(B)
$$
Non è una regola nuova: è la formula del condizionamento riscritta con la moltiplicazione al posto della divisione. Si legge **in sequenza**: prima si verifica $`B`$, poi, dentro quel mondo ristretto, si verifica $`A`$.
**Sui mesi:** $`P(r \cap L) = \tfrac{4}{7} \times \tfrac{7}{12} = \tfrac{4}{12}`$ — torna con il conteggio diretto dei quattro mesi.
### Regola della somma
$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$
L'inclusione-esclusione già vista nel modulo 01: si sottrae l'intersezione perché altrimenti verrebbe contata due volte.
**Sui mesi:** $`\tfrac{8}{12} + \tfrac{7}{12} - \tfrac{4}{12} = \tfrac{11}{12}`$. Controllo diretto: l'unico mese che non è né lungo né con la r è **giugno**, quindi 11 su 12.
---
## Legge della probabilità totale
Qui la partizione del modulo 01 smette di essere una definizione e comincia a servire.
Prendi un evento $`A`$ qualsiasi e una partizione $`C_1, C_2, \dots, C_n`$ di $`\Omega`$. La partizione **taglia **$`A`$** in pezzi**, uno per cassetto:
$$
A = (A \cap C_1) \cup (A \cap C_2) \cup \dots \cup (A \cap C_n)
$$
![](notion-file-block://e469ed60-c940-466a-b92b-abadb691a0c2/b3a678e9-950a-42d6-90f9-de36a4a0822d?space_id=98012abc-808d-816f-9733-00030a2b4817&name=probabilita-totale.svg)
Le due regole della partizione sono esattamente ciò che rende il taglio pulito:
- **mutuamente esclusivi** → i pezzi non si sovrappongono, quindi le loro probabilità si possono **sommare** (assioma 3 del modulo 01)
- **esaustivi** → nessuna parte di $`A`$ resta fuori, quindi la somma ricostruisce $`A`$ per intero
Quindi:
$$
P(A) = P(A \cap C_1) + P(A \cap C_2) + \dots + P(A \cap C_n)
$$
Applicando a ciascun termine la regola del prodotto, $`P(A \cap C_i) = P(A \mid C_i) \cdot P(C_i)`$, si ottiene la **legge della probabilità totale**:
	$$
	P(A) = \sum_{i} P(A \mid C_i) \cdot P(C_i)
	$$
> **Come si legge.** Se una domanda è difficile da affrontare in blocco, la spezzi in scenari: rispondi dentro ogni scenario, dove è facile, e poi ricombini pesando ogni risposta per quanto è probabile quello scenario.
<callout icon="💡" color="gray">
	**Nota sul dado.** Sul lancio di un dado questa legge non serve: $`P(\text{esce } 5) = 1/6`$ si conta direttamente. Serve quando la risposta **dipende da uno scenario che non conosci** — come nell'esempio qui sotto.
</callout>
<details>
<summary>Esempio: il tasso di conversione di un'app</summary>
	Gli utenti arrivano da tre canali, e ogni canale converte in modo diverso.
	<table fit-page-width="true" header-row="true">
<tr>
<td>Canale $`C_i`$</td>
<td>Quota del traffico $`P(C_i)`$</td>
<td>Conversione dentro il canale $`P(A \mid C_i)`$</td>
</tr>
<tr>
<td>Ricerca organica</td>
<td>60%</td>
<td>2%</td>
</tr>
<tr>
<td>Campagna a pagamento</td>
<td>30%</td>
<td>5%</td>
</tr>
<tr>
<td>Newsletter</td>
<td>10%</td>
<td>15%</td>
</tr>
	</table>
	I tre canali sono una partizione: ogni utente arriva da uno e uno solo. Preso un utente a caso, qual è la probabilità che converta?
	$$
	P(A) = (0.60 \times 0.02) + (0.30 \times 0.05) + (0.10 \times 0.15) = 0.042
	$$
	Cioè il **4,2%**. Dentro ogni canale la domanda era banale, in blocco non lo era.
	Nota che non è la media dei tre tassi (che farebbe 7,3%): ogni canale pesa per quanto traffico porta.
	**Se le due regole saltano, il conto è sbagliato.** Se un utente potesse arrivare da due canali insieme lo conteresti due volte; se dimenticassi il traffico diretto, le quote non farebbero 100%. Quando in un report i pezzi non sommano a 1, quasi sempre è uno di questi due errori.
</details>
---
## Il teorema di Bayes
L'intersezione è simmetrica — $`A \cap B`$ e $`B \cap A`$ sono lo stesso insieme — quindi la regola del prodotto si può scrivere nei due versi:
$$
P(A \mid B) \cdot P(B) \;=\; P(A \cap B) \;=\; P(B \mid A) \cdot P(A)
$$
Isolando $`P(A \mid B)`$:
$$
P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}
$$
Questo è il **teorema di Bayes**, ricavato in una riga da ciò che c'è sulla slide. È il ponte fra i due condizionamenti asimmetrici: permette di passare da $`P(B \mid A)`$, che spesso sai calcolare, a $`P(A \mid B)`$, che di solito è quello che ti interessa davvero.
**Verifica sui mesi:**
$$
P(L \mid r) = \frac{P(r \mid L) \cdot P(L)}{P(r)} = \frac{\tfrac{4}{7} \times \tfrac{7}{12}}{\tfrac{8}{12}} = \frac{4}{8} = \tfrac{1}{2}
$$
Lo stesso numero che si ottiene contando a mano: degli 8 mesi con la r, 4 sono lunghi.
### Come si legge, pezzo per pezzo
Ogni termine ha un nome che ritroverai ovunque:
<table fit-page-width="true" header-row="true">
<tr>
<td>Pezzo</td>
<td>Nome</td>
<td>In parole</td>
</tr>
<tr>
<td>$`P(A)`$</td>
<td>**Prior** (probabilità a priori)</td>
<td>Quanto credevi in $`A`$ **prima** di vedere il dato</td>
</tr>
<tr>
<td>$`P(B \mid A)`$</td>
<td>**Verosimiglianza** (*likelihood*)</td>
<td>Quanto il dato $`B`$ è atteso **se** $`A`$ fosse vero</td>
</tr>
<tr>
<td>$`P(B)`$</td>
<td>**Evidenza** (normalizzazione)</td>
<td>Quanto il dato $`B`$ è atteso in generale, considerando tutti gli scenari</td>
</tr>
<tr>
<td>$`P(A \mid B)`$</td>
<td>**Posterior** (probabilità a posteriori)</td>
<td>Quanto credi in $`A`$ **dopo** aver visto il dato</td>
</tr>
</table>
> **In una frase: Bayes prende una convinzione iniziale e la aggiorna alla luce di un dato osservato.** A decidere se la convinzione sale o scende è il rapporto $`P(B \mid A) / P(B)`$: se il dato è più atteso sotto $`A`$ che in generale, allora $`A`$ guadagna credibilità; se è meno atteso, ne perde.
<details>
<summary>Un esempio in cui si vede il ribaltamento</summary>
	Hai due dadi in tasca: uno **normale** e uno **truccato**, che dà 5 la metà delle volte. Ne peschi uno a caso senza guardare e lo lanci: esce **5**. Quale hai in mano?
	- **Prior**: 50% e 50%, non hai motivo di preferirne uno
	- **Verosimiglianza**: $`P(5 \mid \text{normale}) = 1/6`$, $`P(5 \mid \text{truccato}) = 1/2`$
	- **Evidenza**: $`P(5) = \tfrac{1}{2} \cdot \tfrac{1}{6} + \tfrac{1}{2} \cdot \tfrac{1}{2} = \tfrac{1}{3}`$
	- **Posterior**: $`P(\text{truccato} \mid 5) = \dfrac{\tfrac{1}{2} \cdot \tfrac{1}{2}}{\tfrac{1}{3}} = \tfrac{3}{4}`$
	Un solo 5 osservato porta il dado truccato da 50% a **75%**. Nota cosa è successo: il dato non ha *deciso* la risposta, ha **spostato la fiducia**. Con un secondo 5 salirebbe ancora; con una sequenza di numeri bassi tornerebbe a scendere.
</details>
<callout icon="🔎" color="gray">
	**Perché conta più di quanto sembri.** Quasi sempre nella pratica sai calcolare $`P(\text{dato} \mid \text{ipotesi})`$ — quanto è probabile ciò che hai osservato, ammesso che una certa ipotesi sia vera. Ma la domanda che ti interessa è l'opposta: $`P(\text{ipotesi} \mid \text{dato})`$, quanto è credibile l'ipotesi visto ciò che hai osservato. Bayes è l'unico modo legittimo di passare dalla prima alla seconda, e per farlo ha bisogno del prior: senza dire cosa credevi prima, la domanda non ha risposta.
</callout>
### La forma generale, con più ipotesi in gara
Il denominatore di Bayes è $`P(A)`$, e $`P(A)`$ è proprio ciò che calcola la legge della probabilità totale. Sostituendolo si ottiene la forma che userai davvero:
$$
P(C_k \mid A) = \frac{P(A \mid C_k) \cdot P(C_k)}{\sum_{i} P(A \mid C_i) \cdot P(C_i)}
$$
La struttura è semplice da leggere:
- il **numeratore** è il contributo del cassetto $`k`$
- il **denominatore** è la somma dei contributi di **tutti** i cassetti
Quindi il risultato è la *quota* del cassetto $`k`$ sul totale. Ed è il motivo per cui le probabilità a posteriori sommano automaticamente a 1: sono fette della stessa torta.
<details>
<summary>Sull'esempio dei canali: chi ha portato le conversioni?</summary>
	Un utente **ha convertito**. Da quale canale è arrivato con più probabilità? Il denominatore è il $`4{,}2\%`$ appena calcolato.
	- Organica: $``0.012 / 0.042 = ``$ **28,6%**
	- A pagamento: $``0.015 / 0.042 = ``$ **35,7%**
	- Newsletter: $``0.015 / 0.042 = ``$ **35,7%**
	La ricerca organica porta il 60% del traffico ma meno del 30% delle conversioni; la newsletter porta il 10% del traffico e oltre un terzo delle conversioni. **Osservare il dato ha ribaltato la classifica di partenza** — ed è esattamente ciò che fa Bayes.
</details>
---
## Riepilogo
<table fit-page-width="true" header-row="true">
<tr>
<td>Scrittura</td>
<td>Si legge</td>
<td>Denominatore</td>
<td>Sui mesi</td>
</tr>
<tr>
<td>$`P(r)`$</td>
<td>Probabilità di r</td>
<td>Tutti i 12 mesi</td>
<td>$`8/12`$</td>
</tr>
<tr>
<td>$`P(r \cap L)`$</td>
<td>Probabilità di r **e** L</td>
<td>Tutti i 12 mesi</td>
<td>$`4/12`$</td>
</tr>
<tr>
<td>$`P(r \mid L)`$</td>
<td>Probabilità di r **dato** L</td>
<td>Solo i 7 mesi lunghi</td>
<td>$`4/7`$</td>
</tr>
</table>
**In una riga:** condizionare non cambia i casi favorevoli, cambia su quanti li stai contando.
---
## Riferimenti
- Dekking et al., *A Modern Introduction to Probability and Statistics*, cap. 3 ("Conditional probability and independence")
- Dekking et al., cap. 3.3 ("The multiplication rule") per la regola del prodotto
