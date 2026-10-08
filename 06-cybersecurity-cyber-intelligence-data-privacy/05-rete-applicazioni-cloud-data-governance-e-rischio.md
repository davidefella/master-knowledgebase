# 05 - Rete, applicazioni, cloud, data governance e rischio

> Fonte Notion: https://app.notion.com/p/3e712abc808d81ecb31deabe85369fcf — ultima modifica 2026-09-27T11:55:36.852Z

**Corso:** Cybersecurity, Cyber Intelligence and Data Privacy, docente Walter Arrighetti
**Registrazione:** CS-05 (portale, edizione 2025), Teams del 22/09/2025 (a schermo "2025-09-22 16:07 UTC"), durata circa 02:19
**Fonti:** solo la registrazione (parlato e slide a schermo). Il docente non ha distribuito materiale.
> **Contesto.** La registrazione parte a lezione già iniziata: la prima frase è tronca ("La phishing, devo dirvi che…"). I rimandi alla "scorsa lezione" / "l'altra volta" riguardano la lezione 4 (19/09/2025: QRishing, typosquatting "Facelook", modello a livelli delle reti, stratificazione del cybercrimine, "spazio grigio"); il rimando alla "seconda lezione" riguarda la triade del rischio (lezione 2, sezione 4 del relativo manuale).
> **Guida unica.** Il capitolo segue la lezione 2025 (portale) e integra, nei riquadri "Integrazione Teams 2026", ciò che il docente ha aggiunto o cambiato nell'edizione 2026. Riferimenti: `CS-0N @` per il 2025, `Teams N @` per il 2026.
## Indice
1. Due tentativi di phishing reali: QRishing e caratteri sostitutivi
2. Presidi tecnici di monitoraggio della rete
3. Virtual Private Network (VPN)
4. Surface, deep e dark web; la rete Tor
5. Sicurezza delle applicazioni
6. CVE, CVSS e responsible disclosure
7. Sicurezza del cloud
8. Data governance: sovranità, data space, Data Governance Act, policy cloud italiana, ruoli
9. Dati personali e GDPR: ruoli, diritti, impostazioni di privacy
10. Sicurezza amministrativa e assicurazioni cyber
11. Gestione del rischio
12. Business Continuity Plan e Disaster Recovery Plan
13. Domande finali degli studenti
14. Glossario
15. Punti incerti
16. Esame
---
## 1. Due tentativi di phishing reali: QRishing e caratteri sostitutivi
*CS-05 @ 00:00:01*
**Slide "Phishing alternatives – QRishing, vishing, smishing".** Due screenshot di email ricevute dal docente, con riquadri rossi sugli indicatori.
- A sinistra: oggetto "Invito al Canale Teams", mittente "Microsoft Support \<[noreply@amm.admin-help.info](mailto:noreply@amm.admin-help.info)\>", destinatario Walter Arrighetti, "domenica 23:05". Banner arancione del sistema di posta: "Questo messaggio proviene da Internet. Si raccomanda di non cliccare link o aprire allegati a meno che non si riconosca il mittente e si reputi il contenuto legittimo." Corpo con logo "Microsoft Teams": "Ciao Walter / Sei stato aggiunto al **Canale** del tuo nuovo \[gruppo di lavoro\] … \[Ti invitano a **scannerizzare** il **QR-Code**\] sottostante al fine di … suddetto **canale** e prendere visione di tutte le comu\[nicazioni\]…", con un QR code evidenziato.
- A destra: oggetto "Mancata regolarizzazione.Ticket:85641222", mittente "\[Ser v izio\]\[Pago-PA\] \<[workspace.desk@acm.co.in](mailto:workspace.desk@acm.co.in)\>", "19 set 2025, 16:52 (3 giorni fa)". Corpo: "Gentile utente / Risulta ancora u\[n verbale non saldato\] / \[Si in vita a\] completare il pagamento tramite il portale dedicato: / \[Inserire il link qui\] / In caso di mancato adempimento saranno applicate le \[mis\]ure previste dalla normativa / \[Ufficio Sanzioni\] – Servizio pagoPA / Messaggio generato automaticamente – non rispondere". Evidenziati: "Ser v izio", l'indirizzo del mittente, "verbale non saldato", "Si in vita a", "mis" di "misure", "Ufficio Sanzioni".
Il docente dice di non cliccare né scansionare link e QR code della slide: non li ha controllati e "quasi certamente" sono malevoli.
### Primo caso: il QRishing
La prima email è un caso di **phishing con QR code** (QRishing), già introdotto nella lezione precedente. Il messaggio suggerisce di essere stati aggiunti a un nuovo gruppo di lavoro e, invece di cliccare un link, invita a scansionare il QR code. Il motivo tecnico: il link codificato nel QR code non compare in forma testuale nell'email. A meno che l'antivirus, il **mail gateway** aziendale o il sistema che riceve la posta sia in grado di decodificare il QR code, trasformarlo in un link e visitarlo, così si può veicolare un link malevolo anche con la posta normale.
Gli elementi di minaccia:
- il **contesto di lavoro** ("gruppo di lavoro"): chi la riceve nella casella di lavoro può pensare "è una cosa di lavoro, clicco";
- il **dominio del mittente**: in cima si vede subito che non arriva da un dominio Microsoft né da quello del datore di lavoro;
- l'invito a usare il **QR code** invece di un link, che probabilmente verrebbe scansionato dall'antivirus aziendale.
### Secondo caso: il falso pagoPA
*CS-05 @ 00:02:08*
Il docente chiede alla classe quali siano gli indicatori. Lo studente Matteo individua la formattazione del testo (già nell'intestazione), il dominio del mittente che non è di pagoPA e gli errori di battitura. Il docente commenta punto per punto.
**Il dominio.** È vero che [acm.co.in](http://acm.co.in) non è un dominio pagoPA, ma questo da solo non prova che l'email sia malevola: molto spesso i servizi di posta massiva sono affidati, legittimamente, a soggetti terzi che scrivono da un loro indirizzo (esempio: i sondaggi che l'organizzazione manda tramite Mailchimp). È certamente un **indicatore di compromissione**; poi bisognerebbe verificare, e magari si scopre che il dominio è registrato in modo poco trasparente. "Non bisogna mai diventare paranoici."
**Il pretesto.** *CS-05 @ 00:05:46* Caratteristica di tutte le email di phishing è il **pretesto**. Qui l'email è firmata da un "Ufficio Sanzioni", cosa che mette ansia a chi legge, e parla di un verbale non saldato: "si tratta dei sordi", detto alla romana. Qualcuno ti chiede soldi, e per molti basta per pagare subito. Il docente dubita che pagoPA, come società per quanto statale, possa erogare sanzioni come un'autorità (vorrebbe controllarne lo statuto, ma "non mi risulta").
**La lingua.** Un verbale non si "salda": un verbale attesta qualcosa; si salda una fattura o una ricevuta. L'uso improprio dell'italiano fa pensare che l'attore della minaccia non sia madrelingua, come l'uso improprio dell'inglese individuato da una collega la volta precedente. Lo stesso vale per "Si in vita": da chi scrive per conto di pagoPA ci si aspetterebbe almeno una correzione di bozze. Secondo il docente, questi indicatori bastano già da soli a classificare l'email come spam.
### I caratteri sostitutivi
*CS-05 @ 00:08:28*
Oltre alla "V" staccata in "SER V IZIO", il docente fa notare che le **m** minuscole e alcune **d** minuscole in tutto il testo sono di dimensione diversa, e che la **e** di "dedicato" è leggermente più alta delle altre. Nessuno risponde alla domanda sul perché, e il docente spiega.
I computer codificano i caratteri secondo lo standard **Unicode**. Un font completo contiene le lettere di molti alfabeti (greco antico e moderno, cirillico), gli ideogrammi cinesi e giapponesi, in alcuni casi simboli di lingue morte (geroglifici egiziani, lineare B), simboli matematici e finanziari, glifi per le valute, frecce, faccine ed emoticon (spesso colorate, ma in molti font monocromatiche: sono comunque singoli caratteri). Fra questi ci sono **varianti** che rappresentano lettere simili ma con codifica diversa: la "i" senza punto dell'alfabeto turco, oppure, secondo il docente, la "e" usata qui, cioè il simbolo che sulle confezioni indica la tara (esempio: "tara di 25 grammi"), e "d" che in altre lingue sono altri caratteri.
> **Correzione:** lo spazio di codifica Unicode non è limitato a 65.000 caratteri: ha 1.114.112 punti di codice (da U+0000 a U+10FFFF). Circa 65.536 è la dimensione del solo Basic Multilingual Plane, cioè il limite delle vecchie codifiche a 16 bit (UCS-2).
> **Correzione:** il simbolo "℮" che si trova sulle confezioni (U+212E, *estimated sign*) non indica la tara ma la **quantità nominale stimata** del preimballaggio secondo la normativa europea. Il senso dell'esempio del docente non cambia: è un carattere diverso dalla "e" latina che le assomiglia.
Il motivo dell'inganno: i software di verifica delle email cercano **parole chiave**, ne valutano posizione e frequenza (ci sono analisi statistiche basate su **token** interpretati con machine learning, fino alle applicazioni di intelligenza artificiale che leggono il testo, di cui si parlerà più avanti). Quando le rilevazioni superano una soglia, l'email viene classificata come malevola e scartata. Usando lettere che assomigliano a quelle vere, in alcuni font indistinguibili, l'attore della minaccia cerca di ingannare il classificatore. Qui la sostituzione riguarda le minuscole ovunque, ma di solito i caratteri sostitutivi si usano nelle parole più importanti, quelle che se non riconosciute impediscono di classificare l'email come spam.
È un esempio di **typosquatting**: sostituire una parola con una che sembra simile ma non lo è, per ottenere un effetto tecnico diverso. Nei siti web consiste nel registrare un dominio con nome simile (l'esempio della volta prima: "Facelook" invece di "Facebook"); qui serve a ingannare i motori di analisi delle email. "Sembrava che stessi facendo un corso di tipografia con i font."
> **Nota aggiunta:** in letteratura la sostituzione di caratteri con caratteri visivamente simili di altri script si chiama anche *homoglyph attack* (o uso di *confusable characters*); "typosquatting" in senso stretto indica la registrazione di domini con refusi.
### Integrazione Teams 2026 (lezione 6 2026)
*Capitolo 05, sezione 1 (QRishing e falso pagoPA)*
- **QRishing.** Spiegazione più tecnica del QR code: rappresentazione binaria di un indirizzo "spalmata su un quadrato"; il trucco è lo stesso del link malevolo. I lettori QR moderni mostrano l'indirizzo prima di aprirlo: è l'ultimo baluardo, che lascia all'utente "come ultimo firewall" la scelta di non andarci. (Teams 6 @ 0:48:56 - 0:50:31)
- **Falso pagoPA, caratteri sostitutivi.** La "V" di "SER V IZIO" viene identificata come il simbolo matematico dell'OR logico (∨), che viene visualizzato con spazio a destra e a sinistra; anche la "R" maiuscola di "Risulta" e le "m" provengono da altri alfabeti Unicode. Rispetto al 2025 non cita la "e" della tara. Aggiunge: "si invita" scritto "si in vita", e un verbale non si salda. (Teams 6 @ 0:57:42 - 0:59:24)
- **Perché si sostituiscono i caratteri, versione 2026.** I sistemi di filtraggio sono addestrati su milioni di email condivise dai clienti come malevole o spam; un testo che ricalca un pretesto già attribuito a malware viene flaggato. Per riciclare il pretesto basta cambiare almeno un carattere per frase con uno graficamente simile, così anche il mittente nominale "\[Servizio\]\[Pago-PA\]" non viene più riconosciuto come stringa. (Teams 6 @ 0:59:40 - 1:01:51)
## 2. Presidi tecnici di monitoraggio della rete
*CS-05 @ 00:14:08*
**Slide "Network monitoring – IPS/IPS, SIEM, proxies, IPS".** A sinistra la finestra "Scan Results – Mozilla Firefox" ([qualysguard.qualys.eu](http://qualysguard.qualys.eu)) con "Detailed Results" per l'host 192.168.56.101: "Vulnerabilities (29)", un elenco di "CentOS Security Update" (glibc, nss-util, kernel, openssl, bind, graphite2, pcre, setroubleshoot-plugins, libtiff, mariadb, polkit, sos, libssh2, samba…) con livelli di gravità 5, 4 e 3. A destra la dashboard **Qualys WAS** del 17 aprile 2013: "All Vulnerabilities 268", "HIGH Severity 62", "MED Severity 39", "LOW Severity 167", "Malware HIGH 1 detections"; tabella "Most Vulnerable Web Applications" (funkytown.vuln: 100 vulnerabilità, 34 high, 5 med, 61 low; 10.10.26.238: 163, 28/31/104; SimpCMS/lite/: 5, –/3/2); "Catalog" con torta "Total 473" (348 New, 20 Rogue, 84 Approved, 20 Ignored, 1 In Subscription); riquadri "Your Last Scans", "Your Upcoming Scans", "Latest Reports".
Il docente segnala un errore nel titolo: la prima sigla doveva essere "IDS/IPS", invece ha scritto IPS due volte.
Esiste moltissima tecnologia, hardware e software, che gli apparati difensivi possono usare per individuare e prevenire le minacce. Il docente non la tratta perché interessa chi fa sicurezza di mestiere, ma precisa che i presidi tecnici "ci sono, e ce ne sono tanti": identificano le minacce prima che arrivino o quando si presentano sul perimetro, in alcuni casi impediscono che entrino e danneggino l'azienda, in altri fermano la minaccia in corso.
I più avanzati costano di più, ma **quasi nessuno si automatizza** "premendo un bottone". È l'illusione tipica di chi sta ai vertici e non capisce nulla di sicurezza: spendere 10.000, 20.000 o 30.000 per "un aggeggio che si accende" e credere di non dover assumere 3, 4, 5 o 6 esperti che lo mantengano aggiornato ed efficiente. Questi sistemi vanno aggiornati di continuo e soprattutto **configurati sulla realtà organizzativa**: le impostazioni di un firewall, di un IPS o di un SIEM portate da un'organizzazione a un'altra non sono efficaci. L'azienda che fa lacci da scarpe riceverà phishing "a strascico" come tutti, ma anche **spear phishing** mirato su di lei; senza un team che configuri i presidi sul suo profilo di minaccia, nessuna soluzione tecnica è efficace. Se la stessa apparecchiatura passa a un'azienda che vende automobili, con fatturato, esposizione in rete e appetibilità per gli attori della minaccia completamente diversi, va riconfigurata e mantenuta in modo totalmente diverso.
## 3. Virtual Private Network (VPN)
*CS-05 @ 00:17:31*
**Slide "Virtual Private Networking (VPN)".** In alto: una nuvola *Head-office* collegata via *Internet* a due *Regional Office* e a una nuvola *Remote / roaming users* (un desktop e un laptop). In basso: *You* collegato a *Internet* attraverso un tubo etichettato *VPN*; sopra il tubo, con frecce verso di esso, *Hacker*, *ISP*, *Government*, *Corporate*.
"Due aspetti di reti per concludere l'argomento della volta scorsa." Le VPN sono nate per far comunicare le sedi di aziende con più uffici (quartier generale in una città o paese, uffici regionali in altre città, paesi o continenti) **come se fossero un unico luogo**, almeno dal punto di vista logico-tecnico della rete. Anche il dipendente che si collega dal laptop di casa, dal telefono in albergo, in treno o in aeroporto, a Milano o a Roma, vede la stessa rete aziendale: un'unica rete che copre le sedi fisiche e quelle "mobili".
### VPN e modello a livelli
*CS-05 @ 00:18:33*
Una VPN crea un sottostrato di rete, come una LAN, che però è **virtuale**. Richiamando l'approccio a più livelli della lezione precedente, le VPN si collocano tipicamente a **livello 3, 4 o 5**: dal livello 3 o 4 in su la rete è unica, mentre ai livelli 1 e 2, quelli fisici dei cavi, non lo è. La sede di Roma ha il suo data center cablato in un certo modo e magari Vodafone come ISP; quella di Milano ha dispositivi diversi e magari Fastweb; i dipendenti da casa usano il loro router e il loro Wi-Fi; chi viaggia usa le reti degli aeroporti, "con tutte le cautele di cui vi ho già parlato". La VPN è il sostrato software che fa dialogare questo "perimetro totalmente dissolto" come un unico grande ufficio virtuale. È **privata** perché deve anche impedire l'accesso a chi non è legittimato: è, o dovrebbe essere, un sistema protetto.
Durante il richiamo scorrono a schermo, per pochi secondi, le slide della lezione precedente: **"Worldwide Area Network (WWAN, physical view)"** (mappa delle connessioni di Facebook, "December 2010"); **"Information Security at layers 2 and 3"** (pacchetto con "IP Header (with Destination Address 20.1.1.1)" e "Tunnel Header" DA=A attraverso i router C, B, A; output di `ipconfig` con "Physical Address" e di `ifconfig` con "HWaddr" evidenziati; tabella TCP/IP–OSI–protocolli con le righe Internet/Network e Link/Data Link evidenziate); **"The 7-layers networking model"** (i sette livelli, da *7. Application* a *1. Physical*, con esempi di protocolli e l'incapsulamento L7H…L2H/L2F fino ai bit); **"Information Security at layer 4 (transport)"** (TCP con SYN, SYN ACK, ACK contro UDP con Request/Response); **"InfoSec at layers 5 through 7 (application)"**; **"Pivoting – attacks across network(s)"** (router 192.168.10.254, firewall, due switch, access point wireless, PC e smartphone 192.168.10.200–204, due server pubblici); **"Local Area Network (LAN)"**; **"Metropolitan Area Network (MAN)"** (topologia ShowNet di Interop Tokyo 2009); **"Internet topology (WWAN, technical-logical view)"**. Non vengono commentate in questa lezione.
### Come funziona il tunnel
*CS-05 @ 00:20:11*
Il software VPN installato su laptop o smartphone dialoga via Internet con un altro punto dell'azienda e costruisce un **tubo virtuale**, come un cavo di rete "fantasma" attaccato al dispositivo e, virtualmente, allo switch fisico della sede da raggiungere. Tutto ciò che entra nella VPN viene **cifrato**; chi non appartiene alla VPN lo vede solo cifrato; viene decifrato solo dove esce.
L'esempio: sui gateway principali di Roma e di Milano c'è il software VPN. I dati che entrano nel gateway di Milano diretti all'indirizzo virtuale dell'ufficio di Roma vengono cifrati con una chiave che hanno solo i due gateway ("poi parleremo di cifratura"), escono dalla porta Fastweb di Milano, attraversano la rete del provider, la rete nazionale, magari anche l'estero (l'instradamento non è controllato dagli utenti finali), entrano nella rete Vodafone, arrivano al gateway di Roma che riconosce la VPN, decifra e consegna. Lo stesso, al contrario, da Roma a Milano, e lo stesso per il laptop del dipendente che lavora da casa.
**Slide "Original VPN use-cases".** Mappa del mondo: *Head-office* in Nord America, *Regional Office* in Asia orientale, *Remote / roaming users* nel Mediterraneo, collegati da linee rosse.
### VPN per mascherare la provenienza
*CS-05 @ 00:22:48*
**Slide "VPN usage for geo-masking purpose"** (a schermo da 00:27:40; testo da OCR, non verificato visivamente: oltre al titolo si leggono solo "Internet" e "Hacker"). Il docente, nel parlato, descrive un hacker nell'Oceano Indiano che esce da un nodo nella regione dei Grandi Laghi.
Da dentro la VPN i dati sono in chiaro; da fuori appare solo il **punto di uscita**. Chi si collega dal Giappone alla sede di San Francisco produce traffico cifrato visibile solo ai gateway di Tokyo; se il dato esce da San Francisco e viene rimesso su Internet, da fuori sembra provenire dagli Stati Uniti. Con certe VPN non c'è modo di sapere da dove arrivi davvero. Per questo le VPN sono usate anche per fini meno trasparenti, fino a quelli illegali e malevoli: nascondere la provenienza degli attaccanti. L'hacker che si connette dall'Oceano Indiano ed esce nella regione dei Grandi Laghi risulta rintracciabile al massimo a un IP di quella regione (magari americano anziché canadese), e l'attacco sembra partire da lì.
### VPN e contenuti in streaming
*CS-05 @ 00:25:26*
Gli stessi servizi sono offerti ai cittadini per aggirare i **blocchi su base regionale** dei contenuti. Andando all'estero e usando senza VPN Netflix, Amazon, Paramount o Disney+, magari l'80% dei contenuti è uguale ma alcuni mancano e altri si aggiungono, perché le **licenze sono territoriali**. Aneddoto del docente: anni fa, quando in Italia *House of Cards* era su Sky, in Austria lo ha visto su Netflix, doppiato in italiano, perché lì la licenza l'aveva Netflix.
Con una VPN che esce in Nord America la piattaforma legge l'IP e mostra il catalogo nordamericano, anche se si è a Roma o a Istanbul. Tutto lo streaming passa nella VPN: se non è ad alta velocità, l'esperienza video non sarà piacevole. Il docente sottolinea che è **illegittimo**: nelle condizioni d'uso si dichiara espressamente di non usare VPN né altri metodi per mascherare il territorio, quindi si viola il contratto e si è potenzialmente multabili. È lo stesso effetto che molti attori della minaccia usano per intermediarsi ulteriormente e rendersi difficili da rintracciare.
### Integrazione Teams 2026 (lezione 4 2026)
*Capitolo 05, sezione 3 (VPN)*
- **Livelli di rete della VPN.** Nel 2026 il docente dice che esistono VPN di livello 2 e di livello 3 e che non sono mai di livello 1 perché virtuali, anche se possono simularlo; l'immagine proposta è quella di un "cavo di rete virtuale fittizio" che collega due punti altrimenti non connessi da un'unica rete. Nel 2025 aveva parlato di livelli 3, 4 o 5 (vedi Divergenze). (Teams 4 @ 0:01:47)
- **VPN come concetto più ristretto di rete virtuale.** La rete virtuale in generale è un concetto più ampio, tipico di cloud e data center; la VPN è una metodologia specifica, tipicamente finalizzata a unire solo due endpoint (client e server, oppure due sedi). (Teams 4 @ 0:00:42)
- **I due problemi risolti nel caso multisede.** Esempio con sedi a Pechino, Hong Kong, Roma, Londra, Washington, ciascuna con un ISP diverso: senza VPN (1) il traffico fra sedi sull'Internet pubblica è intercettabile da un uomo nel mezzo, (2) gli spazi di indirizzamento delle singole sedi sono diversi e difficili da raggiungere reciprocamente. La VPN crea un unico spazio di indirizzamento dal livello 3 in su e cifra il canale. Topologia tipica: la sede centrale fa da endpoint e le altre sedi generano la VPN verso di essa (collegamento a stella); gli endpoint VPN sono spesso gli unici server esposti in rete dell'azienda. (Teams 4 @ 0:02:59 - 0:06:19)
- **Rimando al corso sui servizi fiduciari.** La cifratura in transito della VPN sarà trattata nel dettaglio nel corso sui servizi fiduciari, dove si fa la crittografia. (Teams 4 @ 0:06:35)
- **La VPN commerciale non garantisce l'anonimato verso le forze dell'ordine.** Il docente aggiunge che risalire all'origine non è così difficile: i fornitori di VPN sono aziende e, se non sono a loro volta fraudolente, sono in grado di fornire alle forze dell'ordine i dati tecnici per ricostruire all'indietro la comunicazione. (Teams 4 @ 0:09:36)
- **Accordi fra piattaforme di streaming e fornitori VPN.** Novità rispetto al 2025: le piattaforme (Netflix, Disney, HBO) hanno sistemi di tracciamento e spesso accordi bilaterali con i vendor di VPN per individuare, se non in tempo reale poco dopo, chi aggira i blocchi geografici e poi bloccarlo o sanzionarlo. Non ripete l'aneddoto di *House of Cards*. (Teams 4 @ 0:10:49)
## 4. Surface, deep e dark web; la rete Tor
*CS-05 @ 00:28:03*
**Slide "Surface, deep and dark web (DDW)".** Un iceberg su tre fasce:
- **4% Surface Web**: "Indexed and easily searchable." (Yahoo, Google, Bing, Wikipedia)
- **90% Deep Web**: "Not indexed, tougher to find." (Academic information, Subscription information, Private databases, Financial records, Government resources, Human resource records, Medical records, Legal documents, Scientific reports, Corporate intranets)
- **6% Dark Web**: "Obscured, difficult to discover." (Zeronet, I2P, TOR encrypted sites, IRC, Private communications)
**Surface web**: siti liberamente accessibili e indicizzabili, con pagine visitabili pubblicamente (Wikipedia, i motori di ricerca, tutti i siti che non chiedono nulla). **Deep web**: pagine web (HTML, World Wide Web) visitabili solo previa **autenticazione**. Gli stessi contenuti di YouTube si vedono in parte senza registrarsi, con pubblicità; registrandosi se ne vedono altri, per esempio quelli comprati. Lo stesso vale per Spotify, Netflix, Disney, Amazon ("pubblicità a nessuno"): sono servizi pubblici, ma la gran parte di ciò che monetizzano è dietro autenticazione, quindi un motore di ricerca non riesce a scansionarlo. Il docente avverte che la slide "comincia ad avere qualche annetto" e che le percentuali andrebbero verificate.
**Dark web** (i siti "non sono pochi"): siti accessibili tramite Internet e il protocollo HTTP, ma non tramite la rete standard. Si entra in reti che "sono delle grandissime VPN", cifrate, in cui i contenuti sono distribuiti in varie parti del mondo; una volta dentro si naviga in questa intranet senza sapere dove si trovino fisicamente i siti.
### Alcune reti del dark web
*CS-05 @ 00:31:16*
**Slide "Some Dark Web networks".**
<table header-row="true">
<tr>
<td></td>
<td>Tor</td>
<td>Freenet</td>
<td>I2P</td>
</tr>
<tr>
<td>Goals</td>
<td>Anonymity & bypassing restriction</td>
<td>Anti-censorship</td>
<td>Anonymity & secure communications</td>
</tr>
<tr>
<td>Access to Internet?</td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Network types</td>
<td>Anonymous services proxed by services</td>
<td>Distributed file-sharing network</td>
<td>One-way encrypted tunnels</td>
</tr>
<tr>
<td>Address</td>
<td>16 or 56-bytes, ending in .onion</td>
<td>CHK, SSK, USK, KSK</td>
<td>516-bytes, ending in .b32 or .i2p</td>
</tr>
<tr>
<td>Project web page</td>
<td>[https://www.torproject.org](https://www.torproject.org)</td>
<td>[https://hyphanet.org](https://hyphanet.org)</td>
<td>[https://geti2p.net](https://geti2p.net)</td>
</tr>
</table>
Non c'è un solo dark web: questi sono i tre più noti, e Tor è il più citato. Quasi sempre serve un accesso a Internet; in altri casi sono reti diverse basate su utenti che mettono a disposizione la propria connettività, "in maniera simile a come si faceva negli anni '90".
> **Nota aggiunta:** gli indirizzi .onion sono lunghi 16 caratteri (versione 2, dismessa) o 56 caratteri (versione 3), non byte; analogamente i 516 dell'I2P sono i caratteri della destinazione completa in Base64. Freenet ha cambiato nome in Hyphanet nel 2023, coerentemente con il link in slide.
### Come funziona Tor
*CS-05 @ 00:31:52*
**Slide "The Onion Router (TOR)".** Alice, con un client, raggiunge un *guard node*, poi un *relay node*, poi un *exit node* da cui il *message* esce verso *internet*; attorno altri *Tor network node*. In basso lo schema a cipolla: il messaggio parte avvolto in più buste (gialla, rossa, blu), ogni nodo con la sua chiave ne toglie una, l'ultimo consegna il messaggio in chiaro. Fonte: [https://www.maketecheasier.com/protect-yourself-from-malicious-tor-exit-nodes/](https://www.maketecheasier.com/protect-yourself-from-malicious-tor-exit-nodes/)
Serve un **client Tor**, che entra da un **nodo di ingresso** e fa rimbalzare il traffico da una parte all'altra della rete. Se si usa Tor per andare anonimi su un sito pubblico, il traffico, come in una VPN, deve uscire da un **nodo di uscita**. Non tutto il traffico ne ha bisogno: solo le attività che devono tornare sull'Internet pubblico. La maggior parte delle attività "totalmente sepolte" avviene su siti accessibili solo dall'interno della rete Tor. \[?\] Il passaggio successivo (*CS-05 @ 00:32:27*) è trascritto in modo contraddittorio ("e quindi in realtà hanno ancora un nodo di uscita, solo che le informazioni che escono dal nodo di uscita sono comunque informazioni tipo Tor").
Si dice spesso che Tor garantisca l'anonimato totale: "una frase che andava bene dieci anni fa". Con un **monitoraggio** abbastanza serrato dei nodi di ingresso e soprattutto di uscita è possibile, con operazioni di **inversione dei percorsi**, ottenere almeno informazioni parziali sulla provenienza di chi è dentro. Per questo, soprattutto in America, forze dell'ordine e intelligence monitorano i nodi di ingresso e uscita.
### Motori di ricerca e cautele
*CS-05 @ 00:33:31*
**Slide "TOR search engines".** "on the surface web: AHMIA, ONION SEARCH"; "on the dark web: AHMIA, ONION SEARCH, TORCH, TOR66". Screenshot di Ahmia, di Tor66 ("Search and Find .onion websites …", "Promoted sites": "TRUST WIKI", "GOOD DARK LINKS LIST") e di Torch ("The Original Tor Search Engine", con categorie *Carding, Forum, Porn, Bitcoin, western union, Hidden Wiki* e banner "SAFE EGIFTS", "BUY REAL MONEY").
I siti del dark web, raggiungibili solo tramite Tor, richiedono motori di ricerca specializzati, alcuni accessibili anche dall'esterno, altri solo dall'interno. Il docente prevede che prima o poi un dark web prevarrà sugli altri, e con lui i suoi motori di ricerca, anche se il crimine avrà sempre bisogno di canali riservati secondari.
**Consiglio del docente** (*CS-05 @ 00:34:38*): è facilissimo (si scarica un client e si naviga, anche da smartphone), ma non va fatto senza aver prima adottato alcune regole di sicurezza. Il dark web funziona come Internet, ma la percentuale di persone con intenti poco raccomandabili è più alta: il rischio di intercettazioni, malware, spam e spyware è molto elevato. Ci sono siti che elencano regole pratiche; la principale per il docente è usare un **computer dedicato**, per esempio un vecchio computer o un vecchio smartphone: "il modo perfetto di riciclarlo".
### Integrazione Teams 2026 (lezione 4 2026)
*Capitolo 05, sezione 4 (Surface, deep e dark web; Tor)*
- **Deep web: autenticazione e interazione.** Il 2026 aggiunge che i siti visitabili senza nemmeno un'autenticazione sono sempre meno; il deep web (stimato al 90% dei contenuti) richiede almeno un token di accesso, spesso autenticazione a due fattori, e in alcuni casi una sequenza di azioni perché le pagine non sono indicizzate con URL, cosa replicabile da un'intelligenza artificiale o da uno scraper ma non in modo immediato. Introduce il termine *scraping* ("grattare via") come indicizzazione automatica indiscriminata del surface web. (Teams 4 @ 0:11:26 - 0:12:57)
- **Dark web: anonimato di entrambe le estremità.** Definizione più articolata: reti basate fisicamente sul backbone di Internet ma con protocolli propri, non scopribili con motori di ricerca e browser normali, spesso raggiungibili solo con software o plug-in dedicati; progettate per rendere anonimi sia chi offre il sito sia chi lo visita. Alcune nascono per esigenze di privacy più o meno legittime, altre espressamente per attività illegali. (Teams 4 @ 0:12:57 - 0:14:53)
- **Tor: pseudonimia, non anonimato.** Il 2026 formula esplicitamente che in Tor "non esiste l'anonimato completo", al massimo una pseudonimia: sorvegliando i nodi di ingresso e uscita, correlando le informazioni, o imponendo ai gestori di quei nodi di consegnare i metadati, si può risalire a ciò che avviene dentro. Aggiunge però che vincoli tecnici e soprattutto giuridici (sovranità legale dei territori) possono rendere in pratica impossibile raggiungere una delle due estremità, cioè il sito illegale o il compratore. Il server Tor fa sì che il percorso cambi anche in tempo reale e non pubblica mai un indirizzo fisico reale. (Teams 4 @ 0:15:25 - 0:17:17)
- Non ripete il consiglio del computer dedicato per navigare nel dark web né la tabella Tor/Freenet/I2P commentata.
## 5. Sicurezza delle applicazioni
*CS-05 @ 00:35:41*
**Slide di sezione "Application Security"** (sfondo con codice Python di Blender, `mirror_mod.use_x = False` ecc.).
L'ingegneria sociale è potente: fa leva su vulnerabilità psicologiche per far fare o non fare qualcosa alla vittima (darmi la password, scendere ad aprirmi la porta), e in molti casi basta. Ma in moltissimi attacchi serve una **componente software**, come un malware. Spesso i malware stanno in **cavalli di Troia**: un piccolo stralcio di codice inserito in un software benigno, o nel sorgente di una pagina web, che fa fare a chi la visita o la usa qualcosa di malevolo.
**Slide "Application Security".** Diagramma: un *Client* con `www.webapp.com` e cookie `_session_id=xyz` invia `webapp.com/project/1/destroy` (con `_session_id=xyz`) a *Server *[*webapp.com*](http://webapp.com), che associa la sessione a `user_id=22`; un *Hacker* fa arrivare al client il codice `<img src="http://www.webapp.com/project/1/destroy" />`. A destra una foto: mani guantate con lente e siringa su uno sfondo binario con le parole "VIRUS", "PASSWORD", "HIJACKED", "INJECTION", "HACKED", "CRACKED". Il diagramma non viene commentato.
> **Nota aggiunta:** lo schema rappresenta un attacco **CSRF** (*Cross-Site Request Forgery*): l'immagine inserita dall'attaccante fa eseguire al browser della vittima, che ha una sessione valida, una richiesta distruttiva verso il sito.
### Firme, codice polimorfico e reverse engineering
*CS-05 @ 00:37:14*
Quando il docente era bambino gli antivirus verificavano se nel codice binario delle applicazioni c'erano **stringhe note**, come in un'analisi del DNA si cerca un ceppo alterato che indica una malattia genetica. È l'**analisi statica delle firme**, ancora usata da molte soluzioni anti-malware. Ma gli attori della minaccia producono spesso codice che **modifica se stesso**: ogni volta che lo stesso malware arriva a una vittima diversa è modificato per non essere identico alle copie già individuate, rendendo difficile o impossibile questo tipo di ricerca. Serve allora la **reverse engineering**: decompilare il software, tornare a (una parte del) codice sorgente, individuare le parti malevole e sradicarle.
### Come si sfrutta un salto nel codice: il crack della licenza
*CS-05 @ 00:38:54*
**Slide "Code injection attacks".** A sinistra il debugger **OllyDbg** su `victim.exe` ("CPU – main thread, module victim"), con disassemblato e un'etichetta "Entry Point"; sotto, una zona di byte `00` (`DB 00`) racchiusa da una parentesi graffa. In alto a destra un blocco modificato: `ASCII "spyware.exe"`, `PUSH 1`, `PUSH victim.0040518A`, `CALL kernel32.WinExec`, `JNB victim.00401189`; una freccia lo collega a un blocco con `CMP EAX,5`, `JNB victim.00405196`, tre `NOP`, `CALL DWORD PTR DS:[<&USER32.MessageBox…`, annotato "(This was JNB SHORT 00401189 earlier before alter)". In basso pseudocodice C decompilato: `qmemcpy(&google_update_path, L"C:\\Program Files (x86)\\Google\\Update\\GoogleUpdate.exe", …)`, `Hardlink::_CreateNativeHardlink(… L"c:\\windows\\tasks\\UpdateTask.job" …)`, `F_to_RunExploit();`, `SchRpcCreateFolder(…)`, `SchRpcSetSecurity(…)` con stringhe SDDL.
Il docente precisa che la slide non mostra la reverse engineering, ma il modo in cui alcuni malware agiscono dentro un software legittimo; e che non può fare una lezione di malware analysis. Per far fare a un programma qualcosa di diverso, spesso malevolo, si individua un punto preciso in cui le istruzioni in linguaggio macchina farebbero un **salto**. Non sempre lo fa un programmatore a mano: esistono software automatici che aiutano gli attori della minaccia.
L'esempio è il **controllo della licenza**. Inserito il codice, il software contatta un servizio online del produttore ("questo codice è registrato a questa macchina, ti risulta?"); il servizio verifica sul database che l'utente abbia pagato e che la data odierna sia nel periodo di licenza, e risponde "ok". Se l'eseguibile viene modificato in modo da saltare questo passaggio e portare l'esecuzione direttamente al responso positivo, il controllo è aggirato. È ciò che fanno i **software craccati**, "quando sono benigni": individuano il punto del codice in cui il programma decide "se il controllo è positivo avvia, altrimenti mostra 'licenza scaduta' e interrompi", e sostituiscono quel salto con uno che porta sempre al ramo positivo. Il software craccato non va mai online e per lui la licenza è sempre valida. Sono le versioni più semplici di bypass. Servono una conoscenza approfondita di come il software è sviluppato e compilato e, a monte, la reverse engineering: il pirata informatico (questo è un attacco di pirateria) ha scaricato la copia benigna, l'ha decompilata e ha visto istruzione per istruzione cosa faceva.
### Sicurezza del ciclo di vita del software, DevSecOps, OWASP
*CS-05 @ 00:42:16*
**Slide "Software lifecycle security and "DevSecOps"".** Il simbolo dell'infinito con *DEV* a sinistra (*PLAN, CODE, BUILD, TEST*) e *OPS* a destra (*RELEASE, DEPLOY, OPERATE, MONITOR*), avvolto da un anello *SEC*; in alto a destra il logo **OWASP®**.
Come si difende un'azienda che produce software? Esiste una letteratura vastissima, soprattutto online e aggiornata ogni anno in base alle minacce, che va sotto il nome di **sicurezza del ciclo di vita del software**. Come un'organizzazione deve aggiornarsi sulle minacce rilevanti per lei, anche i software non sono tutti uguali: un fotoritocco, un videogioco, un poker online, un sistema operativo, un'app bancaria, un social network hanno caratteristiche diverse e interagiscono con hardware diverso (il social con la telecamera, l'app di fitness con il GPS, entrambe magari caricano subito una foto sul social). Ogni componente è software e può essere attaccata.
Il modo migliore è **progettare il software sicuro in tutte le fasi**: formare gli sviluppatori perché non pensino solo alle funzionalità di business e alle scorciatoie, ma alla *security by design*, conoscendo le prassi sicure e non sicure e scrivendo codice che resista il più possibile alla reverse engineering. I compilatori aiutano, ma gran parte della sicurezza la inserisce chi scrive il codice; e questo vale anche quando lo sviluppatore è un'**intelligenza artificiale**, che può scrivere software più o meno sicuro.
**OWASP** (*CS-05 @ 00:44:55*) è un'organizzazione nota perché ogni anno, con sondaggi, produce la **OWASP Top 10**, differenziata per tipi di applicazione: le dieci tipologie di minaccia al software più comuni dell'anno (quindi un profilo di minaccia aggiornato) con le migliori prassi di sviluppo sicuro per contrastarle.
### Integrazione Teams 2026 (lezione 4 2026)
*Capitolo 05, sezione 5 (Sicurezza delle applicazioni)*
- **Doppio punto di vista.** Chi usa software scritto da altri (sistemi operativi inclusi) deve verificare se ha vulnerabilità, se è malevolo o se è già stato sfruttato *in the wild*; chi lo scrive deve verificare che sia sicuro. (Teams 4 @ 0:58:26 - 0:59:54)
- **Analisi statica e dinamica.** Novità strutturale rispetto al 2025 (che parlava di firme e reverse engineering): l'**analisi statica** esamina il sorgente o, se non disponibile, il codice compilato, cercando punti sfruttabili; potente ma non copre tutto, perché gli attori sanno nascondere le tracce. L'**analisi dinamica**, in parte coincidente con il **sandboxing**, esegue il software in un ambiente controllato da cui non può uscire. Il **fuzzing** è la tecnica dinamica che gli fa fare una miriade di cose apparentemente senza senso per trovare errori sfruttabili. (Teams 4 @ 1:01:08 - 1:02:29)
- **Metafora del cavallo di Troia nella sandbox.** Per un malware che sembra innocuo, la sandbox fa sì che se il cavallo si apre i soldati escano non a Troia ma dentro un carcere. (Teams 4 @ 1:02:29 - 1:03:02)
- **Salti nel codice.** Stesso concetto del 2025 (zone di codice inerte, istruzioni forzate verso la parte malevola), qui in forma più sintetica e senza l'esempio del crack della licenza. (Teams 4 @ 0:59:57 - 1:00:59)
- **OWASP e DevSecOps.** Il docente dice "le 10 buone prassi dell'OWASP"; il DevSecOps aggiunge al DevOps la scrittura di codice sicuro fin dall'inizio, verificato poi da personale o sistemi indipendenti. Paragone: lo sviluppatore deve avere nozioni di sicurezza "un po' come voi che siete o sarete analisti dei dati". (Teams 4 @ 1:03:09 - 1:04:52)
## 6. CVE, CVSS e responsible disclosure
*CS-05 @ 00:45:28*
**Slide "Common Vulnerability Events (CVE)".** A sinistra una timeline gennaio–luglio (2015) con CVE per prodotto (legenda: Android, Apache, Flash, Internet Explorer, Java, Office, Windows) e un'icona per gli *Zero-Days*: CVE-2015-0311 (gennaio, zero-day); CVE-2015-0313 (zero-day), CVE-2014-4140, CVE-2015-0069 (febbraio); CVE-2015-1649 (aprile); CVE-2015-1683, -3823, -3824, -1694, -1709, -1835 (maggio); CVE-2015-1754, -3839, -3840, -3842, -2590 (zero-day) (giugno); CVE-2015-2391, -5122, -5119, -2415, -5123, -2425, -2426 (in gran parte zero-day), -3847, -3851, -3852 (luglio). A destra: "Total CVE records for "log4j" (created in December 2021): as of June 2022: **177750**; as of May 2023: **203230**", con il logo LOG4J.
Un altro modo di difendersi è "fare sistema", l'imperativo di von der Leyen. Il sistema in slide è americano ma è diventato lo standard internazionale; il docente anticipa che, per effetto di una nuova normativa europea, l'Europa si doterà di un sistema analogo \[?\] ("di cui è responsabile il titolare").
Il **CVE** ("Common Vulnerability Exposure", nel parlato) è un database consultabile online di tutte le vulnerabilità software riscontrate e pubblicate nel mondo. Ogni vulnerabilità ha un codice **CVE-anno-numero sequenziale**, dove l'anno è quello di pubblicazione. Riguarda tipicamente un prodotto software \[?\] (segue un frammento "di prodotti fisici"). Contiene la descrizione della vulnerabilità e di come sfruttarla, e spesso consigli di rimedio: come aggiornare o configurare il software perché sia, se non invulnerabile, più protetto. Aiuta chi sviluppa e chi usa il software, cioè anche i clienti.
> **Correzione:** CVE significa **Common Vulnerabilities and Exposures**; né "Common Vulnerability Events" (titolo della slide) né "Common Vulnerability Exposure" (parlato).
> **Nota aggiunta:** l'anno nell'identificativo CVE è quello in cui l'ID è stato assegnato o riservato, che può precedere la pubblicazione. Il sistema europeo a cui il docente allude è con buona probabilità l'**EUVD** (European Vulnerability Database), gestito da ENISA in attuazione della direttiva NIS2 e operativo da maggio 2025. I numeri "177750" e "203230" sono dell'ordine di grandezza del **totale** dei record CVE di quei periodi, non dei soli record relativi a log4j (che sono poche decine): la didascalia della slide è probabilmente fuorviante. Il docente non la commenta.
### Perché pubblicare le vulnerabilità
*CS-05 @ 00:47:07*
Il database aiuta anche gli attori della minaccia. Analogia: un elenco online dei lucchetti più e meno sicuri, con scritto come scassinarli; i primi utenti sarebbero i ladri, "un golosissimo database". Perché allora pubblicarlo? Uno studente risponde: per renderle disponibili ai ricercatori, rendere visibile a tutti che la vulnerabilità esiste, darle un nome e indicizzarla. Il docente: "da un punto di vista accademico è vero", ma parliamo di vulnerabilità che permettono milioni di euro di danni o di mettere a rischio vite (i robot chirurgici); c'è un motivo più pratico. Un altro studente: per **fixarle**; e a fixarle sono gli sviluppatori durante il ciclo DevSecOps. "Perfetto." Il sistema esiste perché si è visto che **funziona** e rende più sicura la collettività, tanto che l'Europa ha deciso di dotarsi del suo.
### CVSS
*CS-05 @ 00:49:32*
**Slide "CVSS – CVEs' severity scoring".**
<table header-row="true">
<tr>
<td>Rating</td>
<td>CVSS Score</td>
</tr>
<tr>
<td>None</td>
<td>0.0</td>
</tr>
<tr>
<td>Low</td>
<td>0.1–3.9</td>
</tr>
<tr>
<td>Medium</td>
<td>4.0–6.9</td>
</tr>
<tr>
<td>High</td>
<td>7.0–8.9</td>
</tr>
<tr>
<td>Critical</td>
<td>9.0–10.0</td>
</tr>
</table>
Accanto, la tabella "Distribution of all vulnerabilities by CVSS Scores":
<table header-row="true">
<tr>
<td>CVSS Score</td>
<td>Number of Vulnerabilities</td>
<td>Percentage</td>
</tr>
<tr>
<td>0-1</td>
<td></td>
<td>0.00</td>
</tr>
<tr>
<td>1-2</td>
<td>2</td>
<td>0.40</td>
</tr>
<tr>
<td>2-3</td>
<td>22</td>
<td>4.80</td>
</tr>
<tr>
<td>3-4</td>
<td>5</td>
<td>1.10</td>
</tr>
<tr>
<td>4-5</td>
<td>126</td>
<td>27.80</td>
</tr>
<tr>
<td>5-6</td>
<td>43</td>
<td>9.50</td>
</tr>
<tr>
<td>6-7</td>
<td>31</td>
<td>6.80</td>
</tr>
<tr>
<td>7-8</td>
<td>135</td>
<td>29.70</td>
</tr>
<tr>
<td>8-9</td>
<td>7</td>
<td>1.50</td>
</tr>
<tr>
<td>9-10</td>
<td>83</td>
<td>18.30</td>
</tr>
<tr>
<td>Total</td>
<td>454</td>
<td></td>
</tr>
</table>
"Weighted Average CVSS Score: 7", e l'istogramma "Vulnerability Distribution By CVSS Scores" con gli stessi valori. Sotto, la dashboard [**tenable.sc**](http://tenable.sc) "CVSS Exploitability (E) and Remediation Level (RL) Risk Matrices": quattro heat map (Host Count, Vulnerability Count, Published Exploit Host Ratio, Published Exploit Vulnerability Ratio) con righe *Exploit Unproven / Concept / Functional / High / Not Defined* e colonne *Official Fix / Temporary Fix / Workaround / Unavailable / Not Defined* (i numeri piccoli sono in parte \[illeggibile\]).
"Non ho preparato una slide adeguata", premette il docente. Alle vulnerabilità è associato un **grado di severità**; il sistema di punteggio **CVSS**, non l'unico, dice quanto è grave una vulnerabilità e permette di **proiettare** il punteggio sulla propria organizzazione. Esempio: una vulnerabilità del Mac che dà i privilegi di root a chi visita un sito può essere gravissima (criticità 9.9), ma in un'azienda tutta Windows, dove i dipendenti si collegano solo con il laptop Windows aziendale e dal Mac di casa non possono entrare, "tarata quando vado a calcolare l'indice CVSS sulla mia organizzazione, incide su 0.2%". È un sistema che permette a ciascuno le proprie valutazioni.
> **Nota aggiunta:** la "taratura" di cui parla il docente corrisponde alle **metriche ambientali** (*Environmental*) di CVSS, che modificano il punteggio base in funzione del contesto; il risultato resta un punteggio da 0 a 10, non una percentuale. Il "0.2%" è un'immagine del docente, non un valore prodotto da CVSS.
> **Nota aggiunta (verifica numerica):** i conteggi della tabella sommano a 454 e le percentuali, ricalcolate, coincidono con quelle in slide entro l'arrotondamento a una cifra decimale (somma 99,9%). La media pesata "7" è compatibile solo con una stima che usa l'estremo superiore di ogni fascia (6,98); con il valore centrale delle fasce si ottiene 6,48. Senza i punteggi puntuali non è verificabile oltre. Dettagli nel file divergenze.
### Responsible disclosure
*CS-05 @ 00:51:06*
Accanto al database c'è il processo di **responsible disclosure**. Chi scopre una vulnerabilità (anche per caso, ma di solito **ricercatori di sicurezza** di mestiere oppure **bounty hunter**, più o meno professionali, che lo fanno per ritorno economico) non la pubblica subito: metterebbe in un colpo solo a rischio tutte le organizzazioni vulnerabili. Se decide di adottare il principio, va dall'azienda produttrice. Sui siti di Google, Microsoft, Apple, cercando "responsible disclosure", si trovano le pagine per segnalare, anche con email cifrata; a volte c'è scritto quanto pagano una volta confermata la vulnerabilità.
L'azienda riceve la prova, spesso chiede un **proof of concept**: un piccolo software che dimostra in modo inequivocabile che la vulnerabilità si sfrutta sempre, replicando una procedura, e non solo una volta per caso. A quel punto è incentivata a correggerla: dopo un periodo standard, di solito **90 giorni** (a volte di più, a volte di meno) dal momento in cui ha confermato, la vulnerabilità viene pubblicata. L'azienda ha quindi 90 giorni per produrre un aggiornamento e distribuirlo a tutti gli utenti, in modo che alla pubblicazione abbia fatto tutto il possibile. Se non ha ancora corretto rischia almeno un danno reputazionale, oltre a possibili cause per software non sicuro. L'incentivo è **responsabilizzare** chi vende o distribuisce software, anche open source e gratuito: chiunque può analizzarlo, quindi deve farsi carico delle sue vulnerabilità.
### Ricercatori interni e comunità globale
*CS-05 @ 00:54:38*
Molte aziende mature hanno team di sicurezza interni che testano e ritestano il software prima del rilascio: sono i più efficaci, perché hanno il codice sorgente e conoscono anche vulnerabilità non note. Ma hanno un **bias cognitivo**: dopo otto anni ragionano come dipendenti e sempre meno come attori della minaccia. Serve la comunità mondiale dei ricercatori, anche culturalmente diversa: un giapponese e un italiano, pur entrambi laureati in informatica, notano cose diverse che un ricercatore di Microsoft "a Cupertino" non noterebbe. Sono sentinelle sparse nel mondo, come lo sono gli attori della minaccia.
> **Correzione:** Microsoft ha sede a Redmond (Washington); Cupertino è la sede di Apple. Lapsus del docente, che non cambia il senso.
Lo stesso motivo, anticipa il docente, vale per la **crittografia**: conviene che gli algoritmi siano pubblici e sottoposti a verifiche pubbliche. Quattro, cinque o sei ricercatori della stessa azienda che usa, scopre o brevetta un algoritmo per sé sono molto meno efficaci di un gruppo di ricercatori di tutto il mondo che per anni, anche durante l'uso, ne verifica la robustezza.
### Integrazione Teams 2026 (lezione 4 2026)
*Capitolo 05, sezione 6 (CVE, CVSS e responsible disclosure)*
- **Database europeo.** Conferma che la Commissione europea sta creando un omologo europeo del database CVE. (Teams 4 @ 1:04:58)
- **Crescita esponenziale e intelligenza artificiale.** Nuovo, con dati 2025-2026: il numero di CVE ha cominciato a crescere esponenzialmente dopo il 2023, e ancora di più dopo **marzo 2026**, con i sistemi di identificazione delle vulnerabilità basati su IA generativa, sia generici sia addestrati espressamente. Nel **2025** ci sono state **48.000 CVE**; nei soli **primi due mesi del 2026** questa cifra sarebbe stata superata "di gran lunga". I modelli generativi cercano a tappeto anche cose controintuitive e sanno **concatenare** più vulnerabilità piccole in una catena che complessivamente ha gravità elevatissima. (Teams 4 @ 1:05:25 - 1:05:57, 1:12:16 - 1:13:35) Vedi Punti incerti.
- **Metafora della lama di rasoio.** Pubblicare una vulnerabilità la fa conoscere a difensori e attaccanti; la si pubblica a favore dei difensori, dando loro un vantaggio competitivo con la responsible disclosure. (Teams 4 @ 1:06:09 - 1:06:41)
- **Responsible disclosure: dettagli.** Mail tipicamente cifrata a un indirizzo preposto che garantisce risposta in tempi certi; l'azienda conferma se riesce a riprodurre la vulnerabilità (con indizi o PoC); impegno a correggere entro un massimo, tipicamente **tre mesi**, dopo i quali il ricercatore è autorizzato a pubblicare. Chi segnala è chiunque tranne un dipendente, che usa procedure interne. (Teams 4 @ 1:07:18 - 1:09:44)
- **Zero-day e "N-day".** Definizione nuova e esplicita: una **zero-day** è una vulnerabilità scoperta perché già sfruttata da un attore della minaccia, nota "al giorno zero" in cui si sa che è già usata; sono le più gravi perché è già tardi. Per le CVE pubblicate i giorni si contano dalla pubblicazione: per un PC rimasto spento un mese, una CVE pubblicata 28 giorni prima è una "28-day" per quel computer. Da qui l'igiene informatica: aggiornare sistema operativo, app e software; i software più diffusi hanno aggiornamenti quasi quotidiani. (Teams 4 @ 1:10:29 - 1:12:05)
- **Patch Tuesday record.** Evento di attualità: "martedì scorso" (quindi 8 settembre 2026, rispetto alla lezione del 10/09) Microsoft avrebbe rilasciato patch per **974 CVE** in un giorno, tutte di gravità elevata (fra 7.8 e 8.1), con molte critiche e **due zero-day**; il docente prevede che il trend resterà simile per il resto dell'anno. Spiega che Microsoft rilascia le patch il martedì per distribuirle nel corso della settimana, per limiti di banda verso tutti i PC Windows del mondo. Accenna a nazioni, occidentali e non, che smettono di usare Windows per motivi geopolitici, senza entrare nel merito. (Teams 4 @ 1:13:55 - 1:15:38) Vedi Punti incerti.
- Non ripete l'esempio di CVSS tarato sull'organizzazione (Mac in azienda Windows) né la discussione con gli studenti sul perché pubblicare.
### Integrazione Teams 2026 (lezione 4 2026)
*Contenuti nuovi*
- **Tassonomia a strati dei controlli (parallelo/serie).** Vedi sopra, cap. 06 sez. 6: è la parte concettualmente più nuova, collegata alla catena della compromissione, che però viene rinviata al secondo livello del master. (Teams 4 @ 0:37:04 - 0:38:45)
- **Analisi statica/dinamica, sandboxing, fuzzing.** Non presenti nei manuali 2025 come categorie. (Teams 4 @ 1:01:08 - 1:03:02)
- **Zero-day come categoria definita** e concetto di vulnerabilità "N giorni". Nel 2025 le zero-day comparivano solo come icona sulla slide CVE. (Teams 4 @ 1:10:29 - 1:12:05)
- **Effetto dell'IA generativa sul numero di CVE** e sul concatenamento di vulnerabilità, con i dati 2025 e inizio 2026. (Teams 4 @ 1:05:25, 1:12:16 - 1:13:35)
## 7. Sicurezza del cloud
*CS-05 @ 00:56:49*
A schermo la slide di sezione **"Cloud Security"**. Il docente descrive un data center con gli armadi illuminati e uno "in rosso", compromesso da un dato arrivato dalla rete, in cui un malware si è propagato a tutti i computer dell'armadio: un'ipotesi "purtroppo tutt'altro che ipotetica".
**Slide "Cloud computing and Big Data".**
- Cloud computing **sublimates** data, processes and technologies "into the Cloud": few words have hardly been used more inappropriately than «Cloud» has.
- In fact, nothing is more "*bare metal*" than the infrastructure cloud computing actually relies on.
- Data moved in the Cloud is effectively stored in one or more data centres across the Globe. It is still being stored and processed as usually…though – for public Cloud – *on somebody else's infrastructure*.
- A cloud service provider (**CSP**)'s customers move *capital* (*CapEx*) to *operational* expenses (*OpEx*).
Sotto, la foto di un grande data center.
Come detto nella lezione introduttiva, il cloud è far fare le proprie operazioni sui computer di qualcun altro, che ospita dati e business nel suo data center. Si risparmia molto: niente computer, cavi, abbonamenti Internet, dischi, memoria; niente **spese capitali** (CapEx), solo **spese operative** (OpEx), cioè abbonamenti e affitti. "Mai buzzword è stata più falsa di cloud": evoca le nuvole, ma tutto avviene nei data center, "posti molto freddi e caldi al contempo".
### Edge computing e IoT
*CS-05 @ 00:58:28*
**Slide "Internet-of-Things (IoT)".** "Internet Of Things Ecosystem": più *IoT Device* scambiano *Command* e *Data* (anche "Command & RFI") con un *IoT Hub*, che comunica con la *Internet Network* (Command / Request For Information, Data); la rete invia *Data* alla *IoT Company/Platform* (server), che fa *Analytics* verso un *IoT Remote*, da cui partono *Command / Request For Information*.
Al cloud si accompagna l'**edge computing**: i dati trattati nel cloud (e il docente ricorda che si è in un master in data analytics) sono prodotti o acquisiti da tanti piccoli dispositivi **IoT**: sensori di temperatura e umidità, telecamere, antenne Wi-Fi, apriporta, apri-garage, apri-cofano, alzacristalli, pacemaker, impianti neuronali. Spesso non dialogano direttamente via Internet ma tramite un **hub**, che a sua volta è connesso e parla con il data center del produttore. Richiamando il perimetro di sicurezza: le telecamere di una certa marca si guardano dal telefono collegandosi al **cloud del produttore**, quindi tutti i flussi video passano per quel fornitore. Anche l'IoT è un servizio cloud.
### Macchine virtuali e container
*CS-05 @ 01:00:32*
**Slide "VMs & Containers, the Cloud software layer".** Screenshot di VMware Workstation con macchine Windows 7 annidate, l'ultima delle quali esegue l'emulatore C64 VICE; schema a strati *CONTAINER* (App A/B/C, Bins/Libs, Docker, Host OS, Infrastructure) e due icone di server, una con *Application / Operating System*, l'altra con molte coppie *APP/OS* su *VMware*.
Il cloud conviene perché il gestore fa **economia di scala**: non vi riserva un computer fisico, vi vende una fetta di capacità di calcolo e storage e vi mostra un servizio che gira in una **macchina virtuale** o in un **container**. Il docente dice di non voler spiegare la differenza se non per un aspetto di sicurezza. Ogni volta che si usa Google Drive o Dropbox, o si consuma video o musica, si fa girare software in una VM o in un container nel data center di qualcun altro. Si è clienti (anche di un servizio gratuito); il servizio è software di proprietà di un'azienda, installato in un data center che può essere suo oppure di un terzo, il **cloud service provider**. C'è spesso una **stratificazione di fornitori**, come c'è una stratificazione del cybercrimine (lezione precedente).
**Esempio Netflix.** *CS-05 @ 01:01:42* Fino a qualche anno fa, dice il docente ("lo sapevo perché lavoravo nel settore, non sono più certo che sia così"), tutti i contenuti in streaming di Netflix viaggiavano sul data center di Amazon: app e sito erano brandizzati Netflix, ma i file video stavano su una **CDN** di Amazon, che Netflix pagava. È probabile che nel tempo abbiano differenziato il provider, anche perché Amazon è diventato un concorrente con la sua piattaforma; il docente non entra nelle dinamiche degli studios.
> **Nota aggiunta:** Netflix usa AWS per gran parte della propria infrastruttura applicativa, ma dal 2011–2012 distribuisce i video soprattutto con una CDN propria, **Open Connect**, con server installati presso gli ISP. L'esempio della stratificazione di fornitori resta valido per il backend.
**Slide "Virtualization vs Containerisation".** Due stack: *virtual machines (VMs)* (VM #1, #2, #3 ciascuna con APP, BINS/LIBS, GUEST OS, sopra HYPERVISOR, HOST OPERATING SYSTEM, INFRASTRUCTURE) e *containers* (container #1, #2, #3 con APP e BINS/LIBS sopra DOCKER DAEMON, HOST OPERATING SYSTEM, INFRASTRUCTURE). Testo:
- Virtual machines (**VM**s) emulate hardware, BIOS, firmware, storage, allowing running multiple instances of different OSs, yet with performance and storage overhead due to the need for host machines (so called **hypervisor**s) to emulate one *atomic* stack of hardware, firmware and OS for each **guest** VMs.
- **Container**s rely on compartmentalized resources, running on one (same-OS) kernel which, e.g., shares with every container only bits of its CPU/RAM/storage pools. Linux containers employ in-kernel memory/process/filesystem mechanisms, like cgroups and chroot, as **security boundaries**.
- Containers are collectively managed ("orchestrated") in **swarm**s, which is highly effective for **micro-service** driven architectures.
*CS-05 @ 01:03:22* Nei **container** non si ha l'uso esclusivo della macchina: il sistema operativo è stato scelto per voi e si scelgono solo le applicazioni. Con Linux, comprato un container con una certa versione del kernel \[?\] (numero di versione trascritto in modo non ricostruibile), sopra si può montare una qualunque distribuzione: Red Hat nel mio container, Debian in quello di un altro, SUSE in quello di un terzo. Tutti e tre vedono un sistema apparentemente dedicato, con il proprio file system, ma il kernel è **unico**: mostra a ciascuno come radice di un file system virtuale una sottocartella di un unico file system fisico. Si crede di avere il 100% della CPU, ma il kernel condiviso distribuisce tempo di calcolo e memoria in base a quanto si paga.
Con una **macchina virtuale** vera e propria la macchina è un'astrazione dell'hardware: la si configura (memoria, dischi, numero di processori) e si sceglie il sistema operativo. Sotto c'è un'unica macchina fisica in un cassetto del rack su cui diversi clienti montano sistemi operativi distinti. Il gestore vende pezzi di capacità di calcolo, banda e storage, li **ridimensiona** su richiesta e affitta ad altri ciò che non vi dà. È una vera spesa operativa e ha rivoluzionato l'informatica, rendendo accessibili servizi a chi non poteva permettersi server.
### Il paradigma "Pizza as a Service"
*CS-05 @ 01:06:32*
**Slide "Cloud paradigms – a pizza analogy".** "Pizza-as-a-Service" paradigms, quattro colonne con sei voci (*Kitchen, Gas, Oven, Pizza Dough, Toppings, Cook the Pizza*), in blu "You Manage" e in verde "Vendor Manages":
<table header-row="true">
<tr>
<td>Paradigma</td>
<td>Gestito dal fornitore</td>
<td>Gestito da te</td>
<td>Etichetta</td>
</tr>
<tr>
<td>Traditional On-Premises Deployment</td>
<td>nulla</td>
<td>tutto</td>
<td>Made In-House</td>
</tr>
<tr>
<td>Infrastructure as a Service (IaaS)</td>
<td>Kitchen, Gas, Oven</td>
<td>Pizza Dough, Toppings, Cook the Pizza</td>
<td>Kitchen-as-a-Service</td>
</tr>
<tr>
<td>Platform as a Service (PaaS)</td>
<td>Kitchen, Gas, Oven, Pizza Dough</td>
<td>Toppings, Cook the Pizza</td>
<td>Walk-In-and-Bake</td>
</tr>
<tr>
<td>Software as a Service (SaaS)</td>
<td>tutto</td>
<td>nulla</td>
<td>Pizza-as-a-Service</td>
</tr>
</table>
**Slide "Cloud paradigms – IaaS, PaaS, SaaS"** (source: Microsoft website). Quattro stack di nove livelli (*Applications, Data, Runtime, Middleware, O/S, Virtualization, Servers, Storage, Networking*): in *traditional IT* "You manage" tutto; in *IaaS* "You manage" da Applications a O/S (O/S a metà), il resto "Delivered as a service"; in *PaaS* "You manage" solo Applications e Data; in *SaaS* tutto "Delivered as a service".
Il docente non entra nella "diatriba" fra IaaS, PaaS e SaaS. Il vecchio approccio è quello di chi, per mangiare o vendere la pizza, compra cucina, gas, forno, ingredienti, cuochi. All'estremo opposto si usa tutto di qualcun altro, persino il cuoco e i condimenti, e si paga solo il servizio che la consegna a casa. Si risparmia enormemente, ma **più si virtualizza e si risparmia, più il controllo sulla filiera diventa difficile**. Con tanta concorrenza si trova la pizzeria che piace, ma non si controllano ingredienti e cottura. Aneddoto: c'erano siti di consegna online dove si poteva scegliere la cottura dell'hamburger e altri dove era bloccato dal software.
### Rischi di sicurezza del cloud
*CS-05 @ 01:08:08*
**Slide "Cloud Security".** Citazione: «*The Cloud means powerful computing capabilities for your data – just on somebody* **else**'*s computers.*», attribuita a "someone"; sotto, una fila di rack con al centro uno scudo con lucchetto.
Poiché l'infrastruttura è di altri, non sempre si sa come vengono trattati i dati; spesso i contratti dicono espressamente che alcuni dettagli **non saranno comunicati**, per esempio che i dati potrebbero non stare nel proprio stato ma essere copiati in più località.
Inoltre un servizio cloud, virtuale o fisico, è sempre un sistema informatico ed è vulnerabile come qualunque software. L'hardware virtuale è fornito da un **hypervisor**, che è software: chi compromette la VM o il container e riesce a uscire dalla "prigione virtuale" approda all'hypervisor, lo attacca, scende fino all'hardware. E poiché VM e container sono "aree lottizzate" di un'unica macchina, l'attaccante può trovare un metodo per fare **hopping**, saltare da una VM all'altra, cioè **da un cliente all'altro**.
**Slide "Virtualization-specific TTPs".**
- ***Blue-pill*** **effect**: Some TTPs may allow TAs that have compromised already compromised (sic) a VM/container to *cross* their virtual boundaries and gain access to data stored and/or processed betond (sic) those boundaries. This means pivoting either:
	- from the original VM/container/VLAN to another (so called "VM/container/VLAN hopping");
	- from a VLAN to the overlaying physical LAN or network segment;
	- from a guest VM/container to its host/hypervisor.
- Whatever the effect, such data breach opportunities may potentially impact different customers of one CSP as they propagate to data owned by third subjects.
- Again, this kind of cybersecurity aspects, projected in the cyberspace (5th domain of conflict) must be addressed at a higher level as they usually entail Data Governance.
Diagrammi: in alto *Attacker VLAN 1* e *Victim VLAN 20* collegati a due switch SW1 e SW2 (porte Fa0/1, Fa0/24), con un frame a doppio tag "1 \| 20 \| IP" che diventa "20 \| IP" e poi "IP" (VLAN hopping per *double tagging*); in basso un *Attacker* che entra in VM1 e da lì raggiunge VM2 e VM3 (in rosso) sopra lo stesso *Hypervisor*.
L'esempio del docente (*CS-05 @ 01:10:57*): VM1, VM2 e VM3 nello stesso rack; la prima ospita una pizza delivery italiana, la seconda il database finanziario di un'organizzazione francese, la terza un servizio di streaming musicale americano. Se l'attaccante prende la VM1 ed entra nell'hypervisor, arriva alle altre due: un **attacco alla supply chain** che con un solo colpo gli dà accesso ai dati di aziende di settori e territori completamente diversi. Un cloud non presidiato è un veicolo d'attacco "molto molto lucrativo".
### Fault domain: regioni e zone di disponibilità
*CS-05 @ 01:12:06*
**Slide "Fault domains".**
- For resiliency purposes (mostly availability), CSPs employ *co-located* data centres, grouped in either:
	- \[multi-\]Regions – exclusively based on geography;
	- Availability Zones (**AZ**s) – conglomerates of one or more "*virtual* data centres", atomically available to users.
Figure: la regione AWS *us-west-1 N. California* con i data center *us-west-1a, 1b, 1c* e una mappa con *Oregon*, *N. California*, *GovCloud (US-West)* (legenda *Regions* / *Availability Zones*, source: Amazon, LLC); uno schema *Region* con tre *Availability Zone* collegate da "Low latency resilient fiber connectivity"; uno schema Microsoft con *Region → Availability Zone #1 (Independent power & networking) → Rack #1, #2 → PC #1, #2 → VM #1, #2* e *AZ #2*, *AZ #3* collegate da "Private fiber-optic network" (source: Microsoft).
Per la **disponibilità** (la "A" della triade CIA, l'aspetto che più interessa a un CSP) i fornitori permettono di replicare i dati su più data center. I CSP occidentali hanno data center in tutto il mondo, organizzati in **regioni** (grosso modo stati o aree geografiche), **multiregioni** (grosso modo continenti) e, più astrattamente, **zone di disponibilità**, dove il fornitore ha anche più di un data center. Ci si collega a Spotify o alla pizza delivery "per comprare un kebab", ma il servizio è depositato su vari cloud regionali per servire in modo globale clienti in Nord America, Sud America, Russia, Francia, Egitto. C'è una gerarchia che va dal livello più virtuale (continenti) a quello fisico (la singola VM nel singolo rack), lungo cui i dati sono replicati: se un computer va giù, si rompe un disco, o un albero trancia un cavo in fibra isolando un data center in Florida, il cliente non se ne accorge.
Sono cose positive, e si pagano profumatamente (più disponibilità si chiede, più si paga). Ma sono anche un **rischio**: i canali creati per la replicazione, se non presidiati, permettono agli attori della minaccia di spostarsi molto più rapidamente di quanto farebbero negli altri quattro domini, "terra, mare, cielo e spazio".
### Integrazione Teams 2026 (lezione 1 2026)
*Capitolo 05, sezioni 7 e 12 (cloud, disaster recovery)*
- "Nessuna parola è stata così fuorviante come cloud computing" (Teams 1 @ 0:46:59), coerente con "nulla è più fisico del cloud" del cap. 05.
- CrowdStrike come caso di disaster recovery: i data center con ripristino automatico della versione precedente ripartono, gli altri richiedono intervento manuale macchina per macchina (Teams 1 @ 0:35:09).
### Integrazione Teams 2026 (lezione 4 2026)
*Capitolo 05, sezione 7 (Sicurezza del cloud)*
- **Il data center in foto.** È un data center di Facebook di quasi vent'anni fa; quelli moderni sono capannoni progettati per i computer, che ottimizzano ricircolo di aria calda e fredda fra fronte e retro dei rack, cogenerazione elettrica, impatto ambientale. (Teams 4 @ 1:16:16 - 1:16:59)
- **IoT: l'elaborazione avviene nel cloud.** Motivazione nuova: il sensore o la telecamera da pochi euro, a batteria, ha appena la capacità di registrare e inviare; riconoscimento di persone, movimento, targhe, codici a barre e le notifiche ("il gatto ha attraversato la cucina") sono calcolate nel cloud del produttore. Richiamo alla lezione precedente sulle interdipendenze. (Teams 4 @ 1:17:03 - 1:18:41)
- **Rischio principale: hopping fra clienti.** Stesso contenuto del 2025 (pizza delivery accanto alla VM del produttore di telecamere; effetto pillola blu, "vedere la Matrix"), con l'aggiunta che è oggi "il rischio di sicurezza cloud più grande" perché mette in relazione soggetti di Stati, settori e clientele diverse, ed è difficile da contenere anche giuridicamente. (Teams 4 @ 1:20:30 - 1:23:16)
- Non tratta regioni e zone di disponibilità, né la differenza VM/container, né CapEx/OpEx in questa lezione.
### Integrazione Teams 2026 (lezione 5 2026)
*Contenuti nuovi*
- **Forensics nel cloud, catena di custodia, CTU.** Tema non presente nei manuali 2025, che trattavano la sovranità solo come rogatoria e trasferimento del dato. (Teams 5b @ 0:02:04 - 0:08:10)
- **Geopolitica delle dorsali e dei data center** (mappa generata con Copilot, cavi verso Africa e India, potere politico dei CSP). (Teams 5b @ 0:10:01 - 0:15:18)
- **NOS e NOSI.** Nulla osta di sicurezza per persone e per aziende. (Teams 5b @ 0:36:10 - 0:37:00)
- **Vulnerability and Patch Management e asset management** come processo distinto dal VA. (Teams 5b @ 0:59:26 - 1:04:32)
- **Tabletop exercise** come prima forma di test di resilienza, con esempi di ISAC. (Teams 5b @ 1:14:04 - 1:17:58)
- **Pentest out-to-in.** (Teams 5b @ 1:10:11)
## 8. Data governance
*CS-05 @ 01:15:00*
A schermo la slide di sezione **"Data Governance and Privacy"**. La sicurezza nel cloud porta alla **privacy**, ma prima occorre parlare di **governance dei dati**, "in un corso di data analytics non si può non parlarne"; il docente richiama anche la domanda di un collega, a inizio corso, sui dati in Nord America e in Europa.
### Sovranità, localizzazione, co-location
**Slide "Data Governance".**
- **Sovereignty** – Data is subject to laws of the country which it is physically stored in (data centres!): the ability to own, operate and master data and its processing.
- **Localization** – Copy of certain data (e.g. sensitive/personal/public data) are required to be held within the country's borders, usually to guarantee that the relevant government can audit on its own citizens (subject to legitimate cause) without contending with third subjects' jurisdictions – or (e.g. as is the case with classified data) for national security reasons.
- *Co-location* – Replication of multiple data copies at geographically separate locations (DR).
Data governance also depends on ***data influence*** **zones** (i.e. **political** and **geographical** borders) which ultimately determine both *in-transit* and *at-rest* data policies, e.g. cryptography to adopt.
Sotto, la mappa luminosa delle connessioni mondiali.
"Nulla è più fisico del cloud": parlando di sicurezza si arriva sempre al livello fisico. I dati stanno in data center che sono **immobili piantati sul territorio** di uno stato sovrano, soggetti alle sue leggi. Oltre alle complicazioni tecniche ("negli ultimi dieci minuti ho fatto un crash course sul cloud computing, se non vi ho fatto venire mal di testa sarei stupito"), ci sono quelle **normative**: se i dati di uno stesso servizio stanno in Nord America e in Italia, le leggi differiscono (controllo governativo e parlamentare, law enforcement, codice penale, civil law contro **common law** basata sulle sentenze) e ogni contenzioso diventa "un possibile vespaio".
**L'esempio della rogatoria.** *CS-05 @ 01:17:13* Un attacco a un cliente italiano viene ricondotto a un data center in America. Un giudice italiano dovrà parlare con un giudice americano, che mandi una forza dell'ordine competente (in America c'è anche la questione federale: FBI o polizia locale?). Con quale mandato? Con accordi specifici, soprattutto cyber, è più semplice, e in Europa ci si sta organizzando per snellire le procedure. Ma con stati legalmente e amministrativamente "infinitamente distanti" (Russia, Cina, India, e in alcuni c'è un conflitto in corso) come si fa? E ammesso che ci siano basi legali e che la polizia bussi alla porta del CSP, il CSP può rispondere: gli eventi sono di tre settimane fa (nella migliore delle ipotesi, a volte passano mesi), il dato si è spostato da un disco o da un rack all'altro, il disco si è rotto, non so fisicamente dove fosse; o peggio, nella mia legislazione ho garantito al cliente l'anonimato totale, "non te lo confermo né te lo nego". Questi sono i problemi di **sovranità** del cloud.
Il cyberspazio è tecnicamente uno spazio unico di risorse interconnesse, con uno spazio di indirizzi "flat". Ma i dati viaggiano per **zone di influenza**, e i confini geografici e politici contano perché determinano le politiche sui dati **a riposo** (data center e infrastrutture dove sono memorizzati e processati) e **in transito** (i canali "mica sono nuvole": c'è sempre un router o un satellite; i cavi stanno in tubature su suolo nazionale o internazionale, e i cavi sottomarini hanno anche loro una giurisdizione, "è quasi peggio"). È un tema di governance dibattuto da anni, influenzato dai conflitti recenti e in corso, perché sfocia nell'ambito della guerra.
### Data space
*CS-05 @ 01:22:09*
**Slide "Data Space".** Al centro "Data sharing in a **Data Space**", "Data exchange and data processing along the data value chain". A sinistra *Data Owner* → *Usage Policies* → *Data* → *IDS Connector* (con *App* e scudo), sotto l'etichetta *Data Provider*; a destra, simmetrico, *IDS Connector* → *Data* → *Data User*, etichetta *Data Consumer*. Intorno: *Broker*, *Clearing House*, *App Store*, *Identity Provider*, *Vocabulary*. Nella versione completa (da 01:24:00) le frecce: il provider "publishes metadata" al Broker, il consumer "searches metadata"; entrambi "logs transactions" verso la Clearing House; entrambi sono collegati all'Identity Provider. In basso: «Decentralised infrastructure for trustworthy data sharing and exchange in data ecosystems, based on commonly agreed principles.», fonte OpenDEI.
Si parla di **spazio dei dati** per indicare dove si trovano astrattamente. Di solito si sa chi è il **data provider** e chi il **data consumer**: ascoltando Spotify, il provider è Spotify ("azienda americana con sede legale in California, se non sbaglio") e il consumer sono io. In mezzo ci sono interfacce: per il login uso l'identità di Google o Facebook come **identity provider** (tema del prossimo corso); per scaricare i dati mi servo di intermediari che magari trattano solo **metadati**, a loro volta intermediati da altri. I dati fanno tre o quattro volte il giro del mondo prima di arrivare allo smartphone, ed è impossibile tracciare tutto. Quando c'è una questione legale, per esempio un incidente da trattare con il law enforcement, bisogna risalire la catena di reti e giurisdizioni attraversate: è uno dei maggiori ostacoli, e gli attori della minaccia se ne servono per intermediarsi, rendere difficile individuare l'origine e persino l'**attribuzione**. È lo "spazio grigio" della lezione precedente, fra lo spazio rosso usato dall'attaccante e quello blu della vittima.
> **Correzione:** Spotify non è un'azienda americana: è svedese, con sede operativa a Stoccolma (la holding Spotify Technology S.A. è registrata in Lussemburgo). Il docente stesso esprime incertezza ("se non sbaglio").
### Data Governance Act
*CS-05 @ 01:24:17*
**Slide "Data Governance Act".** In alto: "REGULATION (EU) 2022/868 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL of 30 May 2022 on European data governance and amending Regulation (EU) 2018/1724 (Data Governance Act)".
- Creates conditions for the re-use, within EU, of certain categories of data held by public bodies (it does *neither* force subjects to allow for data re-use, *nor* release their confidentiality obligations).
- Creation of different frameworks for the:
	- provision of data intermediation services;
	- voluntary registration of entities collecting/processing data for altruistic purposes; (riquadro: **data altruism** – voluntary data sharing on the basis of authorizations by data subjects/holders, without any rewards… e.g. healthcare, natural causes prevention, improving mobility, official statistics, public services provisioning, scientific research, …)
	- establishment of the European Data Innovation Board (**EDIB**), also supporting **Data Act** obligations.
- Introduces new concepts:
	- consent – sort of "authorization" as per **GDPR**, by data subjects and related to *personal data* only)
	- permission – sort of "authorization", by data holders and related to *non-personal data* only);
	- data user – *neither* a d. subject *nor* a d. holder, who has the right to use data for \[non-\]commercial purposes.
Anticipazione del docente ("se ci sarà tempo parlerò di altre leggi europee sui dati"): nel 2022 l'Europa si è dotata del **Data Governance Act**, che categorizza i dati, soprattutto quelli usati dal settore pubblico, e stabilisce le condizioni per utilizzarli, condividerli con il pubblico o riutilizzarli fra enti; istituisce un board europeo per l'innovazione sui dati. In analogia al GDPR, che tratta i dati personali, introduce tre concetti: anche per dati non personali può servire un'autorizzazione al trattamento (all'esterno o per finalità diverse); come c'è il **consenso** degli interessati, ci può essere il **permesso** dei titolari dei dati; e c'è una terza categoria, distinta da titolare e interessato, che può avere o meno il diritto di usare il dato (il **data user**).
Il docente dice espressamente che il DGA **non sarà oggetto di esame**; ha dato i riferimenti del regolamento per chi è interessato, ma ritiene che chi si occuperà di dati nel settore pubblico in Europa debba conoscerlo almeno in parte. Vedi sezione 16.
> **Nota aggiunta:** nel parlato la prima frase ("può essere necessario da parte dei titolari dei dati di esprimere il consenso") attribuisce il consenso ai titolari; la slide è più precisa: il *consent* è degli interessati e riguarda solo i dati personali, il *permission* è dei *data holder* e riguarda i dati non personali.
### Policy italiana sul cloud per la PA
*CS-05 @ 01:26:21*
**Slide "Italian Cloud policies – CSP qualification".** Schema: "Classificazione dati e servizi per la PA" → "Elenco dei servizi e dei dati della PA classificati, secondo il proprio livello di criticità": *strategico*, *critico*, *ordinario*. Due frecce verso "Adeguamento di infrastrutture e servizi della PA" e "Migrazione su infrastrutture/servizi qualificati", sotto l'etichetta verticale "Requisiti da rispettare": "**Livelli minimi** di sicurezza e affidabilità, capacità elaborativa, risparmio energetico **delle infrastrutture digitali per la PA**" e "**Caratteristiche** di qualità, sicurezza, performance e scalabilità, interoperabilità e portabilità dei **servizi *cloud* per la PA**". In basso, logo ACN: "Qualificazione di infrastrutture digitali/servizi *cloud*" → "Processo tramite il quale ACN valuta la conformità di infrastrutture/servizi offerti da operatori privati". Source: Agenzia per la Cybersicurezza Nazionale (ACN), [https://www.acn.gov.it/portale/cloud/regolamento-cloud-per-la-pa](https://www.acn.gov.it/portale/cloud/regolamento-cloud-per-la-pa)
In Italia c'è una **policy del cloud** per la pubblica amministrazione. Le prime "qualifiche del cloud" le fece **AgID** nel decennio scorso; poi sono state riviste dall'**ACN** in chiave cyber sicurezza. Riguardano soprattutto i CSP e le PA, che prima di usare un cloud pubblico devono capire se possono farlo. Ciò che il docente vuole che si porti a casa: per i dati nel cloud della PA occorre una **classificazione** in tre livelli, **ordinario**, **critico** e **strategico**. Solo per i dati strategici, stimati da un censimento ACN "dell'anno scorso" nell'**8%** dei dati totali della PA, è obbligatorio che il data center sia **esclusivamente in Italia**.
### Ruoli della data governance
*CS-05 @ 01:27:58*
**Slide "Data governance roles".**
- **Owner** – is the organizational subject responsible for determining about data: the impact on the org.; its replacement costs (if data can be replaced); who can access it (both in/outside of the org.) and under what circumstances; evaluate its quality (e.g. inaccurate) and decide whether to refresh, delete/destroy it (data life-cycle). As regards personal data protection (*ex* **GDPR**) the data owner is the data controller.
- **Steward** – discretionarily translates the data owner's requirements into policies (semantics, data quality, …), creating new or integrating existing business processes with management of those data.
- **Custodian** – is accountable for implementing and maintaining procedures and security controls to meet data security requirements outlined by the data owner.
- **Processor** – Subject actually processing the data on behalf of the data owner, e.g. the CSP itself.
Figura: piramide *Governance Level* (*The Board*, *Senior Management*) → *Business Processes* → *Information Systems*, allineata a *Strategies* / *Tactics* / *Operations* e a *Data Owner* (Strategic Goals, Opportunities, Decision Making), *Data Steward* (Data Quality, Data Rules, Data Semantics), *Data Custodian* (Data Sources). A destra una nuvola incatenata con lucchetto: "vendor **lock-in** !".
La governance stabilisce **ruoli e responsabilità**. Il **titolare** (*owner*) è il soggetto dell'organizzazione che stabilisce tutto sui dati: l'impatto che i dati o la loro indisponibilità avrebbero; i costi per sostituirli o ricostruirli se persi o corrotti; chi vi accede e per fare cosa (leggere, modificare, contribuire aggiungendo o incrementando, usare pagando o no, o perché la legge glielo impone); i livelli minimi di qualità; ad altissimo livello il **ciclo di vita** (quando archiviarli, farne backup, metterli da parte o cancellarli). Per i dati personali il ruolo spetta al titolare del trattamento previsto dal GDPR, con altre considerazioni.
Poi lo **steward** ("pastore dei dati") e il **custode**, che traducono i requisiti di alto livello del titolare e ne curano l'implementazione, soprattutto quando chi tratta il dato è diverso dal titolare. Se faccio trattare il mio dato in un cloud di un altro soggetto, resto titolare; il fornitore può esserne custode; e magari un titolare del servizio cloud si fa carico solo della **disponibilità**, garantendomi l'accesso.
### Integrazione Teams 2026 (lezione 5 2026)
*Capitolo 05, sezione 8 (Data governance)*
- **Perché governance, protezione e classificazione insieme.** Il docente dice che un corso di master di primo livello sarebbe incompleto senza almeno sfiorare questi tre temi, legati alla privacy che è nel titolo del corso. (Teams 5b @ 0:00:04 - 0:00:20)
- **Performance di rete e collocazione dei data center.** Riprende la mappa delle connessioni di Facebook del 2010 (già vista parlando di reti) per mostrare dove conviene collocare i data center: vicino alla clientela o almeno su connessioni veloci. È ingegneria, ma sfocia nella sovranità. (Teams 5b @ 0:00:38 - 0:02:04)
- **Forensics nel cloud e catena di custodia.** Nuovo: in un procedimento penale o in un'inchiesta, oppure quando un privato o un'impresa chiede al CSP prove per difendersi, l'acquisizione deve seguire una **catena di custodia** per mantenere la prova inalterata, altrimenti è contestabile in giudizio; i consulenti tecnici (in Italia i **CTU**) devono recarsi fisicamente dove si trova il dato, come gli agenti in tuta bianca sulla scena del crimine. Le parti coinvolte nel cloud non sono più due ma tre, quattro, cinque, sei. (Teams 5b @ 0:02:04 - 0:04:33)
- **Il CSP può non sapere dove sono i dati.** Anche in totale buona fede il provider può non sapere in quale data center avvenisse il fatto; a volte lo dice per confondere le acque. Se il data center è in un altro Stato, l'hard disk sta in un rack, in un edificio, su un suolo sovrano soggetto alle leggi di quel paese. Esempi di esiti: Russia, costa occidentale USA (San Francisco), un data center "di passaggio" fra Norvegia e Svezia; parte italiana e controparte a Hong Kong, ma la parte materiale si svolge sotto una terza legge. (Teams 5b @ 0:04:33 - 0:07:04)
- **Tempi incompatibili con l'incident response.** Esempio nuovo: dopo un attacco servono i log di un server cloud; il provider li ha ma non sa su quale data center, oppure la procedura prevede che la richiesta la faccia la forza dell'ordine del paese del data center e servono giorni: nel frattempo il criminale ha cancellato le tracce. Anche con la cooperazione di tutti, i tempi legali sono incompatibili con quelli di un attacco. (Teams 5b @ 0:07:19 - 0:08:10)
- **Outage dei grandi CSP.** Nuovi esempi di attualità: i grandi CSP cadono vittime quasi regolarmente di attacchi, in particolare DoS, che rendono inutilizzabili data center o intere regioni; "l'anno scorso" un disservizio legato a un bug DNS; due o tre anni fa un grande down di AWS in America, che per Netflix non ha causato danni grazie alla distribuzione su più data center. (Teams 5b @ 0:08:50 - 0:09:44) Vedi Punti incerti.
- **Potere politico dei CSP.** Nuovo: la capacità di fornire resilienza globale a governi, comparti militari e grandi aziende dà ai grandi provider un potere "illimitato", anche politico: siedono ai tavoli con i decisori su come normare lo spazio dei dati. Per questo l'Europa ha sentito il bisogno di normare IA, identità digitali, cyber resilienza e anche la governance dei dati, per evitare monopoli. Ripete l'esempio Netflix su AWS (Amazon concorrente sugli studios ma fornitore di infrastruttura). (Teams 5b @ 0:10:01 - 0:12:30)
- **Mappa di data center e cavi, generata con Copilot.** Nuova slide: diagramma fatto generare a Copilot un paio d'anni fa, "come disegnato da un bambino" (era uno dei criteri dati), con i data center dei principali CSP (azzurro Azure, verde Google, arancione Amazon, marrone gli altri; quadrati per quelli non confermati) e le dorsali in fibra. Invito a guardare non tanto i cavi transatlantici e transpacifici ma quelli verso **Africa** e **India**: alcune superpotenze sfruttano la carenza di infrastrutture nei paesi meno sviluppati per ottenere un vantaggio competitivo e far passare i dati di paesi con peso geopolitico (anche per le materie prime) attraverso le proprie infrastrutture. Presentato come spunto di riflessione, fuori dagli scopi del corso. (Teams 5b @ 0:12:30 - 0:15:18)
## 9. Dati personali e GDPR
*CS-05 @ 01:30:04*
Con i dati personali si entra nella sfera del **GDPR**. Il docente ripete quanto detto nella lezione 2: il regolamento riguarda tutte le organizzazioni che trattano dati personali di **cittadini europei**, anche in paesi extraeuropei che, in base ai trattati internazionali, riconoscono il diritto dell'Unione e sono quindi obbligati a rispettare i regolamenti europei con effetti extraterritoriali. Se un cittadino francese va a vivere in America, magari con doppia cittadinanza, la protezione dei suoi dati resta soggetta al GDPR, e le organizzazioni degli stati che "riconoscono l'Europa" (quasi tutti, secondo il docente) devono rispettarlo, pena l'infrazione di un trattato.
> **Correzione:** come già segnalato per la lezione 2, l'ambito territoriale del GDPR (art. 3) non dipende dalla **cittadinanza** dell'interessato né dal fatto che lo stato del titolare "riconosca il diritto dell'Unione". Si applica ai titolari e responsabili stabiliti nell'UE e, per quelli non stabiliti, ai trattamenti di dati di interessati **che si trovano nell'Unione** quando si offrono loro beni o servizi o se ne monitora il comportamento. Il cittadino francese residente in America, trattato da un'azienda americana per servizi offerti negli Stati Uniti, di regola non è coperto dal GDPR.
### Titolare, responsabile, DPO
*CS-05 @ 01:31:49*
**Slide "*Personal* data governance roles – ex GDPR".**
- **Controller** (*titolare del trattamento dei dati personali* in Italian) – Subject (usually a legal person) who is responsible for the determination of the purpose about subjects' personal data.
- **Processor** (*responsabile del trattamento…* in Italian) – Subjects to whom controllers have delegated/outsourced data processing tasks.
- Data protection officer (**DPO**, *RPD* in Italian) – Optional but sometimes mandatory accountant that oversees an organisation's data-protection strategies; he/she reports *data breach*es to national GDPR authorities / supervisory bodies.
- GDPR supervisory authority – In Italy, *Garante per la protezione dei dati personali* (**GPDP**).
Figure: logo DPO "Data Protection Officer" e logo GPDP; schema con *Processor* (Payroll, Marketing), *Controller*, *Joint Controllers*, *DPO*, *ROPA*, *Auditor*, *Regulator*; due riquadri: **Data Processors** ("Any organization that collects, processes, stores or transmits personal data"; "Needs to maintain an audit trail of all processing activities") e **Data Controllers** ("Any organization that directs the processor's activities"; "Defines the how and why of personal data processing").
Il GDPR individua tre figure. Il **titolare del trattamento** (*data controller*), tipicamente una persona giuridica, come l'owner per i dati, determina tutto sul trattamento e ne stabilisce le politiche. Il **responsabile del trattamento** (*processor*) è il soggetto a cui il titolare delega i compiti di trattamento.
**Esempio dell'ospedale.** *CS-05 @ 01:32:21* Leggendo in sala d'attesa l'informativa privacy di un ospedale, il titolare è l'azienda sanitaria (una S.p.A. se privata) presso la sua **sede legale**, magari in un'altra città rispetto all'ospedale di provincia in cui ci si trova. Il responsabile può essere il singolo dipartimento, per esempio la diagnostica per immagini per le radiografie, oppure, se le macchine diagnostiche sono gestite da un servizio terzo, quel servizio. Il GDPR impone che l'interessato sappia chi è, dove si trova e come raggiungerlo legalmente. Le figure di una certa grandezza devono avere un indirizzo di contatto per reclami, informazioni e per l'esercizio dei diritti definiti dal GDPR.
**Il DPO.** *CS-05 @ 01:33:55* Per alcune organizzazioni è obbligatorio (secondo il docente tutte le PA e le aziende oltre una certa grandezza), per le altre facoltativo. Contrariamente a quanto si crede, può essere un dipendente o un consulente esterno; anche se dipendente ha una certa **autonomia**. Il suo compito principale è vigilare che il trattamento dei dati personali sia conforme al GDPR; da regolamento "si schiera dalla parte degli interessati" e consiglia azienda o committente su modalità diverse di trattamento. In Europa il trattamento dei dati personali è stato ritenuto così critico, perché tocca **diritti fondamentali**, da richiedere non solo obblighi ma anche persone in ogni soggetto che ne controllino il rispetto.
> **Correzione:** l'obbligo di nominare un DPO (art. 37 GDPR) non dipende dalla dimensione dell'azienda. È obbligatorio per autorità e organismi pubblici (salvo le autorità giurisdizionali) e per i soggetti le cui attività principali consistono in un monitoraggio regolare e sistematico degli interessati su larga scala o nel trattamento su larga scala di categorie particolari di dati o di dati giudiziari.
> **Nota aggiunta:** secondo il GDPR (art. 33) la notifica dei data breach all'autorità di controllo spetta al **titolare**; il DPO è il punto di contatto con l'autorità e ne coopera. La dicitura della slide ("he/she reports data breaches…") descrive una prassi frequente, non l'obbligo normativo.
### Diritti degli interessati e impostazioni di privacy
*CS-05 @ 01:35:38*
**Slide "Privacy and data processing".** Screenshot delle "Privacy Settings" di Facebook (account "Alex Wawro"): "Control Privacy When You Post", "Control Your Default Privacy" cerchiato in rosso con le opzioni *Public* (selezionata), *Friends*, *Custom*; sotto *How You Connect*, *Timeline and Tagging*, *Ads, Apps and Websites*, *Limit the Audience for Past Posts*, *Blocked People and Apps*. Una freccia rossa indica la voce "Privacy Settings" nel menu a tendina.
I diritti degli interessati sono tantissimi. A monte: l'interessato deve poter sempre **esprimere il consenso** al trattamento e **revocarlo**; deve essergli presentata con chiarezza la **finalità**: perché l'organizzazione tratta certi dati, come, e soprattutto se li trasferisce a **terzi e quarti**, specialmente se fuori dall'Unione, dove il GDPR potrebbe non essere altrettanto rispettato e l'enforcement più debole; il GDPR obbliga a farlo sapere prima. Per questo i servizi fanno compilare tante opzioni di privacy, che il docente invita a controllare su tutti i siti dove si ha un account: esistono impostazioni avanzate che "cambiano posto nel tempo appositamente per rendervi difficile trovarle".
**Slide "Privacy settings and their defaults"** (diagramma di flusso). *Functionality / behaviour* → "Configurable by user?". Se NO: "Wired-in; no choice by user possible" (domande: *Which setting? Who decided?*). Se YES → "Preconfigured?". Se YES: "Default setting; change by user possible" (*Which setting? Who decided? Changes possible how & when?*). Se NO: "No default setting; choice by user possible or necessary" (*Who decided? Configuration possible how & when?*).
Una grande discriminante sono i trattamenti su cui il fornitore permette di esprimersi (autorizzarli o no, capire cosa significa) e, se autorizzati, se saranno **automatici** o no: con l'intelligenza artificiale il trattamento automatico ha un'importanza enorme.
**Il caso LinkedIn.** *CS-05 @ 01:37:42* Da poche settimane LinkedIn (il docente è solo su LinkedIn, ma gli dicono che su altri social è successo anni prima) ha aggiunto un'impostazione con cui chiede il consenso ad **addestrare la sua intelligenza artificiale** sui contenuti generati dagli utenti, anche in passato. Il problema non è l'impostazione, ma che, come spesso accade con le app mobile, essendo nuova è stata **attivata di default**; secondo il docente in modo non perfettamente trasparente né conforme al GDPR. Ad alcuni utenti è stato presentato solo "sono cambiate le condizioni di servizio, rileggi e ridacci il consenso": chi avesse letto tutte le 89 pagine avrebbe trovato il nuovo trattamento, e oltre ad accettare l'intero accordo (pena "cancellarsi dall'internet") avrebbe dovuto trovare quell'impostazione specifica (dati per l'addestramento, inclusi post passati, attività, pubblicità viste) e disattivarla.
**Slide "Privacy settings and their defaults"** (seconda versione, a schermo verso 01:43:03). Tre screenshot: iOS "Privacy \> Microphone" (Instagram e WhatsApp attivati; Shazam, Skype, Snapchat disattivati; "Applications that have requested access to the microphone will appear here."); Android "App permissions" di Hangouts (Device & app history, Identity, Contacts, Location, SMS, Photos/Media/Files, Camera, tutti attivi); Android "App permissions \> Camera" (Camera, Chrome, Drive, Google app, Google Play services, Google+, Hangouts, Translate, tutti attivi).
**Le app mobile.** *CS-05 @ 01:40:05* Lo store elenca i privilegi richiesti e permette di scegliere se installare; poi si possono disattivare, per esempio, microfono o webcam. Ma quando l'app si **aggiorna** (in automatico, e il docente consiglia di lasciarlo così) e ha bisogno di nuovi permessi, spesso il fornitore li **abilita di default**. Esempio: un videogioco che all'inizio permetteva solo di parlare con gli altri giocatori chiedeva solo il microfono; aggiunta l'opzione webcam, dopo l'aggiornamento serve la telecamera e il permesso è attivo per impostazione predefinita. Secondo il docente, trattando la telecamera dati personali (anche di altri), il default dovrebbe essere **disattivato**, con un pop-up chiaro ("abbiamo aggiornato l'app, se vuoi abilita la camera"). Molte app si trincerano dietro il fatto che senza quel permesso l'app non funzionerebbe, quindi il consenso "non può essere chiesto": è una scusa comoda, perché potrebbe trattarsi di una funzione opzionale. Su questo c'è un dibattito legale che coinvolge i garanti europei. Consiglio generale: **controllare periodicamente** le app installate su smartphone e computer e i permessi concessi, perché con gli aggiornamenti vengono rivisti "nell'ottica non del consumatore ma del produttore".
### Integrazione Teams 2026 (lezione 5 2026)
*Capitolo 05, sezione 9 (Dati personali e GDPR)*
- **Date.** GDPR adottato nel 2016, in vigore di fatto dal 2018; ci si adeguava già da prima e forse ancora non completamente. La protezione dei dati personali è riconosciuta come diritto fondamentale. (Teams 5b @ 0:15:24 - 0:16:17)
- **Esempio del menù a tendina della nazionalità.** Nuovo: le piattaforme americane o cinesi chiedono la nazionalità con un menù a tendina; se per errore scelgo "Iraq" invece di "Italia" (è poco sotto), il sistema tratterà i miei dati secondo altra legge (cinese, o americana, che varia da Stato a Stato, la più nota quella californiana), ma il mio diritto europeo non viene meno: in teoria il fornitore dovrebbe accertare la reale nazionalità. Per alcune corti la dichiarazione basta, per altre no. Il ragionamento si basa sulla cittadinanza (vedi Divergenze). (Teams 5b @ 0:16:52 - 0:18:48)
- **Diritti elencati.** Informativa prima del consenso, minimizzazione (dati minimi necessari al servizio), opposizione al trattamento, rettifica, cancellazione se non servono ad altri obblighi di legge (**diritto all'oblio**). (Teams 5b @ 0:18:48 - 0:19:38)
- **Il GDPR come modello.** Stati Uniti, Canada e Svizzera hanno adottato regolamenti simili (negli USA con differenze importanti), per la giustezza di alcuni diritti e perché trattare i dati in due modi a seconda del passaporto era troppo costoso; resta il problema di chi ha due o tre passaporti. Il docente precisa che è un campo legale, non suo. (Teams 5b @ 0:19:38 - 0:20:48)
- **Quattro ruoli, ne tratta tre.** Titolare (*data controller*), responsabile (*data processor*), DPO. (Teams 5b @ 0:20:48)
- **Esempio dell'ospedale, versione 2026.** Diverso dal 2025 (che citava sede legale e dipartimento di diagnostica): il titolare è l'azienda ospedaliera; se ci visita un dipendente (infermiere, medico), titolare e responsabile coincidono nell'azienda; se ci visita un medico esterno a partita IVA, il responsabile per quel trattamento è il professionista, con una "corresponsabilità" dell'ospedale. (Teams 5b @ 0:21:34 - 0:23:05) Vedi Divergenze.
- **DPO "as a service".** Nuovo: il DPO non è necessariamente un dipendente; esistono molti DPO esterni che lavorano per più titolari, soprattutto per aziende e PA di media dimensione, obbligate ad averlo ma non abbastanza grandi da averne uno interno. Se è dipendente, gli vanno garantite autonomie e poteri. La ragione storica: il GDPR, regolamento di rango superiore imposto a molti più soggetti (molti obblighi esistevano già nella legge italiana), poteva trovare impreparati AD e CdA anche in buona fede. (Teams 5b @ 0:23:05 - 0:26:40)
- **Opt-in e opt-out.** Nuovo come definizione esplicita: **opt-in** = funzione disattivata di default, l'utente deve attivarla; **opt-out** = attivata di default, l'utente può tirarsene fuori. Secondo il docente il GDPR impone l'opt-in di default per tutti i trattamenti di dati di cittadini europei, o di non europei da parte di aziende con sede in Europa; per questo c'è sempre una barriera all'ingresso alla registrazione, con un minimo di trattamento autorizzato. La slide 2025 a rombi ("preconfigured sì/no") viene qui spiegata come domanda su quale sia l'impostazione di default. (Teams 5b @ 0:27:44 - 0:30:08)
- **Permessi delle app: lettura e scrittura.** Nuovo e pratico: sia su iOS sia su Android, dando accesso ai **contatti** l'app li può leggere ma anche scrivere; con l'accesso al **telefono** può leggere il registro chiamate, rispondere e persino chiamare al posto vostro; con gli **SMS** può inviarli e rispondere. Tecnicamente esistono permessi distinti in lettura e scrittura, ma di solito le app non li usano e il permesso è bidirezionale. Su iPhone, per le foto, si può scegliere a quali singole foto dare accesso. Esempi di permessi da revocare dopo la prima configurazione: fotocamera per il login con QR code, scansione della rete, Bluetooth (salvo per le cuffie). Conclusione: le app tendono a scalare privilegi con gli aggiornamenti, vanno riviste periodicamente, soprattutto quelle di cui ci si fida meno. Non ripete il caso LinkedIn e IA. (Teams 5b @ 0:30:24 - 0:33:43)
## 10. Sicurezza amministrativa e assicurazioni cyber
*CS-05 @ 01:43:50*
A schermo la slide di sezione **"Administrative Security"**. Ricapitolando la triade dei controlli (fisici, tecnologici, amministrativi): la sicurezza tecnologica, "apparentemente la più rilevante per la cyber security", è stata declinata in sicurezza delle applicazioni e del cloud, con la digressione su data governance e privacy. Ora si arriva alla **sicurezza amministrativa**, che "non è meno importante" delle altre due.
**Slide "Administrative Security".** Un modello di **NON-DISCLOSURE AGREEMENT** ("This Agreement is made on DD/MM/YYYY BETWEEN \[The Disclosing Party\] AND \[The Receiving Party\]", con "Reference" e "1. Confidential Information and Materials"); un laptop con "CYBER INSURANCE"; un pulsante "Terms & Conditions"; la mappa d'Europa con stelle e lucchetto "GDPR – General Data Protection Regulation".
Ne fa parte tutto ciò che si firma o si vista: accordi di riservatezza, di non concorrenza, termini e condizioni d'uso, contratti di fornitura di servizi e di acquisto di beni, il GDPR stesso e altri regolamenti e leggi nazionali e internazionali.
**Assicurazioni cyber.** *CS-05 @ 01:45:05* Vanno di moda e sono solitamente molto costose, a seconda di massimali e coperture. Per una grande azienda possono coprire un attacco **ransomware** o **DoS** che produce un danno reputazionale non subito quantificabile, o rende i servizi indisponibili per un certo tempo mettendo l'azienda fuori mercato o esponendola a cause dei clienti. Nel ransomware, in teoria, rimborsano il riscatto. Ma molte compagnie preferiscono non coprire il ransomware, perché i riscatti possono essere talmente elevati da non essere assicurabili; altre lo fanno di mestiere ed è diventato un business. È un presidio amministrativo: se non riesco a coprire il rischio cyber con formazione, protezione tecnica, firewall, copro il **rischio residuo** con un'assicurazione.
### Integrazione Teams 2026 (lezione 4 2026)
*Capitolo 05, sezione 10 (Sicurezza amministrativa e assicurazioni cyber)*
- **Sicurezza amministrativa detta anche operativa.** Richiamo: "alcune volte vi ho detto si chiama sicurezza operativa". (Teams 4 @ 0:17:53)
- **Terms and conditions come firma elettronica semplice.** Nuovo: il docente critica i T&C scritti in un legalese volutamente verboso per scoraggiare la lettura (anche da parte di un giurista che non ha tempo) e spingere ad accettare in fretta; spuntare "accetto" è in molti casi giuridicamente vincolante e ha l'effetto di una firma elettronica semplice ("che vedremo"). I contratti possono rendere legittime multe, sanzioni, interruzione della fornitura, o la consegna dei dati personali alle forze dell'ordine su richiesta. (Teams 4 @ 0:18:08 - 0:19:51)
- **Limiti delle assicurazioni cyber.** Stesso concetto del 2025, con l'aggiunta che anche le assicurazioni "normali" (danni ai beni materiali, infortuni) sono misure di sicurezza amministrativa. (Teams 4 @ 0:20:22 - 0:21:16)
- **Esempio NDA: la formula della Coca-Cola.** Nuovo esempio: per vendere in un paese dove non ho stabilimenti, conviene dare in licenza la formula a uno stabilimento locale; un patto di riservatezza gli impedisce di rivenderla o usarla per altri scopi e consente di rivalersi legalmente. Cita anche i patti di non concorrenza. (Teams 4 @ 0:21:22 - 0:22:24)
## 11. Gestione del rischio
*CS-05 @ 01:46:44*
**Slide "The Triad of Risk".** Venn disegnato a mano con *Threat*, *Asset*, *Vulnerability*; l'intersezione, in rosso, è indicata come *Risk* da una mano che scrive.
Richiamo della lezione 2 ("la seconda lezione, se non sbaglio"): c'è rischio quando coesistono una **minaccia** (a sua volta la terna intento, capacità, opportunità), un **asset** dell'organizzazione e una **vulnerabilità** dell'asset esposta alla minaccia.
### Definizione di rischio
*CS-05 @ 01:47:15*
**Slide "Risk Management".** Venn *Threat*, *Vulnerability*, *Consequence* con *Risk* al centro. "Definition of Risk":
R ≝ (incident probability) × (expected loss)
Oltre alla definizione tripartita, il docente ne dà un'altra. Minaccia e vulnerabilità insieme danno la **probabilità** che l'incidente accada: la probabilità che la vulnerabilità venga sfruttata con successo dalla minaccia. Poi c'è la **conseguenza**, quantificabile in una perdita (di reputazione, economica, di materiale fisico, di personale).
Probabilità e perdita attesa non sono sempre quantificabili. Allora si fa un'**analisi qualitativa**, con etichette da basso ad alto, "da inconsistente a critico", e si stima il rischio come **prodotto** delle due. Perché un prodotto? Perché il rischio è rilevante sia quando la probabilità è molto alta e la perdita piccola (l'incidente può ripetersi molte volte, e perdite singole basse sommate danno un rischio elevato), sia quando la probabilità è piccolissima ma la perdita incalcolabile (un incidente reputazionale da cui l'organizzazione non si riprenderebbe mai). Per questo tutte le organizzazioni fanno una **valutazione del rischio** che si traduce in un'**analisi del rischio**: stimare nel modo più quantitativo possibile probabilità e perdite attese, moltiplicarle "esattamente come fossero numeri" quando sono numeriche, e distinguere ciò che è ad alto, medio e basso rischio.
**Slide "Risk Assessment"** (a schermo da 01:48:40, non commentata nel dettaglio). Un cono a quattro fasce con asse verticale *URGENCY* (*Potential Threat* in basso, *Imminent Threat* in alto): **NO EXPLOIT** – Risk: Low; **EXPLOITABLE** – Risk: Medium; **EXPLOITED** – Risk: High; **EXPOSED** – Risk: Critical.
**Slide "Risk Analysis"** (a schermo da 01:50:11). A sinistra un grafico: in ascissa *Probability \[% /year\]* da 0 a 100, in ordinata *Expected Loss \[\$\]*; una curva decrescente parte dall'"Accounting value of the company" e scende verso 0; annotazioni "Last year's losses", "\$ per year", "Probability of discontinuation of the company per year". A destra una matrice con assi *Low/High Level of Threat* e *Low/High Level of Vulnerability*: quadranti *Low Risk*, *Medium Risk*, *Medium Risk*, *High Risk* (in alto a destra, più rosso).
### Soglia di tolleranza e trattamento
*CS-05 @ 01:50:47*
**Slide "Risk Profile Map".** Matrice con righe "Probability of an event taking place" e colonne "Impact of Event":
<table header-row="true">
<tr>
<td></td>
<td>Marginal</td>
<td>Significant</td>
<td>Critical</td>
<td>Catastrophic</td>
</tr>
<tr>
<td>Very High</td>
<td>6</td>
<td>10</td>
<td>15</td>
<td>20</td>
</tr>
<tr>
<td>High</td>
<td>8</td>
<td>8</td>
<td>12</td>
<td>16</td>
</tr>
<tr>
<td>Occasional</td>
<td>3</td>
<td>6</td>
<td>9</td>
<td>12</td>
</tr>
<tr>
<td>Very Low</td>
<td>2</td>
<td>4</td>
<td>10</td>
<td>8</td>
</tr>
<tr>
<td>Improbable</td>
<td>1</td>
<td>2</td>
<td>4</td>
<td>7</td>
</tr>
</table>
Colori: rosso per 10, 15, 20 (Very High), 12, 16 (High), 12 (Occasional/Catastrophic); giallo per 6 (Very High/Marginal), 8 (High/Significant), 6 e 9 (Occasional), 10 e 8 (Very Low/Critical e Catastrophic); verde per gli altri. Una linea nera a scalini separa le celle rosse, sotto il richiamo "Proactive measures needed BEFORE the events take place". Un riquadro azzurro: "The organization's Risk Tolerance Line: *Every organization has a different tolerance for risk.*" In basso a destra una "RISK ASSESSMENT MATRIX" (*SEVERITY*: Catastrophic (1), Critical (2), Marginal (3), Negligible (4); *PROBABILITY*: Frequent (A), Probable (B), Occasional (C), Remote (D), Improbable (E), Eliminated (F)):
<table header-row="true">
<tr>
<td></td>
<td>Catastrophic</td>
<td>Critical</td>
<td>Marginal</td>
<td>Negligible</td>
</tr>
<tr>
<td>Frequent (A)</td>
<td>High</td>
<td>High</td>
<td>Serious</td>
<td>Medium</td>
</tr>
<tr>
<td>Probable (B)</td>
<td>High</td>
<td>High</td>
<td>Serious</td>
<td>Medium</td>
</tr>
<tr>
<td>Occasional (C)</td>
<td>High</td>
<td>Serious</td>
<td>Medium</td>
<td>Low</td>
</tr>
<tr>
<td>Remote (D)</td>
<td>Serious</td>
<td>Medium</td>
<td>Medium</td>
<td>Low</td>
</tr>
<tr>
<td>Improbable (E)</td>
<td>Medium</td>
<td>Medium</td>
<td>Medium</td>
<td>Low</td>
</tr>
<tr>
<td>Eliminated (F)</td>
<td>Eliminated</td>
<td></td>
<td></td>
<td></td>
</tr>
</table>
L'organizzazione traccia una **linea di tolleranza**: ciò che sta sopra (qui la diagonale nera, che coincide "quasi completamente con ciò che è di rischio alto, ma non del tutto") va **trattato**; ciò che sta sotto viene **accettato**. Sotto la linea non significa rischio basso o nullo: può essere un rischio medio che si decide di non trattare subito. Il trattamento, nella sicurezza informatica, consiste nel migliorare i presidi fisici, logici e amministrativi per abbassare il rischio. Poi l'analisi si **ripete** a valle dei nuovi controlli: ci si aspetta che i valori siano tutti o quasi diminuiti (anche in un'analisi qualitativa: da altissimo ad alto, da alto a medio, da medio a basso), si ritraccia la linea e, se tutto il rischio è sotto, il rischio è "eliminato": non azzerato, ma portato sotto la **soglia di accettazione**. Ciò che resta sopra va trattato ancora: è abbassato ma non del tutto trattato.
> **Nota aggiunta (verifica numerica):** se la mappa fosse il prodotto di un indice di probabilità (Improbable = 1 … Very High = 5) e di impatto (Marginal = 1 … Catastrophic = 4), cinque celle non tornerebbero: Very High/Marginal 6 invece di 5, High/Marginal 8 invece di 4, Very Low/Critical 10 invece di 6, Improbable/Critical 4 invece di 3, Improbable/Catastrophic 7 invece di 4. La slide non dichiara la scala usata, quindi potrebbe essere una mappa illustrativa, ma è proprio da queste incongruenze che nasce l'osservazione del docente sulla linea che "non coincide del tutto" con il rischio alto (il 10 di Very Low/Critical resta sotto la linea, il 10 di Very High/Significant sopra). Dettagli nel file divergenze.
### Trasferimento del rischio e ciclicità
*CS-05 @ 01:52:22*
Le **assicurazioni cyber** sono il tipico esempio di **trasferimento del rischio**. Decido di non poter trattare il rischio ransomware e pago un'azienda che, a fronte di un corrispettivo, mi paga un premio se ne sono vittima. La perdita economica dovuta al ransomware diventa un rischio dell'assicuratore, che "se lo accolla" letteralmente: l'attacco che colpirà me impatterà sulle sue finanze. Ma non è detto che il rimborso copra tutto, né che copra la perdita **reputazionale**. Per questo le assicurazioni cyber, che esistono per quasi tutti i rischi informatici, difficilmente coprono minacce globali come la **guerra cibernetica**, il ransomware e in alcuni casi i DoS: le perdite potenziali sono così elevate che le compagnie tendono a non offrirle.
> **Nota aggiunta:** nel lessico assicurativo il *premio* è ciò che l'assicurato paga alla compagnia, mentre ciò che la compagnia paga in caso di sinistro è l'*indennizzo*. Il docente si corregge a metà frase ("tramite pagamento di un premio, scusate, tramite pagamento di un corrispettivo… a me un premio") e finisce per chiamare "premio" l'indennizzo.
Il rischio va trattato **periodicamente**: analizzare, mettere presidi, rianalizzare non si fa una volta sola. L'analisi del rischio è un **processo circolare** continuo.
### Integrazione Teams 2026 (lezione 4 2026)
*Capitolo 05, sezione 11 (Gestione del rischio)*
- **Categorie di rischio.** Il rischio informatico ha varie sottocategorie: rischio cyber, rischio operativo, rischio operativo informatico (non approfondite). (Teams 4 @ 0:22:47)
- **Stima della perdita "come se l'evento fosse certo".** La perdita attesa è la perdita che si realizzerebbe qualora l'evento si verificasse con certezza; la probabilità si può misurare con la statistica se disponibile, la perdita si può stimare con precisione per esempio dal processo industriale (fermo produzione, prodotto perso). (Teams 4 @ 0:23:34 - 0:24:35)
- **Esempio dell'alieno.** Nuovo caso limite per la probabilità trascurabile: un alieno che atterra e diffonde una cultura per cui i clienti smettono di comprare i miei prodotti ha perdita gravissima (andrei fuori mercato) ma probabilità così bassa che il rischio è bassissimo. (Teams 4 @ 0:26:07)
- **Scale qualitative.** Esistono schemi a 3 etichette (basso, medio, elevato) e a 5 (molto basso, basso, medio, alto, critico); il valore dell'analisi è dare ai decisori un criterio oggettivo, replicato su tutti i rischi aziendali, non solo cyber. (Teams 4 @ 0:27:06)
- **Trattamento per colori e rischio residuo.** Formulazione nuova e più operativa: i rischi verdi si accettano, gli arancioni o rossi si trattano; dopo il trattamento si ricalcola il **rischio residuo**, che dovrebbe essere sempre inferiore all'originario; un residuo ancora rosso va trattato ancora aggiungendo presidi finché scende almeno ad arancione, da cui si può accettare, anche se un arancione conviene trattarlo ancora fino al verde. (Teams 4 @ 0:27:59 - 0:29:23)
- **Trasferimento del rischio.** Definizione esplicita: la responsabilità viene demandata a un altro soggetto, che può essere un'altra funzione dell'organizzazione o un terzo; l'esempio più semplice resta l'assicurazione. Precisazione: il trattamento del rischio non è finalizzato al trasferimento ma all'annullamento; quando non è possibile si accetta il residuo, lo si trasferisce o si continua a trattarlo. (Teams 4 @ 0:29:27 - 0:30:35)
- **Ripetizione periodica.** Stesso principio del 2025, con la motivazione esplicita: rischi prima accettati possono non esserlo più, e rischi prima non trattati perché accettabili possono richiedere trattamento. (Teams 4 @ 0:30:35 - 0:31:25)
## 12. Business Continuity Plan e Disaster Recovery Plan
### Business Continuity Plan
*CS-05 @ 01:55:07*
**Slide "Business Continuity Plan (BCP)".** A sinistra un riquadro "Potential threats to continuous supply" circondato da icone con frecce: *Storm damage*, *Theft*, *Power loss*, *Viral outbreak*, *Mechanical failure*, *Water supply interruption*, *Fire*, *Human error*, *Cyber attack*, *Natural disaster*. A destra un ciclo attorno a "Piano Business Continuity": *Analisi dell'impatto sul business* → *Analisi dei rischi* → *Gestione della crisi* → *Risposta di Emergenza* → *Comunicazione della Crisi* → *Recupero del disastro* → di nuovo *Analisi dell'impatto sul business*.
Riguarda le operazioni del **core business** (se si parla di core business si parla di un'azienda privata che fa profitti) e, nella *operational continuity*, anche i **compiti istituzionali** di un soggetto pubblico. Sono gli aspetti su cui l'azienda fa soldi e resta in piedi, o su cui lavora la PA: se fossero compromessi, sarebbe a rischio l'esistenza stessa dell'organizzazione. Il presidio amministrativo è scrivere un **piano di continuità operativa (BCP)** che individua compiti principali, asset principali, tutti i possibili rischi e come comportarsi perché la continuità non si interrompa, o non troppo a lungo.
Contiene misure di **business**: ricorso a un fornitore di posta diverso, a un certo tipo di assicurazione, a un'altra compagnia aerea, attivazione di nuove linee di credito bancarie. Non è un piano solo contro gli attacchi cyber: gli attacchi cyber vi sono stati integrati regolarmente solo da pochi anni, perché le cause di interruzione del core business riguardano anche altre sfere. Business e compiti sono un **unicum**: il piano deve essere **unico e omnicomprensivo**, non uno per il cyber e uno "fisico" per incendi, alluvioni, tornado e terremoti. È scritto in **linguaggio di business**, per i vertici e al massimo i top manager.
### Disaster Recovery Plan
*CS-05 @ 01:57:47*
**Slide "Disaster Recovery Plan (DRP)".** A sinistra un grafico *COST* con al centro "Disaster" sull'asse dei tempi: a sinistra **RPO (Recovery Point Objective)** su scala "months, weeks, days, hours, seconds", con "Backup RPO \> 0" (verde, costo più basso) e "Backup RPO = 0" (rosso, costo più alto); a destra **RTO (Recovery Time Objective)** su scala "seconds, hours, days, weeks, months", con *DR Site*: "Hot Site" (costo alto), "Warm Site", "Cold Site" (costo basso). In alto a destra un globo collegato a *CLOUD DISASTER RECOVERY*, *DISASTER RECOVERY ON-PREMISE*, *DISASTER RECOVERY AS A SERVICE*. In basso la tabella "Cold, Warm and Hot Disaster Recovery Models":
<table header-row="true">
<tr>
<td></td>
<td>Cold Site</td>
<td>Warm Site</td>
<td>Hot Site</td>
</tr>
<tr>
<td>Secondary Location</td>
<td>sì</td>
<td>sì</td>
<td>sì</td>
</tr>
<tr>
<td>Equipment at Location</td>
<td>no</td>
<td>sì</td>
<td>sì</td>
</tr>
<tr>
<td>Connectivity at Location</td>
<td>no</td>
<td>sì</td>
<td>sì</td>
</tr>
<tr>
<td>Active before Failover</td>
<td>no</td>
<td>no</td>
<td>sì</td>
</tr>
<tr>
<td>Outage Measured in</td>
<td>WEEKS</td>
<td>DAYS/HOURS</td>
<td>HOURS/MINUTES</td>
</tr>
</table>
Il **piano di recupero dai disastri** è spesso un'appendice del BCP o parte del suo corpo documentale, ma è un documento di tipo diverso. Si concentra solo sui **disastri**, eventi *disruptive* per l'organizzazione, e soprattutto è un **piano pratico**: fino a qualche anno fa andava solitamente stampato e messo bene in vista dove chi deve attuarlo possa trovarlo e consultarlo rapidamente. Contiene l'elenco delle persone da chiamare, in che ordine, con i numeri di telefono principali e personali.
Può attuarlo anche il singolo dipendente del "reparto bulloni" se c'è un incendio o un terremoto e le macchine cadono a terra; oppure in un disastro cyber: un ransomware ha cifrato i dati di tutti i server, non funzionano computer né cellulari, non si inviano né ricevono email. Chi chiamo? Nel DRP ci sono i numeri d'emergenza, a volte anche quello di casa dell'amministratore delegato, che chiunque può chiamare da un telefono fisso, "perché ogni minuto conta, ogni singolo secondo può contare". E la catena: chiamo il mio capo; se non risponde, aspetto un minuto e chiamo il suo capo; se non risponde, chiamo l'amministratore delegato. Il docente riconosce che è un esempio estremo, ma vero: a volte il DRP è stampato, in bella vista o in un armadio, e i quadri preposti alle funzioni da recuperare ne hanno una copia cartacea da consultare se i computer smettono di funzionare.
> **Nota aggiunta:** il docente non commenta il grafico. L'**RPO** è la quantità massima di dati, espressa in tempo, che si accetta di perdere (quanto indietro nel tempo si torna con il ripristino); l'**RTO** è il tempo massimo entro cui il servizio deve tornare operativo. Ridurli verso zero (backup continui, hot site) costa di più.
**Slide "BCP vs DRP in practice"** (a schermo da 02:00:46, ultima slide: "con questa slide direi che ho concluso"). Una *Control Matrix* con controlli *Directive, Detective, Deterrent, Preventive, Corrective* (giallo), *Restorative* (rosso), *Compensating*, declinati in *Administrative*, *Technical/Logical*, *Physical*. Flusso: *Initial event* → *Investigate and determine impact*. Tre esiti verso un *Incident Resolution Plan* (verde) con un'*Escalation path*: "Critical business functions are not impacted." (resta nel piano di risoluzione degli incidenti); "Critical business functions are impacted but business still continues." → **BCP**, "We have controls that correct the situation." (collegato ai controlli *Corrective*); "Critical business functions have stopped." → **DRP** (con *RPO, RTO, MTD*), "We have controls to restore operation." (collegato ai controlli *Restorative*).
### Integrazione Teams 2026 (lezione 4 2026)
*Capitolo 05, sezione 12 (BCP e DRP)*
- **BCP più ampio del cyber.** Il 2026 elenca rischi non cyber coperti dal BCP: cambiamenti del mercato, del sentiment, del valore di azioni in cui l'azienda ha investito, aumento improvviso del costo delle materie prime. Un BCP può anche non includere minacce cyber. (Teams 4 @ 0:31:50 - 0:32:51)
- **DRP da conoscere a memoria.** Il DRP è procedurale; chi vi figura dovrebbe conoscerne a memoria la parte che gli compete, perché eventi come alluvione, ransomware o attacco aereo improvviso lasciano le persone "basite". Contiene una catena di comando d'emergenza diversa da quella ordinaria, con pochi passaggi (1, 2 o 3) prima di chiamare l'amministratore delegato. (Teams 4 @ 0:33:06 - 0:34:27)
- **Esempio numerico RTO/RPO.** Nuovo e utile per l'esame: azienda con sede vicino a un corso d'acqua (per l'idroelettrico) esposta ad alluvioni; il BCP prevede un secondo data center "freddo", magari in affitto presso un altro cloud provider, sincronizzato una volta a settimana. **RPO = 1 settimana**, **RTO = 7 minuti**: dopo 7 minuti dal riconoscimento dell'alluvione l'azienda torna operativa, ma con i dati della settimana prima (mancano email, fatture, preventivi dell'ultima settimana). Il DRP contiene le procedure (evacuazione del sito primario, attivazione del passaggio al secondo sito, da cui partono i 7 minuti); il BCP contiene la strategia. Nel 2025 RPO e RTO erano solo in una nota aggiunta. (Teams 4 @ 0:34:44 - 0:36:59)
## 13. Domande finali degli studenti
*CS-05 @ 02:00:47*
**Esame, lezione di domani, bibliografia.** Riportato per intero nella sezione 16.
### Conviene una VPN sul PC personale?
*CS-05 @ 02:02:39*
Una studentessa chiede se convenga usare una VPN sul PC personale anche su siti indicizzati, per proteggere i dati trasmessi. Il docente: "questa domanda me la fanno da dieci anni, quasi a ogni edizione". Come per ogni presidio, bisogna sapere **da cosa protegge**, altrimenti ci si complica la vita accendendo e spegnendo una VPN a ogni navigazione. I veri servizi VPN **non sono gratis** (qualcuno paga infrastruttura ed energia per farvi viaggiare cifrati nella sua rete); c'è un **onere operativo** (usare sempre un software) e la connessione è sempre un po' più lenta, soprattutto con i servizi economici, che a volte hanno limiti oltre i quali non si naviga.
Nell'uso quotidiano il docente la consiglia **solo su reti che non controlliamo**: fuori casa, oppure su una rete domestica di cui non ci si fida perché condivisa da tutto il palazzo; certamente su reti di alberghi e luoghi pubblici (Starbucks, aeroporti, treni). Lì chiunque sia sulla stessa rete può fare **hopping** sul nostro dispositivo o spiare il traffico prima che esca su Internet; se si naviga su siti **HTTP e non HTTPS** il traffico è in chiaro e chiunque legge dove andiamo e cosa scambiamo, la posta per esempio. Dove non c'è una crittografia che controlliamo o di cui ci fidiamo, la VPN è una buona alternativa. Se si usa già la VPN del lavoro, non ha senso aggiungerne un'altra, "se ci fidiamo del nostro datore di lavoro, ovviamente. È una provocazione".
**E il router di casa?** *CS-05 @ 02:06:39* Molti usano la configurazione semplice del router: **password di default** del Wi-Fi e **WPS** (premendo il tasto il dispositivo vicino entra in rete). Sono comodità, ma se lo faccio io lo può fare anche un attore della minaccia; e per alcune password di default si trovano online programmini che le calcolano dal nome della rete. Cambiare le configurazioni di default è una buona idea. Alcuni spengono il Wi-Fi del router del provider e ne comprano uno proprio, ma "la coperta è corta": ci si fa carico di tutta la messa in sicurezza, cosa buona se la si sa fare; altrimenti il gestore che si paga ogni mese potrebbe saperne "due spicci" più di noi. Viceversa il Wi-Fi di un albergo, di una caffetteria o di un aeroporto è spesso gestito in automatico da chi non ha presidi professionali per migliaia di utenti nei terminal: quel Wi-Fi pubblico che non costa nulla rischia di essere poco protetto.
### Accesso ai servizi universitari da fuori UE e NAS domestico
*CS-05 @ 02:09:30*
Una studentessa racconta che, da fuori Unione Europea, per accedere a Teams e alla posta di Roma Tre serve un'app di autenticazione (un Authenticator, secondo fattore) mentre un altro servizio di lavoro blocca il login se l'IP non è europeo. Come soluzione ha configurato una VPN sul **NAS** di casa a Roma, ma non è stabile: se lì cade Internet durante una riunione, resta scollegata senza poter avvisare. Chiede se si possa fare altrimenti, per esempio configurando il router o un secondo punto in un'altra casa fuori UE (i due punti non devono comunicare fra loro). Il docente, che non conosceva il primo meccanismo, le chiede di mandarglielo in chat anche alla lezione successiva.
Risposta, "andando a naso": i router offrono l'**aggiornamento automatico del DNS**, che permette di pubblicare l'indirizzo interno su un indirizzo esterno raggiungibile; uno dei problemi probabili è che il router sia dietro l'indirizzamento del provider, che scherma le connessioni in ingresso in parte per risparmiare e in parte per proteggere la clientela. In generale la connessione da casa, dentro o fuori UE, **non è affidabile** per cose critiche come una videochiamata: anche se la linea non cade, la **banda** non è garantita. I provider vendono magari "20 giga" come massimo, non come minimo; una banda minima garantita (per esempio un gigabit fisso) è un servizio business a pagamento. Il video in tempo reale richiede un flusso minimo, quindi il problema è probabilmente la banda più che la caduta. Il consiglio "da tecnico": usare un **servizio in cloud**, una piccola macchina virtuale in un data center raggiungibile da Internet, eventualmente localizzata sia dentro sia fuori UE, pagata in base a dove deve essere disponibile; probabilmente esistono anche soluzioni SaaS chiavi in mano che non richiedono competenze sistemistiche. Per chi è "smanettona" c'è la VM Linux configurata da sé, ma allora la messa in sicurezza della macchina esposta su Internet diventa critica, perché può diventare un punto d'ingresso.
Il docente chiude dicendo che di solito non dà consigli di questo tipo, ma la domanda permetteva di "mettere a terra" cose astratte delle ultime lezioni. La registrazione termina a *CS-05 @ 02:18:48*.
---
## 14. Glossario
<table header-row="true">
<tr>
<td>Termine</td>
<td>Significato nella lezione</td>
</tr>
<tr>
<td>QRishing</td>
<td>Phishing che veicola il link in un QR code, invisibile ai filtri testuali</td>
</tr>
<tr>
<td>Mail gateway</td>
<td>Sistema che riceve e filtra la posta in arrivo per l'organizzazione</td>
</tr>
<tr>
<td>Pretesto</td>
<td>Leva narrativa del phishing (sanzione, pagamento, gruppo di lavoro)</td>
</tr>
<tr>
<td>Indicatore di compromissione</td>
<td>Elemento che suggerisce, senza provarla, la natura malevola</td>
</tr>
<tr>
<td>Caratteri sostitutivi</td>
<td>Caratteri Unicode simili a lettere latine usati per eludere i filtri</td>
</tr>
<tr>
<td>Typosquatting</td>
<td>Sostituire una parola o un dominio con uno simile per ingannare</td>
</tr>
<tr>
<td>Spear phishing</td>
<td>Phishing mirato su un'organizzazione o una persona</td>
</tr>
<tr>
<td>IDS / IPS</td>
<td>Intrusion Detection / Prevention System</td>
</tr>
<tr>
<td>SIEM</td>
<td>Security Information and Event Management</td>
</tr>
<tr>
<td>VPN</td>
<td>Rete privata virtuale: tunnel cifrato fra punti su rete pubblica</td>
</tr>
<tr>
<td>Geo-masking</td>
<td>Uso della VPN per mascherare la provenienza geografica</td>
</tr>
<tr>
<td>Surface / deep / dark web</td>
<td>Web indicizzato / dietro autenticazione / su reti overlay cifrate</td>
</tr>
<tr>
<td>Tor</td>
<td>The Onion Router: rete con nodi guard, relay, exit e cifratura a strati</td>
</tr>
<tr>
<td>Freenet (Hyphanet), I2P</td>
<td>Altre reti del dark web: anti-censura / tunnel cifrati unidirezionali</td>
</tr>
<tr>
<td>Cavallo di Troia</td>
<td>Codice malevolo inserito in software o pagine benigne</td>
</tr>
<tr>
<td>Analisi delle firme</td>
<td>Ricerca di stringhe note nel binario (antivirus tradizionali)</td>
</tr>
<tr>
<td>Reverse engineering</td>
<td>Decompilazione e analisi del software per risalire al funzionamento</td>
</tr>
<tr>
<td>DevSecOps</td>
<td>Sicurezza integrata in tutto il ciclo DEV (plan, code, build, test) e OPS</td>
</tr>
<tr>
<td>OWASP Top 10</td>
<td>Elenco periodico delle 10 minacce più comuni al software</td>
</tr>
<tr>
<td>CVE</td>
<td>Common Vulnerabilities and Exposures, database pubblico con ID CVE-anno-numero</td>
</tr>
<tr>
<td>CVSS</td>
<td>Punteggio di severità delle vulnerabilità, da 0 a 10</td>
</tr>
<tr>
<td>Responsible disclosure</td>
<td>Segnalazione al produttore prima della pubblicazione (di solito 90 giorni)</td>
</tr>
<tr>
<td>Proof of concept</td>
<td>Software che dimostra in modo replicabile lo sfruttamento</td>
</tr>
<tr>
<td>Bounty hunter</td>
<td>Chi cerca vulnerabilità per ricompensa</td>
</tr>
<tr>
<td>CSP</td>
<td>Cloud service provider</td>
</tr>
<tr>
<td>CapEx / OpEx</td>
<td>Spese in conto capitale / spese operative</td>
</tr>
<tr>
<td>Edge computing, IoT hub</td>
<td>Dispositivi periferici che producono dati e il nodo che li collega al cloud</td>
</tr>
<tr>
<td>VM / hypervisor</td>
<td>Macchina virtuale / software che emula l'hardware per le VM</td>
</tr>
<tr>
<td>Container</td>
<td>Ambiente isolato che condivide il kernel dell'host</td>
</tr>
<tr>
<td>IaaS / PaaS / SaaS</td>
<td>Infrastruttura / piattaforma / software come servizio</td>
</tr>
<tr>
<td>Hopping</td>
<td>Salto da una VM, container o VLAN a un'altra</td>
</tr>
<tr>
<td>Blue-pill effect</td>
<td>Uscita dai confini virtuali di una VM/container</td>
</tr>
<tr>
<td>Regione, multiregione, AZ</td>
<td>Livelli geografici e di disponibilità dei data center di un CSP</td>
</tr>
<tr>
<td>Sovranità / localizzazione / co-location</td>
<td>Legge del luogo dei dati / obbligo di tenerli nel paese / repliche geografiche</td>
</tr>
<tr>
<td>Data space</td>
<td>Infrastruttura decentralizzata di condivisione dati (provider, consumer, broker, clearing house, identity provider)</td>
</tr>
<tr>
<td>Data Governance Act</td>
<td>Reg. (UE) 2022/868; introduce consent, permission, data user</td>
</tr>
<tr>
<td>Dato ordinario / critico / strategico</td>
<td>Classificazione ACN dei dati della PA; gli strategici solo in Italia</td>
</tr>
<tr>
<td>Owner, steward, custodian, processor</td>
<td>Ruoli della data governance</td>
</tr>
<tr>
<td>Titolare / responsabile del trattamento</td>
<td>Data controller / data processor (GDPR)</td>
</tr>
<tr>
<td>DPO</td>
<td>Data protection officer (RPD)</td>
</tr>
<tr>
<td>GPDP</td>
<td>Garante per la protezione dei dati personali</td>
</tr>
<tr>
<td>Assicurazione cyber</td>
<td>Presidio amministrativo che trasferisce il rischio residuo</td>
</tr>
<tr>
<td>Rischio</td>
<td>Probabilità dell'incidente × perdita attesa</td>
</tr>
<tr>
<td>Linea di tolleranza</td>
<td>Soglia oltre la quale il rischio va trattato</td>
</tr>
<tr>
<td>Trasferimento del rischio</td>
<td>Spostare la perdita su un terzo (assicurazione)</td>
</tr>
<tr>
<td>BCP</td>
<td>Business Continuity Plan: piano unico di continuità, in linguaggio di business</td>
</tr>
<tr>
<td>DRP</td>
<td>Disaster Recovery Plan: piano pratico di recupero, con catena di chiamate</td>
</tr>
<tr>
<td>RPO / RTO</td>
<td>Recovery Point / Recovery Time Objective</td>
</tr>
<tr>
<td>Cold / warm / hot site</td>
<td>Siti di DR con crescente prontezza e costo</td>
</tr>
<tr>
<td>WPS</td>
<td>Configurazione Wi-Fi a pulsante</td>
</tr>
</table>
## 15. Punti incerti
- \[?\] *CS-05 @ 00:22:48*: "i dati che nel portatile del dipendente X che sta a casa sua, vigevano con il laptop… entrano… nel gay nel ghetto e di una delle ditte aziendali". Ricostruito come "gateway di una delle sedi aziendali"; "vigevano" non ricostruibile (forse "a Vigevano").
- \[?\] *CS-05 @ 00:32:27*: "e quindi in realtà hanno ancora un nodo di uscita": contraddice la frase precedente (i servizi interni a Tor non richiedono un nodo di uscita). Possibile "non hanno".
- \[?\] *CS-05 @ 00:35:09*: "è molto transciando": parola non ricostruibile.
- \[?\] *CS-05 @ 00:41:46*: "l'ha decompilata… e alla fine l'ha decompilata": la seconda occorrenza è forse "ricompilata" o "modificata".
- \[?\] *CS-05 @ 00:45:28*: "l'Europa si doterà di un sistema analogo proprio di cui è responsabile il titolare": non è chiaro chi sia il "titolare" (forse ENISA).
- \[?\] *CS-05 @ 00:46:33*: "ogni CVE riguarda tipicamente un prodotto software \[...\] di prodotti fisici": manca un pezzo di frase.
- \[?\] *CS-05 @ 01:03:53*: "la versione del kernel 2627508602": numero non ricostruibile.
- \[?\] *CS-05 @ 01:13:58*: "a quella fisica che va all'interno della singola macchina virtuale nel singolo rack": ordine dei livelli poco chiaro nel parlato.
- \[?\] *CS-05 @ 01:25:49*: "e poi c'è una categoria terza dal titolare e dall'interessato, il dato, i quali…": ricostruito come il *data user* della slide.
- \[?\] *CS-05 @ 02:01:38*: "di solito alla fine del corso, alla fine della seconda lezione": non è chiaro a quale "seconda lezione" si riferisca.
- \[?\] *CS-05 @ 02:13:41*: "pubblicare il suo indirizzo interno su un indirizzo esterno al suo gestore di interrompo": fine frase non ricostruibile.
- *CS-05 @ 02:05:26*: "tutte le volte che siamo in VPN di alberghi" e *@ 02:04:55* "non è la VPN in casa mia ma è la VPN del palazzo": dal contesto il docente intende "rete", non "VPN". Lapsus.
- *CS-05 @ 01:33:55*: "tutti quei casi in cui il titolare deve esercitare i propri diritti": dal contesto è l'**interessato**. Lapsus.
- *CS-05 @ 00:10:46*: la dimensione della "e" di "dedicato" e la sua identità con "℮" non sono verificabili dal fotogramma (testo troppo piccolo).
- Heat map [tenable.sc](http://tenable.sc) (*CS-05 @ 00:50:41*): molti valori \[illeggibile\].
- Trascrizione automatica corretta nel testo: "Fonder Line" = von der Leyen; "type of quoting" = typosquatting; "spare phishing" = spear phishing; "IBS" = IPS; "geografici egiziani" = geroglifici; "parquet generale" = quartier generale; "ghetto" / "gay nel ghetto" = gateway; "monitoria" = monitoraggio; "TOTR", "rete d'or" = Tor; "radicandole" = sradicandole; "a COPS" = DevSecOps; "CV", "Common Vulnerability Exposure" = CVE; "REC" = rack; "appicciato" = patchato; "per terra, male, cero e spazio" = terra, mare, cielo e spazio; "Agid" = AgID; "BGP" = BCP; "nasda", "massa" = NAS; "honore" = onere; "direttografia" = crittografia; "Pago PA", "pagopiare" = pagoPA; "Si in vita" = si invita; "ESSER"/"SER VIZIO" = "SER V IZIO" in slide.
## 16. Esame
Menzioni esplicite dell'esame in questa lezione:
- *CS-05 @ 01:25:49*: parlando del **Data Governance Act**: "non vi preoccupate perché **non sarà comunque oggetto di nessun tipo di esame**; se siete interessati vi ho dato i riferimenti del regolamento". Aggiunge che per chi si occuperà di dati nel settore pubblico in Europa è un argomento da conoscere almeno in parte.
- *CS-05 @ 02:00:47 – 02:03:04*: uno studente, arrivato con dieci minuti di ritardo, chiede se all'inizio sia stato detto qualcosa sull'esame. Il docente: "**No, non è stato detto nulla sull'esame.** Ho solo accennato oggi che non ci sarà nulla che riguarda il Data Governance Act. Non volevo spaventarvi con la slide sulle partizioni del regolamento."
	- **Lezione di domani.** Nello stesso scambio lo studente chiede conferma che **domani (23/09/2025) la lezione non ci sarà**; lo scambio si chiude con "Ok, perfetto" (non è chiaro dall'audio chi lo pronunci, ma la conferma è data per acquisita). È coerente con la sequenza delle registrazioni: la lezione successiva, CS-06, è del 25/09/2025.
	- **Riferimenti bibliografici.** Alla domanda su libri e articoli per approfondire, anche dopo il corso, il docente risponde che di solito dà i riferimenti alla fine del corso \[?\] ("alla fine della seconda lezione"), e che mostrerà la stessa slide anche alla fine di questo corso; ci saranno anche riferimenti sulla **crittografia**, argomento "intermedio" fra questo corso e l'altro, ma trattato prevalentemente nell'altro. Sono riferimenti esterni: ogni anno cerca libri di testo esaustivi, possibilmente in italiano, che coprano tutti gli argomenti, e non li trova ("sto pensando di scriverne uno io, ma il tempo non lo trovo mai"). I testi trattano la materia da punti di vista differenti e vanno considerati **solo ed esclusivamente per l'approfondimento**.
	- **Cosa fa fede.** "Quindi **fa fede solamente quello che vi dico nelle lezioni per il, tra virgolette, esame**, come ve lo dico io, ovviamente. Perché altrimenti si rischia che ci siano definizioni differenti, punti di vista differenti: purtroppo è una materia talmente vasta e interdisciplinare che il rischio c'è."
Indicazioni utili per lo studio, senza valore di esclusione: il docente dice di non trattare in dettaglio i presidi tecnici di rete (IDS/IPS, SIEM, proxy: "rilevanti per chi di mestiere si occupa di sicurezza informatica"), la malware analysis e la differenza tecnica fra VM e container (tranne l'aspetto di sicurezza); insiste invece su ciò che vuole "vi portiate a casa": la classificazione dei dati della PA in ordinario, critico e strategico, con i soli strategici obbligatoriamente in Italia.
Ricordare, per le definizioni, che fa fede la lezione: dove nel manuale compaiono riquadri **Correzione** (Unicode, CVE, ambito del GDPR, obbligo del DPO, Spotify, Microsoft/Cupertino), la versione del docente è quella detta in aula; la correzione serve a non portare all'esterno un'informazione imprecisa.
