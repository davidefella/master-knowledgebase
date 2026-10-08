# 04 - Ransomware, ingegneria sociale e reti

> Fonte Notion: https://app.notion.com/p/3e712abc808d81368b4af25df18df5f2 — ultima modifica 2026-09-27T11:41:59.823Z

**Corso:** Cybersecurity, Cyber Intelligence and Data Privacy, docente Walter Arrighetti
**Registrazione:** CS-04 (portale, edizione 2025), Teams del 19/09/2025 (16:03 UTC), durata circa 01:44
**Fonti:** solo la registrazione (parlato e slide a schermo). Il docente non ha distribuito materiale.
> **Contesto.** La lezione riprende quella del giorno prima ("ieri", "la scorsa lezione"), cioè la lezione 3 del 18/09/2025, in cui il docente aveva introdotto il ransomware, la tassonomia degli attori della minaccia (attori statuali, cybercriminali, hacktivisti) e lo schema dell'infrastruttura dell'attaccante ("quella rossa della slide di ieri"). I rimandi restano come tali.
> **Guida unica.** Il capitolo segue la lezione 2025 (portale) e integra, nei riquadri "Integrazione Teams 2026", ciò che il docente ha aggiunto o cambiato nell'edizione 2026. Riferimenti: `CS-0N @` per il 2025, `Teams N @` per il 2026.
## Indice
1. Ransomware di prima generazione (richiamo)
2. Cybercrime-as-a-Service (CaaS)
3. Ransomware a estorsione multipla
4. Attori della minaccia dai confini sfumati e attribuzione
5. La minaccia interna (insider threat)
6. Attacchi nelle strutture ricettive: "hotel scams" ed evil maid
7. Ingegneria sociale: definizione, frode del CEO, frode del supporto tecnico, varianti del phishing
8. Anatomia di un'email di phishing (esercizio in aula)
9. Pretesti, siti facciata e typosquatting
10. Tipi di campagne di phishing: phishing, spear phishing, whaling
11. Attacchi alla supply chain
12. Slide saltate e avviso organizzativo
13. Sicurezza fisica
14. Sicurezza logica (o tecnica): il caso Stuxnet
15. Reti informatiche e modello a strati
16. Minaccia dall'interno, segmentazione e pivoting
17. Dalle LAN alla rete globale: MAN, WWAN, vista semantica
18. Glossario
19. Punti incerti
20. Esame
---
## 1. Ransomware di prima generazione (richiamo)
*CS-04 @ 00:00:02*
**Slide "Ransomware".** A sinistra, in alto, un *Attacker* (monitor con figura con cappello e mascherina) collegato con freccia bidirezionale al *Command and Control* (tre server). Dal C&C due frecce tratteggiate verso la vittima (server, figura con capelli azzurri, documento rosso): **5** "Give me the ransomware." e **6** "Here it is. Start encrypting."; sotto la vittima una griglia di file rossi e un monitor con "! \$". Testo in basso:
- *First-generation ransomware aims at implanting a malware into the victim's infrastructure that silently replaces as many files as possible (including across network shares) with encrypted versions of them.*
- *A "ransom" (e.g. via anonymous cryptocurrency) is requested as only means to provide the victim with decryption keys to get those data available again.*
In una seconda animazione (a schermo da 00:02:38) si sovrappongono tre schermate: la finestra rossa **"Wanna Decryptor 1.0"** ("Ooops, your files have been encrypted!", con i riquadri *What Happened to My Computer?*, *Can I Recover My Files?*, *How Do I Pay?*, i contatori *Payment will be raised on 5/15/2017 16:25:02* e *Your files will be lost on 5/19/2017 16:25:02*, la richiesta "Send \$300 worth of bitcoin to this address"); una cartella di Windows "test" con 151 file rinominati `1.doc.CONTI`, `1.jpg.CONTI`, `1.png.CONTI` e così via; due finestre di Blocco note `README.txt`, una leggibile ("Thanks for installing SecretSync...") e una piena di caratteri illeggibili, cioè lo stesso file prima e dopo la cifratura.
Il docente riprende il ransomware "canonico". Il malware viene impiantato in un sistema informatico e cerca di propagarsi, come i virus di una volta, sul numero più alto possibile di macchine: più computer infetta, più file diversi raggiunge. In un'organizzazione l'infezione parte tipicamente dalla postazione di un dipendente (il docente anticipa che nel corso della lezione si vedrà come avviene, di solito, questa **infezione primaria**). Il dipendente del reparto progettazione ha accesso ad alcune risorse di rete legate al suo lavoro, ma comunica anche, via posta elettronica o chat aziendale, con i computer di altri colleghi. Se il malware si propaga **lateralmente** e infetta le macchine di risorse umane, vendite, quality assurance, ognuna di queste ha accesso a file e cartelle diversi: le risorse umane ai fascicoli del personale, le vendite ai sistemi di fatturazione, alle offerte, ai preventivi, ai database dei fornitori. Più il malware si propaga lateralmente (i computer grigi nell'immagine), maggiore è il numero di file a cui ha accesso.
Il ransomware ha bisogno di **diritti di scrittura** sui file: li sostituisce, in modo più o meno silenzioso o lento, con varianti cifrate. La cifratura avviene con una chiave (il docente dice "una password" e rimanda alla parte di crittografia dei due corsi) che non è, o non dovrebbe essere, depositata sulla macchina. Per alcuni ransomware si è scoperto che la chiave si poteva recuperare dal malware stesso: facendo **malware analysis**, cioè cercando le vulnerabilità non del software ma del malware, si ricavava la chiave e si decifravano i file senza pagare l'attore della minaccia. Questo valeva per la prima generazione, "pre-Covid per così dire".
Il ransomware è usato prevalentemente da attori **cybercriminali** a fini **estorsivi**: si monetizza indirettamente il successo dell'attacco chiedendo un pagamento in criptovaluta. Dai primi attacchi, all'inizio degli anni Dieci di questo secolo, il ransomware è diventato una delle minacce cyber più rilevanti: nei rapporti nazionali ed esteri è sempre ai primi posti.
> **Nota aggiunta:** le schermate non vengono nominate dal docente. La finestra "Wanna Decryptor" è quella di **WannaCry** (maggio 2017, coerente con le date a schermo); l'estensione `.CONTI` è quella del ransomware **Conti**. Il primo ransomware noto (AIDS Trojan) è del 1989; la diffusione di massa con pagamento in criptovaluta inizia con CryptoLocker (2013), coerente con "inizio degli anni Dieci".
## 2. Cybercrime-as-a-Service (CaaS)
*CS-04 @ 00:04:37*
**Slide "Cybercrime-as-a-Service (CaaS)".** A sinistra, in un riquadro tratteggiato rosa con icone (hacker, mano con dollaro): *The provision of services to others to facilitate their commission of cybercrimes*. Sotto, un manifesto **"WANTED BY THE FBI – EVGENIY MIKHAILOVICH BOGACHEV"** con l'elenco dei capi d'accusa (*Conspiracy to Participate in Racketeering Activity; Bank Fraud; ... Money Laundering; Conspiracy to Commit Bank Fraud*), quattro foto e *\$ 3,000,000 Reward*. Al centro un fumetto arancione con la citazione *"They're financially lucrative with little chance of arrest."* attribuita a **McAfee**. A destra un diagramma a nove passi:
1. *Malware writer designs the framework for spreading malware*
2. *Attacker starts distributing malware for targeted infections*
3. *User is coerced to visit malicious domain; the embedded code exploits browser vulnerabilities to download malware using a drive-by-download attack* / *Credentials are stolen from target machines and data is sent back to C&C servers*
4. *Attacker retrieves credentials from the C&C server*
5. *Attacker initiates a stealthy connection using compromised proxy server*
6. *Victim's bank account is accessed through a compromised proxy server*
7. *Money is transferred to mules (agents)*
8. *Mules launder money, keeping a small percentage*
9. *Profit is shared among the end party, hacker, and the malware writer*
Rispetto alla classificazione della lezione precedente (attori statuali, cybercriminali, hacktivisti, più una "mezza categoria" che si vedrà oggi, sezione 5), ciò che è cambiato è il modo in cui il ransomware viene usato. I gruppi criminali che sviluppavano malware avanzati, ransomware e non solo, si sono **specializzati**, come accade nel crimine organizzato tradizionale: non effettuano più necessariamente l'attacco, ma lo **offrono come servizio**.
Da un lato vendono il malware ad altri attori della minaccia, che possono essere cybercriminali ma anche attori statuali o attivisti; i primi si possono definire cybercriminali perché producono il malware per profitto, vendendolo su un mercato nero. Nelle forme più avanzate vendono un **pacchetto completo**. L'analogia del docente è la pizza a domicilio: pagando il servizio di delivery si paga tutto l'indotto, la pizzeria remota (spesso un capannone in un sobborgo attrezzato con cucina e forno a mattoni), i pizzaioli, il fattorino. Allo stesso modo il CaaS offre agli attori di ogni matrice servizi di **personalizzazione del malware** e servizi di **call center** che, per telefono, SMS, WhatsApp, social o qualunque canale, raggiungono le vittime finali, che non sono vittime dirette dei cybercriminali ma dei loro committenti.
Le indagini degli organi investigativi di diversi paesi negli ultimi vent'anni hanno mostrato che dietro moltissimi attacchi non c'è un solo attore ma una **filiera**, "una catena dell'approvvigionamento, paradossalmente", come per un prodotto commerciale. Gli attori si passano la staffetta: alcuni sono **mandanti** che finanziano la campagna senza comparire, altri sviluppano il malware, altri lo personalizzano, altri ogni giorno stanno al telefono a contattare le vittime da imbrogliare. La catena è altamente infiltrata in alcuni settori e alcuni dei gruppi più pericolosi se ne sono serviti: il cybercrimine è diventato "un servizio in modalità cloud".
Contribuisce il fatto che molti software sono disponibili online, anche sulla rete normale, ma per un uso professionale e in scala vanno personalizzati. Il cybercriminale lavora con tool abbastanza standardizzati e li **"arma"** (*weaponization*): strumenti nati magari per la ricerca accademica diventano armi affilate, tagliate sulle specificità tecniche e organizzative di una vittima precisa. La catena che ne risulta è complessa, e per le forze dell'ordine è difficile risalire all'**attore originario**. Il docente anticipa che se ne parlerà con la cyber intelligence: dietro tecniche generate da un software usato in tante campagne è difficile capire se l'intento fosse criminale, attivista o se il mandante sia statuale, perché nell'"autopsia dell'attacco" questi soggetti appaiono comportarsi in modo simile.
> **Nota aggiunta:** Evgeniy Bogachev è ritenuto l'autore del malware bancario **Zeus/GameOver Zeus**; la taglia dell'FBI di 3 milioni di dollari è reale (2015). Il docente non commenta il manifesto; richiama solo "la vignetta in alto" (sezione 4).
## 3. Ransomware a estorsione multipla
*CS-04 @ 00:11:06*
**Slide "Multiple extortion ransomware".** Cerchi concentrici rossi, dall'interno verso l'esterno: **Single extortion** (*Encryption*), **Double extortion** (*Exfiltration*), **Triple extortion** (*DDoS*), **Quadruple extortion** (*Direct communication with customers and stakeholders*). A destra due riquadri: *Attacchi ransomware*: **1 attacco ogni 11"**; *Costo da ransomware (2021)*: **20 miliardi di euro**. In basso: *Source: European Commission*.
Il docente osserva che il ransomware non è più usato solo, come dieci anni fa, da cybercriminali con intento estorsivo ("sono riuscito ad attaccarti, ho cifrato i tuoi file, li rivuoi indietro? Mi devi pagare": un vero riscatto). Oggi il ricatto legato alla cifratura dei dati è **una leva estorsiva** accanto ad altre; si parla di ransomware a doppia, tripla, quadrupla estorsione, e in letteratura si trovano varianti anche più fantasiose.
- **Esfiltrazione** (seconda leva nella slide; il docente, dopo averla chiamata "terza", si corregge). Prima di cifrare, l'attore copia una parte dei dati nella propria infrastruttura, non necessariamente per spionaggio ma per ripubblicarli. Può pubblicarli subito su un forum o sul proprio canale Telegram ("guardate questi dati, magari firmati digitalmente, che ho estratto da questo ministero, agenzia, azienda"), una forma di **doxing** che rende impossibile alla vittima negare l'attacco e le rende quasi certo il danno reputazionale. Oppure li minaccia soltanto nella lettera di riscatto: "pagami in bitcoin entro tot; se non paghi non solo non ti do la chiave, ma pubblico i tuoi dati". Doppio danno, doppia leva.
- **DoS/DDoS.** L'attore bombarda la vittima con attacchi di negazione del servizio per farle capire che il danno può prolungarsi. Il sito non è disponibile, i clienti si insospettiscono, comincia a girare online la voce dell'attacco: anche una vittima che avrebbe voluto tenere segreto il fatto non può più negarlo, e la pressione psicologica sui vertici aumenta.
- **Comunicazione diretta con clienti e stakeholder** (quadrupla estorsione). L'attore non si limita ai forum: contatta direttamente i clienti importanti del bersaglio, di cui magari conosce l'identità. In alcuni casi reali ai clienti sono stati inviati loro documenti che avrebbe dovuto avere solo la vittima: "ho attaccato il tuo partner commerciale, ho esfiltrato i contratti riservati che stavate discutendo, lui è totalmente bucato; convincilo a pagare oppure gli distruggiamo tutto".
Si parla quindi di **leva estorsiva multipla**. Da qui la domanda: qual è la vera finalità dell'attore? Rendere il dato non disponibile cifrandolo è un attacco al dominio della **disponibilità**; chi usa un ransomware, magari acquistato da altri, può non chiedere affatto il riscatto e usarlo per danneggiare un soggetto, un concorrente commerciale o una nazione avversaria.
> **Nota aggiunta:** le cifre della slide (un attacco ogni 11 secondi, 20 miliardi di costo nel 2021) risalgono a una **previsione** di Cybersecurity Ventures, espressa in **dollari** (20 miliardi di USD di danni globali entro il 2021), ripresa poi da fonti istituzionali europee. Un attacco ogni 11 secondi corrisponde a circa 2,87 milioni di attacchi l'anno (verificato con python: 365·24·3600/11 ≈ 2.866.909). Il docente non commenta le cifre.
## 4. Attori della minaccia dai confini sfumati e attribuzione
*CS-04 @ 00:16:16*
Per questo la classificazione rigida della lezione precedente (cybercriminali, attori statuali, \[?\] attivisti) resta in molti casi valida, perché quei gruppi non sono spariti, ma i gruppi **"sfumano in grigio"** e non hanno più un solo intento. Il motivo è che lo scenario della minaccia cambia nel tempo: come detto nella slide sulla cyber security, chi se ne occupa guarda il **contesto esterno**, che cambia dal punto di vista politico (e quindi militare), tecnologico e normativo. Un attore che oggi punta al ministero di uno stato domani può trovare più conveniente, per motivi ideologici o commerciali, colpire il settore sanitario di un altro.
Spesso gli attori vengono raggiunti dalle forze dell'ordine e preferiscono **sparire**: viene arrestata la testa, o quella che si crede tale, del gruppo. Sono organizzazioni complesse e profonde, a volte vere cellule in cui non tutti sanno chi è l'altro, come nel crimine tradizionale. Dopo mesi o anni si riformano, in parte con le stesse persone e in parte no; altri membri si affiliano ad altre gang con intenti diversi, ma tecnicamente continuano a operare nello stesso modo. Quando si ripresenta un attacco tecnicamente simile, o rivendicato da soggetti che dicono di appartenere allo stesso gruppo, è difficile stabilire se sia davvero così e quale fosse l'intento originario. La catena del CaaS è lunga e ci si ferma spesso agli stadi iniziali: l'**attribuzione** dell'attacco è un compito molto difficile, che richiede tecniche investigative mutuate da varie discipline, incluso il **law enforcement**.
**Asimmetria.** Come dice "la vignetta in alto" (la citazione McAfee della slide CaaS), il cybercrime è un mestiere redditizio con poche probabilità di arresto. Non è impossibile essere presi: ogni giorno si leggono notizie di gruppi smantellati e persone finite in carcere, ma nel complesso il fenomeno resta **asimmetrico**.
**Aneddoto.** Un docente con lunga esperienza sugli attori statuali, quando Arrighetti era studente, ripeteva: "ricordatevi che gli attori della minaccia di questi gruppi altamente organizzati hanno i loro piani pensione". Sono persone che la mattina vanno al lavoro: hanno la lista di vittime da chiamare per frodarle, oppure uno o due computer controllati da remoto su cui osservano per tutto il giorno il povero dipendente vittima (come usa il computer, a quali servizi accede, le sue routine) per poi agire dopo giorni, settimane o mesi. A una certa ora staccano e vanno a casa: fanno un lavoro illegale, ma qualcuno li paga. Per quanto pubblicamente noto, questo è l'assetto tipico di un gruppo cybercriminale altamente organizzato.
### Integrazione Teams 2026 (lezione 1 2026)
*Capitolo 04, sezioni 4 e 7 (fattore umano, security awareness)*
- Dati ACN 2023: un'azienda su quattro senza capacità avanzate di risposta agli incidenti, poca sensibilizzazione; la **security awareness** funziona meglio come programma di coinvolgimento che come corso di formazione (letteratura scientifica) (Teams 1 @ 0:24\:11-0\:25:24).
- Dipendenza da prodotti di sicurezza di terzi, spesso esteri, non controllati: firewall e antivirus non bastano e il fornitore stesso può diventare vettore (Teams 1 @ 0:25:40).
## 5. La minaccia interna (insider threat)
*CS-04 @ 00:21:14*
**Slide "Threat actors – Insider threat".** In alto cinque icone: *Privileged users*, *Remote employees*, *Contractors*, *Former employees*, *Inadvertent insiders*. Sotto tre illustrazioni con didascalia:
- **Negligent**: *Insiders who pose an unintentional threat due to human error and lack of security awareness.*
- **Malicious**: *Current or former employees who abused their access to steal intellectual property for personal gains.*
- **Third - Party**: *Vendors who misuse their access and compromise the security of critical data.*
È la "mezza tipologia" annunciata. Riguarda dipendenti dell'organizzazione oppure contractor e consulenti (fiscali, legali, sanitari) che lavorano da casa o in sede ogni tanto, spesso in segmenti non di business e quindi parzialmente esternalizzati.
- **Negligenti.** "Non gliene frega niente" della sicurezza dell'azienda, magari perché è un cliente presso cui lavorano poche settimane prima di cambiare, oppure perché semplicemente non interessa loro.
- **Inconsapevoli.** Il fattore più importante e quello su cui i professionisti della sicurezza lavorano di più: persone in totale buona fede, non attori malevoli, che espongono l'azienda a rischi senza saperlo. Esempi: il laptop avuto per due settimane diventa "il loro laptop", ci installano di tutto e navigano dove non dovrebbero ("tanto se prendo un virus fra due settimane lo restituisco"); le password non sono quelle del loro conto in banca e quindi stanno scritte su un post-it.
- **Malevoli.** Chi è una minaccia perché vuole esserlo: tipicamente impiegati delusi (non hanno avuto l'aumento: "è brutto parlare di queste cose, ma accadono nel *day by day*") che hanno qualche diritto informatico in più e decidono di prendersi una piccola rivincita. Di solito sono azioni di poco conto, ed è per questo che questa categoria non si mette al pari delle altre tre.
Nell'analisi di grandi incidenti, anche recenti e accaduti in Italia, si vede però spesso che chi materialmente veicola l'attacco è un impiegato **incauto**, non adeguatamente formato e reso consapevole dalla propria organizzazione, oppure il dipendente **disamorato**, che da solo non sarebbe una vera minaccia ma viene **avvicinato** da un attore più organizzato. Questo cerca sui social e su LinkedIn profili adatti, lo convince, lo "aiuta" nella sua rivincita: "esegui questo software quando sei in azienda". Il software magari cerca foto compromettenti e le manda ai dirigenti minacciandoli, ma nel frattempo persegue l'intento del vero attore, che appartiene alle altre tre categorie. In questo caso l'insider non è la vera minaccia: è il **vettore** di un attore "di classe superiore", che sfrutta il fatto che il dipendente insoddisfatto o distratto, o il consulente di terze parti, abbia già "un piede tecnico o organizzativo" dentro l'azienda.
Chi opera da solo resta una minaccia: un amministratore di sistema arrabbiato può cancellare file e magari coprire le tracce, con danni anche rilevanti. Questo fenomeno, il **dipendente traditore** della letteratura anglosassone, è rilevante ma statisticamente non è quello che fa più danno sui grandi numeri. Sui grandi numeri contano gli attori altamente organizzati che si servono degli insider (dipendenti sbadati o inconsapevoli, disamorati o astiosi, terze parti con accessi privilegiati) per un attacco più profondo. Questo introduce attacchi non più basati necessariamente sul malware ma sull'**ingegneria sociale**.
## 6. Attacchi nelle strutture ricettive: "hotel scams" ed evil maid
*CS-04 @ 00:28:17*
### "Hotel" scams
**Slide ""Hotel" scams".** Due fotografie: il bancone di una *Reception* d'albergo con un cliente e una receptionist; una mano che fotografa con lo smartphone un passaporto statunitense (schermata dell'app "ID/Passport"). Nessun testo oltre al titolo.
Prima di parlare di social engineering, una deviazione: gli attori della minaccia sono organizzati, pazienti, e sanno quali vittime, o quale tipologia di vittime, colpire. Da alcuni anni si è rilevato che alcuni attacchi cyber avvengono nelle **catene alberghiere**. "Albergo" va inteso tra virgolette: vale per qualunque **struttura ricettiva**, anche lo Starbucks, la caffetteria, la libreria di turno, magari quella vicino a un ministero importante o a una "casa del potere".
- **Wi-Fi.** Queste strutture offrono Wi-Fi, spesso gratuito, come servizio in più; oggi con le tariffe flat se ne sente meno il bisogno, ma c'è ancora chi, pur avendo giga infiniti, preferisce il Wi-Fi della struttura. Spesso non è protetto: la password è in chiaro su un cartello davanti alla reception, o è uguale per tutti e viene data al check-in; anche con accessi personalizzati, la sicurezza di queste reti di solito è scarsa. Per un attore è facile inserirsi e **intercettare** le comunicazioni. Il docente rinvia la spiegazione tecnica al termine della parte di crittografia, probabilmente nel corso successivo.
- **Furto del documento d'identità.** Oggi di solito al check-in si fotografa il documento e lo si restituisce subito, ma in alcune strutture, soprattutto all'estero, lo si trattiene mezza giornata o due ore: che fine fa in quelle ore? E anche se viene restituito subito, le foto di tutti i documenti dei clienti finiscono magari su un iPad lasciato nel desk interno senza password, da cui qualunque dipendente o contractor può inviarle con un clic alla propria casella email. Il docente cita un incidente recente in una struttura italiana: sono stati trovati online database con centinaia e centinaia di foto di carte d'identità e patenti di cittadini italiani.
Che cosa c'entra con il cyber? In molti processi si può ottenere il reset di una password, o creare un nuovo account, **allegando via email la foto del documento**. Per un attore della minaccia avere l'immagine di un documento è quindi sufficiente per molte cose: è un processo ancora molto poco sicuro.
### Evil maid attack
*CS-04 @ 00:33:04*
**Slide ""Evil maid" attack".** A sinistra una persona in costume da cameriera con piumino. Sotto, la foto di un laptop aperto dall'interno, con un dispositivo collegato alla scheda madre e un cacciavite; un telefono accanto segna 09.34. In alto a destra un laptop con due antenne Wi-Fi esterne e terminali con testo verde. Sotto, l'output testuale di un avvio da chiavetta: `SYSLINUX 3.75 2009-04-16 EBIOS Copyright (C) 1994-2009 H. Peter Anvin et al`, `Waiting for the USB stick to init...`, `mount -r -t vfat /dev/sdb1 /mnt/stick`, `What do you want to do today: Run [E]vil Maid, [S]hell, [R]eboot`, `EvilMaid patcher v0.1`, `TrueCrypt Boot Loader detected`, `PatchAskPassword() failed`, `TrueCryptPassword(): Password is "..."`, `...sectors in /mnt/stick/sectors-2009-10-15-170716`, `You can reboot safely.`
L'attacco della **cameriera cattiva** (o del cameriere cattivo) prende il nome dal caso d'uso principale, ma vale per qualunque struttura ricettiva. È un attacco di **sicurezza fisica**, nel senso dei controlli fisici visti nelle lezioni precedenti. Si parte dal fatto che in una struttura dove crediamo il dispositivo al sicuro (laptop, ma vale anche per il cellulare) lo lasciamo incustodito, e qualcuno con un **passe-partout** può entrare sapendo quando non ci siamo. È un attacco sofisticato, perché richiede vari complici: chi sa in quale albergo siamo, chi sa a che ora usciamo e lo comunica, chi ha il passe-partout. Presuppone quello che la normativa europea chiama un **potenziale d'attacco elevato**. Si fa perché chiunque abbia **accesso fisico indiscriminato** a un dispositivo, con un po' di tempo, di solito ne vince la sicurezza.
Due esempi del docente:
- **Clonazione del disco.** Anche se il disco è cifrato, avendolo a disposizione per un'ora si smonta il laptop, si mette il disco su un dispositivo che ne fa una copia byte per byte (il tempo dipende dalla dimensione del disco e dalla velocità del dispositivo), si rimonta tutto e con calma si analizza la copia offline.
- **Keylogger fisico.** Esistono keylogger hardware: una retina con un contatto per ogni tasto, alimentata dalla batteria del laptop, in alcuni casi con una propria antenna Wi-Fi a corto raggio. L'attore si prenota la camera accanto o sta in macchina nel parcheggio; la sera, dopo cena, la prima cosa che digitiamo aprendo il laptop è username e password. Non serve nemmeno installare software malevolo: il dispositivo cattura il dato, e con quella password si sblocca la cifratura del disco.
"Quello che ho descritto è un attacco avanzato, ma esiste, si fa."
> **Nota aggiunta:** la schermata della slide è quella dell'attacco originale che ha dato il nome alla tecnica: l'**Evil Maid** di Joanna Rutkowska (Invisible Things Lab, ottobre 2009), una chiavetta avviabile che modifica il bootloader di **TrueCrypt** per registrare la password di cifratura del disco al successivo avvio. Il docente non lo cita; i suoi due esempi (clonazione e keylogger hardware) sono varianti dello stesso principio.
### Intelligence criminale
*CS-04 @ 00:36:32*
In tutti questi casi, dall'insider threat agli hotel scam all'evil maid \[?\], gli attori hanno spesso una rete criminale acquistata come servizio da una rete di CaaS, oppure offrono essi stessi questi servizi. Fra questi ci sono servizi di **intelligence criminale**, che analizzano per esempio i dipendenti di un'azienda per trovare i più vulnerabili. Su LinkedIn vedono che i manager più importanti cambiano ruolo ogni tre anni e trovano quello che fa carriera più lentamente, ogni cinque: ipotizzano che voglia "togliersi un sassolino dalla scarpa". Dai suoi profili social vedono a quali eventi partecipa (c'è chi si fotografa la pizza al ristorante "qui per il convegno tal dei tali"), fanno il giro degli alberghi convenzionati con il convegno per capire quali sono i più economici, si infiltrano, e sorvegliandolo capiscono quando esce dalla camera. Attacchi avanzati, "ma che ahimè accadono nel mondo reale".
### Integrazione Teams 2026 (lezione 6 2026)
*Capitolo 04, sezione 6 (hotel scam ed evil maid)*
- **Wi-Fi: la camera accanto.** Password unica per tutte le stanze e login col numero di camera: chiunque al bar della reception può connettersi. Per il whaling l'attore può prenotare una notte nella camera accanto alla vittima. Principio generale: servizio gratuito e obbligato, poco investimento, poca sicurezza, a volte connessione nemmeno cifrata. (Teams 6 @ 1:14:03 - 1:16:16 e 1:18:27 - 1:19:20)
- **Cosa si vede sulla rete dell'albergo (nuovo).** Con un'app gratuita di scansione (legittima se usata bene) si vedono gli IP dei dispositivi degli altri ospiti, dai MAC address il produttore della scheda o del telefono, con altre scansioni la versione del sistema operativo e le porte aperte, fino a tentare un contatto con il dispositivo. (Teams 6 @ 1:19:20 - 1:20:27)
- **Consiglio pratico (nuovo in questo capitolo).** Meglio usare i giga del proprio telefono in tethering; altrimenti comprare una VPN privata per quelle ore, che protegge soprattutto dagli altri clienti della stessa rete. Collegamento con Capitolo 05, sezione 13. (Teams 6 @ 1:20:46 - 1:21:39)
- **Documenti d'identità.** Obbligo di comunicare alla questura gli ospiti (in alcuni casi tramite app dedicate); la patente nell'app IO con codice a barre riduce le fotocopie, ma pochi alberghi la gestiscono. All'albergo interessa la carta di credito, il documento serve solo per l'obbligo di legge: "poco pagare, poca sicurezza", e le foto finiscono nel posto meno protetto. Un solo attacco riuscito a un grande albergo in alta stagione fa sottrarre migliaia di documenti, usati direttamente, alterati, o per impersonare la vittima presso banche ("ho perso la carta, ecco il mio documento"). Vale per chiunque chieda un documento, anche via email. Rinvio al corso sui trust service per i documenti firmati. (Teams 6 @ 1:21:39 - 1:25:14)
- **Evil maid, dettagli nuovi.** La ricognizione passa dai social (la foto della cena "terza notte di fiera"), dagli alberghi convenzionati con convegni e fiere, da un po' di HUMINT fingendosi dipendenti o amici; un complice segnala quando la vittima è lontana; talvolta l'attore si fa assumere come cameriera. Il keylogger fisico può rilevare i tasti anche dal suono o dal movimento, si alimenta dalla batteria e ha un'antenna nel telaio o nello schermo; il ricevente sta nella camera o nel bungalow accanto o parcheggiato fuori. La copia forense bit a bit del disco può richiedere decine di minuti o ore. (Teams 6 @ 1:25:22 - 1:30:15)
- **Contromisure (nuove).** Presidi tecnici: algoritmi crittografici robusti, sistemi che segnalano l'apertura del laptop da spento, pochissimi tentativi di password prima dell'autodistruzione del disco. Ma la difesa vera è la security awareness: i dispositivi con dati sensibili, anche se cifrati, vanno portati sempre con sé. (Teams 6 @ 1:30:15 - 1:31:13)
## 7. Ingegneria sociale
*CS-04 @ 00:38:14*
**Slide "Social Engineering attacks".** *Exploiting human behavioural weaknesses (fear, compassion, anxiety, love, anger, frustration, ...) to convince natural person(s) to perform (or not perform) actions which are, ultimately, advantageous to the threat actor.* Sotto, a sinistra, lo screenshot dell'email "Reconfirm your Johncabot Password" (sezione 8); a destra un'illustrazione: un ladro con canna da pesca che "pesca" da uno schermo, una donna preoccupata al computer, un uomo con occhiali che tiene davanti a sé la maschera di un criminale, e una finestra con **"Request from CEO – Subject: Immediate Wire Transfer"**.
Tutti gli attacchi visti rientrano nel **social engineering**. Può servire a reclutare una persona, per esempio l'impiegato insoddisfatto "lì lì indeciso" che, sufficientemente convinto e manipolato, diventa il vettore d'attacco di una minaccia più organizzata. Ma si usa anche contro persone che non sono bersagli altamente mirati. Consiste nello sfruttare le **debolezze della psiche umana**, qualunque aspetto: paura, orgoglio, ingordigia, amore, pietà, frustrazione, per convincere le persone a fare o non fare azioni funzionali all'attore. Le forme più blande e più diffuse, anche negli attacchi **a strascico**, sono rappresentate nella slide: a sinistra un tipico phishing, a destra la frode del CEO.
### Frode del CEO
*CS-04 @ 00:40:13*
È stata usata per sottrarre somme ingenti a molte aziende. L'attore manda un'email abbastanza convincente a chi ha **capacità dispositive**: qualcuno dell'ufficio del CFO, o un impiegato dell'ufficio acquisti con sufficienti poteri. L'email sembra arrivare dall'amministratore, dal "capo del capo", da un senior vice president: "sono in riunione negli Emirati Arabi, devo lasciare il cellulare di business in una scatola prima di entrare, fra due minuti non ho più accesso alla posta aziendale, mi serve assolutamente questa transazione per chiudere l'accordo; mandami la conferma alla mia email privata". L'email privata, naturalmente, l'ha creata l'attore. È un **pretesto plausibile**: "devo fare un bonifico consistente entro 10 minuti, te lo scrivo io direttamente, non fare cavolate". Molti dipendenti ci sono cascati: bonifico istantaneo o metodo non tracciabile, "boom, soldi scomparsi".
### Frode del supporto tecnico
*CS-04 @ 00:41:56* (slide commentata a *00:46:21*)
**Slide "Technical support fraud".** A sinistra la chat di uno smartphone con **"HitBTC Support @HitBTCAssist"**: *"This case usually takes 48 to 72 hours unless the customer contacts us, as you did."*, *"Well because your withdrawal is already put on the lengthy hold, the way we can process it now and this way we can verify your identity"*, *"Is if you complete the withdrawal while we watch on TeamViewer this way I can instantly process your withdrawal on my side as well"*, *"Are you familiar with the screenshare teamviewer ? It comes on all new macs and PC's."* Al centro un'illustrazione di un'operatrice con cuffie e una donna al telefono. In alto a destra una finta schermata blu **"CRITICAL WINDOWS ERROR"**: *WINDOWS FOUND 11 VIRUS ON YOUR COMPUTER. YOUR DEVICE HEALTH IS CRITICAL! DO NOT RESTART. CONTACT WINDOWS CERTIFIED TECHNICIANS ON (XXX)-XXX-XXXX IMMEDIATELY TO RECTIFY PROBLEM. ERROR CODE 0x2CA981 DRIVER_NOT_FOUND*, con sopra il popup del browser *"This page says: WARNING! YOUR DEVICE IS INFECTED WITH MANY TROJANS! FIREWALL IS AT 5 PERCENT! CALL CERTIFIED TECHNICIANS (XXX)-XXX-XXXX IMMEDIATELY TO PREVENT DATA LOSS"*.
Qualcuno telefona o scrive dicendo di essere dell'IT aziendale: "abbiamo trovato un virus sul tuo computer, dobbiamo entrare da remoto, ci serve la password". Il dipendente la dà e in cinque minuti hanno fatto tutto. Spesso la vittima viene fatta navigare su una pagina che simula un messaggio d'errore ("vai su questa pagina e dimmi se funziona"): compare *Critical Windows Error*, "allora il tuo computer è stato preso dal malware, devi subito darmi la password". È la versione digitale di truffe antiche: quel giorno stesso al docente aveva telefonato una sedicente compagnia di contatori elettrici; alla terza o quarta domanda hanno riattaccato.
### Le varianti del phishing
*CS-04 @ 00:42:58*
Il **phishing** avviene tipicamente via email, con messaggi predisposti per sfruttare una vulnerabilità psicologica e far compiere o non compiere un'azione. Accanto ci sono:
- **vishing**, che il docente descrive come la variante tramite videochiamata (chiamata Teams, WhatsApp e simili);
- **smishing**, solo tramite testo: un tempo l'SMS, oggi qualunque chat testuale;
- **quishing** (trascritto "quarrishing"), tramite **QR code**.
> **Correzione:** il **vishing** è il *voice phishing*, cioè il phishing tramite **chiamata vocale** (telefono, VoIP), non specificamente la videochiamata. Le chiamate Teams o WhatsApp citate dal docente vi rientrano in quanto chiamate vocali.
**Come funziona il QR code e l'attacco.** La fotocamera decodifica un codice a barre che contiene tipicamente un link: il menu del ristorante, le norme igieniche mentre si fa la fila, il sondaggio di gradimento del convegno. Scansionando, si va automaticamente al link. Alcuni smartphone mostrano prima il link: **prima raccomandazione del docente, guardate sempre il link prima di andarci**. Spesso però il link legittimo è comunque poco riconoscibile: chi fa un sondaggio usa un servizio gratuito o economico con un indirizzo indecifrabile; il ristorante "La Lampara" (nome di fantasia, "non ne sto sconsigliando nessuno") magari ha il menu su un sito tipo `fged2793462`, del tutto legittimo, solo la versione più economica che il gestore poteva permettersi. L'attacco consiste nell'appiccicare fisicamente un adesivo con un altro QR code, stampare un finto menu o appendere un finto cartellone all'evento. Il QR punta a un link che, nella migliore delle ipotesi, scarica un malware o presenta una schermata di login in cui autenticarsi.
### Integrazione Teams 2026 (lezione 6 2026)
*Capitolo 04, sezione 7 (ingegneria sociale, frode del CEO, varianti del phishing)*
- **Definizione ripresa.** Social engineering: sfruttamento delle caratteristiche psicologiche dell'uomo, non della macchina, per fargli compiere o non compiere azioni funzionali all'attore. Il fattore umano resta l'anello più sfruttato proprio perché le difese tecniche sono sempre più automatizzate. (Teams 6 @ 0:20:15 - 0:21:16)
- **Frode del CEO, versione 2026.** Il caso raccontato cambia rispetto al 2025 (Emirati Arabi): un'email vera, mostratagli in un corso da cui ha imparato, in cui il sedicente amministratore delegato scriveva da un indirizzo Gmail sfruttando un'informazione nota (era davvero in Cina per riunioni riservate): "mi hanno tolto il telefono, scrivo dal PC della sala", bonifico immediato a un IBAN, presentato come 1-2% di un contratto multimiliardario. Il dipendente ha bypassato gli schemi autorizzativi e i soldi sono andati persi. L'attore era un criminale comune, senza legami con attori statuali cinesi. (Teams 6 @ 0:23:21 - 0:25:06)
- **Contromisura procedurale (nuova).** Le aziende insegnano, soprattutto a chi può movimentare denaro in uscita, a rispettare sempre tutti i passaggi autorizzativi: "anche l'amministratore delegato apprezzerà" che si controlli due o tre volte. Più livelli di approvazione per importi elevati costringono l'attore a ingannare anche il terzo e il quarto livello. (Teams 6 @ 0:25:06 - 0:26:07)
- **Il pretesto è la parte curata**, oggi con l'aiuto dell'IA; la leva psicologica è il dipendente che non vuole scontentare il capo davanti a un'urgenza. (Teams 6 @ 0:22:15 - 0:23:03)
- **Phishing come categoria ampia.** Oggi si chiama phishing, per antonomasia, qualunque attacco di social engineering basato su un messaggio **asincrono**, cioè che presuppone una risposta non in tempo reale. (Teams 6 @ 0:28:13 - 0:28:51; ripreso a 0:48:41)
- **Smishing e vishing.** Smishing: interazione con messaggi di testo in tempo reale (il nome viene dagli SMS). Vishing: operatore che parla al telefono o in videochiamata. Rispetto al 2025 il docente include esplicitamente la chiamata telefonica. (Teams 6 @ 1:11:21)
- **Frode del supporto tecnico, dettagli nuovi.** Contatto via messaggistica aziendale, telefono, chat o WhatsApp; gli operatori delle organizzazioni criminali conoscono scuse e procedure aziendali e sfruttano il fatto che molti service desk sono esternalizzati (accento non madrelingua giustificato, "lavoro qui da una settimana"). L'obiettivo finale: credenziali, login su un link malevolo, oppure installazione di una versione modificata dell'app di supporto, non dallo store ufficiale, che installa il malware. (Teams 6 @ 1:10:45 - 1:13:33)
- **Consapevolezza come prima difesa.** La security awareness è "più forte di qualunque sistema software"; il docente dice di essere stato vent'anni senza antivirus senza mai prendere un virus. Non serve una preparazione tecnica per essere resi consapevoli. (Teams 6 @ 0:50:31 - 0:51:37)
### Integrazione Teams 2026 (lezione 6 2026)
*Caso 2026: furto di documenti a un fornitore di pagamenti elettronici (Teams 6 @ 0:17:18 - 0:20:58)*
- Il docente premette che per chi seguirà negli anni successivi sarà un incidente "dell'anno precedente", e che non fa il nome perché le informazioni diffuse a ridosso di un incidente non sono sempre esatte.
- Fatti riferiti: a un fornitore di servizi di pagamento elettronico (si corregge: "non di moneta elettronica") sono stati sottratti diversi gigabyte di scansioni di documenti d'identità dei clienti. L'attore li userà per assumere quelle identità o li venderà.
- Modalità, "a quanto sembra": nessuna violazione tecnica. Email di phishing che si spacciavano per un'**autorità di controllo** e chiedevano i dati con informazioni credibili; i dipendenti, per paura di sanzioni e per ottemperare a presunti obblighi normativi, hanno consegnato i dati in blocco attraverso un canale del tutto normale.
- Morale: gli attacchi diventano sempre più sofisticati e l'IA li farà crescere, ma il fattore umano resta l'anello più debole e più sfruttato. Rinvio al corso sull'identità digitale per l'importanza di proteggere questi dati.
## 8. Anatomia di un'email di phishing (esercizio in aula)
*CS-04 @ 00:46:53*
**Slide "Anatomy of a phishing email".** A sinistra lo screenshot dell'email:
- **From:** Microsoft Johncabot Outlook \<[no-reply-96561lRs@wyQ.apcprd01.prod.exchangepro.com](mailto:no-reply-96561lRs@wyQ.apcprd01.prod.exchangepro.com)\>
- **Sent:** Wednesday, September 12, 2018 9:23 AM
- **To:** (vuoto)
- **Subject:** Reconfirm your Johncabot password
- riga in grigio chiaro: *Message is from a Johncabot trusted source.*
- banner blu: **Reconfirm your Johncabot Password**
- *Your account password on ph\\*\*\*\*\*\*\*@[johncabot.edu](http://johncabot.edu) is due for reconfirmation and might be blocked.\*
- *You have limited time to make this corrections to avoid Johncabot Violation*
- link evidenziato *Reconfirm Johncabot Password* seguito da *Review Messages*
- in piccolo: *To stop separating items that are identified as clutter, go to Options. This system notification isn't an email message and you can't reply to it.* / *You received this mandatory service announcement to notify you about the important changes.*
A destra l'icona di una busta con amo e asterischi, *Phishing attack*, e una barra degli indirizzi con [**http://JJ.com**](http://JJ.com) (le J sono ami da pesca), firma [*drhack.net*](http://drhack.net).
Nelle versioni successive (a schermo da circa 01:02:17, testo da OCR, non verificato visivamente) il titolo diventa "Anatomy of a phishing email (reve\[...\])", compaiono rettangoli rossi del docente sugli indicatori e il tooltip del link: `http://www.oo-d.com/?ip=...` con la dicitura "Fare clic o toccare per aprire il collegamento".
L'email è arrivata realmente al docente nel **2018**, quando insegnava un corso simile alla **John Cabot University**, università americana a Roma. Quel giorno doveva parlare d'altro: fece uno screenshot, lo mise nelle slide e parlò solo di quello. Chiede agli studenti di individuare gli elementi che la rendono sospetta: "questa email è zeppa di **indicatori di compromissione**, l'ho scelta apposta perché una più facile da sgamare non mi era mai capitata".
**Falsa partenza (00:48:08).** Uno studente nota "HTTP e non HTTPS". Il docente chiarisce che l'immagine a destra ([http://JJ.com](http://JJ.com)) è decorativa e non c'entra con il testo dell'email: "colpa mia, la rimuoverò".
### Indicatore 1: il mittente
*CS-04 @ 00:48:38*
Christian osserva che l'indirizzo `...prod.exchangepro.com` ha poco a che fare con Outlook dell'università. Il docente dà il contesto. Il protocollo su cui si basa tutta la posta elettronica (anche la PEC, che ha "una struttura in più", di cui forse si parlerà nel corso successivo) è stato inventato più di 45 anni fa, ai tempi di **ARPANET**, quando su Internet c'erano 30-40 soggetti, università o agenzie della difesa americana. Era un protocollo semplice per scambiarsi messaggi, non cifrato, perché non era concepibile che un attore della minaccia si infilasse fra agenzie e università che si scambiavano dati di ricerca, e non era pensato per il boom dei 45 anni successivi. Non aveva e non ha sicurezza integrata; oggi è potenziato da "3, 4, 5 tecniche" che il docente non illustra ("roba per informatici"). In mancanza di queste, chiunque può registrare un dominio e mandare email da un indirizzo usa e getta, come `no-reply-96561...`, e scrivere nel campo **From** qualunque nome visualizzato: "Microsoft Johncabot Outlook". Esempio: niente vieta al docente di creare una casella e presentarsi come "Sergio Mattarella"; chi riceve legge in nero "Sergio Mattarella". Sul computer si vede anche l'indirizzo tecnico, da cui si può dedurre che è strano; sullo **smartphone**, per risparmiare spazio, si vede solo il nome, e l'indirizzo vero compare solo toccando il nome e aprendo un menu a tendina. Il dominio dell'università era ed è `johncabot.edu`.
È un indicatore di compromissione, **non una prova**: l'ateneo potrebbe aver esternalizzato il servizio a "[exchangepro.com](http://exchangepro.com), vattela pesca". Succede con i servizi di sondaggi come SurveyMonkey: fate un sondaggio per conto della vostra Acme S.r.l., l'email ha il logo dell'azienda ma arriva dal dominio del fornitore. Da solo non basta.
> **Nota aggiunta:** le "3, 4, 5 tecniche" che autenticano la posta sono principalmente **SPF**, **DKIM** e **DMARC** (più BIMI, ARC, MTA-STS). Il protocollo di posta è **SMTP**: la sua specifica di riferimento (RFC 821) è del 1982, mentre la posta elettronica su ARPANET risale al 1971; "più di 45 anni" è compatibile con entrambe le date.
### Indicatore 2: il pretesto e l'urgenza
*CS-04 @ 00:53:56*
Christian nota che non ha senso "riconfermare" una password: in caso di violazione, a livello procedurale, se ne crea una nuova. Il docente conferma: in tutti gli attacchi di social engineering c'è un **pretesto**. Il titolo è grande (blu, forse il colore della livrea dell'ateneo; il docente "avrebbe usato il rosso" per più urgenza) e la frase è un po' minacciosa. Non chiedono di cambiarla ma di rimetterla, probabilmente perché la pagina serve solo a farla digitare ("non lo so, non ho mai cliccato"). Sotto c'è il pretesto vero: "se non lo fai il tuo account potrebbe essere bloccato". Deve essere convincente e insieme instillare un **senso di urgenza** ("oddio, se non agisco subito mi bloccano l'account"), per farti pensare di meno, non darti il tempo di sospettare né di chiedere al vero servizio IT dell'ateneo. Con due indicatori così "già non mi sento tranquillo". Più avanti uno studente aggiunge il "tempo limitato" (*limited time*): il docente lo fa rientrare nello stesso pretesto.
### Indicatori 3 e 4: la lingua e il nome dell'ateneo
*CS-04 @ 00:56:34*
Anna (dai commenti in chat) segnala errori di inglese (*this corrections*) e "Johncabot" scritto attaccato ("Johncabot password non ha senso in inglese").
- **Correttezza linguistica.** Un errore d'ortografia può capitare in un'email importante, ma un'email automatica o con forte valenza istituzionale non può avere errori; la lingua deve essere da madrelingua, e anche minime sfumature sono un ottimo indicatore di falso. Il docente "torna sui suoi passi": oggi gli attori usano sistemi di **intelligenza artificiale** che traducono quasi perfettamente in qualunque lingua, quindi l'indicatore vale meno.
- **Sintassi del nome.** "John Cabot" (Giovanni Caboto) è nome e cognome: "Johncabot" tutto attaccato con la J maiuscola indica che il software che manda le email "a stampone" ha preso il dominio, tolto il `.edu` di primo livello e messo la maiuscola. Il docente ha visto casi in cui nemmeno la maiuscola veniva messa.
### Indicatore 5: il falso banner di fiducia
*CS-04 @ 01:00:12*
La riga *Message is from a Johncabot trusted source.* Giancarlo propone la mancanza di "www" nel link: il docente risponde che di per sé non è un problema. Il punto è un altro: un messaggio simile Outlook lo mostra, ma **fuori** dalla finestra del messaggio, sopra il campo From. Qui fa parte del corpo scritto dal mittente, con il font della dimensione giusta: è un messaggio **posticcio**. Se fossero stati usati i protocolli di sicurezza accennati, sarebbe stato il client di posta a dire in cima "ho verificato che chi ti scrive è davvero lui"; sapendo che non potrebbe comparire, l'hanno falsificato nell'unico posto disponibile, il testo. Chi sa come funziona Outlook lo individua.
### Indicatore 6: il saluto mancante
*CS-04 @ 01:02:20*
Sotto il banner, prima di *Your account password*, il docente ha tracciato un rettangolo rosso vuoto: che cosa manca? "Nulla di tecnico. È una comunicazione." Manca la **salutation** ("Gentile signora", "Caro utente"). Qualunque comunicazione minimamente seria ha una forma di introduzione, formale o meno; forse l'usanza si perderà, ma è ancora valida. Qui manca del tutto; in altri casi è **generica** ("Gentile utente", "Caro studente"), segno che chi scrive **non sa come vi chiamate**. Le email sono automatiche, ma per una questione di password il sistema sa chi siete: un sistema serio scriverebbe "Dear Professor Arrighetti" o "Greetings Walter". Anche qui non è una prova, ma insieme agli altri indicatori basta per dire che è un phishing.
Collegamento con l'osservazione di Anna: a volte le salutation sono "sofisticate" e deducono il nome dall'indirizzo. Se l'utente fosse stato John Cabot e avesse letto "Dear Johncabot", tutto minuscolo o con la maiuscola sbagliata, avrebbe dovuto insospettirsi. **Consiglio del docente:** non create caselle con nome e cognome scritti per bene; mettete un numero all'inizio, in mezzo o alla fine. Se vi scrivono "Dear Walter Arrighetti 92266" avete la prova che non sanno come vi chiamate e l'hanno letto dall'indirizzo. Con `walter.arrighetti@...` un software ci mette zero a togliere il punto, mettere le maiuscole e chiamarvi per nome e cognome: "l'ho visto fare".
### Indicatore 7: il link
*CS-04 @ 01:07:03*
Il link sembra portare a `johncabot.edu`, ma passando il mouse sopra, dopo un po', il fumetto mostra la vera destinazione: `http://www.oo-d.com`. Sugli smartphone è più difficile (tenere premuto, a volte tre o quattro menu a tendina), e spesso la gente non lo fa: "vabbè, mi fido" e clicca. Ma la **catena d'attacco parte quando cliccate**: accorgersi dopo ("ho visto l'indirizzo in cima al browser, torno indietro") non basta. Con malware particolarmente pericolosi, dotati di **rootkit**, basta cliccare perché il malware venga scaricato automaticamente, con una tecnica chiamata **HTML smuggling**, e si installi: bisogna vedere **prima** dove si sta per andare. Da solo, `oo-d.com` avrebbe potuto essere il servizio esternalizzato di reset delle password; insieme agli altri indicatori dava la certezza dell'attacco. Poco dopo telefonò al docente il presidente dell'università: l'email era arrivata anche a lui e voleva sapere che fare.
> **Nota aggiunta:** l'**HTML smuggling** consiste nel ricostruire il file malevolo direttamente nel browser (JavaScript, blob HTML5) per eludere i filtri perimetrali; di norma la vittima deve poi aprire il file scaricato. L'installazione senza ulteriori azioni dopo il solo clic corrisponde piuttosto al **drive-by download**, che sfrutta vulnerabilità del browser (è il passo 3 della slide CaaS e la voce *Drive by exploits* della slide sulle campagne). Nel tooltip della versione annotata (testo da OCR), il parametro `ip=` del link è la codifica **Base64 dell'indirizzo del destinatario** (vi si leggono i frammenti `b2huY2Fib3QuZWR1` = "[ohncabot.edu](http://ohncabot.edu)"): è un modo comune per tracciare quale vittima ha cliccato.
### Integrazione Teams 2026 (lezione 6 2026)
*Capitolo 04, sezione 8 (anatomia dell'email John Cabot)*
- **Nessun esercizio in aula.** Nel 2025 gli indicatori venivano trovati dagli studenti; nel 2026 il docente li espone da solo perché la sessione è registrata. (Teams 6 @ 0:27:15)
- **Classificazione rivista alla luce dell'IA.** Nel 2018 l'email si poteva quasi classificare come spear phishing (elementi grafici dell'ateneo, destinatari solo `johncabot.edu`); oggi, con i pretesti generati dall'IA, ricadrebbe nel phishing di più basso livello. (Teams 6 @ 0:28:01 e 0:32:53)
- **Contesto aneddotico diverso.** Il corso alla John Cabot era "più semplice", per studenti di una liberal arts university con background umanistico; nello stesso periodo il presidente dell'università ricevette una frode del CEO e chiese consiglio al docente. L'email mostrata era forse di una collega ("vedo PH"). (Teams 6 @ 0:26:27 e 0:41:27)
- **Mittente su smartphone.** Consiglio ribadito e reso operativo: toccare il nome del mittente e aprire le proprietà per vedere il vero indirizzo, sempre, prima di aprire link o allegati. Aggiunge che `exchangepro.com` non è nemmeno un dominio di Microsoft Exchange. (Teams 6 @ 0:34:08 - 0:35:41)
- **Errori di scrittura nelle comunicazioni legittime.** Conseguenza pratica nuova: chi scrive comunicazioni ufficiali deve evitare refusi, perché colleghi del docente hanno visto email legittime cestinate come spam per un typo nell'oggetto. (Teams 6 @ 0:35:57 - 0:36:32)
- **Falso banner di fiducia, spiegazione tecnica.** I sistemi reali (DLP, sistemi di prevenzione delle intrusioni sulla posta) aggiungono un avviso quando il mittente è esterno, registrato da pochi giorni, segnalato o non nell'elenco dei fidati, e lo mettono **fuori** dal contenuto; avvisano quando il messaggio potrebbe **non** essere autentico, mai il contrario. (Teams 6 @ 0:37:32 - 0:39:54)
- **Saluto e resistenza all'IA.** Consiglio già presente nel 2025 (indirizzi personali senza nome e cognome per esteso, per esempio con sigle e numeri), con un'aggiunta: il trucco resiste anche ai pretesti scritti con l'IA, perché l'IA non può inventare nome e cognome se non ci sono informazioni da cui dedurli. (Teams 6 @ 0:43:35 - 0:45:00)
- **Link e HTTPS.** Il link punta a un dominio (trascritto "[oomenod.com](http://oomenod.com)", nel 2025 `oo-d.com` \[?\]) che risulta usato in diverse campagne; il parametro nel link identifica la vittima che ha cliccato (coerente con la nota 2025 sul Base64). Il docente rimanda al corso sui trust service la spiegazione di HTTPS. Su tutti i sistemi operativi mobili oggi è possibile vedere il vero link, perché riconosciuta come caratteristica di sicurezza importante. (Teams 6 @ 0:45:24 - 0:47:04)
## 9. Pretesti, siti facciata e typosquatting
*CS-04 @ 01:09:10*
**Slide "Health-related social engineering scam".** Tre esempi:
- email **"COVID-19 Payment"** da *COVID-19 Relief \<*[*Renee.Tiberio4695604@gmx.com*](mailto:Renee.Tiberio4695604@gmx.com)*\>*, *Wednesday, March 18, 2020 at 6:17 PM*: *Immediate check of \$2,500.00 -/AUD for those who choose to stay at home during the Coronavirus crisis. Here is the form for the request. Please fill it out and submit it no later than 25/03/2020. Password is 1234*;
- SMS di *Sunday, 22 March 2020* (mittente "COVID"): *URGENT: UKGOV has issued a payment of 458 GBP to all residents as part of its promise to battle COVID 19. TAP here *[*https://uk-covid-19.webredirect.org/*](https://uk-covid-19.webredirect.org/)* to apply*;
- email da [*public-safety@yourmunicipality.it*](mailto:public-safety@yourmunicipality.it), *Subject: DANGER: Smallpox outbreak in public transport !*: *You have been likely exposed to smallpox travellers on today's metro line leading you to work. If you are in close-contact with a smallpox infected traveller for more than 5 minutes chances are you are infected as well. To be sure whether you have been in contact with such ill persons we have set up an anonymous contact-tracing app, accessible using your own Gmail account. Click here, login with your Google credentials, answer 3 easy anonymous questions and we'll tell you if you're likely gonna die of smallpox or not.*
Gli attacchi di social engineering usano pretesti di ogni tipo. Oltre al classico "se non lo fai ti blocco l'account", durante il Covid sono fioccati attacchi basati sulla paura del contagio, sulla pietà o sull'avidità delle persone. Durante la guerra russo-ucraina il docente ha visto "le cose più bieche", che sfruttavano la pietà per un paese in sofferenza simulando situazioni umanamente condannabili. Come diceva un suo docente, gli attori della minaccia sono come i veri criminali: "non c'è fondo" a ciò a cui possono arrivare.
Un'email di phishing come quella della sezione 8 **non ha di per sé contenuto malevolo**: probabilmente passerebbe un antivirus; non passerebbe forse un sistema di controllo più approfondito, che oggi anche con l'intelligenza artificiale sa riconoscere un pretesto (il docente rinvia a un esempio più calzante quando si parlerà di sicurezza dell'IA).
**Slide "Phishing attacks".** Diagramma: *Hacker* → **1.** *Attacker sends phishing mail to target* → *Target*; **2.** *Victim clicks on Phishing link and visits fake website* (verso *Phishing Website*); **3.** *Hacker collects important credentials*; **4.** *Hacker uses victim's credentials to access private information* (verso *Original Website*). In basso a sinistra una vecchia pagina di Facebook ("Facebook helps you connect and share with the people in your life", "Create your account") con la scritta rossa **Fake Page** e una freccia **Hacker's URL** sulla barra degli indirizzi (`https://www.facelook.com/fakepage.htm`); a destra una finta finestra di login Microsoft ("Sign in", "Only recipient email can access shared files") sopra un documento sfocato.
Spesso il phishing invita ad andare su un **sito facciata**, che simula quello vero. La schermata, "che mi porto appresso perché è fatta bene", è la pagina di login di Facebook di circa una dozzina di anni fa, identica "al pixel". Unico indizio: il dominio [**facelook.com**](http://facelook.com), un caso di **typosquatting**: un dominio con un piccolo errore tipografico, che in realtà era semplicemente un dominio libero, registrato dall'attore. Può essere anche la pagina aziendale dove vi autenticate per scaricare il menu della mensa. Il sito è un **sifone**: le credenziali finiscono subito in un sistema controllato dall'attore. A volte il sito vi reindirizza sulla pagina vera, incolla le credenziali e preme "login" per voi: con un'attesa un po' più lunga vi ritrovate autenticati e non vi accorgete di nulla. Altre volte mostra una pagina bianca, e solo guardando la barra degli indirizzi vi chiedete dove avete messo le credenziali. Dietro non c'è una persona che aspetta ma sistemi automatici: in meno di un secondo si autenticano sul sito vero al posto vostro, vi tolgono l'accesso e dispongono operazioni.
**Osservazione di Anna (01:14:32)** (non udibile nella registrazione): essere troppo prudenti o paranoici fa rischiare il contrario. Il docente concorda: i sistemi antifrode e antivirus funzionano proprio così, con **soglie di paranoia** ("si chiama in gergo tecnico paranoia"), tarate con un processo di *trial and error* come l'addestramento del machine learning: se si hanno troppi **falsi positivi** si tara in un verso, se troppi **falsi negativi** nell'altro, fino a trovare una quadra.
### Integrazione Teams 2026 (lezione 6 2026)
*Capitolo 04, sezione 9 (siti facciata, typosquatting)*
- **Credential phishing e payload phishing (distinzione nuova).** Il phishing usa due tecniche distinte: il **credential phishing**, che porta su un sito civetta per rubare le credenziali, e il **payload phishing**, che fa scaricare un malware tramite allegato (esempio: il "verbale d'arresto" in PDF), tramite link a un sito di download o tramite HTML smuggling con scaricamento anche invisibile e autoesecuzione. (Teams 6 @ 1:01:51 - 1:03:05)
- **Typosquatting, percezione della lettura.** Spiegazione nuova del perché "facelook" inganna: leggendo in fretta guardiamo le lettere con aste e le doppie; la "l" sembra una "b" senza pancia e la "oo" viene letta come parte attesa della parola. Il termine typosquatting vale anche per la sostituzione di singoli caratteri nei testi. (Teams 6 @ 1:04:00 - 1:05:29)
- **Cosa fa il sito civetta con la password.** Il docente contrappone il sito vero, che secondo lui invia al server l'email e l'hash della password in un canale HTTPS, al sito finto, che invia email e password in chiaro al server dell'attaccante. Vedi "Divergenze" per la precisazione. (Teams 6 @ 1:05:45 - 1:07:07)
- **Il secondo fattore non salva (argomento nuovo).** Se c'è l'autenticazione a due fattori, il sito finto mostra anche una finta seconda pagina, raccoglie il codice e il sistema automatico (non "Giovanni con la felpa col cappuccio") lo usa entro pochi secondi sul sito vero; poi cambia subito la password, oppure resta sottotraccia se gli serve l'account come ponte per scrivere ai contatti. A volte rimanda la vittima loggata sul sito vero; se deve fare qualcosa di pericoloso mostra invece un errore "riprova tra 5 minuti". (Teams 6 @ 1:05:45 - 1:10:12)
- **Browser in the browser.** Attacchi più complessi mostrano finte pagine di autenticazione Microsoft o Google, a seconda dell'authenticator presunto, che si spacciano per una finestra separata del browser. (Teams 6 @ 1:10:12 - 1:10:45)
## 10. Tipi di campagne di phishing
*CS-04 @ 01:15:04*
**Slide "Phishing campaign types".** Piramide a tre livelli, con etichette a sinistra e caratteristiche a destra:
<table header-row="true">
<tr>
<td>Livello</td>
<td>Nome nella piramide</td>
<td>Caratteristiche</td>
</tr>
<tr>
<td>**whaling** (vertice)</td>
<td>*Targeted espionage*</td>
<td>*Target is intellectual property or operational data*; *Warrant specific exploit research*; *High potential revenue per unit*</td>
</tr>
<tr>
<td>**spear-phishing**</td>
<td>*Spear phishing*</td>
<td>*Ability to act is targeted*; *Medium revenue per unit*; **BBB/IRS/DOJ spear phishing**</td>
</tr>
<tr>
<td>**phishing** (base)</td>
<td>*Mass internet attacks*</td>
<td>*Computing power or ability to act is targeted*; *Low revenue per unit*; **Drive by exploits**</td>
</tr>
</table>
- **Phishing** (quello che il docente chiamava "a strascico"). Lo stesso messaggio a un numero elevatissimo di persone, centinaia di migliaia di indirizzi al giorno, spesso generati a caso sperando che esistano. Pretesti fatti male, errori di grammatica, a volte nemmeno tradotti (il docente ha ricevuto un messaggio "delle Poste" tutto in inglese, con il logo fatto male), personalizzati spesso in automatico. Basso livello di sofisticazione, non mirati; ma se su centinaia di migliaia due abboccano e rubano migliaia di euro, "sono soldi ben spesi".
- **Spear phishing**, la pesca con l'arpione. L'attore sceglie uno o più bersagli specifici, per esempio un settore merceologico: gli abbonati Netflix e Amazon. Manda comunque a molte persone, ma email fatte bene, con un **sito civetta** curato e procedure commerciali analoghe a quelle vere; tipicamente a un numero limitato di persone, magari clienti di lunga data di cui ha trovato credenziali online.
- **Whaling**, la pesca alla balena. Mira a specifici individui di una specifica organizzazione, con ruoli importanti non necessariamente nella gerarchia: anche amministratori di sistema che hanno password per accedere ai computer. Le email sono perfette ("non trovate un errore grammaticale neanche con un esperto di lettere"; un'email come quella della sezione 8 non farebbe mai parte di un whaling). Conoscono il bersaglio e **simulano le procedure interne**: se serve l'autorizzazione di una certa persona per un pagamento lo sanno, perché hanno fatto prima un'operazione di intelligence, e sanno a quale unità o divisione appartenete. Attacchi molto mirati, spesso di attori con **potenziale d'attacco elevato**, più difficili da individuare, rivolti a uno o pochissimi individui.
> **Nota aggiunta:** BBB, IRS e DOJ sono il Better Business Bureau, l'Internal Revenue Service (fisco USA) e il Department of Justice: enti di cui lo spear phishing negli Stati Uniti imita spesso le comunicazioni. Il docente non commenta queste sigle.
### Integrazione Teams 2026 (lezione 6 2026)
*Capitolo 04, sezione 10 (tipi di campagne)*
- **Numeri e analogie aggiornati.** Phishing "a strascico": anche l'1% su 10.000 email in qualche mese può fruttare centinaia di migliaia di euro. Spear phishing: bersaglio preparato, pochi soggetti con caratteristiche comuni (per esempio tutti i dipendenti di un'azienda, con email che ne imita lo stile); su 100 dipendenti ci si aspetta una decina di successi. Whaling: uno o pochissimi bersagli, anche di organizzazioni diverse per attivare una catena di compromissione precisa; basato su **prepositioning** (attacchi precedenti per raccogliere informazioni); esempi: il CFO, "il politico di turno". (Teams 6 @ 0:28:51 - 0:32:49)
### Integrazione Teams 2026 (lezione 6 2026)
*Phishing nell'era dell'IA (Teams 6 @ 0:52:22 - 0:57:23)*
- Negli ultimi anni i tentativi di phishing generati con IA "di frontiera" sono moltissimi. Un'IA oggi non commetterebbe gli errori della email John Cabot: prende il logo dall'organizzazione e costruisce un'email graficamente perfetta.
- Tecnica di raccolta dei template: l'attore dialoga prima con il supporto tecnico del bersaglio per ottenere, anche dal secondo o terzo livello, un'email formale di una persona di alto grado, da cui copiare firma, font, colori, loghi.
- Evoluzione della lingua: vent'anni fa il phishing in italiano era quasi impossibile; poi traduttori automatici e sistemi di machine learning; da 5-6 anni i testi sono grammaticalmente corretti. L'indicatore residuo era il **tono**: chi scrive un falso atto istituzionale deve creare urgenza mantenendo il tono giusto, e spesso non ci riusciva.
- Esempio 2025: il falso "verbale d'arresto" della Polizia di Stato inviato da Gmail con PDF infetto. La Polizia non scriverebbe da Gmail; al massimo userebbe PEC, SEND o una notifica sull'app IO, "ma più probabilmente sarebbero venuti a casa".
## 11. Attacchi alla supply chain
*CS-04 @ 01:18:54*
**Slide "Supply chain attacks".** A sinistra loghi: **MOVEit**, **3CX**, **CROWDSTRIKE**, **PyTorch**, il logo **Microsoft** con quello di **Exchange**, **MAERSK**, **solarwinds**. A destra uno schema su fondo blu: *Attacker* → riquadro *Service Provider* (icona di un computer, poi codice `</>` + icona: *Product/service infected*) → frecce verso tre organizzazioni (edificio circondato da persone). Didascalia: *Multiple companies compromised through trusted channels*.
Già descritti nella prima lezione, qui con qualche dettaglio in più. In uno dei modi possibili, "perché non si veicola solo così", l'attaccante, anziché colpire direttamente tre organizzazioni (in celeste nell'immagine), individua un **prodotto software, o hardware, molto utilizzato**, magari senza sapere quali aziende lo usano. Se trova una vulnerabilità e riesce a entrarci, **modificando il codice sorgente** per inserirvi malware oppure sfruttando il **canale di comunicazione** con cui il prodotto dà supporto tecnico, aggiornamenti o dati ai clienti (esempio: un software che distribuisce mappe stradali aggiornate), si ritrova "nella pancia" di tutti i clienti. Con una sola vulnerabilità moltiplica il potenziale d'attacco. Alcune aziende sono presidiate e l'attore si ritira; altre sono più libere e da lì naviga all'interno.
A volte è una pesca a strascico: l'attore non sa in quale azienda atterrerà. Altre volte sceglie il prodotto perché sa che è usato da un bersaglio specifico o da bersagli di un certo tipo: se è venduto alle agenzie della difesa di un paese, colpendo il fornitore si ritrova nelle reti di marina, aeronautica ed esercito. Oppure: un software di revisione di contenuti cinematografici usato da molti broadcaster internazionali; colpendolo, l'attore entra in moltissime reti televisive e può diffondere un messaggio di tipo attivista.
> **Nota aggiunta:** il docente non commenta i singoli loghi. Si riferiscono a casi noti: SolarWinds Orion (2020), NotPetya via l'aggiornamento del software contabile ucraino M.E.Doc, che colpì fra gli altri Maersk (2017), 3CX (2023), MOVEit Transfer (2023, sfruttato dal gruppo Cl0p), la dipendenza compromessa `torchtriton` di PyTorch nightly (dicembre 2022), le vulnerabilità di Microsoft Exchange (2021). **CrowdStrike** (luglio 2024) non fu un attacco ma un aggiornamento difettoso, come già annotato per la lezione 2: qui vale come esempio di dipendenza da un canale fidato, non di compromissione.
### Integrazione Teams 2026 (lezione 1 2026)
*Capitolo 04, sezione 11 (supply chain)*
- Attacchi alla filiera come conseguenza diretta dell'interconnessione (Teams 1 @ 0:13:10); nella slide 2020s compaiono SolarWinds, Exchange, Log4j, MOVEit, xz, CrowdStrike e i cercapersone (vista a Teams 1 @ 0:16:40).
### Integrazione Teams 2026 (lezione 2 2026)
*Capitolo 02, sezione 9 (perimetro globale) e Capitolo 04, sezione 11 (supply chain)*
- Esempio nuovo, la fatturazione elettronica: pochissime aziende hanno un sistema interno; il fornitore cloud a sua volta usa un CSP (Amazon, Google, Microsoft), un fornitore di pagamenti, un sistema di invio PDF via email, e librerie di terze parti open source mantenute da sconosciuti o closed source mai verificate. Le interdipendenze "non sono neanche più conoscibili". (Teams 2 @ 1:10:58 - 1:13:07)
- **DORA**: impone ai soggetti obbligati un elenco dei fornitori terzi e la conoscenza dell'intera filiera, perché l'attacco può venire dal fornitore del fornitore del fornitore. (Teams 2 @ 1:13:07)
- Casi citati: **Log4j** (libreria di logging, 2021) e **XZ** (libreria di compressione): un attore, statuale o meno, ottiene l'accesso a un progetto open source e vi inserisce una backdoor; nel caso XZ l'attore ha atteso anni per ottenere l'accesso e qualcuno se n'è accorto in tempo. Vedi Divergenze per le imprecisioni. (Teams 2 @ 1:14:01 - 1:16:03)
- Senza una **bill of materials** (elenco delle dipendenze) il cliente finale non sa se il suo software dipende da una libreria compromessa. (Teams 2 @ 1:15:04)
- Tre livelli di risposta a "come ci si difende": 1) approccio basato sul rischio; 2) fare sistema, con scambio informativo strutturato (von der Leyen); 3) "conosci te stesso": sapere che cosa si ha "in pancia" e quali sono le proprie interdipendenze, perché non si protegge ciò che non si conosce. Senza questo, una PMI è alla mercé dei supply chain attack. (Teams 2 @ 1:16:19 - 1:18:23)
---
### Integrazione Teams 2026 (lezione 2 2026)
*Supply chain software: Log4j, XZ, SBOM, DORA*
Nel 2025 i supply chain attack erano trattati con SolarWinds, 3CX, MOVEit (capitolo 04, sezione 11), senza Log4j, XZ, SBOM né l'obbligo DORA sul registro dei fornitori. Qui il focus è la **non conoscibilità** delle dipendenze e il "conosci te stesso" come terza leva di difesa (Teams 2 @ 1:10:58 - 1:18:23).
---
## 12. Slide saltate e avviso organizzativo
*CS-04 @ 01:21:34*
Il docente scorre rapidamente due slide dicendo "queste le salto, non sono importanti":
- **"Types of threat"**: quattro riquadri. *Interception* (forme geometriche sovrapposte), *Interruption* (una fila di cerchi rosa che si blocca contro una barra gialla), *Modification* (martelli che colpiscono un chiodo su una tavola), *Fabrication* (una fila di cerchi in un condotto, da cui escono cerchi inseriti da un ramo laterale, mentre la prosecuzione è tratteggiata).
- **"Non-scripted ~~content~~ threats"** (la parola *content* è barrata): *bugs and failures* (lente su un insetto fra cifre binarie), *operational (human) errors* (un'auto finita in acqua mentre vara una barca), *dependencies* (patch panel e cavi di rete), *natural causes (including unlikely events like wars, pandemics, ...)* (un tornado).
Avviso: la lezione del **23 settembre** salta; per recuperare il tempo il docente allunga un po' le lezioni restanti, a partire da questa.
### Integrazione Teams 2026 (lezione 2 2026)
*Capitolo 04, sezione 12 (slide "Non-scripted threats", saltate nel 2025)*
- Nel 2025 la slide era stata saltata come "non importante"; nel 2026 viene spiegata. Le minacce "fuori copione" (termine che il docente prende dal linguaggio cinematografico) non derivano da attacchi ma da eventi: bug e malfunzionamenti non voluti, errori operativi umani, disastri naturali, dipendenze tecnologiche. Si possono prevedere solo sul piano organizzativo. (Teams 2 @ 0:10:32)
- Esempio di causa naturale: nella società di post-produzione in cui lavorava, le sedi erano collegate da fibre spente (dark fiber) affittate su migliaia di chilometri. Le tratte Roma-Parigi e Parigi-Londra si interrompevano circa ogni due settimane per lavori stradali, un contadino che arava troppo in profondità, cali di corrente. Da qui la necessità di ridondanze. (Teams 2 @ 0:11:19)
- Esempio di dipendenza tecnologica: switch di un vendor e firewall di un altro usavano la stessa porta per messaggi proprietari; con apparati dello stesso vendor tutto funzionava, mescolandoli la rete smetteva di funzionare. (Teams 2 @ 0:13:38)
- Distinzione nuova: prevenire questi rischi è compito della sicurezza informatica, non della cyber security. (Teams 2 @ 0:13:23, 0:14:45)
### Integrazione Teams 2026 (lezione 2 2026)
*Capitolo 02, sezione 2 (triade dei controlli) e Capitolo 04, sezione 12 ("Types of threat")*
- Denominazioni: controlli fisici, tecnici o logici (sicurezza tecnologica), amministrativi o organizzativi. Per il digital trust i controlli presidiano anche l'autenticità. (Teams 2 @ 0:15:47)
- La slide "Types of threat", saltata nel 2025, viene commentata: le minacce si esprimono in quattro tipi, intercettazione, interruzione, modifica e fabbricazione di informazioni (per esempio informazioni false). Il docente la definisce classificazione "molto accademica" e "un po' antiquata", utile per capire che i controlli servono a prevenire o individuare queste tipologie. (Teams 2 @ 0:16:58)
## 13. Sicurezza fisica
*CS-04 @ 01:22:11*
**Slide di sezione "Physical Security"** (01:21:51, testo da OCR, non verificato visivamente), poi **slide "Physical Security"** con tre immagini: una mappa antica di Bruxelles (*BRVXELLA*) con la doppia cinta muraria (© The Hebrew University of Jerusalem & The Jewish National & University Library); una città fortificata bianca a più cerchie addossata alla montagna (simile a Minas Tirith); un castello in rovina circondato da un fossato pieno d'acqua con un ponte.
Riprendendo la triade dei controlli, la sicurezza si divide in domini; il docente "si trattiene poco", ma la sicurezza fisica è un aspetto importante di tutta la cyber sicurezza di un'azienda. Spesso si applica la **difesa in profondità**, già citata nella prima lezione: più strati di sicurezza, fisici, logici e amministrativi, a protezione di qualcosa. È il concetto delle città medievali, reali o di fantasia, con una o più cinte murarie: chi penetra una cinta deve poi superare l'altra. Non tutti i meccanismi di difesa medievali servivano a impedire l'ingresso: le **torri di vedetta** erano alte per individuare il nemico (*detection*) a distanza maggiore.
**Slide "Physical Security"** (01:23:07). A sinistra l'infografica **"CASTLE TRAPS & DEFENSES – AWESOME FEATURES TO WITHSTAND ANNIHILATION"** (National Geographic Channel, *Doomsday Castle*): *Trou de loup* (pit with sharp stake), *Arrowslits*, *Talus* (sloped base of a defense wall), *Bent entrance*, *Murder hole*, *Spiral staircase* (usually spiraled clockwise going up, put right-handed attackers at a disadvantage), *Moat*. A destra:
*Physical security is all of these and more:*
- Knowing where you are, who is around you
- Fences, Gates, Lights and Barbwire
- Walls, Windows and Doors
- Locks, Keys, Keycards and Passwords
- Guards, Armaments and Dogs
- Fire Alarms and Suppression Systems
- CCTV and Motion Sensors
- Employee Identification
- Organizational Procedures
- Building Construction
- Specialized Landscaping
**Slide "Physical Security"** (01:23:38). Schema di un sito a zone concentriche: *Zone 0: Down Range 100 – 1000m* (ellissi di copertura con *Ground Sensors* fra gli alberi), *Zone 1: Near Perimeter 0 – 100m*, *Zone 2: Perimeter Line* (recinzione con telecamere agli angoli), *Zone 3: Inside Perimeter 0 – 50m*, *Zone 4: Site Infrastructure* (con *Control Center*); sotto un riquadro *Security Operations* con monitor.
Un altro dominio tipico sono le **telecamere**: c'è un'arte nel progettarne posizione, orientamento e caratteristiche tecniche, da cui dipende se restano o meno **angoli morti**. Sulle telecamere il docente ha già raccontato aneddoti (lezione 2) e non si dilunga.
### Tailgating e ingegneria sociale fisica
*CS-04 @ 01:23:50*
**Slide "Tailgating and social engineering".** Foto di una donna che entra in un portone seguita da vicino da un'altra; silhouette di due persone che passano una porta una dietro l'altra; persone in fila rapida davanti a tornelli di un edificio a vetri; un fumetto con un fattorino carico di pacchi davanti alla guardia di un desk; una foto di persone che entrano in fila da una porta a vetri sotto la scritta *THE WEST END*.
Molti attacchi di ingegneria sociale servono a **entrare fisicamente** negli edifici.
- **Tailgating**: seguire una persona che entra con il proprio badge, bloccando con il piede o la mano la porta che si richiude. Per questo in alcuni edifici ci sono tornelli che si richiudono appena passa una persona.
- **Il falso fattorino** (in basso a sinistra nella slide): "ho questi pacchi da consegnare a Tizio, mi fai entrare?"; la guardia si impietosisce e lo fa passare, e con i pacchi davanti alla faccia non viene nemmeno ripreso dalle telecamere. Il personale di sicurezza è spesso addestrato, ma questi attacchi sono ancora concreti.
### Shoulder spying
*CS-04 @ 01:25:09*
**Slide "Shoulder spying".** Pittogramma di una persona che guarda lo schermo di un'altra da dietro; una donna che lavora al laptop coperta da un grande cappuccio di lana arancione; un fumetto con *Hacker* che osserva la tastiera di una *Victim* (*Passwords*); una ragazza con tablet fra due giovani incappucciati, titolo *WHAT IS SHOULDER SURFING ATTACK ?*; un uomo che sbircia il laptop di una donna al tavolino di un bar.
Rilevato in vari casi, soprattutto per chi viaggia e lavora in posti non sicurissimi: una persona accanto in treno o in metropolitana, o che guarda attraverso il riflesso di un vetro, può venire a conoscenza delle attività o leggere la password dal movimento delle dita sulla tastiera. In alcuni casi la **prima compromissione** è avvenuta così. Contromisura tecnica: lo **schermo antiriflesso** (filtro privacy) per smartphone e laptop, che impedisce di vedere lo schermo a chi non sta proprio di fronte. Contro la lettura della digitazione, motivo per cui le password stanno "molto lentamente" uscendo dall'uso quotidiano, l'unico contrasto è guardarsi alle spalle e non digitare la password se non si è sicuri di non essere osservati.
### Data center e impersonificazione
*CS-04 @ 01:26:37*
**Slide "Physical Security"** (01:28:38). Il cartello **"NOTICE – AUTHORIZED PERSONNEL ONLY"**, il riquadro **"There is No Patch to Human Stupidity"** e una foto in bianco e nero di un data center, con persone (una con camicia rossa) tra i rack, una che porta un monitor in spalla e una con un carrello.
L'ingegneria sociale serve a \[?\] superare la sicurezza fisica perché i "gioielli della corona" tecnici sono spesso i **data center** o comunque i luoghi dove ci sono i computer. Come nell'evil maid: chi entra fisicamente in un data center e ha accesso anche per pochi secondi a un computer o a uno switch può collegarci una **chiavetta USB con antenna Wi-Fi**. Alcuni computer la riconoscono, la configurano e la connettono; se fuori, in macchina, c'è qualcuno con l'altra antenna, si crea una connessione di rete che **bypassa tutti i firewall** aziendali. Servono computer configurati molto male, ma il docente si è sentito dire più volte \[?\] "non ho configurato la sicurezza di questo computer, tanto sta dentro il data center". Ecco perché la sicurezza fisica è spesso trascurata, mentre chi entra in un data center può fare danni incalcolabili.
La "frode del CEO trasfigurata" in versione fisica: vestirsi con giacca e cravatta, darsi un tono, camminare spediti, recitare una parte. In un reparto tecnico dove i manager non girano, una persona con l'aria di un vicedirettore arrabbiato che sta per "dirne quattro" a qualcuno non viene fermata dall'impiegato medio, che non si prende la briga di chiedere "scusi, dove va?": fa leva sulla paura di essere licenziati o ripresi. Per questo molte aziende hanno **policy** che impongono di fermare chiunque non abbia il badge da dipendente o l'adesivo da visitatore. In alcuni casi gli adesivi riportano la data esatta e hanno un **inchiostro che scolorisce** dopo poche ore, così si sa da quanto tempo il visitatore è entrato; nel dubbio si chiama la reception o la security ("c'è un visitatore da solo senza supervisione, lo devo fermare?"). Queste procedure esistono, ma non sempre sono seguite.
### Integrazione Teams 2026 (lezione 3 2026)
*Capitolo 04, sezione 13 (sicurezza fisica)*
- Doppie mura: nel Medioevo la cinta esterna racchiudeva anche i campi per garantire il cibo durante un assedio lungo mesi (richiamo all'Iliade); lo stesso principio a strati, a guscio di cipolla, si ritrova nella segmentazione delle reti. (Teams 3 @ 0:54:32 - 0:55:49)
- Tailgating e piggybacking: entrare dietro una persona autorizzata bloccando la porta con il piede; la bussola lo impedisce. Il finto postino carico di pacchi, nell'esempio del docente, arriva alla scrivania della vittima e, già che c'è, collega un dispositivo USB al PC. (Teams 3 @ 0:57:10 - 0:58:03)
- Shoulder spying, consigli nuovi: scegliere una posizione che non esponga lo schermo; filtri privacy polarizzati; in aeroporto o sui mezzi non sedersi con le spalle a una superficie riflettente come un vetro; per la digitazione delle password, guardarsi alle spalle o mettersi letteralmente con le spalle al muro. (Teams 3 @ 0:58:18 - 1:00:25)
- Data center: chi entra può fare più danni di chi arriva a una sola scrivania, anche perché dentro le misure sono spesso più lasche (armadi aperti, telecamere davanti ma non dietro i rack). Badge con foto verificabili appoggiandoli a un lettore NFC a parete. (Teams 3 @ 1:00:25 - 1:02:07)
- Impersonificazione di un dirigente: le policy dicono che chiunque, anche "l'ultima ruota del carro", è autorizzato a fermare una persona senza badge o a chiamare la sorveglianza, come nelle campagne di segnalazione della metropolitana di Londra. (Teams 3 @ 1:02:24 - 1:03:46)
- Aneddoto nuovo 1: una major cinematografica impose di aumentare la risoluzione delle telecamere del data center in modo da leggere il codice a barre dei nastri di backup inseriti o estratti a mano, così da sapere chi, quando e quale contenuto. (Teams 3 @ 1:04:16 - 1:05:34)
- Aneddoto nuovo 2: a fine anni 2000 uscì in rete una copia non finita di un film della saga X-Men (effetti incompleti, cavi dello stuntman visibili su Hugh Jackman). Secondo il docente la facility era air-gapped e il pirata entrò nel data center, nel corridoio posteriore dei rack privo di telecamere, e lasciò per oltre un giorno un disco USB collegato a un server. Dopo l'incidente le major imposero telecamere anche sul retro dei rack e la perquisizione di chi lascia la struttura. (Teams 3 @ 1:05:34 - 1:08:22)
- Perquisizioni: negli Stati Uniti la security privata poteva farle; in Italia, secondo il docente, sono vietate ai privati e si può solo chiedere un'auto-perquisizione (vedi Divergenze). (Teams 3 @ 1:08:22 - 1:09:24)
## 14. Sicurezza logica (o tecnica): il caso Stuxnet
*CS-04 @ 01:29:22*
**Slide di sezione "Logical / Technical Security"** (testo da OCR, non verificato visivamente), poi **slide "Logical (or Technical) Security"**. A sinistra uno schema di rete industriale: *Internet* (nuvola) collegata tramite firewall all'*Office Network*; sotto, *Plant Network*, *Control Network* ed *External Network*. In rosso i punti deboli, con frecce che mostrano i percorsi d'attacco: *Misconfigured Firewalls*, *Infected Laptops*, *Insecure Wireless*, *Insecure Remote Support*, *Insecure Modems*, *Infected USB Keys*, *Infected PLC Logic*, *RS-232 – Insecure Serial Links*, *3rd Party Issues*. A destra una vignetta di **Chappatte** (International Herald Tribune): una centrale nucleare esplosa, un computer con la scritta *Stuxnet VIRUS* e due religiosi che guardano le macerie; uno chiede **"DO WE HAVE A BACKUP?"**.
Tutto quello che si è detto sulle reti vale anche qui. L'immagine mostra l'"aftermath" di un attacco avvenuto, secondo il docente, all'inizio del 2010, probabilmente per rallentare il programma nucleare di un paese: un attacco di tipo **statuale**. Nella rete dell'azienda è stato inserito il virus poi chiamato **Stuxnet**. Ma i computer che controllavano la centrale erano **segregati** dalla rete esterna, come accade in molte aziende per i computer legati al vero business, alla proprietà intellettuale o ai segreti industriali (quella che il docente chiama colloquialmente "la ricetta della Coca-Cola"): separati, spesso anche fisicamente, dalla rete aziendale e da Internet, per impedire che un attacco dall'esterno, o dall'interno da parte di chi non ha accesso fisico a quelle stanze, comprometta il core business o il segreto industriale, militare o di Stato.
Premessa del docente: sono ricostruzioni basate su dati spesso non oggettivi né noti con certezza. **Si crede** che l'attacco sia stato veicolato da una **chiavetta USB**, allora molto diffuse, lanciata oltre il muro di cinta, sapendo che sarebbe atterrata nel giardino dove gli impiegati passavano il tempo libero: si è fatto leva sulla **curiosità** ("fammi vedere che c'è dentro, magari me la porto a casa"). La chiavetta è stata collegata o alla rete esterna dell'azienda, e poi il malware con **escalation di privilegi** e **movimento laterale** ha raggiunto la rete segregata, oppure direttamente da un impiegato incauto a un computer isolato dal punto di vista logico ma non da quello delle porte USB.
Stuxnet ha fatto cambiare radicalmente la **postura di sicurezza**: oggi in moltissime organizzazioni è vietato, o tecnicamente impedito, usare chiavette. Il docente ha visto anche **tappi fisici** sulle porte USB; in altri casi il sistema operativo è programmato per non montare la chiavetta, un blocco meno efficace. La sicurezza tecnologica "è un mondo totalmente a parte"; il docente se ne occupa, ma non può scendere nei dettagli.
> **Nota aggiunta:** Stuxnet colpì le centrifughe per l'arricchimento dell'uranio dell'impianto iraniano di **Natanz** (un impianto di arricchimento, non una centrale elettrica). Fu scoperto e reso pubblico nel **giugno 2010**, ma era attivo almeno dal 2009 (una prima versione risale al 2007); "inizio del 2010" è quindi un'approssimazione. L'ingresso tramite supporti USB è la ricostruzione più accreditata; la chiavetta "lanciata oltre il muro" è un racconto diffuso ma non documentato, e il docente stesso lo presenta come "si crede". Le fonti pubbliche più citate parlano di chiavette introdotte tramite fornitori o personale.
### Integrazione Teams 2026 (lezione 1 2026)
*Capitolo 04, sezione 14 (Stuxnet)*
- Aggiunte 2026: attribuzione tramite commenti nel codice e ipotesi di **false flag** ("falsa bandiera", un tempo "disinformazione"); ripresa del caso in vari film (Teams 1 @ 0:41\:45-0\:44:26). Vedi Divergenze per la descrizione tecnica errata.
### Integrazione Teams 2026 (lezione 3 2026)
*Capitolo 04, sezione 14 (sicurezza logica, Stuxnet)*
- La sicurezza logica è presentata come la più rilevante per chi fa data analysis. (Teams 3 @ 1:09:28)
- Dettaglio nuovo sulla ricostruzione: la chiavetta, lanciata oltre il muro, non sarebbe stata collegata direttamente a un computer di controllo ma a un computer air-gapped su un altro segmento; il malware avrebbe attraversato più segmenti prima di raggiungere la rete OT, forse con un ruolo di una chiamata di supporto remoto da Internet. Il docente invita a prendere tutte le ricostruzioni "con le pinze". (Teams 3 @ 1:10:16 - 1:11:37)
- Quasi tutti gli attacchi che attraversano più computer in una rete aziendale sono attacchi basati su rete. (Teams 3 @ 1:11:52 - 1:12:09)
## 15. Reti informatiche e modello a strati
*CS-04 @ 01:32:56*
**Slide "The 7-layers networking model".** A sinistra una pila di sette piani colorati con icone:
<table header-row="true">
<tr>
<td>Livello</td>
<td>Funzione</td>
<td>Esempi sulla slide</td>
</tr>
<tr>
<td>7. Application</td>
<td>*Network process to application*</td>
<td>DNS, WWW/HTTP, P2P, EMAIL/POP, SMTP, Telnet, FTP</td>
</tr>
<tr>
<td>6. Presentation</td>
<td>*Data representation and encryption*</td>
<td>*Recognizing data:* HTML, DOC, JPEG, MP3, AVI, Sockets</td>
</tr>
<tr>
<td>5. Session</td>
<td>*Interhost communication*</td>
<td>*Session establishment in* TCP, SIP, RTP, RPC-Named pipes</td>
</tr>
<tr>
<td>4. Transport</td>
<td>*End-to-end connections and reliability*</td>
<td>TCP, UDP, SCTP, SSL, TLS</td>
</tr>
<tr>
<td>3. Network</td>
<td>*Path determination and logical addressing*</td>
<td>IP, ARP, IPsec, ICMP, IGMP, OSPF</td>
</tr>
<tr>
<td>2. Data Link</td>
<td>*Physical addressing*</td>
<td>Ethernet, 802.11, MAC/LLC, VALN (sic), ATM, HDP, Fibre Channel, Frame Relay, HDLC, PPP, Q.921, Token Ring</td>
</tr>
<tr>
<td>1. Physical</td>
<td>*Media, signal, and binary transmission*</td>
<td>RS-232, RJ45, V.34, 100BASE-TX, SDH, DSL, 802.11</td>
</tr>
</table>
A destra lo schema dell'**incapsulamento** fra due pile 7→1 e 1→7: al livello 7 *L7H + Data*; scendendo si aggiungono intestazioni (L6H, L5H, L4H, L3H), al livello 2 *L2H ... Data L2F* (intestazione e coda di trama), al livello 1 una sequenza di bit `1 0 0 1 0 1 1 0 1 1 0 0 1 0 1 1`; le due pile sono collegate in basso dal mezzo fisico.
Le slide successive, scorse mentre il docente parla, riprendono una tabella comune **TCP/IP – OSI Model – Protocols**, evidenziando di volta in volta una riga:
<table header-row="true">
<tr>
<td>TCP/IP</td>
<td>OSI Model</td>
<td>Protocols</td>
</tr>
<tr>
<td>Application Layer</td>
<td>Application Layer</td>
<td>DNS, DHCP, FTP, HTTPS, IMAP, LDAP, NTP, POP3, RTP, RTSP, SSH, SIP, SMTP, SNMP, Telnet, TFTP</td>
</tr>
<tr>
<td></td>
<td>Presentation Layer</td>
<td>JPEG, MIDI, MPEG, PICT, TIFF</td>
</tr>
<tr>
<td></td>
<td>Session Layer</td>
<td>NetBIOS, NFS, PAP, SCP, SQL, ZIP</td>
</tr>
<tr>
<td>Transport Layer</td>
<td>Transport Layer</td>
<td>TCP, UDP</td>
</tr>
<tr>
<td>Internet Layer</td>
<td>Network Layer</td>
<td>ICMP, IGMP, IPsec, IPv4, IPv6, IPX, RIP</td>
</tr>
<tr>
<td>Link Layer</td>
<td>Data Link Layer</td>
<td>ARP, ATM, CDP, FDDI, Frame Relay, HDLC, MPLS, PPP, STP, Token Ring</td>
</tr>
<tr>
<td></td>
<td>Physical Layer</td>
<td>Bluetooth, Ethernet, DSL, ISDN, 802.11 Wi-Fi</td>
</tr>
</table>
- **"Information Security at layer 1 (physical)"** (01:33:55 e 01:37:19): riga *Physical Layer* evidenziata e foto di uno switch con cavi di rete blu.
- **"Information Security at layers 2 and 3"** (01:34:25): righe *Network Layer* e *Data Link Layer* evidenziate; in alto tre router *C*, *B*, *A* e un pacchetto *data \| DA=20.1.1.1* (*IP Header (with Destination Address 20.1.1.1)*) che diventa *data \| DA=20.1.1.1 \| DA=A* (*IP Header*, *Tunnel Header*); screenshot di `ipconfig` di Windows con *Physical Address . . . : 00-1B-2F-BB-4C-98* evidenziato e di `ifconfig` Linux con *HWaddr 08:00:27:15:84:10* evidenziato da una freccia rossa.
- **"Information Security at layer 4 (transport)"** (01:35:16): riga *Transport Layer* evidenziata; in alto **TCP vs UDP**: per TCP *Client* e *Server* con *SYN*, *SYN ACK*, *ACK*; per UDP *Request*, *Response*, *Response*.
- **"InfoSec at layers 5 through 7 (application)"** (01:36:23): le tre righe applicative evidenziate; immagini di una barra `http://www.`, pellicole fotografiche, una busta *EMAIL*, uno smartphone e un orologio digitale rosso **10:28:28 GPS/NTP MASTER**.
Il docente fa "qualche parola sulle reti". Il modello di rete di casa è lo stesso dell'azienda e di Internet. Tutte le comunicazioni seguono un protocollo che qualunque testo accademico descrive a **strati** \[?\]. Gli strati corrispondono a **livelli di astrazione**. Il **layer 1**, fisico, tratta i bit 0 e 1 come corrente elettrica su un doppino di rame, come luce in una fibra ottica o come onda elettromagnetica nell'etere per il Wi-Fi: conta l'aspetto elettromagnetico o ottico della comunicazione, "che poi in realtà è la stessa cosa". Salendo, i layer successivi descrivono come questi bit formano un **indirizzo** (l'indirizzo Internet) e vengono usati da tutti gli apparati di rete che il messaggio incontra dalla sorgente alla destinazione: dalla casa del docente, audio e video delle slide arrivano alle case degli studenti, anche in differita. I protocolli di **instradamento** descrivono a livello di bit e byte il messaggio ai **layer 2 e 3** e lo **impacchettano** in contenitori di livello via via più basso, fino a quello fisico. Gli strati superiori descrivono come il dato è **trasportato** e, più su ancora, come è **codificato** in bit e byte: l'email in un file, l'immagine, il suono, una transazione bancaria, una firma elettronica, un orario nei messaggi con cui i computer si scambiano l'ora. Tutti funzionano insieme, a cascata, ciascuno impilato dentro l'altro.
**Attacchi ai protocolli.** Moltissimi attacchi consistono nell'**ingannare** uno di questi protocolli. Si costruisce ad arte un messaggio che a livello applicativo \[?\] ("livello applicativo numero 5") è legittimo, per esempio sembra un'immagine; ma quando lo interpreta un certo firewall o router, magari del gestore della rete di destinazione, l'immagine viene spezzata in due, perché al suo interno c'è un pezzo codificato dalla sorgente come immagine che viene invece letto come **informazione di instradamento**. Il messaggio viene costruito dal layer più alto al più basso e, a destinazione, viene "sbucciato come una cipolla" dal più basso al più alto. Se al layer 6 è stato iniettato un contenuto che assomiglia all'**intestazione di un pacchetto di layer 3**, il dispositivo di layer 3 che lo spacchetta viene ingannato e instrada altrove la seconda metà dell'"immagine", che non è più un'immagine ma il pezzetto malevolo che viene installato. Il docente chiama la tecnica **smuggling**. È uno dei tanti attacchi tecnici per ingannare le reti e aggirare i sistemi di sicurezza.
> **Nota aggiunta:** la descrizione è volutamente semplificata. Tecniche reali basate su questo principio (dati di un livello interpretati come intestazioni di un altro) sono il **packet-in-packet injection** e, a livello applicativo, l'**HTTP request smuggling**; non va confusa con l'HTML smuggling della sezione 8. Nel modello OSI il livello applicativo è il 7; "numero 5" corrisponde al livello applicativo nel modello ibrido a 5 strati (fisico, collegamento, rete, trasporto, applicazione), quindi va letto come un riferimento a quel modello o come un lapsus.
### Integrazione Teams 2026 (lezione 3 2026)
*Capitolo 04, sezione 15 (modello OSI)*
- Metafora postale: layer 2 e 3 descrivono la busta e il servizio di recapito (instradamento tramite router e switch come un indirizzo con via e numero civico); il layer 4 descrive come si apre la busta e si ricompone un messaggio spezzato in più buste. (Teams 3 @ 1:13:26 - 1:14:47)
- TCP e UDP come protocolli di trasporto sostanzialmente unici; **three-way handshake** (SYN, SYN-ACK, ACK), bersaglio di molte tipologie di attacco. (Teams 3 @ 1:14:47 - 1:15:35)
- Livelli applicativi: esempio **NTP**, con cui si sincronizzano smartphone, computer e perfino il forno a microonde. (Teams 3 @ 1:16:05 - 1:16:39)
- Esempio nuovo di incapsulamento: uno streaming YouTube verso la smart TV viaggia su tratte fisiche diverse (Wi-Fi, rame fino all'armadio stradale, fibra, rete del provider, punto di interscambio e CDN di Google), ma il contenuto di layer 7 (video compresso) arriva incapsulato nei livelli 6, 5, trasporto, IPv4 ed Ethernet. (Teams 3 @ 1:17:28 - 1:20:17)
- Gli attacchi che sfruttano la stratificazione (un messaggio innocuo a un livello che diventa malevolo a un altro) sono chiamati qui attacchi di **injection** (nel 2025: smuggling); servono ai malware per muoversi lateralmente e scalare privilegi. (Teams 3 @ 1:20:34 - 1:21:38)
## 16. Minaccia dall'interno, segmentazione e pivoting
*CS-04 @ 01:37:36*
**Slide "Pivoting – attacks across network(s)".** *Internet* (nuvola) collegata a *Public Server1*, *Public Server2* e a un *Router 192.168.10.254*; dietro, un *Firewall*; poi *Switch1 192.168.10.240* (con *PC1 192.168.10.200* e *PC2 192.168.10.201*) e *Switch2 192.168.10.241* con un *Wireless Access Point* a cui sono collegati *PC3 192.168.10.202*, *PC4 192.168.10.203* e, via Wi-Fi, uno *Smartphone 192.168.10.204*.
Le reti sono progettate per resistere ad attacchi dall'interno e dall'esterno. L'errore frequente, anche nelle reti piccole o casalinghe, è pensare che la minaccia arrivi **solo dall'esterno**: metto un firewall davanti all'azienda, magari lo configuro bene, "ho speso 5000 euro, magari ne ho comprati due" e mi sento al sicuro con l'armatura. Ma se il dipendente ha aperto l'email di phishing e scaricato il malware, il malware si connette dall'interno verso l'esterno ed esfiltra dati attraverso un firewall che in uscita non blocca, perché lo scambia per il legittimo traffico Internet di un dipendente. La protezione salta del tutto; lo stesso vale se il dipendente è una minaccia interna: nessun sistema di blocco dall'esterno lo impedisce.
**Slide "Local Area Network (LAN)"** (01:39:59). A sinistra *Logical Topology*: *Internet* → *Router-Firewall*; un segmento *Ethernet 192.168.2.0* con *Department Server* (*Mail Server 192.168.2.1*, *Web Server 192.168.2.2*, *File Server 192.168.2.3*) e *Admin Group* (*192.168.2.4*, *.5*, *.6*); un segmento *Ethernet 192.168.1.0* con *Classroom 1* (*192.168.1.1–.3*), *Classroom 2* (*192.168.1.4–.6*), *Classroom 3* e *Printer* (indirizzi troncati: *192.168.1*). A destra la vista fisica: *Router*, *Ethernet Switch*, *Admin Office* con *Admin Hub*, *Switch* con *Mail Server*, *Web Server*, *File Server*, e tre *Classroom Hub* per *Classroom 1*, *2*, *3*.
Spesso le reti sono **segmentate** in reti locali. L'esempio è la rete di un campus: i computer di ogni aula sono collegati a un hub d'aula, le aule a una rete più grande che contiene altrove i server dell'università. Sugli hub si possono mettere controlli di sicurezza, per esempio per impedire che un computer di un'aula comunichi con uno di un'altra, o con l'ufficio amministrativo (uno studente che deve parlare con l'amministrazione manda un'email o va al ricevimento), e anche per impedire che l'ufficio amministrativo, se compromesso, invii dati a un computer d'aula. Se dall'ufficio amministrativo, magari sorvegliato, si esfiltrassero dati sensibili direttamente, una sonda rileverebbe l'esfiltrazione anomala. Ma se li mando alla **stampante** dell'altra aula e me li porto via stampati, oppure a un computer d'aula da cui un complice, studente iscritto a quel corso, si logga e li carica su Google Drive, **aggiro** i sistemi di protezione dei dati dell'organizzazione. Attacchi sofisticati; e si può immaginare quanto lo diventino su reti enormi.
### Integrazione Teams 2026 (lezione 3 2026)
*Capitolo 04, sezioni 16 e 17 (segmentazione, MAN, WWAN, vista semantica)*
- Oltre a firewall, IDS/IPS e bilanciatori, la **complessità stessa della rete** è una protezione. Esempio del campus: router o firewall fra il segmento delle aule e quello dei server del dipartimento (voti, dati finanziari e personali degli studenti). (Teams 3 @ 1:21:54 - 1:23:25)
- Mappa semantica: il docente ammette che l'immagine mostrata in realtà rappresenta l'importanza dei gruppi musicali nell'industria discografica ("facciamo finta che sia un diagramma della rete Internet"). (Teams 3 @ 1:25:12)
- Contenuto nuovo, la navigazione dell'attaccante: chi entra in una rete di solito non sa dove si trova né dove andare; si costruisce la mappa man mano, come una **fog of war**, con strumenti che ricostruiscono la rete in tempo reale. Analogia del radiologo interventista che dalla safena deve arrivare al cuore guardando il catetere sullo schermo. Ogni tentativo aumenta la probabilità di essere scoperti; gli attacchi riescono molto meglio se l'attaccante "ha fatto i compiti a casa", per esempio cercando per prima cosa i server che ospitano le mappe di rete. (Teams 3 @ 1:25:43 - 1:28:56)
---
### Integrazione Teams 2026 (lezione 3 2026)
*Come si muove un attaccante in una rete sconosciuta*
Nessun manuale 2025 tratta questo punto (il capitolo 04, sezione 16, parla di pivoting ma dal lato della rete). Sintesi (Teams 3 @ 1:25:43 - 1:28:56):
- l'attaccante, umano o automatico, spesso non conosce la topologia della rete in cui è atterrato;
- la ricostruisce passo dopo passo (fog of war), spesso con strumenti che la mappano automaticamente;
- sa grosso modo dove si trovano i "gioielli" (per esempio le ricette segrete) ma deve trovare il percorso, tornando indietro quando sbaglia;
- ogni passo falso è un'occasione di rilevamento, quindi conta lavorare "sottotraccia";
- le mappe di rete interne sono un obiettivo in sé.
## 17. Dalle LAN alla rete globale: MAN, WWAN, vista semantica
*CS-04 @ 01:40:51*
**Slide "Metropolitan Area Network (MAN)".** Un diagramma fittissimo con scritte in giapponese in alto a sinistra (*CONFIDENTIAL*, *名前*) e il logo **INTEROP TOKYO \| 8-12 JUNE 2009 – ShowNet topology 06/12-09:00-pub**. Riquadri con i nomi di provider e punti di interscambio (*JGN2plus*, *KDDI*, *WIDE*, *JPIX*, *DIX-IE*, [*ntt.net*](http://ntt.net), *JPNAP I*, *JPNAP II*, *OCN*, *StarBED project*) e segmenti etichettati *.notemachi*, *.noc*, *.apa*, *.mgmt*, *.monitor*, *.conf*, *.server*, *.life*, *exhibitors*.
Il docente la presenta come l'immagine di una **rete metropolitana di Tokyo**, un diagramma solo schematico e datato 2009: si immagini quanto possa essere complessa oggi la rete di una città come Tokyo, "10 milioni di abitanti e più, pare 11", con tutte le telecamere agli incroci.
> **Correzione:** il diagramma non rappresenta la rete della città di Tokyo ma la **ShowNet**, la rete dimostrativa costruita per la fiera **Interop Tokyo 2009** (8-12 giugno 2009, come indicato sulla slide), collegata a diversi provider e punti di interscambio giapponesi. Resta un buon esempio di complessità di una rete di scala metropolitana, ma non è la rete di Tokyo. Quanto agli abitanti: la Metropoli di Tokyo ne conta circa 14 milioni, i 23 quartieri speciali circa 9,7 milioni, l'area metropolitana oltre 37 milioni.
**Slide "Worldwide Area Network (WWAN, physical view)"** (01:42:21). Mappa del mondo su fondo blu scuro tracciata solo da linee luminose di connessione, fitte su Nord America, Europa, India, Sud-est asiatico; logo **facebook** e data *December 2010*.
Il docente la descrive come un'immagine che collega alcuni punti della rete Facebook, da un sito pubblico di Facebook, datata 2010: molte interconnessioni intercontinentali, che evidenziano dove c'era più attività di dati su quel social. Il tecnico non ci fa nulla, è un grafico puramente esplicativo, ma dà un'idea di quanto fosse interconnessa la rete degli utenti e potrebbe servire a un attaccante per capire quali paesi avevano più utenti e più conversazioni in quel periodo.
> **Nota aggiunta:** è la visualizzazione pubblicata da Paul Butler (stagista Facebook) nel dicembre 2010: ogni linea rappresenta coppie di **amicizie** fra città, pesate per numero di amici; non è una mappa dell'infrastruttura fisica né del traffico dati, benché la slide la intitoli *physical view*.
**Slide "Internet topology, (WWAN, technical-logical view)"** (01:42:39). Grafo a nodi colorati (arancione, rosso, verde, blu, grigio, viola), di dimensioni diverse, con fittissimi archi; il docente vi passa sopra senza commento specifico.
**Slide "The Internet = The WWW (semantic view)"** (01:43:01). Screenshot di **"The Internet map"**: cerchi di dimensioni diverse su fondo nero, i più grandi [*google.com*](http://google.com), [*facebook.com*](http://facebook.com), [*youtube.com*](http://youtube.com), [*yahoo.com*](http://yahoo.com), poi [*bing.com*](http://bing.com), [*ask.com*](http://ask.com); casella di ricerca *Site address or country*.
Oltre ai diagrammi basati sulla vicinanza fisica, ci sono quelli basati sulle caratteristiche tecnologiche della rete: questa è una **rete semantica**, che non considera la vicinanza dei punti ma classifica i nodi in base alla loro **importanza**. Dal punto di vista della sicurezza possono essere utili o no, ma sono spesso usati da chi fa **analisi dei dati**, perché danno una rappresentazione visiva della rilevanza metrica dei siti o nodi in una rete. Per lo stesso motivo un attore della minaccia può usarli per capire quali sono i nodi più rilevanti, quelli che statisticamente conviene usare per indirizzare un attacco.
> **Nota aggiunta:** "The Internet map" ([internet-map.net](http://internet-map.net), Ruslan Enikeev, 2011-2012) rappresenta i siti come cerchi di area proporzionale al traffico e li avvicina in base ai passaggi degli utenti da un sito all'altro. Il titolo della slide "The Internet = The WWW" va inteso come provocazione: Internet è l'infrastruttura di rete, il Web è uno dei servizi che vi girano sopra.
La lezione si chiude a *CS-04 @ 01:43:36*: "per oggi ho detto più o meno tutto, la prossima lezione riprenderemo da qui", con la richiesta di eventuali domande (la registrazione termina lì).
---
## 18. Glossario
<table header-row="true">
<tr>
<td>Termine</td>
<td>Significato nella lezione</td>
</tr>
<tr>
<td>Ransomware</td>
<td>Malware che cifra i file della vittima e chiede un riscatto per la chiave</td>
</tr>
<tr>
<td>Movimento laterale</td>
<td>Propagazione del malware da una macchina all'altra dentro l'organizzazione</td>
</tr>
<tr>
<td>Malware analysis</td>
<td>Analisi del malware stesso, anche per trovarne le vulnerabilità (es. chiave recuperabile)</td>
</tr>
<tr>
<td>Cybercrime-as-a-Service (CaaS)</td>
<td>Offerta di servizi (malware, personalizzazione, call center, riciclaggio) a chi commette crimini informatici</td>
</tr>
<tr>
<td>Weaponization ("armare")</td>
<td>Personalizzare strumenti generici per colpire le specificità di una vittima</td>
</tr>
<tr>
<td>Money mule</td>
<td>Intermediario che ricicla il denaro trattenendo una percentuale</td>
</tr>
<tr>
<td>Drive-by download</td>
<td>Download e installazione di malware alla sola visita di una pagina, sfruttando vulnerabilità del browser</td>
</tr>
<tr>
<td>Estorsione singola / doppia / tripla / quadrupla</td>
<td>Cifratura / + esfiltrazione / + DDoS / + contatto diretto con clienti e stakeholder</td>
</tr>
<tr>
<td>Esfiltrazione</td>
<td>Copia non autorizzata di dati verso l'infrastruttura dell'attaccante</td>
</tr>
<tr>
<td>Doxing</td>
<td>Pubblicazione di dati per esporre pubblicamente la vittima</td>
</tr>
<tr>
<td>Attribuzione</td>
<td>Individuare chi sta davvero dietro un attacco</td>
</tr>
<tr>
<td>Insider threat</td>
<td>Minaccia interna: negligente, inconsapevole, malevola, terze parti</td>
</tr>
<tr>
<td>Dipendente traditore</td>
<td>Insider malevolo che agisce per rivalsa</td>
</tr>
<tr>
<td>Evil maid attack</td>
<td>Attacco fisico a un dispositivo lasciato incustodito (es. in albergo)</td>
</tr>
<tr>
<td>Potenziale d'attacco</td>
<td>Livello di risorse e competenze richiesto da un attacco (qui "elevato")</td>
</tr>
<tr>
<td>Keylogger hardware</td>
<td>Dispositivo fisico che registra i tasti premuti</td>
</tr>
<tr>
<td>Social engineering</td>
<td>Sfruttare debolezze psicologiche per indurre azioni utili all'attore</td>
</tr>
<tr>
<td>Pretesto</td>
<td>Scusa plausibile che motiva la richiesta, spesso con urgenza</td>
</tr>
<tr>
<td>Frode del CEO</td>
<td>Finta richiesta urgente di pagamento da un vertice aziendale</td>
</tr>
<tr>
<td>Phishing / vishing / smishing / quishing</td>
<td>Via email / voce / SMS e chat / QR code</td>
</tr>
<tr>
<td>Indicatore di compromissione</td>
<td>Elemento che segnala un possibile attacco, non una prova da solo</td>
</tr>
<tr>
<td>Display name</td>
<td>Nome visualizzato nel campo From, arbitrario</td>
</tr>
<tr>
<td>Salutation</td>
<td>Formula di saluto iniziale; se assente o generica, indizio di phishing</td>
</tr>
<tr>
<td>HTML smuggling</td>
<td>Ricostruzione del file malevolo nel browser per eludere i filtri</td>
</tr>
<tr>
<td>Rootkit</td>
<td>Componente malware che si nasconde nel sistema con privilegi elevati</td>
</tr>
<tr>
<td>Sito facciata / civetta</td>
<td>Copia di un sito legittimo che raccoglie credenziali</td>
</tr>
<tr>
<td>Typosquatting</td>
<td>Registrazione di domini simili a quelli legittimi ([facelook.com](http://facelook.com))</td>
</tr>
<tr>
<td>Soglia di paranoia</td>
<td>Taratura di antifrode/antivirus fra falsi positivi e falsi negativi</td>
</tr>
<tr>
<td>Spear phishing</td>
<td>Phishing mirato a un gruppo o settore</td>
</tr>
<tr>
<td>Whaling</td>
<td>Phishing su individui specifici e rilevanti di un'organizzazione</td>
</tr>
<tr>
<td>Supply chain attack</td>
<td>Compromissione di un fornitore per raggiungerne i clienti tramite canali fidati</td>
</tr>
<tr>
<td>Difesa in profondità</td>
<td>Più strati di controlli (fisici, logici, amministrativi) in sequenza</td>
</tr>
<tr>
<td>Tailgating</td>
<td>Entrare in un edificio accodandosi a chi ha il badge</td>
</tr>
<tr>
<td>Shoulder spying / surfing</td>
<td>Spiare schermo o tastiera da vicino</td>
</tr>
<tr>
<td>Air gap / rete segregata</td>
<td>Rete isolata logicamente o fisicamente da quella aziendale e da Internet</td>
</tr>
<tr>
<td>Escalation di privilegi</td>
<td>Ottenere diritti maggiori di quelli iniziali</td>
</tr>
<tr>
<td>Postura di sicurezza</td>
<td>Insieme di regole e scelte di sicurezza di un'organizzazione</td>
</tr>
<tr>
<td>Modello OSI / TCP/IP</td>
<td>Modelli a strati (7 e 4) delle comunicazioni di rete</td>
</tr>
<tr>
<td>Incapsulamento</td>
<td>Aggiunta di intestazioni scendendo di livello, rimozione risalendo</td>
</tr>
<tr>
<td>Segmentazione</td>
<td>Suddivisione della rete in segmenti con controlli fra di essi</td>
</tr>
<tr>
<td>Pivoting</td>
<td>Usare un sistema compromesso come trampolino verso altre reti</td>
</tr>
<tr>
<td>LAN / MAN / WWAN</td>
<td>Rete locale / metropolitana / mondiale</td>
</tr>
<tr>
<td>Rete semantica</td>
<td>Rappresentazione dei nodi per importanza, non per posizione</td>
</tr>
</table>
## 19. Punti incerti
- \[?\] *CS-04 @ 00:16:47*: "in cybercriminali, attori statuali, attori di giuramento attori attuali, attori attuali". Trascrizione degenerata; dal contesto la terza categoria è "attivisti" (hacktivisti), ma non è ricostruibile con certezza.
- \[?\] *CS-04 @ 00:36:32*: "all'evolume di attacchi in particolare". Probabilmente "all'evil maid attack in particolare".
- \[?\] *CS-04 @ 01:26:37*: "l'ingegneria sociale è usata per barcare la sicurezza fisica". Verbo non chiaro (forse "valicare" o "scavalcare"); il senso è superare.
- \[?\] *CS-04 @ 01:27:09*: "anche da OZO, almeno sono fatto sentir dire". Frase non ricostruibile; il senso è "mi sono sentito dire più volte".
- \[?\] *CS-04 @ 01:33\:02-01\:33:35*: fra "sulle reti informatiche" e "strati" manca un pezzo (probabilmente "è descritto in sette strati").
- \[?\] *CS-04 @ 01:35:53*: "a livello applicativo numero 5" e poi "al layer 6": numerazione non coerente, vedi Nota aggiunta nella sezione 15.
- *CS-04 @ 01:14:32*: l'osservazione di Anna sulla paranoia non è nell'audio (probabilmente scritta in chat); è ricostruita dalla risposta del docente.
- *CS-04 @ 01:40:51*: diagramma presentato come rete metropolitana di Tokyo; è la ShowNet di Interop Tokyo 2009 (Correzione, sezione 17).
- Nomi degli studenti ricostruiti dai riquadri Teams: "Cristian" = Christian Mari; "Anna" = Anna Alexan\[...\]; "Giancarlo" = Giancarlo Usai.
- Trascrizione automatica corretta nel testo: "John Capote University" = John Cabot University; "Arrichetti" = Arrighetti; "Harpanet" = ARPANET; "chip monkey" = SurveyMonkey; "socio-anginio" = social engineering; "evil made" = evil maid; "shoulder spine" = shoulder spying; "quarrishing" = quishing; "[facelock.com](http://facelock.com)" = [facelook.com](http://facelook.com) (come a schermo); "type of squatting" = typosquatting; "sfiltrazione/sfiltrato" = esfiltrazione/esfiltrato; "lo enforcement" = law enforcement; "sassonino" = sassolino; "contretto" = contractor; "conserge" = concierge; "gravatta" = cravatta; "polisi" = policy; "John Cappatrust source" = Johncabot trusted source; "indicatorio" = indicatore; "aggennato" = accennato; "criptografia" = crittografia; "in pare 11" = "pare 11"; "indifferita" = in differita.
## 20. Esame
In questa lezione il docente non dice nulla sull'esame né sulla valutazione. L'unico segnale di peso è a *CS-04 @ 01:21:34*: le slide "Types of threat" e "Non-scripted content threats" vengono saltate con "queste le salto, non sono importanti". Avviso organizzativo: la lezione del 23 settembre non si tiene e le lezioni restanti vengono allungate per recuperare.
