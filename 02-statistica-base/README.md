# 📐 Statistica Base

> Fonte Notion: https://app.notion.com/p/3c612abc808d81af96d2c76325396a5f — ultima modifica 2026-08-25T21:04:48.790Z

<table_of_contents color="gray"/>
Materiale del corso MDA — **Statistica Base**. Appunti di lezione rielaborati e integrati.
<callout icon="ℹ️" color="gray">
	Le parti marcate **\[integrazione\]** non sono presenti nelle slide del docente: sono aggiunte per completezza o per collegare argomenti.
</callout>
---
## Programma del corso
Il corso ha un **filo conduttore esplicito**: la *PDF* (Probability Density Function). Ogni blocco costruisce sul precedente.
- **Probabilità** — le regole di base per assegnare e combinare le probabilità.
- **Variabili aleatorie** — come si descrive con i numeri un fenomeno incerto, nel caso discreto e nel caso continuo.
- **Stimatori** — come si ricava un valore (una media, una percentuale) a partire dai dati raccolti.
- **Test di ipotesi** — come si decide se un'ipotesi è compatibile con i dati osservati.
- **Test di ipotesi → Bayes** — la stessa domanda affrontata con l'approccio bayesiano.
<callout icon="⚠️" color="yellow_bg">
	**\[integrazione\] Nota terminologica.** La slide dice "variabili statistiche", ma dal contesto (caso discreto/continuo, PDF) si intendono **variabili aleatorie** (*random variables*). In italiano "variabile statistica" indica di solito il carattere rilevato su una popolazione, oggetto della statistica descrittiva. Tenerle distinte evita di confondere **distribuzione di frequenza** (dati osservati) e **distribuzione di probabilità** (modello).
</callout>
---
## Bibliografia
Riferimenti indicati dal docente: gli **appunti** delle lezioni e **qualsiasi testo base** di statistica, più i due volumi seguenti.
<table fit-page-width="true" header-row="true">
<tr>
<td>Autore</td>
<td>Titolo</td>
<td>Impostazione</td>
</tr>
<tr>
<td>**F. M. Dekking** et al.</td>
<td>*A Modern Introduction to Probability and Statistics — Understanding Why and How*</td>
<td>Prevalentemente **frequentista**. Manuale classico Springer: probabilità → v.a. → inferenza (stima, intervalli, test). Riferimento standard, ottimo per esercizi.</td>
</tr>
<tr>
<td>**G. D'Agostini**</td>
<td>*Bayesian Reasoning in Data Analysis — A Critical Introduction*</td>
<td>Dichiaratamente **bayesiano**, di scuola fisico-sperimentale. Probabilità come *grado di credenza*, inferenza come aggiornamento via teorema di Bayes.</td>
</tr>
</table>
---
## ⭐ Da dove partire
- [**Bignami — i 10 concetti da sapere**](bignami-i-10-concetti-da-sapere.md) — tutto il corso in una pagina: formule, esempi e le trappole tipiche. Da leggere prima e rileggere alla fine.
---
## Moduli
- [01 - Probabilità: linguaggio e assiomi](01-probabilita-linguaggio-e-assiomi.md)
- [02 - Probabilità condizionata](02-probabilita-condizionata.md)
- [03 - Variabili casuali e statistiche](03-variabili-casuali-e-statistiche.md)
- [04 - Funzione di probabilità e cumulativa](04-funzione-di-probabilita-e-cumulativa.md)
- [05 - Distribuzioni notevoli](05-distribuzioni-notevoli.md)
- [06 - Dal discreto al continuo](06-dal-discreto-al-continuo.md)
- [07 - Cumulativa e densità nel continuo](07-cumulativa-e-densita-nel-continuo.md)
- [08 - Distribuzioni continue: uniforme ed esponenziale](08-distribuzioni-continue-uniforme-ed-esponenziale.md)
- [09 - Distribuzioni continue: Pareto e Gauss](09-distribuzioni-continue-pareto-e-gauss.md)
- [10 - Valore atteso](10-valore-atteso.md)
- [11 - Varianza](11-varianza.md)
- [12 - Variabili congiunte](12-variabili-congiunte.md)
- [13 - Marginali e covarianza](13-marginali-e-covarianza.md)
- [14 - Distribuzione di Poisson](14-distribuzione-di-poisson.md)
- [15 - Grandi numeri e limite centrale](15-grandi-numeri-e-limite-centrale.md)
- [16 - Verosimiglianza](16-verosimiglianza.md)
- [17 - Verosimiglianza: il calcolo per esteso](17-verosimiglianza-il-calcolo-per-esteso.md)
- [18 - Verosimiglianza nel continuo](18-verosimiglianza-nel-continuo.md)
- [19 - Bayes: derivazione e linguaggio](19-bayes-derivazione-e-linguaggio.md)
- [20 - Intervalli e livelli di confidenza](20-intervalli-e-livelli-di-confidenza.md)
- [21 - Test di ipotesi: le basi](21-test-di-ipotesi-le-basi.md)
- [22 - Valori critici e intervallo per la media](22-valori-critici-e-intervallo-per-la-media.md)
- [23 - Intervallo di confidenza per una percentuale](23-intervallo-di-confidenza-per-una-percentuale.md)
- [24 - Setup di un test di ipotesi](24-setup-di-un-test-di-ipotesi.md)
- [25 - Il p-value e i due tipi di errore](25-il-p-value-e-i-due-tipi-di-errore.md)
- [26 - Valore critico e regione di rifiuto: l'autovelox](26-valore-critico-e-regione-di-rifiuto-l-autovelox.md)
---
## Quale lezione sta in quale modulo
<table fit-page-width="true" header-row="true">
<tr>
<td>Lezione</td>
<td>Moduli</td>
<td>Argomento</td>
</tr>
<tr>
<td>1</td>
<td>01–04</td>
<td>assiomi, condizionata, variabili casuali, PMF e cumulativa</td>
</tr>
<tr>
<td>2</td>
<td>05–09</td>
<td>distribuzioni notevoli, passaggio al continuo, Gauss</td>
</tr>
<tr>
<td>3</td>
<td>10–12</td>
<td>valore atteso, varianza, variabili congiunte</td>
</tr>
<tr>
<td>4</td>
<td>13–16</td>
<td>marginali e covarianza, Poisson, grandi numeri e TLC, verosimiglianza</td>
</tr>
<tr>
<td>5</td>
<td>17–18</td>
<td>il calcolo completo della verosimiglianza, il caso continuo</td>
</tr>
<tr>
<td>6</td>
<td>19–21</td>
<td>Bayes, intervalli di confidenza, test di ipotesi</td>
</tr>
<tr>
<td>7 e 8</td>
<td>confluite nel 19</td>
<td>ridimostrano Bayes; aggiunte la giustificazione di 1/P(H) e la ricetta in 4 passi</td>
</tr>
<tr>
<td>9</td>
<td>22</td>
<td>valori critici, intervallo per la media, il numero 1,96</td>
</tr>
<tr>
<td>10</td>
<td>23</td>
<td>intervallo per una percentuale, exit poll</td>
</tr>
<tr>
<td>11</td>
<td>24</td>
<td>setup di un test, l'esempio dei numeri di serie</td>
</tr>
<tr>
<td>12</td>
<td>25</td>
<td>p-value e i due tipi di errore</td>
</tr>
<tr>
<td>13 e 14</td>
<td>26</td>
<td>valore critico e regione di rifiuto, l'autovelox</td>
</tr>
</table>
---
## Riferimenti
- [Dekking et al. — A Modern Introduction to Probability and Statistics (PDF ufficiale)](https://link.springer.com/book/10.1007/1-84628-168-7)
- [G. D'Agostini — pagina personale, Roma La Sapienza](https://www.roma1.infn.it/~dagos/)
- [01 - Probabilità: linguaggio e assiomi](01-probabilita-linguaggio-e-assiomi.md)
- [02 - Probabilità condizionata](02-probabilita-condizionata.md)
- [03 - Variabili casuali e statistiche](03-variabili-casuali-e-statistiche.md)
- [04 - Funzione di probabilità e cumulativa](04-funzione-di-probabilita-e-cumulativa.md)
- [05 - Distribuzioni notevoli](05-distribuzioni-notevoli.md)
- [06 - Dal discreto al continuo](06-dal-discreto-al-continuo.md)
- [07 - Cumulativa e densità nel continuo](07-cumulativa-e-densita-nel-continuo.md)
- [08 - Distribuzioni continue: uniforme ed esponenziale](08-distribuzioni-continue-uniforme-ed-esponenziale.md)
- [09 - Distribuzioni continue: Pareto e Gauss](09-distribuzioni-continue-pareto-e-gauss.md)
- [10 - Valore atteso](10-valore-atteso.md)
- [11 - Varianza](11-varianza.md)
- [12 - Variabili congiunte](12-variabili-congiunte.md)
- [13 - Marginali e covarianza](13-marginali-e-covarianza.md)
- [14 - Distribuzione di Poisson](14-distribuzione-di-poisson.md)
- [15 - Grandi numeri e limite centrale](15-grandi-numeri-e-limite-centrale.md)
- [16 - Verosimiglianza](16-verosimiglianza.md)
- [17 - Verosimiglianza: il calcolo per esteso](17-verosimiglianza-il-calcolo-per-esteso.md)
- [18 - Verosimiglianza nel continuo](18-verosimiglianza-nel-continuo.md)
- [19 - Bayes: derivazione e linguaggio](19-bayes-derivazione-e-linguaggio.md)
- [20 - Intervalli e livelli di confidenza](20-intervalli-e-livelli-di-confidenza.md)
- [21 - Test di ipotesi: le basi](21-test-di-ipotesi-le-basi.md)
- [22 - Valori critici e intervallo per la media](22-valori-critici-e-intervallo-per-la-media.md)
- [23 - Intervallo di confidenza per una percentuale](23-intervallo-di-confidenza-per-una-percentuale.md)
- [24 - Setup di un test di ipotesi](24-setup-di-un-test-di-ipotesi.md)
- [25 - Il p-value e i due tipi di errore](25-il-p-value-e-i-due-tipi-di-errore.md)
- [26 - Valore critico e regione di rifiuto: l'autovelox](26-valore-critico-e-regione-di-rifiuto-l-autovelox.md)
- [Bignami - i 10 concetti da sapere](bignami-i-10-concetti-da-sapere.md)
