# 02 - Crittografia simmetrica

> Fonte Notion: https://app.notion.com/p/3e312abc808d81329b42ddd34029e861 — ultima modifica 2026-09-22T13:29:01.114Z

**Docente:** Elia Onofri — Master in Data Analytics, Roma Tre, A.A. 2026
**Registrazione:** `CR-02`, durata 01:14:54
**Fonte:** la registrazione. Integrazioni marcate `> **Nota aggiunta:**`.
> La lezione riprende dai modelli di attacco lasciati aperti alla fine della prima (`CR-01 @ 02:03:22`), poi percorre la crittografia simmetrica dal cifrario di Vernam ad AES.
## 1. Ripresa: i modelli di attacco
### Richiamo — `CR-02 @ 00:00:14`
Le quattro proprietà (confidenzialità, integrità, autenticità, non ripudio) **non sono garantite tutte da ogni algoritmo**. Tipicamente si punta almeno alla confidenzialità, ma esistono casi opposti.
L'esempio che usa è efficace: **un atto pubblico** deve essere integro, autentico e non ripudiabile, ma la confidenzialità **non è un requisito** — anzi, l'atto verrà reso pubblico.
Sul simmetrico (`@ 00:03:35`): la conoscenza della chiave di cifratura implica quella della chiave di decifratura. In Cesare, se la chiave è «aggiungi 3», per decifrare basta lo shift inverso — «aggiungere 3 o togliere 3 se stiamo lavorando in $`\mathbb{Z}_{26}`$».
⚠️ **Divergenza.** Fra `@ 00:01:53` e `@ 00:02:26` il docente dice tre volte «cifratura simmetrica e cifratura simmetrica». Dal contesto la seconda occorrenza di ogni coppia è **asimmetrica**.
### Capacità dell'attaccante — `CR-02 @ 00:05:09`
Un chiarimento che nella lezione 1 mancava: **l'attaccante si assume con capacità polinomiali**, cioè in grado di eseguire un numero polinomiale di operazioni — tempo lineare, quadratico, cubico o con una potenza successiva rispetto alla dimensione dell'input.
Un attaccante con **potenza esponenziale** è considerato irrealistico, «perché tipicamente consideriamo un algoritmo che scali oltre il quadrato o il cubo della dimensione dell'input come non pratico» — con la riserva esplicita: «quantomeno fino a quando non si giungerà all'avvento effettivo dei computer quantistici».
### I quattro modelli, in dettaglio
#### COA — Ciphertext-Only Attack `@ 00:06:45`
L'attaccante intercetta solo i testi cifrati in transito. È **il modello più debole**. I cifrari moderni vi rispondono rendendo il cifrato **indistinguibile da una stringa random**.
> «Se l'attaccante non è in grado di distinguere neppure se l'oggetto che vede passare è un cifrato o è una stringa random, allora non avrà nessuna possibilità di riuscire a decifrare il contenuto.»
Nota a margine (`@ 00:07:54`): **tutti i modelli si generalizzano ai tre contesti** della lezione 1 — dato in transito, at rest, in esecuzione. «Un attaccante che ha accesso a un disco rigido su cui sono salvati solo dati cifrati è l'equivalente dell'attaccante che guarda il dato che viene trasmesso.»
#### KPA — Known-Plaintext Attack `@ 00:08:59`
L'attaccante conosce **alcune coppie (testo in chiaro, testo cifrato)**, e può cercare correlazioni lineari o non lineari fra i bit di input e output.
**La sicurezza contro KPA è richiesta ai cifrari moderni**, e il motivo è storico (`@ 00:09:33`):
> Durante la Seconda guerra mondiale i messaggi tedeschi fra U-Boot e terraferma iniziavano sempre con «Heil Hitler», altre frasi di convenevoli, e poi le previsioni meteo. Conoscendo quella porzione di testo in chiaro, gli alleati riuscivano a rompere Enigma con maggiore facilità.
#### CPA — Chosen-Plaintext Attack `@ 00:10:31`
L'avversario può **scegliere quali plaintext far cifrare**. Ha accesso alla macchina cifrante o a un **oracolo** — un'entità terza capace di cifrare, di cui non deve conoscere la chiave.
L'esempio che ne chiarisce la potenza (`@ 00:11:39`): su Vigenère, sottomettere **un messaggio di tutti zeri restituisce direttamente in chiaro la chiave**.
I cifrari moderni estendono la proprietà come **IND-CPA**. E qui arriva il collegamento che rende il modello tutt'altro che teorico (`@ 00:12:49`):
> Un attaccante capace di cifrare a piacimento sembra troppo potente, **ma nella cifratura asimmetrica è il caso standard**: pubblicando la chiave pubblica, chiunque — avversario incluso — può cifrare qualunque messaggio, senza poterlo decifrare.
#### CCA — Chosen-Ciphertext Attack `@ 00:13:22`
Il modello **più potente**: per un periodo limitato l'attaccante può cifrare *e decifrare* a volontà. Da un massimo di $`k`$ decifrature vorrebbe ricavare **la chiave**, o la regola per decifrare tutto il resto.
Variante: **IND-CCA2**, «il modello classico più complesso di tutti da dimostrare», dove l'attaccante è adattivo e può chiedere decifrature **prima e dopo** aver visto il ciphertext da attaccare.
## 2. Il cifrario di Vernam e l'OTP
`CR-02 @ 00:15:30` — slide *Vernam Cipher*
**Gilbert Vernam**, 1917, ai Bell Labs. Un metodo per comunicazioni via telegrafo basato **solo sull'OR esclusivo**:
$`C = P \oplus K`$
Perché lo XOR funziona qui: un messaggio telegrafato è punto o linea, cioè 0 o 1, «esattamente come per il codice binario dei computer moderni».
### Le tre condizioni — `CR-02 @ 00:16:51`
Il cifrario è **realmente sicuro** solo se la chiave è:
1. **veramente casuale**;
2. **lunga quanto il plaintext** — «non si ripete mai con nessuna regolarità»;
3. **usata una e una sola volta**.
Da qui il nome **one-time pad**. L'intuizione che lo collega alla lezione 1: «possiamo pensarlo un po' come un Vigenère con una chiave totalmente random lunga quanto il cifrato stesso».
## 3. Segretezza perfetta
`CR-02 @ 00:18:34` — slide *Perfect Secrecy (Shannon, 1949)*
Un cifrario è perfettamente sicuro quando **il cifrato non fornisce alcuna informazione addizionale sul plaintext**.
Le condizioni: chiavi **uniformemente casuali**, **indipendenti dal plaintext**, **lunghe esattamente quanto il messaggio**.
Il perché della terza è il punto che lega tutto alla lezione 1 (`@ 00:20:22`):
> Con chiavi più corte si può lavorare **modulo la lunghezza della chiave**. Un Vigenère con chiave di lunghezza 5 «altro non è che 5 cifrari di Cesare».
È il test di Kasiski della lezione 1, riletto come conseguenza della violazione della terza condizione.
### Le due formulazioni — `@ 00:20:52`
**Prima.** Ogni messaggio $`m`$ e ogni ciphertext $`c`$ hanno equa probabilità: la conoscenza di $`c`$ non dà informazione sulla distribuzione dei messaggi.
**Seconda**, che il docente giudica più semplice:
$`\Pr[\mathrm{Enc}(m) = c] = \Pr[\mathrm{Enc}(m') = c] = \frac{1}{|\mathcal{C}|}`$
## 4. La definizione a gioco
`CR-02 @ 00:22:46` — slide *The Game definition*
> «Un gioco non è altro che una prova matematica che avviene attraverso due parti interattive che cercano di ottenere un certo obiettivo.»
**Il protocollo:**
1. L'attaccante sceglie **due messaggi** $`m_0`$ e $`m_1`$ e li manda al challenger.
2. Il challenger sceglie un **bit casuale** $`b`$ — «lancia una monetina».
3. Genera $`k \leftarrow \mathrm{KeyGen}(\cdot)`$ e calcola $`c \leftarrow \mathrm{Enc}(m_b, k)`$.
4. Manda $`c`$ all'attaccante.
5. L'attaccante produce un guess $`b'`$.
Se per **ogni** attaccante $`\Pr[b' = b] = \tfrac{1}{2}`$, il cifrario è **indistinguibile**.
### Perché un mezzo e non zero
Il docente si ferma due volte su questo punto:
> «Perché non chiediamo che la probabilità sia zero? Perché se lui sbagliasse sempre sarebbe sufficiente costruire un attaccante che risponde l'opposto per avere sempre ragione. Quindi il meglio che possiamo ottenere è la probabilità equa, ovvero un mezzo.»
E aggiunge: «questo ritorna anche con il concetto di **massima entropia** del sistema».
## 5. Pregi e limiti dell'OTP
### Pregi
- **Unconditionally secure**, alle tre condizioni.
- **Immune a qualunque attacco diretto**, forza bruta inclusa: anche tentando tutte le chiavi, «i messaggi di partenza sono uniformemente tutti plausibili».
> L'esempio: cifrata la parola `CIAO`, provando tutte le decifrature si ottengono «in generale **tutte le parole di quattro lettere**».
>
> ✅ *Verificato: *$`26^4 = 456.976`$* chiavi e altrettanti testi di 4 lettere. La corrispondenza è biunivoca.*
### Limiti
L'obiezione decisiva (`@ 00:27:59`):
> «Se tanto io riesco a mandare una chiave in maniera sicura lunga $`n`$ bit, tanto vale che mando direttamente il mio messaggio di $`n`$ bit in maniera sicura.»
Il contesto in cui ha senso: incontrarsi di persona, scambiarsi gli OTP per un mese. «Questo è esattamente quello che succedeva durante la Seconda guerra mondiale con i sottomarini tedeschi.»
### Usi reali — `CR-02 @ 00:29:01`
- **Il token OTP della banca** — stesso principio, e da lì il nome.
- **La hotline Stati Uniti–Russia**, via telegrafo sotto l'oceano.
- **Il libro di chiavi**: entrambe le parti avevano la stessa pagina di lettere casuali.
- **I fogli di codici cartacei della banca**: chi faceva un bonifico scriveva il codice e poi **lo depennava**.
## 6. Cifrari a flusso
`CR-02 @ 00:31:14`
Cifra **bit per bit o byte per byte**, generando un **keystream** pseudo-casuale.
> «Quando voi generate un numero random, quel numero non è realmente random, ma è l'output di un processo deterministico. Essendo l'output di un processo deterministico non possiamo definirlo random ma **pseudo-random**.»
### L'idea, in risposta a una domanda — `@ 00:33:12`
> L'OTP non è praticabile perché richiede una stringa arbitrariamente lunga e casuale. Allora: **prendo una chiave più piccola e la espando** in una molto più lunga, che uso come chiave di un OTP.
Il **seme**: «si chiama seme perché è il punto di partenza per la generazione, e dato lo stesso seme otterrò sempre la stessa pianta».
### Proprietà richieste al keystream
1. **Non predicibilità** — dati i primi $`k`$ elementi, non si deve poter predire il $`(k+1)`$-esimo.
2. **Distribuzione uniforme**.
3. **Lunghezza sufficiente**.
### Il limite di fondo — `@ 00:35:59`
> Questi generatori sono **pseudo**-casuali: «se prendiamo un numero sufficiente di bit di chiave, a un certo punto inizieremo a trovare una probabilità non banale di poter predire l'elemento successivo».
### La struttura
<table header-row="true">
<tr>
<td>Componente</td>
<td>Cosa fa</td>
</tr>
<tr>
<td>**Stato interno** $`S_t`$</td>
<td>Vettore di bit, organizzato in $`N`$ registri</td>
</tr>
<tr>
<td>**Inizializzazione**</td>
<td>Prende seme e IV pubblico, genera lo stato iniziale</td>
</tr>
<tr>
<td>**Aggiornamento**</td>
<td>$`S_t \mapsto S_{t+1}`$</td>
</tr>
<tr>
<td>**Output**</td>
<td>$`S_t \mapsto b_t`$, il bit di keystream</td>
</tr>
</table>
### Sincrono contro asincrono
- **Sincrono** — keystream **indipendente** dal messaggio.
- **Asincrono** — usa **parte del testo** che si sta cifrando per generare il bit successivo.
Il compromesso: il sincrono è più veloce «però è prono a errori»:
> «Se ho una stringa lunga 10.000 bit e a un certo punto mi perdo un bit, questa stringa diventerà lunga 9.999 e invaliderà tutta la catena di operazioni dal punto in cui si è rotta.»
> È lo stesso difetto di allineamento già visto su Vigenère (`CR-01 @ 00:57:50`): la struttura del problema si ripete.
## 7. LFSR
`CR-02 @ 00:38:14`, ripreso `@ 00:46:37`
- solo il **primo bit** viene calcolato a ogni passo;
- gli altri **shiftano di una posizione** — *shift register*;
- il primo bit è una **combinazione lineare** degli altri — *linear feedback*;
- **l'ultimo bit a destra è espulso** nel keystream.
In $`\mathbb{F}_2`$ la combinazione lineare **è uno XOR**.
### L'esempio numerico svolto a schermo — `@ 00:40:56` – `00:42:09`
> Il docente svolge i conti **annotando a mano sopra la slide**. Contenuto presente solo nel video.
Registro a **6 celle**: `[IV₁ IV₂ IV₃ | s₁ s₂ s₃]`, **tap** su **IV₂, s₁, s₃**. Stato iniziale: `0 0 1 0 1 0`
<table header-row="true">
<tr>
<td>Passo</td>
<td>Stato</td>
<td>Bit espulso</td>
<td>Nuovo bit = IV₂ ⊕ s₁ ⊕ s₃</td>
</tr>
<tr>
<td>—</td>
<td>`0 0 1 0 1 0`</td>
<td></td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>`0 0 0 1 0 1`</td>
<td>0</td>
<td>$`0 \oplus 0 \oplus 0 = 0`$</td>
</tr>
<tr>
<td>2</td>
<td>`0 0 0 0 1 0`</td>
<td>1</td>
<td>$`0 \oplus 1 \oplus 1 = 0`$</td>
</tr>
</table>
✅ *Verificato per esecuzione: la catena **`001010 → 000101 → 000010`** coincide esattamente con le annotazioni a schermo.*
### Il ciclo
⚠️ **Divergenza.** Il docente dice che per 6 bit il ciclo è «$`2^6`$». $`2^6 = 64`$ è il numero di configurazioni, ma **il ciclo massimo di un LFSR è **$`2^n - 1 = 63`$: lo stato tutto-zero è assorbente.
### Combinare più LFSR
> «Se prendo tanti LFSR e le lunghezze dei loro cicli sono **prime fra loro**, allora combinandoli ottengo un ciclo di lunghezza pari al prodotto.»
Si autocorregge sul termine: «cresce esponenzialmente — nel senso che... non cresce esponenzialmente: **cresce come il prodotto**».
> Il collegamento: «ci ricorda il funzionamento dei rotori di Enigma, perché ogni volta che il primo faceva un giro completo allora girava il secondo».
⚠️ **Divergenza numerica.** L'esempio cita cicli **136, 154, 155**: **non sono coprimi** ($`\gcd(136,154)=2`$), quindi il ciclo combinato è il mcm ($`1.623.160`$) e non il prodotto ($`3.246.320`$).
## 8. Sicurezza dei cifrari a flusso
1. **Impossibilità di state reconstruction** — «altrimenti saremo in grado da quel momento in poi di decifrare tutto quanto».
2. **Impredicibilità bidirezionale** — né i bit successivi **né quelli precedenti**.
### La fase di warm-up
Il problema, sull'esempio stesso dell'LFSR:
> «I primi tre bit che escono in questa costruzione sono **proprio i bit della chiave**. Se un avversario riesce a ottenerli, ha imparato la chiave senza nessuno sforzo.»
Soluzione: **far girare a vuoto** il cifrario prima di emettere il keystream.
### Cifrari a flusso noti
<table header-row="true">
<tr>
<td>Cifrario</td>
<td>Nota del docente</td>
</tr>
<tr>
<td>**RC4**</td>
<td>Usato nel WiFi, «molto molto efficiente», poi scoperto insicuro</td>
</tr>
<tr>
<td>**Salsa20**, **ChaCha20**</td>
<td>Sicuri ed efficienti, oltre gli LFSR</td>
</tr>
<tr>
<td>**Grain**, **Trivium**</td>
<td>Lightweight, per computazioni rapide</td>
</tr>
</table>
### Security considerations
- **Mai riutilizzare la stessa coppia (chiave, IV)** — stesso vincolo dell'OTP.
- Tap non ottimali rendono **tutto il sistema insicuro**.
### Side channel — `@ 00:55:23`
> Negli algoritmi di esponenziazione veloce, **se un bit della chiave è 0 si salta una parte del calcolo**. Se un attaccante misura **l'energia consumata a ogni passo** ottiene informazioni su quanti bit erano attivi.
Gli LFSR sono **implementabili in hardware**, e questo li espone: «anche non mettendoci proprio le mani, ma pensate a misurare la temperatura dei singoli transistor durante l'esecuzione».
## 9. Cifrari a blocchi
Si **suddivide il plaintext in blocchi** (64, 128, 256 bit) e **si cifra ogni blocco con la stessa chiave**.
> «Prendo questo blocco di bit, gli applico una funzione semplice da calcolare, ma applicandola più e più volte ottengo uno stato mescolato talmente tanto che diventa impossibile ritornare allo stato di partenza senza conoscere la chiave.»
Strutture classiche: **reti di Feistel** e **substitution-permutation network**. La chiave di round è derivata dalla principale, e il metodo di espansione «può essere lo stesso stream cipher visto precedentemente» — il collegamento fra le due famiglie.
### I tre tipi di operazione
<table header-row="true">
<tr>
<td>Layer</td>
<td>Natura</td>
<td>Scopo</td>
</tr>
<tr>
<td>**S-box**</td>
<td>Non lineare</td>
<td>**Confusione**</td>
</tr>
<tr>
<td>**Mixing layer**</td>
<td>Lineare</td>
<td>**Diffusione**</td>
</tr>
<tr>
<td>**Add key**</td>
<td>XOR con la chiave di round</td>
<td>Parametrizzazione</td>
</tr>
</table>
- **Confusione** — «è difficile ritornare indietro e capire da dove viene un elemento»;
- **Diffusione** — «l'informazione in una specifica posizione viene spalmata su diverse altre posizioni».
### S-box
> Le S-box sono talmente standard che **anche cifrari diversi usano le stesse**. Quella di AES «viene utilizzata in non so quante altre decine di protocolli crittografici».
**Proprietà di una buona S-box:** non linearità, effetto valanga, uniformità differenziale bassa, **nessun punto fisso** («se prendo 3 non devo ottenere $`-3`$, perché applicando due volte la S-box otterrei il valore di partenza»), pochi cicli molto grandi, bilanciamento.
### Crittoanalisi
- **lineare** — correlazioni fra bit di input e output;
- **differenziale** — correlazioni **fra le differenze** di coppie.
⚠️ Il docente dice «crittografia» dove intende **crittoanalisi**.
## 10. AES
`CR-02 @ 01:09:42`
Standardizzato dal **NIST** nel **2001**.
<table header-row="true">
<tr>
<td>Parametro</td>
<td>Valore</td>
</tr>
<tr>
<td>Blocco</td>
<td>**128 bit** = 16 byte = **matrice 4×4 di byte**</td>
</tr>
<tr>
<td>Chiave</td>
<td>**128, 192 o 256 bit**</td>
</tr>
</table>
**Struttura:** primo round con sola AddRoundKey → round con SubBytes, ShiftRows, MixColumns, AddRoundKey → **round finale senza MixColumns**, «perché sarebbe virtualmente inutile: è possibile tornare indietro per quell'ultima operazione».
- **SubBytes** — sostituzione non lineare byte per byte, tabella affine. Confusione.
- **ShiftRows** — cicla le righe di 1, 2 o 3 unità **a seconda della riga**.
- **MixColumns** — trasformazione lineare sulle colonne. «Attenzione, **non stiamo più lavorando a livello di bit ma di byte**, quindi la combinazione lineare non è semplicemente lo XOR.» La formula non viene completata né a voce né a schermo. `[illeggibile]`
- **AddRoundKey** — XOR con la chiave di round.
> «Esistono attacchi noti su AES ma tutti su **numero di round ridotti**: con 4 o 5 round è facile romperlo, ma al numero totale — che non ricordo, dipende dalla dimensione della chiave — il cifrario è tuttora sicuro.»
>
> **Nota aggiunta:** i round sono 10 per AES-128, 12 per AES-192, 14 per AES-256.
Usi: **TLS**, **cifratura dei dischi** — «una delle scelte consigliate dal file system è proprio **AES-256**».
## Appendici
### Punti a bassa confidenza
L'audio è buono: **1 segmento** su 546 sotto la soglia $`-0.6`$.
<table header-row="true">
<tr>
<td>Timestamp</td>
<td>Punto</td>
<td>Natura</td>
</tr>
<tr>
<td>`@ 00:08:59`</td>
<td>«non plaintext attack»</td>
<td>**Errore di trascrizione**: è *known*-plaintext attack</td>
</tr>
<tr>
<td>`@ 00:15:30`</td>
<td>«American Telegraphers and Recorg»</td>
<td>Il docente intende AT&T</td>
</tr>
<tr>
<td>`@ 00:16:10`</td>
<td>«Oxor», «Oxford», «oxhole»</td>
<td>La trascrizione rende **XOR** in molti modi</td>
</tr>
<tr>
<td>`@ 00:17:28`</td>
<td>«cifrario di Burnham»</td>
<td>**Vernam**</td>
</tr>
<tr>
<td>`@ 01:09:42`</td>
<td>«dell'ICE»</td>
<td>**AES**</td>
</tr>
</table>
### Divergenze
1. ⚠️ `@ 00:42:45` — ciclo massimo LFSR dato come $`2^6`$; è $`2^6 - 1`$.
2. ⚠️ `@ 00:50:56` — cicli 136/154/155 non coprimi: il combinato è il mcm, non il prodotto.
3. ⚠️ `@ 00:01:53` — «simmetrica» al posto di «asimmetrica», tre volte.
4. ℹ️ `@ 01:08:36` — «crittografia» invece di **crittoanalisi**.
5. ℹ️ `@ 01:12:48` — la formula di MixColumns resta incompleta.
### Materiale
103 frame estratti, 89 dopo deduplica, **73 slide logiche** dopo triage. Frame letti visivamente: `00:22:57`, `00:26:07`, `00:43:34`, `00:45:30`, `00:50:48`, `01:10:43`. Conti verificati: catena LFSR, ciclo massimo, coprimalità, spazio chiavi OTP, geometria del blocco AES.
