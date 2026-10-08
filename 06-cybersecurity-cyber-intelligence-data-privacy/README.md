# Cybersecurity, Cyber Intelligence and Data Privacy

> Fonte Notion: https://app.notion.com/p/3e712abc808d81a6b6e5ecb419cc456a — ultima modifica 2026-09-27T12:47:16.815Z

Modulo del Master Data Analytics, docente **Walter Arrighetti**. Il corso copre i fondamenti della sicurezza delle informazioni (triadi, rischio, organizzazione della sicurezza, NIST CSF), la minaccia cyber (malware, attori, ransomware, ingegneria sociale), la sicurezza di rete, applicativa e cloud, data governance e GDPR, compliance, cyber threat intelligence, framework di analisi (MITRE ATT&CK, kill chain, Diamond Model) e un'introduzione alla crittografia, ripresa nel corso Digital Identities and Trust Services.
## Fonti
<table header-row="true">
<tr>
<td>Fonte</td>
<td>Uso</td>
</tr>
<tr>
<td>Registrazioni del portale `learn.master-data-analytics.it` (`CS-02` … `CS-08`), **edizione 2025** (Teams, settembre 2025)</td>
<td>**fonte di verità** del manuale</td>
</tr>
<tr>
<td>Materiale del docente</td>
<td>**nessuno**: il docente non distribuisce slide. Tutto ciò che è a schermo è letto dai fotogrammi</td>
</tr>
<tr>
<td>Registrazioni Teams 2026 (SharePoint, "Solo visualizzazione")</td>
<td>**integrate nei capitoli** (guida unica): riquadri "Integrazione Teams 2026" dentro la sezione a cui si riferiscono; la lezione 1 2026 è il capitolo 01. Le lezioni "MDA II Level" non sono incluse</td>
</tr>
</table>
> ⚠️ **Il portale carica file sbagliati.** La pagina "lezione 1" mostra un altro video (lo stesso di "lezione 8"); "lezione 7" dura 105 secondi (interrotta per un problema di condivisione schermo); "lezione 8" è la ripresa della lezione 7. Il docente dice che il corso finisce con quella lezione (`CS-08 @ 00:49:59`): le lezioni sono **7**, e **la lezione 1 (15/09/2025) non è disponibile**: il capitolo 01 la sostituisce con la lezione 1 dell'edizione 2026. I rimandi a "ieri" nella lezione 2 riguardano la lezione 1 2025.
## Come sono fatte queste pagine
Ogni capitolo segue una lezione per sezioni tematiche, con riferimenti `CS-0N @ hh:mm:ss`. Il testo delle slide è riportato fedelmente (in inglese se la slide è in inglese).
Convenzioni:
- `[?]`: parola non chiara nell'audio o contenuto dubbio
- `[illeggibile]`: schermo non leggibile
- **Nota aggiunta**: integrazione non detta a lezione
- **Correzione**: affermazione del docente imprecisa, dettagli nella pagina Divergenze
## Capitoli
<table header-row="true">
<tr>
<td>Capitolo</td>
<td>Data</td>
<td>Durata</td>
<td>Contenuto</td>
</tr>
<tr>
<td>01 - Introduzione (Teams 2026)</td>
<td>07/09/2026</td>
<td>01:25:41</td>
<td>Chi è il docente, perché la sicurezza in un master di data analytics (Davenport), von der Leyen, incidenti storici, Yahoo, CrowdStrike, attacchi OT/ICS, Stuxnet, cyberspazio come quinto dominio, triade CIA. Ricostruito da Teams 2026 (la lezione 1 2025 non è sul portale)</td>
</tr>
<tr>
<td>02 - Triadi, organizzazione della sicurezza, NIST CSF</td>
<td>16/09/2025</td>
<td>01:30:17</td>
<td>Triadi (controlli, minaccia, rischio, informazione), SOC/CSIRT/CERT/ISAC, NIST CSF 2.0, superficie d'attacco, perimetro</td>
</tr>
<tr>
<td>03 - Malware, attori della minaccia, botnet e ransomware</td>
<td>18/09/2025</td>
<td>01:35:45</td>
<td>Virus e malware, trojan, rootkit, spyware, RAT, kill chain, hacker e hacktivismo, APT, botnet, DDoS, ransomware</td>
</tr>
<tr>
<td>04 - Ransomware, ingegneria sociale e reti</td>
<td>19/09/2025</td>
<td>01:43:36</td>
<td>CaaS, estorsione multipla, insider, evil maid, social engineering, phishing (esercizio), supply chain, sicurezza fisica, Stuxnet, modello OSI</td>
</tr>
<tr>
<td>05 - Rete, applicazioni, cloud, data governance e rischio</td>
<td>22/09/2025</td>
<td>02:18:48</td>
<td>IDS/IPS/SIEM, VPN, dark web e Tor, OWASP, CVE/CVSS, cloud, data governance, GDPR, assicurazioni, rischio, BCP/DRP</td>
</tr>
<tr>
<td>06 - Compliance, AI e cyber intelligence</td>
<td>25/09/2025</td>
<td>01:56:08</td>
<td>ISO 27000, audit e assessment, classificazione dei dati, TLP, controlli, AI e attacchi all'AI, ciclo dell'intelligence, OSINT, CTI, attribuzione</td>
</tr>
<tr>
<td>07 - Framework di analisi, verifiche e crittografia</td>
<td>26/09/2025</td>
<td>00:01:45 + 01:10</td>
<td>MITRE ATT&CK, kill chain, Diamond Model, VA/PT, red/purple teaming, TLPT e DORA, storia e fondamenti della crittografia</td>
</tr>
</table>
## Qualità dell'audio
Ottima: logprob mediano circa −0.10. Né la soglia −0.6 né −0.3 discriminano; gli errori veri sono sigle e nomi propri trascritti con sicurezza ("XIRT" per CSIRT, "Fonderlion" per von der Leyen), corretti nel testo ed elencati in ogni capitolo.
## Dove sta il materiale
Sul Mac: `~/Work/Projects/data-science/data-analytics/60-cybersecurity-intelligence-privacy/`
- `video/CS-0N.mp4`: le registrazioni (CS-01 è un duplicato di CS-08)
- `out/lezione-0N/`: manuale e divergenze in markdown
- `out/CS-0N/`: trascrizioni, frame, OCR, triage
- `out/teams-2026/`: riassunti delle registrazioni Teams 2026 (nessuna trascrizione salvata)
- `scripts/`: pipeline

[Divergenze](divergenze.md)
[02 - Triadi, organizzazione della sicurezza, NIST CSF](02-triadi-organizzazione-della-sicurezza-nist-csf.md)
[06 - Compliance, AI e cyber intelligence](06-compliance-ai-e-cyber-intelligence.md)
[04 - Ransomware, ingegneria sociale e reti](04-ransomware-ingegneria-sociale-e-reti.md)
[03 - Malware, attori della minaccia, botnet e ransomware](03-malware-attori-della-minaccia-botnet-e-ransomware.md)
[05 - Rete, applicazioni, cloud, data governance e rischio](05-rete-applicazioni-cloud-data-governance-e-rischio.md)
[07 - Framework di analisi, verifiche e crittografia](07-framework-di-analisi-verifiche-e-crittografia.md)
[Assessment](assessment.md)
[01 - Introduzione (Teams 2026)](01-introduzione-teams-2026.md)
[Edizione 2026: organizzazione, esame e contenuti nuovi](edizione-2026-organizzazione-esame-e-contenuti-nuovi.md)
