# Social Data Analytics I

Modulo del Master Data Analytics (I livello, 3 CFU, 15 ore), docente **Ida Mele**, ricercatrice IASI-CNR (ida.mele@iasi.cnr.it). Il corso segue i tre "ingredienti" delle piattaforme social: gli **utenti** e la loro attività, le **connessioni** come grafi, il **contenuto** testuale analizzato con l'NLP, fino alla **sentiment analysis**, con tutorial Python in Jupyter (NLTK, spaCy, scikit-learn, TextBlob).

L'idoneità si ottiene con un **progetto congiunto** con il corso di NLP, un notebook su una di tre tracce di sentiment analysis: vedi [Assessment](assessment.md).

## Fonti

| Fonte | Uso |
|---|---|
| Video del portale `learn.master-data-analytics.it` (`SD-01` … `SD-08`), lezioni **preregistrate** caricate il 21/07/2026, circa 10 h | **fonte di verità** dei capitoli |
| Slide SDA25 (portale, quelle dei video) e SDA26 (Teams), notebook dei tutorial 2025 e 2026, i due libri | contorno; il **codice viene dai notebook** ufficiali, rieseguiti per intero |
| Registrazioni Teams 2026 (SharePoint `MDA2026-SocialDataAnalytics`, "Solo visualizzazione", 01-13/10/2026) | **solo Teams 4** (06/10, NLP) è utilizzabile: le altre trascrizioni sono generate in inglese su parlato italiano. Teams 8 e 9 sono del II livello. Trascrizioni lette in pagina, mai salvate |

Per il I livello la docente dichiara: "seguirò lo stesso programma dell'anno scorso, quindi il materiale è sempre quello e le lezioni sono sempre quelle" (Teams 4 @ 0:02:44). Il materiale "II level" (slide `7_DL_SDA26_II_level.pdf`, tutorial RoBERTa, LDA con Gensim, BERTopic) è fuori da questa guida, salvo citazioni in nota.

> ⚠️ **Ordine dei video:** la parte "Supervised Approach" di SD-06, dal minuto 50, va vista **dopo SD-07**, prima di Naive Bayes (nota ufficiale della docente). Nella guida è nel capitolo 06.

### Libri

- [1] G. Szabo, G. Polatkan, O. Boykin, A. Chalkiopoulos, *Social Media Data Mining and Analytics*, Wiley: Introduzione, capitoli 1, 2, 4 (il 3, analisi temporale, è saltato).
- [2] B. Liu, *Sentiment Analysis and Opinion Mining*, Morgan & Claypool: capitoli 1-4 (la slide `0_General_Info` cita anche il 5).

## Come sono fatte queste pagine

Ogni capitolo segue le lezioni per sezioni tematiche, con riferimenti `SD-0N @ hh:mm:ss` e, per il 2026, `Teams N @ h:mm:ss`. Il testo delle slide è riportato fedelmente. Ogni blocco di codice e ogni esempio numerico (TF-IDF, power law, Naive Bayes, metriche micro/macro, cosine similarity, clustering) è **verificato per esecuzione**.

Convenzioni:
- `[?]`: parola non chiara nell'audio o contenuto dubbio
- `[illeggibile]`: schermo non leggibile
- **Nota aggiunta**: integrazione non detta a lezione
- **Correzione**: affermazione della docente o della slide imprecisa, dettagli in [Divergenze](divergenze.md)
- **Dal materiale ufficiale, non mostrato a lezione**: contenuto presente solo nei notebook o nel libro

## Capitoli

| Capitolo | Lezioni | Durata | Contenuto |
|---|---|---|---|
| [01 - Introduzione](01-introduzione-social-data-analytics.md) | SD-01 | 1:14:15 | Programma, libri, idoneità; definizione, motivazioni (targeted advertising), sfide (big data, MapReduce, 5 V); social media e i loro ingredienti; data analytics, data science e "unicorni"; data mining contro data analytics; progetti data-driven: pattern, task, step |
| [02 - Attività degli utenti](02-attivita-degli-utenti.md) | SD-02 | 1:05:08 | Monitorare gli utenti; Wikipedia e X; media contro mediana; log-log e power law U(r) = K·r^γ; ranking, bot, 80/20; PDF e coefficienti fra periodi; burst activity; CDF e CCDF |
| [03 - Reti sociali](03-reti-sociali.md) | SD-03 | 1:16:12 | Reti esplicite e implicite; grafi, grado, in/out degree; grafi pesati; legge di Metcalfe; snowball sampling; distribuzione dei gradi; clustering e rewiring; assortatività e omofilia; small world; preferential attachment e urna di Pólya |
| [04 - Natural Language Processing](04-natural-language-processing.md) | SD-04, SD-05 (+ Teams 4) | 2:26:01 | Approcci e componenti; NLTK e spaCy; tokenizzazione, stopword, WordCloud; stemming e lemmatizzazione; PoS, chunking, NER; WordNet; bag-of-words, CountVectorizer; TF-IDF a mano e con scikit-learn; tutorial spaCy |
| [05 - Text similarity e topic modeling](05-text-similarity-e-topic-modeling.md) | SD-06 fino a 00:49:53 | 0:49:53 | Clustering gerarchico e linkage; cosine similarity; dendrogramma; Stack Exchange Fiction & Fantasy; popolarità dei topic; string matching; LDA: modello grafico, processo generativo, Gibbs sampling, soft e hard clustering |
| [06 - Sentiment analysis](06-sentiment-analysis.md) | SD-07, SD-06 da 00:49:53, SD-08 | circa 2:49 | Opinione e quintupla di Liu; soggettività e polarità; livelli documento, frase, aspetto; lessico e Turney; approcci supervisionati; Naive Bayes; precision, recall, F1, micro e macro, ROC/AUC; tutorial Twitter (classificazione, VADER, TextBlob, frequenze, LDA); proposte di progetto e review di abbigliamento; sfide |

- [Assessment](assessment.md): progetto congiunto, tracce #SDA1-#SDA3, dati ammessi, cosa resta da chiarire
- [Divergenze](divergenze.md): correzioni e note, capitolo per capitolo

## Qualità delle fonti

- **Audio** dei video del portale pulito: pochissimi segmenti sotto la soglia di confidenza (-0,3). Gli errori veri sono nomi e sigle ("Zabbo" per Szabo, "spesi" per spaCy, "warnet" per WordNet), corretti nel testo. Quattro tratti saltati dalla prima trascrizione (SD-02, SD-04, SD-05) sono stati recuperati con una seconda passata; uno resta marcato [?].
- **Video** a 640x360 (`_low`, unica versione disponibile): il codice si legge male dai fotogrammi, per questo viene dai notebook.
- **SD-03** si interrompe a metà dell'ultima frase (3 s di parlato perso, nessuna slide mancante); **SD-05** dura 39 minuti ma è completa.

## Dove sta il materiale

Sul Mac: `~/Work/Projects/data-science/data-analytics/100-social-data-analytics/`
- `video/SD-0N.mp4`: i video del portale
- `out/lezione-0N/`: manuale e divergenze (stesso contenuto di queste pagine), script `verifica_sd0N.py` con il loro output, notebook rieseguiti. Gli script di verifica e i loro output sono anche qui in [`verifiche/`](verifiche/)
- `out/SD-0N/`: trascrizioni, frame, OCR
- `out/teams-2026/integrazioni-capitolo-04.md`: riassunto di Teams 4 (nessuna trascrizione salvata)
- `out/controlli-iniziali.md`: identità dei file, audio, esame
- `Materiale/Portale/estratti/`, `Materiale/Teams/estratti/`: slide, notebook, dataset, libri
- `Esame/`: traccia e modalità
