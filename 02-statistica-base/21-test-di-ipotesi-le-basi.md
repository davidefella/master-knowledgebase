# 21 - Test di ipotesi: le basi

> Fonte Notion: https://app.notion.com/p/3c712abc808d81539383e8a7a378c5e1 — ultima modifica 2026-08-25T21:11:07.999Z

<table_of_contents color="gray"/>
Il passo finale: trasformare i dati in una **decisione**.
<callout icon="💬" color="green_bg">
	**In parole semplici**
	Come un processo in tribunale. L'imputato è innocente fino a prova contraria: quella è l'ipotesi di partenza.
	Si condanna solo se le prove sono così poco compatibili con l'innocenza da rendere assurdo continuare a crederci. Se le prove sono deboli non si dichiara "innocente": si dice che non ci sono elementi sufficienti.
</callout>
---
## Le due ipotesi
<table fit-page-width="true" header-row="true">
<tr>
<td>Simbolo</td>
<td>Nome</td>
<td>Che cos'è</td>
</tr>
<tr>
<td>$`H_0`$</td>
<td>**ipotesi nulla** (null hypothesis)</td>
<td>l'ipotesi sotto studio, quella che si mette alla prova</td>
</tr>
<tr>
<td>$`H_1`$</td>
<td>ipotesi alternativa</td>
<td>l'ipotesi contraria: parole del docente, “**tutto il resto**”</td>
</tr>
</table>
---
## I due errori possibili
La decisione può essere sbagliata in due modi diversi, e non sono la stessa cosa.
<table fit-page-width="true" header-row="true">
<tr>
<td></td>
<td>$`H_0`$ è vera</td>
<td>$`H_1`$ è vera</td>
</tr>
<tr>
<td>**Rifiuto **$`H_0`$</td>
<td>**errore di I tipo**</td>
<td>ok</td>
</tr>
<tr>
<td>**Non rifiuto **$`H_0`$</td>
<td>ok</td>
<td>**errore di II tipo**</td>
</tr>
</table>
<table fit-page-width="true" header-row="true">
<tr>
<td>Errore</td>
<td>In tribunale</td>
<td>In medicina</td>
</tr>
<tr>
<td>**I tipo** — rifiuto $`H_0`$ vera</td>
<td>condanno un innocente</td>
<td>allarme su un paziente sano</td>
</tr>
<tr>
<td>**II tipo** — non rifiuto $`H_0`$ falsa</td>
<td>assolvo un colpevole</td>
<td>malattia non individuata</td>
</tr>
</table>
---
## Il livello di significatività
Il docente chiama $`H_0`$ il **working point**: è il punto da cui si ragiona, quello che si assume vero finché i dati non dicono il contrario.
Si sceglie in anticipo un $`\alpha`$ — il **livello di significatività** — e si costruisce il test in modo che, assunta vera $`H_0`$:
$$
P(\text{errore di I tipo}) \le \alpha
$$
Il valore convenzionale è:
$$
\alpha = 0{,}05 \qquad\text{cioè}\qquad 5\%
$$
<callout icon="⚠️" color="yellow_bg">
	**Si controlla un errore solo.** $`\alpha`$ tiene sotto controllo l'errore di I tipo, non l'altro. È una scelta deliberata: si decide che condannare un innocente sia lo sbaglio da evitare per primo.
	E il prezzo si paga: abbassando $`\alpha`$ si diventa più prudenti nel rifiutare $`H_0`$, quindi l'errore di II tipo cresce.
</callout>
<callout icon="🎯" color="blue_bg">
	Per questo si dice "**non rifiuto** $`H_0`$" e non "accetto $`H_0`$": non rifiutare vuol dire che i dati non bastano a smentirla, non che sia vera.
</callout>
---
## Il legame con la confidenza
È lo stesso $`\alpha`$ del modulo 20:
$$
\gamma = 1 - \alpha
$$
Un livello di confidenza del 95% e un test al 5% sono lo stesso conto guardato da due lati.
---
## Riferimenti
- Dekking et al., *A Modern Introduction to Probability and Statistics*, cap. 25–26
