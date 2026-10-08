# Assessment

> Fonte Notion: https://app.notion.com/p/3dd12abc808d8160a125d7762fd486ba — ultima modifica 2026-09-17T09:36:57.376Z

La verifica del modulo sono **5 questionari a risposta aperta**, pubblicati su Teams in *Class Materials → Assessment*.
## Modalità
Dal testo dei questionari:
- risposte individuali, consegnate come **PDF**
- invio a [**flavio.lombardi@uniroma3.it**](mailto:flavio.lombardi@uniroma3.it)
- oggetto obbligatorio con **MDA-LSD**
Dalle registrazioni Teams (edizione 2026):
- `Teams 2 @ 0:06:58` — i questionari vengono valutati, e il docente apprezza chi aggiunge "di suo": esperienze e impressioni personali oltre allo standard richiesto
- `Teams 2 @ 0:09:54`–`0:11:39` — i questionari stanno in *Class Materials → Assessment*
- `Teams 2 @ 2:15:43` — per rispondere "avete un sacco di tempo", ma il consiglio è di togliersi il pensiero presto
- `Teams 4 @ 0:15:07` — alcuni hanno già mandato le risposte; "saranno valutate comunque e varranno come esonero di questo modulo"
- `Teams 5 @ 0:06:18` — i questionari valgono come **esonero in itinere**: superarli con risposte adeguate significa superare il modulo
- `Teams 5 @ 1:42:45` — le slide MDA21 "fanno parte delle domande dell'ultimo" questionario
- `Teams 5 @ 1:43:45` — "la deadline non è così stringente"; `1:48:11` — feedback e domande per email con **MDA** nell'oggetto
- nessuna scadenza precisa indicata
Edizione passata (portale), per confronto:
- `LSD-01 @ 00:18:24`–`00:19:04` — valutazione "il più integrata possibile" con gli altri corsi, più un piccolo progetto facoltativo; nell'edizione 2026 non se ne parla più
- `LSD-07 @ 00:24:19` — consegna dei questionari entro **settembre** (vale per quell'edizione)
## Stato
<table header-row="true">
<tr>
<td>Questionario</td>
<td>Domande</td>
<td>Capitolo</td>
<td>Bozza</td>
<td>Rivisto</td>
<td>Inviato</td>
</tr>
<tr>
<td>1</td>
<td>10</td>
<td>[01](../01-data-science-e-scalabilita.md) (e 05)</td>
<td>[bozza](risposte-questionario-1.md)</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td>2</td>
<td>12</td>
<td>[02](../02-storia-dei-linguaggi-di-programmazione.md)</td>
<td>[bozza](risposte-questionario-2.md)</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td>3</td>
<td>10</td>
<td>[03](../03-cosa-rende-scalabile-un-linguaggio.md)</td>
<td>[bozza](risposte-questionario-3.md)</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td>4</td>
<td>10</td>
<td>[04](../04-python-java-e-rust.md)</td>
<td>[bozza](risposte-questionario-4.md)</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td>5</td>
<td>10</td>
<td>[06](../06-scalabilita-e-data-race.md) (e 05)</td>
<td>[bozza](risposte-questionario-5.md)</td>
<td>—</td>
<td>—</td>
</tr>
</table>
## Come leggere le coordinate
Sotto ogni domanda: **Slide** = file nella cartella `Materiale/Teams/Slides` e pagina del PDF; **Video** = `LSD-0N @ hh:mm:ss` per le lezioni del portale, `Teams N @ h:mm:ss` per le registrazioni 2026 (`Teams Extra-1` e `Teams Extra-2` sono le lezioni extra del 28 e 30 aprile: non a calendario, probabilmente una continuazione informale per la classe, successive alla pubblicazione del Questionario 5. Nelle coordinate valgono come **supporto**, non come fonte principale); **Manuale** = capitolo e paragrafo. "fine" indica la fine della registrazione. Dove una domanda non è trattata a voce lo dico esplicitamente: in quel caso la risposta si appoggia a slide e **Note aggiunte** del manuale.
---
## Questionario 1 — Data science e scalabilità
1. Discuss the main differences between predictive and prescriptive analysis.
	- **Slide:** `MDA1Definitions` p8–p10
	- **Video:** `LSD-01 @ 00:23:46`–`00:25:26`, `00:51:22`–`00:56:12`, `01:01:44`–`01:04:53`
	- **Manuale:** 01 §3, tabella di confronto
2. What is prescriptive analysis particularly useful for?
	- **Slide:** `MDA1Definitions` p9–p10
	- **Video:** `LSD-01 @ 00:55:41`–`01:04:53`
	- **Manuale:** 01 §3, Prescrittiva
3. Define scalability. Where has it proved particularly useful over the last few years?
	- **Slide:** `MDA1Definitions` p12, p15; `MDA5` p10–p14
	- **Video:** `LSD-01 @ 00:34:33`–`00:36:13`, `01:06:34`–`01:10:37`; `LSD-02 @ 00:00:46`–`00:01:34`; `LSD-05 @ 01:09:06`–`01:12:58`, `01:46:23`–`01:48:09`; `LSD-07 @ 00:33:06`–`00:35:30`; `Teams Extra-1 @ 0:07:41`, `0:13:51`–`0:28:05`
	- **Manuale:** 01 §5 e §2; 05 §5. "Negli ultimi anni" non è esplicito nelle slide: esempi a voce sono webscale e addestramento dei modelli generativi
4. Provide examples of Scaling-out and Scaling-up approaches
	- **Slide:** `MDA1Definitions` p13–p14; `MDA5` p21–p22
	- **Video:** `LSD-01 @ 01:10:37`–`01:12:46`, `01:14:01`–`01:16:24`, `01:17:33`–fine; `LSD-05 @ 01:33:53`–`01:37:34`, `01:47:35`–`01:48:09`; `LSD-07 @ 00:13:20`–`00:15:22`; `Teams Extra-2 @ 0:16:02`–`0:27:11`
	- **Manuale:** 01 §5 (tabella, analogia del bar); 05 §4 (analogia della festa)
5. Which one between scaling-out and scaling up is better for data science and why?
	- **Slide:** `MDA1Definitions` p14
	- **Video:** `LSD-01 @ 01:12:15`–`01:14:01`, `01:16:24`–fine; `LSD-02 @ 00:00:09`–`00:00:46`; `LSD-05 @ 01:34:29`–`01:36:45`, `01:44:11`–`01:46:23`; `LSD-07 @ 00:13:57`–`00:15:22`, `00:18:42`–`00:21:29`; `Teams 5 @ 0:52:39`–`0:53:46`; `Teams Extra-2 @ 0:46:03`–`0:48:01`
	- **Manuale:** 01 §5 ultimo paragrafo (docente e slide non concordano); 05 §4, nota
6. Computational complexity of an algorithm and scalability, what the relationship?
	- **Slide:** `MDA1Definitions` p15–p16
	- **Video:** `LSD-02 @ 00:01:34`–`00:03:33`; `LSD-05 @ 01:20:41`–`01:21:47`; `LSD-07 @ 00:31:35`–`00:33:06`; `Teams Extra-1 @ 0:33:28`–`0:34:30`
	- **Manuale:** 01 §6, nota; 05 §3 (forza bruta) e §5 (weak scaling con O(n³)). La complessità O-grande non è trattata formalmente a lezione
7. What is design abstracion? Is it useful or not to scalability? Provide examples.
	- **Slide:** `MDA1Definitions` p17–p18; `MDA3` p55–p62
	- **Video:** `LSD-02 @ 00:06:50`–`00:10:56`, `00:44:54`–`00:46:07`; `LSD-03 @ 00:18:57`–`00:22:25`; `LSD-04 @ 01:42:35`–`01:55:20`; `LSD-05 @ 00:04:02`–`00:06:48`
	- **Manuale:** 01 §6, nota con esempi; 03 §6
8. What are the main distinctive factors of a Programming Language?
	- **Slide:** nessuna dedicata; `MDA2_PLHistory` p2–p7; `MDA3` (intero)
	- **Video:** `LSD-02 @ 00:10:23`–`00:13:15`, `00:26:17`–`00:33:13`; `LSD-03 @ 00:32:12`–`00:42:32`, `00:45:57`–`00:47:36`; `Teams Extra-2 @ 0:29:39`–`0:32:17`
	- **Manuale:** 02 §1–§2 e excursus compilatore/interprete; 03. Domanda aperta: i "fattori distintivi" non sono definiti come tali
9. What is the main difference between a scalable PL and a non scalable one? Please provide examples.
	- **Slide:** `MDA1Definitions` p18–p19; `MDA3` p9, p20; `MDA16` p8–p16
	- **Video:** `LSD-02 @ 00:01:34`–`00:06:50`, `00:09:21`–`00:22:09`, `01:26:36`–fine; `LSD-03 @ 00:46:30`–`00:47:36`; `LSD-04 @ 00:04:39`–`00:06:53`, `00:42:06`–`00:42:38`; `LSD-05 @ 00:40:27`–`00:43:54`, `01:37:34`–`01:39:38`, `01:55:34`–`01:57:46`; `LSD-07 @ 00:19:12`–`00:21:29`; `Teams 2 @ 1:21:04`; `Teams Extra-2 @ 1:47:56`
	- **Manuale:** 01 §6; 02 §3 C; 03; 04 §3 e §5
10. What are the fundamental ingredients to study and address Data Science problems?
	- **Slide:** `MDA1Definitions` p2, p4, p11
	- **Video:** `LSD-01 @ 00:20:35`–`00:22:25`, `00:24:47`–`00:25:26`, `00:38:36`–`00:40:51`, `01:04:21`–`01:06:34`
	- **Manuale:** 01 §4 e §2
## Questionario 2 — Storia dei linguaggi
1. Explain the main factors that influenced the historical development of programming languages, and briefly describe the role played by hardware, applications, and theory.
	- **Slide:** `MDA2_PLHistory` p2–p7
	- **Video:** `LSD-02 @ 00:24:10`–`00:26:17`, `00:33:13`–`01:02:44`
	- **Manuale:** 02 §1
2. Why did early programming languages prioritize efficiency over safety, and how has this balance changed over time?
	- **Slide:** `MDA2_PLHistory` p9–p10, p16; `MDA3` p45, p47
	- **Video:** `LSD-02 @ 00:24:55`–`00:33:13`, `01:25:33`–fine; `LSD-03 @ 00:00:10`–`00:03:15`; `Teams Extra-2 @ 0:29:39`–`0:32:17`
	- **Manuale:** 02 §1, Dall'efficienza alla sicurezza; 02 §3 C
3. Why is FORTRAN considered the first real high-level imperative programming language? Discuss its design goals and historical context.
	- **Slide:** `MDA2_PLHistory` p9–p10
	- **Video:** `LSD-02 @ 01:02:44`–`01:07:00`; `Teams 2 @ 1:09:56`
	- **Manuale:** 02 §3 FORTRAN (IBM 704 e "performance first" solo nelle slide)
4. Describe the main contributions of LISP to programming language design. Focus in particular on higher-order programming and memory management.
	- **Slide:** `MDA2_PLHistory` p11–p12; `MDA3` p2–p11
	- **Video:** `LSD-02 @ 01:06:29`–`01:11:00`; `LSD-04 @ 00:08:21`–`00:08:52`
	- **Manuale:** 02 §3 LISP; 03 §2 (garbage collection)
5. Explain how ALGOL reacted to FORTRAN and identify the key innovations it introduced in programming language structure.
	- **Slide:** `MDA2_PLHistory` p13
	- **Video:** `LSD-02 @ 01:10:29`–`01:12:47`; `LSD-03 @ 00:14:33`–`00:15:07`
	- **Manuale:** 02 §3 ALGOL e nota ("reazione a FORTRAN" e begin/end solo nelle slide)
6. Discuss the main design goals of the C programming language and explain why it became widely adopted for both system and general-purpose programming.
	- **Slide:** `MDA2_PLHistory` p14–p16
	- **Video:** `LSD-02 @ 00:16:12`–`00:17:21`, `01:12:06`–`01:13:52`, `01:19:29`–`01:23:50`; `LSD-03 @ 00:00:10`–`00:01:25`
	- **Manuale:** 02 §3 C
7. Identify and explain the main strengths and weaknesses of C, with particular reference to pointers and the type system.
	- **Slide:** `MDA2_PLHistory` p16; `MDA3` p12–p20, p28–p30, p40, p45
	- **Video:** `LSD-02 @ 01:13:21`–`01:19:29`, `01:23:19`–fine; `LSD-03 @ 00:01:25`–`00:13:21`, `00:29:05`–`00:31:02`; `LSD-04 @ 00:03:30`–`00:04:39`, `00:24:26`–`00:25:38`, `01:14:23`–`01:14:56`, `01:27:40`–`01:28:12`; `Teams 2 @ 1:21:04`, `1:36:37`
	- **Manuale:** 02 §3 C, tabella; 03 §3 (puntatori)
8. ML’s type inference system reduces the burden on the programmer. Could such automation ever become a limitation? Discuss possible drawbacks.
	- **Slide:** `MDA2_PLHistory` p20–p22; `MDA3` p26–p27, p33–p34
	- **Video:** `LSD-03 @ 00:22:25`–`00:32:12`, `00:42:32`–`00:44:54`; `LSD-04 @ 01:11:32`–`01:12:45`, `01:22:22`–`01:22:54`
	- **Manuale:** 02 §3 ML e nota sui limiti; 03 §4. I limiti dell'inferenza non sono trattati a lezione: domanda di riflessione
9. Logic programming languages like PROLOG differ radically from imperative and functional languages. In what application domains do they still have an advantage today?
	- **Slide:** `MDA2_PLHistory` p23–p25
	- **Video:** `LSD-02 @ 00:47:19`–`00:48:08`; `LSD-03 @ 00:45:57`–`00:58:34`
	- **Manuale:** 02 §3 PROLOG e nota (i domini di oggi non sono elencati a lezione, a parte SQL)
10. Java was designed with networked execution and security in mind. How did the rise of the Web shape language design choices in the 1990s?
	- **Slide:** `MDA2_PLHistory` p26–p30; `MDA16` p14–p15
	- **Video:** `LSD-03 @ 00:57:59`–`01:15:42`; `LSD-02 @ 00:48:08`–`00:50:46`; `LSD-05 @ 01:50:35`–`01:55:34`; `Teams 2 @ 1:48:36`
	- **Manuale:** 02 §3 Java e nota; 04 §5
11. Explain why Simula is considered the first object-oriented language and describe its most influential concepts.
	- **Slide:** `MDA2_PLHistory` p17–p19
	- **Video:** `LSD-03 @ 00:13:21`–`00:23:05`; `LSD-02 @ 00:42:53`–`00:46:48`
	- **Manuale:** 02 §3 Simula
12. Considering the languages surveyed in the PDF, which historical ideas continue to shape modern data-science and scalable-system languages?
	- **Slide:** `MDA2_PLHistory` p12, p17–p18, p21–p22, p28–p30; `MDA3` p21
	- **Video:** `LSD-02 @ 00:18:37`–`00:22:09`, `00:35:34`–`00:37:12`, `01:04:53`–`01:06:29`; `LSD-03 @ 00:12:11`–`00:13:21`, `00:26:59`–`00:29:05`, `00:43:14`–`00:44:54`, `00:56:55`–`00:58:34`, `01:08:25`–`01:12:07`; `LSD-05 @ 01:52:16`–`01:52:55`; `Teams 2 @ 1:18:47`
	- **Manuale:** 02, nota sulle idee storiche e §2. Domanda di sintesi, non trattata come tale
## Questionario 3 — Caratteristiche che influenzano la scalabilità
1. **Garbage Collection and Scalability**: Explain why garbage collection (GC) is considered the single most important feature for ensuring the scalability of a programming language. Discuss both its advantages and its associated costs in terms of time and space.
	- **Slide:** `MDA3ScalableFeatures` p2–p11
	- **Video:** `LSD-03 @ 01:15:42`–`01:18:08`, `01:26:32`–`01:35:02`; `LSD-04 @ 00:06:53`–`00:24:26`; `Teams 3 @ 0:40:52`–`0:46:00`, `1:10:00`–`1:33:12`
	- **Manuale:** 03 §2 (con la correzione su reference counting e tracing)
2. **Manual Memory Management vs Garbage Collection**: Describe the challenges of manual memory management in languages without garbage collection. Why does this often lead programmers to restrict themselves to simpler data structures, and how does this affect scalability?
	- **Slide:** `MDA3ScalableFeatures` p3–p6, p14
	- **Video:** `LSD-03 @ 01:18:08`–`01:26:32`; `LSD-04 @ 00:08:21`–`00:17:34`, `00:26:14`–`00:28:34`
	- **Manuale:** 03 §2, Senza GC
3. **Pointer Arithmetic as a Scalability Barrier**: Analyze why direct memory access and pointer arithmetic are considered harmful to scalability. In your answer, refer to safety, debugging, and long-term maintenance issues.
	- **Slide:** `MDA3ScalableFeatures` p12–p21
	- **Video:** `LSD-03 @ 00:01:25`–`00:13:21`, `01:18:50`–`01:21:11`; `LSD-04 @ 00:24:26`–`00:26:14`, `00:39:12`–`00:54:26`; `Teams 3 @ 1:35:00`–`1:49:27`
	- **Manuale:** 03 §3
4. **Performance Trade-offs of Low-Level Programming**: Discuss the claim that languages enabling micro-optimizations (e.g., through pointer arithmetic) often make macro-optimizations impossible. Explain why this trade-off negatively impacts scalability in large systems.
	- **Slide:** `MDA3ScalableFeatures` p13, p17
	- **Video:** `LSD-04 @ 00:25:38`–`00:26:14`, `00:46:16`–`00:46:47`; `Teams 3 @ 1:43:49`–`1:45:17`
	- **Manuale:** 03 §3, nota sul pointer aliasing
5. **Static Type Checking: Benefits and Productivity**: Explain the main scalability advantages of static type checking. How does static typing improve programmer productivity and facilitate code reuse in large projects?
	- **Slide:** `MDA3ScalableFeatures` p22–p25
	- **Video:** `LSD-04 @ 00:54:26`–`01:04:29`; `LSD-05 @ 01:48:09`–`01:50:35`
	- **Manuale:** 03 §4; 04 §5 (Java)
6. **Type Inference versus Explicit Type Declaration**: Compare explicit type declarations with type inference. Why does type inference help reconcile the benefits of static typing with code conciseness, and why is this important for scalability?
	- **Slide:** `MDA3ScalableFeatures` p26–p27, p33–p34
	- **Video:** `LSD-04 @ 01:05:00`–`01:06:36`, `01:11:32`–`01:12:45`, `01:22:22`–`01:22:54`
	- **Manuale:** 03 §4 e note
7. **Static vs Dynamic Typing**: Compare static and dynamic type systems in terms of expressiveness, performance, and scalability. Why does the author argue that dynamically typed languages scale poorly despite their flexibility?
	- **Slide:** `MDA3ScalableFeatures` p25, p31–p38
	- **Video:** `LSD-04 @ 01:18:46`–`01:25:46`; `LSD-05 @ 01:48:09`–`01:50:35`; `Teams 3 @ 1:50:00`–`2:11:25`
	- **Manuale:** 03 §4 e nota
8. **Run-Time Error Checking and Safety**: Explain why run-time error checking is necessary even in statically typed languages. Use array bounds checking and arithmetic errors as examples, and discuss the trade-off between safety and performance.
	- **Slide:** `MDA3ScalableFeatures` p42–p47
	- **Video:** `LSD-04 @ 01:30:48`–`01:38:27`; `Teams 3 @ 2:25:07`–`2:30:00`
	- **Manuale:** 03 §5
9. **Assertions and Design by Contract**: Describe the role of assertions and Design by Contract in improving language scalability. Why do these mechanisms help reduce debugging effort in large software systems?
	- **Slide:** `MDA3ScalableFeatures` p48–p54
	- **Video:** `LSD-04 @ 01:38:27`–`01:42:35`; `Teams 3 @ 2:30:00`–`2:31:25`
	- **Manuale:** 03 §5 e nota
10. **Abstractions and Programming Paradigms**: Discuss how support for abstractions (modules, object-oriented programming, and functional programming) contributes to scalability. Compare the strengths of object-oriented and functional programming in the context of large-scale software development.
	- **Slide:** `MDA3ScalableFeatures` p55–p67 (p68–p73 correlate)
	- **Video:** `LSD-04 @ 01:42:35`–`02:00:39`; `LSD-05 @ 00:00:11`–`00:20:29`; `LSD-03 @ 00:43:14`–`00:47:36`; `Teams 3 @ 2:36:56`–`2:43:05`
	- **Manuale:** 03 §6 (confronto OOP/FP nella nota)
## Questionario 4 — Python, Java e Rust
1. Explain the design goals behind Python as a programming language and discuss how these goals influence its typical areas of application. Your answer should refer to language characteristics such as typing, interpretation, readability, and ecosystem.
	- **Slide:** `MDA16PythonvsJava` p3–p7; `MDA19PythonVsRust` p3
	- **Video:** `LSD-05 @ 00:25:57`–`00:38:42`; `LSD-06 @ 00:01:48`–`00:05:18`; `LSD-04 @ 01:06:06`–`01:08:51`; `Teams 4 @ 0:17:14`–`0:20:23`, `0:25:47`–`0:27:00`
	- **Manuale:** 04 §1
2. Discuss the scenarios in which Python is preferred over Java, providing concrete examples from data science or machine learning. Explain why Python’s features and libraries make it particularly suitable for these domains.
	- **Slide:** `MDA16PythonvsJava` p5–p7, p18–p19
	- **Video:** `LSD-05 @ 00:26:28`–`00:29:56`, `00:36:18`–`00:38:03`, `01:38:35`–`01:39:38`; `LSD-06 @ 00:00:10`–`00:03:32`; `LSD-04 @ 01:20:32`–`01:21:11`; `Teams 4 @ 0:20:23`–`0:27:00`
	- **Manuale:** 04 §2
3. Analyze the advantages and drawbacks of the Python GIL with respect to concurrency and parallelism. In your answer, distinguish between CPU-bound and I/O-bound workloads.
	- **Slide:** `MDA16PythonvsJava` p8–p13; `MDA19PythonVsRust` p8, p12
	- **Video:** `LSD-05 @ 00:38:42`–`00:46:15`, `01:40:55`–`01:42:31`; `LSD-06 @ 00:34:16`–`00:43:51`; `Teams 4 @ 0:27:00`–`0:37:57`
	- **Manuale:** 04 §3 (con correzione: i termini CPU-bound e I/O-bound non sono usati a voce)
4. Explain how Python applications can still achieve parallelism despite the presence of the GIL. Discuss the role of multiprocessing, external libraries, or native extensions.
	- **Slide:** `MDA16PythonvsJava` p8, p10; `MDA19PythonVsRust` p6, p9, p12
	- **Video:** `LSD-05 @ 00:40:27`–`00:41:05`; `LSD-06 @ 00:43:51`–`00:48:50`; `LSD-04 @ 00:49:42`–`00:50:49`; `Teams 4 @ 0:30:09`–`0:31:43`, `0:37:57`–`0:40:24`, `1:56:04`–`1:59:28`
	- **Manuale:** 04 §4 e nota (multiprocessing e asyncio solo nelle slide)
5. Describe the core characteristics of Java that support the “Write Once, Run Anywhere” (WORA) principle. Explain the role of the Java Virtual Machine (JVM) and bytecode in achieving platform independence.
	- **Slide:** `MDA16PythonvsJava` p14–p15, p18
	- **Video:** `LSD-05 @ 01:50:35`–`01:52:55`; `LSD-06 @ 00:06:32`–`00:07:34`, `00:28:41`–`00:29:47`; `LSD-04 @ 00:58:20`–`00:59:23`; `Teams 4 @ 0:40:24`–`0:42:30`, `1:31:10`
	- **Manuale:** 04 §5; 02 §3 Java
6. Explain why Java is often chosen for large-scale, enterprise-level applications. In your answer, reference object-oriented design, concurrency control, and database connectivity.
	- **Slide:** `MDA16PythonvsJava` p15–p16, p19
	- **Video:** `LSD-05 @ 01:52:55`–`01:57:46`; `LSD-06 @ 00:00:41`–`00:01:48`, `00:05:55`–`00:08:07`, `00:27:27`–`00:33:41`; `LSD-04 @ 01:56:40`–`02:00:39`
	- **Manuale:** 04 §5 (con correzione sulle classi thread-safe)
7. Given a performance-critical numerical application, justify whether you would choose Java, pure Python, or an optimized Python approach (e.g., Cython or PyPy).
	- **Slide:** `MDA16PythonvsJava` p18, p20–p30
	- **Video:** `LSD-06 @ 00:08:45`–`00:27:27`; `LSD-04 @ 01:08:51`–`01:13:53`; `LSD-05 @ 01:55:34`–`01:57:46`; `Teams 4 @ 1:29:27`–`1:38:16`
	- **Manuale:** 04 §6 e nota con i criteri di scelta
8. Give one example of an application better suited for Python and one better suited for Rust, and briefly explain why.
	- **Slide:** `MDA19PythonVsRust` p4–p7, p14
	- **Video:** `LSD-07 @ 00:28:23`–`00:29:48`, `00:40:00`–`00:41:01`; `Teams 4 @ 1:38:16`–`1:49:58`, `1:56:04`–`1:59:28`
	- **Manuale:** 04 §7
9. Why is Rust described as enabling predictable performance in large-scale systems?
	- **Slide:** `MDA19PythonVsRust` p4, p13; `Java_vs_Rust` p6–p8; `RustLearningResources` p7–p8, p59, p66–p68
	- **Video:** `LSD-07 @ 00:40:00`–`00:40:30`; `Teams 4 @ 1:55:02` (solo citato)
	- **Manuale:** 04 §7, nota. Il perché non è spiegato a voce: la risposta si appoggia alle slide
10. Why is Rust particularly suitable for highly concurrent, multithreaded applications?
	- **Slide:** `MDA19PythonVsRust` p8–p13; `Java_vs_Rust` p9; `RustLearningResources` p8, p57–p58, p66–p88
	- **Video:** `LSD-07 @ 00:28:23`–`00:29:48`, `00:41:01`–`00:42:41`; `LSD-06 @ 00:43:19`; `Teams 4 @ 1:49:58`–`1:55:02`
	- **Manuale:** 04 §7, nota e correzione
## Questionario 5 — Scalabilità e data race
1. What is a data race? Explain the three necessary conditions for a data race to occur and why each condition is essential.
	- **Slide:** `MDA21ScalabilityandDataRaces` p3; `ChiarissimoDataRaceVsRaceCondition` p1–p2; `Race-condition-Wikipedia` p2–p4; `design-of-parallel-programs` p6
	- **Video:** `Teams 5 @ 1:28:20`–`1:29:31`, `1:38:30`–`1:42:45`; `Teams Extra-1 @ 1:00:03`–`1:08:37`; `LSD-06 @ 01:11:03`–`01:20:25`; `LSD-07 @ 00:42:41`–`00:44:31`
	- **Manuale:** 06 §1–§2; perché ogni condizione è essenziale: nota in §2 (non spiegato a voce)
2. Scalability is not purely a performance property. Explain why scalability must be considered a joint property of performance and correctness, and how data races sit at this intersection.
	- **Slide:** `MDA21ScalabilityandDataRaces` p4, p21–p22, p25
	- **Video:** `Teams 5 @ 0:56:16`–`0:57:17`, `1:02:43`–`1:05:52`, `1:35:50`–`1:36:53`; `Teams 4 @ 0:47:04`; `Teams Extra-1 @ 1:09:39`–`1:10:45`, `1:17:09`, `1:56:35`
	- **Manuale:** 06 §5.1 e §5.8
3. Why has concurrency become the primary mechanism for performance scaling in modern systems? Discuss the architectural and historical reasons mentioned in the slides.
	- **Slide:** `MDA21ScalabilityandDataRaces` p5–p6; `MDA5Multithreading` p2–p14
	- **Video:** `Teams 5 @ 1:29:31`; `Teams 4 @ 2:15:25`–`2:24:46`; `Teams Extra-1 @ 0:10:05`–`0:11:05`; `LSD-05 @ 00:46:15`–`00:55:22`
	- **Manuale:** 06 §5.2; 05 §1
4. Explain how increasing the number of threads affects the number of possible execution interleavings. Why does this make data races emergent properties of scaling rather than incidental bugs?
	- **Slide:** `MDA21ScalabilityandDataRaces` p6–p8; `MDA5Multithreading` p55, p98, p138 (esecuzioni con ordini diversi)
	- **Video:** `Teams 5 @ 1:29:31`–`1:30:33`; `Teams Extra-1 @ 1:07:34`–`1:08:37`; `LSD-06 @ 01:18:12`–`01:19:22`; `LSD-07 @ 00:21:29`–`00:22:41`
	- **Manuale:** 06 §5.3, nota con il conteggio degli interleaving
5. Explain why a program behaving correctly with 2 threads can fail consistently with 64 threads.
	- **Slide:** `MDA21ScalabilityandDataRaces` p9
	- **Video:** `Teams 5 @ 1:30:33`, `1:47:11`; `Teams 4 @ 0:33:40`–`0:34:41`
	- **Manuale:** 06 §5.3, nota
6. What are load amplification effects, and how do they increase the likelihood of observing data races under scalable workloads?
	- **Slide:** `MDA21ScalabilityandDataRaces` p10–p11
	- **Video:** `Teams 5 @ 1:30:33`–`1:31:45`; `Teams Extra-1 @ 2:01:58`–`2:07:23`
	- **Manuale:** 06 §5.4, nota
7. Describe the fundamental tension between synchronization and scalability.
	- **Slide:** `MDA21ScalabilityandDataRaces` p12–p14
	- **Video:** `Teams 5 @ 1:31:45`–`1:33:46`; `Teams Extra-1 @ 1:08:37`–`1:12:47`, `1:38:44`, `1:54:20`–`1:57:37`; `Teams Extra-2 @ 1:39:12`
	- **Manuale:** 06 §4 (traghetto, versioni della somma) e §5.5
8. Why does removing synchronization improve scalability but risk correctness, while adding it improves correctness but limits scalability?
	- **Slide:** `MDA21ScalabilityandDataRaces` p14; `design-of-parallel-programs` p7–p13
	- **Video:** `Teams 5 @ 1:41:44`–`1:42:45`; `Teams Extra-1 @ 1:39:52`–`1:57:37`; `Teams 4 @ 0:31:43`–`0:34:41`; `LSD-05 @ 00:41:05`–`00:43:54`
	- **Manuale:** 06 §4 e §5.5, nota
9. Why can even small synchronized regions severely limit scalability at large scale?
	- **Slide:** `MDA21ScalabilityandDataRaces` p15–p16
	- **Video:** `Teams 5 @ 1:32:46`–`1:33:46`; `Teams Extra-1 @ 0:20:30`–`0:25:30`, `1:17:40`–`1:24:28`; `LSD-07 @ 00:12:07`–`00:12:46`
	- **Manuale:** 06 §5.6, nota con i numeri di Amdahl e la Universal Scalability Law; 05 §5
10. Why do many modern programming languages and systems restrict shared mutable state or enforce race freedom?
	- **Slide:** `MDA21ScalabilityandDataRaces` p19–p20, p23; `MDA19PythonVsRust` p10–p11; `RustLearningResources` p57–p58, p66–p88
	- **Video:** `Teams 5 @ 1:34:49`–`1:35:50`; `Teams 4 @ 1:49:58`–`1:55:02`; `LSD-07 @ 00:41:01`–`00:42:41`; `Teams Extra-1 @ 1:58:40`
	- **Manuale:** 06 §5.7 e §5.9, nota sui linguaggi
[Risposte Questionario 1](risposte-questionario-1.md)
[Risposte Questionario 2](risposte-questionario-2.md)
[Risposte Questionario 3](risposte-questionario-3.md)
[Risposte Questionario 4](risposte-questionario-4.md)
[Risposte Questionario 5](risposte-questionario-5.md)
