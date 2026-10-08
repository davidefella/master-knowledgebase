# Biotech Data Processing

> Fonte Notion: https://app.notion.com/p/3e912abc808d81eeaeb4dbf1398ee05f — ultima modifica 2026-09-28T18:31:57.766Z

Modulo del Master Data Analytics, docente **Matteo Rucco** (Biocentis). Nonostante il nome, il corso è soprattutto di **modellistica di sistemi biologici complessi**: equazioni differenziali (Eulero, `odeint`), modelli ad agenti con MESA, Topological Data Analysis, epidemiologia computazionale, un'introduzione alla bioinformatica e gli algoritmi genetici. Tutte le esercitazioni sono in Python su Google Colab.
## Fonti
<table header-row="true">
<tr>
<td>Fonte</td>
<td>Uso</td>
</tr>
<tr>
<td>Registrazioni del portale `learn.master-data-analytics.it` (`BT-01` … `BT-06`), **edizione 2025** (novembre 2025)</td>
<td>**fonte di verità** del manuale</td>
</tr>
<tr>
<td>Slide: `Day1_v25.pdf`, `Math_in_biology.pdf`, `TDA.pdf` (portale e Teams), `ABMS.pdf` e `Biotech Data Processing Course Introduction.pdf` (solo Teams 2026)</td>
<td>contorno; testo delle slide riportato fedelmente</td>
</tr>
<tr>
<td>17 notebook Colab (Teams)</td>
<td>fonte dei blocchi di codice dove esistono: **codice dal notebook, sequenza ed errori dal video**</td>
</tr>
<tr>
<td>Registrazioni Teams 2026 ("Solo visualizzazione")</td>
<td>integrazioni dentro le sezioni dei capitoli; mappatura nella pagina Divergenze</td>
</tr>
<tr>
<td>`Test_Finale_BDP_26` (Teams)</td>
<td>traccia del test finale 2026, vedi **Assessment**</td>
</tr>
</table>
> ⚠️ **Mancano due giornate sul portale.** Il **Day 1** (introduzione) e il **Day 8** (lavoro guidato e test finale) non sono registrati. Il capitolo 00 è ricostruito dalle slide e dalla registrazione `Teams 1`. BT-06 si interrompe prima della lettura della traccia del test (`BT-06 @ 00:56:11`).
> ⚠️ **BT-02 contiene un segmento duplicato** (`00:20:05`-`00:25:05`, copia dell'inizio di BT-01): escluso dal capitolo 02.
> ⚠️ **Il programma nelle slide del Day 1 non coincide con l'ordine reale** (Day 4 "DIY on Modeling" è diventato TDA, genoma ed epidemiologia sono invertiti, il Day 7 non era previsto). I capitoli seguono le lezioni effettivamente tenute.
## Come sono fatte queste pagine
Ogni capitolo segue una lezione per sezioni tematiche, con riferimenti `BT-0N @ hh:mm:ss`. Il testo delle slide è riportato fedelmente (in inglese se la slide è in inglese).
Convenzioni:
- `[?]`: parola non chiara nell'audio o contenuto dubbio
- `[illeggibile]`: schermo non leggibile
- **Nota aggiunta**: integrazione non detta a lezione
- **Correzione**: affermazione del docente imprecisa, dettagli nella pagina Divergenze
- **Dal materiale ufficiale, non mostrato a lezione**: contenuto presente solo in slide o notebook
## Capitoli
<table header-row="true">
<tr>
<td>Capitolo</td>
<td>Giornata</td>
<td>Durata</td>
<td>Contenuto</td>
<td>Stato</td>
</tr>
<tr>
<td>00 - Introduzione al corso</td>
<td>Day 1</td>
<td>nessuna registrazione</td>
<td>Presentazione, biotech e dati, programma, casi di studio Biocentis (glioblastoma). Slide 2025 e 2026, `Teams 1`</td>
<td>completo</td>
</tr>
<tr>
<td>01 - Matematica in biologia: ODE, Eulero e odeint</td>
<td>Day 2</td>
<td>01:27:44</td>
<td>Sistemi complessi, applicazioni della matematica alla biologia, derivata ed Eulero esplicito, `odeint`, Lotka-Volterra, zombie, SIR, sensitivity analysis con SALib</td>
<td>completo, con `Teams 1`-`3`</td>
</tr>
<tr>
<td>02 - Modellazione ad agenti (ABMS) e MESA</td>
<td>Day 3</td>
<td>01:32:15</td>
<td>ABM come complemento alle ODE, caratteristiche degli agenti, MESA, zombie e preda-predatore ad agenti</td>
<td>completo</td>
</tr>
<tr>
<td>03 - Topological Data Analysis di sistemi complessi</td>
<td>Day 4</td>
<td>01:19:43</td>
<td>Kuramoto, Vicsek e Jerne con MESA come generatori di dati, Mapper, omologia persistente, entropia persistente</td>
<td>completo, con `Teams 4`</td>
</tr>
<tr>
<td>04 - Epidemiologia computazionale</td>
<td>Day 5</td>
<td>01:17:24</td>
<td>Epidemiologia come scienza complessa, SIR e sue assunzioni, SIR ad agenti, SIR su grafo, esercizio a tabella</td>
<td>completo, con `Teams 6`</td>
</tr>
<tr>
<td>05 - Introduzione alla bioinformatica</td>
<td>Day 6</td>
<td>01:25:55</td>
<td>Banche dati biologiche, FASTA, NCBI e BLAST, analisi del genoma umano con pandas</td>
<td>completo (nessuna registrazione 2026)</td>
</tr>
<tr>
<td>06 - Algoritmi genetici</td>
<td>Day 7</td>
<td>01:01:23</td>
<td>Rappresentazione, fitness, selezione, crossover, mutazione, applicazioni, TSP in Python</td>
<td>completo (nessuna registrazione 2026)</td>
</tr>
</table>
## Qualità dell'audio
Buona: logprob mediano tra −0.11 e −0.15, nessuna allucinazione nei silenzi. L'`initial_prompt` usato per la trascrizione era tarato su bioinformatica e non sulla modellistica: nomi come Jerne, Lotka-Volterra, SALib, odeint escono storpiati ("GERNE", "lott cover terra", "Saltelli", "the int") e sono corretti nel testo capitolo per capitolo.
## Dove sta il materiale
Sul Mac: `~/Work/Projects/data-science/data-analytics/70-biotech-data-processing/`
- `video/BT-0N.mp4`: le registrazioni
- `out/lezione-0N/`: manuale e divergenze in markdown
- `out/BT-0N/`: trascrizioni, frame, OCR, triage
- `out/controlli-iniziali.md`: identità dei file ed estrazione sull'esame
- `Materiale/Portale`, `Materiale/Teams`: slide, notebook Colab, traccia del test
- `scripts/`: pipeline

[Assessment](assessment.md)

[Divergenze](divergenze.md)

[00 - Introduzione al corso](00-introduzione-al-corso.md)

[01 - Matematica in biologia: ODE, Eulero e odeint](01-matematica-in-biologia-ode-eulero-e-odeint.md)

[02 - Modellazione ad agenti (ABMS) e MESA](02-modellazione-ad-agenti-abms-e-mesa.md)

[03 - Topological Data Analysis di sistemi complessi](03-topological-data-analysis-di-sistemi-complessi.md)

[04 - Epidemiologia computazionale](04-epidemiologia-computazionale.md)

[05 - Introduzione alla bioinformatica](05-introduzione-alla-bioinformatica.md)

[06 - Algoritmi genetici](06-algoritmi-genetici.md)
