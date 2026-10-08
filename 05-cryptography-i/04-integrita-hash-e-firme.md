# 04 - Integrità, hash e firme

> Fonte Notion: https://app.notion.com/p/3e312abc808d818aaff9e79df4a2a3c6 — ultima modifica 2026-09-22T13:34:55.070Z

**Docente:** Elia Onofri — Master in Data Analytics, Roma Tre, A.A. 2026
**Registrazione:** `CR-04`. **Durata reale del parlato: 01:20:27** (il file dura 02:04:21).
> ⚠️ **La registrazione è incompleta.** Il parlato si interrompe a `01:20:27`, a metà di un elenco di algoritmi di firma. Gli **schemi di impegno** (commitment schemes), lo schema di **Lamport** e gli **alberi di Merkle** — annunciati a `@ 00:01:15` e presenti nella roadmap della lezione 1 — **non compaiono**. Vedi l'ultima sezione.
## 1. Il problema: tre esempi
Il docente introduce l'hash con tre situazioni che hanno tutte la stessa struttura: **serve integrità, non confidenzialità**.
**Esempio 1 — canale sicuro lento, canale insicuro veloce.** Perché non usare solo quello sicuro? «Perché è difficoltoso da usare, o molto lento, o costoso». Come mandare **dati grandi** sul canale insicuro restando certi che non siano corrotti?
> Precisazione: **corruzione non implica un attaccante**. Il canale può semplicemente non essere affidabile.
**Esempio 2 — archiviazione su cloud.** Alice salva su Drive o Dropbox; al momento di riscaricare, come verifica che nulla sia cambiato?
**Esempio 3 — l'immagine ISO.** Alice si fida del sito Ubuntu, ma le ISO si scaricano da **server mirror**. Come verifica che non ci sia una **backdoor**?
> Raccomandazione diretta (`@ 00:09:48`): «se scaricate un'immagine disco di un qualunque sistema operativo o di una applicazione con accessi privilegiati, **mi raccomando, fate sempre questa verifica**».
## 2. Impronta digitale e funzioni di hash
La risposta è l'**impronta digitale** del dato.
**Proprietà richieste**: calcolabile su dati di qualunque dimensione; **piccola** e di dimensione fissa — «altrimenti tanto vale conservare tutto il dato»; indipendente dalla lunghezza; facile da calcolare; **deterministica**.
Una funzione con queste proprietà è una **funzione di hash**; l'impronta è il **digest**.
$`h : \{0,1\}^* \longrightarrow \mathbb{F}_2^{\,n}`$
**Perché non è invertibile**: si parte da un dominio arbitrario e si mappa in uno finito e molto più piccolo. «A più elementi corrisponderà lo stesso digest.»
### Usi
- **Verifica di integrità**. Sul cloud: «mi salvo il digest, carico il file, quando lo riscarico ricalcolo e verifico». Limite esplicito: «non mi garantisce la possibilità di **riparare** un dato corrotto».
- **Hash table** — il dizionario di Python: «faccio l'hash della chiave e valuto dove andarlo a ripescare».
- **Secure password storage** — si salva il digest, «in modo che un attaccante che rompe il sistema non sia in grado di recuperare la password».
- **Proof of work** — «trovi un messaggio che abbia come digest i primi 20 bit settati a 0». ⚠️ Il docente dice che richiede «**1 alla 20**» tentativi: è $`2^{20}`$.
- **Firme digitali** e **blockchain**.
### Distribuzione uniforme — `@ 00:14:57`
Una funzione è **buona** se i digest sono **uniformemente distribuiti**, cioè con probabilità $`2^{-n}`$. Da qui due conseguenze, ed è il passaggio concettualmente più interessante:
1. **L'unico modo efficiente di calcolare **$`h(m)`$** è valutare **$`h`$** in **$`m`$**.** Se esistesse una scorciatoia $`h(m_1)+h(m_2) = h(m_1+m_2)`$, allora «magari $`h(m_1)`$ e $`h(m_2)`$ sono uniformi, ma $`h(m_1+m_2)`$ non lo sarebbe più».
2. **Non si ottiene informazione su un hash a partire da altri hash.**
Questo la rende «non solo non invertibile, ma **fortemente non invertibile**».
### Effetto valanga
L'esempio a schermo: l'hash di `Roma` e quello di `roma` — una sola lettera di differenza — sono completamente diversi.
## 3. Sicurezza crittografica
<table header-row="true">
<tr>
<td>Proprietà</td>
<td>Definizione data a lezione</td>
</tr>
<tr>
<td>**Collision resistance**</td>
<td>È difficile trovare **due messaggi diversi** con lo stesso hash</td>
</tr>
<tr>
<td>**Preimage resistance**</td>
<td>Dato un digest, è difficile trovare **un** messaggio che lo generi</td>
</tr>
<tr>
<td>**Second preimage resistance**</td>
<td>Dato **uno specifico** messaggio, è difficile trovarne un secondo con lo stesso digest</td>
</tr>
</table>
La distinzione fra la prima e la terza, che il docente esplicita perché si confondono:
> La **collision resistance è generica**: non deve esistere *nessuna* coppia che collide. La **second preimage** parte da un dato specifico, «che magari sto cercando di falsificare».
**SHA** sta per *Secure Hash Algorithm*, dove «secure sta implicitamente per *cryptographically* secure».
## 4. Costruzione Merkle–Damgård
Introdotta da **Ralph Merkle nel 1979**. Si prende una $`f`$ che **dimezza**: $`f : \mathbb{F}_2^{2n} \to \mathbb{F}_2^{n}`$.
**Pseudocodice**:
1. $`[m_1 \| \dots \| m_k] \leftarrow \mathrm{Pad}(m)`$
2. $`y_0 \leftarrow IV`$
3. $`y_i = f(y_{i-1} \| m_i)`$ — l'output precedente **concatenato** col blocco corrente
4. **Digest** $`= g(y_k)`$, con una funzione finale «per rendere il tutto più sicuro»
### Il padding non è innocuo — `@ 00:25:40`
Uno dei punti meglio costruiti della lezione:
> Riempire l'ultimo blocco **con zeri** non funziona: presi due messaggi opportuni, dopo il padding si ottiene lo **stesso** blocco finale, e quindi lo stesso digest. «Rompiamo il requisito di sicurezza della seconda preimmagine.»
La soluzione: **inserire un 1 all'inizio** della sequenza di padding.
## 5. Funzioni a spugna e SHA-3
Introdotte nel **2005** da quattro autori, fra cui **Daemen**, uno dei due autori di AES. **L'idea**: sostituire la funzione di compressione con una **permutazione pseudo-casuale**.
> Conseguenza: se prima era la compressione ad avere «tutto il ruolo di comprimere, mappare e mischiare», ora è **la permutazione** l'oggetto dell'analisi di sicurezza.
### Perché "spugna"
Stato di $`r + c`$ bit, due fasi:
<table header-row="true">
<tr>
<td>Fase</td>
<td>Cosa succede</td>
</tr>
<tr>
<td>**Assorbimento**</td>
<td>Il messaggio viene caricato progressivamente, **solo sulla porzione **$`r`$, in XOR</td>
</tr>
<tr>
<td>**Spremitura**</td>
<td>A ogni passo si rilasciano $`r`$ bit, che compongono il digest</td>
</tr>
</table>
**La conseguenza notevole**: non si ha più un digest di lunghezza fissa, ma **input arbitrario → output di lunghezza arbitraria**.
> È «a suo modo geniale», con il limite: «dopo un tot spremo una spugna perché arrivo a un punto fisso, un po' come succedeva per gli LFSR».
**I due parametri**: $`r`$ è l'**efficienza**; $`c`$ la **capacità** — «più grande sarà la capacità, maggiore la sicurezza, perché più volte potrò mischiare questa spugna senza ottenere un punto fisso».
### Permutazione pseudo-casuale
1. per ogni $`k`$, $`f_k`$ è una **biiezione**;
2. esiste un **algoritmo efficiente** per calcolarla;
3. è impossibile costruire un **distinguisher polinomiale**.
> Richiamo esplicito alla lezione 2: «l'un mezzo nasce perché non voglio probabilità zero — se avessi probabilità zero vorrebbe dire che sto sempre sbagliando, e invertendo il mio guess avrei sempre ragione. **Un mezzo è il meglio, perché corrisponde alla massima entropia.**»
### La storia degli standard NIST
<table header-row="true">
<tr>
<td>Anno</td>
<td>Esito</td>
</tr>
<tr>
<td>**1993**</td>
<td>Funzione su design **MD5**, stile Merkle–Damgård, di Rivest</td>
</tr>
<tr>
<td>**1995**</td>
<td>Sostituita da **SHA-1**: il NIST dichiarò «problemi significativi» **senza mai dichiarare quali**</td>
</tr>
<tr>
<td>**2001**</td>
<td>**SHA-2**, suite di **sei** funzioni; le più usate SHA-256 e SHA-512</td>
</tr>
<tr>
<td>**2015**</td>
<td>Competizione vinta da **Keccak** → **SHA-3**</td>
</tr>
</table>
> Il dettaglio che il docente sottolinea è la **mancata pubblicazione dei motivi** del ritiro del 1993.
**Stato di SHA-3**: «non sono noti attacchi rilevanti, a meno di distinguisher o preimage attack per versioni estremamente semplificate».
⚠️ Elencando le varianti dice «224, 256, **284**, 512»: la terza è **384**.
### Struttura di Keccak
Stato $`5 \times 5 \times w`$ con $`w = 2^L`$, $`L \in [0,6]`$. Per $`L = 6`$: $`5 \cdot 5 \cdot 64 = \mathbf{1600}`$ bit — ✅ *verificato, è lo stato di SHA-3 standard*.
⚠️ Dice «da **50** fino a $`25 \times 2^6`$»: l'estremo inferiore è $`25 \cdot 1 = 25`$ bit.
**Round**: $`12 + 2L`$, che per $`L=6`$ dà **24** — ✅ *verificato*.
**Permutazione**, cinque funzioni: $`\theta`$, $`\rho`$, $`\pi`$, $`\chi`$, $`\iota`$ — solo $`\iota`$ **dipende dal round**.
<table header-row="true">
<tr>
<td>Funzione</td>
<td>Cosa fa, nelle parole del docente</td>
</tr>
<tr>
<td>$`\theta`$</td>
<td>Prende le **colonne antipodali** e ne applica una somma pesata — «una convoluzione, per usare i termini matematici»</td>
</tr>
<tr>
<td>$`\rho`$</td>
<td>Una **rotazione** per ogni striscia verticale</td>
</tr>
<tr>
<td>$`\pi`$</td>
<td>Una **permutazione**, rotazione rispetto alle fette $`5\times5`$</td>
</tr>
<tr>
<td>$`\chi`$</td>
<td>«Ispirata in qualche modo a un LFSR»</td>
</tr>
</table>
**Parametri della spugna**: per un digest di taglia $`d`$, **capacità **$`c = 2d`$ e rate $`r = b - c`$. ✅ *Verificato per SHA3-256: *$`d=256 \Rightarrow c=512`$*, e con *$`b=1600`$* si ottiene *$`r=1088`$*, il valore standard.*
## 6. Hades e Poseidon
**Il problema**: la strategia Keccak è «buona, ottima per certi versi, molto sicura, ma anche **mediamente costosa**», e su hardware limitato «potrei non essere in grado di girare questa funzione». È il problema dei cifrari lightweight, trasposto sulle funzioni di hash.
**Hades**, di **Grassi e collaboratori, 2019**:
> Alternare **round in cui la S-box è applicata sull'intero stato** e **round in cui è applicata solo su una porzione**.
Così si hanno **round forti**, che garantiscono sicurezza contro crittoanalisi lineare e differenziale, e **round deboli**, a costo ridotto, il cui scopo è **mischiare rapidamente i bit**.
<table header-row="true">
<tr>
<td>Strategia</td>
<td>S-box</td>
</tr>
<tr>
<td>**SPN** classica</td>
<td>sempre, ovunque</td>
</tr>
<tr>
<td>**Partial SPN**</td>
<td>solo su un insieme limitato di celle</td>
</tr>
<tr>
<td>**Hades**</td>
<td>alterna layer **full** e layer **partial**</td>
</tr>
</table>
**Poseidon** (Grassi et al., 2019): permutazione su Hades per applicazioni **zero-knowledge**. Stato di $`t`$ elementi su $`\mathbb{Z}_p`$; costanti di round dagli **LFSR Grain** della lezione 2; S-box del tipo $`x^\alpha`$. È stato «in lizza come finalista per la standardizzazione».
## 7. MAC e HMAC
Il docente introduce il MAC con **due esempi costruiti per differenza** rispetto a quelli degli hash.
**Esempio 1.** Alice e Bob hanno un canale insicuro **e uno sicuro solo per un breve periodo** — «si incontrano al parco». La differenza decisiva: lì potevano condividere il digest sul canale sicuro, «qui non lo possono più fare».
**Esempio 2.** Alice vuole accedere ai dati **da un altro dispositivo**: non può pre-calcolare il digest e distribuirlo in anticipo.
### Definizione
Un MAC prende **messaggio + chiave segreta** e garantisce **integrità** e **autenticità**. **Non garantisce la confidenzialità**: «un documento pubblicato su un sito internet, di cui chi lo scarica vuole garantire l'integrità».
**Le fasi**: key generation («anche con uno scambio alla Diffie–Hellman»), computation, verification.
**Sicurezza — la forgery**:
> Anche se Eve avesse accesso a un **oracolo** che calcola il MAC, non deve poter calcolare un nuovo messaggio che produca lo stesso MAC.
### Costruire un MAC da una funzione di hash
**Primo tentativo, insicuro**: usare la chiave come **vettore di inizializzazione**. Perché non funziona — il punto tecnicamente più fine della lezione:
> Se si prende un messaggio che **estende** un precedente, si può calcolare il nuovo MAC senza difficoltà:
> $`H_k(m \| x) = f(H_k(m) \| x)`$
> È l'attacco di **length extension**. C'è la funzione finale $`g`$, «ma tipicamente quelle funzioni potrebbero essere anche invertibili».
**L'approccio standard — HMAC**:
> Da una chiave $`K`$ si ricavano **due sottochiavi**, usate come **primo e ultimo blocco** della funzione di hash:
> $`\mathrm{HMAC}_K(m) = h(K_1 \| h(K_2 \| m))`$
La struttura a due passaggi è esattamente ciò che chiude il buco del length extension.
**Sicurezza**: il miglior attacco noto è **solo un distinguisher**, su versioni ridotte. Inoltre «siccome solo parte della funzione dipende dal messaggio», collisioni e preimmagini diventano più difficili. La conclusione: **la sicurezza di un HMAC è legata indissolubilmente a quella della funzione di hash sottostante**.
## 8. Firme elettroniche e firma digitale
**Autenticazione**: fornire una **prova certa sull'identità dell'entità** che ha generato un messaggio — «un utente, un sistema, un computer».
**Esempi reali**: firma autografa, timbro dell'università sulla pergamena, carta d'identità col timbro del comune, tessera di uno sport club, **watermarking** delle banconote, chip della carta di credito.
**Trasposizioni digitali**: firma scansionata su PDF, **tavoletta grafometrica**, credenziali, token fisici, **parametri biometrici**.
### Il quadro normativo
In Italia: **AGID**, con legislazione dal **2005, D.Lgs. 82**.
> Il punto da cui tutto discende: **la firma elettronica è diversa dalla firma digitale**, e da sola **non garantisce integrità, autenticazione e non ripudio**. «In un contesto in cui le parti si fidano è un mezzo sufficiente, ma non ha valore legale in pratica.»
### I quattro tipi
**1. Firma elettronica semplice** — nessun requisito e **nessun beneficio legale**. Esempi: scansione su PDF, username/password.
> Perché è debolissima: «chiunque può prendere un documento mio su cui ho apposto la firma — pensiamo al **curriculum vitae**, che tanto spesso viene pubblicato provvisto di firma autografa — la scontorna con Gimp e la va ad appiccicare su un altro documento. **Non c'è neanche più bisogno del falsario.**»
> Nota di diritto controintuitiva: «In Italia **solo il proprietario della firma può contestarla**. Se vedete firmare un'altra persona contraffacendo la firma di un terzo, non potete denunciarla.»
**2. Firma elettronica avanzata — AES** (art. 26). Quattro requisiti: **unicamente collegata** al firmatario; **capace di identificarlo**; creata con mezzi **di esclusivo controllo**; **collegata al documento** in modo da rilevare **modifiche successive**. Avvalorata da un **provider trusted**.
> L'analogia per il punto 4: «è l'equivalente di quando in un documento notarizzato viene fatta una modifica fuori dal campo di stampa, e questa viene **controfirmata** dalle parti».
Valore legale: **ad substantiam**, vincolante contrattualmente.
> ⚠️ **Attenzione all'acronimo:** qui **AES = Advanced Electronic Signature**, non *Advanced Encryption Standard*.
**3. Firma elettronica qualificata — QES.** Richiede **tecnologia certificata**, conforme a **ETSI**, «l'equivalente del NIST». La differenza che conta:
> Con una firma **avanzata** il firmatario **può negare** di aver firmato. Con una **qualificata** non può, «a meno di presentare prove, tipo la denuncia in cui mi hanno rubato le credenziali»: **l'onere della prova passa a lui**.
**4. Firma digitale** — una QES **basata su crittografia asimmetrica**. Rilasciata da Poste, Aruba.
### Il meccanismo — sciolto il cliffhanger della lezione 3
> Poiché chiave pubblica e privata hanno **ruolo duale**, posso **cifrare con la privata** e chiunque abbia la pubblica può decifrare. Che senso ha? «Siccome **solo io possiedo la chiave privata**, il fatto che io abbia firmato con essa garantisce che io sia io.»
<table header-row="true">
<tr>
<td>Proprietà</td>
<td>Perché</td>
</tr>
<tr>
<td>**Autenticità**</td>
<td>Il ricevente verifica l'identità del mittente</td>
</tr>
<tr>
<td>**Non ripudio**</td>
<td>Se qualcuno firma con la sua chiave, «spetta a lui dimostrare che gli sono state rubate le credenziali»</td>
</tr>
<tr>
<td>**Integrità**</td>
<td>Chiunque può verificare se il documento è stato modificato</td>
</tr>
</table>
### Firmare il digest, non il messaggio
Qui hash e firma si saldano, ed è il punto di arrivo della lezione:
> «Gli algoritmi a chiave pubblica sono estremamente pesanti, ecco che entra in gioco l'hash: posso prendere un documento, effettuarne l'hash, e **firmare esclusivamente il digest**.»
<table header-row="true">
<tr>
<td></td>
<td>Alice (firma)</td>
<td>Bob (verifica)</td>
</tr>
<tr>
<td>1</td>
<td>Genera la coppia, distribuisce la pubblica</td>
<td>Recupera la chiave pubblica</td>
</tr>
<tr>
<td>2</td>
<td>Calcola $`d = h(m)`$</td>
<td>Calcola $`h(m)`$ sul messaggio ricevuto</td>
</tr>
<tr>
<td>3</td>
<td>Firma: $`s = \mathrm{Sign}_{sk}(d)`$</td>
<td>Verifica che $`\mathrm{Verify}_{pk}(s)`$ corrisponda</td>
</tr>
</table>
Il guadagno cumulativo: l'hash dà l'integrità, la firma ci aggiunge **non ripudio e autenticità**.
### Classi di attacco
<table header-row="true">
<tr>
<td>Attacco</td>
<td>Capacità di Eve</td>
</tr>
<tr>
<td>**Full key recovery**</td>
<td>Recupera la chiave privata → può firmare qualunque messaggio</td>
</tr>
<tr>
<td>**Selective forgery**</td>
<td>Dato **uno specifico** messaggio, genera una firma valida</td>
</tr>
<tr>
<td>**Existential forgery**</td>
<td>**Esiste almeno un** messaggio per cui riesce a firmare</td>
</tr>
</table>
### L'ultima frase — `@ 01:20:08`
> «Metodi esistono chiaramente a bizzeffe. Il primo fra tutti è quello di usare l'RSA al contrario. Esistono altri metodi come la **firma di Schnorr**, il **Digital Signature Algorithm**, o la versione su **elliptic curves** o su **curve di Edwards**»
La registrazione si interrompe qui.
## 9. Dove si interrompe
Il parlato termina a **01:20:27**. I 43 minuti successivi sono **vuoti**.
<table header-row="true">
<tr>
<td>Blocco annunciato a `@ 00:01:15`</td>
<td>Nella registrazione</td>
</tr>
<tr>
<td>Funzioni di hash e costruzioni</td>
<td>✅</td>
</tr>
<tr>
<td>Message Authentication Codes</td>
<td>✅</td>
</tr>
<tr>
<td>Digital signatures</td>
<td>✅, **interrotto sugli algoritmi**</td>
</tr>
<tr>
<td>**Schemi di impegno**</td>
<td>❌ **assente**</td>
</tr>
</table>
Sui commitment aveva anticipato: «quando un utente vuole impegnarsi su una proprietà, su un asserto, senza volerlo rivelare fino a quando questo non si avvera». E nella roadmap della prima lezione erano previsti anche lo **schema di Lamport** e gli **alberi di Merkle**.
**Da chiedere al docente** se esiste una registrazione della parte finale, o se i commitment sono stati rimandati al Case Study — ipotesi plausibile, visto che durante questa lezione ci rimanda almeno quattro volte.
## Appendici
### Riferimenti normativi citati
**AGID** · **D.Lgs. 82/2005** · **Articolo 26** (firma elettronica avanzata) · **ETSI**.
### Punti a bassa confidenza
<table header-row="true">
<tr>
<td>Timestamp</td>
<td>Punto</td>
<td>Natura</td>
</tr>
<tr>
<td>`@ 00:27:26`</td>
<td>«Merkle-Demgaard», «Mertol-Demgard»</td>
<td>**Merkle–Damgård**</td>
</tr>
<tr>
<td>`@ 00:27:26`</td>
<td>«uno dei quali è Damon»</td>
<td>**Joan Daemen**</td>
</tr>
<tr>
<td>`@ 00:37:52`</td>
<td>«Kessack», «che è sacchi»</td>
<td>**Keccak**</td>
</tr>
<tr>
<td>`@ 01:12:25`</td>
<td>«LETSI»</td>
<td>**ETSI**</td>
</tr>
<tr>
<td>`@ 01:02:45`</td>
<td>«carretta di identità»</td>
<td>**carta d'identità**, ricorrente</td>
</tr>
</table>
### Avvertenza sulla trascrizione
La coda vuota ha prodotto **88 segmenti «Grazie a tutti.»** allucinati fra `01:21:05` e `02:04:05`. Rimossi dalla trascrizione e aggiunti al filtro anti-boilerplate. Nelle altre tre lezioni non compaiono mai.
### Divergenze
1. 🔴 **struttura** — registrazione troncata a `01:20:27`, commitment schemes assenti.
2. ⚠️ `@ 00:21:41` — «1 alla 20» tentativi per una proof of work a 20 bit: è $`2^{20}`$.
3. ⚠️ `@ 00:39:23` — stato minimo di Keccak dato come 50 bit: è 25.
4. ⚠️ `@ 00:37:52` — varianti SHA-3: «284» è **384**.
5. ℹ️ `@ 01:12:25` — collisione di acronimi: AES = Advanced Electronic Signature.
6. ℹ️ `@ 00:36:12` — «MD5 inventata da Rivest tra il 1992 e il 1992».
### Materiale
144 frame estratti, 96 dopo deduplica, **65 slide logiche** dopo triage. Conti verificati: dimensione dello stato Keccak, round, parametri della spugna per SHA3-256, cronologia NIST, tentativi attesi per la proof of work.
