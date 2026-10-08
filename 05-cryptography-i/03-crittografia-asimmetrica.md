# 03 - Crittografia asimmetrica

> Fonte Notion: https://app.notion.com/p/3e312abc808d81b1b207d3b068d4e6dc — ultima modifica 2026-09-22T13:33:08.795Z

**Docente:** Elia Onofri — Master in Data Analytics, Roma Tre, A.A. 2026
**Registrazione:** `CR-03`, durata 02:10:53
> È la lezione più densa del modulo: chiude la simmetrica, apre lo scambio di chiavi, e attraversa quattro crittosistemi a chiave pubblica più le curve ellittiche. Il docente lo dichiara a `@ 01:59:49`: «sono già alle 18:26, cercherò di essere rapido».
## 1. Chiusura di AES
Il docente riprende AES perché «probabilmente è uno dei possibili cifrari che implementeremo nel secondo modulo».
Nome originale **Rijndael**. Blocco 128 bit = griglia **4×4 di byte**. Varianti a **10, 12, 14 round** — qui fornisce il numero che nella lezione 2 non ricordava.
**Struttura**: layer iniziale con sola AddRoundKey → 9, 11 o 13 round con SubBytes, ShiftRows, MixColumns, AddRoundKey → ultimo round senza MixColumns, «banalmente perché si potrebbe invertire con facilità, in quanto è una combinazione lineare».
Il punto nuovo rispetto alla lezione 2 (`@ 00:09:16`): standardizzare una S-box è costoso, perché si deve studiare «se ci sono delle **trapdoor**, se ci sono meccanismi per cui diventa facilmente linearizzabile».
**ShiftRows** con i numeri precisi: prima riga ferma, seconda shifta a sinistra di 1, terza di 2, quarta di 3.
### La scelta del cifrario dipende dal compito — `@ 00:12:08`
Due esempi nuovi: un'ora d'attacco da proteggere per 5 ore — «non mi interessa che tra un mese il nemico non sia in grado di decifrare» — e un'informazione su un'operazione in borsa, che eseguita l'operazione «non ha più alcun valore».
## 2. Stream contro block
<table header-row="true">
<tr>
<td></td>
<td>**Stream cipher**</td>
<td>**Block cipher**</td>
</tr>
<tr>
<td>Granularità</td>
<td>bit o byte</td>
<td>blocco fisso</td>
</tr>
<tr>
<td>Chiave</td>
<td>keystream sempre nuovo</td>
<td>**stessa chiave** su tutti i blocchi</td>
</tr>
<tr>
<td>Modalità</td>
<td>sincrono o asincrono</td>
<td>solo sul plaintext</td>
</tr>
<tr>
<td>Implementazione</td>
<td>**facile in hardware**</td>
<td>più sensata in software</td>
</tr>
<tr>
<td>Memoria/latenza</td>
<td>tiene solo lo stato</td>
<td>processa il blocco</td>
</tr>
<tr>
<td>Riuso della chiave</td>
<td>**rischioso** (è un OTP)</td>
<td>previsto per progetto</td>
</tr>
<tr>
<td>Uso tipico</td>
<td>bassa latenza</td>
<td>archiviazione</td>
</tr>
</table>
Il punto che il docente sottolinea: **i blocchi si cifrano in parallelo**, quindi si sfrutta il parallelismo di processori e GPU. Lo stream cipher è iterativo e va passo per passo — «chiaramente generare il keystream è molto meno costoso».
## 3. Cifrari lightweight
Il docente aggancia il tema al master: una **rete di sensori** che trasmette temperatura e umidità deve cifrare, garantendo almeno l'integrità.
Ambienti: **IoT**, **RFID** («l'equivalente del chip della carta di credito»), domotica, Arduino.
### L'esempio dell'agricoltura 5.0 — `@ 00:20:55`
> Monitorare un campo di granturco: interessa soprattutto l'**integrità**, non tanto contro un attacco quanto per un guasto dei sensori. Ma anche contro l'esterno: in una serra con termostato, «un concorrente potrebbe voler distruggere il mio raccolto modificando i dati trasmessi. Il sensore dovrebbe trasmettere 30°, invece trasmette 45°: vengono accesi i condizionatori e tutte le piante muoiono per eccessivo freddo».
Basso rischio ⟹ è accettabile un livello di sicurezza minore.
**Come si costruisce**: meno round, **S-box più piccole** — «invece di lavorare sull'intero byte, lavorano su coppie o terne di bit». Esempi: PRESENT, Simon & Speck, Ascon.
**Ordini di grandezza**: dove uno standard offre 128–256 bit di sicurezza, un lightweight sta sugli **80 bit**, e il blocco scende da 128 a **64**.
> Essendo più semplici sono anche più facili da attaccare, «e l'interesse del crittografo si sposta molto su questi cifrari, perché c'è la convinzione di poterli rompere più facilmente».
## 4. Terminologia
> Contenuto che il docente dichiara di **non aver incluso nelle slide**.
<table header-row="true">
<tr>
<td>Livello</td>
<td>Definizione</td>
<td>Esempio</td>
</tr>
<tr>
<td>**Primitiva**</td>
<td>Le operazioni alla base</td>
<td>Esponenziazione modulare per RSA; AddRoundKey, MixColumns, ShiftRows, SubBytes per AES</td>
</tr>
<tr>
<td>**Crittosistema**</td>
<td>Raggruppa le primitive in una struttura sensata</td>
<td>AES</td>
</tr>
<tr>
<td>**Schema**</td>
<td>L'operazione **più lo standard** con cui è costruita</td>
<td>—</td>
</tr>
<tr>
<td>**Protocollo**</td>
<td>Come lo schema si inserisce nelle comunicazioni: dalla generazione delle chiavi alla decifratura</td>
<td>Alice e Bob, ciclo completo</td>
</tr>
</table>
### Una conseguenza sui modelli di attacco — `@ 00:27:41`
Nel contesto asimmetrico **chiunque può cifrare**:
> «Il ciphertext-only attack non è più preso in considerazione realmente, perché chiunque può costruire un plaintext ed effettuarne la cifratura. Restano solo **CPA e CCA**.»
## 5. Scambio di chiavi
Un protocollo con cui **due parti si accordano su una chiave attraverso un canale insicuro**.
> Il docente ammette che la collocazione è anomala: «doveva essere forse nella lezione della cifratura simmetrica, ma speravo di finire l'altra volta».
Il problema della chiave pubblica (`@ 00:33:26`):
> Bob vuole condividere la sua chiave pubblica col mondo. Ma **come fa a condividerla in maniera sicura?** Un attaccante potrebbe sostituirla con quella di Eve, e tutti i messaggi finirebbero a Eve.
Da qui la **PKI**, rimandata.
**Requisiti**: stessa chiave per entrambi; chiave **indistinguibile da una casuale**; **autenticazione delle parti** («altrimenti con un man in the middle una terza parte potrebbe inserirsi»); **forward secrecy**.
Limite di scalabilità: con $`n`$ utenti servono $`\binom{n}{2}`$ chiavi. Usi: **WPA del Wi-Fi**, autenticazione **GSM**.
### Domanda dall'aula: le API key — `@ 00:35:45`
Uno studente chiede che tipo di chiave sia quella per collegarsi a Firebase:
> È **un meccanismo di autenticazione basato su token**, non uno scambio di chiavi. «Lei sta sincronizzando in due luoghi diversi lo stesso oggetto, il token. **Non si stanno scambiando il segreto**: stanno controllando che entrambe le parti abbiano lo stesso segreto.»
E il ponte: l'API token ha un **duplice scopo** — autenticazione, e punto di partenza per una chiave di sessione.
## 6. Il problema del logaritmo discreto
Il problema cambia natura su un **campo finito**:
> In $`\mathbb{Z}_n`$ **non esistono i numeri con la virgola**: non posso trovare che il logaritmo vale 2,13. Posso solo cercare il numero intero modulo $`n`$ che risolve il problema.
### L'esempio in $`\mathbb{Z}_7`$ — `@ 00:43:46`
<table header-row="true">
<tr>
<td>$`x`$</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
</tr>
<tr>
<td>$`x^2 \bmod 7`$</td>
<td>1</td>
<td>4</td>
<td>**2**</td>
<td>**2**</td>
<td>**4**</td>
<td>**1**</td>
</tr>
</table>
✅ *Verificato: tutti i valori calcolati a voce sono corretti.*
Le due osservazioni che ne trae sono giuste: **non tutti i numeri hanno un logaritmo** (i residui quadratici sono solo $`\{1,2,4\}`$) e **chi ne ha uno ne ha due**, $`\pm x`$. Vale perché **7 è primo**.
⚠️ **Nota terminologica.** Il docente usa «logaritmo in base 2» per la **radice quadrata**: il 2 è l'esponente, non la base. Si corregge da solo molto più avanti (`@ 01:32:56`).
### Generatori — `@ 00:47:37`
🔴 **Divergenza.** Il docente verifica se 2 genera $`\mathbb{Z}_7^*`$. Al primo tentativo usa le **potenze** e ottiene $`2 \to 4 \to 1 \to 2`$, concludendo **correttamente** che non genera tutto il gruppo. Poi si interrompe — «aspettate, scusate, ho detto una fesseria» — e rifà il conto con i **multipli**, concludendo che genera l'intero gruppo.
**La prima conclusione era quella giusta.** I multipli generano il gruppo **additivo**; Diffie–Hellman vive in quello **moltiplicativo**, dove contano le potenze. In $`\mathbb{Z}_7^*`$ l'elemento 2 ha ordine 3: **non è un generatore**. I generatori veri sono **3 e 5**.
✅ *Verificato per esecuzione.*
## 7. Diffie–Hellman
Il **primo protocollo di key exchange** (1976), sul problema del **logaritmo discreto**.
<table header-row="true">
<tr>
<td></td>
<td>Alice</td>
<td>Bob</td>
</tr>
<tr>
<td>Segreto</td>
<td>$`a`$</td>
<td>$`b`$</td>
</tr>
<tr>
<td>Invia</td>
<td>$`A = g^a \bmod p`$</td>
<td>$`B = g^b \bmod p`$</td>
</tr>
<tr>
<td>Chiave</td>
<td>$`K = B^a = (g^b)^a`$</td>
<td>$`K = A^b = (g^a)^b`$</td>
</tr>
</table>
Le due coincidono **per la proprietà associativa dell'esponenziazione**.
Cosa vede l'attaccante: solo $`A`$ e $`B`$. Può calcolare $`A \cdot B = g^{a+b}`$, ma da lì non si ricava $`g^{ab}`$.
### L'esempio numerico — `@ 00:54:49`
Dalla slide:
```javascript
Public: p = 23, g = 5
Alice: secret a = 6  ⟹  A = 5⁶  mod 23 = 8
Bob:   secret b = 15 ⟹  B = 5¹⁵ mod 23 = 2
Shared key:
   Alice: 2⁶  mod 23 = 64 mod 23 = 18
   Bob:   8¹⁵ mod 23 = 18
```
🔴 **Divergenza grave — la slide è sbagliata in due punti.**
<table header-row="true">
<tr>
<td></td>
<td>Slide</td>
<td>Calcolato</td>
</tr>
<tr>
<td>$`A = 5^6 \bmod 23`$</td>
<td>8</td>
<td>**8** ✅</td>
</tr>
<tr>
<td>$`B = 5^{15} \bmod 23`$</td>
<td>2</td>
<td>**19** ❌</td>
</tr>
<tr>
<td>Chiave</td>
<td>18</td>
<td>**2** ❌</td>
</tr>
</table>
Il **2** è in realtà il segreto condiviso dell'esempio canonico, finito nella casella di $`B`$. Da lì il calcolo $`2^6 = 18`$ è coerente *col valore sbagliato*, e il 18 è stato riportato anche per Bob, dove non torna ($`8^{15} \bmod 23 = 2`$).
È **lo stesso meccanismo** dell'errore di Vigenère nella lezione 1.
### Sicurezza e vulnerabilità
**Dimensione**: il problema è assunto difficile per $`p`$ dell'ordine di **2048 bit**.
**Man in the middle**: Eve fa **due key agreement separati**. Il punto sottolineato: è **difficile da rilevare**, perché Eve rinoltra i messaggi «così com'è».
La contromisura pratica:
> «È quello che fa WhatsApp con la crittografia end-to-end. Se cliccate su crittografia viene generato un **numero a 60 cifre**: posso confrontarlo con quello del telefono dell'altra persona. Stesso vuol dire che non ci sono parti inserite nel mezzo.»
### Computer quantistici — `@ 00:56:52`
Il **qubit** rappresenta entrambi gli stati: si seguono **due computazioni allo stesso tempo**; con 4 bit, $`2^4`$.
L'analogia: è l'equivalente di una **macchina di Turing non deterministica**. E la precisazione:
> «Nel problema P = NP, vi ricordo che P sta per polinomiale ma **NP non sta per non polinomiale**: sta per **non deterministico polinomiale**.»
L'**algoritmo di Shor** rompe il logaritmo discreto in tempo polinomiale. Stato dell'arte: «parliamo di poche decine di qubit, non ancora numeri effettivamente sfruttabili».
## 8. RSA
Introdotto nel **1977** da **Rivest, Shamir e Adleman**. Si basa sul **problema della fattorizzazione**.
Un'osservazione epistemologica che vale per tutto il corso (`@ 01:07:05`):
> «La maggior parte dei problemi su cui si basano gli algoritmi crittografici **non sono provati essere in NP**, ma sono problemi che si *crede* siano difficili. È il caso della fattorizzazione: non conosciamo un algoritmo polinomiale, ma potrebbe esistere — nessuno ci dice il contrario.»
### Generazione delle chiavi
1. Due primi grandi $`p`$, $`q`$ — il caso più difficile è $`n`$ prodotto di **due soli primi**.
2. $`n = pq`$, il **modulo RSA**.
3. $`e \in \mathbb{Z}^*_{\varphi(n)}`$.
4. $`d`$ tale che $`e \cdot d \equiv 1 \pmod{\varphi(n)}`$.
Con $`\varphi(n) = (p-1)(q-1)`$.
> Il docente dice inizialmente «modulo $`n`$» e si autocorregge: «in $`\mathbb{Z}`$ di $`\varphi(n)`$, scusate, non in $`\mathbb{Z}`$ di $`n`$».
**Perché **$`d`$** è difficile da trovare**: è facile **solo se **$`p`$** e **$`q`$** sono noti**. Calcolarlo direttamente modulo $`n`$ è «almeno tanto complesso quanto la fattorizzazione» — lo si mostra per **riduzione**.
### Cifratura e decifratura
$`c = m^e \bmod n \qquad\qquad m = c^d \bmod n`$
Funziona per il **teorema di Eulero**: $`m^{\varphi(n)} \equiv 1 \pmod n`$.
✅ *Verificato per esecuzione con *$`p=61`$*, *$`q=53`$*, *$`e=17`$*: *$`d = 2753`$*, ciclo cifra-decifra corretto.*
> Il docente oscilla fra Eulero e Fermat. Il piccolo teorema di Fermat vale per $`n`$ primo; qui, con $`n`$ composto, serve quello di Eulero.
### La dualità di $`e`$ e $`d`$ — `@ 01:13:39`
> $`e`$ e $`d`$ sono **interscambiabili**. Posso cifrare con la pubblica e decifrare con la privata, **ma anche cifrare con la privata e decifrare con la pubblica**.
E chiude con un cliffhanger: «perché dovrei essere interessato a farlo non ve lo dico, ve lo lascio come sorpresa per la prossima lezione» — è la firma digitale.
### Sicurezza
**Costo di fattorizzazione** per un intero di $`b`$ bit:
<table header-row="true">
<tr>
<td>Metodo</td>
<td>Costo</td>
</tr>
<tr>
<td>Forza bruta</td>
<td>$`\sqrt{2^b}`$</td>
</tr>
<tr>
<td>Dixon / crivello quadratico</td>
<td>$`2^{\sqrt{b}}`$</td>
</tr>
<tr>
<td>**GNFS**</td>
<td>$`2^{\sqrt[3]{b}}`$</td>
</tr>
</table>
**Chiavi deboli**: $`m^e < n`$; $`p`$** e **$`q`$** troppo vicini**; $`p-1`$ e $`q-1`$ con fattori primi piccoli; $`d < \frac{1}{3}n^{1/4}`$.
**Chiavi forti**: la più lunga mai rotta è di **829 bit**; con **un milione di euro** si rompe una chiave da **768 bit in 6 mesi**; 768 bit ≈ $`10^{231}`$ — ✅ *verificato*; **1024 bit non è più sicuro**; per chi usa ancora RSA — «che inizia a essere un metodo legacy» — si suggerisce **4096 bit**.
> Avvertenza del docente: «questi sono dati di 4 anni fa, dovrei aggiornarli».
**Shor**: circa $`b^3`$ operazioni.
## 9. ElGamal
**Taher ElGamal**, **1985**. Sul **logaritmo discreto**, garantisce **IND-CPA** — a differenza di RSA, che essendo deterministico non ce l'ha.
**Chiavi**: primo $`p`$, generatore $`g`$, segreto $`x`$, pubblico $`h = g^x \bmod p`$.
**Cifratura** con un **effimero casuale** $`y`$:
$`c_1 = g^y \bmod p \qquad c_2 = m \cdot h^y \bmod p`$
> Il ruolo di $`y`$ è centrale: «se cifro due volte lo stesso messaggio, la cifratura sarà differente ogni volta». È **cifratura probabilistica**, ed è ciò che dà l'indistinguibilità.
**Decifratura**: $`m = c_2 \cdot (c_1^x)^{-1} \bmod p`$, perché $`h^y = g^{xy}`$ e moltiplicando per $`g^{-xy}`$ resta $`m`$.
**Espansione del ciphertext**: bisogna trasmettere $`c_1`$ e $`c_2`$, «circa doppio rispetto al messaggio».
### Omomorfismo moltiplicativo — `@ 01:28:46`
Il prodotto delle cifrature è la cifratura del prodotto:
> «Mi permette di fare operazioni sul testo cifrato come se le stessi facendo sul testo in chiaro.» — «fondamentale nell'analisi dei dati».
E lo estende: $`m_1^e \cdot m_2^e = (m_1 m_2)^e`$, quindi **anche RSA è omomorfo rispetto alla moltiplicazione**.
✅ *Verificato per esecuzione: *$`\mathrm{Enc}(7)\cdot\mathrm{Enc}(11) \equiv \mathrm{Enc}(77)`$*.*
Per l'omomorfismo **pieno** si è dovuto attendere la **Fully Homomorphic Encryption** su **Learning With Errors**, attribuita a **Regev, 2009**.
⚠️ Il docente dà due quantificazioni incompatibili: «più di 25 anni» e poi «quasi 15 anni». Da 1985 a 2009 sono **24**.
## 10. Paillier
**Pascal Paillier**, **1999**. Motivo didattico esplicito: se ElGamal è omomorfo rispetto **al prodotto**, Paillier lo è rispetto **alla somma**.
**Chiavi**: $`n = pq`$, $`\lambda = \mathrm{lcm}(p-1, q-1)`$, $`g \in \mathbb{Z}^*_{n^2}`$ — **attenzione, in **$`\mathbb{Z}_{n^2}^*`$ — con $`\gcd(L(g^\lambda \bmod n^2), n) = 1`$, e $`\mu = (L(g^\lambda \bmod n^2))^{-1}`$.
> «Questo è necessario per garantire la sicurezza. Fidatevi, è complesso: non è semplicemente tornare nei conti scegliendo questi numeri.»
**Cifratura**: $`c = g^m \cdot r^n \bmod n^2`$
> «Questa parte è **l'inverso** rispetto a RSA: prendo il generatore e lo elevo al messaggio, non viceversa.» E sul modulo: «se fosse modulo $`n`$ questa cosa si annullerebbe, quindi **modulo **$`n^2`$».
**Decifratura**: il docente non svolge la derivazione — «tediosa e poco utile per i nostri effetti». `[non svolto a lezione]`
### Omomorfismo additivo
$`c_1 \cdot c_2 = g^{m_1 + m_2} \cdot (r_1 r_2)^n`$
Poiché $`m`$ sta **all'esponente**, il prodotto dei cifrati è la cifratura della **somma**.
**Applicazione**: **voto elettronico** — «la possibilità di votare in maniera elettronica e non con la cartella che va imbucata». Si sommano i voti senza decifrarli.
## 11. Rabin e l'oblivious transfer
**Michael O. Rabin**, **1979**. Quello che lo rende speciale: è **uno dei primi crittosistemi per cui è dimostrata l'equivalenza alla fattorizzazione** — non "basato su", ma **equivalente**.
- **Esponente fissato a 2**: $`c = m^2 \bmod n`$.
- $`p \equiv q \equiv 3 \pmod 4`$, che **garantisce quattro radici**.
- Decifratura col **teorema cinese dei resti**: $`m_p = c^{(p+1)/4} \bmod p`$, $`m_q = c^{(q+1)/4} \bmod q`$, e si combinano $`\pm m_p`$, $`\pm m_q`$.
✅ *Verificato con *$`p=7`$*, *$`q=11`$*, *$`n=77`$*: *$`m=20`$* dà *$`c=15`$*, le cui radici modulo 77 sono esattamente quattro — *$`\{13, 20, 57, 64\}`$*.*
> Il docente tenta di spiegare l'algoritmo di Euclide esteso e si interrompe due volte: «mi sono spiegato malissimo, perdonate». Rimanda al testo **Languasco–Zaccagnini** e si offre di dedicarci mezz'ora nel Case Study. `[non svolto a lezione]`
**Disambiguazione**: un **tag** nel messaggio — «il messaggio corretto inizia con 50».
**Limite**: senza elemento casuale, Rabin **non è indistinguibile**.
### Oblivious transfer — `@ 01:49:34`
Il vero motivo per cui ha introdotto Rabin.
**OT randomizzato**: il ricevente decifra **solo con probabilità 1/2**, e:
- **non è il mittente a decidere** se ci riuscirà;
- il mittente **resta oblivious** sull'esito.
**OT 1-su-2**: il destinatario sceglie quale dei due messaggi ottenere, il mittente **resta ignaro della scelta**, il destinatario può decifrare **solo uno**.
> L'esempio: «un'azienda offre due servizi a pagamento. Il destinatario ne acquista uno **senza rivelare quale**. L'azienda condivide le chiavi di entrambi, il destinatario ne ottiene una sola, e l'azienda non apprende quale.»
**Il protocollo su Rabin**: il destinatario sceglie un casuale $`x`$, invia $`y = x^2`$; il mittente calcola le **quattro radici** e ne comunica **solo una coppia**. Se è quella che il destinatario già conosceva non ha appreso nulla; se è l'altra, possiede tutte e quattro le radici e **può fattorizzare **$`n`$.
Il caveat esplicito: tutto si regge su $`p \equiv q \equiv 3 \pmod 4`$.
**Applicazioni**: private information retrieval, **zero-knowledge**, **multi-party computation** — «più entità mettono insieme i propri dati per una computazione comune senza rivelare quali sono i dati in loro possesso» — e **blockchain**.
## 12. Curve ellittiche e post-quantum
<table header-row="true">
<tr>
<td></td>
<td>**Basata su modulo**</td>
<td>**Curve ellittiche**</td>
</tr>
<tr>
<td>Esempi</td>
<td>RSA, Rabin, Paillier</td>
<td>ECDH, ECDSA</td>
</tr>
<tr>
<td>Problema</td>
<td>fattorizzazione, residui quadratici</td>
<td>log discreto su curva</td>
</tr>
<tr>
<td>Maturità</td>
<td>«studiata per quasi mezzo secolo»</td>
<td>«più recente e meno compresa»</td>
</tr>
</table>
**Cos'è una curva ellittica**, nella sola costruzione geometrica:
> Presi due punti sulla curva, si calcola un terzo punto come **l'intersezione con la retta che passa per i due**. Quel terzo punto è la **somma**.
**Il vantaggio**: per una sicurezza equivalente a **1024 bit di RSA** bastano **160 bit**.
> «Potete fare la prova da soli generandovi delle chiavi col comando `ssh-keygen`, con una chiave RSA o a curve ellittiche, e vedere la differenza in dimensione del file.»
**Perché allora non si migra in massa** — due ragioni:
1. **Studiare la sicurezza di ogni curva è un problema a sé**, e trovarne di sicure è difficile.
2. **Sia RSA sia le curve sono vulnerabili a Shor**, quindi «non ha tutto questo senso mettere questo effort sulle curve ellittiche se tanto anche queste verranno rotte».
**Candidati post-quantum**: **reticoli** («punti discreti costruiti come prodotti cartesiani di assi non perpendicolari»), **teoria dei codici**, **isogenie**, costruzioni su **funzioni di hash**.
**L'obiettivo del NIST**: abbandonare **sia RSA sia le curve ellittiche** sul lungo periodo.
Le ultime slide, mostrate rapidamente: criteri per curve sicure (metodi di generazione **trasparenti e verificabili**) e il confronto **Ed25519 contro curve NIST**.
## Appendici
### Riferimenti dati dal docente
- **Languasco–Zaccagnini**, per il teorema cinese dei resti.
- Il comando **`ssh-keygen`** per confrontare le dimensioni di chiave RSA e ECC.
### Punti a bassa confidenza
<table header-row="true">
<tr>
<td>Timestamp</td>
<td>Punto</td>
<td>Natura</td>
</tr>
<tr>
<td>`@ 01:05:19`</td>
<td>«Riedest, Shamir e Adleman»</td>
<td>**Rivest**</td>
</tr>
<tr>
<td>`@ 01:06:28`</td>
<td>«2046 bit o 4098, 2048, 2190»</td>
<td>«scusate mi sto incartando con i numeri»</td>
</tr>
<tr>
<td>`@ 01:15:58`</td>
<td>«crivello di Ratostene»</td>
<td>**Eratostene**</td>
</tr>
<tr>
<td>`@ 01:31:48`</td>
<td>«Payet», «Payere»</td>
<td>**Paillier**</td>
</tr>
<tr>
<td>`@ 01:50:05`</td>
<td>«probabilità 1.5»</td>
<td>**1/2**</td>
</tr>
</table>
### Divergenze
1. 🔴 `@ 00:54:49` — l'esempio Diffie–Hellman sulla slide è **sbagliato**: $`B`$ vale 19, non 2; la chiave è 2, non 18.
2. 🔴 `@ 00:49:25` — il docente conclude che 2 genera $`\mathbb{Z}_7^*`$ dopo aver elencato i **multipli** invece delle **potenze**; la sua prima conclusione, ritrattata, era corretta.
3. ⚠️ `@ 01:30:39` — «più di 25 anni» e «quasi 15 anni» per lo stesso intervallo.
4. ℹ️ `@ 00:44:27` — «logaritmo in base 2» per la radice quadrata; corretto dal docente stesso.
5. ℹ️ `@ 01:12:32` — attribuzione oscillante fra Eulero e Fermat.
### Materiale
180 frame estratti, 157 dopo deduplica, **118 slide logiche** dopo triage. Conti verificati: Diffie–Hellman con i toy values, generatori di $`\mathbb{Z}_7^*`$ e $`\mathbb{Z}_{23}^*`$, residui quadratici, ciclo RSA, omomorfismo moltiplicativo, quattro radici di Rabin, ordine di grandezza di $`2^{768}`$.
