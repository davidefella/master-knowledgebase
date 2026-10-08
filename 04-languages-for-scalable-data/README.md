# Languages for Scalable Data

> Fonte Notion: https://app.notion.com/p/3dd12abc808d81c7b016ec66fad193cb — ultima modifica 2026-09-17T09:21:42.974Z

Modulo del Master Data Analytics, docente **Flavio Lombardi** (IAC-CNR e Dipartimento di Matematica e Fisica, Roma Tre). Sulle slide il titolo è *Languages for Scalable Data Science*.
Il corso è una panoramica su linguaggi di programmazione e scalabilità: definizioni, storia dei linguaggi, caratteristiche che rendono un linguaggio scalabile, confronto Python / Java / Rust, concorrenza e data race.
## Fonti
<table header-row="true">
<tr>
<td>Fonte</td>
<td>Edizione</td>
<td>Uso</td>
</tr>
<tr>
<td>7 lezioni del portale `learn.master-data-analytics.it` (`LSD-01` … `LSD-07`)</td>
<td>passata</td>
<td>base del manuale: trascrizione audio</td>
</tr>
<tr>
<td>Slide e dispense da Teams (*Class Materials*)</td>
<td>2026</td>
<td>base del manuale</td>
</tr>
<tr>
<td>Registrazioni Teams (MDA LSD 1, 2, …)</td>
<td>2026</td>
<td>solo integrazioni rispetto all'edizione passata</td>
</tr>
<tr>
<td>Questionari 1–5 (*Class Materials → Assessment*)</td>
<td>2026</td>
<td>verifica del corso, vedi pagina Assessment</td>
</tr>
</table>
## Come sono fatte queste pagine
Ogni capitolo è organizzato per argomento, non per lezione: unisce slide, parlato del docente e materiale correlato. I riferimenti tipo `LSD-01 @ 00:18:37` indicano la lezione del portale e il minuto; `Teams 2 @ 0:06:58` la registrazione Teams. `Teams Extra-1` e `Teams Extra-2` sono le lezioni extra del 28 e 30/04/2026: non a calendario, successive ai questionari, usate solo come integrazione ed esempio.
Convenzioni:
- `[?]` — parola non chiara nell'audio
- **Nota aggiunta** — integrazione non trattata a lezione né nel materiale
- **Edizione 2026** — punto nuovo o diverso rispetto alle lezioni del portale
## Capitoli
Ogni capitolo termina con una tabella di collegamento al questionario: per ogni domanda, slide (file e pagina), video (lezione e minuto) e paragrafo del manuale. Le stesse coordinate sono raccolte sotto ogni domanda nella pagina [Assessment](assessment/README.md).
<table header-row="true">
<tr>
<td>Capitolo</td>
<td>Materiale principale</td>
<td>Questionario</td>
<td>Stato</td>
</tr>
<tr>
<td>[01 - Data science e scalabilità](01-data-science-e-scalabilita.md)</td>
<td>`MDA0`, `MDA1Definitions`</td>
<td>1</td>
<td>bozza completa</td>
</tr>
<tr>
<td>[02 - Storia dei linguaggi di programmazione](02-storia-dei-linguaggi-di-programmazione.md)</td>
<td>`MDA2_PLHistory`</td>
<td>2</td>
<td>bozza completa</td>
</tr>
<tr>
<td>[03 - Cosa rende scalabile un linguaggio](03-cosa-rende-scalabile-un-linguaggio.md)</td>
<td>`MDA3ScalableFeatures` (da Mike Vanier et al.)</td>
<td>3</td>
<td>bozza completa</td>
</tr>
<tr>
<td>[04 - Python, Java e Rust](04-python-java-e-rust.md)</td>
<td>`MDA16PythonvsJava`, `MDA19PythonVsRust`, `Java_vs_Rust`, `RustLearningResources`</td>
<td>4</td>
<td>bozza completa</td>
</tr>
<tr>
<td>[05 - Thread, processi e parallelismo](05-thread-processi-e-parallelismo.md)</td>
<td>`MDA5Multithreading` (Pthreads, OpenMP, MPI), `008_OpenMP`, `ProcessesVsThreads.png`</td>
<td>1 (dom. 3–6), 5 (dom. 3)</td>
<td>bozza completa</td>
</tr>
<tr>
<td>[06 - Scalabilità e data race](06-scalabilita-e-data-race.md)</td>
<td>`MDA21ScalabilityandDataRaces`, `ChiarissimoDataRaceVsRaceCondition`, `design-of-parallel-programs`, voci Wikipedia *Race condition* e *Deadlock*</td>
<td>5</td>
<td>bozza completa</td>
</tr>
<tr>
<td>[07 - Approfondimenti](07-approfondimenti-julia-altri-linguaggi-sicurezza-e-strumenti.md)</td>
<td>Julia (`julia-slides`, `julia-course-slides`), `SCALA book`, `RustLearningResources`, `us-17-Domas-Breaking-The-x86-ISA`; strumenti</td>
<td>—</td>
<td>bozza completa</td>
</tr>
<tr>
<td>[08 - Appendici](08-appendici.md)</td>
<td>glossario, fonti e lezioni, differenze tra edizioni</td>
<td>—</td>
<td>bozza completa</td>
</tr>
</table>
La corrispondenza capitolo ↔ questionario è confermata dal materiale: il Questionario 2 segue `MDA2_PLHistory`, il 3 il testo di Vanier in `MDA3`, il 4 `MDA16` e `MDA19`, il 5 `MDA21` (il docente lo dice in `Teams 5 @ 1:42:45`).
## Stato delle fonti
<table header-row="true">
<tr>
<td>Fonte</td>
<td>Stato</td>
</tr>
<tr>
<td>`LSD-01` (portale)</td>
<td>trascritta</td>
</tr>
<tr>
<td>`LSD-02` … `LSD-07` (portale)</td>
<td>trascritte (\~10 ore in totale)</td>
</tr>
<tr>
<td>Slide Teams (22 file, 2 duplicati)</td>
<td>scaricate</td>
</tr>
<tr>
<td>Questionari 1–5</td>
<td>scaricati</td>
</tr>
<tr>
<td>Registrazioni Teams</td>
<td>consultate in pagina la 2, 3, 4, 5 e le due lezioni extra del 28 e 30/04/2026 (non a calendario, continuazione informale: usate solo come integrazione); non esaminata `MDALSD-20260416cut.mkv`</td>
</tr>
</table>
[Assessment](assessment/README.md)
[01 - Data science e scalabilità](01-data-science-e-scalabilita.md)
[02 - Storia dei linguaggi di programmazione](02-storia-dei-linguaggi-di-programmazione.md)
### Materiale nuovo nell'edizione 2026
Il materiale del portale (edizione passata) comprende solo `MDA0`, `MDA1Definitions`, `MDA2_PLHistory`, `MDA3ScalableFeatures`, `MDA5Multithreading`, `MDA16PythonvsJava`, `008_OpenMP`, `us-17-Domas-Breaking-The-x86-ISA` e le voci Wikipedia su race condition e deadlock.
Sono nuovi, e quindi senza parlato sul portale: `MDA19PythonVsRust`, `Java_vs_Rust`, `MDA21ScalabilityandDataRaces`, `ChiarissimoDataRaceVsRaceCondition`, `design-of-parallel-programs`, le slide su Julia, `SCALA book`, `RustLearningResources`. Per questi (domande 8–10 del Questionario 4 e tutto il Questionario 5) servono le registrazioni Teams.
Mappa delle lezioni del portale per argomento: `LSD-01` definizioni e scalabilità; `LSD-02` scalabilità dei linguaggi e inizio della storia; `LSD-03` storia (C → Java) e inizio delle caratteristiche scalabili; `LSD-04` caratteristiche scalabili e Python/Java; `LSD-05` Python/Java e multithreading; `LSD-06`–`LSD-07` thread, OpenMP e MPI.
[03 - Cosa rende scalabile un linguaggio](03-cosa-rende-scalabile-un-linguaggio.md)
[04 - Python, Java e Rust](04-python-java-e-rust.md)
[05 - Thread, processi e parallelismo](05-thread-processi-e-parallelismo.md)
[06 - Scalabilità e data race](06-scalabilita-e-data-race.md)
[07 - Approfondimenti: Julia, altri linguaggi, sicurezza e strumenti](07-approfondimenti-julia-altri-linguaggi-sicurezza-e-strumenti.md)
[08 - Appendici](08-appendici.md)
