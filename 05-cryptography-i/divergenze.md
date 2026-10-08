# Divergenze

> Fonte Notion: https://app.notion.com/p/3e312abc808d81eba9d1c14f9b5ed8ba — ultima modifica 2026-09-22T13:36:41.903Z

Registro completo dei punti in cui quello che il docente dice, quello che la slide mostra e quello che il calcolo dà non coincidono. **Nessuno è stato corretto in silenzio**: ognuno è riportato nel capitolo dov'è, con rimando qui.
Tutte le verifiche numeriche sono state eseguite in Python: `scripts/verifica_cr0N.py`.
## Le due che contano
Entrambe sono **errori nelle slide**, ed entrambe hanno **lo stesso identico meccanismo**: un valore corretto dell'esempio canonico finito nella casella sbagliata, coi calcoli a valle rifatti sul valore errato invece che sulla fonte.
### 🔴 Lezione 1 — l'esempio di Vigenère `@ 00:56:07`
La slide mostra:
```javascript
Plaintext    A T T A C K A T M I D N I G H T
Keyword      L E M O N L E M O N L E M O N L
Ciphertext   L X F O P V E F R N H R Y G U Z
```
Il calcolo dà:
```javascript
posizione    1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
plaintext    A  T  T  A  C  K  A  T  M  I  D  N  I  G  H  T
chiave       L  E  M  O  N  L  E  M  O  N  L  E  M  O  N  L
corretto     L  X  F  O  P  V  E  F  A  V  O  R  U  U  U  E
slide        L  X  F  O  P  V  E  F  R  N  H  R  Y  G  U  Z
                                     ↑  ↑  ↑     ↑  ↑     ↑
```
**Origine ricostruita e verificata.** Il ciphertext della slide è quello dell'esempio canonico con plaintext `ATTACKATDAWN`:
```javascript
ATTACKATDAWN + LEMON  →  LXFOPVEFRNHR      (12 lettere)
slide, primi 12:         LXFOPVEFRNHR       ← coincidono esattamente
```
Il plaintext è stato allungato da `ATTACKATDAWN` a `ATTACKATMIDNIGHT` **senza ricalcolare il cifrato**. Le prime 8 lettere sopravvivono perché `ATTACKAT` è il prefisso comune. Le ultime quattro, `YGUZ`, non corrispondono né al calcolo corretto né all'esempio canonico.
**Perché conta:** è la slide su cui uno studente verifica di aver capito il meccanismo. Chi rifa i conti a mano trova un disaccordo dalla nona lettera e conclude di aver sbagliato lui.
### 🔴 Lezione 3 — l'esempio Diffie–Hellman `@ 00:54:49`
La slide mostra:
```javascript
Public: p = 23, g = 5
Alice: secret a = 6   ⟹  A = 5⁶  mod 23 = 8
Bob:   secret b = 15  ⟹  B = 5¹⁵ mod 23 = 2
Shared key:
   Alice: 2⁶  mod 23 = 64 mod 23 = 18
   Bob:   8¹⁵ mod 23 = 18
```
<table header-row="true">
<tr>
<td>Valore</td>
<td>Slide</td>
<td>Corretto</td>
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
<td>Chiave lato Alice</td>
<td>18</td>
<td>**2** ❌</td>
</tr>
<tr>
<td>Chiave lato Bob</td>
<td>18</td>
<td>**2** ❌</td>
</tr>
</table>
**Origine ricostruita.** Con questi parametri l'esempio canonico dà $`A=8`$, $`B=19`$ e **segreto condiviso **$`= 2`$. Sulla slide il **2 — che è il segreto condiviso — è finito nella casella di **$`B`$. Da lì il calcolo $`2^6 \bmod 23 = 18`$ è aritmeticamente corretto ma parte dal valore sbagliato, e il 18 è stato riportato anche sulla riga di Bob, dove non torna in nessun modo.
**Il protocollo resta valido.** Sostituendo $`B = 19`$: $`19^6 \equiv 8^{15} \equiv 2 \pmod{23}`$, e le due parti concordano.
> Il docente, a `@ 00:55:32`, si sofferma proprio sul passaggio errato e ne verifica l'aritmetica ad alta voce — «2 alla sesta, che è uguale a 64: 2, 4, 8, 16, 32, 64, sì, che è congruo a 18 modulo 23» — senza rimettere in discussione il valore di partenza.
## La svista concettualmente più interessante
### 🔴 Lezione 3 — «2 genera $`\mathbb{Z}_7^*`$» `@ 00:49:25`
**Primo tentativo — corretto.** Il docente calcola le **potenze** di 2 modulo 7:
```javascript
2 → 4 → 8 ≡ 1 → 2 → …          insieme generato: {1, 2, 4},  ordine 3
```
e conclude giustamente: «questo non genera interamente il gruppo ciclico».
**Ritrattazione — sbagliata.** Poco dopo si interrompe: «aspettate, scusate, ho detto una fesseria, questi sono i quadrati progressivi», e rifà il conto con i **multipli**:
```javascript
2·1=2, 2·2=4, 2·3=6, 2·4≡1, 2·5≡3, 2·6≡5     insieme: {1,2,3,4,5,6}
```
concludendo: «vedete che 2 ha generato l'intero gruppo ciclico».
**Il problema.** I multipli generano il gruppo **additivo** $`(\mathbb{Z}_7, +)`$, dove *ogni* elemento non nullo è un generatore e il conto non dice nulla di interessante. Diffie–Hellman vive nel gruppo **moltiplicativo** $`\mathbb{Z}_7^*`$, dove contano le **potenze**.
```javascript
ordine di 2 in Z7*  = 3     →  NON è un generatore
generatori veri di Z7*: 3 e 5
```
Il docente sembra avvertire l'ambiguità, perché subito dopo dice «ora può essere un gruppo ciclico rispetto alla moltiplicazione, rispetto alla somma», senza però scegliere.
**Perché conta.** La scelta del generatore è il primo passo di Diffie–Hellman: un $`g`$ di ordine piccolo riduce drasticamente lo spazio della chiave. Ed è tanto più insidioso perché **la conclusione giusta era già stata raggiunta e poi scartata**.
## Lacuna strutturale
### 🔴 Lezione 4 — la registrazione è troncata
Il file dura 02:04:21 ma il parlato finisce a **01:20:27**, a metà di un elenco. I 43 minuti successivi sono vuoti e hanno prodotto **88 «Grazie a tutti.»** allucinati da Whisper.
Gli **schemi di impegno** (commitment schemes), lo **schema di Lamport** e gli **alberi di Merkle** — annunciati a `CR-04 @ 00:01:15` e nella roadmap di `CR-01 @ 00:15:45` — **non compaiono**. È l'unica lacuna di contenuto del corso.
## Tabella completa
<table header-row="true">
<tr>
<td>Lez.</td>
<td>Timestamp</td>
<td>Gravità</td>
<td>Punto</td>
<td>Tipo</td>
</tr>
<tr>
<td>1</td>
<td>`@ 00:56:07`</td>
<td>🔴</td>
<td>Vigenère: ciphertext della slide sbagliato</td>
<td>Errore sulla slide</td>
</tr>
<tr>
<td>1</td>
<td>`@ 00:25:37`</td>
<td>⚠️</td>
<td>«K è la 14ª lettera»: è l'11ª. La coordinata $`(2,5)`$ è comunque corretta</td>
<td>Lapsus</td>
</tr>
<tr>
<td>1</td>
<td>`@ 01:58:36`</td>
<td>⚠️</td>
<td>«simmetrica» detto due volte al posto di «asimmetrica»</td>
<td>Lapsus</td>
</tr>
<tr>
<td>1</td>
<td>`@ 00:27:49`</td>
<td>ℹ️</td>
<td>Erodoto a voce, Polibio sulla slide</td>
<td>Voce vs slide</td>
</tr>
<tr>
<td>2</td>
<td>`@ 00:42:45`</td>
<td>⚠️</td>
<td>Ciclo massimo LFSR dato come $`2^6`$: è $`2^6-1`$, lo stato tutto-zero è assorbente</td>
<td>Imprecisione concettuale</td>
</tr>
<tr>
<td>2</td>
<td>`@ 00:50:56`</td>
<td>⚠️</td>
<td>Cicli 136/154/155 non coprimi: il combinato è il mcm, non il prodotto</td>
<td>Esempio che viola la regola appena data</td>
</tr>
<tr>
<td>2</td>
<td>`@ 00:01:53`</td>
<td>⚠️</td>
<td>«simmetrica» al posto di «asimmetrica», tre volte</td>
<td>Lapsus ricorrente</td>
</tr>
<tr>
<td>2</td>
<td>`@ 01:08:36`</td>
<td>ℹ️</td>
<td>«crittografia» lineare/differenziale invece di **crittoanalisi**</td>
<td>Lapsus terminologico</td>
</tr>
<tr>
<td>2</td>
<td>`@ 01:12:48`</td>
<td>ℹ️</td>
<td>La formula di MixColumns resta incompleta</td>
<td>Contenuto non svolto</td>
</tr>
<tr>
<td>3</td>
<td>`@ 00:54:49`</td>
<td>🔴</td>
<td>Diffie–Hellman: $`B`$ e chiave sbagliati sulla slide</td>
<td>Errore sulla slide</td>
</tr>
<tr>
<td>3</td>
<td>`@ 00:49:25`</td>
<td>🔴</td>
<td>Generatore di $`\mathbb{Z}_7^*`$: conclusione corretta ritrattata</td>
<td>Svista concettuale</td>
</tr>
<tr>
<td>3</td>
<td>`@ 01:30:39`</td>
<td>⚠️</td>
<td>«più di 25 anni» e «quasi 15 anni» per lo stesso intervallo (sono 24)</td>
<td>Contraddizione interna</td>
</tr>
<tr>
<td>3</td>
<td>`@ 00:44:27`</td>
<td>ℹ️</td>
<td>«logaritmo in base 2» per la radice quadrata — corretto dal docente stesso a `@ 01:32:56`</td>
<td>Uso improprio</td>
</tr>
<tr>
<td>3</td>
<td>`@ 01:12:32`</td>
<td>ℹ️</td>
<td>Attribuzione oscillante Eulero/Fermat (l'enunciato è corretto)</td>
<td>Attribuzione</td>
</tr>
<tr>
<td>4</td>
<td>troncata</td>
<td>🔴</td>
<td>Registrazione finisce a `01:20:27`, commitment schemes assenti</td>
<td>**Lacuna strutturale**</td>
</tr>
<tr>
<td>4</td>
<td>`@ 00:21:41`</td>
<td>⚠️</td>
<td>«1 alla 20» tentativi per proof of work a 20 bit: è $`2^{20}`$</td>
<td>Lapsus numerico</td>
</tr>
<tr>
<td>4</td>
<td>`@ 00:39:23`</td>
<td>⚠️</td>
<td>Stato minimo di Keccak dato come 50 bit: è 25</td>
<td>Errore sull'estremo</td>
</tr>
<tr>
<td>4</td>
<td>`@ 00:37:52`</td>
<td>⚠️</td>
<td>Varianti SHA-3: «284» è **384**</td>
<td>Lapsus numerico</td>
</tr>
<tr>
<td>4</td>
<td>`@ 01:12:25`</td>
<td>ℹ️</td>
<td>AES = Advanced Electronic **Signature**, non Encryption Standard</td>
<td>Ambiguità di sigla, non errore</td>
</tr>
<tr>
<td>4</td>
<td>`@ 00:36:12`</td>
<td>ℹ️</td>
<td>«MD5 inventata da Rivest tra il 1992 e il 1992»</td>
<td>Lapsus</td>
</tr>
</table>
## Cosa segnalare al docente
I due **errori sulle slide** (Vigenère e Diffie–Hellman) valgono una mail: sono refusi che si propagano a ogni edizione del corso, e sono proprio gli esempi su cui uno studente verifica di aver capito. Il resto sono lapsus verbali, che in una lezione parlata sono fisiologici.
## Nota di metodo
La **sostanza è corretta ovunque**. Tutte le definizioni — segretezza perfetta, la definizione a gioco, le tre proprietà di sicurezza degli hash, il length extension e il motivo dell'HMAC, la classificazione giuridica delle firme — sono esposte senza errori. E le verifiche per esecuzione hanno **confermato** i conti più impegnativi: la catena LFSR svolta a mano a schermo, il ciclo RSA, l'omomorfismo moltiplicativo, le quattro radici di Rabin, i parametri di SHA3-256.
