# Edizione 2026: organizzazione, esame e contenuti nuovi

> Fonte Notion: https://app.notion.com/p/3e812abc808d813aae39e758113136c3 — ultima modifica 2026-09-27T11:03:32.876Z

Sintesi dell'edizione **2026** del corso dalle registrazioni Teams (sola visualizzazione, riassunte). Le lezioni 2026 sono 7 (7-15/09/2026) e hanno un taglio diverso dal 2025: i contenuti propri di Cybersecurity finiscono con la lezione 6; la lezione 7 è un "ponte" sulla crittografia verso il corso Digital Identities and Trust Services. Diversi temi che nel 2025 erano nel corso (kill chain, IA nella sicurezza, CTI avanzata, DoS, ransomware in parte) sono rimandati al **master di secondo livello**. Le integrazioni puntuali sono in fondo a ciascun capitolo, nella sezione "Integrazioni Teams 2026"; la lezione 1 2026 è il capitolo 01.
## Esclusioni esplicite dall'esame (2026)
- Elenco degli incidenti 2000-2020, slide "A data security retrospective" (Teams 1 @ 0:14:30)
- Slide sui domini della cybersicurezza (Teams 2 @ 0:53:01)
- Tipologie di controlli ambigue (Teams 4 @ 0:39:09)
- IaaS/PaaS/SaaS, rimandati al corso cloud (Teams 4 @ 1:19:53)
- Livelli di classificazione e loro equivalenze (Teams 5b @ 0:39:38)
Nessuna registrazione 2026 contiene modalità d'esame, scadenze o bibliografia. Nella lezione 6 il docente recupera "la domanda iniziale" (Teams 6 @ 1:25:22), ma la domanda non è nella registrazione.
# Lezione 1 2026 (Teams 1)
## Esame e organizzazione
- **Esclusione esplicita:** l'elenco degli incidenti 2000-2020 (slide "A data security retrospective", due pagine) "non sarà oggetto di esame" (Teams 1 @ 0:14:30).
- **Obiettivo del corso:** formare data analyst consapevoli dei concetti principali di sicurezza e capaci di applicarli ai dati, non esperti di sicurezza (Teams 1 @ 0:49:21). Da qui l'insistenza su contesto, igiene cibernetica e costo dei controlli.
- **Due corsi con lo stesso docente:** questo è il "primo corso"; il "secondo corso che vedrete con me" ne è l'evoluzione ed è centrato sulle identità digitali applicate all'analisi dei dati (Teams 1 @ 0:04:24; "tutti questi corsi che vedrete con me", Teams 1 @ 0:07:05).
- **Rapporto con il master di secondo livello (novità 2026):** il docente rinvia esplicitamente al master di secondo livello:
	- CERT e Red Team, "se non nel primo corso" (Teams 1 @ 0:03:52);
	- approfondimento di "fare sistema" con temi di cyber intelligence, "soprattutto per chi rimarrà per il master di secondo livello" (Teams 1 @ 0:13:30);
	- DoS e ransomware, "poi li vedremo nel corso del master di secondo livello" (Teams 1 @ 0:23:40);
	- la triade dell'informazione tornerà nel secondo livello parlando di cyber intelligence (Teams 1 @ 0:56:27).
	Però a Teams 1 @ 1:14:17 dice che il ransomware si vedrà "la prossima o le prossime lezioni". Nel 2025 tutti questi temi erano nel corso di primo livello: il perimetro d'esame 2026 va verificato sulle lezioni 2026 successive.
- **Argomenti annunciati:** differenza fra sicurezza informatica e cybersicurezza "più avanti" (Teams 1 @ 0:49:36); data governance "brevemente" (Teams 1 @ 0:03:15); crittografia (Teams 1 @ 1:08:18).
- **Calendario:** "ci sentiamo domani" (Teams 1 @ 1:25:41), quindi lezione l'8/09/2026; la parte tassonomica prosegue oltre questa lezione (Teams 1 @ 0:53:54).
- **Nessuna indicazione** su modalità, date, consegne, materiali o bibliografia. Nessuna domanda degli studenti registrata.
# Lezione 2 2026 (Teams 2)
## Esame e organizzazione
- **Esclusione esplicita:** la slide sui domini della cybersicurezza "non sarà oggetto d'esame". (Teams 2 @ 0:53:01)
- **Rapporto con l'altro corso:** la triade del digital trust sarà l'oggetto principale del corso sulle identità digitali e i servizi fiduciari; qui è anticipata perché rilevante in generale. (Teams 2 @ 0:00:25, 0:06:20)
- **Rapporto con il master di secondo livello:** degli ISAC si parlerà di più "nelle lezioni specifiche per il secondo livello". (Teams 2 @ 0:30:46)
- **Rimandi interni al corso:** cyber threat intelligence e ISAC più avanti (Teams 2 @ 0:32:25); rischio calcolato in pratica con la sicurezza organizzativa (Teams 2 @ 0:24:46); computer quantistici più avanti (Teams 2 @ 0:43:49); test di sicurezza e resilienza più avanti (Teams 2 @ 0:32:41); caso del governo tedesco "ne parleremo più avanti" (Teams 2 @ 0:52:01).
- **Crittografia nel master:** è uno degli argomenti principali di più corsi, non solo di quelli del docente. (Teams 2 @ 0:04:35)
- **Struttura del corso:** il focus di entrambi i moduli (primo e secondo) è la cyber security, con alcuni aspetti di sicurezza informatica. (Teams 2 @ 0:36:42)
- **Registrazione incompleta:** la registrazione parte a lezione avviata; il docente fa riferimento a una domanda di uno studente non registrata (Teams 2 @ 0:18:34) e a una domanda fatta "in passato" che "non è registrata nel corso" (Teams 2 @ 0:54:52).
- Nessuna indicazione su modalità d'esame, date o consegne.
---
## Contenuti nuovi senza capitolo 2025
### Il ruolo del CISO e la percezione della sicurezza come centro di costo
Assente nei manuali 2025 (che in sezione 7 parlano di governance solo in termini di ruoli e responsabilità). Punti chiave (Teams 2 @ 0:58:41 - 1:01:34):
- la cybersicurezza è spesso vista come puro costo perché il ritorno dell'investimento non è misurabile quando le cose vanno bene;
- la governance richiede una linea di reporting, di management e di spesa;
- il CISO può mancare, essere ad interim (CIO, CTO), stare sotto CIO o CTO, oppure essere un vero C-level che parla con il board;
- deve saper tradurre requisiti e scenari di rischio per il vertice.
### Supply chain software: Log4j, XZ, SBOM, DORA
Nel 2025 i supply chain attack erano trattati con SolarWinds, 3CX, MOVEit (capitolo 04, sezione 11), senza Log4j, XZ, SBOM né l'obbligo DORA sul registro dei fornitori. Qui il focus è la **non conoscibilità** delle dipendenze e il "conosci te stesso" come terza leva di difesa (Teams 2 @ 1:10:58 - 1:18:23).
---
# Lezione 3 2026 (Teams 3)
## Esame e organizzazione
- **Master di secondo livello:** l'elenco più avanzato degli attori della minaccia sarà trattato "nel modulo del secondo livello sulla Cyber Threat Intelligence". (Teams 3 @ 0:46:01)
- **Rimandi interni:** terminologia di malware più complessa nella parte di cyber threat intelligence (Teams 3 @ 0:16:49); ruolo degli script kiddie per attori organizzati ripreso nella parte di cyber intelligence (Teams 3 @ 0:52:49); keylogger hardware nascosti nei laptop più avanti nel corso (Teams 3 @ 0:24:30).
- **Struttura:** con questa lezione il docente dichiara di concludere "la parte tassonomica del corso" (terminologia). (Teams 3 @ 0:00:21)
- **Tempi:** a fine lezione dice di aver recuperato i minuti persi in precedenza; seguono domande non registrate. (Teams 3 @ 1:29:02 - 1:29:18)
- **Riferimenti alla lezione 1 2026:** Stuxnet e la chiavetta lanciata oltre il muro erano stati raccontati nella prima lezione. (Teams 3 @ 1:10:16)
- Nessuna indicazione su modalità d'esame, date o consegne.
---
## Contenuti nuovi senza capitolo 2025
### Come si muove un attaccante in una rete sconosciuta
Nessun manuale 2025 tratta questo punto (il capitolo 04, sezione 16, parla di pivoting ma dal lato della rete). Sintesi (Teams 3 @ 1:25:43 - 1:28:56):
- l'attaccante, umano o automatico, spesso non conosce la topologia della rete in cui è atterrato;
- la ricostruisce passo dopo passo (fog of war), spesso con strumenti che la mappano automaticamente;
- sa grosso modo dove si trovano i "gioielli" (per esempio le ricette segrete) ma deve trovare il percorso, tornando indietro quando sbaglia;
- ogni passo falso è un'occasione di rilevamento, quindi conta lavorare "sottotraccia";
- le mappe di rete interne sono un obiettivo in sé.
### Miner fraudolenti come uso tipico delle botnet
Il capitolo 03 del 2025 parla di botnet soprattutto per DDoS; il cryptomining con rilevamento dell'inattività dell'utente e l'aneddoto del contatore elettrico sono nuovi (Teams 3 @ 0:34:11 - 0:36:05).
---
# Lezione 4 2026 (Teams 4)
## Mappatura per contenuto sui capitoli 2025
<table header-row="true">
<tr>
<td>Blocco Teams 4</td>
<td>Intervallo</td>
<td>Capitolo 2025</td>
</tr>
<tr>
<td>VPN</td>
<td>0:00:03 - 0:11:06</td>
<td>Cap. 05, sez. 3</td>
</tr>
<tr>
<td>Surface, deep e dark web, Tor</td>
<td>0:11:11 - 0:17:47</td>
<td>Cap. 05, sez. 4</td>
</tr>
<tr>
<td>Sicurezza amministrativa: T&C, contratti, NDA, assicurazioni</td>
<td>0:17:53 - 0:22:24</td>
<td>Cap. 05, sez. 10</td>
</tr>
<tr>
<td>Gestione del rischio</td>
<td>0:22:32 - 0:31:25</td>
<td>Cap. 05, sez. 11</td>
</tr>
<tr>
<td>BCP e DRP</td>
<td>0:31:34 - 0:36:59</td>
<td>Cap. 05, sez. 12</td>
</tr>
<tr>
<td>Tipi di controlli, difesa a strati</td>
<td>0:37:04 - 0:47:39</td>
<td>Cap. 06, sez. 6</td>
</tr>
<tr>
<td>Aneddoto audit, compliance, certificazioni</td>
<td>0:47:39 - 0:57:27</td>
<td>Cap. 06, sez. 1-3</td>
</tr>
<tr>
<td>Sicurezza delle applicazioni, analisi statica e dinamica, DevSecOps</td>
<td>0:57:27 - 1:04:52</td>
<td>Cap. 05, sez. 5</td>
</tr>
<tr>
<td>CVE, responsible disclosure, zero-day, Patch Tuesday</td>
<td>1:04:52 - 1:15:38</td>
<td>Cap. 05, sez. 6</td>
</tr>
<tr>
<td>Sicurezza del cloud, IoT, VM, hopping</td>
<td>1:15:51 - 1:23:16</td>
<td>Cap. 05, sez. 7</td>
</tr>
</table>
Rispetto al 2025 l'ordine è diverso: la sicurezza amministrativa (rischio, BCP/DRP, controlli, compliance) viene PRIMA di applicazioni e cloud, e compliance e tipi di controlli, che nel 2025 aprivano la lezione 6, sono anticipati qui. La data governance, che nel 2025 seguiva il cloud nella stessa lezione, slitta alla lezione 5 del 2026. La lezione parte direttamente dalle VPN: la parte su reti e modello a strati (cap. 04, sez. 15-17) è stata evidentemente trattata nella lezione 3 del 2026 ("lo stack di rete che abbiamo visto nella scorsa lezione", 0:02:02).
## Esame e organizzazione
- **Tipi di controlli: niente domande sulle tipologie ambigue.** "Se ci fossero domande d'esame, comunque non ci saranno riguardo a tipologie un po' ambigue, che in alcuni schemi si chiamano in un modo e in altri schemi si chiamano in un altro, quindi state tranquilli." Il docente usa la tassonomia più semplice. (Teams 4 @ 0:39:09)
- **IaaS, PaaS, SaaS non oggetto d'esame.** "So che fate un corso cloud, quindi non mi dilungo sulle differenze tra IaaS, PaaS e SaaS che non saranno oggetto d'esame"; invita ad andarle a vedere nel corso cloud. (Teams 4 @ 1:19:53)
- **Master di secondo livello / secondo modulo.** Nuova informazione organizzativa, assente nei manuali 2025: il docente rimanda più volte alla "parte del master di secondo livello":
	- la catena della compromissione (kill chain) "nella parte del secondo livello del master di secondo livello" (Teams 4 @ 0:38:45);
	- gli usi dell'intelligenza artificiale nella sicurezza, "nel secondo modulo", con "una sezione dedicata nel master di secondo livello" (Teams 4 @ 1:13:35);
	- l'approfondimento sul trend delle CVE "nel master di secondo livello" (Teams 4 @ 1:15:38).
	Nel 2025 kill chain (cap. 07) e IA (cap. 06, sez. 7-8) erano parte di questo corso: nel 2026 sembrano spostati fuori dal primo livello. Da verificare con il programma ufficiale prima di escluderli dallo studio.
- **Crittografia rinviata.** La cifratura sarà trattata "nel corso sui servizi fiduciari" (Teams 4 @ 0:06:35); la firma elettronica semplice "vedremo" (Teams 4 @ 0:19:02).
- **Calendario.** La lezione chiude con qualche minuto di anticipo per non iniziare un argomento più complesso, rinviato a "domani" (11/09/2026, Lezione 5). Nessuna domanda degli studenti. (Teams 4 @ 1:23:24 - 1:23:40)
## Contenuti nuovi senza capitolo 2025
- **Tassonomia a strati dei controlli (parallelo/serie).** Vedi sopra, cap. 06 sez. 6: è la parte concettualmente più nuova, collegata alla catena della compromissione, che però viene rinviata al secondo livello del master. (Teams 4 @ 0:37:04 - 0:38:45)
- **Analisi statica/dinamica, sandboxing, fuzzing.** Non presenti nei manuali 2025 come categorie. (Teams 4 @ 1:01:08 - 1:03:02)
- **Zero-day come categoria definita** e concetto di vulnerabilità "N giorni". Nel 2025 le zero-day comparivano solo come icona sulla slide CVE. (Teams 4 @ 1:10:29 - 1:12:05)
- **Effetto dell'IA generativa sul numero di CVE** e sul concatenamento di vulnerabilità, con i dati 2025 e inizio 2026. (Teams 4 @ 1:05:25, 1:12:16 - 1:13:35)
# Lezione 5 2026 (Teams 5b)
## Le due registrazioni
<table header-row="true">
<tr>
<td></td>
<td>Teams 5a</td>
<td>Teams 5b</td>
</tr>
<tr>
<td>File</td>
<td>"... Lezione 5-20260911_180310-Registrazione della [riunione.mp](http://riunione.mp)4"</td>
<td>"... Lezione 5-20260911_180403-Registrazione della [riunione.mp](http://riunione.mp)4"</td>
</tr>
<tr>
<td>Data e ora di inizio</td>
<td>11/09/2026, 18:03:10</td>
<td>11/09/2026, 18:04:03</td>
</tr>
<tr>
<td>Durata</td>
<td>0:00:43</td>
<td>1:29:44 (trascrizione fino a 1:29:26)</td>
</tr>
<tr>
<td>Trascrizione</td>
<td>assente</td>
<td>presente</td>
</tr>
<tr>
<td>Contenuto</td>
<td>solo la slide di sezione "Data Protecion, Classification and Governance" (refuso della slide), nessun parlato trascritto</td>
<td>lezione completa</td>
</tr>
</table>
Verifica: la 5a dura 43 secondi, non ha trascrizione e mostra la stessa slide con cui si apre la 5b; la 5b parte 53 secondi dopo l'inizio della 5a. È quindi confermato che la registrazione è stata riavviata e che tutto il contenuto è nella 5b. Nel seguito tutti i riferimenti sono "Teams 5b".
- **Fonte:** trascrizione automatica Microsoft consultata in pagina (solo visualizzazione), riassunta.
## Mappatura per contenuto sui capitoli 2025
<table header-row="true">
<tr>
<td>Blocco Teams 5b</td>
<td>Intervallo</td>
<td>Capitolo 2025</td>
</tr>
<tr>
<td>Data governance, sovranità, forensics nel cloud, geopolitica dei data center</td>
<td>0:00:04 - 0:15:18</td>
<td>Cap. 05, sez. 8 (e sez. 7, fault domain)</td>
</tr>
<tr>
<td>GDPR, ruoli, DPO</td>
<td>0:15:24 - 0:26:40</td>
<td>Cap. 05, sez. 9</td>
</tr>
<tr>
<td>Opt-in/opt-out, permessi delle app</td>
<td>0:26:40 - 0:33:43</td>
<td>Cap. 05, sez. 9</td>
</tr>
<tr>
<td>Classificazione dei dati, NOS, DLP</td>
<td>0:33:43 - 0:43:59</td>
<td>Cap. 06, sez. 4</td>
</tr>
<tr>
<td>Traffic Light Protocol</td>
<td>0:43:59 - 0:57:07</td>
<td>Cap. 06, sez. 5</td>
</tr>
<tr>
<td>Vulnerability and patch management, VA, PT</td>
<td>0:57:20 - 1:13:17</td>
<td>Cap. 07, sez. 9 (e cap. 05 sez. 6, cap. 06 sez. 6)</td>
</tr>
<tr>
<td>Cyber resilienza: tabletop, red, purple, golden teaming, TLPT</td>
<td>1:13:17 - 1:29:26</td>
<td>Cap. 07, sez. 10</td>
</tr>
</table>
Rispetto al 2025: la lezione unisce la coda della lezione 5 (governance, GDPR), la parte centrale della lezione 6 (classificazione, TLP) e le verifiche di sicurezza della lezione 7 (cap. 07, sez. 9-10). Nel 2026 sono assenti, fra le due lezioni 4 e 5, i blocchi 2025 su IA e sicurezza (cap. 06, sez. 7-8), cyber intelligence, OSINT, TTP, ATT&CK, kill chain, Diamond Model (cap. 06 sez. 9-14, cap. 07 sez. 1-8) e crittografia (cap. 07 sez. 11-17): coerente con i rimandi al "secondo modulo" e al corso sui servizi fiduciari (vedi Esame e organizzazione). Non sono trattati Data Space, Data Governance Act, policy cloud ACN per la PA (ordinario/critico/strategico) e ruoli owner/steward/custodian.
## Esame e organizzazione
- **Classificazione di riservatezza: niente domande su livelli ed equivalenze.** "Non ci saranno domande d'esame su questo argomento, o meglio non ci saranno domande sulla definizione dei livelli di classificazione o sulla loro equivalenza, è un argomento specifico." Il docente aggiunge di aver solo fatto copia e incolla dai siti ufficiali. (Teams 5b @ 0:39:38)
- **Slide riservate agli studenti di questa edizione.** "Le slide di questo corso non sono TLP:CLEAR perché sono riservate solo a voi studenti di questa edizione di questo corso. Non le potete dare a nessun altro." Non portano l'etichetta TLP perché non sono informazioni di cyber threat intelligence. Rilevante anche per l'uso dei manuali 2025 e di queste note: vanno tenuti per uso personale. (Teams 5b @ 0:49:54 - 0:50:12)
- **Secondo modulo.** Altri rimandi espliciti a un secondo modulo:
	- gli attacchi DoS ai cloud provider "li vedremo nella seconda parte" (Teams 5b @ 0:08:50);
	- la cyber threat intelligence "come vedremo poi nel secondo modulo" (Teams 5b @ 0:44:44);
	- come gli attaccanti capiscono di essere tracciati "vi spiegherò nel secondo modulo" (Teams 5b @ 0:57:07).
	Insieme ai rimandi di Teams 4 al "master di secondo livello" (kill chain, IA nella sicurezza, CVE), indicano che nel 2026 CTI, kill chain e IA non fanno parte di questo modulo. Da confermare sul programma ufficiale.
- **Scopo della parte sulle verifiche.** "Spero che risponda a un po' di domande che avete fatto": vocabolario per data analyst, non competenze da sicurista. (Teams 5b @ 0:57:20 - 0:57:35)
- **Fine lezione.** La trascrizione termina con "Ci sono domande" a 1:29:26; nessuna domanda trascritta. Nessuna indicazione su data o modalità d'esame in questa lezione.
- **Registrazione doppia.** La 5a (43 s) è un avvio a vuoto; non contiene nulla da studiare.
## Contenuti nuovi senza capitolo 2025
- **Forensics nel cloud, catena di custodia, CTU.** Tema non presente nei manuali 2025, che trattavano la sovranità solo come rogatoria e trasferimento del dato. (Teams 5b @ 0:02:04 - 0:08:10)
- **Geopolitica delle dorsali e dei data center** (mappa generata con Copilot, cavi verso Africa e India, potere politico dei CSP). (Teams 5b @ 0:10:01 - 0:15:18)
- **NOS e NOSI.** Nulla osta di sicurezza per persone e per aziende. (Teams 5b @ 0:36:10 - 0:37:00)
- **Vulnerability and Patch Management e asset management** come processo distinto dal VA. (Teams 5b @ 0:59:26 - 1:04:32)
- **Tabletop exercise** come prima forma di test di resilienza, con esempi di ISAC. (Teams 5b @ 1:14:04 - 1:17:58)
- **Pentest out-to-in.** (Teams 5b @ 1:10:11)
# Lezione 6 2026 (Teams 6)
## Esame e organizzazione
- **Esame:** nessuna indicazione in tutta la registrazione. Nessun riferimento bibliografico.
- **Domanda iniziale non registrata:** a 1:25:22 il docente dice di recuperare i minuti persi con "la domanda iniziale"; la registrazione non contiene né la domanda né la risposta. Se riguardava l'esame o l'organizzazione, va recuperata da chi era presente. (Teams 6 @ 1:25:22)
- **Chiusura del corso di Cybersecurity:** al termine il docente rimanda "alla prossima lezione, quando cominceremo il corso di identità digitale e servizi fiduciari". Questa è quindi l'ultima lezione dei contenuti propri di Cybersecurity; la lezione 7 fa da ponte (vedi teams-07). (Teams 6 @ 1:31:19 - 1:31:35)
- **Rapporto con il master di II livello:** l'uso dell'IA per individuare e filtrare email malevole e alcuni usi malevoli dell'IA in sicurezza saranno trattati "nel secondo livello". (Teams 6 @ 0:59:24)
- **Rimandi al corso Digital Identities and Trust Services:** protezione dei documenti d'identità (0:18:42), HTTPS (0:45:46), hash delle password e crittografia (1:06:16), documenti firmati (1:25:14).
- **Registrazioni riusate:** "per chi ci segue gli anni successivi" (0:17:18) e "trattandosi di una sessione registrata" non chiede l'aiuto degli studenti per l'esercizio (0:27:15).
- **Segnali di peso per lo studio:** la BIA "esula completamente dallo scopo di questo corso" (0:02:07), come nel 2025; la DPIA è collocata nel perimetro privacy/GDPR.
## Contenuti nuovi senza capitolo 2025
### Caso 2026: furto di documenti a un fornitore di pagamenti elettronici (Teams 6 @ 0:17:18 - 0:20:58)
- Il docente premette che per chi seguirà negli anni successivi sarà un incidente "dell'anno precedente", e che non fa il nome perché le informazioni diffuse a ridosso di un incidente non sono sempre esatte.
- Fatti riferiti: a un fornitore di servizi di pagamento elettronico (si corregge: "non di moneta elettronica") sono stati sottratti diversi gigabyte di scansioni di documenti d'identità dei clienti. L'attore li userà per assumere quelle identità o li venderà.
- Modalità, "a quanto sembra": nessuna violazione tecnica. Email di phishing che si spacciavano per un'**autorità di controllo** e chiedevano i dati con informazioni credibili; i dipendenti, per paura di sanzioni e per ottemperare a presunti obblighi normativi, hanno consegnato i dati in blocco attraverso un canale del tutto normale.
- Morale: gli attacchi diventano sempre più sofisticati e l'IA li farà crescere, ma il fattore umano resta l'anello più debole e più sfruttato. Rinvio al corso sull'identità digitale per l'importanza di proteggere questi dati.
### Phishing nell'era dell'IA (Teams 6 @ 0:52:22 - 0:57:23)
- Negli ultimi anni i tentativi di phishing generati con IA "di frontiera" sono moltissimi. Un'IA oggi non commetterebbe gli errori della email John Cabot: prende il logo dall'organizzazione e costruisce un'email graficamente perfetta.
- Tecnica di raccolta dei template: l'attore dialoga prima con il supporto tecnico del bersaglio per ottenere, anche dal secondo o terzo livello, un'email formale di una persona di alto grado, da cui copiare firma, font, colori, loghi.
- Evoluzione della lingua: vent'anni fa il phishing in italiano era quasi impossibile; poi traduttori automatici e sistemi di machine learning; da 5-6 anni i testi sono grammaticalmente corretti. L'indicatore residuo era il **tono**: chi scrive un falso atto istituzionale deve creare urgenza mantenendo il tono giusto, e spesso non ci riusciva.
- Esempio 2025: il falso "verbale d'arresto" della Polizia di Stato inviato da Gmail con PDF infetto. La Polizia non scriverebbe da Gmail; al massimo userebbe PEC, SEND o una notifica sull'app IO, "ma più probabilmente sarebbero venuti a casa".
# Lezione 7 2026 (Teams 7)
## Esame e organizzazione
- **Esame:** nessuna indicazione in tutta la registrazione. **Nessun riferimento bibliografico**, nessuna consegna, nessuna scadenza.
- **Non è l'ultima lezione:** il docente chiude con "riprenderei domani con qualche caso d'uso e qualche altro laboratorio con CyberChef". C'è quindi almeno una lezione successiva (presumibilmente 16/09/2026). L'ultima lezione dei contenuti propri di Cybersecurity è la Teams 6, che si chiude rimandando all'inizio del corso di identità digitale e servizi fiduciari; questa Teams 7 è la lezione ponte. (Teams 7 @ 1:29:03; Teams 6 @ 1:31:35)
- **Confine fra i corsi:** la crittografia è dichiarata argomento ponte fra Cybersecurity e Digital Identities and Trust Services; nel corso DITS il docente si sposterà sulla parte applicativa. Si dilunga meno sulla crittografia simmetrica perché gli studenti la fanno "in altri corsi di crittografia". (Teams 7 @ 0:00:06 - 0:01:00)
- **Rimandi espliciti al corso DITS:** firma digitale dietro le smart card (0:25:28), crittografia post-quantistica (0:31:35, 0:35:38), cripto-agilità come caratteristica fondamentale (0:33:32), considerazioni quantistiche su RSA e curve ellittiche (1:28:24).
- **Segnali di peso per lo studio:** i simboli matematici delle funzioni hash non vengono commentati, "non è questo l'oggetto del corso" (0:38:15); "questo non è un corso di CyberChef" (0:49:55); per le curve ellittiche "non è un corso di matematica" (1:20:52). Contano i concetti: proprietà delle hash, sale, rapporto fra chiave privata e pubblica, robustezza come antieconomicità, cripto-agilità.
- **Laboratorio da rifare a casa:** CyberChef, calcolo di impronte SHA-256 e verifica dell'effetto valanga. Invito, non consegna. (Teams 7 @ 0:45:18)
- **Master di II livello:** nessun riferimento in questa lezione (il riferimento è in Teams 6 @ 0:59:24).
## Contenuti nuovi senza capitolo 2025
### Funzioni di hash crittografico (Teams 7 @ 0:37:12 - 0:50:28)
- **Scelta didattica:** invece di partire dalla riservatezza, come fanno i testi, parte da **integrità** e autenticità, per mostrare che la crittografia non serve solo a nascondere. (0:37:12)
- **Definizione:** funzione che mappa un messaggio di lunghezza finita arbitraria in una stringa di **h bit** costante (lunghezza dell'impronta). L'output si chiama **digest**, ma nel gergo si dice "hash" anche per l'output. Formalismo matematico mostrato in slide ma non commentato ("non è questo l'oggetto del corso"). (0:38:00 - 0:40:02)
- **Proprietà elencate dal docente:**
	1. output di lunghezza costante;
	2. cambiando anche un solo bit dell'input il digest cambia radicalmente (effetto valanga);
	3. dato un digest è computazionalmente difficile trovare un messaggio che lo produce (resistenza alla preimmagine);
	4. dato un messaggio è computazionalmente difficile trovarne un secondo con lo stesso digest (resistenza alla seconda preimmagine / alle collisioni). (0:40:20 - 0:42:11)
- **Collisioni:** esistono sempre, perché la funzione non è iniettiva (infinite controimmagini); la robustezza consiste nel rendere antieconomico trovarle. Se un attaccante trova una collisione, l'impronta non prova più che il dato è integro. Più bit di output, codominio più grande, più difficoltà. Tabella in slide con h = 32, 64, 160 bit e le relative probabilità, riferita a versioni di SHA ormai deprecate. (0:42:11 - 0:44:57, 0:49:21)
- **Laboratorio CyberChef:** strumento online sviluppato dal GCHQ britannico, funziona lato client nel browser, installabile anche in locale, codice sorgente scaricabile. Dimostrazione con SHA-2 a 256 bit: cambiando "i" in "j" l'impronta cambia completamente. Da terminale Linux o macOS esistono comandi equivalenti (il docente cita `md5sum`). Il docente invita a rifare l'esercizio a casa, ma precisa: "non a me interessa che sappiate usare CyberChef", interessa poter replicare i concetti. (0:45:14 - 0:50:28)
- **Password memorizzate come hash.** Il server non deve conoscere la password in chiaro (esempio della pizzeria online che potrebbe ordinare pizze a nome del cliente). Secondo il docente il client calcola l'impronta, cancella la password dalla memoria e invia solo l'impronta; il server la confronta con quelle memorizzate. Vedi "Divergenze". (0:50:28 - 0:52:22)
- **Rischio del riuso delle password.** Un attaccante che viola un servizio poco protetto (la piccola pizzeria artigianale) ottiene email e hash; se lo stesso hash compare in un altro servizio sa che la password è riusata e può tentare l'accesso al PC di lavoro, alla posta, alla banca. (0:52:25 - 0:54:20)
- **Il sale.** A ogni creazione di password si genera un numero usato una sola volta (il docente lo chiama *nonce*), memorizzato **in chiaro** sul server insieme all'hash calcolato su nonce concatenato alla password. Non semplifica la forza bruta, ma la stessa password su due servizi produce hash diversi: chi compra nel dark web due archivi di password rubate non può dedurre il riuso. Aumenta il costo per l'attaccante e migliora la postura di sicurezza. Consiglio esplicito: non riusare password tipo "Walter123". (0:54:36 - 0:58:13)
### RSA (Teams 7 @ 1:11:33 - 1:19:18)
- Scelto come esempio perché è il più semplice e tra i più usati fra gli algoritmi non quantum-safe. Inventato da Rivest, Shamir, Adleman alla fine degli anni '70; poco implementato negli anni '80 per mancanza di potenza di calcolo, poi diffuso negli anni '90, 2000 e 2010.
- Spiegazione del docente: la chiave pubblica è il prodotto di due numeri primi molto grandi e comparabili; la privata è uno dei due fattori; trovato un fattore, l'altro si ottiene per divisione. Richiamo della scomposizione in fattori primi (6 = 3×2, 22 = 11×2, 33 = 11×3). Sapere che i fattori sono solo due semplifica la crittoanalisi, ma con numeri così grandi la fattorizzazione resta computazionalmente impossibile. Vedi "Divergenze" per la precisazione sulla struttura reale delle chiavi RSA.
- **Notizia settembre 2026:** secondo il docente, pochi giorni prima era uscita la notizia della fattorizzazione di un numero della sfida RSA, con premio riscosso, ma con poche centinaia di bit: lontano da RSA-1024, già deprecato da anni. Oggi si usa almeno RSA-2048, anche 4096, e si pensa di deprecare il 2048 nei prossimi anni. Vedi "Punti incerti".
- **Allungare la chiave o cambiare algoritmo?** In software allungare la chiave costa solo tempo di calcolo, e cambiare algoritmo è facile se la libreria lo supporta. Su una smart card raddoppiare i bit significa riprogettare il chip: più consumo, più lentezza, più costo. Può convenire passare a un algoritmo diverso che lavora con lo stesso numero di bit, per esempio da RSA alle curve ellittiche. Il docente dice di essersi occupato in passato di questa progettazione. (1:17:31 - 1:19:18)
### Crittografia a curve ellittiche (Teams 7 @ 1:19:25 - 1:29:03)
- Non è un solo algoritmo ma una famiglia; non tutte le curve sono adatte, come non tutti i primi sono adatti a RSA (devono poter essere generati casualmente senza che due utenti ottengano le stesse chiavi).
- Il docente precisa che non è un corso di matematica e che non è un crittoanalista di professione, pur essendosi occupato di curve ellittiche.
- Curva ellittica come luogo delle soluzioni di un polinomio di terzo grado in due variabili con coefficienti interi, considerato **modulo p** (p tipicamente primo); le soluzioni discrete si rappresentano come punti. Le curve con buone proprietà vengono parametrizzate e ricevono un nome: `secp256r1`, `secp256k1` e simili, con coefficienti e modulo pubblicati in tabelle standard.
- Problema matematico diverso da RSA: invece della fattorizzazione, il **logaritmo discreto**. L'esponenziale modulare è facile da calcolare, l'inverso è computazionalmente complesso.
- **Confronto con RSA:** a parità di robustezza le chiavi a curve ellittiche sono molto più corte. Il docente cita RSA-2048 ≈ ECC-256 e RSA-4096 ≈ ECC-512 (vedi "Divergenze").
- **Criterio di scelta:** RSA dove i dispositivi lavorano bene con molti bit e conviene una matematica più semplice; curve ellittiche dove lavorare con pochi bit è essenziale per efficienza e costo, accettando un'algebra più complessa. Considerazioni quantistiche rinviate al corso successivo. (1:28:08 - 1:29:03)
