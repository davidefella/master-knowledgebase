# 01 - Introduzione al corso, cripto-agilità, hash e salting, cifratura simmetrica e a chiave pubblica, RSA

*DI-01, registrazione Teams del 07/10/2025 (portale), 1:48:12; parlato fino a 01:09:08. Integrazioni da Teams 1 (21/09/2026).*

> **Come leggere questo capitolo.** Gran parte della prima ora ripete la crittografia già introdotta nel corso di Cybersecurity, Cyber Intelligence and Data Privacy (guida [Cybersecurity](../06-cybersecurity-cyber-intelligence-data-privacy/README.md), capitolo 07, sezioni 11-17). Qui quelle parti sono riassunte con un rimando; sono scritte per esteso solo le cose nuove: cripto-agilità vista dalle carte e dai documenti, funzioni di hash, salting, demo CyberChef, crittoanalisi, RSA, curve ellittiche. Da 01:09:08 a 01:47:42 la registrazione 2025 **non ha audio** (silenzio digitale) mentre le slide avanzano: quella parte è ricostruita dalle slide e dalla lezione Teams 1 del 2026, e il docente la rispiega in DI-02.

## Indice

1. Il corso e il docente
2. Crittografia trasversale: triade del digital trust e privacy (rimando)
3. Cripto-agilità: carte di pagamento, documenti d'identità, lettori
4. Integrità: le funzioni di hash crittografiche
5. Collisioni
6. Hash delle password e salting
7. Laboratorio: SHA-256 e sale con CyberChef
8. Riservatezza: cifratura e crittografia simmetrica (rimando)
9. Crittografia a chiave pubblica (rimando)
10. Crittoanalisi e cripto-agilità come processo
11. RSA
12. La parte senza audio: curve ellittiche, casi d'uso, svantaggi della simmetrica, key wrapping
13. Glossario
14. Punti incerti
15. Esame

## 1. Il corso e il docente

*DI-01 @ 00:00:02*

Il docente si presenta senza webcam. Si occupa di cybersicurezza da più di 15 anni, ha lavorato nel settore pubblico, nel privato e come freelance, con esperienze "orizzontali oltre che verticali". Tiene anche il corso di Cybersecurity, Cyber Intelligence and Data Privacy dello stesso master. Lavora per la **Banca d'Italia** e precisa che partecipa al master **a titolo esclusivamente personale**: le opinioni espresse sono sue e non impegnano l'istituto. Si dissocia anche dal corso di fintech del master, di cui non è titolare. Ha insegnato e creato corsi analoghi per altri atenei, italiani e americani (*DI-01 @ 00:02:11*).

**Slide "Introducing the lecturer"** (*DI-01 @ 00:01:21*). Ing. Walter Arrighetti, Ph.D.:
- Ph.D. in Electromagnetism, Sapienza, 2007; laurea in Ingegneria Elettronica, Sapienza, 2002;
- certificazioni attive: CISSP, GCTI, CCSP, GRTP, GXPN, GDAT, C|EH;
- 2 brevetti, contributi a diversi standard tecnologici;
- carriera iniziata nella post-produzione cinematografica e VFX (cyber threat intelligence, content protection, anti-pirateria, fino al ruolo di CISO/CTO), poi security governance, identità digitali e servizi fiduciari, pianificazione e conduzione di audit di sicurezza;
- settore privato e pubblico e freelance, in Italia, in Europa, a Los Angeles e a Londra;
- insegna cyber intelligence a Tor Vergata, Roma Tre, UNINT, in passato alla John Cabot University;
- nel 2021 ha vinto il primo concorso nazionale per esperti di CTI, entrando nel CERTBI della Banca d'Italia; di recente è passato al Red Team della Banca.

### Integrazione Teams 2026 (lezione 1 2026)

*Sezione 1 (il corso e il docente)*

- Nel 2026 il docente aggiunge: carriera iniziata nel cinema quando la sicurezza dei contenuti era "già informatica" ma legata all'anti-pirateria, facendo cyber threat intelligence "quando ancora non si chiamava così"; ha cominciato "ricevendo verifiche di sicurezza" e poi si è specializzato nel condurle; negli ultimi anni si è specializzato nelle identità digitali, lavorando come consulente per l'**Agenzia per l'Italia Digitale** (AgID) "a cavallo del COVID". (Teams 1 @ 0:00:07-0:02:29)
- Stessa precisazione sul titolo personale, "come nell'altro corso che avete visto con me". (Teams 1 @ 0:02:25)
- Nel 2026 la lezione 1 non ripete la crittografia di base: il docente dà per visti chiave pubblica, hash, chiave privata, curve ellittiche e RSA (fatti nella lezione 7 Teams di Cybersecurity) e parte direttamente da "come si utilizza in pratica la crittografia a chiave pubblica", cioè dai contenuti della sezione 12 di questo capitolo e del capitolo 02. (Teams 1 @ 0:02:29-0:03:19)

## 2. Crittografia trasversale: triade del digital trust e privacy

*DI-01 @ 00:02:11-00:06:19*

La crittografia è "uno degli argomenti centrali" sia di Cybersecurity sia di questo corso, una disciplina trasversale: per questo il corso precedente si è chiuso parlando di crittografia e qui la si riprende "per un po' di lezioni". Gli altri corsi del master trattano i problemi matematici; qui l'obiettivo sono gli **utilizzi pratici**.

Il docente ripete brevemente:
- la **triade della sicurezza informatica** (integrità, riservatezza, disponibilità);
- la **triade del digital trust** (o della sicurezza dei dati), dove al posto della disponibilità c'è l'**autenticità**, "fondamentale di tutto questo insegnamento": il dominio che garantisce l'**origine del dato**;
- la **privacy** in senso tecnico: assicurarsi che i dati personali degli interessati (*data subject*) siano trattati conformemente a leggi e regolamenti, per l'europeo rispetto al GDPR.

**Slide "The Triad of Digital Trust"** (*DI-01 @ 00:04:37*) e **"The realms of Cryptography"** (*00:06:09*): sono le stesse slide della guida Cybersecurity, capitolo 07, sezione 11, a cui si rimanda per testo e commento.

La storia della crittografia viene saltata (*DI-01 @ 00:05:48*: "salto la lezione sulla storia della crittografia"; le slide scorrono in pochi secondi a *00:06:11-00:06:19*): vedi guida Cybersecurity, capitolo 07, sezione 12.

Gli algoritmi crittografici servono a presidiare **tutti e tre** i domini della triade del digital trust (integrità, riservatezza, autenticità) e, "se ci sarà tempo", anche la privacy. Si basano su problemi matematici la cui soluzione o "rottura" è demandata alla tecnologia (*DI-01 @ 00:06:53*).

## 3. Cripto-agilità: carte di pagamento, documenti d'identità, lettori

*DI-01 @ 00:07:31*

Gli algoritmi crittografici, anche se robusti, **non lo restano per sempre**. Pesano tutti i fattori della minaccia cyber visti in Cybersecurity (evoluzione continua della minaccia, temi geopolitici, economici, finanziari, psicologici: un attore oggi irrilevante per l'organizzazione può diventarlo domani, o viceversa), ma soprattutto la **tecnologia**: con il progresso scientifico e tecnologico un algoritmo robusto oggi rispetto a una certa minaccia potrebbe non esserlo domani.

Da qui la **cripto-agilità**: una **capacità organizzativa**, non solo tecnologica, perché migrare è un cambiamento aziendale, raramente di piccola scala. È la capacità dell'organizzazione di **migrare le proprie tecnologie crittografiche** (algoritmi, ma anche dispositivi hardware e software che li implementano, procedure, schemi crittografici) verso altre che le consentono di restare robusta rispetto alla minaccia di riferimento (*DI-01 @ 00:10:11*).

**Slide "Crypto-agility"** (*DI-01 @ 00:24:20*). Testo:

> Crypto-agility is the capability to enact technical, organisational and physical (e.g. logistics) procedures to migrate towards different cryptographic algorithms, on time before they are no longer considered robust.
>
> Quantum computing is a "*doubly*" convincing argument towards reaching crypto-agility, because:
> - current encryption, hashing and signing algorithms shall be broken by next-generation quantum computers;
> - threat actors who **harvest** cryptography-protected data, even if they can't exploit them **now**, could be able to **crack** them **later**, when they shall have availability of quantum computers (and algorithms).

(Nella slide i due incisi del secondo punto sono separati da trattini lunghi, resi qui con virgole.) Immagini: una carta *Visa Classic Credit*, una *student card*, una smart card *tivùsat 4K Ultra HD* con il modulo CAM, due finestre "Sicurezza di Windows" (inserimento del PIN della smart card, scelta del lettore *Alcor Micro USB Smart Card Reader 0*) e un facsimile di carta d'identità elettronica italiana. Il frame completo di questa slide nella guida Cybersecurity aveva il secondo punto tagliato: qui è leggibile.

> **Nota aggiunta:** come già osservato nella guida Cybersecurity (capitolo 07, sezione 13), il primo punto va preso con cautela per hash e cifratura simmetrica: l'algoritmo di Grover dà solo un vantaggio quadratico, per cui SHA-256/384 e AES-256 non sono considerati "rotti" dal calcolo quantistico; a rischio sono soprattutto RSA e le curve ellittiche (algoritmo di Shor). Il secondo punto è il noto scenario *harvest now, decrypt later*.

### L'esempio delle smart card

*DI-01 @ 00:10:48*

Carte d'identità elettroniche, passaporti e carte di pagamento sono tecnicamente **smart card**: dentro c'è un chip con memoria e processore; se la carta è contactless o NFC c'è anche un'antenna; se è *contact* ci sono i "piedini dorati" che toccano il lettore. Tutte hanno una **data di scadenza**. Ci sono motivi legali (regolamenti dei sistemi di pagamento e dei documenti di viaggio), ma c'è un motivo comune: la **cripto-agilità** (*DI-01 @ 00:12:57*).

Ogni pagamento con carta (o con smartphone e smartwatch, dove si usa il chip del telefono "ma il funzionamento è analogo") e ogni passaggio di un passaporto elettronico al gate o al lettore delle forze dell'ordine comporta operazioni crittografiche eseguite dentro la carta, per verificare l'identità della carta e del titolare.

Il meccanismo (*DI-01 @ 00:14:01-00:17:30*):
1. l'emittente (il ministero per i documenti, il circuito per le carte di pagamento) rileva, con un'analisi del rischio, che l'attore della minaccia rilevante sta acquisendo capacità che in futuro potrebbero rompere l'algoritmo usato;
2. se è cripto-agile, decide per tempo di adottare uno schema con un algoritmo più robusto e da una certa data emette carte esternamente identiche ma con chip più robusti;
3. poiché tutte le carte hanno una scadenza, dalla data di scadenza dell'ultima carta emessa con la vecchia tecnologia **tutto il parco carte** (passaporti, carte d'identità, carte di pagamento) sarà stato sostituito.

È un processo invisibile per l'utente, che vede solo le scadenze: le carte di pagamento qualche anno fa scadevano dopo 5 anni, oggi spesso dopo 4 o 3; i documenti d'identità di solito dopo 10. Se lo scenario della minaccia non cambia, la carta successiva avrà la stessa robustezza della precedente; se cambia, la scadenza programmata "nel DNA della carta" permette di pianificare l'evoluzione (*DI-01 @ 00:17:30-00:18:39*). Come si programma tecnicamente la scadenza (dentro i certificati) si vedrà più avanti nel corso.

La metafora dell'**asticella** (*DI-01 @ 00:19:11*): la difesa va tenuta "un pelo più in alto" della minaccia più alta nota. Nello sport l'asticella si alza dopo che il record è battuto; in sicurezza va alzata **prima**, perché l'atleta è l'attore della minaccia.

In termini tecnologici, la cripto-agilità è anche la capacità di **separare gli algoritmi crittografici dal resto della tecnologia**: se si riesce a cambiare l'algoritmo senza cambiare tutto il resto "si fa bingo", perché costo organizzativo ed economico sono minori (*DI-01 @ 00:19:52*).

### Non basta cambiare le carte: i lettori

*DI-01 @ 00:20:30-00:24:42*

Con dispositivi fisici non è possibile separare: le carte vanno lette, e una carta con un algoritmo nuovo richiede probabilmente **lettori nuovi**. Il docente usa l'analogia CD, DVD, Blu-ray: un Blu-ray in un lettore DVD non si legge, perché il laser non ha la frequenza giusta per solchi molto più piccoli. Cambiare l'algoritmo delle carte di pagamento significa cambiare tutti i POS di tutti gli esercizi; se i POS non leggono le carte nuove, la banca "si è data la zappa sui piedi". Per i documenti d'identità: se il gate dell'aeroporto non legge l'algoritmo nuovo il cittadino non parte, salvo un controllo manuale delle caratteristiche fisiche del documento, impossibile dove il controllo è solo elettronico. La cripto-agilità comporta allora acquisto, distribuzione e sostituzione di hardware **a livello globale**.

Per questo i documenti di viaggio sono normati a livello internazionale dall'**ICAO** (*DI-01 @ 00:24:10*), l'organizzazione internazionale dell'aviazione civile, che fra le altre cose definisce come sono fatti i passaporti per garantire l'**interoperabilità**: un cittadino con passaporto italiano, tedesco, russo, cinese o canadese deve poter passare dai gate di tutto il mondo. Lo stesso vale per i sistemi di pagamento. Il riferimento ai **wallet** (software negli smartphone che rappresentano documenti e carte) è anticipato: si vedranno alla fine del corso; dal punto di vista crittografico non cambia nulla fra carta fisica e virtuale, "dietro c'è sempre la crittografia" (*DI-01 @ 00:21:00*).

**Slide di sezione "Cryptology & Crypto-analysis"** (*DI-01 @ 00:25:02*): sopra lo sfondo, il dump esadecimale di una chiave privata EC in formato PEM/DER con la struttura ASN.1 annotata: `ECPrivateKey` di 119 byte, `ecPrivkeyVer1` = 01, `privateKey` di 32 byte, parametri di dominio `secp256k1` (OID 1.3.132.0.10), `publicKey` di 66 byte con coordinate x e y; una legenda dei tipi ASN.1 (02 Integer, 03 Bit String, 04 Octet String, 06 OID, 30 Sequence). Non commentata.

## 4. Integrità: le funzioni di hash crittografiche

*DI-01 @ 00:25:20*

Si parte dall'integrità invece che dalla cifratura, "per non annoiare", e perché le funzioni crittografiche a presidio dell'integrità hanno una caratteristica diversa da tutte le altre: sono **funzioni senza chiave**. Esistono anche funzioni di integrità con chiave, ma il corso non le tratta.

> **Nota aggiunta:** le funzioni di integrità con chiave sono i MAC, per esempio HMAC-SHA256: l'hash è calcolato insieme a una chiave segreta condivisa, e garantisce anche l'origine fra chi conosce la chiave.

**Slide "Integrity: Hash functions"** (*DI-01 @ 00:28:10*). Testo: "Cryptographic **hash functions** taking data of any lengths as input and mapping it into *h*-bits **digest\*** as output", con la notazione $\mathbb{Z}_2^{\mathbb{N}} \to \mathbb{Z}_2^{h}$; "Slight change in initial data completely changes its digest"; icone *data* e *hash function*; nota: "\* Digests (*impronte crittografiche*) are also colloquially, though improperly, called "hashes" in the jargon."

Terminologia (*DI-01 @ 00:26:08*): il risultato di una funzione di hash crittografica si chiama **digest**, in italiano **impronta crittografica**. Nel gergo, anche fra professionisti, il digest si chiama "hash", lo stesso nome della funzione: "come se chiamassi seno il seno di x". Nel corso, "hash" indicherà spesso il digest.

Le funzioni di hash si ottengono di solito **iterando molte volte una funzione più semplice**, che "sminuzza" (*to hash*) il dato in una sintesi di pochi bit e rimescola il risultato a ogni ripetizione (*DI-01 @ 00:27:16*).

Le **tre caratteristiche** (*DI-01 @ 00:27:49-00:32:28*):
1. **Lunghezza fissa.** Qualunque sia la lunghezza dell'input (finita: un bit, 12 bit, un exabyte), il digest ha sempre $h$ bit, la **lunghezza dell'hash**.
2. **Difficile da invertire.** Dato il digest, è computazionalmente difficile, rispetto alla capacità di calcolo attuale, risalire al dato originario. La non invertibilità matematica deriva dalla **non iniettività**: con output fisso di $h$ bit esistono infiniti (un'infinità numerabile) dati diversi con lo stesso digest.
3. **Difficile trovare collisioni.** Dato un messaggio (es. "the red fox jumps over the blue dog"), è praticamente impossibile trovarne un secondo, simile o diverso, con la stessa impronta. Una piccolissima variazione del testo produce un digest completamente diverso.

Le **collisioni**, messaggi diversi con lo stesso digest, esistono e sono infinite, ma la probabilità di trovarle è così bassa da essere "sotto ogni aspetto pratico irrilevante".

> **Nota aggiunta:** in letteratura le tre proprietà di sicurezza standard sono: resistenza alla **preimmagine** (dato $d$, trovare $m$ con $H(m)=d$), resistenza alla **seconda preimmagine** (dato $m$, trovare $m' \neq m$ con $H(m')=H(m)$) e resistenza alle **collisioni** (trovare una qualunque coppia $m \neq m'$ con lo stesso digest). La "terza caratteristica" descritta dal docente, con un messaggio di riferimento dato, è la seconda preimmagine; la resistenza alle collisioni in senso stretto è più forte e, per il paradosso del compleanno, costa circa $2^{h/2}$ tentativi invece di $2^h$. La "lunghezza fissa" è una proprietà della funzione, non di sicurezza.

### Hash come codici di integrità

*DI-01 @ 00:32:28-00:37:07*

Poiché le collisioni sono statisticamente irrilevanti e ogni modifica cambia il digest, gli hash si usano come **codici di integrità**. Esempio: un dato di 84 MB, se ne calcola il digest con **SHA-2 a 256 bit** e lo si conserva o lo si trasmette a parte. Il dato "fa il giro del mondo" fra cloud, applicazioni e soggetti; quando torna (o torna una sua elaborazione), si ricalcola l'impronta, o la si chiede a chi ha processato il dato, e **si confrontano 256 bit invece di 84 MB**. Il dato può essersi alterato per un attacco (l'uomo nel mezzo) ma anche per degradazione, canali rumorosi, cause endogene o esogene: in ogni caso si verifica l'integrità.

Chi confronta le impronte non ha bisogno di conoscere il dato, che può essere privato, riservato o segreto. Ottiene una certezza **non matematica** (le collisioni esistono) ma **effettiva**, finché l'algoritmo è robusto: se gli hash coincidono è lo stesso dato, se differiscono sono dati diversi.

Per questo l'hash è un buon candidato anche per la **riservatezza** e la **privacy**: si possono confrontare o memorizzare impronte invece dei dati veri (*DI-01 @ 00:37:07*).

## 5. Collisioni

**Slide "Hash collisions"** (*DI-01 @ 00:33:02*, mostrata durante la spiegazione delle collisioni). A sinistra lo schema classico *keys → hash function → hashes*: John Smith, Lisa Smith, Sam Doe, Sandra Dee mappati su 00…15, con John Smith e Sandra Dee che collidono su 02; notazione $\mathbb{Z}_{2^b}^{\mathbb{N}} \to \mathbb{Z}_2^{h}$. A destra una tabella: quanti valori di hash a 32, 64 e 160 bit servono per una data probabilità di collisione (per esempio 77163 valori a 32 bit, 5,06 miliardi a 64 bit e $1{,}42 \times 10^{24}$ a 160 bit per una probabilità di 1 su 2), affiancata da probabilità di riferimento (full house a poker 1 su 693, fulmine 1 su 576000, lotteria 6/49 1 su 13,9 milioni, attacco di squalo 1 su 300 milioni, meteorite sulla propria casa 1 su 182 trilioni). Testo:

> The data space (domain) is countably infinite (messages of *any finite* lengths, with *b*-bits blocking factor, can be hashed), whereas the hash-space is finite ($2^h$ codomain cardinality for a *h*-bits hash function), digests' pre-images are infinite sets: there are infinite messages that can be mapped to each digest → **collisions**.
>
> "Longer" hash functions (higher *h*'s) make collisions unlikely, thus harder to crack.

Verifica per esecuzione: la tabella segue l'approssimazione del compleanno $n \approx \sqrt{2 \cdot 2^h \ln\frac{1}{1-p}}$. Per $p = 1/2$: 77163 (32 bit), $5{,}06 \times 10^9$ (64 bit), $1{,}42 \times 10^{24}$ (160 bit); per $p = 1/10$: 30084, $1{,}97 \times 10^9$, $5{,}55 \times 10^{23}$; per $p = 10^{-18}$ a 160 bit: $1{,}71 \times 10^{15}$. I valori della slide coincidono.

## 6. Hash delle password e salting

*DI-01 @ 00:37:40*

L'uso più pratico degli hash: le **password**. Alcuni sistemi mal progettati memorizzano la password vera, per esempio il browser quando gli si chiede di salvarla. Per questo un attore della minaccia (anche un malware) che prende il controllo di un dispositivo per prima cosa cerca file di password in chiaro.

I sistemi sicuri memorizzano invece l'**impronta crittografica** della password. A ogni autenticazione il sistema calcola l'impronta di ciò che è stato digitato e la confronta con quella registrata: se coincidono, la password è ragionevolmente la stessa. Un attaccante che ruba il database ottiene gli hash, "con cui può fare tanti danni", ma non le password.

> **Nota aggiunta:** il docente dice che il sistema "trasferisce al sistema che controlla la password solamente l'impronta". Nella pratica comune la password viaggia (dentro TLS) fino al server, che calcola l'hash: se fosse il client a inviare l'hash, l'hash diventerebbe di fatto la password (è l'attacco *pass-the-hash* a cui il docente accenna subito dopo). Inoltre per le password non si usa un hash veloce come SHA-256 ma una funzione di derivazione lenta e con sale (bcrypt, scrypt, Argon2, PBKDF2), proprio per rendere costosa la forza bruta.

### Il sale

*DI-01 @ 00:39:50*

**Slide "Salting hashes… and other secrets"** (*DI-01 @ 00:45:46*). Testo:

> To counter threat actors' **cryptanalysis** capabilities (i.e. cracking / brute-forcing encryption or hashing), messages' **entropy** must be increased, by appending enough randomly-generated bits (commonly referred to as "**salt**") to the plaintexts prior to their encryption or hashing.
>
> Salt is a ***nonce*** («*a secret number used once*»). It is not secret by itself, yet re-hashing the same data (e.g. passwords) with different salts, yields different digests.
>
> A threat actor that only gets hashed-n-salted secrets may not detect where/whether they are re-used, hugely increasing security.
>
> **Salt** is to hashing like **I.V.** (initialisation vector) is to encryption.

Schema a sinistra: saliera con *Salt (abc123def456hij)*, *Welcome1* → *Hash* → *ENC(zsd#qh$35md)*. Schema a destra: *Password* → *Add Salt* → *PasswordS4LT* → *Hash function* → *39e19b234v32* → *Password Store* (*Hashed password + Salt (S4LT)*), con il sale S4LT salvato anche lui nel database.

Il procedimento (*DI-01 @ 00:39:50-00:45:39*): prima di calcolare l'hash si aggiunge alla password un piccolo dato casuale, il **sale**, detto anche **nonce** ("numero usato una sola volta"). Esempio: password `tempo123`; il gestore di posta genera il sale `ZSD#`, calcola l'hash di `ZSD#tempo123` e memorizza **sia il sale (in chiaro) sia l'hash**. Se l'utente riusa la stessa password per un servizio di pizza a domicilio, quel servizio genera un altro sale, `$35MD`, e memorizza l'hash di `$35MD tempo123`: i due hash sono per forza diversi.

Perché serve: il **riuso delle password** è uno dei comportamenti meno virtuosi. Senza sale, un attaccante che recupera l'hash di una password può "rispenderlo" su altri sistemi dove l'utente ha usato la stessa password, o confrontare gli hash fra database esfiltrati diversi per scoprire dove la password è stata riusata. Con il sale, chi compromette il servizio di pizza (magari con una postura di sicurezza più debole del gestore di posta aziendale) ottiene hash che non può confrontare con quelli di un altro sistema.

Il sale è memorizzato **in chiaro** perché serve a ogni verifica (si antepone alla password digitata prima di calcolare l'hash), ma questo non indebolisce le impronte, che restano difficili da invertire.

> **Nota aggiunta:** "nonce" sta per *number used once*; la slide lo glossa come «a secret number used once» ma subito dopo precisa che il sale "is not secret by itself", e il docente lo conferma (memorizzato in chiaro). L'effetto più importante del sale, oltre a nascondere il riuso, è impedire attacchi precalcolati (tabelle di hash e *rainbow table*) e il cracking simultaneo di molte password uguali: ogni hash va attaccato singolarmente.

## 7. Laboratorio: SHA-256 e sale con CyberChef

*DI-01 @ 00:45:39-00:51:15*

Il docente mostra **CyberChef** (`gchq.github.io/CyberChef`), "un giocattolino" gratuito, online o scaricabile, sviluppato dal **GCHQ**, l'agenzia britannica di intelligence dei segnali, per testare funzioni di codifica dei dati, non solo crittografiche. Lo metterà in chat perché verrà usato più volte nel corso. Non risponderà a domande sull'uso del software, "non è il software di per sé l'oggetto del corso", ma volentieri a domande sulle cose crittografiche provate con CyberChef (*DI-01 @ 00:50:44*).

Ricetta: operazione **SHA2**, *Size* 256, *Rounds* 64.

1. Input `Benvenuti al corso di Digita Identitiedd and Trust Services` (59 caratteri, con i refusi di digitazione in diretta) → output `cfefa87897e9136408cab67095224601bb39612a1a7f944f1fd8a9d3d814b63c` (*DI-01 @ 00:47:48*). Mentre digita, l'output cambia completamente a ogni carattere ma resta sempre lungo 256 bit (64 cifre esadecimali). Cambiando una minuscola in maiuscola, o una S in T (lettere consecutive in ASCII, un solo bit di differenza), l'impronta cambia del tutto. Il riquadro verde di CyberChef indica i **64 round**: la stessa operazione ripetuta 64 volte "sparpaglia" ogni bit su tutta l'impronta.
2. Sale: il gestore di posta genera un sale (a voce `$AC`) e lo antepone alla password; l'impronta risultante (a voce "96587…") viene salvata accanto al sale in chiaro. Al login, il sistema riantepone lo stesso sale a ciò che si digita e confronta.
3. Stessa password presso il servizio di pizza: nuovo sale `_F7`. Input `_F7Benvenuti al corso di Digita Identities and Trust Services` (61 caratteri) → output `a3ca82def937717f3daac699cdb4e72a00d072adf51fe423279c25d17782d0d5` (*DI-01 @ 00:49:48*): impronta totalmente diversa. Chi recupera questo hash e il sale `_F7` non può risalire alla password né accorgersi che è la stessa usata presso il gestore di posta.

Verifica per esecuzione (Python, `hashlib.sha256`): entrambi i digest letti a schermo coincidono con quelli calcolati sugli input mostrati. Per confronto, l'input corretto senza sale e senza refusi (`Benvenuti al corso di Digita Identities and Trust Services`) dà `9dba32b2781d2572ea5bd6c3802a5802b75c3ad192507e73503d838cc11ba0e5`. Il digest "96587…" del primo esempio con sale non è leggibile in nessun frame: [illeggibile].

## 8. Riservatezza: cifratura e crittografia simmetrica

*DI-01 @ 00:51:15-00:59:29*

Ripresa breve della guida Cybersecurity (capitolo 07, sezioni 15-16).

**Slide "Confidentiality: Encryption"** (*DI-01 @ 00:52:29*): plaintext → *Encryption* (chiave arancione della *key pair*) → cipher-text `A4$h*L@9. T6=#/>B#1 R06/J2.>1L 1PRL39P20` → *Decryption* (chiave verde) → plaintext. Testo: "Encryption via a robust algorithm means that it is **computationally hard** for adversaries who know the cipher-text alone to derive either the plaintext or the key to decrypt the cipher-text."

Le funzioni di cifratura combinano un dato in chiaro (*plaintext*) con un altro dato, la **chiave di cifratura**, e producono il **ciphertext**; per decifrare serve la funzione inversa e la **chiave di decifratura**. Le due chiavi, pensabili come numeri molto grandi, sono **matematicamente correlate**. Nel caso più semplice coincidono: una **chiave simmetrica**, usata per cifrare e decifrare.

**Slide "Symmetric cryptography"** (*DI-01 @ 00:59:29*): una sola chiave $\kappa^{\text{sym}}$ per entrambe le operazioni. Testo: "Digital analogue to previous-eras' cryptography, symmetric cryptography relies on *one* key represented as a *k*-bits string (roughly speaking, a usually very large number in a key-space of cardinality $2^k$), which is hard to guess and which is used for *both* encryption of the plaintext and decryption of its cipher-text. Common "classic" ciphers are: AES, Blowfish, DES/3DES, RC4, Serpent, SM4, Twofish."

Esempio tipico: **AES**, caratterizzato dalla lunghezza in bit della chiave: AES-256 usa una chiave di 256 bit. La robustezza sta nel fatto che chi conosce il ciphertext ma non la chiave ha una difficoltà computazionale a risalire al testo in chiaro o alla chiave (*DI-01 @ 00:53:26*).

**Algoritmi pubblici** (*DI-01 @ 00:54:49*): molte aziende vendono algoritmi brevettati e *closed source* sostenendo che la segretezza sia un presidio in più. Matematicamente ha senso, ma la storia dimostra che è molto più affidabile far verificare un algoritmo in modo indipendente, per anni, dall'intera comunità scientifica internazionale. Vedi guida Cybersecurity, capitolo 07, sezione 14 (security through obscurity).

Non tutti gli algoritmi vanno bene per tutti gli usi: un algoritmo **troppo robusto** rispetto all'avversario raggiunge l'obiettivo, ma a costi, complessità e spese inutili. L'obiettivo è sempre mettere l'asticella "un pelo" sopra l'avversario, e saperla **alzare** quando l'avversario cresce (cripto-agilità). Mettere subito l'asticella altissima può costare cento volte di più di alzarla domani; non è però una verità universale: chi distribuisce POS e carte in mezzo mondo fa bene a partire con una crittografia sufficientemente robusta, perché cambiarla ogni anno costerebbe molto di più. Serve sempre un'**analisi del rischio** tarata sull'organizzazione (*DI-01 @ 00:56:58-00:59:29*). Nel gergo crittografico l'attore della minaccia si chiama **avversario**.

## 9. Crittografia a chiave pubblica

*DI-01 @ 00:59:29-01:05:05*

Ripresa della guida Cybersecurity (capitolo 07, sezione 17, compresa l'analogia della moneta).

**Slide "Public-key cryptography"** (*DI-01 @ 01:02:06*): coppia di chiavi asimmetrica, $\kappa^{\text{priv}}$ o $\kappa^{\text{pub}}$ per cifrare, l'altra per decifrare; riquadro *Alice*: *Large random number* → *Key generation program* → chiave *Public* e chiave *Private*. Testo: "With asymmetric cryptography, decryption must be accomplished with the opposite key of the key-pair that was used for the encryption of a plaintext. It relies on solving number-theoretical / algebro-geometric problems, relatively easy to compute one way, yet computationally difficult to invert. Different algorithms follow radical approaches in key-pair definition. When **public** [**private**] is used for encryption, the private [public] key **must** be used for decryption. "Classic" ciphers are: RSA; ECDSA, ECDH, EdDSA (elliptic curve cryptography), ElGamal, DSS/DSA, Paillier."

Variante a *01:05:06*: "Private and public keys can be thought of as very large numbers (whose length is measured in bits): from the **private key** the **public key** can be easily derived; from the **public key** it's computationally hard (i.e. practically impossible) to derive the **private key**", con la moneta da 1 euro italiana del 2016 (l'uomo vitruviano) per metà oscurata.

Le due caratteristiche (*DI-01 @ 01:00:09-01:04:35*):
1. si basano su problemi di **teoria dei numeri** o **geometria algebrica** facili nel verso diretto e difficili da invertire; chi vuole rompere la crittografia deve risolvere il problema inverso;
2. se si cifra con una chiave si **deve** decifrare con l'altra; in quasi tutti gli algoritmi si può scegliere quale usare per cifrare.

Di solito si genera prima la chiave privata e da questa la pubblica (facile, a volte banale); dalla pubblica è praticamente impossibile risalire alla privata. Da qui i nomi: quella facile da derivare si può rendere **pubblica**, l'altra resta **privata**, "ce l'ha solamente chi la deve avere".

L'**analogia della moneta** (*DI-01 @ 01:03:26*): la moneta è quasi perfettamente simmetrica salvo la lettera R; chi conosce la metà con l'asimmetria (la chiave privata) ricostruisce tutta la moneta; chi vede solo l'altra metà (la pubblica) non sa a cosa sono attaccate le mani né come è orientata la R, e potrebbe immaginare tantissime "chiavi private" compatibili.

Le famiglie classiche più usate: le **curve ellittiche** (nomi che iniziano con EC o Ed) e **RSA** (*DI-01 @ 01:05:05*).

## 10. Crittoanalisi e cripto-agilità come processo

*DI-01 @ 01:05:28*

**Slide "Cryptanalysis and Crypto-agility"** (*DI-01 @ 01:05:28*; nel titolo la seconda parola è coperta da un riquadro di transizione). Testo:
- **Cryptanalysis** is the study and practice of analyzing and defeating cryptographic systems to reveal hidden information, often by finding vulnerabilities in encryption algorithms / implementations.
- **Crypto-agility** is an organisation's capability to shift its own technologies and/or processes to be always adopting robust cryptographic primitives and schemes over time.

Diagramma di sequenza: il *Server* dichiara di accettare gli algoritmi ABC e XYZ; il *Cryptographic System* dell'organizzazione accetta la configurazione ("System supports algorithms ABC & XYZ"); arriva la notizia "Algorithm XYZ is compromised"; il *System Administrator* rimuove XYZ ("System supports algorithm ABC"); il server cambia configurazione e accetta solo ABC.

Il docente dice che la slide "forse doveva stare prima": la **crittoanalisi** è la capacità di un ricercatore di sicurezza, anche benevolo, o di un attore della minaccia (l'avversario) di rompere la crittografia, cioè di risolvere il problema inverso; è lo studio e la pratica di analizzare e battere gli algoritmi trovandone le vulnerabilità, cosa che l'attore della minaccia fa "per mestiere" (*DI-01 @ 01:05:36*). Il diagramma, non commentato, mostra la cripto-agilità come processo operativo: togliere un algoritmo compromesso dalla configurazione senza fermare il servizio.

## 11. RSA

*DI-01 @ 01:06:11*

**RSA** è l'acronimo delle iniziali di **Rivest, Shamir e Adleman**, i tre matematici americani che alla fine degli anni '70 proposero questo schema. Si basa sulla **fattorizzazione** in numeri primi. I numeri primi hanno come divisori solo 1 e se stessi: 2 (l'unico primo pari), 3, 5, 7, 11, 13, 17, 19, 23 e così via. In crittografia si usano primi **enormi**, di centinaia o migliaia di bit.

La forza bruta (provare tutti i possibili divisori) è perdente; esistono tecniche sofisticatissime e parallelizzabili, ma con numeri di centinaia o migliaia di bit anche i calcolatori classici più potenti hanno difficoltà oggettive, più che a verificare se un numero è primo, a trovare i **divisori non banali** di un numero grande (*DI-01 @ 01:07:23-01:08:27*).

> **Correzione:** il docente elenca i primi partendo da "1, 2 che è l'unico numero primo pari, 3…": **1 non è un numero primo** (per definizione un primo ha esattamente due divisori distinti). Poco dopo dice "i divisori non banali di un numero primo": un primo non ha divisori non banali per definizione; il problema difficile è trovare i fattori primi di un numero **composto**, il prodotto $N = p \cdot q$.

In RSA la **chiave privata** è rappresentata da una **coppia di numeri primi molto grandi**, diversi fra loro, estratti a caso da un algoritmo (ogni estrazione dà primi diversi) e noti, come divisori, solo a chi deve averli (*DI-01 @ 01:08:27-01:09:08*). Qui finisce l'audio della registrazione 2025; il seguito (la chiave pubblica come prodotto dei due primi) è spiegato all'inizio di DI-02.

**Slide "RSA cryptography"** (*DI-01 @ 01:08:21*). A sinistra: *PRIVATE KEY* = due cancelletti rosso e verde ("a very large secret prime number" ciascuno) e una chiave; freccia "# × # ="; *PUBLIC KEY* = un cancelletto viola, "the product of those two very large prime numbers used to make the private key, which is very, very hard to reverse back", e una casa con la chiave sul tetto. In basso: "references: PKCS#1 version 2.2 (2012); IEEE 1363". A destra:

> All asymmetric cryptography relies on a few hypotheses (not just RSA crypto):
> - You must always decrypt using the *opposite* key of the key pair that was used for encrypting.
> - It is hard to *derive* the **private** key from the **public** key alone.
> - It is hard to derive the plaintext from the cipher-text without knowledge of the key used for decryption.
>
> Loosely speaking, for the **RSA** algorithm:
> - the *public* key is a **very huge** integer number $N$, product of only two very large **prime** numbers $p$ and $q$;
> - The *private* key is one of $N = p \cdot q$'s prime factors.
>
> This is why public keys can be known to anyone (including threat actors), whereas the strength of a cryptographic scheme is as strong as much are its private keys kept secret.

> **Nota aggiunta:** la slide stessa dice "loosely speaking". In RSA la chiave pubblica è la coppia $(N, e)$, con $N = p \cdot q$ e un esponente pubblico $e$ (di solito 65537); la chiave privata è l'esponente $d$ tale che $e \cdot d \equiv 1 \pmod{\varphi(N)}$, con $\varphi(N) = (p-1)(q-1)$. Conoscere $p$ e $q$ permette di calcolare $d$, per questo "la privata sono i fattori" è una buona intuizione; ma la chiave privata non è uno solo dei due fattori. Cifratura $c = m^e \bmod N$, decifratura $m = c^d \bmod N$. Le chiavi RSA attuali hanno $N$ di 2048-4096 bit, cioè primi di 1024-2048 bit (circa 300-600 cifre decimali).

## 12. La parte senza audio: curve ellittiche, casi d'uso, svantaggi della simmetrica, key wrapping

*DI-01 @ 01:09:08-01:47:42 (audio a -91 dB, slide che avanzano)*

Da qui la registrazione non ha voce: probabilmente il microfono del docente si è disattivato. Le slide scorrono avanti e indietro; il contenuto sotto è letto dai frame, e il commento a voce viene da **DI-02** (2025, primi 50 minuti, trattato nel capitolo 02) e da **Teams 1** (2026, integrato qui sotto). All'inizio di DI-02 il docente riparte da "la scorsa volta dovremmo essere arrivati a parlare della crittografia RSA. Potete confermarmi anche per chat che state vedendo le slide?".

**Slide "Elliptic Curve Cryptography (ECC)"** (*DI-01 @ 01:13:17*). Equazione in riquadro:

$$y^2 \equiv (x^3 + ax + b) \bmod p$$

"where $p \in \mathbb{P}$ while $a, b \in \mathbb{N}$ are (usually very large integers) which distinguish specific elliptic curves from one another." Immagini: i punti di una curva su un campo finito (griglia 0-250 con rette che si "avvolgono"), un toro con punti e geodetiche, e la costruzione geometrica dei multipli di un punto $G$ (tangente in $G$ → $-2G$, riflessione sull'asse x → $2G$, poi $4G$, $8G$…). Fonte citata: `https://neuromancer.sk`.

> **Nota aggiunta:** nelle curve standard $p$ è primo e $a, b$ sono elementi del campo $\mathbb{F}_p$, non necessariamente grandi: secp256k1 (la curva del dump ASN.1 della sezione 3 e di Bitcoin) ha $a = 0$, $b = 7$. La sicurezza poggia sul **logaritmo discreto su curva ellittica**: dato $Q = kG$, trovare $k$. La chiave privata è lo scalare $k$ (256 bit per secp256k1), la pubblica il punto $Q$. La figura con tangenti e riflessioni è proprio il calcolo dei multipli di $G$ per raddoppi successivi.

**Slide "Basic use cases of asymmetric ciphers"** (*DI-01 @ 01:14:34*). Due schemi affiancati:
- **Confidentiality (+ some integrity)**: Bob cifra "Hello Alice!" con la **chiave pubblica di Alice**, ottiene `6EB69570 08E03CE4`; Alice decifra con la propria **chiave privata**.
- **Authenticity (+ some integrity)**: Bob cifra "Hello Alice!" con la **propria chiave privata**, ottiene `6EB69570 08E03CE4`; Alice decifra con la **chiave pubblica di Bob**.

**Slide "Asymmetric for confidentiality and authenticity"** (*DI-01 @ 01:28:00*). Schema: *Bob's Public Key* + *Alice's Private Key* → *Combine keys* → `751A696C 24D97009` *Alice and Bob' shared secret*; e simmetricamente *Alice's Public Key* + *Bob's Private Key* → stesso segreto `751A696C 24D97009`. Testo:
- Using both parties' asymmetric keys provides both confidentiality and authenticity.
- Yet, symmetric algorithms are provably faster than corresponding asymmetric algorithms with comparable cryptographic strength.
- However, asymmetric cryptography (aka *public-key cryptography*) still offers several advantages over symmetric one, independently from the algorithms.

> **Nota aggiunta:** lo schema disegnato è un **accordo di chiave** (Diffie-Hellman, ECDH): ciascuno combina la propria chiave privata con la pubblica dell'altro e ottiene lo stesso segreto condiviso, che poi si usa come chiave simmetrica. Il commento a voce del 2026 (vedi sotto) descrive invece la doppia cifratura; sono due modi diversi di combinare le chiavi delle due parti. Diffie-Hellman è nominato dal docente in DI-04.

**Slide "Disadvantages of symmetric cryptography"** (*DI-01 @ 01:36:16*). Rete di sei computer, ciascuno con una chiave diversa per ogni altro (fonte: sciencedirect.com, *private-key cryptography*). Testo: "If $N$ parties were to mutually exchange confidential information with each other, then: $N(N-1)/2$ symmetric keys are needed (~5000 keys for 100 users; ~0.5M keys for 1k users); documents to exchange need to be re-encrypted multiple times, once for each sender–recipient." Verifica: $100 \cdot 99 / 2 = 4950$, $1000 \cdot 999 / 2 = 499500$.

**Slide "Asymmetric key wrapping"** (*DI-01 @ 01:40:31*, versione completa *01:47:27*). Schema: il plaintext è cifrato con una chiave simmetrica $\kappa^{\text{sym}}$ (*encrypted content*); la chiave simmetrica è cifrata con la chiave pubblica $\kappa^{\text{pub}}$ del destinatario (*encrypted symmetric key*); i due oggetti stanno in una **busta crittografica** (*cryptographic envelope*); il destinatario decifra con la chiave privata $\kappa^{\text{priv}}$ la chiave simmetrica, e con questa il contenuto. Testo: "Given their secrecy requirements, *symmetric* and *private* keys are commonly referred to as ***secret* keys**, as opposed to *public* keys."

### Integrazione Teams 2026 (lezione 1 2026)

*Sezione 12 (casi d'uso della chiave pubblica, svantaggi della simmetrica, key wrapping): nel 2026 la lezione 1 parte da qui*

- **Riservatezza.** Bob cifra "ci vediamo stasera alle 8 al cinema" con la chiave pubblica di Alice, che può avergliela data lei o che lui ha letto in un registro pubblico: è irrilevante, chiunque la conosce, anche Carl, l'uomo nel mezzo. Solo Alice, con la sua chiave privata, decifra. La crittografia "regge" finché gli algoritmi sono robusti e le chiavi private restano nella sola disponibilità dei titolari. (Teams 1 @ 0:03:19-0:06:25)
- **"Un po' di integrità".** In teoria, se Carl altera il messaggio, Alice decifrando otterrebbe testo senza senso e capirebbe che è stato alterato. In pratica il software di decifratura avverte prima che la chiave è sbagliata o il messaggio non è cifrato per lei. (Teams 1 @ 0:06:25-0:07:55)
- **Errore nella slide, segnalato dal docente.** Il crittogramma `6EB69570 08E03CE4` compare identico nei due esempi: è un refuso, con chiavi diverse i crittogrammi sarebbero diversi. (Teams 1 @ 0:07:55)
- **Autenticità: il passaggio logico inverso.** Bob cifra con la propria chiave privata; chiunque può decifrare con la chiave pubblica di Bob, quindi il messaggio non è riservato. Ma se lo si decifra con la pubblica di Bob e l'algoritmo è robusto, allora è stato cifrato con la privata di Bob, che solo Bob possiede: il messaggio ha origine da Bob. "È la chiave per capire tutto il meccanismo del digital trust." (Teams 1 @ 0:08:40-0:11:44)
- **Riservatezza e autenticità insieme**: doppia cifratura con le chiavi delle due parti e decifratura con le chiavi duali in ordine inverso; quale ordine sia più sicuro "non ci interessa ai fini del corso". (Teams 1 @ 0:11:44)
- **Simmetrica contro asimmetrica a parità di robustezza.** Gli algoritmi simmetrici sono computazionalmente più leggeri: il docente cita la stima secondo cui RSA-2048 equivale ad AES con chiave di 256 bit. Per un singolo documento fra due soggetti la simmetrica conviene. (Teams 1 @ 0:12:29-0:14:48)

> **Correzione:** secondo le tabelle di equivalenza NIST (SP 800-57 parte 1), RSA-2048 offre circa **112 bit** di sicurezza, cioè meno di AES-128; AES-128 equivale a RSA-3072, e AES-256 richiederebbe RSA di circa 15360 bit. Il senso del ragionamento (a parità di sicurezza la simmetrica usa chiavi molto più corte ed è più veloce) resta valido, ma il rapporto citato è sbagliato.

- **Kerberos** come esempio di schema solo simmetrico usato fra più soggetti per l'autenticazione (anni '80), poi irrobustito con la chiave pubblica; forse verrà visto parlando di identità digitali. (Teams 1 @ 0:14:48-0:15:35)
- **Il problema delle chiavi fra molti soggetti.** Rosso, giallo, verde, viola, azzurro devono scambiarsi messaggi a volte a due, a volte in gruppi: servono $n(n-1)/2$ chiavi simmetriche, che crescono col quadrato (circa 5000 per 100 soggetti, mezzo milione per 1000), e ogni nuovo arrivato in un gruppo di 1000 deve generare 1000 chiavi. Il **key management** "potrebbe divorare tutte le risorse". Inoltre un documento per 78 destinatari va cifrato 78 volte, e si perde il vantaggio di velocità. Con la chiave pubblica ogni soggetto conosce al più $n+1$ chiavi: le $n$ pubbliche (compresa la propria) più la propria privata. (Teams 1 @ 0:15:35-0:20:13)
- **Chiavi segrete.** Simmetriche e private si chiamano collettivamente **chiavi segrete**, perché non vanno condivise (la simmetrica solo fra sorgente e destinazione, spesso sistemi tecnici e non persone; la privata solo dal titolare). (Teams 1 @ 0:23:25-0:24:12)
- **Key encapsulation, passo per passo.** (1) L'applicazione genera una chiave simmetrica casuale specifica per quel contenuto, nel cinema e nel multimedia chiamata **content key**; (2) cifra il documento con la content key; (3) cifra la content key con la chiave pubblica del destinatario, o fa $n$ copie e cifra ciascuna con la pubblica di uno degli $n$ destinatari; (4) **cancella** la content key in chiaro; (5) mette ciphertext e chiavi cifrate in una **busta crittografica**, che può viaggiare in chiaro; (6) il destinatario estrae con la propria privata la copia della chiave cifrata per lui, decifra il contenuto e cancella di nuovo la chiave. La chiave simmetrica è detta **effimera**: vive in chiaro solo nella memoria dei software di cifratura e decifratura, "il meglio dei due mondi". (Teams 1 @ 0:20:13-0:29:34)

## 13. Glossario

| Termine | Significato nel corso |
|---|---|
| Cripto-agilità | Capacità organizzativa di migrare per tempo algoritmi, dispositivi, procedure e schemi crittografici verso altri più robusti |
| Smart card | Carta con chip (memoria, processore, eventuale antenna NFC o contatti): carte di pagamento, CIE, passaporto |
| ICAO | Organizzazione internazionale dell'aviazione civile; norma anche i passaporti per l'interoperabilità |
| Funzione di hash crittografica | Funzione senza chiave che mappa dati di lunghezza qualunque in un digest di $h$ bit, difficile da invertire e con collisioni difficili da trovare |
| Digest, impronta crittografica | Output della funzione di hash; nel gergo chiamato anche "hash" |
| Collisione | Due dati diversi con lo stesso digest |
| Sale, nonce | Dato casuale anteposto al segreto prima dell'hash; memorizzato in chiaro; rende diversi i digest della stessa password |
| CyberChef | Strumento del GCHQ per funzioni di codifica e crittografiche, usato nel corso |
| Chiave simmetrica | Unica chiave per cifrare e decifrare (es. AES-256) |
| Chiave pubblica / privata | Coppia asimmetrica: si decifra sempre con la chiave opposta a quella usata per cifrare |
| Chiavi segrete | Collettivamente, chiavi simmetriche e chiavi private |
| Avversario | Nel gergo crittografico, l'attore della minaccia |
| Crittoanalisi | Studio e pratica di analizzare e battere i sistemi crittografici |
| RSA | Algoritmo a chiave pubblica basato sulla difficoltà di fattorizzare $N = p \cdot q$ |
| ECC | Crittografia su curve ellittiche ($y^2 \equiv x^3 + ax + b \bmod p$) |
| Key wrapping, key encapsulation | Cifrare il contenuto con una chiave simmetrica effimera e questa con la chiave pubblica del destinatario |
| Busta crittografica | Contenitore unico con contenuto cifrato e chiavi cifrate |
| Content key | Nome della chiave simmetrica effimera nel cinema e nel multimedia |

## 14. Punti incerti

- Il digest del primo esempio salato in CyberChef (a voce "96587…", sale `$AC`) non compare in nessun frame: [illeggibile].
- Il titolo della slide di *01:05:28* è parzialmente coperto da un riquadro di transizione; "Crypto-agility" è dedotto dal testo della slide.
- La parte 01:09:08-01:47:42 non ha audio: non sappiamo cosa il docente abbia detto su curve ellittiche, casi d'uso e key wrapping nel 2025 in questa lezione; il commento viene da DI-02 e da Teams 1.

## 15. Esame

Nessuna indicazione d'esame in questa lezione. Il docente esclude esplicitamente le **domande sull'uso di CyberChef** ("non mi fate domande sull'utilizzo di CyberChef"), mentre le domande sulle funzioni crittografiche provate con lo strumento sono benvenute (*DI-01 @ 00:50:44*). Per il quadro completo vedi la pagina [Assessment](assessment.md).
