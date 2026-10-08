# Divergenze

> Fonte Notion: https://app.notion.com/p/3e712abc808d81b5a5f1e5fb5fe1b87c — ultima modifica 2026-09-27T11:05:44.187Z

La pagina raccoglie le divergenze di tutte le lezioni: parlato contro slide, affermazioni del docente contro fonti esterne note, e l'affidabilità della trascrizione. Nei capitoli le stesse voci sono segnalate con i riquadri **Correzione** e **Nota aggiunta**.
# Lezione 2
**Registrazione:** CS-02, Teams del 16/09/2025, 01:30:17
**Fonti di confronto:** nessun materiale del docente. Le divergenze sono fra parlato e slide a schermo, e fra lezione e fonti esterne note (segnalate come tali).
### Mappatura dei file del portale (vale per tutto il corso)
<table header-row="true">
<tr>
<td>File portale</td>
<td>Data a schermo</td>
<td>Contenuto reale</td>
</tr>
<tr>
<td>`lezione_1-1.mp4` (pagina "lezione 1")</td>
<td>26/09/2025 16:15</td>
<td>**Non è la lezione 1**: stesso contenuto di `lezione_8.mp4`</td>
</tr>
<tr>
<td>`lezione_2.mp4`</td>
<td>16/09/2025</td>
<td>Lezione 2 (cita "ieri" = lezione 1 del 15/09, mancante)</td>
</tr>
<tr>
<td>`lezione_3.mp4`</td>
<td>18/09/2025</td>
<td>Lezione 3</td>
</tr>
<tr>
<td>`lezione_4.mp4`</td>
<td>19/09/2025</td>
<td>Lezione 4</td>
</tr>
<tr>
<td>`lezione_5.mp4`</td>
<td>22/09/2025</td>
<td>Lezione 5</td>
</tr>
<tr>
<td>`lezione_6.mp4`</td>
<td>25/09/2025</td>
<td>Lezione 6</td>
</tr>
<tr>
<td>`lezione_7.mp4`</td>
<td>26/09/2025 16:08</td>
<td>Solo 105 s: inizio della lezione 7, interrotto per un problema di condivisione schermo</td>
</tr>
<tr>
<td>`lezione_8.mp4`</td>
<td>26/09/2025 16:15</td>
<td>Ripresa della lezione 7 dopo l'interruzione (TTP, MITRE ATT&CK)</td>
</tr>
</table>
Mancano quindi la **lezione 1 (15/09/2025)** e, se esiste, un'**ottava lezione** successiva al 26/09.
### Divergenze della lezione 2
<table header-row="true">
<tr>
<td>#</td>
<td>Dove</td>
<td>Tipo</td>
<td>Descrizione</td>
</tr>
<tr>
<td>1</td>
<td>CS-02 @ 00:19:16</td>
<td>Slide</td>
<td>Titolo "The Triad **or** Risk" invece di "of". Refuso.</td>
</tr>
<tr>
<td>2</td>
<td>CS-02 @ 00:59:13</td>
<td>Slide</td>
<td>"Hactivism" invece di "Hacktivism". Refuso.</td>
</tr>
<tr>
<td>3</td>
<td>CS-02 @ 00:51:42</td>
<td>Parlato vs CSF</td>
<td>Identify descritta come individuazione di una minaccia "che sta per avvenire o magari che sta avvenendo". Nel CSF 2.0 l'individuazione di eventi in corso è Detect; Identify è comprensione del rischio. Riquadro Correzione nel manuale.</td>
</tr>
<tr>
<td>4</td>
<td>CS-02 @ 00:58:44</td>
<td>Slide vs CSF ufficiale</td>
<td>Tabella con [ID.SC](http://ID.SC) e senza [GV.SC/GV.OV](http://GV.SC/GV.OV); nel CSF 2.0 definitivo la supply chain è [GV.SC](http://GV.SC) e c'è GV.OV (Oversight). Riportata com'è, con Nota aggiunta.</td>
</tr>
<tr>
<td>5</td>
<td>CS-02 @ 00:48:25</td>
<td>Incertezza del docente</td>
<td>Data del CSF 2.0 non ricordata ("l'anno scorso, no, due anni fa"). Pubblicato il 26/02/2024. Nota aggiunta.</td>
</tr>
<tr>
<td>6</td>
<td>CS-02 @ 01:19:45</td>
<td>Parlato vs norma</td>
<td>GDPR applicato in base alla **cittadinanza** europea e al riconoscimento del diritto UE da parte dello stato del titolare. L'art. 3 GDPR si basa sulla localizzazione dell'interessato nell'Unione. Il docente premette "non sono un giurista". Riquadro Correzione.</td>
</tr>
<tr>
<td>7</td>
<td>CS-02 @ 01:28:17</td>
<td>Esempio impreciso</td>
<td>"Chi controlla gli aggiornamenti di Windows? Una sola azienda" seguito dall'incidente CrowdStrike: l'incidente del 19/07/2024 fu un aggiornamento difettoso di CrowdStrike Falcon, non di Microsoft, e non un attacco. Nota aggiunta.</td>
</tr>
<tr>
<td>8</td>
<td>CS-02 @ 01:17:31</td>
<td>Lapsus</td>
<td>"non voglio essere vendor neutral": il senso è l'opposto.</td>
</tr>
</table>
Nessun esempio numerico né blocco di codice in questa lezione: nulla da verificare per esecuzione.
### Trascrizione: affidabilità
- `avg_logprob` su CS-02: minimo -0.295, mediana -0.105. La soglia -0.6 non segnala nulla; -0.3 nulla; -0.2 segnala 31 segmenti, quasi tutti parlato corretto. Anche la probabilità per parola (\< 0.25) segnala soprattutto parole a inizio frase.
- **Su questo corso nessuna delle due metriche discrimina**: l'audio è pulito e gli errori veri sono nomi propri e sigle trascritti con sicurezza (XIRT per CSIRT, Fonderlion, Fred Hector). La revisione utile si fa leggendo, e i punti sono elencati nella sezione 11 del manuale.
- Filtro boilerplate: 1 segmento scartato.
- Distribuzione `avg_logprob` sulle altre lezioni: quasi identica (mediana \~ -0.10/-0.11, minimo fra -0.24 e -0.49).
# Lezione 3
**Registrazione:** CS-03, Teams del 18/09/2025, circa 01:35:45
**Fonti di confronto:** nessun materiale del docente. Le divergenze sono fra parlato e slide a schermo, e fra lezione e fonti esterne note (segnalate come tali). Per la mappatura dei file del portale vedi `lezione-02-divergenze.md`.
### Divergenze della lezione 3
<table header-row="true">
<tr>
<td>#</td>
<td>Dove</td>
<td>Tipo</td>
<td>Descrizione</td>
</tr>
<tr>
<td>1</td>
<td>CS-03 @ 00:00:03 a 00:17:07</td>
<td>Registrazione</td>
<td>Slide non condivise per i primi 17 minuti: virus, trojan e parte del rootkit sono spiegati senza nulla a schermo. Le slide "Malware terminology – Virus" e "– Trojan" non hanno fotogramma né voce OCR.</td>
</tr>
<tr>
<td>2</td>
<td>CS-03 @ 00:00:40</td>
<td>Parlato</td>
<td>LAN sciolta come "Local Access Network" invece di **Local Area Network**. Riquadro Correzione.</td>
</tr>
<tr>
<td>3</td>
<td>CS-03 @ 00:04:10</td>
<td>Parlato vs fonti</td>
<td>Origine dell'HIV "forse ai primi dell'Ottocento" e diffusione legata a turismo e voli di linea. La stima scientifica è Kinshasa intorno al 1920 (Faria et al., *Science* 2014). Il docente premette "non sono un biologo". Riquadro Correzione.</td>
</tr>
<tr>
<td>4</td>
<td>CS-03 @ 00:01:44</td>
<td>Parlato incerto</td>
<td>Nome "virus" trovato "fino agli anni 60": frase poco chiara; il termine moderno è di Fred Cohen (1983-84). Nota aggiunta.</td>
</tr>
<tr>
<td>5</td>
<td>CS-03 @ 00:22:25</td>
<td>Dato senza fonte</td>
<td>Il trucco dell'utente non amministratore "vale per circa il 30% dei malware". Stima del docente, non verificabile; riportata come tale.</td>
</tr>
<tr>
<td>6</td>
<td>CS-03 @ 00:39:24</td>
<td>Parlato vs slide</td>
<td>Permessi di Ks Clean: *read phone status and identity* interpretato come accesso alla rubrica (è stato e identificativi del telefono, non contatti); *USB storage* interpretato come dispositivi collegati alla porta USB (è la memoria condivisa interna di Android). Riquadro Correzione.</td>
</tr>
<tr>
<td>7</td>
<td>CS-03 @ 00:52:53</td>
<td>Slide</td>
<td>Nella slide "Types of Hackers" le etichette *Black/White/Grey Hat Hackers* non corrispondono ai colori dei cappelli disegnati sopra. Il docente non la commenta nel dettaglio.</td>
</tr>
<tr>
<td>8</td>
<td>CS-03 @ 00:58:51, 00:59:11</td>
<td>Slide non commentate</td>
<td>"Cyber warfare" (Great Cannon / Great Firewall) e "Cyber warfare & geopolitics" sono a schermo mentre il docente parla di cyber warfare in generale, senza spiegarle. Descritte nel manuale con Nota aggiunta sul Great Cannon.</td>
</tr>
<tr>
<td>9</td>
<td>CS-03 @ 01:04:39</td>
<td>Parlato impreciso</td>
<td>Mandiant "prima ancora si chiamava FireEye": FireEye acquisì Mandiant (2013), riprese il nome Mandiant nel 2021, acquisita da Google nel 2022. Nota aggiunta.</td>
</tr>
<tr>
<td>10</td>
<td>CS-03 @ 01:16:38</td>
<td>Parlato / trascrizione</td>
<td>"La parola DDoS significa Denial of Service": è DoS; la distinzione con DDoS è poi spiegata correttamente. In Punti incerti.</td>
</tr>
<tr>
<td>11</td>
<td>CS-03 @ 01:18:15</td>
<td>Parlato vs slide</td>
<td>Il docente descrive la "richiesta di orario" come inviata al server bersaglio; la slide (NTP Servers) mostra un attacco di riflessione e amplificazione, in cui il server NTP è l'amplificatore e la vittima riceve le risposte. Il docente dice di non scendere nei dettagli. Nota aggiunta, non Correzione.</td>
</tr>
<tr>
<td>12</td>
<td>CS-03 @ 01:24:52</td>
<td>Slide non commentata</td>
<td>"Costo criminalità informatica (2021): 5,5 trilioni di euro, Source: European Commission". Il docente non cita la cifra; non verificata anno per anno, riportata com'è.</td>
</tr>
<tr>
<td>13</td>
<td>CS-03 @ 01:33:20</td>
<td>Slide</td>
<td>La schermata di riscatto è di WannaCry (2017), mentre i file in Esplora risorse hanno estensione *.CONTI* (ransomware Conti, 2020-22): due casi diversi accostati. Il docente non nomina nessuno dei due. Nota aggiunta.</td>
</tr>
</table>
### Verifiche numeriche
Unico esempio numerico verificabile: i conteggi della schermata WannaCry (slide "Ransomware" 2). Verificato con Python:
- `5/15/2017 16:25:02 - 2g 23:58:28 = 2017-05-12 16:26:34`
- `5/19/2017 16:25:02 - 6g 23:58:28 = 2017-05-12 16:26:34`
Stesso istante di partenza, quindi 3 e 7 giorni esatti, coerenti con il testo "You only have 3 days … if you don't pay in 7 days". Nessuna divergenza.
L'esempio degli "80 preventivi in un minuto" (circa 1,3 file al secondo) è qualitativo; il "30%" e i "12 MB" sono cifre aneddotiche senza calcolo da verificare.
### Trascrizione: affidabilità
- Audio pulito, un solo parlante per quasi tutta la lezione; unico intervento di studente @ 00:17:07 (segnalazione dello schermo non condiviso).
- Gli errori sono, come nelle altre lezioni, parole e sigle trascritte con sicurezza ma sbagliate ("hardware" per adware, "tre-tactor", "low enforcement", "l'autopasso", "farselle d'ordine"); l'elenco completo è nella sezione 17 del manuale.
- Frammenti non ricostruibili marcati \[?\]: 4 (vedi sezione 17).
- I fotogrammi a 01:07\:09-01\:07:11 e 01:10\:30-01\:10:50 mostrano il docente che scorre avanti e indietro fra le slide (cyber warfare, geopolitics, APT, state-sponsored actors, botnet) per richiamare lo schema rosso/grigio/blu: non sono nuove slide.
# Lezione 4
**Registrazione:** CS-04, Teams del 19/09/2025 (16:03 UTC), circa 01:44
**Fonti di confronto:** nessun materiale del docente. Le divergenze sono fra parlato e slide a schermo, e fra lezione e fonti esterne note (segnalate come tali). Per la mappatura dei file del portale vedi il documento della lezione 2.
### Divergenze della lezione 4
<table header-row="true">
<tr>
<td>#</td>
<td>Dove</td>
<td>Tipo</td>
<td>Descrizione</td>
</tr>
<tr>
<td>1</td>
<td>CS-04 @ 00:12:41</td>
<td>Parlato vs slide</td>
<td>Il docente chiama l'esfiltrazione "terza leva estorsiva", poi si corregge: nella slide è la seconda (double extortion). Nel manuale segue l'ordine della slide.</td>
</tr>
<tr>
<td>2</td>
<td>CS-04 @ 00:11:06 (slide)</td>
<td>Slide vs fonte originale</td>
<td>"1 attacco ogni 11 secondi" e "20 miliardi di euro (2021)", fonte "European Commission". Le cifre derivano da una **previsione** di Cybersecurity Ventures, in **dollari** (USD 20 miliardi entro il 2021). Non commentate dal docente. Nota aggiunta.</td>
</tr>
<tr>
<td>3</td>
<td>CS-04 @ 00:43:28</td>
<td>Parlato vs definizione</td>
<td>Vishing descritto come phishing "tramite videochiamata". È il *voice phishing* (chiamata vocale). Riquadro Correzione.</td>
</tr>
<tr>
<td>4</td>
<td>CS-04 @ 00:48:08</td>
<td>Slide</td>
<td>L'immagine "[http://JJ.com](http://JJ.com)" nella slide dell'email di phishing è decorativa e induce in errore uno studente (HTTP vs HTTPS); il docente dice che la rimuoverà.</td>
</tr>
<tr>
<td>5</td>
<td>CS-04 @ 01:08:05</td>
<td>Parlato impreciso</td>
<td>HTML smuggling associato al rootkit e all'installazione automatica al solo clic. L'HTML smuggling ricostruisce il file nel browser per eludere i filtri; l'installazione senza interazione è il drive-by download. Nota aggiunta (non Correzione: il concetto "il clic basta a far partire la catena" è corretto).</td>
</tr>
<tr>
<td>6</td>
<td>CS-04 @ 01:29:24</td>
<td>Parlato vs fatti noti</td>
<td>Stuxnet "avvenuto all'inizio del 2010", su una "centrale nucleare". Scoperto nel giugno 2010, attivo almeno dal 2009; il bersaglio era l'impianto di arricchimento di Natanz. Chiavetta "lanciata oltre il muro": racconto non documentato, presentato dal docente come "si crede". Nota aggiunta.</td>
</tr>
<tr>
<td>7</td>
<td>CS-04 @ 01:35:53</td>
<td>Incoerenza interna</td>
<td>"Livello applicativo numero 5" e poi "messaggio al layer 6" che imita un header di layer 3. Numerazione compatibile solo con il modello ibrido a 5 strati o lapsus. Nota aggiunta e \[?\].</td>
</tr>
<tr>
<td>8</td>
<td>CS-04 @ 01:40:51</td>
<td>Parlato vs slide</td>
<td>Diagramma presentato come "rete metropolitana di Tokyo": è la ShowNet della fiera Interop Tokyo 2009 (lo dice la slide stessa). Riquadro Correzione.</td>
</tr>
<tr>
<td>9</td>
<td>CS-04 @ 01:40:51</td>
<td>Dato numerico</td>
<td>Tokyo "10 milioni di abitanti e più, pare 11": Metropoli circa 14 milioni, 23 quartieri circa 9,7 milioni, area metropolitana oltre 37 milioni. Nota nella Correzione.</td>
</tr>
<tr>
<td>10</td>
<td>CS-04 @ 01:41:24</td>
<td>Parlato vs fonte</td>
<td>Mappa Facebook 2010 descritta come interconnessioni/attività dati della rete; è la visualizzazione delle amicizie fra città (Paul Butler). La slide la chiama *physical view*. Nota aggiunta.</td>
</tr>
<tr>
<td>11</td>
<td>CS-04 @ 01:32:56 (slide)</td>
<td>Slide</td>
<td>"VALN" invece di "VLAN" nel livello Data Link. Refuso.</td>
</tr>
<tr>
<td>12</td>
<td>CS-04 @ 01:18:54 (slide)</td>
<td>Slide</td>
<td>Il logo CrowdStrike fra gli attacchi alla supply chain: l'incidente di luglio 2024 fu un aggiornamento difettoso, non un attacco (come già annotato per la lezione 2). Nota aggiunta.</td>
</tr>
<tr>
<td>13</td>
<td>CS-04 @ 00:49:08</td>
<td>Precisazione</td>
<td>"Protocollo inventato più di 45 anni fa": SMTP (RFC 821) è del 1982, la posta su ARPANET del 1971. L'affermazione è compatibile; nessuna correzione.</td>
</tr>
</table>
### Verifiche numeriche (python)
- **Un attacco ogni 11 secondi** → 365 × 24 × 3600 / 11 = 2.866.909 attacchi l'anno (circa 2,87 milioni). Coerente con l'ordine di grandezza della fonte; non discusso dal docente.
- **Parametro del link di phishing** (`http://www.oo-d.com/?ip=...`, testo da OCR): decodificando in Base64 il frammento con le maiuscole ripristinate (`b2huY2Fib3QuZWR1`) si ottiene "[ohncabot.edu](http://ohncabot.edu)". Il parametro contiene quindi l'indirizzo del destinatario codificato, per tracciare chi clicca. L'indirizzo completo non è stato ricostruito (l'OCR perde le maiuscole, necessarie in Base64) e non è riportato.
- Nessun altro esempio numerico o blocco di codice nella lezione.
### Trascrizione e frame: affidabilità
- Audio pulito; gli errori sono, come nelle altre lezioni, su nomi propri, sigle e termini inglesi (John Capote, Harpanet, chip monkey, socio-anginio, evil made, quarrishing). Elenco completo nella sezione 19 del manuale.
- Un segmento degenerato (00:16:47, ripetizione "attori attuali") e un probabile salto (01:33\:02-01\:33:35).
- Gli interventi degli studenti scritti in chat (Anna, 00:56:34 e 01:14:32) sono letti o ripresi dal docente, non sempre udibili.
- Frame: 38 selezionati, tutti letti visivamente (2 sono la schermata iniziale Teams e il docente in video). Fra 00:46:27 e 00:47:17 il docente scorre rapidamente molte slide ("ho fatto un po' di confusione con l'ordine"): i timestamp dei frame di queste slide non coincidono con il momento in cui vengono commentate. Nel manuale ogni sezione usa il timestamp del parlato.
- Dall'indice OCR (non verificati visivamente): versione annotata "Anatomy of a phishing email (reve\[...\])" con il tooltip del link, slide di sezione "Physical Security" (01:21:51) e "Logical / Technical Security" (01:29:22).
# Lezione 5
**Registrazione:** CS-05, Teams del 22/09/2025 (a schermo "2025-09-22 16:07 UTC"), durata circa 02:19 (ultimo segmento a 02:18:48)
**Fonti di confronto:** nessun materiale del docente. Le divergenze sono fra parlato e slide a schermo, e fra lezione e fonti esterne note (segnalate come tali). Per la mappatura dei file del portale vale la tabella del file divergenze della lezione 2.
### Divergenze della lezione 5
<table header-row="true">
<tr>
<td>#</td>
<td>Dove</td>
<td>Tipo</td>
<td>Descrizione</td>
</tr>
<tr>
<td>1</td>
<td>CS-05 @ 00:00:01</td>
<td>Registrazione</td>
<td>La registrazione inizia a lezione avviata, con frase tronca ("La phishing, devo dirvi che…"). Eventuali minuti iniziali non sono recuperabili.</td>
</tr>
<tr>
<td>2</td>
<td>CS-05 @ 00:09:41</td>
<td>Parlato vs standard</td>
<td>"Unicode … permette di codificare fino a 65.000 caratteri". Lo spazio Unicode ha 1.114.112 punti di codice; 65.536 è il solo BMP. Riquadro Correzione.</td>
</tr>
<tr>
<td>3</td>
<td>CS-05 @ 00:10:46</td>
<td>Parlato vs norma</td>
<td>La "e" sostitutiva descritta come "simbolo della tara". Il simbolo ℮ (U+212E) indica la quantità nominale stimata dei preimballaggi, non la tara. Riquadro Correzione.</td>
</tr>
<tr>
<td>4</td>
<td>CS-05 @ 00:13:07</td>
<td>Terminologia</td>
<td>La sostituzione con caratteri simili è chiamata "typosquatting"; il termine specifico è *homoglyph attack*. Nota aggiunta, non correzione.</td>
</tr>
<tr>
<td>5</td>
<td>CS-05 @ 00:14:08</td>
<td>Slide (ammessa dal docente)</td>
<td>Titolo "Network monitoring – IPS/IPS, SIEM, proxies, IPS": il docente dice che la prima sigla doveva essere "IDS/IPS". IPS compare comunque tre volte.</td>
</tr>
<tr>
<td>6</td>
<td>CS-05 @ 00:31:16</td>
<td>Slide</td>
<td>Tabella "Some Dark Web networks": lunghezze degli indirizzi espresse in "bytes" (16/56 per .onion, 516 per I2P); sono caratteri. "proxed" per "proxied". Nota aggiunta.</td>
</tr>
<tr>
<td>7</td>
<td>CS-05 @ 00:32:27</td>
<td>Parlato incoerente</td>
<td>Sui servizi interni a Tor: "hanno ancora un nodo di uscita", dopo aver detto che non ne hanno bisogno. Segnato \[?\].</td>
</tr>
<tr>
<td>8</td>
<td>CS-05 @ 00:37:03</td>
<td>Slide non commentata</td>
<td>Il diagramma "Application Security" (CSRF con `<img src=".../destroy">`) non è spiegato dal docente. Nota aggiunta con il nome dell'attacco.</td>
</tr>
<tr>
<td>9</td>
<td>CS-05 @ 00:44:59 / 00:46:00</td>
<td>Slide e parlato vs standard</td>
<td>CVE chiamato "Common Vulnerability Events" (slide) e "Common Vulnerability Exposure" (parlato); il nome è Common Vulnerabilities and Exposures. Riquadro Correzione.</td>
</tr>
<tr>
<td>10</td>
<td>CS-05 @ 00:44:59</td>
<td>Slide, probabile didascalia errata</td>
<td>"Total CVE records for "log4j"": 177750 (giugno 2022) e 203230 (maggio 2023) sono dell'ordine del totale dei record CVE, non dei soli record log4j. Differenza fra i due valori: 25.480 in 11 mesi, plausibile come crescita dell'intero database. Nota aggiunta con "probabilmente"; non commentata dal docente.</td>
</tr>
<tr>
<td>11</td>
<td>CS-05 @ 00:46:00</td>
<td>Precisazione</td>
<td>"L'anno … in cui la vulnerabilità è stata pubblicata": è l'anno di assegnazione/riserva dell'ID. Nota aggiunta.</td>
</tr>
<tr>
<td>12</td>
<td>CS-05 @ 00:45:28</td>
<td>Riferimento vago</td>
<td>"Un nuovo regolamento europeo, l'Europa si doterà di un sistema analogo": con buona probabilità l'EUVD di ENISA (direttiva NIS2, operativo da maggio 2025), quindi già esistente alla data della lezione e previsto da una direttiva, non da un regolamento. Nota aggiunta, formulata come probabile.</td>
</tr>
<tr>
<td>13</td>
<td>CS-05 @ 00:50:33</td>
<td>Esempio impreciso</td>
<td>CVSS "tarato" sull'organizzazione che "incide su 0.2%": le metriche ambientali CVSS producono un punteggio 0–10, non una percentuale. Nota aggiunta.</td>
</tr>
<tr>
<td>14</td>
<td>CS-05 @ 00:50:41</td>
<td>Verifica numerica slide</td>
<td>Vedi sezione "Esempi numerici": conteggi e percentuali coerenti; "Weighted Average CVSS Score: 7" compatibile solo con l'estremo superiore delle fasce.</td>
</tr>
<tr>
<td>15</td>
<td>CS-05 @ 00:55:43</td>
<td>Lapsus</td>
<td>"Un ricercatore di sicurezza di Microsoft a Cupertino": Microsoft è a Redmond, Cupertino è Apple. Riquadro Correzione.</td>
</tr>
<tr>
<td>16</td>
<td>CS-05 @ 01:01:42</td>
<td>Esempio datato</td>
<td>Netflix con i video "sul data center di Amazon" / CDN Amazon: il backend è su AWS, ma i video sono distribuiti dal 2011–2012 soprattutto con la CDN propria Open Connect. Il docente stesso dubita ("non sono più certo"). Nota aggiunta.</td>
</tr>
<tr>
<td>17</td>
<td>CS-05 @ 01:12:02</td>
<td>Slide</td>
<td>"Virtualization-specific TTPs": refusi "that have compromised already compromised" e "betond". Riportati con (sic).</td>
</tr>
<tr>
<td>18</td>
<td>CS-05 @ 01:22:09</td>
<td>Parlato vs fatti</td>
<td>"Spotify azienda americana con sede legale in California, se non sbaglio": Spotify è svedese (holding in Lussemburgo). Riquadro Correzione.</td>
</tr>
<tr>
<td>19</td>
<td>CS-05 @ 01:25:19</td>
<td>Parlato vs slide</td>
<td>Data Governance Act: nel parlato il consenso è attribuito ai "titolari dei dati"; la slide lo attribuisce ai *data subjects* (dati personali) e il *permission* ai *data holders* (dati non personali). Nota aggiunta.</td>
</tr>
<tr>
<td>20</td>
<td>CS-05 @ 01:27:28</td>
<td>Non verificato</td>
<td>"8% dei dati totali della PA" come dati strategici, da un censimento ACN "dell'anno scorso": non verificato, riportato come detto.</td>
</tr>
<tr>
<td>21</td>
<td>CS-05 @ 01:30:04 – 01:31:49</td>
<td>Parlato vs norma (ripetuto dalla lezione 2)</td>
<td>GDPR applicato in base alla cittadinanza europea e al "riconoscimento del diritto dell'Unione" da parte degli stati terzi, con l'esempio del cittadino francese residente in America. L'art. 3 si basa sullo stabilimento del titolare e sulla presenza dell'interessato nell'Unione. Riquadro Correzione.</td>
</tr>
<tr>
<td>22</td>
<td>CS-05 @ 01:33:55</td>
<td>Parlato vs norma</td>
<td>DPO obbligatorio per "tutte le aziende al di là di una certa grandezza": l'art. 37 GDPR non usa la dimensione, ma la natura pubblica del soggetto e il tipo di trattamento (monitoraggio sistematico su larga scala, categorie particolari su larga scala). Riquadro Correzione.</td>
</tr>
<tr>
<td>23</td>
<td>CS-05 @ 01:31:28</td>
<td>Slide vs norma</td>
<td>"DPO … reports data breaches to national GDPR authorities": la notifica (art. 33) spetta al titolare; il DPO è punto di contatto. Nota aggiunta. Anche "accountant" per il DPO è un uso improprio.</td>
</tr>
<tr>
<td>24</td>
<td>CS-05 @ 01:33:55</td>
<td>Lapsus</td>
<td>"il titolare deve esercitare i propri diritti": è l'interessato. Segnalato in Punti incerti.</td>
</tr>
<tr>
<td>25</td>
<td>CS-05 @ 01:51:35</td>
<td>Verifica numerica slide</td>
<td>"Risk Profile Map": cinque celle non coerenti con un prodotto probabilità × impatto. Vedi sezione "Esempi numerici". Coerente con l'osservazione del docente che la linea "non coincide del tutto" con il rischio alto.</td>
</tr>
<tr>
<td>26</td>
<td>CS-05 @ 01:52:53</td>
<td>Terminologia</td>
<td>Nel trasferimento del rischio il docente chiama "premio" ciò che l'assicuratore paga (è l'indennizzo) dopo essersi corretto a metà frase. Nota aggiunta.</td>
</tr>
<tr>
<td>27</td>
<td>CS-05 @ 01:57:47 / 02:00:46</td>
<td>Slide non commentate</td>
<td>RPO, RTO, MTD e i modelli cold/warm/hot site non sono spiegati nel parlato. Nota aggiunta per RPO/RTO; MTD solo citato come testo di slide.</td>
</tr>
<tr>
<td>28</td>
<td>CS-05 @ 00:18:55 – 00:20:08</td>
<td>Slide di altra lezione</td>
<td>Scorrono per pochi secondi slide della lezione 4 (modello a livelli, LAN, MAN, WWAN, pivoting) durante il richiamo ai livelli di rete. Descritte come richiamo, senza commento del docente.</td>
</tr>
<tr>
<td>29</td>
<td>CS-05 @ 02:01:19</td>
<td>Coerenza calendario</td>
<td>"Domani la lezione non ci sarà" (23/09/2025): coerente con la registrazione successiva, CS-06, del 25/09/2025.</td>
</tr>
</table>
### Esempi numerici verificati con Python
**Dashboard Qualys WAS** (CS-05 @ 00:14:04–00:18:55): HIGH 62 + MED 39 + LOW 167 = 268 = "All Vulnerabilities". Catalog 348 + 20 + 84 + 20 + 1 = 473 = "Total". Righe applicazioni: 34 + 5 + 61 = 100; 28 + 31 + 104 = 163; 0 + 3 + 2 = 5. Tutto coerente.
**Surface/deep/dark web** (CS-05 @ 00:29:26): 4% + 90% + 6% = 100%. Coerente (il docente avverte che le percentuali andrebbero aggiornate; si tratta comunque di stime divulgative senza fonte in slide).
**Distribuzione CVSS** (CS-05 @ 00:50:41): conteggi 0, 2, 22, 5, 126, 43, 31, 135, 7, 83; somma 454 = "Total". Percentuali ricalcolate: 0,44; 4,85; 1,10; 27,75; 9,47; 6,83; 29,74; 1,54; 18,28; coincidono con la slide entro l'arrotondamento a una cifra (somma delle percentuali in slide 99,9). Media pesata: 6,48 con i valori centrali delle fasce, 5,98 con gli estremi inferiori, 6,98 con gli estremi superiori. Il "7" della slide è compatibile solo con l'ultimo calcolo o con punteggi puntuali non mostrati.
**Risk Profile Map** (CS-05 @ 01:51:35), confronto con probabilità (Improbable = 1 … Very High = 5) × impatto (Marginal = 1 … Catastrophic = 4):
<table header-row="true">
<tr>
<td>Cella</td>
<td>Slide</td>
<td>Prodotto atteso</td>
</tr>
<tr>
<td>Very High / Marginal</td>
<td>6</td>
<td>5</td>
</tr>
<tr>
<td>High / Marginal</td>
<td>8</td>
<td>4</td>
</tr>
<tr>
<td>Very Low / Critical</td>
<td>10</td>
<td>6</td>
</tr>
<tr>
<td>Improbable / Critical</td>
<td>4</td>
<td>3</td>
</tr>
<tr>
<td>Improbable / Catastrophic</td>
<td>7</td>
<td>4</td>
</tr>
</table>
Le altre 15 celle coincidono. La slide non dichiara la scala, quindi la divergenza è segnalata come incongruenza interna, non come errore certo. Effetto pratico: il valore 10 compare sia sopra la linea di tolleranza (Very High / Significant) sia sotto (Very Low / Critical), e l'8 compare in verde (High / Marginal) e in giallo (High / Significant, Very Low / Catastrophic).
Nessun calcolo di rischio con valori numerici è svolto nel parlato: il docente spiega la formula R = probabilità × perdita attesa solo qualitativamente.
### Trascrizione: affidabilità
- Per CS-05 è disponibile solo la trascrizione in markdown con timestamp ogni \~30 s; **non ci sono metriche** `avg_logprob` o probabilità per parola da analizzare. La revisione è stata fatta leggendo l'intera trascrizione e confrontandola con le slide.
- L'audio del docente è in generale ben trascritto. Gli errori sono, come nelle altre lezioni, su sigle e nomi propri (Fonder Line, TOTR, COPS, BGP, Agid, nasda) e su alcune parole comuni scambiate per omofoni ("ghetto" per gateway, "male, cero" per mare, cielo). Elenco completo nella sezione 15 del manuale.
- Le parti meno affidabili sono gli interventi degli studenti (CS-05 @ 00:02:52–00:03:24, 00:47:43, 00:48:59, 02:09:30–02:16:35): voci più lontane, frasi spezzate e alternanza non marcata fra studente e docente. Il contenuto è stato ricostruito solo dove il senso è inequivocabile.
- Fotogrammi: letti tutti i 56 selezionati; 6 non contengono slide di contenuto (copertina Teams, due griglie dei partecipanti, due inquadrature del docente durante le domande finali, la slide di sezione "Application Security"); 9 sono slide della lezione 4 richiamate di passaggio. Per "VPN usage for geo-masking purpose" (00:27:40) e per le slide di sezione "Cloud Security" (00:55:12), "Data Governance and Privacy" (01:15:03) e "Administrative Security" (01:43:49), non presenti fra i fotogrammi selezionati, il testo viene dall'indice OCR, segnalato come tale nel manuale dove rilevante.
# Lezione 6
**Registrazione:** CS-06, Teams del 25/09/2025 (16:04 UTC), durata circa 01:56
**Fonti di confronto:** nessun materiale del docente. Le divergenze sono fra parlato e slide a schermo, e fra lezione e fonti esterne note (segnalate come tali). Per la mappatura dei file del portale vedi `lezione-02-divergenze.md`.
### Divergenze della lezione 6
<table header-row="true">
<tr>
<td>#</td>
<td>Dove</td>
<td>Tipo</td>
<td>Descrizione</td>
</tr>
<tr>
<td>1</td>
<td>CS-06 @ 01:05:52</td>
<td>Parlato vs fatti</td>
<td>Chatbot che impara gli insulti dagli utenti, "ritirato dopo poche settimane". È Tay di Microsoft (23/03/2016), ritirato dopo circa 16 ore. Riquadro Correzione.</td>
</tr>
<tr>
<td>2</td>
<td>CS-06 @ 00:49:41</td>
<td>Slide, verifica numerica</td>
<td>Risk Profile Map (slide della lezione 5, a schermo di passaggio): con P = 5→1 e I = 1→4 il prodotto P×I torna in 15 celle su 20. Non tornano Very High/Marginal (6 vs 5), High/Marginal (8 vs 4), Very Low/Critical (10 vs 6), Improbable/Critical (4 vs 3), Improbable/Catastrophic (7 vs 4). Il valore 10 sta sia sopra sia sotto la linea di tolleranza. Verificato con Python. Nota aggiunta.</td>
</tr>
<tr>
<td>3</td>
<td>CS-06 @ 00:49:46</td>
<td>Parlato vs terminologia</td>
<td>Trasferimento del rischio (assicurazione cyber, vigilanza con copertura economica) accostato ai controlli compensativi. Nella terminologia usuale è un'opzione di trattamento del rischio distinta; la slide definisce i compensativi come "alternative measure of control". Nota aggiunta, non correzione: il parlato è ambiguo.</td>
</tr>
<tr>
<td>4</td>
<td>CS-06 @ 00:45:29</td>
<td>Parlato vs slide</td>
<td>La piramide ha sei categorie; il docente ne commenta cinque, omettendo *corrective*. Nota aggiunta.</td>
</tr>
<tr>
<td>5</td>
<td>CS-06 @ 01:29:25 e 01:31:21</td>
<td>Parlato vs slide</td>
<td>CTI operativa: "pochi giorni, poche settimane" (slide: weeks/months). CTI tattica: "secondi, minuti, al massimo ore" (slide: minutes/hours). Nota aggiunta.</td>
</tr>
<tr>
<td>6</td>
<td>CS-06 @ 01:14:20</td>
<td>Parlato vs slide</td>
<td>Esempio "nonna": il docente parla di Cappuccetto Rosso che ruba la mela nel negozio del lupo; la slide mostra una storia della buonanotte sul rubare mele dall'albero del vicino. Riportati entrambi.</td>
</tr>
<tr>
<td>7</td>
<td>CS-06 @ 01:11:42</td>
<td>Slide</td>
<td>Lo schema intitolato "Prompt Injection attack" rappresenta un model extraction attack (f = f′). Le immagini su Anthropic riguardano uno scenario di test controllato (system card di Claude Opus 4, maggio 2025), non un incidente reale; non commentate dal docente. Nota aggiunta.</td>
</tr>
<tr>
<td>8</td>
<td>CS-06 @ 01:09:41</td>
<td>Esempio non nominato</td>
<td>Auto a guida autonoma ingannata da segni sulla strada: verosimilmente Tencent Keen Security Lab su Tesla Autopilot (2019). Tecnicamente è un attacco con adversarial examples in inferenza più che un poisoning dei dati di addestramento. Nota aggiunta.</td>
</tr>
<tr>
<td>9</td>
<td>CS-06 @ 00:37:42</td>
<td>Parlato incompleto</td>
<td>TLP "istituito dal FIRST": nato in ambito governativo britannico (NISCC) nei primi anni 2000, standardizzato dal FIRST; TLP 2.0 dell'agosto 2022. Nota aggiunta.</td>
</tr>
<tr>
<td>10</td>
<td>CS-06 @ 00:11:16</td>
<td>Nome impreciso</td>
<td>"Payment Card Industry Consortium": l'ente è il PCI Security Standards Council (2006). Nota aggiunta.</td>
</tr>
<tr>
<td>11</td>
<td>CS-06 @ 01:55:07</td>
<td>Parlato vs fatti</td>
<td>Mimikatz e Rubeus "sviluppati da aziende più che dal singolo programmatore": Mimikatz è di un singolo ricercatore (Benjamin Delpy); Rubeus della suite GhostPack (SpecterOps). Nota aggiunta.</td>
</tr>
<tr>
<td>12</td>
<td>CS-06 @ 00:32:19</td>
<td>Slide</td>
<td>Slide UK con refusi e duplicazioni: "nuances protective controls", "as well as to as well as to", frase finale ripetuta. Riportata com'è.</td>
</tr>
<tr>
<td>13</td>
<td>CS-06 @ 01:42:35</td>
<td>Slide</td>
<td>Riquadro "The Script Kiddie" con testo che comincia "The Getaway is too young…". Refuso della slide.</td>
</tr>
<tr>
<td>14</td>
<td>CS-06 @ 00:54:11</td>
<td>Slide</td>
<td>Titolo `Security controls" matrix` con doppio apice al posto dell'apostrofo. Refuso.</td>
</tr>
<tr>
<td>15</td>
<td>CS-06 @ 00:28:22</td>
<td>Citazione non attribuita</td>
<td>"Un noto politico all'epoca della guerra fredda": è il *trust, but verify* di Reagan. Nota aggiunta.</td>
</tr>
<tr>
<td>16</td>
<td>CS-06 @ 00:21:42</td>
<td>Organizzazione non nominata</td>
<td>Associazione dei major studios per gli assessment: verosimilmente MPA (già MPAA), oggi programma TPN. Nota aggiunta, con "verosimilmente".</td>
</tr>
</table>
**Verifica numerica.** L'unico contenuto numerico verificabile è la Risk Profile Map (divergenza 2), controllata con uno script Python (prodotto P×I cella per cella). Nessun comando di terminale o tool d'attacco a schermo; i prompt degli esempi di prompt injection sono trascritti in blocchi di testo dalle slide (@ 01:13:13 e @ 01:14:13 dall'immagine, la risposta "grandma" @ 01:14:57 da OCR).
**Slide non presenti fra i frame selezionati** e riportate da OCR (segnalate nel manuale come "testo da OCR, non verificato visivamente"): versione completa di "Artificial Intelligence in Cybersecurity" (@ 01:01:54), di "AI phases and related attack types" (@ 01:09:53), di "Prompt injections" con la risposta "grandma" (@ 01:14:57), di "Cyber \[Threat\] Intelligence" con ciclo, CI, CTI e controintelligence (@ 01:19:29, @ 01:26:29).
### Trascrizione: affidabilità
- Per CS-06 nella cartella non sono disponibili i valori `avg_logprob`: la valutazione è solo qualitativa.
- Come per le altre lezioni del corso, l'audio è pulito e il parlato è trascritto bene; gli errori veri sono sigle e termini tecnici trascritti con sicurezza (XIRT per CSIRT, Synth/Closing per OSINT/CLOSINT, "modo superandi" per modus operandi, "saperspazio" per cyberspazio). L'elenco completo delle correzioni è nella sezione 16 del manuale.
- Sette passaggi restano \[?\] (sezione 16 del manuale), nessuno decisivo per il contenuto.
- Il docente scorre brevemente all'indietro le slide della lezione 5 (@ 00:49:40–00:50:45: BCP, DRP, BCP vs DRP, Risk Profile Map, ISO 27000, classificazioni) per mostrare la matrice del rischio; queste slide non sono commentate in questa lezione, tranne il rimando alla matrice.
# Lezione 7
**Registrazione:** CS-07 (portale `lezione_7`, 26/09/2025 16:08, 105 s) + CS-08 (portale `lezione_8`, 26/09/2025 16:15, circa 01:10:00), due parti della stessa lezione.
**Fonti di confronto:** nessun materiale del docente. Le divergenze sono fra parlato e slide a schermo, e fra lezione e fonti esterne note (segnalate come tali).
**Nota sulla struttura del corso.** A *CS-08 @ 00:49:59* il docente dice che il corso "oggi finisce": la lezione 7 è l'ultima. Questo chiude la domanda lasciata aperta nella mappatura (lezione 2) sull'esistenza di un'ottava lezione: non c'è; manca solo la lezione 1.
### Divergenze della lezione 7
<table header-row="true">
<tr>
<td>#</td>
<td>Dove</td>
<td>Tipo</td>
<td>Descrizione</td>
</tr>
<tr>
<td>1</td>
<td>CS-08 @ 00:20:16</td>
<td>Parlato vs modello</td>
<td>Infrastructure del Diamond Model descritta come "l'infrastruttura che l'avversario colpisce"; nel modello (e nell'esempio della slide: C2 domain, C2 IP) è l'infrastruttura **usata** dall'avversario. Il docente si corregge in parte a 00:20:47. Riquadro Correzione.</td>
</tr>
<tr>
<td>2</td>
<td>CS-08 @ 00:09:29</td>
<td>Parlato vs slide</td>
<td>Exploitation descritta come movimento laterale e scalata di privilegi; la slide: "the malware is triggered, exploiting vulnerable applications or systems". Nota aggiunta.</td>
</tr>
<tr>
<td>3</td>
<td>CS-08 @ 00:31:57</td>
<td>Parlato vs norma</td>
<td>"Tipicamente il DPO può decidere" sulle DPIA facoltative; per l'art. 35 GDPR decide il titolare, consultato il DPO. Correzione.</td>
</tr>
<tr>
<td>4</td>
<td>CS-08 @ 00:36:49</td>
<td>Parlato vs norma</td>
<td>Libero professionista con partita IVA indicato come persona giuridica; è una persona fisica. Correzione.</td>
</tr>
<tr>
<td>5</td>
<td>CS-08 @ 00:39:28</td>
<td>Slide e parlato vs norma</td>
<td>Privacy/GDPR riferiti ai "cittadini europei" / "EU nationals": l'art. 3 GDPR si basa sulla localizzazione, non sulla cittadinanza (già corretto in lezione 2). Nota aggiunta.</td>
</tr>
<tr>
<td>6</td>
<td>CS-08 @ 00:43:12</td>
<td>Slide</td>
<td>Cesare presentato come cifrario a **trasposizione**; è a **sostituzione**. Correzione (slide).</td>
</tr>
<tr>
<td>7</td>
<td>CS-08 @ 00:42:45</td>
<td>Parlato vs fonte</td>
<td>Messaggero con testa rasata e tatuata attribuito ai "poemi omerici"; l'episodio è in Erodoto (Istieo), ed è steganografia. Correzione.</td>
</tr>
<tr>
<td>8</td>
<td>CS-08 @ 00:44:41</td>
<td>Slide vs storiografia</td>
<td>"Vigenère's (invented by Leon Battista Alberti)" e tabula recta "described in book Steganographia": il cifrario detto di Vigenère è di Bellaso (1553), Alberti inventò il disco cifrante (1467); la tabula recta è nella *Polygraphia* di Tritemio. Nota aggiunta.</td>
</tr>
<tr>
<td>9</td>
<td>CS-08 @ 00:50:03</td>
<td>Slide (OCR)</td>
<td>"Rotor cipher machines started to be used… in XIX century": sono del XX secolo. Correzione (slide).</td>
</tr>
<tr>
<td>10</td>
<td>CS-08 @ 00:47:46</td>
<td>Parlato vs storia</td>
<td>La macchina di Turing "universalmente considerata il primo calcolatore della storia" che fa brute force: la Bombe era elettromeccanica e specializzata, usava i crib; il primo calcolatore elettronico programmabile di Bletchley Park fu Colossus (contro Lorenz). Correzione.</td>
</tr>
<tr>
<td>11</td>
<td>CS-08 @ 00:46:51</td>
<td>Generalizzazione</td>
<td>"Ogni algoritmo… almeno classico… può essere rotto per brute force": eccezione del one-time pad. Nota aggiunta.</td>
</tr>
<tr>
<td>12</td>
<td>CS-08 @ 00:52:58</td>
<td>Slide</td>
<td>"current encryption, hashing and signing algorithms shall be broken by… quantum computers": gli hash e i simmetrici con parametri adeguati non sono considerati rotti (Grover è solo quadratico); a rischio la crittografia a chiave pubblica (Shor). Nota aggiunta.</td>
</tr>
<tr>
<td>13</td>
<td>CS-08 @ 00:53:47</td>
<td>Terminologia</td>
<td>Crittologia e crittoanalisi presentate come le due branche; nell'uso standard la crittologia comprende crittografia e crittoanalisi. Correzione.</td>
</tr>
<tr>
<td>14</td>
<td>CS-08 @ 01:03:16</td>
<td>Parlato vs fatti</td>
<td>Blowfish "usato nelle vecchie versioni del protocollo Bluetooth": il Bluetooth classico usava E0 e SAFER+, poi AES-CCM. Correzione.</td>
</tr>
<tr>
<td>15</td>
<td>CS-08 @ 01:05:08</td>
<td>Parlato impreciso</td>
<td>Le KDF eviterebbero che una password semplice dia una chiave debole: una KDF non aggiunge entropia, rallenta gli attacchi (stretching, salt). Correzione (precisazione).</td>
</tr>
<tr>
<td>16</td>
<td>CS-08 @ 01:06:10 e slide 01:05:39</td>
<td>Generalizzazione</td>
<td>"Cifro con una chiave, decifro con l'altra" in entrambi i versi vale per RSA; nella lista della slide ECDSA, EdDSA, DSS/DSA sono firme, ECDH è accordo di chiave. Nota aggiunta.</td>
</tr>
<tr>
<td>17</td>
<td>CS-08 @ 01:07:52</td>
<td>Parlato vs slide della stessa lezione</td>
<td>"La chiave privata è molto più grande" della pubblica: falso in generale; la slide "Cryptology & Crypto-analysis" mostra una chiave secp256k1 con privata di 32 byte e pubblica di 66. Correzione.</td>
</tr>
<tr>
<td>18</td>
<td>CS-08 @ 00:53:50</td>
<td>Slide, verifica numerica</td>
<td>Etichette della struttura ECPrivateKey ("119 Bytes", "\[0\] 10 Bytes", "\[secp256k1\] 8 Bytes") non coincidono con il dump a schermo (`30 74` = 118 byte) né con la generazione in Python (118; \[0\] 9 byte; OID 7 byte). OID 1.3.132.0.10 corretto. Nota aggiunta.</td>
</tr>
<tr>
<td>19</td>
<td>CS-08 @ 00:15:23</td>
<td>Slide</td>
<td>Infografica "MITRE Kill Chain" con tattiche PRE-ATT&CK (TA0012–TA0025) dismesse da MITRE nel 2020: materiale datato. Nota aggiunta.</td>
</tr>
<tr>
<td>20</td>
<td>CS-08 @ 00:23:57, 00:44:41</td>
<td>Slide, forma</td>
<td>Le slide usano il trattino lungo; nel manuale è reso con due punti o virgola per rispetto delle convenzioni. Non è una divergenza di contenuto.</td>
</tr>
<tr>
<td>21</td>
<td>CS-08 @ 00:21:05</td>
<td>Slide</td>
<td>"Capabilites" (sic) nella slide "Attribution of cyber incidents". Refuso.</td>
</tr>
</table>
### Verifiche numeriche e crittografiche (Python)
<table header-row="true">
<tr>
<td>Oggetto</td>
<td>Esito</td>
</tr>
<tr>
<td>"Ancient ciphers": HELLO → URYYB con tabella A–M / N–Z</td>
<td>Corretto: ROT13 (spostamento 13)</td>
</tr>
<tr>
<td>ACH: riga *Scoring* 5, 1, -1, 2, -5</td>
<td>Corretto: coincide con le somme per colonna</td>
</tr>
<tr>
<td>CVE-2023-5625: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H → 7.5 HIGH</td>
<td>Corretto: formula CVSS 3.1 dà 7.5</td>
</tr>
<tr>
<td>ECPrivateKey secp256k1</td>
<td>DER di 118 byte (`30 74`), privata 32 byte, punto pubblico 65 byte (BIT STRING 66): coerente con il dump, non con le etichette "119/10/8 Bytes" (divergenza 18)</td>
</tr>
<tr>
<td>Tabula recta 26×26</td>
<td>676 celle; nessun calcolo nella lezione</td>
</tr>
</table>
### Trascrizione: affidabilità
- Audio pulito, come nelle altre lezioni; gli errori sono di nuovo su sigle e nomi propri trascritti con sicurezza (inmitter, cyber che il cipre, wifi ROG, DPA, partita IME, security to obscurity). Elenco completo nella sezione 19 del manuale.
- Lacuna di circa 30 s in CS-08 fra 00:15:55 e 00:16:33 (inizio descrizione della UKC).
- CS-07 contiene solo tre segmenti utili (00:00:10–00:01:14); il contenuto è ripreso quasi identico all'inizio di CS-08.
- Frame letti visivamente: 2 (CS-07) + 41 (CS-08). Testi presi dall'OCR, perché assenti dai frame selezionati, e segnalati nel manuale: CKC con descrizioni (00:09:05, 00:14:05), Triad of Information Security (00:34:35, 00:35:35), voce Privacy della Triad of Digital Trust (00:39:28), testo completo della slide Enigma (00:50:03), matrice ATT&CK a 00:02:53, diagramma completo della cifratura (01:02:57).
- Tre slide (Pyramid of Pain, ACH, CoA) sono passate in circa tre secondi senza commento; il loro testo è letto dai frame.
# Edizione 2026 (Teams)
# Lezione 1 2026
## Divergenze
- **Organizzazione del corso.** Nel 2025 SOC/CSIRT/CERT (cap. 02, sez. 5), DDoS e ransomware (cap. 03, sez. 14-15), CTI (cap. 06) e red teaming (cap. 07, sez. 10) sono nel corso di primo livello. Nel 2026 il docente ne colloca almeno una parte nel master di secondo livello (Teams 1 @ 0:03:52, 0:23:40), con un'indicazione contraddittoria sul ransomware (Teams 1 @ 1:14:17). Possibile ristrutturazione, da confermare.
- **CrowdStrike.** Nel cap. 02 (sez. 9) l'incidente è evocato come dipendenza da Microsoft ("chi controlla gli aggiornamenti di Windows?"). Nel 2026 il docente chiarisce che si trattò di una patch sbagliata di CrowdStrike, un EDR, e di un evento di sicurezza senza intento malevolo (Teams 1 @ 0:28:56). Resta l'imprecisione "i prodotti Microsoft di tutto il mondo smettono di funzionare" (Teams 1 @ 0:28:07) e il ripristino descritto come reinstallazione con chiavetta USB (Teams 1 @ 0:35:29), mentre la procedura reale era cancellare il file difettoso in modalità provvisoria.
- **Stuxnet.** Cap. 04 (sez. 14): attacco "all'inizio del 2010", chiavetta collegata alla rete esterna o direttamente al computer isolato, poi escalation e movimento laterale. Teams 1: attacco del 2009 (come la slide) scoperto anni dopo, "la più grande catastrofe nucleare del mondo" evitata, meccanismo descritto come una **ventola di raffreddamento** fatta sembrare funzionante per surriscaldare l'impianto (Teams 1 @ 0:41:30), e in più l'attribuzione tramite commenti nel codice e il possibile false flag (Teams 1 @ 0:43:25). **Correzione:** Stuxnet alterava la velocità delle centrifughe di arricchimento di Natanz tramite i PLC, mostrando valori normali agli operatori; non c'erano ventole né rischio di fusione di un reattore.
- **WannaCry: la data.** Cap. 03 (sez. 15) mostra la schermata del maggio 2017. Teams 1 dice più volte 2016 ("nel 2016, poi proseguito nel 2017", Teams 1 @ 0:15:52; "i media nel 2016", Teams 1 @ 1:15:19; "dal 2016 al 2026", Teams 1 @ 1:16:47). **Correzione:** WannaCry è del 12 maggio 2017.
- **Von der Leyen.** Coerente con i rimandi 2025 (cap. 02 sez. 5, cap. 05 sez. 6): discorso sullo Stato dell'Unione 2021, "tutto è interconnesso, tutto può essere hackerato", "fare sistema". Nel 2026 in più l'elenco degli atti legislativi (NIS, NIS2, DORA, Cyber Resilience Act, Cybersecurity Act) (Teams 1 @ 0:11:17).
- **GDPR e cittadinanza.** Il docente ripete la tesi del cap. 02 (sez. 9) e del cap. 05 (sez. 9): GDPR applicabile ai dati dei cittadini europei in tutti i paesi che riconoscono il diritto dell'Unione (Teams 1 @ 1:11:03). Stessa **Correzione** del 2025: l'art. 3 GDPR guarda allo stabilimento del titolare e alla presenza dell'interessato nell'Unione, non alla cittadinanza.
- **Triade CIA nel 2026 subito con la voce Privacy.** La slide "The triad of Information Security" vista a Teams 1 @ 1:12:00 riporta già la voce Privacy sotto le tre proprietà; nel cap. 07 (sez. 11) la stessa slide compare con Safety aggiunta e la voce Privacy sta sulla triade del digital trust. Differenza di impaginazione, non di contenuto.
- **TAC da "diversi miliardi"** (Teams 1 @ 1:20:50): lapsus, costano da centinaia di migliaia a qualche milione di euro.
# Lezione 2 2026
## Divergenze
- **Identify nel CSF 2.0 (ripetuta dal 2025).** Il docente descrive di nuovo identify come individuazione delle minacce presenti o che "si affacciano alla porta", anche dalla sicurezza perimetrale. Nel CSF 2.0 identify riguarda la comprensione del rischio (asset, risk assessment, improvement); rilevare eventi in corso è detect. Stessa correzione del capitolo 02, sezione 7. (Teams 2 @ 0:56:18)
- **"La quinta e la sesta in giallo".** Parlando di Govern il docente dice "la quinta e la sesta"; Govern è la sesta funzione aggiunta alle cinque storiche. Lapsus. (Teams 2 @ 0:58:08)
- **CERT "brevettato".** Correzione: CERT è un **marchio registrato** (service mark) della Carnegie Mellon University, non un brevetto. Nel 2025 il docente parlava correttamente di marchio con processo di autorizzazione all'uso. (Teams 2 @ 0:28:39)
- **CSIRT e CERT.** Nel 2025 il docente diceva che i compiti coincidono sempre di più e che molti CSIRT diventano CERT con l'accreditamento; nel 2026 insiste invece che la differenza c'è (risposta immediata contro emergenza a medio e lungo termine con threat intelligence). Non è una contraddizione netta ma un'enfasi diversa. (Teams 2 @ 0:29:09)
- **ISAC.** Il docente scioglie la sigla come "Information Sharing Analytics Center"; nel 2025 la slide riportava "Information Sharing and Analysis Centre", forma corretta. Probabile imprecisione orale o di trascrizione. (Teams 2 @ 0:30:31)
- **Log4j.** Correzione: Log4Shell (CVE-2021-44228, dicembre 2021) era una vulnerabilità di progettazione involontaria (lookup JNDI), non codice malevolo inserito da un attore della minaccia. Il docente dice che per Log4j "è avvenuta esattamente così", cioè come una backdoor iniettata: vale solo per XZ. (Teams 2 @ 1:14:48)
- **Data di XZ.** Il docente la colloca "nel 2023, se non sbaglio, o inizio 2024". La backdoor in xz-utils (CVE-2024-3094) è stata scoperta il 29 marzo 2024 nelle versioni 5.6.0 e 5.6.1, pubblicate fra febbraio e marzo 2024; l'attore aveva costruito la propria reputazione nel progetto a partire dal 2021. Nota aggiunta. (Teams 2 @ 1:14:15)
- **Ordine degli argomenti.** Rispetto al 2025 la lezione anticipa digital trust (capitolo 07) e red teaming (capitolo 07) e recupera le slide "Types of threat" e "Non-scripted threats" che nel 2025 erano state saltate come non importanti.
---
## Punti incerti
- \[?\] Teams 2 @ 0:29:58: "[italialabbiamovistoanchenelreport.cn](http://italialabbiamovistoanchenelreport.cn) del 2023". Il report non è ricostruibile con certezza; plausibile "report ACN" (Agenzia per la Cybersicurezza Nazionale) o "report Clusit".
- \[?\] Teams 2 @ 0:52:01: ransomware in un sito del governo tedesco con circa 6 TB di dati pubblicati, "pochi giorni fa" (inizio settembre 2026). Evento non verificabile da qui; il docente dice che ne riparlerà.
- Teams 2 @ 0:55:08 e 1:16:34: la "domanda fatta all'inizio del corso" su come ci si difende non è nella registrazione; le tre risposte sono ricostruite dal parlato.
- Trascrizione automatica corretta nel testo: "xirt" = CSIRT, "certe" = CERT, "Isaac" = ISAC, "CIA Technology officer" = Chief Technology Officer, "CO" = CIO, "Red Taving" = red teaming, "Ida team" = red team, "lock for J / log for J" = Log4j, "d'ora" = DORA, "nist/list" = NIST, "tumper proof" = tamper-proof, "singulisti" = sicuristi.
- Voci oltre l'ora con formato "1 ora N secondi" (senza minuti): interpretate come 1:00:13, 1:00:27, 1:00:45.
# Lezione 3 2026
## Divergenze
- **Consiglio dell'utente senza privilegi e trojan.** Nel 2025 il docente diceva che il consiglio **non protegge dai trojan** (se si dà la password all'installazione il danno è fatto) e che vale per circa il 30% dei malware. Nel 2026 lo presenta come difesa efficace proprio contro i trojan generici (grazie al prompt che fa scattare il sospetto) e parla di una percentuale "non altissima" senza cifre. Le due versioni si conciliano solo se l'utente, vedendo il prompt, rifiuta. (Teams 3 @ 0:07:56 - 0:08:31)
- **RAT mirato o di massa.** Nel 2025: il RAT presuppone un attaccante umano e un attacco molto mirato, non è il caso standard. Nel 2026: dall'altra parte può esserci un sistema automatico o un'AI, e le infezioni sono il più delle volte di massa, a strascico, con i computer riuniti in botnet. (Teams 3 @ 0:31:48 - 0:32:22)
- **Origine dell'HIV.** Correzione: nel 2026 il docente colloca lo spillover a "fine del Seicento, primi del Settecento" (nel 2025: "primi dell'Ottocento"). La stima scientifica per l'HIV-1 gruppo M è intorno al 1920, area di Kinshasa (Faria et al., Science, 2014). (Teams 3 @ 0:04:55)
- **Assistenti di volo "primi importatori" dell'HIV in Occidente.** Correzione: è la tesi del cosiddetto "paziente zero" (lo steward Gaétan Dugas), smentita da analisi genetiche (Worobey et al., Nature, 2016), secondo cui il virus circolava negli Stati Uniti già dai primi anni '70, arrivato attraverso i Caraibi. (Teams 3 @ 0:05:27)
- **Perquisizioni in Italia.** Correzione parziale: per i dipendenti l'art. 6 dello Statuto dei lavoratori (L. 300/1970) ammette visite personali di controllo solo se indispensabili per la tutela del patrimonio aziendale, all'uscita, con selezione automatica, nel rispetto della dignità e previo accordo sindacale o autorizzazione dell'ispettorato. Non è quindi un divieto assoluto come dice il docente, ma un regime molto restrittivo. (Teams 3 @ 1:08:40)
- **Leak del film X-Men.** Nota aggiunta: si tratta con ogni probabilità di "X-Men le origini: Wolverine", la cui copia di lavorazione circolò online nell'aprile 2009, circa un mese prima dell'uscita. La modalità di esfiltrazione raccontata (disco USB nel data center) è la versione del docente; le fonti pubbliche non ne ricostruiscono ufficialmente l'origine. (Teams 3 @ 1:05:51)
- **Frequenza della revisione dei permessi delle app:** 4-6 mesi nel 2026, tre mesi nel 2025. (Teams 3 @ 0:44:45)
- **Injection e smuggling.** L'attacco basato su contenuti di un livello interpretati come intestazioni di un altro livello è chiamato "smuggling" nel 2025 e "injection" nel 2026. Per la nota tecnica vale quella del capitolo 04, sezione 15 (packet-in-packet injection, HTTP request smuggling). (Teams 3 @ 1:21:06)
- **Mappa di Tokyo.** Il docente ripete che il diagramma è la rete metropolitana di Tokyo di circa vent'anni fa; resta valida la correzione del 2025 (è la ShowNet di Interop Tokyo 2009). (Teams 3 @ 1:23:41)
- **Mappa Facebook 2010.** Il docente la descrive come flusso di dati rilevato da Facebook; resta valida la nota del 2025 (visualizzazione delle amicizie fra città, Paul Butler). (Teams 3 @ 1:24:25)
---
## Punti incerti
- \[?\] Teams 3 @ 0:21:49: variabile d'ambiente "Magic" valorizzata con "MTZE" nello screenshot del rootkit; il valore e il rootkit specifico non sono ricostruibili dalla trascrizione, e il docente stesso dice di non sapere quale vulnerabilità sfrutti.
- \[?\] Teams 3 @ 0:33:24 - 0:33:41: "Le botnet possono ... non risultare infettate": dal contesto, i computer della botnet possono non sembrare infetti.
- Teams 3 @ 1:07:16: "il primo corridoio, se non sbaglio": dettaglio incerto dichiarato dal docente.
- Trascrizione automatica corretta nel testo: "cavallo di \*\*\*\*\*" = cavallo di Troia (la parola è censurata dal filtro della trascrizione), "rat/rabbia" = RAT, "sminare" = minare, "Besh" = bash, "LS mod" = lsmod, "Staxnet" = Stuxnet, "Freeway Handshake" = three-way handshake, "syn Hack / Hack" = SYN-ACK / ACK, "PCPODPE" = TCP o UDP, "IPV4E" = IPv4 e, "shoulder spine / schulde spine" = shoulder spying, "[undiscous.be](http://undiscous.be)" = un disco USB, "Cybertrath / Cyber Creating Intelligence" = Cyber Threat Intelligence, "blackout" = black hat, "genere/genio informatico" = igiene informatica, "Air gaped" = air-gapped.
# Lezione 4 2026
## Divergenze
- **Livelli della VPN.** 2026: VPN di livello 2 e di livello 3. 2025 (cap. 05 sez. 3): livelli 3, 4 o 5. La versione 2026 è più corretta (esistono VPN L2, per esempio L2TP o VPN su Ethernet, e L3 come IPsec; le VPN TLS operano più in alto ma trasportano comunque traffico L2/L3). Per l'esame, fa fede ciò che il docente dice in aula: attenzione se la domanda riprende l'una o l'altra formulazione. (Teams 4 @ 0:01:47)
- **Correzione: Tor e protocollo IP.** Il docente dice che dal punto di ingresso in poi "smette di parlare il protocollo IP e parla il protocollo Tor", "molto diverso dal protocollo IP". In realtà Tor è una rete overlay che viaggia sopra TCP/IP: i relay comunicano fra loro con connessioni TCP cifrate TLS; ciò che cambia è l'instradamento a cipolla e l'indirizzamento dei servizi .onion, non il protocollo di rete sottostante. (Teams 4 @ 0:13:28, 0:16:15)
- **IDS "funzione del firewall".** Il docente presenta l'intrusion detection system come "una funzione del firewall" e mescola IDS e IPS nella stessa frase. IDS e IPS possono essere integrati nei firewall di nuova generazione, ma sono anche sistemi autonomi; l'IDS rileva e segnala, l'IPS rileva e blocca. Non è un errore netto, ma è una semplificazione. (Teams 4 @ 0:45:05)
- **BCP correttivo, DRP di recovery.** Coerente con la slide 2025 "BCP vs DRP in practice" (Corrective/Restorative). Nessuna divergenza, ma nel 2025 la classificazione non era detta esplicitamente a voce. (Teams 4 @ 0:47:08)
- **CVE.** Il docente dice ancora "evento di vulnerabilità comune" e che "comune sta per noto pubblico". Come già corretto nel manuale 2025: CVE significa Common Vulnerabilities and Exposures. (Teams 4 @ 1:05:09)
- **Patch Tuesday "ogni martedì o ogni due martedì".** Microsoft pubblica gli aggiornamenti di sicurezza ordinari il **secondo martedì del mese** (Patch Tuesday), con rilasci straordinari fuori ciclo; non ogni martedì. (Teams 4 @ 1:14:39)
- **Trasferimento del rischio.** 2026: può avvenire anche verso un'altra funzione interna dell'organizzazione. Nel 2025 era presentato solo verso terzi (assicurazione). Non contraddittorio, ma più ampio. (Teams 4 @ 0:29:27)
## Punti incerti
- \[?\] **974 CVE in un solo Patch Tuesday** con due zero-day (Teams 4 @ 1:14:57). Numero molto superiore ai record storici noti fino al 2025 (ordine di grandezza 100-200 per ciclo mensile); non verificabile dalla sola trascrizione, potrebbe essere un errore di trascrizione del numero o un dato reale del settembre 2026. Da verificare sul Security Update Guide di Microsoft prima di citarlo.
- \[?\] **"Nei primi due mesi del 2026 abbiamo di gran lunga superato" le 48.000 CVE del 2025** (Teams 4 @ 1:12:32). Il docente dice anche che la crescita è esplosa "dopo il marzo di quest'anno" (1:05:43): le due affermazioni sono in tensione sul periodo. Il dato 2025 (circa 48.000) è plausibile; quello 2026 non è verificabile qui.
- \[?\] "Motori di intelligenza artificiale generativa come cloud e altri" (Teams 4 @ 1:12:48): quasi certamente "Claude" trascritto come "cloud".
- \[?\] "RTRPO recovery point objective" (Teams 4 @ 0:35:34): il docente nomina insieme RTO e RPO; dal contesto RTO = 7 minuti e RPO = 1 settimana.
- \[?\] "1 1 tassonomia", "A1ESPA1 fornitore" (Teams 4 @ 0:39:09, 0:03:16): trascrizione di "una tassonomia", "a un ISP, a un fornitore".
- Trascrizione corretta nel testo: "Thor" = Tor; "rakeretici" = hacker etici; "Zerodei" = zero-day; "CPE pubblicate" = CVE pubblicate; "matura della minaccia" = attore della minaccia; "iaspas e SAS" = IaaS, PaaS e SaaS; "owasp" = OWASP; "PCIDSS" = PCI DSS; "trusted panel network" = Trusted Partner Network; "cavallo di \*\*\*\*\*" = cavallo di Troia (parola oscurata dal filtro della trascrizione).
- Nella trascrizione mancano i timestamp dei minuti fra 1:00:00 e 1:01:08 (formato "1 ora N secondi"): i riferimenti in quella fascia sono approssimati.
# Lezione 5 2026
## Divergenze
- **GDPR e cittadinanza.** Il docente ripete che il GDPR si applica in base alla cittadinanza europea dell'interessato, in tutti i paesi che "riconoscono il diritto dell'Unione", e costruisce su questo l'esempio del menù a tendina. Come già corretto nei manuali 2025 (cap. 02 e cap. 05, sez. 9): l'ambito territoriale (art. 3 GDPR) dipende dallo stabilimento del titolare nell'UE o, per titolari extra UE, dal fatto che l'interessato **si trovi nell'Unione** quando gli si offrono beni o servizi o se ne monitora il comportamento; non dalla cittadinanza. Per l'esame fa fede la formulazione del docente, ma è bene sapere che non è quella normativa. (Teams 5b @ 0:16:17 - 0:18:48)
- **Correzione: DPO obbligatorio per dimensione.** Il docente dice di nuovo che il DPO è obbligatorio per le PA e per le aziende "di una certa grandezza" o che fanno trattamenti automatizzati. L'art. 37 GDPR non usa la dimensione: obbligo per autorità e organismi pubblici e per chi, come attività principale, fa monitoraggio regolare e sistematico su larga scala o tratta su larga scala categorie particolari di dati o dati giudiziari. Stessa correzione del manuale 2025. (Teams 5b @ 0:23:21 - 0:23:58)
- **Medico esterno a partita IVA "responsabile" e "corresponsabilità".** Qualificazione incerta sul piano giuridico: un professionista esterno può essere responsabile del trattamento (art. 28) se agisce per conto dell'ospedale, oppure titolare autonomo o contitolare (art. 26) a seconda di chi determina finalità e mezzi. "Corresponsabilità" non è un termine del GDPR; il più vicino è la contitolarità. Da non riprendere fuori dal contesto dell'esame. (Teams 5b @ 0:22:33 - 0:23:05)
- **Opt-in "per tutto" di default.** Il GDPR richiede consenso esplicito e attivo quando la base giuridica è il consenso, e la protezione dei dati per impostazione predefinita (art. 25); non tutti i trattamenti però si basano sul consenso (contratto, obbligo legale, legittimo interesse). La regola "tutto opt-in di default" è una semplificazione. (Teams 5b @ 0:29:03 - 0:29:36)
- **Zero-day al momento della pubblicazione.** In Teams 4 la zero-day è definita come vulnerabilità scoperta perché già sfruttata; in Teams 5b il docente dice "al momento dello zero day, al momento della pubblicazione" della vulnerabilità viene assegnato il numero CVE, confondendo zero-day con il giorno di pubblicazione. Vale la definizione di Teams 4. (Teams 5b @ 0:59:58)
- **Correzione: il G7 non "impone".** Il docente dice che il G7 nel 2018 "ha imposto" segretezza, gruppo di controllo ristretto, scenari basati sulla minaccia. Il documento *G7 Fundamental Elements for Threat-Led Penetration Testing* (ottobre 2018) è non vincolante: raccomanda, non impone. L'obbligo di TLPT per le entità finanziarie UE viene da DORA (Reg. UE 2022/2554). Nel 2025 il docente aveva detto correttamente "ha consigliato". (Teams 5b @ 1:22:31)
- **TLP "inventato" dal FIRST.** Ripetuto come nel 2025; vale la nota del manuale 2025 (nato in ambito governativo britannico, standardizzato dal FIRST, versione 2.0 dell'agosto 2022). (Teams 5b @ 0:44:15)
- **TLP a quattro o cinque livelli.** Il docente dice "questi quattro, o meglio questi cinque livelli": coerente con il 2025 (CLEAR, GREEN, AMBER, AMBER+STRICT, RED). (Teams 5b @ 0:48:54)
- **Netflix su AWS.** Ripete che Netflix trasmette i contenuti usando il cloud di Amazon; vale la nota del manuale 2025 (backend su AWS, video soprattutto sulla CDN propria Open Connect). (Teams 5b @ 0:10:42)
## Punti incerti
- \[?\] "L'anno scorso è successo in occasione di un bug nel protocollo DNS, due o tre anni fa ci fu un grande down del cloud AWS in America" (Teams 5b @ 0:09:06). L'evento DNS "dell'anno scorso" è verosimilmente il disservizio AWS di ottobre 2025 nella regione us-east-1, legato alla risoluzione DNS; non è chiaro quale sia il down "di due o tre anni fa". La frase precedente attribuisce i down ad attacchi DoS, mentre l'esempio DNS è un guasto, non un attacco.
- \[?\] "Una traduzione, ma... cronica, dall'inglese" (Teams 5b @ 0:33:59): probabilmente "anacronistica" o "acritica"; il senso è che "classificazione" ricalca l'inglese *classified*.
- \[?\] "Dall'Italia come vengo dal Gibuti ... scrivo Iraq ... che sono iraniano" (Teams 5b @ 0:17:23 - 0:18:30): il docente passa da Iraq a "iraniano", lapsus o errore di trascrizione; non cambia il senso.
- \[?\] "Questo per prevenire possibili attacchi di phishing di cui parleremo tra poco" (Teams 5b @ 0:43:46): nel 2025 il phishing era già trattato (cap. 04); non è chiaro se nel 2026 sia stato fatto prima (lezioni 1-3 non analizzate qui) o se sia in programma dopo.
- \[?\] "Ne avevamo parlato all'inizio del corso" riferito al red teaming (Teams 5b @ 1:17:58): nei manuali 2025 disponibili il red team compare solo nel cap. 07; forse nella lezione 1 2026 (e 2025, non disponibile).
- \[?\] "Se il data center è... la Norvegia e la Svezia" (Teams 5b @ 0:06:25): esempio del docente, non un caso specifico.
- Trascrizione corretta nel testo: "Traffic Life Protocol", "Cyber Flight Intelligence", "Cyber Trought Intelligence", "Cybertrate" = Traffic Light Protocol, Cyber Threat Intelligence; "tlp number" = TLP:AMBER; "aisac", "isac", "Isaac" = ISAC; "Redat" = Red Hat; "WA White box" = VA white box; "table stop" = tabletop; "red timing", "Purple timing", "Golden timing" = red/purple/golden teaming; "[tl.pt](http://tl.pt)", "Fred Light penetration test" = TLPT, Threat-Led Penetration Test; "wana Cry" = WannaCry; "AVS" = AWS; "euci" = EUCI; "nos", "osi" = NOS, NOSI; "ciso" = CISO; "no piece Brosnan" = Pierce Brosnan (il film *For Your Eyes Only*, 1981, ha però come protagonista Roger Moore); "sequel" = SQL; "TPO" = DPO.
# Lezione 6 2026
## Divergenze
- **Frode del CEO:** nel 2025 il pretesto erano gli Emirati Arabi; nel 2026 la Cina, con indirizzo Gmail e telefono ritirato. Probabilmente due modi di raccontare lo stesso schema; nel 2026 è presentato come email reale vista in un corso. (Teams 6 @ 0:23:21)
- **Aneddoto John Cabot:** nel 2025 il presidente telefona per l'email di phishing; nel 2026 il presidente riceve una frode del CEO e chiede consiglio. (Teams 6 @ 0:26:57)
- **Vishing:** nel 2025 descritto solo come videochiamata (corretto nel manuale); nel 2026 "conversazione video o telefonica", ora in linea con la definizione standard. (Teams 6 @ 1:11:39)
- **Caratteri sostitutivi:** nel 2025 la "e" della tara e le "d"; nel 2026 il simbolo ∨, la "R" e le "m". Stessa email, dettagli diversi.
- **Correzione, hash della password inviato dal client.** Il docente dice che un sito vero invia al server "la password cifrata" o il suo hash. Nella prassi dei siti web la password viaggia in chiaro dentro il canale TLS (HTTPS) e l'hash con salt, calcolato con una funzione lenta, viene fatto **lato server**: se il client inviasse solo l'hash, quell'hash diventerebbe esso stesso l'equivalente della password. Lo stesso punto ritorna in Teams 7 @ 0:50:39. (Teams 6 @ 1:05:59 - 1:06:47)
- **Precisazione normativa (Teams 6 @ 0:14:37).** "Soggetti importanti e critici, scusate, significativi e critici" ai sensi della NIS: la NIS2 (Direttiva UE 2022/2555) distingue soggetti **essenziali** e **importanti**. Inoltre il Cybersecurity Act (Reg. UE 2019/881) istituisce schemi di certificazione, per lo più volontari, più che obblighi di test per i produttori; il Cyber Resilience Act impone ai fabbricanti requisiti di sicurezza e di gestione delle vulnerabilità; il Digital Services Act impone alle piattaforme molto grandi valutazioni del rischio e audit indipendenti. Nessuno dei tre prevede TLPT come DORA. Il docente rinvia la materia a più avanti.
- **Typosquatting:** la trascrizione riporta "facelock"; la slide, come nel 2025, mostra `facelook.com`.
## Punti incerti
- Contenuto della domanda iniziale non registrata (vedi sopra).
- Identità del fornitore di pagamenti elettronici colpito: il docente non la dice e avverte che le notizie a ridosso possono essere imprecise.
- Dominio del link dell'email John Cabot: trascritto "[oomenod.com](http://oomenod.com)"; nel manuale 2025 (da OCR) `oo-d.com`. \[?\]
- Il docente dice che il dominio risulta su "Have I Been Pwned" come usato in campagne criminali: quel servizio raccoglie soprattutto violazioni di account, non domini malevoli; forse intendeva un altro servizio di reputazione. \[?\] (Teams 6 @ 0:46:19)
- Passaggio audio disturbato a 1:16:47 - 1:17:13 ("servizio nativo ... chiave di cifratura che viaggia in tutti gli altri clienti"): il senso sembra che la rete condivisa non isoli i client né usi chiavi per cliente, ma la frase è incompleta.
# Lezione 7 2026
## Divergenze
- **Correzione, password e hash lato client (Teams 7 @ 0:50:39 - 0:51:52).** Nei siti web la password viene di norma inviata al server dentro il canale TLS e l'hash con sale viene calcolato **lato server** con funzioni lente (bcrypt, scrypt, Argon2, PBKDF2). Se il client inviasse solo l'hash, l'hash diventerebbe l'equivalente della password e il furto del database permetterebbe l'accesso diretto. Il concetto corretto, e importante, è che il server memorizza l'hash salato e non la password.
- **Correzione, il sale (Teams 7 @ 0:54:36).** "Nonce" viene da *number used once*, non da "secret number used once"; e il sale **non è segreto**, come del resto il docente dice poco dopo (memorizzato in chiaro). Il sale serve a rendere diversi gli hash della stessa password e a impedire tabelle precalcolate, non a nascondere qualcosa.
- **Correzione, "i" e "j" (Teams 7 @ 0:47:10).** In ASCII "i" è 0x69 (01101001) e "j" è 0x6A (01101010): differiscono per **due** bit, non uno. Il senso della dimostrazione (piccolo cambiamento, digest completamente diverso) non cambia.
- **Nota, MD5.** Il docente cita `md5sum` come strumento da terminale: MD5 è rotto per le collisioni e non va usato per garantire integrità contro un avversario; per l'esercizio sono preferibili `sha256sum` (Linux) o `shasum -a 256` (macOS, dove `md5sum` di norma non è presente e il comando è `md5`). (Teams 7 @ 0:48:30)
- **Correzione, Rossignol (Teams 7 @ 0:15:05).** Il capo delle spie di Elisabetta I che sventò il complotto di Babington (1586) fu **Francis Walsingham**; **Antoine Rossignol** fu il crittografo di Luigi XIV (*Grand Chiffre*). La slide 2025 riportava entrambi correttamente.
- **Correzione, Turing e il computer (Teams 7 @ 0:07:20 e 0:18:13).** Come già nel manuale 2025: la macchina usata contro Enigma (la Bombe) era elettromeccanica e specializzata, non una realizzazione della macchina di Turing né "il computer". Anche "Enigma prodotta dai nazisti" va precisato: la versione commerciale è del 1923, adottata poi dalle forze armate tedesche.
- **Correzione, struttura delle chiavi RSA (Teams 7 @ 1:12:42 - 1:13:45).** In RSA la chiave pubblica è la coppia (n, e), con n = p·q; la chiave privata è l'esponente d (in pratica si conservano anche p e q). I due primi p e q sono scelti casualmente e di dimensione simile, non sono "primi gemelli": due primi gemelli (che differiscono di 2) renderebbero n banalmente fattorizzabile (metodo di Fermat). È vero invece che conoscere un fattore di n permette di ricavare la chiave privata.
- **Correzione, RSA come azienda (Teams 7 @ 1:15:24).** RSA Security fu acquisita da EMC (2006), e con EMC passò a Dell (2016), ma nel 2020 Dell l'ha ceduta a un consorzio di investitori (STG, Ontario Teachers', AlpInvest). Oggi non è il braccio crittografico di Dell.
- **Correzione, equazione delle curve ellittiche (Teams 7 @ 1:21:47).** La forma usata in crittografia è y² = x³ + ax + b (forma di Weierstrass ridotta), non "y² = ax³ + x + b". "Modulo p" significa che i calcoli avvengono nel campo finito degli interi modulo p, cioè si cercano le coppie (x, y) per cui y² e x³ + ax + b sono congrui modulo p; non "soluzioni che divise per p danno resto zero".
- **Correzione, equivalenze RSA/ECC (Teams 7 @ 1:27:09 - 1:28:08).** Secondo il NIST (SP 800-57): RSA-2048 ≈ 112 bit di sicurezza ≈ ECC-224; RSA-3072 ≈ ECC-256 (128 bit); RSA-15360 ≈ ECC-512 (256 bit). RSA-4096 è ben lontano da ECC-512. Inoltre il passaggio "fattore 8 nei bit, 10\^8 volte più complicato" non ha fondamento: i due algoritmi poggiano su problemi diversi e la difficoltà non si confronta così. Il principio (chiavi ECC molto più corte a parità di sicurezza) resta corretto.
- **Lapsus.** "Nel caso della crittografia asimmetrica sono quell'unica chiave simmetrica" (1:07:02) va letto "simmetrica"; "curve ellittiche... sempre gli algoritmi a chiave simmetrica" (1:19:25) va letto "a chiave pubblica".
- **Rispetto al 2025:** l'analogia del doblone con la B diventa la moneta da 1 euro; il one-time pad passa da nota aggiunta a citazione del docente; il 2025 dedicava più spazio a crittologia/crittoanalisi e alla KDF, il 2026 non le riprende e si concentra su hash, sale, RSA ed ECC.
## Punti incerti
- **Notizia della sfida RSA (Teams 7 @ 1:15:43 - 1:16:24):** la RSA Factoring Challenge è stata ufficialmente chiusa nel 2007 e i premi non vengono più pagati; la notizia di settembre 2026 citata dal docente (numero di poche centinaia di bit fattorizzato, "premio riscosso") non è verificabile qui. \[?\]
- **L'intuizione su Enigma (Teams 7 @ 0:18:58):** il docente dice che le prime lettere indicavano la sigla dell'operatore. Nel film e nella storia il punto chiave furono soprattutto le frasi prevedibili nei messaggi (i *crib*, per esempio bollettini meteo e formule di saluto); anche le abitudini degli operatori furono sfruttate. Non è chiaro a quale dei due aspetti si riferisca. \[?\]
- **Lunghezze di chiave RSA (Teams 7 @ 1:16:40):** trascritto "2048 quando non già 2046 4096": probabilmente "3072 o 4096". \[?\]
- **Tabella delle collisioni (Teams 7 @ 0:42:27):** il docente non è sicuro che la tabella provenga da SHA ("non sono sicuro che la tabella provenga dallo..."); lunghezze trascritte "32, 64, 160".
- **Titolo del corso nella slide:** lettura da screenshot a bassa risoluzione, non verificata.
